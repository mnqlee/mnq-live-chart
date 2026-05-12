import streamlit as st
import databento as db
import pandas as pd
from datetime import datetime, timedelta, timezone
import time
import plotly.graph_objects as go
from plotly.subplots import make_subplots

t = chr(77)+chr(78)+chr(81)+chr(32)+chr(76)+chr(105)+chr(118)+chr(101)+chr(32)+chr(67)+chr(104)+chr(97)+chr(114)+chr(116)
w = chr(119)+chr(105)+chr(100)+chr(101)
st.set_page_config(page_title=t, layout=w)

css = chr(60)+chr(115)+chr(116)+chr(121)+chr(108)+chr(101)+chr(62)+chr(98)+chr(111)+chr(100)+chr(121)+chr(123)+chr(98)+chr(97)+chr(99)+chr(107)+chr(103)+chr(114)+chr(111)+chr(117)+chr(110)+chr(100)+chr(58)+chr(35)+chr(48)+chr(51)+chr(48)+chr(51)+chr(48)+chr(51)+chr(125)+chr(60)+chr(47)+chr(115)+chr(116)+chr(121)+chr(108)+chr(101)+chr(62)
st.markdown(css, unsafe_allow_html=True)

def calc_ema(s, p):
return s.ewm(span=p, adjust=False).mean()

def calc_vwap(df):
tp = (df[‘high’] + df[‘low’] + df[‘close’]) / 3
return (tp * df[‘volume’]).cumsum() / df[‘volume’].cumsum()

def detect_fvgs(df):
fvgs = []
d = df.tail(50).reset_index(drop=True)
for i in range(2, len(d)):
if d.iloc[i][‘low’] > d.iloc[i-2][‘high’]:
fvgs.append({‘type’:‘bull’,‘top’:d.iloc[i][‘low’],‘bot’:d.iloc[i-2][‘high’]})
if d.iloc[i][‘high’] < d.iloc[i-2][‘low’]:
fvgs.append({‘type’:‘bear’,‘top’:d.iloc[i-2][‘low’],‘bot’:d.iloc[i][‘high’]})
return fvgs[-10:]

TF = {
‘1m’: (‘ohlcv-1m’, 60, 1),
‘2m’: (‘ohlcv-1m’, 60, 2),
‘5m’: (‘ohlcv-1m’, 60, 5),
‘15m’:(‘ohlcv-1m’, 60, 15),
‘30m’:(‘ohlcv-1m’, 60, 30),
‘1H’: (‘ohlcv-1h’, 3600, 1),
‘4H’: (‘ohlcv-1h’, 3600, 4),
‘D’:  (‘ohlcv-1d’, 86400, 1),
}

@st.cache_data(ttl=10, show_spinner=False)
def fetch(api_key, tf, n=200):
schema, base, agg = TF.get(tf, (‘ohlcv-1m’, 60, 1))
try:
client = db.Historical(api_key)
end = datetime.now(timezone.utc) - timedelta(seconds=30)
start = end - timedelta(seconds=base * agg * n)
data = client.timeseries.get_range(
dataset=‘GLBX.MDP3’, symbols=‘MNQ.c.0’,
schema=schema, start=start, end=end, limit=n*agg+50)
df = data.to_df()
if df.empty:
return None, ‘No data’
df = df[[‘open’,‘high’,‘low’,‘close’,‘volume’]].copy()
if df[‘close’].mean() > 1e6:
for c in [‘open’,‘high’,‘low’,‘close’]:
df[c] = df[c] / 1e9
if agg > 1:
df = df.resample(str(base*agg)+‘s’).agg(
{‘open’:‘first’,‘high’:‘max’,‘low’:‘min’,‘close’:‘last’,‘volume’:‘sum’}).dropna()
return df.tail(n), None
except Exception as e:
return None, str(e)

