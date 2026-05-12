import streamlit as st
import databento as db
import pandas as pd
import numpy as np
from datetime import datetime, timedelta, timezone
import time
import plotly.graph_objects as go
from plotly.subplots import make_subplots

st.set_page_config(
page_title="MNQ Live Chart",
page_icon="",
layout=“wide",
initial_sidebar_state="collapsed"
)

hide_style = """

<style>
body{background:#030303;color:#e0e0e0;font-family:monospace}
.stApp{background:#030303}
div[data-testid="stToolbar"]{display:none}
div[data-testid="stDecoration"]{display:none}
div[data-testid="stStatusWidget"]{display:none}
#MainMenu{visibility:hidden}
footer{visibility:hidden}
header{visibility:hidden}
.stButton>button{background:#00ff9f11;border:1px solid #00ff9f33;color:#00ff9f;font-family:monospace;font-weight:700;width:100%}
</style>

“””
st.markdown(hide_style, unsafe_allow_html=True)

st.markdown(”## MNQ LIVE CHART”)

def calc_ema(series, period):
return series.ewm(span=period, adjust=False).mean()

def calc_vwap(df):
tp = (df[“high”] + df[“low”] + df[“close”]) / 3
return (tp * df[“volume”]).cumsum() / df[“volume”].cumsum()

def detect_fvgs(df, lookback=50):
fvgs = []
data = df.tail(lookback).reset_index(drop=True)
for i in range(2, len(data)):
prev = data.iloc[i-2]
curr = data.iloc[i]
if curr[“low”] > prev[“high”]:
fvgs.append({“type”: “bull”, “top”: curr[“low”], “bot”: prev[“high”]})
if curr[“high”] < prev[“low”]:
fvgs.append({“type”: “bear”, “top”: prev[“low”], “bot”: curr[“high”]})
return fvgs[-10:]

TF_MAP = {
“1m”:  (“ohlcv-1m”,  60,   1),
“2m”:  (“ohlcv-1m”,  60,   2),
“5m”:  (“ohlcv-1m”,  60,   5),
“15m”: (“ohlcv-1m”,  60,   15),
“30m”: (“ohlcv-1m”,  60,   30),
“1H”:  (“ohlcv-1h”,  3600, 1),
“4H”:  (“ohlcv-1h”,  3600, 4),
“D”:   (“ohlcv-1d”,  86400,1),
}

@st.cache_data(ttl=10, show_spinner=False)
def fetch_candles(api_key, tf, n_bars=200):
schema, base_sec, agg = TF_MAP.get(tf, (“ohlcv-1m”, 60, 1))
try:
client = db.Historical(api_key)
end   = datetime.now(timezone.utc) - timedelta(seconds=30)
start = end - timedelta(seconds=base_sec * agg * n_bars)
data  = client.timeseries.get_range(
dataset=“GLBX.MDP3”,
symbols=“MNQ.c.0”,
schema=schema,
start=start,
end=end,
limit=n_bars * agg + 50,
)
df = data.to_df()
if df.empty:
return None, “No data returned”
df = df[[“open”,“high”,“low”,“close”,“volume”]].copy()
df.index = pd.to_datetime(df.index)
if df[“close”].mean() > 1e6:
for col in [“open”,“high”,“low”,“close”]:
df[col] = df[col] / 1e9
if agg > 1:
df = df.resample(str(base_sec * agg) + “s”).agg({
“open”:“first”,“high”:“max”,“low”:“min”,
“close”:“last”,“volume”:“sum”
}).dropna()
return df.tail(n_bars), None
except Exception as e:
return None, str(e)

with st.sidebar:
st.markdown(”### API KEY”)
api_key = st.text_input(“Databento API Key”, placeholder=“db-xxx”, type=“password”)
st.markdown(”—”)
tf = st.selectbox(“Timeframe”, list(TF_MAP.keys()), index=2)
st.markdown(”—”)
st.markdown(”### INDICATORS”)
show_ema9   = st.checkbox(“EMA 9”,     value=True)
show_ema21  = st.checkbox(“EMA 21”,    value=True)
show_ema50  = st.checkbox(“EMA 50”,    value=False)
show_ema200 = st.checkbox(“EMA 200”,   value=False)
show_vwap   = st.checkbox(“VWAP”,      value=True)
show_fvg    = st.checkbox(“FVG Zones”, value=True)
st.markdown(”—”)
st.markdown(”### ORB LEVELS”)
orb_high = st.text_input(“ORB High”, placeholder=“e.g. 29420”)
orb_low  = st.text_input(“ORB Low”,  placeholder=“e.g. 29180”)
auto_ref = st.checkbox(“Auto-refresh 5s”, value=True)
st.markdown(”—”)
st.markdown(”[Back to WarRoom](https://mnqlee.github.io/MNQ-Warroom-Claude-)”)

if not api_key:
st.info(“Enter your Databento API key in the sidebar to load live MNQ candles.”)
st.markdown(”””
**Setup:**

1. Go to databento.com and log in
1. Click your name top right -> API Keys
1. Create new key -> copy it
1. Paste in the sidebar

**Free $125 credits included on signup - enough for ~4 months of data**
“””)
else:
with st.spinner(“Loading MNQ data…”):
df, err = fetch_candles(api_key, tf)

```
if err:
    st.error("Error: " + err)
elif df is not None and not df.empty:
    last = df.iloc[-1]
    prev = df.iloc[-2] if len(df) > 1 else last
    price_chg = last["close"] - prev["close"]
    price_pct = (price_chg / prev["close"]) * 100
    vwap_val  = calc_vwap(df).iloc[-1]
    ema9_val  = calc_ema(df["close"], 9).iloc[-1]
    ema21_val = calc_ema(df["close"], 21).iloc[-1]

    col1, col2, col3, col4, col5 = st.columns(5)
    col1.metric("MNQ LAST", f"{last['close']:,.2f}", f"{price_pct:+.2f}%")
    col2.metric("HIGH",     f"{df['high'].max():,.2f}")
    col3.metric("LOW",      f"{df['low'].min():,.2f}")
    col4.metric("VWAP",     f"{vwap_val:,.2f}", "ABOVE" if last["close"] > vwap_val else "BELOW")
    col5.metric("EMA 9/21", "BULL" if ema9_val > ema21_val else "BEAR")

    fig = make_subplots(rows=2, cols=1, shared_xaxes=True,
                        vertical_spacing=0.02, row_heights=[0.8, 0.2])

    fig.add_trace(go.Candlestick(
        x=df.index, open=df["open"], high=df["high"],
        low=df["low"], close=df["close"],
        increasing_line_color="#00ff9f", decreasing_line_color="#ff3d57",
        increasing_fillcolor="#00ff9f", decreasing_fillcolor="#ff3d57",
        name="MNQ", line_width=1
    ), row=1, col=1)

    colors = ["#00ff9f44" if c >= o else "#ff3d5744"
              for c, o in zip(df["close"], df["open"])]
    fig.add_trace(go.Bar(
        x=df.index, y=df["volume"], marker_color=colors,
        name="Volume", showlegend=False
    ), row=2, col=1)

    if show_ema9:
        fig.add_trace(go.Scatter(x=df.index, y=calc_ema(df["close"], 9),
            line=dict(color="#fbbf24", width=1), name="EMA 9"), row=1, col=1)
    if show_ema21:
        fig.add_trace(go.Scatter(x=df.index, y=calc_ema(df["close"], 21),
            line=dict(color="#7ec8e3", width=1), name="EMA 21"), row=1, col=1)
    if show_ema50:
        fig.add_trace(go.Scatter(x=df.index, y=calc_ema(df["close"], 50),
            line=dict(color="#a78bfa", width=1), name="EMA 50"), row=1, col=1)
    if show_ema200:
        fig.add_trace(go.Scatter(x=df.index, y=calc_ema(df["close"], 200),
            line=dict(color="#ff6b35", width=1), name="EMA 200"), row=1, col=1)
    if show_vwap:
        fig.add_trace(go.Scatter(x=df.index, y=calc_vwap(df),
            line=dict(color="#ff3d57", width=1, dash="dot"), name="VWAP"), row=1, col=1)

    if orb_high and orb_low:
        try:
            oh, ol = float(orb_high), float(orb_low)
            fig.add_hrect(y0=ol, y1=oh, fillcolor="rgba(251,191,36,0.06)",
                          line_width=0, row=1, col=1)
            fig.add_hline(y=oh, line_color="#fbbf2488", line_dash="dash",
                          line_width=1, row=1, col=1,
                          annotation_text="ORB H " + str(oh))
            fig.add_hline(y=ol, line_color="#fbbf2488", line_dash="dash",
                          line_width=1, row=1, col=1,
                          annotation_text="ORB L " + str(ol))
        except Exception:
            pass

    if show_fvg:
        for f in detect_fvgs(df):
            color = "rgba(0,255,159,0.07)" if f["type"] == "bull" else "rgba(255,61,87,0.07)"
            fig.add_hrect(y0=f["bot"], y1=f["top"], fillcolor=color,
                          line_width=0, row=1, col=1)

    fig.update_layout(
        paper_bgcolor="#030303", plot_bgcolor="#070707",
        font=dict(family="monospace", color="#e0e0e0", size=10),
        xaxis_rangeslider_visible=False,
        margin=dict(l=0, r=60, t=10, b=0),
        height=520,
    )
    fig.update_xaxes(gridcolor="#111", showgrid=True, zeroline=False)
    fig.update_yaxes(gridcolor="#111", showgrid=True, zeroline=False, side="right")
    st.plotly_chart(fig, use_container_width=True, config={"displayModeBar": False})

    ts = df.index[-1].strftime("%H:%M:%S UTC")
    st.caption("Last bar: " + ts + " | Auto-refreshing | NOT FINANCIAL ADVICE | USE STOPS")

    if auto_ref:
        time.sleep(5)
        st.rerun()
else:
    st.warning("No data. Market may be closed or outside trading hours.")
```
