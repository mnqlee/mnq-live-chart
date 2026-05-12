import streamlit as st
import databento as db
import pandas as pd
import numpy as np
from datetime import datetime, timedelta, timezone
import time
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# PAGE CONFIG

_title = “MNQ Live Chart”
_icon = “”
_layout = “wide”
st.set_page_config(
page_title=_title,
page_icon=_icon,
layout=_layout,
initial_sidebar_state=“collapsed”
)

# DARK THEME CSS

st.markdown(”””

<style>
body, .stApp { background-color: #030303; color: #e0e0e0; font-family: monospace; }
.stApp { background-color: #030303; }
div[data-testid="stToolbar"] { display: none; }
div[data-testid="stDecoration"] { display: none; }
div[data-testid="stStatusWidget"] { display: none; }
#MainMenu { visibility: hidden; }
footer { visibility: hidden; }
header { visibility: hidden; }
.stSelectbox > div > div { background-color: #0a0a0a; color: #e0e0e0; border: 1px solid #222; }
.stTextInput > div > div > input { background-color: #0a0a0a; color: #00ff9f; border: 1px solid #00ff9f33; font-family: monospace; }
.stButton > button { background-color: #00ff9f11; border: 1px solid #00ff9f33; color: #00ff9f; font-family: monospace; font-weight: 700; width: 100%; }
.stButton > button:hover { background-color: #00ff9f22; border-color: #00ff9f; }
.metric-card { background: #0a0a0a; border: 1px solid #111; border-radius: 6px; padding: 8px 12px; text-align: center; }
.metric-label { font-size: 10px; color: #555; font-family: monospace; letter-spacing: 1px; }
.metric-value { font-size: 20px; font-weight: 700; font-family: monospace; }
.level-row { display: flex; justify-content: space-between; padding: 3px 0; border-bottom: 1px solid #111; font-family: monospace; font-size: 11px; }
h1, h2, h3 { font-family: monospace; color: #e0e0e0; }
</style>

“””, unsafe_allow_html=True)

# HELPERS

def calc_ema(series, period):
return series.ewm(span=period, adjust=False).mean()

def calc_vwap(df):
tp = (df[‘high’] + df[‘low’] + df[‘close’]) / 3
return (tp * df[‘volume’]).cumsum() / df[‘volume’].cumsum()

def detect_fvgs(df, lookback=50):
fvgs = []
data = df.tail(lookback).reset_index(drop=True)
for i in range(2, len(data)):
prev = data.iloc[i-2]
curr = data.iloc[i]
if curr[‘low’] > prev[‘high’]:
fvgs.append({‘type’: ‘bull’, ‘top’: curr[‘low’], ‘bot’: prev[‘high’], ‘idx’: i, ‘time’: curr.name})
if curr[‘high’] < prev[‘low’]:
fvgs.append({‘type’: ‘bear’, ‘top’: prev[‘low’], ‘bot’: curr[‘high’], ‘idx’: i, ‘time’: curr.name})
return fvgs[-10:]

TF_MAP = {
“1s”:  (“ohlcv-1s”,  1,    1),
“5s”:  (“ohlcv-1s”,  1,    5),
“15s”: (“ohlcv-1s”,  1,    15),
“30s”: (“ohlcv-1s”,  1,    30),
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
df = df[[‘open’,‘high’,‘low’,‘close’,‘volume’]].copy()
df.index = pd.to_datetime(df.index)
# Fix fixed-point prices
if df[‘close’].mean() > 1e6:
for col in [‘open’,‘high’,‘low’,‘close’]:
df[col] = df[col] / 1e9
# Aggregate if needed
if agg > 1:
df = df.resample(f’{base_sec * agg}s’).agg({
‘open’:‘first’,‘high’:‘max’,‘low’:‘min’,
‘close’:‘last’,‘volume’:‘sum’
}).dropna()
return df.tail(n_bars), None
except Exception as e:
return None, str(e)

def build_chart(df, orb_high, orb_low, show_ema9, show_ema21, show_ema50, show_ema200, show_vwap, show_fvg):
fig = make_subplots(rows=2, cols=1, shared_xaxes=True,
vertical_spacing=0.02, row_heights=[0.8, 0.2])

```
# Candlesticks
fig.add_trace(go.Candlestick(
    x=df.index, open=df['open'], high=df['high'],
    low=df['low'], close=df['close'],
    increasing_line_color='#00ff9f', decreasing_line_color='#ff3d57',
    increasing_fillcolor='#00ff9f', decreasing_fillcolor='#ff3d57',
    name='MNQ', line_width=1
), row=1, col=1)

# Volume bars
colors = ['#00ff9f44' if c >= o else '#ff3d5744'
          for c, o in zip(df['close'], df['open'])]
fig.add_trace(go.Bar(
    x=df.index, y=df['volume'], marker_color=colors,
    name='Volume', showlegend=False
), row=2, col=1)

# EMAs
if show_ema9:
    fig.add_trace(go.Scatter(x=df.index, y=calc_ema(df['close'], 9),
        line=dict(color='#fbbf24', width=1), name='EMA 9'), row=1, col=1)
if show_ema21:
    fig.add_trace(go.Scatter(x=df.index, y=calc_ema(df['close'], 21),
        line=dict(color='#7ec8e3', width=1), name='EMA 21'), row=1, col=1)
if show_ema50:
    fig.add_trace(go.Scatter(x=df.index, y=calc_ema(df['close'], 50),
        line=dict(color='#a78bfa', width=1), name='EMA 50'), row=1, col=1)
if show_ema200:
    fig.add_trace(go.Scatter(x=df.index, y=calc_ema(df['close'], 200),
        line=dict(color='#ff6b35', width=1), name='EMA 200'), row=1, col=1)

# VWAP
if show_vwap and 'volume' in df.columns:
    vwap = calc_vwap(df)
    fig.add_trace(go.Scatter(x=df.index, y=vwap,
        line=dict(color='#ff3d57', width=1, dash='dot'), name='VWAP'), row=1, col=1)

# ORB zone
if orb_high and orb_low:
    try:
        oh, ol = float(orb_high), float(orb_low)
        fig.add_hrect(y0=ol, y1=oh, fillcolor='rgba(251,191,36,0.06)',
                     line_width=0, row=1, col=1)
        fig.add_hline(y=oh, line_color='#fbbf2488', line_dash='dash',
                     line_width=1, row=1, col=1,
                     annotation_text=f"ORB H {oh}", annotation_position="right")
        fig.add_hline(y=ol, line_color='#fbbf2488', line_dash='dash',
                     line_width=1, row=1, col=1,
                     annotation_text=f"ORB L {ol}", annotation_position="right")
    except:
        pass

# FVGs
if show_fvg:
    fvgs = detect_fvgs(df)
    for f in fvgs:
        color = 'rgba(0,255,159,0.08)' if f['type']=='bull' else 'rgba(255,61,87,0.08)'
        fig.add_hrect(y0=f['bot'], y1=f['top'], fillcolor=color,
                     line_width=0, row=1, col=1)

fig.update_layout(
    paper_bgcolor='#030303', plot_bgcolor='#070707',
    font=dict(family='monospace', color='#e0e0e0', size=10),
    xaxis_rangeslider_visible=False,
    margin=dict(l=0, r=60, t=20, b=0),
    legend=dict(bgcolor='#0a0a0a', bordercolor='#111', font=dict(size=9)),
    height=500,
)
fig.update_xaxes(gridcolor='#111', showgrid=True, zeroline=False)
fig.update_yaxes(gridcolor='#111', showgrid=True, zeroline=False, side='right')
return fig
```

# MAIN UI

st.markdown(”””

<div style="display:flex;align-items:center;gap:12px;margin-bottom:8px">
  <div>
    <div style="font-size:18px;font-weight:700;letter-spacing:3px;font-family:monospace">
      MNQ <span style="color:#00ff9f">LIVE</span> <span style="color:#ff3d57">CHART</span>
    </div>
    <div style="font-size:9px;color:#333;font-family:monospace">POWERED BY DATABENTO . REAL-TIME CME DATA</div>
  </div>
</div>
""", unsafe_allow_html=True)

# SIDEBAR / API KEY

with st.sidebar:
st.markdown(”### DATABENTO API KEY”)
api_key = st.text_input(””, placeholder=“db-xxxxxxxxxxxxxxxxxxxxxxxx”,
type=“password”, key=“api_key”,
help=“Your key stays in your browser session only”)
st.markdown(”—”)
st.markdown(”### TIMEFRAME”)
tf = st.selectbox(””, list(TF_MAP.keys()), index=6, key=“tf”)
st.markdown(”—”)
st.markdown(”### MOVING AVERAGES”)
show_ema9   = st.checkbox(“EMA 9”,   value=True)
show_ema21  = st.checkbox(“EMA 21”,  value=True)
show_ema50  = st.checkbox(“EMA 50”,  value=False)
show_ema200 = st.checkbox(“EMA 200”, value=False)
show_vwap   = st.checkbox(“VWAP”,    value=True)
show_fvg    = st.checkbox(“FVG Zones”, value=True)
st.markdown(”—”)
st.markdown(”### ORB LEVELS”)
orb_high = st.text_input(“ORB High”, placeholder=“e.g. 29420”, key=“orb_high”)
orb_low  = st.text_input(“ORB Low”,  placeholder=“e.g. 29180”, key=“orb_low”)
auto_refresh = st.checkbox(“Auto-refresh (5s)”, value=True)
st.markdown(”—”)
st.markdown(”””
<div style="font-size:8px;color:#333;font-family:monospace;line-height:1.6">
MNQ WARROOM<br>
<a href="https://mnqlee.github.io/MNQ-Warroom-Claude-" 
style="color:#00ff9f" target="_blank">
Back to WarRoom</a>
</div>
“””, unsafe_allow_html=True)

# MAIN CONTENT

if not api_key:
st.markdown(”””
<div style="background:#0a0a0a;border:1px solid #00ff9f22;border-radius:8px;padding:20px;text-align:center">
<div style="font-size:14px;color:#00ff9f;font-weight:700;margin-bottom:8px;font-family:monospace">
ENTER YOUR DATABENTO API KEY IN THE SIDEBAR
</div>
<div style="font-size:10px;color:#444;font-family:monospace;line-height:1.8">
1. Go to databento.com and log in<br>
2. Click your name top right -> API Keys<br>
3. Create new key -> copy it<br>
4. Paste in the sidebar to the left<br><br>
<span style="color:#fbbf24">$125 free credits included on signup</span>
</div>
</div>
“””, unsafe_allow_html=True)
else:
# Fetch data
with st.spinner(””):
df, err = fetch_candles(api_key, tf)

```
if err:
    st.error(f"Error: {err}")
elif df is not None and not df.empty:
    last = df.iloc[-1]
    prev = df.iloc[-2] if len(df) > 1 else last
    price_chg = last['close'] - prev['close']
    price_pct  = (price_chg / prev['close']) * 100

    # Price metrics row
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.markdown(f"""
        <div class="metric-card" style="border-color:#00ff9f22">
            <div class="metric-label">MNQ LAST</div>
            <div class="metric-value" style="color:#00ff9f">{last['close']:,.2f}</div>
            <div style="font-size:9px;color:{'#00e676' if price_chg>=0 else '#ff3d57'};font-family:monospace">
                {'' if price_chg>=0 else ''}{abs(price_pct):.2f}%
            </div>
        </div>""", unsafe_allow_html=True)
    with col2:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-label">HIGH</div>
            <div class="metric-value" style="color:#00ff9f;font-size:15px">{df['high'].max():,.2f}</div>
        </div>""", unsafe_allow_html=True)
    with col3:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-label">LOW</div>
            <div class="metric-value" style="color:#ff3d57;font-size:15px">{df['low'].min():,.2f}</div>
        </div>""", unsafe_allow_html=True)
    with col4:
        vwap_val = calc_vwap(df).iloc[-1]
        above = last['close'] > vwap_val
        st.markdown(f"""
        <div class="metric-card" style="border-color:#ff3d5722">
            <div class="metric-label">VWAP</div>
            <div class="metric-value" style="color:#ff3d57;font-size:15px">{vwap_val:,.2f}</div>
            <div style="font-size:9px;color:{'#00ff9f' if above else '#ff3d57'};font-family:monospace">
                {'ABOVE' if above else 'BELOW'}
            </div>
        </div>""", unsafe_allow_html=True)
    with col5:
        ema9_val = calc_ema(df['close'], 9).iloc[-1]
        ema21_val = calc_ema(df['close'], 21).iloc[-1]
        bull_ema = ema9_val > ema21_val
        st.markdown(f"""
        <div class="metric-card" style="border-color:#fbbf2422">
            <div class="metric-label">EMA 9/21</div>
            <div class="metric-value" style="color:#fbbf24;font-size:13px">
                {'BULL' if bull_ema else 'BEAR'}
            </div>
            <div style="font-size:8px;color:#555;font-family:monospace">
                {ema9_val:,.0f} / {ema21_val:,.0f}
            </div>
        </div>""", unsafe_allow_html=True)

    st.markdown("<div style='margin-top:8px'></div>", unsafe_allow_html=True)

    # Chart
    fig = build_chart(df, orb_high, orb_low,
                     show_ema9, show_ema21, show_ema50, show_ema200,
                     show_vwap, show_fvg)
    st.plotly_chart(fig, use_container_width=True, config={'displayModeBar': False})

    # Entry assessment
    price = last['close']
    signals = []
    score = 0
    direction = None

    if orb_high and orb_low:
        try:
            oh, ol = float(orb_high), float(orb_low)
            if price > oh:
                direction = "LONG"; score += 25
                signals.append(("ORB BREAKOUT", "#00ff9f"))
            elif price < ol:
                direction = "SHORT"; score += 25
                signals.append(("ORB BREAKDOWN", "#ff3d57"))
            elif abs(price - oh) / oh < 0.002:
                direction = "LONG"; score += 15
                signals.append(("ORB HIGH RETEST", "#fbbf24"))
            elif abs(price - ol) / ol < 0.002:
                direction = "SHORT"; score += 15
                signals.append(("ORB LOW RETEST", "#fbbf24"))
        except:
            pass

    if direction == "LONG" and price > vwap_val:
        score += 20; signals.append(("ABOVE VWAP", "#00ff9f"))
    elif direction == "SHORT" and price < vwap_val:
        score += 20; signals.append(("BELOW VWAP", "#ff3d57"))
    elif direction:
        score -= 10; signals.append(("AGAINST VWAP", "#ff3d57"))

    if direction == "LONG" and bull_ema:
        score += 20; signals.append(("EMA BULLISH", "#00ff9f"))
    elif direction == "SHORT" and not bull_ema:
        score += 20; signals.append(("EMA BEARISH", "#ff3d57"))

    if score > 0:
        verdict = "STRONG " + (direction or "") if score >= 60 else "POSSIBLE " + (direction or "")
        vcolor = "#00ff9f" if direction=="LONG" else "#ff3d57"
        st.markdown(f"""
        <div style="background:{vcolor}0d;border:1px solid {vcolor}33;border-radius:6px;padding:8px 12px;margin-top:4px">
            <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:4px">
                <span style="font-size:13px;color:{vcolor};font-weight:700;font-family:monospace">{verdict}</span>
                <span style="font-size:9px;color:#444;font-family:monospace">score: {min(score,100)}/100</span>
            </div>
            <div style="height:4px;background:#111;border-radius:2px;overflow:hidden;margin-bottom:6px">
                <div style="height:100%;width:{min(score,100)}%;background:{vcolor}"></div>
            </div>
            <div style="display:flex;flex-wrap:wrap;gap:4px">
                {''.join([f"<span style='font-size:8px;color:{s[1]};background:{s[1]}11;border:1px solid {s[1]}33;border-radius:2px;padding:1px 5px;font-family:monospace'>{s[0]}</span>" for s in signals])}
            </div>
        </div>
        """, unsafe_allow_html=True)

    # Last updated
    st.markdown(f"""
    <div style="font-size:7px;color:#222;font-family:monospace;text-align:right;margin-top:4px">
        Last bar: {df.index[-1].strftime('%H:%M:%S UTC')} . 
        Refreshing every 5s . NOT FINANCIAL ADVICE . USE STOPS
    </div>
    """, unsafe_allow_html=True)

    # Auto refresh
    if auto_refresh:
        time.sleep(5)
        st.rerun()
else:
    st.warning("No data returned. Market may be outside trading hours or API key issue.")
```