with st.sidebar:
st.markdown(’### DATABENTO API KEY’)
api_key = st.text_input(’’, placeholder=‘db-xxx’, type=‘password’)
tf = st.selectbox(‘Timeframe’, list(TF.keys()), index=2)
st.markdown(’—’)
e9  = st.checkbox(‘EMA 9’,     value=True)
e21 = st.checkbox(‘EMA 21’,    value=True)
e50 = st.checkbox(‘EMA 50’,    value=False)
e200= st.checkbox(‘EMA 200’,   value=False)
vwap= st.checkbox(‘VWAP’,      value=True)
fvg = st.checkbox(‘FVG Zones’, value=True)
st.markdown(’—’)
orb_hi = st.text_input(‘ORB High’, placeholder=‘29420’)
orb_lo = st.text_input(‘ORB Low’,  placeholder=‘29180’)
auto   = st.checkbox(‘Auto-refresh 5s’, value=True)
st.markdown(’[Back to WarRoom](https://mnqlee.github.io/MNQ-Warroom-Claude-)’)

if not api_key:
st.info(‘Enter Databento API key in sidebar. Get one free at databento.com’)
else:
df, err = fetch(api_key, tf)
if err:
st.error(’Error: ’ + err)
elif df is not None and not df.empty:
last = df.iloc[-1]
prev = df.iloc[-2] if len(df) > 1 else last
chg  = last[‘close’] - prev[‘close’]
pct  = chg / prev[‘close’] * 100
vw   = calc_vwap(df).iloc[-1]
e9v  = calc_ema(df[‘close’], 9).iloc[-1]
e21v = calc_ema(df[‘close’], 21).iloc[-1]

```
    c1,c2,c3,c4,c5 = st.columns(5)
    c1.metric('MNQ', str(round(last['close'],2)), str(round(pct,2))+'%')
    c2.metric('HIGH', str(round(df['high'].max(),2)))
    c3.metric('LOW',  str(round(df['low'].min(),2)))
    c4.metric('VWAP', str(round(vw,2)), 'ABOVE' if last['close']>vw else 'BELOW')
    c5.metric('EMA',  'BULL' if e9v>e21v else 'BEAR')

    fig = make_subplots(rows=2, cols=1, shared_xaxes=True,
                        vertical_spacing=0.02, row_heights=[0.8,0.2])
    fig.add_trace(go.Candlestick(
        x=df.index, open=df['open'], high=df['high'],
        low=df['low'], close=df['close'],
        increasing_line_color='#00ff9f', decreasing_line_color='#ff3d57',
        increasing_fillcolor='#00ff9f', decreasing_fillcolor='#ff3d57',
        name='MNQ', line_width=1), row=1, col=1)
    colors = ['#00ff9f44' if c>=o else '#ff3d5744'
              for c,o in zip(df['close'],df['open'])]
    fig.add_trace(go.Bar(x=df.index,y=df['volume'],
        marker_color=colors,name='Vol',showlegend=False),row=2,col=1)
    if e9:  fig.add_trace(go.Scatter(x=df.index,y=calc_ema(df['close'],9),
        line=dict(color='#fbbf24',width=1),name='EMA9'),row=1,col=1)
    if e21: fig.add_trace(go.Scatter(x=df.index,y=calc_ema(df['close'],21),
        line=dict(color='#7ec8e3',width=1),name='EMA21'),row=1,col=1)
    if e50: fig.add_trace(go.Scatter(x=df.index,y=calc_ema(df['close'],50),
        line=dict(color='#a78bfa',width=1),name='EMA50'),row=1,col=1)
    if e200:fig.add_trace(go.Scatter(x=df.index,y=calc_ema(df['close'],200),
        line=dict(color='#ff6b35',width=1),name='EMA200'),row=1,col=1)
    if vwap:fig.add_trace(go.Scatter(x=df.index,y=calc_vwap(df),
        line=dict(color='#ff3d57',width=1,dash='dot'),name='VWAP'),row=1,col=1)
    if orb_hi and orb_lo:
        try:
            oh,ol = float(orb_hi),float(orb_lo)
            fig.add_hrect(y0=ol,y1=oh,fillcolor='rgba(251,191,36,0.06)',
                line_width=0,row=1,col=1)
            fig.add_hline(y=oh,line_color='#fbbf2488',line_dash='dash',
                line_width=1,row=1,col=1)
            fig.add_hline(y=ol,line_color='#fbbf2488',line_dash='dash',
                line_width=1,row=1,col=1)
        except Exception:
            pass
    if fvg:
        for f in detect_fvgs(df):
            col = 'rgba(0,255,159,0.07)' if f['type']==chr(98)+chr(117)+chr(108)+chr(108) else 'rgba(255,61,87,0.07)'
            fig.add_hrect(y0=f['bot'],y1=f['top'],fillcolor=col,line_width=0,row=1,col=1)
    fig.update_layout(
        paper_bgcolor='#030303',plot_bgcolor='#070707',
        font=dict(family='monospace',color='#e0e0e0',size=10),
        xaxis_rangeslider_visible=False,
        margin=dict(l=0,r=60,t=10,b=0),height=520)
    fig.update_xaxes(gridcolor='#111',showgrid=True,zeroline=False)
    fig.update_yaxes(gridcolor='#111',showgrid=True,zeroline=False,side='right')
    st.plotly_chart(fig,use_container_width=True,config={'displayModeBar':False})
    st.caption('Last: '+df.index[-1].strftime('%H:%M:%S UTC')+' | NOT FINANCIAL ADVICE')
    if auto:
        time.sleep(5)
        st.rerun()
else:
    st.warning('No data returned.')
```
