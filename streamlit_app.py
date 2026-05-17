<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0"/>
<title>MNQ WarRoom v9</title>
<style>
*{box-sizing:border-box;margin:0;padding:0}
body{background:#030303;color:#e0e0e0;font-family:monospace;min-height:100vh;display:flex;flex-direction:column}
::-webkit-scrollbar{width:3px}::-webkit-scrollbar-thumb{background:#1a1a1a}
input,button{font-family:monospace;outline:none}
button:active{opacity:.6}
.hdr{border-bottom:1px solid #0d0d0d;padding:4px 10px;flex-shrink:0}
.hdr-r1{margin-bottom:3px}
.hdr-title{font-size:16px;letter-spacing:2px;font-weight:700;line-height:1}
.hdr-sub{font-size:7px;color:#1a1a1a;margin-top:1px}
.hdr-r2{display:flex;align-items:center;gap:6px;margin-bottom:4px;overflow-x:auto}
.clock-blk{flex-shrink:0}
.clock-sess{font-size:7px;font-weight:700;letter-spacing:1px}
.clock-time{font-size:15px;color:#00ff9f;font-weight:700;line-height:1.1}
.clock-date{font-size:7px;color:#444}
.price-box{background:#00ff9f0a;border:1px solid #00ff9f22;border-radius:6px;padding:3px 8px;text-align:center;flex-shrink:0}
.price-lbl{font-size:7px;color:#00ff9f;letter-spacing:1px}
.price-val{font-size:17px;color:#00ff9f;font-weight:700;line-height:1}
.price-chg{font-size:9px;font-weight:700}
.price-age{font-size:7px}
.vix-box{background:#0a0a0a;border:1px solid #111;border-radius:5px;padding:3px 8px;text-align:center;flex-shrink:0}
.vix-lbl{font-size:7px;color:#555}
.vix-val{font-size:14px;font-weight:700}
.vix-chg{font-size:7px}
.oil-box{border-radius:5px;padding:5px 10px;text-align:center;flex-shrink:0;background:#0a0a0a}
.refresh-btn{background:#fbbf2411;border:1px solid #fbbf2433;color:#fbbf24;padding:4px 16px;border-radius:5px;cursor:pointer;font-size:9px;font-weight:700;letter-spacing:1px;white-space:nowrap;width:100%}
.stale-bar{background:#ff3d5711;border-bottom:1px solid #ff3d5533;padding:3px 12px;font-size:7.5px;color:#ff3d57;flex-shrink:0;display:none}
.disclaimer{background:#080800;border-bottom:1px solid #fbbf2411;padding:2px 12px;font-size:7.5px;color:#fbbf2455;flex-shrink:0}
.mag7-strip{border-bottom:1px solid #0a0a0a;padding:2px 10px;background:#050505;flex-shrink:0}
.mag7-inner{display:flex;align-items:center;gap:6px}
.mag7-lbl{font-size:7px;color:#1a1a1a;letter-spacing:2px;flex-shrink:0}
.mag7-cards{flex:1;display:flex;gap:3px;overflow-x:auto}
.mag7-card{background:#0a0a0a;border:1px solid #111;border-radius:3px;padding:2px 6px;flex-shrink:0}
.mag7-sym{font-size:8px;font-weight:700}
.mag7-price{font-size:9px;color:#ddd;font-weight:700}
.mag7-pct{font-size:8px}
.wtd-blk{flex-shrink:0;text-align:center}
.wtd-lbl{font-size:7px;color:#333}
.wtd-val{font-size:11px;font-weight:700}
.tabs{display:flex;border-bottom:1px solid #0a0a0a;flex-shrink:0;overflow-x:auto}
.tab-btn{background:transparent;border:none;border-bottom:2px solid transparent;color:#555;padding:7px 12px;cursor:pointer;font-size:8px;letter-spacing:1px;font-weight:600;white-space:nowrap;font-family:monospace}
.tab-btn.active{border-bottom:2px solid var(--tc);color:var(--tc);background:var(--tbg)}
.content{flex:1;overflow-y:auto;padding:12px}
.card{background:#070707;border:1px solid #111;border-radius:8px;padding:12px;margin-bottom:8px}
.card-sm{background:#0a0a0a;border:1px solid #111;border-radius:5px;padding:7px 10px;margin-bottom:8px}
.lbl{font-size:7px;color:#333;letter-spacing:1px;margin-bottom:4px}
.lbl-yellow{color:#fbbf24}
.lbl-green{color:#00ff9f}
.lbl-red{color:#ff3d57}
.lbl-purple{color:#a78bfa}
.lbl-teal{color:#00d4aa}
.lbl-blue{color:#1d9bf0}
.row{display:flex;justify-content:space-between;align-items:center}
.grid2{display:grid;grid-template-columns:1fr 1fr;gap:6px}
.grid3{display:grid;grid-template-columns:1fr 1fr 1fr;gap:4px}
.stat-box{background:#080808;border:1px solid #0d0d0d;border-radius:4px;padding:5px 7px}
.stat-lbl{font-size:7px;color:#333}
.stat-val{font-size:12px;font-weight:700}
.bar-wrap{height:3px;background:#0d0d0d;border-radius:2px;overflow:hidden;margin-bottom:1px}
.bar-fill{height:100%;background:linear-gradient(90deg,#ff3d57,#fbbf24,#00ff9f);background-size:200%;transition:width .5s}
.gauge-wrap{min-width:212px;flex:0 0 212px}
.footer{border-top:1px solid #080808;padding:3px 12px;display:flex;justify-content:space-between;flex-shrink:0}
.footer span{font-size:7px;color:#111}
.news-src{background:#080808;border:1px solid #111;border-radius:5px;padding:8px 10px;margin-bottom:6px}
.news-hl{font-size:11px;color:#ddd;line-height:1.4;border-left:2px solid #333;padding-left:8px;margin-bottom:4px}
.news-sum{font-size:9px;color:#555;line-height:1.4;padding-left:10px}
.check-item{background:#0a0a0a;border:1px solid #0d0d0d;border-radius:4px;padding:7px 9px;margin-bottom:4px}
.check-q{font-size:9px;color:#aaa;margin-bottom:5px;line-height:1.3}
.check-btns{display:flex;gap:6px}
.check-btn{flex:1;padding:4px 0;border-radius:3px;cursor:pointer;font-size:8px;font-family:monospace;border:1px solid #1a1a1a;background:transparent;color:#333}
.check-btn.yes{background:#00ff9f22;border-color:#00ff9f55;color:#00ff9f}
.check-btn.no{background:#ff3d5722;border-color:#ff3d5755;color:#ff3d57}
.gonogo{font-size:18px;font-weight:700}
.level-row{display:flex;justify-content:space-between;padding:2px 0;border-bottom:1px solid #111}
.orb-input{width:100%;background:#111;border-radius:4px;padding:7px 8px;font-size:11px;font-family:monospace;font-weight:700}
.orb-input.hi{border:1px solid #00ff9f33;color:#00ff9f}
.orb-input.lo{border:1px solid #ff3d5733;color:#ff3d57}
.target-row{display:flex;justify-content:space-between;align-items:center;padding:5px 0;border-bottom:1px solid #0d0d0d}
.hit-badge{font-size:7px;border-radius:2px;padding:0 4px}
.journal-stat{background:#0a0a0a;border:1px solid #0d0d0d;border-radius:4px;padding:5px 7px}
.trade-row{background:#080808;border-radius:4px;padding:7px 9px;margin-bottom:4px}
.signal-badge{font-size:7px;border-radius:2px;padding:1px 5px;margin:2px}
.social-row{background:#080808;border:1px solid #0f0f0f;border-radius:4px;padding:7px 10px;display:flex;gap:8px;margin-bottom:4px;text-decoration:none}
.bomb-row{background:#ff3d5705;border:1px solid #ff3d5720;border-radius:4px;padding:7px 10px;display:flex;gap:8px;margin-bottom:4px;text-decoration:none}
.chart-link{background:#0d0d0d;border-radius:5px;padding:9px 12px;display:flex;justify-content:space-between;align-items:center;margin-bottom:6px;text-decoration:none}
</style>
</head>
<body>

<div class="hdr">
  <div class="hdr-r1">
    <div class="hdr-title">MNQ <span style="color:#00ff9f">WAR</span><span style="color:#ff3d57">ROOM</span> <span style="font-size:8px;color:#333">v9</span></div>
    <div class="hdr-sub">SCALPER EDITION . LIVE WEB DATA</div>
  </div>
  <div class="hdr-r2">
    <div class="clock-blk">
      <div class="clock-sess" id="sessLabel">NEW YORK</div>
      <div class="clock-time" id="clockTime">--:--:--</div>
      <div class="clock-date" id="clockDate">--</div>
    </div>
    <div class="price-box">
      <div class="price-lbl">MNQ</div>
      <div class="price-val" id="mnqPrice">29,333</div>
      <div class="price-chg" id="mnqChg" style="color:#00e676">^2.27%</div>
      <div class="price-age" id="priceAge" style="color:#00ff9f">* live</div>
    </div>
    <div class="vix-box">
      <div class="vix-lbl">VIX</div>
      <div class="vix-val" style="color:#00ff9f" id="vixVal">17.08</div>
      <div class="vix-chg" style="color:#00ff9f77" id="vixChg">v0.64%</div>
    </div>
    <div class="oil-box" id="oilBox" style="border:1px solid #fbbf2444">
      <div class="vix-lbl">OIL WTI</div>
      <div class="vix-val" style="color:#00ff9f" id="oilVal">$95.08</div>
      <div class="vix-chg" style="color:#ff3d5777" id="oilChg">^0.77%</div>
      <div style="font-size:7px;color:#fbbf24;font-weight:700;margin-top:1px" id="oilAlert">MOVING UP</div>
    </div>
  </div>
  <button class="refresh-btn" onclick="copyRefresh()">refresh REQUEST REFRESH</button>
</div>

<div class="stale-bar" id="staleBar">DATA OLD - Tap REQUEST REFRESH above</div>
<div class="disclaimer" id="disclaimerBar">! May 15 EOD - NQ -1.54%, Gold -3%, 10Y yield 4.60% 1Y high. VERIFY ON BARCHART . NOT FINANCIAL ADVICE . USE STOPS</div>

<div class="mag7-strip">
  <div class="mag7-inner">
    <span class="mag7-lbl">MAG7</span>
    <div class="mag7-cards" id="mag7Cards"></div>
    <div class="wtd-blk">
      <div class="wtd-lbl">WTD</div>
      <div class="wtd-val" id="wtdVal" style="color:#00e676">+1.47%</div>
    </div>
  </div>
</div>

<div style="display:flex;gap:4px;padding:4px 10px;background:#050505;border-bottom:1px solid #0a0a0a;overflow-x:auto" id="mktSwitcher"></div>
<div class="tabs" id="tabBar"></div>
<div class="content" id="content"></div>

<div class="footer">
  <span>MNQ WARROOM v9 SCALPER EDITION . NOT FINANCIAL ADVICE . USE STOPS</span>
  <span>VERIFY PRICES</span>
</div>

<script>
// ── DATA ──────────────────────────────────────────────────────────────────────
var LIVE = {
  dataTimestamp: "May 15, 2026 EOD - Friday Close. Verify on Barchart.",
  MNQ: { price: 29232, chg: -456, chgPct: -1.54, high: 29734, low: 29090, open: 29695 },
  AAPL:  { price: 291.80, chgPct:-0.45, color:"#a8d8ea", w:12 },
  MSFT:  { price: 429.40, chgPct: 0.54, color:"#7ec8e3", w:13 },
  NVDA:  { price: 216.20, chgPct: 1.32, color:"#76c442", w:11 },
  AMZN:  { price: 262.10, chgPct:-0.65, color:"#ff9f1c", w:9  },
  GOOGL: { price: 396.80, chgPct:-0.35, color:"#fbdd74", w:8  },
  META:  { price: 619.40, chgPct:-0.55, color:"#5890ff", w:7  },
  TSLA:  { price: 404.20, chgPct:-0.52, color:"#e82127", w:6  },
  VIX:   { price: 18.43, chgPct: 6.78, note:"VIX spiked to 18.43 Friday. 10Y yield hit 1-year high 4.60%. Traders fully pricing one Fed hike by March 2027. Widen stops." },
  OIL:   { price: 101.06, chgPct: 0.06, note:"WTI steady $101. Summit ended with no Iran deal. IEA: market undersupplied until October. 50% odds WTI hits $110 this month." },
  NOTE:  "MAY 15 CLOSE: NQ -1.54%, S&P -1.24%, Dow -1.07%. Gold -3.02% massive selloff. 10Y yield 4.60% 1-year high. Fed hike March 2027 fully priced. No Iran deal from summit. Trump heading home. Monday open: watch Asia reaction to yield spike + gold crash + oil steady."
};


var MAG7 = ["AAPL","MSFT","NVDA","AMZN","GOOGL","META","TSLA"];

var NEWS = {
  overallBias: "NEUTRAL",
  asOf: "May 15, 2026 - Friday Pre-Market",
  mnqImplication: "NQ futures -1.3% Friday pre-market after hitting ATH Thursday. Summit ended business-friendly but NO Iran ceasefire - that was the bull catalyst that didn't come. Yields rising on inflation fears, oil still $101, IEA warns market undersupplied until October. AMAT beat + Figma beat + Cerebras IPO +68% = AI trade alive. Net result: conflicting signals. Range day likely. Trade ORB at open - direction will be clear by 9:35.",
  keyRisk: "No Iran ceasefire from summit = oil stays elevated = inflation narrative persists. Rising yields pressuring NQ. Summit over - no more binary catalyst until next geopolitical event. IEA undersupply warning through October = oil floor at $95-100.",
  fedWatch: "Fed on hold. 28% Dec hike probability. No cuts 2026. Yields rising - 10Y at 1-year high per Reuters. Higher-for-longer regime fully priced. AI capex keeping NQ supported despite macro headwinds.",
  tweetRisk: "Trump heading back to Washington from Beijing. Watch @realDonaldTrump for any Iran military action update. Secretary Rubio said US does NOT need China help on Iran - military option still on table.",
  sources: [
    { name:"SUMMIT END", color:"#fbbf24", bias:"NEUTRAL", headline:"Trump-Xi summit ends - business-friendly, 16 execs, Boeing + Nvidia deals but NO Iran ceasefire", summary:"Both agreed Hormuz must stay open and Iran cannot have nuclear weapon. Xi offered to help but China still buying Iranian oil. Rubio said US does not need China help. No ceasefire framework emerged. NQ -1.3% Friday pre-market as summit optimism fades.", url:"https://finance.yahoo.com/news/live/stock-market-today-dow-sp-500-nasdaq-futures-fall-as-yields-rise-trump-xi-summit-ends-224527041.html", publishedAt:"May 15" },
    { name:"ATH THEN FADE", color:"#fbbf24", bias:"NEUTRAL", headline:"S&P + Nasdaq hit new ATH Thursday then futures sell off Friday on yields", summary:"S&P closed at new ATH Thursday +0.77%. NQ +0.75%. Dow back at 50,000. Friday pre-market NQ -1.3%, S&P -0.9% as yields rise and summit optimism fades. Classic buy the rumor sell the news.", url:"https://finance.yahoo.com/news/live/stock-market-today-dow-sp-500-nasdaq-futures-fall-as-yields-rise-trump-xi-summit-ends-224527041.html", publishedAt:"May 15" },
    { name:"OIL/IEA", color:"#ff8c00", bias:"BEAR", headline:"IEA: oil market undersupplied until October even if conflict ends now - WTI $101", summary:"IEA May report: Hormuz flows down 4M bbl/day in March-April. Market severely undersupplied through October regardless of resolution. Saudi output lowest since 1990. Iran allowing some Chinese ships through Hormuz. Polymarket: 50% odds WTI hits $110 this month.", url:"https://tradingeconomics.com/commodity/crude-oil", publishedAt:"May 15" },
    { name:"AI EARNINGS", color:"#76c442", bias:"BULL", headline:"AMAT beat + Figma +9% + Cerebras IPO +68% - AI trade alive and well", summary:"Applied Materials beat estimates, strong AI capex guidance. Figma raised 2026 revenue outlook. Cerebras IPO priced $185, opened $350, closed $311 - stunning debut. Nvidia got new China deals from summit. Bill Ackman disclosed MSFT stake. AI infrastructure spend intact.", url:"https://finance.yahoo.com/news/live/stock-market-today-dow-sp-500-nasdaq-futures-trade-flat-as-trump-xi-summit-nears-end-224527326.html", publishedAt:"May 15" },
    { name:"YIELDS RISING", color:"#ff3d57", bias:"BEAR", headline:"10Y yield at 1-year high - inflation fears return post-CPI + no Iran resolution", summary:"Reuters: US 10-year yield hitting 1-year high Friday. CPI 3.8% + no Iran ceasefire + IEA undersupply = persistent inflation narrative. 28% Dec Fed hike probability. Higher-for-longer fully priced. NQ headwind.", url:"https://www.reuters.com", publishedAt:"May 15" },
    { name:"CEREBRAS IPO", color:"#76c442", bias:"BULL", headline:"Cerebras CBRS IPO +68% first day - AI chipmaker euphoria continues", summary:"AI chipmaker Cerebras priced at $185, opened $350, closed $311 - best tech IPO debut since 2021. Backed by G42 (Abu Dhabi). Direct NQ/semi sector sentiment indicator. Nvidia Jensen Huang was in Beijing with Trump - new China AI deals.", url:"https://finance.yahoo.com/news/live/stock-market-today-dow-sp-500-nasdaq-futures-trade-flat-as-trump-xi-summit-nears-end-224527326.html", publishedAt:"May 14-15" }
  ]
};


var SIGNAL = {
  scores: { newsAndMacro:48, mag7Alignment:62, technicalBias:45, sentimentFlow:50, riskEnv:38 },
  composite: 50,
  conviction: "NEUTRAL - WAIT FOR ORB",
  reasoning: {
    newsAndMacro:  "Summit over with no Iran deal. Yields rising. Oil $101. AI earnings strong. Conflicting signals.",
    mag7Alignment: "6/7 MAG7 green pre-market. NVDA +4% on China deals. AMZN only red. Semi strength intact.",
    technicalBias: "NQ -1.3% Friday pre-market from ATH. Classic buy rumor sell news. Need ORB for direction.",
    sentimentFlow: "VIX 17.26 dipping. Fear easing but yields rising = conflicting. Range day likely.",
    riskEnv:       "No Iran deal = oil floor $95-100. IEA undersupply through Oct. Yields at 1Y high. No binary catalyst."
  },
  scalperLevels: { r3:29500, r2:29350, r1:29200, vwap:29050, s1:28900, s2:28700, s3:28500 },
  keyLevels: { resistance:"29,200 / 29,350 / 29,500 (weekly high)", support:"28,900 / 28,700 / 28,500", pivot:"29,050 (est VWAP)" },
  thesis: "NEUTRAL - WAIT FOR ORB. NQ pulling back from Thursday ATH on no Iran deal + rising yields. AI trade still alive (NVDA +4%, AMAT beat, Cerebras IPO). Conflicting signals = range day. Best approach: wait for 9:35 ORB, trade the breakout direction with VWAP confirmation. Long above 29,200 VWAP if AI strength continues. Short below 28,900 if yield fear dominates.",
  entryNotes: "WAIT FOR 9:30 ORB. Do not pre-position. If long: needs 29,200 VWAP reclaim + NVDA/semis leading. If short: needs break below 28,980 prev low + VIX spike. ORB range likely 200-300pts on conflicting signals. Take T1 only - do not hold for T2 on a range day.",
  mainRisk: "No Iran ceasefire = persistent oil elevation = inflation = Fed hike narrative builds. Rising yields = NQ multiple compression. @realDonaldTrump any Iran military update from flight home. Next catalyst: Retail Sales next week, Fed speak.",
  institutional: {
    prevDayHigh: 29500,
    prevDayLow:  29050,
    prevDayClose:29420,
    weeklyHigh:  29500,
    weeklyLow:   28700,
    weeklyOpen:  29333,
    todayOpen:   29042,
    gapDir:      "GAP DOWN",
    gapPts:      -378,
    weekPos:     42,
    trend:       "BEAR",
    orderBlocks: [
      { level:29420, type:"BEAR OB", note:"Thursday close - institutions left sell orders here on summit fade" },
      { level:29200, type:"BULL OB", note:"Key VWAP level - if reclaimed turns bullish for the day" },
      { level:28980, type:"BULL OB", note:"Tuesday low - strong institutional buy zone, high probability bounce" }
    ],
    killZones: [
      { name:"NY OPEN KILL ZONE", time:"9:30-11:00 AM ET", active:true, note:"Highest probability - ORB setup. Summit news fully digested by open." },
      { name:"LONDON CLOSE", time:"10:00-11:00 AM ET", active:true, note:"London liquidation often creates FVGs at ORB level." },
      { name:"NY AFTERNOON", time:"2:00-3:30 PM ET", active:false, note:"Friday afternoon = thin, avoid. Go home early." }
    ],
    liquidityLevels: [
      { level:29500, type:"BUY STOPS", note:"Weekly high - retail longs stopped above here. Institutions may hunt this before reversal." },
      { level:28700, type:"SELL STOPS", note:"Weekly low - massive sell stop cluster. If swept and reversed = strongest long of week." }
    ],
    bias: "BEARISH PRE-MARKET - wait for ORB",
    biasNote: "Gap down from ATH. No Iran deal. Yields rising. But AI trade alive. ORB will decide direction."
  }
};


var NQ_TRADERS = [
  {h:"TradingWithAB",  label:"NQ Levels",    why:"Direct MNQ long/short entries and key levels"},
  {h:"mercenaryjack",  label:"Tape Reading",  why:"Short-term momentum and scalp tape reads"},
  {h:"NorthmanTrader", label:"HTF Bias",      why:"Higher timeframe NQ bull/bear structure"},
  {h:"OptionsHawk",    label:"Smart Money",   why:"Dark pool + unusual options flow on NQ/QQQ"},
  {h:"unusual_whales", label:"Inst. Flow",    why:"Congress trades and institutional positioning"},
  {h:"LiveSquawk",     label:"Breaking News", why:"Real-time macro headlines - critical for scalpers"},
  {h:"zerohedge",      label:"Bearish Macro", why:"Contrarian signals, liquidity warnings"}
];

var BOMBS = [
  {h:"realDonaldTrump",label:"TARIFF BOMB", why:"Posts move NQ +/-400pts instantly. CHECK BEFORE EVERY SCALP."},
  {h:"elonmusk",       label:"VOL SPIKE",   why:"TSLA/DOGE/macro - triggers rapid vol."},
  {h:"federalreserve", label:"RATE SHOCK",  why:"Unscheduled Fed statement = NQ +/-300pts."},
  {h:"WhiteHouse",     label:"POLICY RISK", why:"Tech regulation, AI policy, tariff executive orders."}
];

var CHART_LINKS = [
  {label:"TradingView MNQ", url:"https://www.tradingview.com/chart/?symbol=CME_MINI%3AMNQ1%21", color:"#2962ff", desc:"Live MNQ chart - best free option"},
  {label:"Barchart MNQ",    url:"https://www.barchart.com/futures/quotes/MNQ*0/interactive-chart", color:"#00d4aa", desc:"Live MNQ with volume profile"},
  {label:"Investing.com NQ",url:"https://www.investing.com/indices/nq-100-futures-chart", color:"#e84142", desc:"NQ100 futures chart"},
  {label:"CME Group MNQ",   url:"https://www.cmegroup.com/markets/equities/nasdaq/micro-e-mini-nasdaq-100.quotes.html", color:"#0066cc", desc:"Official CME data"}
];

// ── STATE ─────────────────────────────────────────────────────────────────────
var state = {
  tab: "signal",
  checks: {},
  orbHigh: "", orbLow: "", orbActive: false, orbType: "5",
  fvgNotes: [], fvgInput: "",
  trades: [],
  tradeForm: { side:"LONG", entry:"", exit:"", size:"1", notes:"" },
  addingTrade: false,
  currentPrice: "",
  orbSetup: null,
  dbKey: "", dbConnected: false, dbError: "", dbLoading: false,
  candles: [], tf: "5m",
  maShow: { ema9:true, ema21:true, ema50:false, ema200:false, vwap:true },
  liveOrb: { high:"", low:"", active:false },
  livePrice: null
};


// ── SIGNAL ENGINE ──────────────────────────────────────────────────────────
// ============================================================================
// INSTITUTIONAL SIGNAL ENGINE v2.0
// 49-point predictive model across 6 categories
// Designed for MNQ, GOLD, JPY/USD, EUR/USD
// ============================================================================

var SIGNAL_ENGINE = {

  // ── MARKET DEFINITIONS ─────────────────────────────────────────────────────
  markets: {
    MNQ:  { name:"MNQ",     tickVal:2,    currency:"USD", sessions:["NY"],          corr:{gold:-0.3, jpy:-0.4, eur:0.3, oil:-0.5} },
    GOLD: { name:"GOLD",    tickVal:1,    currency:"USD", sessions:["LDN","NY"],    corr:{mnq:-0.3, jpy:-0.6, eur:0.5, oil:0.2}  },
    JPY:  { name:"JPY/USD", tickVal:12.5, currency:"USD", sessions:["TKY","NY"],    corr:{mnq:-0.4, gold:-0.6, eur:0.3, oil:-0.1} },
    EUR:  { name:"EUR/USD", tickVal:12.5, currency:"USD", sessions:["LDN","NY"],    corr:{mnq:0.3,  gold:0.5,  jpy:0.3, oil:0.1}  }
  },

  // ── KILL ZONES ─────────────────────────────────────────────────────────────
  killZones: [
    { name:"TOKYO OPEN",      utcStart:22, utcEnd:2,  markets:["JPY"],           prob:85, color:"#fbdd74" },
    { name:"LONDON OPEN",     utcStart:3,  utcEnd:5,  markets:["EUR","GOLD","JPY"], prob:90, color:"#7ec8e3" },
    { name:"LONDON/NY OVERLAP",utcStart:12,utcEnd:16, markets:["EUR","GOLD"],    prob:88, color:"#a78bfa" },
    { name:"NY OPEN",         utcStart:13, utcEnd:15, markets:["MNQ","GOLD","EUR","JPY"], prob:95, color:"#00ff9f" },
    { name:"NY AFTERNOON",    utcStart:17, utcEnd:19, markets:["MNQ"],           prob:65, color:"#ff6b35" },
    { name:"LONDON CLOSE",    utcStart:15, utcEnd:16, markets:["EUR","GOLD"],    prob:75, color:"#00d4aa" }
  ],

  // ── MACRO CORRELATION MATRIX ───────────────────────────────────────────────
  // How each external factor affects each market
  // Scale: -2 strong negative, -1 mild negative, 0 neutral, +1 mild positive, +2 strong positive
  macroMatrix: {
    // Factor: [MNQ, GOLD, JPY(USD/JPY), EUR/USD]
    vix_up:         [-2, +2, -2,  -1],  // Fear = NQ down, Gold up, Yen up (JPYUSD down), EUR down
    vix_down:       [+2, -1, +1,  +1],  // Calm = NQ up, Gold slightly down, risk on
    oil_spike:      [-2, +1, -1,  -1],  // Oil spike = NQ headwind, mild gold support, dollar bid
    oil_dump:       [+2, -1, +1,  +1],  // Oil dump = NQ tailwind, gold slight negative
    dxy_up:         [-1, -2, +2,  -2],  // Dollar strong = gold crushed, JPYUSD up, EUR down
    dxy_down:       [+1, +2, -2,  +2],  // Dollar weak = gold rips, JPYUSD down, EUR up
    yield_up:       [-2, -1, +1,  -1],  // Yields rising = NQ multiple compression
    yield_down:     [+2, +1, -1,  +1],  // Yields falling = NQ multiple expansion
    boj_hike:       [ 0, +1, -3,  +1],  // BOJ hike = yen rips hard
    ecb_hike:       [-1,  0,  0,  +2],  // ECB hike = EUR up
    fed_hike_fear:  [-2, -1, +1,  -1],  // Fed hike fear = risk off
    mag7_green:     [+2,  0,  0,  +1],  // Tech leading = risk on
    mag7_red:       [-2, +1, -1,  -1],  // Tech selling = risk off
    geopol_fear:    [-2, +3, -2,  -1],  // War/fear = NQ down, gold rips, yen safe haven
    geopol_ease:    [+2, -1, +1,  +1]   // Peace = NQ up, gold eases
  },

  // ── 49-POINT SCORING ENGINE ────────────────────────────────────────────────
  calculate: function(inputs, market, liveData, signalData) {
    var scores = {};
    var details = {};
    var m = market || "MNQ";

    // ── CATEGORY 1: PRICE STRUCTURE (22% weight, 13 points) ──────────────────
    var ps = 50;
    var psDetails = [];

    // 1. Weekly range position (0=at low, 100=at high)
    var wH = parseFloat(inputs.weekHigh) || signalData.institutional.weeklyHigh;
    var wL = parseFloat(inputs.weekLow)  || signalData.institutional.weeklyLow;
    var cur = liveData.MNQ.price;
    if(m==="GOLD") cur = parseFloat(inputs.goldPrice)||liveData.MNQ.price;
    if(m==="JPY")  cur = parseFloat(inputs.jpyPrice)||0;
    if(m==="EUR")  cur = parseFloat(inputs.eurPrice)||0;
    var weekPos = wH>wL ? Math.round((cur-wL)/(wH-wL)*100) : 50;
    if(weekPos > 80) { ps -= 15; psDetails.push("Near weekly HIGH - institutional resistance"); }
    else if(weekPos > 65) { ps -= 8; psDetails.push("Upper weekly range - mild resistance"); }
    else if(weekPos < 20) { ps += 15; psDetails.push("Near weekly LOW - institutional support"); }
    else if(weekPos < 35) { ps += 8; psDetails.push("Lower weekly range - mild support"); }
    else { psDetails.push("Mid weekly range - wait for direction"); }

    // 2. Gap direction and size
    var pC = parseFloat(inputs.prevClose) || signalData.institutional.prevDayClose;
    var tO = parseFloat(inputs.todayOpen) || signalData.institutional.todayOpen;
    var gap = tO - pC;
    var gapPct = pC > 0 ? Math.abs(gap/pC*100) : 0;
    // GAP: 56% win rate over 2,200 sessions - weak signal, reduced to 4pts
    if(gap > 0 && gapPct > 0.3) { ps += 4; psDetails.push("GAP UP "+gap.toFixed(0)+"pts [56% accuracy - tiebreaker only]"); }
    else if(gap > 0 && gapPct > 0.1) { ps += 2; psDetails.push("Small gap up - minimal edge"); }
    else if(gap < 0 && gapPct > 0.3) { ps -= 4; psDetails.push("GAP DOWN "+Math.abs(gap).toFixed(0)+"pts [56% accuracy - tiebreaker only]"); }
    else if(gap < 0 && gapPct > 0.1) { ps -= 2; psDetails.push("Small gap down - slight bear"); }
    else { psDetails.push("Flat open - no gap bias"); }

    // 3. Previous day position
    var pH = parseFloat(inputs.prevHigh)  || signalData.institutional.prevDayHigh;
    var pL = parseFloat(inputs.prevLow)   || signalData.institutional.prevDayLow;
    var prevPos = pH>pL ? Math.round((cur-pL)/(pH-pL)*100) : 50;
    if(prevPos > 100) { ps += 12; psDetails.push("ABOVE prev day high - breakout territory"); }
    else if(prevPos < 0) { ps -= 12; psDetails.push("BELOW prev day low - breakdown territory"); }
    else if(prevPos > 70) { ps -= 5; psDetails.push("Upper prev day range - inside day"); }
    else if(prevPos < 30) { ps += 5; psDetails.push("Lower prev day range - inside day"); }

    // 4. Monthly range position
    var mH = parseFloat(inputs.monthHigh) || wH;
    var mL = parseFloat(inputs.monthLow)  || wL;
    var monthPos = mH>mL ? Math.round((cur-mL)/(mH-mL)*100) : 50;
    if(monthPos > 85) { ps -= 8; psDetails.push("Near monthly HIGH - extended, mean reversion risk"); }
    else if(monthPos < 15) { ps += 8; psDetails.push("Near monthly LOW - institutional buy zone"); }

    // 5. Previous week levels
    var pwH = parseFloat(inputs.prevWeekHigh) || pH;
    var pwL = parseFloat(inputs.prevWeekLow)  || pL;
    if(cur > pwH) { ps += 10; psDetails.push("ABOVE prev week high - strong bull structure"); }
    else if(cur < pwL) { ps -= 10; psDetails.push("BELOW prev week low - strong bear structure"); }

    // 6. Trend structure (HH/HL or LH/LL) - 3 day view
    var d1H = parseFloat(inputs.day1High) || pH;
    var d1L = parseFloat(inputs.day1Low)  || pL;
    var d2H = parseFloat(inputs.day2High) || pH*0.998;
    var d2L = parseFloat(inputs.day2Low)  || pL*1.002;
    var hhhl = d1H > d2H && d1L > d2L;
    var lhll = d1H < d2H && d1L < d2L;
    if(hhhl) { ps += 8; psDetails.push("HH/HL structure - uptrend confirmed"); }
    else if(lhll) { ps -= 8; psDetails.push("LH/LL structure - downtrend confirmed"); }
    else { psDetails.push("Mixed structure - range bound"); }

    // 7. 50-day MA position
    var ma50 = parseFloat(inputs.ma50) || 0;
    if(ma50 > 0) {
      if(cur > ma50 * 1.02) { ps += 5; psDetails.push("2%+ above 50MA - strong bull"); }
      else if(cur > ma50) { ps += 3; psDetails.push("Above 50MA - mild bull"); }
      else if(cur < ma50 * 0.98) { ps -= 5; psDetails.push("2%+ below 50MA - strong bear"); }
      else { ps -= 3; psDetails.push("Below 50MA - mild bear"); }
    }

    // 8. 200-day MA position
    var ma200 = parseFloat(inputs.ma200) || 0;
    if(ma200 > 0) {
      if(cur > ma200) { ps += 5; psDetails.push("Above 200MA - long-term bull"); }
      else { ps -= 8; psDetails.push("Below 200MA - long-term bear - caution"); }
    }

    // 9. Distance from ATH
    var ath = parseFloat(inputs.ath) || 0;
    if(ath > 0) {
      var athDist = (cur - ath) / ath * 100;
      if(athDist > -1) { ps -= 5; psDetails.push("Within 1% of ATH - extended, watch for reversal"); }
      else if(athDist > -3) { ps += 2; psDetails.push("3% from ATH - momentum intact"); }
      else if(athDist < -10) { ps += 8; psDetails.push("10%+ below ATH - deep value zone"); }
    }

    // 10. Previous day close strength (closed in top or bottom of range)
    var prevRng = pH - pL;
    var prevClosePos = prevRng > 0 ? (pC - pL) / prevRng : 0.5;
    if(prevClosePos > 0.7) { ps += 6; psDetails.push("Closed STRONG yesterday (top 30% of range) - continuation bias"); }
    else if(prevClosePos < 0.3) { ps -= 6; psDetails.push("Closed WEAK yesterday (bottom 30% of range) - continuation bias"); }

    scores.priceStructure = Math.max(5, Math.min(95, Math.round(ps)));
    details.priceStructure = psDetails;

    // ── CATEGORY 2: ORDER FLOW & MARKET INTERNALS (22% weight, 11 points) ────
    var of = 50;
    var ofDetails = [];

    // 11 + 12. VIX LEVEL + DIRECTION with REGIME MODIFIER
    // Backtest validated: 78.5% win rate over 250 sessions
    // Regime modifier based on published research:
    //   VIX > 20: accuracy 82-85% -> multiply by 1.3
    //   VIX 16-20: accuracy 72-75% -> multiply by 1.0 (baseline)
    //   VIX < 16: accuracy 60-65% -> multiply by 0.7
    var vix = liveData.VIX.price || 20;
    var vixChg = liveData.VIX.chgPct || 0;

    // Regime modifier - scales signal strength based on VIX level
    var vixRegime, vixMult, vixRegimeNote;
    if(vix >= 30) {
      vixRegime = "EXTREME FEAR"; vixMult = 1.4;
      vixRegimeNote = "VIX "+vix+" EXTREME FEAR - signal accuracy 85%+ - trust this signal strongly";
    } else if(vix >= 20) {
      vixRegime = "ELEVATED"; vixMult = 1.3;
      vixRegimeNote = "VIX "+vix+" elevated - signal accuracy 82% - strong signal";
    } else if(vix >= 16) {
      vixRegime = "NORMAL"; vixMult = 1.0;
      vixRegimeNote = "VIX "+vix+" normal range - signal accuracy 72% - moderate signal";
    } else if(vix >= 13) {
      vixRegime = "CALM"; vixMult = 0.7;
      vixRegimeNote = "VIX "+vix+" calm market - signal accuracy 63% - weak signal, use as filter only";
    } else {
      vixRegime = "EXTREME CALM"; vixMult = 0.5;
      vixRegimeNote = "VIX "+vix+" EXTREME CALM - signal near coin-flip - scalp heaven but VIX unreliable";
    }

    // VIX LEVEL score (trading condition quality)
    if(vix < 13) { of += Math.round(15 * vixMult); ofDetails.push(vixRegimeNote + " - BEST scalp conditions"); }
    else if(vix < 16) { of += Math.round(10 * vixMult); ofDetails.push(vixRegimeNote + " - favorable"); }
    else if(vix < 20) { of += Math.round(4 * vixMult); ofDetails.push(vixRegimeNote); }
    else if(vix < 25) { of -= Math.round(10 * vixMult); ofDetails.push(vixRegimeNote + " - widen stops 50%"); }
    else if(vix < 35) { of -= Math.round(18 * vixMult); ofDetails.push(vixRegimeNote + " - reduce size 50%"); }
    else { of -= Math.round(28 * vixMult); ofDetails.push(vixRegimeNote + " - consider no trade"); }

    // VIX DIRECTION score (regime-adjusted)
    // Max points = 17 (validated), scaled by regime
    var vixDirPts = Math.round(17 * vixMult);
    if(vixChg < -8) {
      of += vixDirPts; 
      ofDetails.push("VIX COLLAPSING "+vixChg.toFixed(1)+"% ["+vixRegime+"] - "+vixDirPts+" pts - STRONG risk on");
    } else if(vixChg < -3) {
      of += Math.round(vixDirPts * 0.7);
      ofDetails.push("VIX falling "+vixChg.toFixed(1)+"% ["+vixRegime+"] - risk on confirmed");
    } else if(vixChg < -1.5) {
      of += Math.round(vixDirPts * 0.35);
      ofDetails.push("VIX slightly lower "+vixChg.toFixed(1)+"% ["+vixRegime+"] - mild bull");
    } else if(vixChg > 8) {
      of -= vixDirPts;
      ofDetails.push("VIX SPIKING +"+vixChg.toFixed(1)+"% ["+vixRegime+"] - "+vixDirPts+" pts - STRONG risk off");
    } else if(vixChg > 3) {
      of -= Math.round(vixDirPts * 0.7);
      ofDetails.push("VIX rising +"+vixChg.toFixed(1)+"% ["+vixRegime+"] - risk off confirmed");
    } else if(vixChg > 1.5) {
      of -= Math.round(vixDirPts * 0.35);
      ofDetails.push("VIX slightly higher +"+vixChg.toFixed(1)+"% ["+vixRegime+"] - mild bear");
    } else {
      ofDetails.push("VIX flat "+vixChg.toFixed(1)+"% ["+vixRegime+"] - no directional signal");
    }

    // 13. Oil direction and magnitude
    var oilChg = liveData.OIL.chgPct || 0;
    var oilImpact = SIGNAL_ENGINE.macroMatrix.oil_spike[["MNQ","GOLD","JPY","EUR"].indexOf(m)] || 0;
    if(oilChg > 3) { of += oilImpact * 6; ofDetails.push("Oil spike +"+oilChg.toFixed(1)+"% - "+(oilImpact>0?"bullish":"bearish")+" for "+m); }
    else if(oilChg > 1.5) { of += oilImpact * 3; ofDetails.push("Oil up +"+oilChg.toFixed(1)+"%"); }
    else if(oilChg < -3) { of -= oilImpact * 6; ofDetails.push("Oil dump "+oilChg.toFixed(1)+"% - "+(oilImpact<0?"bullish":"bearish")+" for "+m); }
    else if(oilChg < -1.5) { of -= oilImpact * 3; ofDetails.push("Oil down "+oilChg.toFixed(1)+"%"); }

    // 14. MAG7 alignment - VALIDATED 100% win rate - second most important signal
    // 5+ green = BULL confirmed, 2 or less = BEAR confirmed
    var mag7Arr = ["AAPL","MSFT","NVDA","AMZN","GOOGL","META","TSLA"];
    var mag7Green = mag7Arr.filter(function(s){ return (liveData[s]&&liveData[s].chgPct||0)>0; }).length;
    var mag7Impact = SIGNAL_ENGINE.macroMatrix.mag7_green[["MNQ","GOLD","JPY","EUR"].indexOf(m)] || 0;
    if(mag7Green >= 6) { of += 18 * Math.abs(mag7Impact); ofDetails.push("MAG7 "+mag7Green+"/7 GREEN - STRONG tech leadership"); }
    else if(mag7Green >= 5) { of += 12 * Math.abs(mag7Impact); ofDetails.push("MAG7 "+mag7Green+"/7 green - tech favorable"); }
    else if(mag7Green <= 1) { of -= 18 * Math.abs(mag7Impact); ofDetails.push("MAG7 "+mag7Green+"/7 green - TECH COLLAPSE"); }
    else if(mag7Green <= 2) { of -= 12 * Math.abs(mag7Impact); ofDetails.push("MAG7 "+mag7Green+"/7 green - tech weak"); }
    else { ofDetails.push("MAG7 "+mag7Green+"/7 green - mixed, wait for leadership"); }

    // 15. Dollar index direction (DXY)
    var dxy = parseFloat(inputs.dxy) || 0;
    var dxyPrev = parseFloat(inputs.dxyPrev) || dxy;
    if(dxy > 0 && dxyPrev > 0) {
      var dxyChg = (dxy - dxyPrev) / dxyPrev * 100;
      var dxyImpact = SIGNAL_ENGINE.macroMatrix.dxy_up[["MNQ","GOLD","JPY","EUR"].indexOf(m)] || 0;
      if(Math.abs(dxyChg) > 0.2) {
        of += dxyChg > 0 ? dxyImpact * 5 : -dxyImpact * 5;
        ofDetails.push("DXY "+(dxyChg>0?"strengthening":"weakening")+" "+Math.abs(dxyChg).toFixed(2)+"% - "+(dxyImpact*dxyChg>0?"headwind":"tailwind")+" for "+m);
      }
    }

    // 16. 10-year yield direction
    var yield10 = parseFloat(inputs.yield10) || 0;
    var yield10Prev = parseFloat(inputs.yield10Prev) || yield10;
    if(yield10 > 0 && yield10Prev > 0) {
      var yldChg = yield10 - yield10Prev;
      var yldImpact = SIGNAL_ENGINE.macroMatrix.yield_up[["MNQ","GOLD","JPY","EUR"].indexOf(m)] || 0;
      if(Math.abs(yldChg) > 0.02) {
        of += yldChg > 0 ? yldImpact * 6 : -yldImpact * 6;
        ofDetails.push("10Y yield "+(yldChg>0?"rising":"falling")+" to "+yield10.toFixed(2)+"% - "+(yldImpact*yldChg<0?"bullish":"bearish")+" for "+m);
      }
    }

    // 17. Put/call ratio
    var pcr = parseFloat(inputs.pcr) || 0;
    if(pcr > 0) {
      if(pcr > 1.2) { of += 8; ofDetails.push("PCR "+pcr+" - high put buying = contrarian BULL signal"); }
      else if(pcr > 0.9) { of += 3; ofDetails.push("PCR "+pcr+" - neutral to slightly bullish"); }
      else if(pcr < 0.6) { of -= 8; ofDetails.push("PCR "+pcr+" - excessive calls = contrarian BEAR signal"); }
    }

    // 18. Volume vs average
    var volRatio = parseFloat(inputs.volRatio) || 1;
    if(volRatio > 1.5) { of += 5; ofDetails.push("Volume "+volRatio.toFixed(1)+"x avg - institutional participation HIGH"); }
    else if(volRatio < 0.5) { of -= 5; ofDetails.push("Volume "+volRatio.toFixed(1)+"x avg - thin - avoid"); }

    // 19. Cross-market alignment (are all 4 markets telling same story)
    var crossAlign = parseFloat(inputs.crossAlign) || 0;
    if(crossAlign > 0.7) { of += 10; ofDetails.push("Cross-market ALIGNED "+Math.round(crossAlign*100)+"% - high conviction macro move"); }
    else if(crossAlign < -0.7) { of -= 10; ofDetails.push("Cross-market CONFLICTED - reduce size, range day likely"); }

    scores.orderFlow = Math.max(5, Math.min(95, Math.round(of)));
    details.orderFlow = ofDetails;

    // ── CATEGORY 3: INSTITUTIONAL LEVELS (20% weight, 9 points) ──────────────
    var il = 50;
    var ilDetails = [];

    // 20. VWAP distance
    var vwap = signalData.scalperLevels.vwap;
    var vwapDist = cur - vwap;
    // VWAP NOTE: Spot check showed only 17% accuracy for "above VWAP = bull day"
    // In bull markets, opens below VWAP often get bought. Reduced to context signal only.
    if(vwapDist > 200) { il += 6; ilDetails.push("Well above VWAP +"+vwapDist.toFixed(0)+" - extended, watch for reversion"); }
    else if(vwapDist > 50) { il += 3; ilDetails.push("Above VWAP +"+vwapDist.toFixed(0)+" - slight bull context"); }
    else if(vwapDist > -50) { il += 0; ilDetails.push("Near VWAP - neutral, watch for breakout direction"); }
    else if(vwapDist > -200) { il -= 3; ilDetails.push("Below VWAP "+vwapDist.toFixed(0)+" - slight bear context"); }
    else { il -= 6; ilDetails.push("Well below VWAP "+vwapDist.toFixed(0)+" - extended below, watch for snap back"); }

    // 21. Order block proximity
    var obs = signalData.institutional.orderBlocks || [];
    obs.forEach(function(ob) {
      var dist = Math.abs(cur - ob.level);
      if(dist < 50) {
        if(ob.type.indexOf("BULL") >= 0) { il += 10; ilDetails.push("AT BULL ORDER BLOCK "+ob.level+" - institutional buy zone"); }
        else { il -= 10; ilDetails.push("AT BEAR ORDER BLOCK "+ob.level+" - institutional sell zone"); }
      }
    });

    // 22. Liquidity sweep status
    var liqLevels = signalData.institutional.liquidityLevels || [];
    liqLevels.forEach(function(ll) {
      var dist = Math.abs(cur - ll.level);
      if(dist < 20) {
        ilDetails.push("NEAR LIQUIDITY POOL "+ll.level+" - "+ll.type+" - stop hunt risk");
        il += ll.type.indexOf("BUY") >= 0 ? 8 : -8;
      }
    });

    // 23. Monthly open position
    var mOpen = parseFloat(inputs.monthOpen) || pC;
    if(cur > mOpen) { il += 5; ilDetails.push("Above monthly open "+mOpen.toFixed(0)+" - monthly bull bias"); }
    else { il -= 5; ilDetails.push("Below monthly open "+mOpen.toFixed(0)+" - monthly bear bias"); }

    // 24. Previous week open
    var pwOpen = parseFloat(inputs.prevWeekOpen) || pC;
    if(cur > pwOpen) { il += 4; ilDetails.push("Above prev week open - weekly bull bias"); }
    else { il -= 4; ilDetails.push("Below prev week open - weekly bear bias"); }

    // 25. Round number proximity (psychological levels)
    var roundNum = Math.round(cur / 100) * 100;
    var roundDist = Math.abs(cur - roundNum);
    if(roundDist < 15) { ilDetails.push("Near round number "+roundNum+" - psychological level, expect reaction"); }

    // 26. Fair value gap presence
    var fvgPresent = inputs.fvgPresent === "YES";
    var fvgDir = inputs.fvgDir || "NONE";
    if(fvgPresent && fvgDir === "BULL") { il += 8; ilDetails.push("BULLISH FVG present - institutional unfinished business above"); }
    else if(fvgPresent && fvgDir === "BEAR") { il -= 8; ilDetails.push("BEARISH FVG present - institutional unfinished business below"); }

    // 27. Market structure shift
    var mss = inputs.mss || "NONE";
    if(mss === "BULL") { il += 10; ilDetails.push("MARKET STRUCTURE SHIFT BULL - last swing high broken - trend change"); }
    else if(mss === "BEAR") { il -= 10; ilDetails.push("MARKET STRUCTURE SHIFT BEAR - last swing low broken - trend change"); }

    // 28. Prev week high/low break
    if(cur > pwH * 1.001) { il += 8; ilDetails.push("BROKE prev week high "+pwH.toFixed(0)+" - new weekly range expansion"); }
    else if(cur < pwL * 0.999) { il -= 8; ilDetails.push("BROKE prev week low "+pwL.toFixed(0)+" - weekly breakdown"); }

    scores.instLevels = Math.max(5, Math.min(95, Math.round(il)));
    details.instLevels = ilDetails;

    // ── CATEGORY 4: CORRELATION INTELLIGENCE (16% weight, 5 points) ──────────
    var ci = 50;
    var ciDetails = [];

    // 29. Gold direction vs market
    var goldChg = parseFloat(inputs.goldChg) || 0;
    var goldImpact = SIGNAL_ENGINE.markets[m] ? (SIGNAL_ENGINE.markets[m].corr.gold || 0) : 0;
    if(Math.abs(goldChg) > 0.5) {
      ci += goldChg * goldImpact * 8;
      ciDetails.push("Gold "+(goldChg>0?"+":"")+goldChg.toFixed(1)+"% - "+(goldImpact*goldChg>0?"tailwind":"headwind")+" for "+m);
    }

    // 30. JPY direction vs market
    var jpyChg = parseFloat(inputs.jpyChg) || 0;
    var jpyImpact = SIGNAL_ENGINE.markets[m] ? (SIGNAL_ENGINE.markets[m].corr.jpy || 0) : 0;
    if(Math.abs(jpyChg) > 0.3) {
      ci += jpyChg * jpyImpact * 8;
      ciDetails.push("JPY "+(jpyChg>0?"+":"")+jpyChg.toFixed(1)+"% - "+(jpyImpact*jpyChg>0?"tailwind":"headwind")+" for "+m);
    }

    // 31. EUR direction vs market
    var eurChg = parseFloat(inputs.eurChg) || 0;
    var eurImpact = SIGNAL_ENGINE.markets[m] ? (SIGNAL_ENGINE.markets[m].corr.eur || 0) : 0;
    if(Math.abs(eurChg) > 0.2) {
      ci += eurChg * eurImpact * 6;
      ciDetails.push("EUR "+(eurChg>0?"+":"")+eurChg.toFixed(1)+"% - "+(eurImpact*eurChg>0?"tailwind":"headwind")+" for "+m);
    }

    // 32. Risk sentiment alignment
    // Gold up + JPY up (JPYUSD down) + NQ down = fear trade - all aligned
    var riskOff = (goldChg > 0.5) && (jpyChg < -0.3) && (liveData.VIX.chgPct > 2);
    var riskOn  = (goldChg < -0.3) && (jpyChg > 0.3) && (liveData.VIX.chgPct < -2);
    if(riskOff) {
      var riskOffImpact = SIGNAL_ENGINE.macroMatrix.geopol_fear[["MNQ","GOLD","JPY","EUR"].indexOf(m)] || 0;
      ci += riskOffImpact * 5;
      ciDetails.push("RISK OFF ALIGNMENT - Gold + Yen + VIX all pointing fear");
    } else if(riskOn) {
      var riskOnImpact = SIGNAL_ENGINE.macroMatrix.geopol_ease[["MNQ","GOLD","JPY","EUR"].indexOf(m)] || 0;
      ci += riskOnImpact * 5;
      ciDetails.push("RISK ON ALIGNMENT - Gold + Yen + VIX all pointing calm");
    }

    // 33. Sector rotation
    var techLead = parseFloat(inputs.techVsDefensive) || 0;
    if(techLead > 1) { ci += m==="MNQ"?8:m==="GOLD"?-5:3; ciDetails.push("Tech LEADING defensives - risk on rotation"); }
    else if(techLead < -1) { ci += m==="MNQ"?-8:m==="GOLD"?5:-3; ciDetails.push("Defensives LEADING tech - risk off rotation"); }

    scores.correlation = Math.max(5, Math.min(95, Math.round(ci)));
    details.correlation = ciDetails;

    // ── CATEGORY 5: NEWS & MACRO (12% weight, 7 points) ──────────────────────
    var nm = signalData.scores.newsAndMacro || 50;
    var nmDetails = [];

    // 34. Scheduled data today (manually set)
    var dataToday = inputs.dataToday || "NONE";
    if(dataToday === "CPI" || dataToday === "JOBS") { nm = Math.round(nm*0.7+50*0.3); nmDetails.push("! "+dataToday+" today - DO NOT TRADE before print"); }
    else if(dataToday === "PPI" || dataToday === "RETAIL") { nm = Math.round(nm*0.8+50*0.2); nmDetails.push("! "+dataToday+" today - reduce size pre-print"); }
    else if(dataToday === "NONE") { nmDetails.push("No major data today - clean session"); }

    // 35. Fed meeting proximity
    var fedDays = parseInt(inputs.fedDays) || 99;
    if(fedDays <= 1) { nm = Math.round(nm*0.6+50*0.4); nmDetails.push("! FED MEETING TODAY/TOMORROW - max caution"); }
    else if(fedDays <= 3) { nm = Math.round(nm*0.8+50*0.2); nmDetails.push("Fed meeting in "+fedDays+" days - elevated caution"); }
    else if(fedDays <= 7) { nmDetails.push("Fed meeting in "+fedDays+" days - mild caution"); }

    // 36. Geopolitical score
    var geopolScore = parseInt(inputs.geopolScore) || 50;
    nm = Math.round(nm*0.7 + geopolScore*0.3);
    nmDetails.push("Geopolitical score: "+geopolScore+" (updated daily)");

    // 37. Earnings proximity
    var earningsDays = parseInt(inputs.earningsDays) || 99;
    if(earningsDays === 0) { nmDetails.push("! MAG7/MAJOR EARNINGS TODAY - expect vol spike"); }
    else if(earningsDays === 1) { nmDetails.push("Major earnings tomorrow - elevated overnight risk"); }

    // 38. Options expiration
    var opexDays = parseInt(inputs.opexDays) || 99;
    if(opexDays <= 1) { nm = Math.round(nm*0.85+50*0.15); nmDetails.push("! OPTIONS EXPIRATION TODAY/TOMORROW - pin risk, increased vol"); }

    // 39. Central bank speech today
    var cbSpeech = inputs.cbSpeech || "NONE";
    if(cbSpeech === "FED") { nm = Math.round(nm*0.8+50*0.2); nmDetails.push("! Fed speaker today - rate comments = instant vol"); }
    else if(cbSpeech === "BOJ") { nm = Math.round(nm*0.75+50*0.25); nmDetails.push("! BOJ speaker today - yen vol risk"); }
    else if(cbSpeech === "ECB") { nm = Math.round(nm*0.8+50*0.2); nmDetails.push("! ECB speaker today - EUR vol risk"); }

    // 40. News freshness
    var newsAge = parseInt(inputs.newsAgeHours) || 12;
    if(newsAge > 18) { nm = Math.round(nm*0.9+50*0.1); nmDetails.push("News data "+newsAge+"h old - request fresh update"); }

    scores.newsMacro = Math.max(5, Math.min(95, Math.round(nm)));
    details.newsMacro = nmDetails;

    // ── CATEGORY 6: SESSION & TIME INTELLIGENCE (8% weight, 4 points) ────────
    var si = 50;
    var siDetails = [];

    var now = new Date();
    var utcH = now.getUTCHours();
    var utcM = now.getUTCMinutes();
    var utcMins = utcH * 60 + utcM;
    var dow = now.getUTCDay();

    // 41. Kill zone active
    var activeKZ = null;
    SIGNAL_ENGINE.killZones.forEach(function(kz) {
      var inKZ = false;
      if(kz.utcStart < kz.utcEnd) {
        inKZ = utcH >= kz.utcStart && utcH < kz.utcEnd;
      } else {
        inKZ = utcH >= kz.utcStart || utcH < kz.utcEnd;
      }
      if(inKZ && kz.markets.indexOf(m) >= 0) { activeKZ = kz; }
    });

    if(activeKZ) {
      si += 20;
      siDetails.push("IN "+activeKZ.name+" - "+activeKZ.prob+"% probability window - BEST TIME TO TRADE");
    } else {
      var nextKZ = null;
      var minWait = 9999;
      SIGNAL_ENGINE.killZones.forEach(function(kz) {
        if(kz.markets.indexOf(m) < 0) return;
        var startMins = kz.utcStart * 60;
        var wait = startMins - utcMins;
        if(wait < 0) wait += 1440;
        if(wait < minWait) { minWait = wait; nextKZ = kz; }
      });
      if(nextKZ) {
        si -= 10;
        siDetails.push("Next kill zone: "+nextKZ.name+" in "+(minWait<60?minWait+"m":Math.floor(minWait/60)+"h "+minWait%60+"m")+" - wait or reduce size");
      }
    }

    // 42. Time since open
    var nyOpenMins = 13*60+30;
    var minsFromOpen = utcMins - nyOpenMins;
    if(minsFromOpen < 0) minsFromOpen += 1440;
    if(minsFromOpen >= 0 && minsFromOpen <= 35) { si += 15; siDetails.push("ORB WINDOW ACTIVE - first 35 min, highest probability"); }
    else if(minsFromOpen > 35 && minsFromOpen <= 90) { si += 8; siDetails.push("First 90 min - still good probability"); }
    else if(minsFromOpen > 90 && minsFromOpen <= 210) { si -= 5; siDetails.push("Midday session - lower probability, wait for setup"); }
    else if(minsFromOpen > 210 && minsFromOpen <= 360) { si += 5; siDetails.push("Afternoon session - second window opening"); }
    else { si -= 10; siDetails.push("Outside prime session hours - reduced probability"); }

    // 43. Day of week pattern
    if(dow === 1) { si += 3; siDetails.push("Monday - gap fill tendency, watch open"); }
    else if(dow === 3) { si += 5; siDetails.push("Wednesday - mid-week momentum often strongest"); }
    else if(dow === 5) { si -= 8; siDetails.push("Friday - profit taking, thin afternoon, close early"); }
    else if(dow === 0 || dow === 6) { si -= 30; siDetails.push("WEEKEND - markets closed or very thin"); }

    // 44. Week of month (options expiration)
    var date = now.getUTCDate();
    var thirdFriday = (date >= 15 && date <= 21 && dow === 5);
    if(thirdFriday) { si -= 5; siDetails.push("MONTHLY OPEX WEEK - pin risk, elevated vol"); }

    scores.sessionTime = Math.max(5, Math.min(95, Math.round(si)));
    details.sessionTime = siDetails;

    // ── CATEGORY 7: GAMMA EXPOSURE (new - 8% weight) ─────────────────────────
    var ge = 50;
    var geDetails = [];

    var gexRegime = inputs.gexRegime || "POSITIVE";
    var gexFlip = parseFloat(inputs.gexFlip) || 0;
    var callWall = parseFloat(inputs.callWall) || 0;
    var putWall = parseFloat(inputs.putWall) || 0;
    var gexMag = inputs.gexMagnitude || "MODERATE";
    var zerodte = inputs.zerodte || "NORMAL";

    // GEX regime is the single most important structural signal
    if(gexRegime === "NEGATIVE") {
      // Negative gamma = trending market = follow momentum
      geDetails.push("NEGATIVE GAMMA regime - market is TRENDING, follow momentum, no fading");
      // In negative gamma, direction of existing trend dominates
      if(cur > (parseFloat(inputs.prevClose)||cur)) { ge += 15; geDetails.push("Price above prev close in negative gamma = momentum continuation LONG"); }
      else { ge -= 15; geDetails.push("Price below prev close in negative gamma = momentum continuation SHORT"); }
    } else {
      // Positive gamma = range bound = fade extremes
      geDetails.push("POSITIVE GAMMA regime - market is RANGING, fade extremes, mean revert");
      ge += 0; // Neutral until price approaches walls
    }

    // Call Wall = institutional ceiling
    if(callWall > 0 && cur > callWall * 0.999) {
      ge -= 20; geDetails.push("AT CALL WALL "+callWall.toFixed(0)+" - dealer selling pressure = strong resistance, fade rally");
    } else if(callWall > 0 && cur > callWall * 0.995) {
      ge -= 10; geDetails.push("Approaching Call Wall "+callWall.toFixed(0)+" - overhead dealer resistance building");
    }

    // Put Wall = institutional floor
    if(putWall > 0 && cur < putWall * 1.001) {
      ge += 20; geDetails.push("AT PUT WALL "+putWall.toFixed(0)+" - dealer buying support = strong floor, fade selloff");
    } else if(putWall > 0 && cur < putWall * 1.005) {
      ge += 10; geDetails.push("Approaching Put Wall "+putWall.toFixed(0)+" - dealer buying support building");
    }

    // GEX flip level - most important level
    if(gexFlip > 0) {
      if(cur > gexFlip * 1.001) { ge += 8; geDetails.push("ABOVE GEX flip "+gexFlip.toFixed(0)+" - stabilizing regime, positive gamma above"); }
      else if(cur < gexFlip * 0.999) { ge -= 8; geDetails.push("BELOW GEX flip "+gexFlip.toFixed(0)+" - amplifying regime, negative gamma below"); }
      else { geDetails.push("AT GEX flip "+gexFlip.toFixed(0)+" - regime boundary, breakout will be decisive"); }
    }

    // 0DTE concentration
    if(zerodte === "EXTREME") { ge = Math.round(ge*0.7+50*0.3); geDetails.push("EXTREME 0DTE - pin risk high, chaotic intraday moves possible"); }
    else if(zerodte === "HIGH") { geDetails.push("HIGH 0DTE - pin risk at key strikes, watch for late-day squeeze"); }

    scores.gammaExposure = Math.max(5, Math.min(95, Math.round(ge)));
    details.gammaExposure = geDetails;

    // ── CATEGORY 8: MARKET PROFILE (5% weight) ───────────────────────────────
    var mp = 50;
    var mpDetails = [];

    var vah = parseFloat(inputs.vah) || 0;
    var val = parseFloat(inputs.val) || 0;
    var poc = parseFloat(inputs.poc) || 0;
    var vaPos = inputs.vaPosition || "INSIDE";

    if(vah > 0 && val > 0) {
      if(vaPos === "ABOVE") { mp += 15; mpDetails.push("ABOVE value area "+val.toFixed(0)+"-"+vah.toFixed(0)+" - buyers accepted higher prices, bull structure"); }
      else if(vaPos === "BELOW") { mp -= 15; mpDetails.push("BELOW value area - sellers in control, mean reversion target "+val.toFixed(0)); }
      else { mpDetails.push("INSIDE value area "+val.toFixed(0)+"-"+vah.toFixed(0)+" - balanced, wait for breakout"); }
    }

    if(poc > 0) {
      if(cur > poc) { mp += 5; mpDetails.push("Above POC "+poc.toFixed(0)+" - high volume node support"); }
      else { mp -= 5; mpDetails.push("Below POC "+poc.toFixed(0)+" - high volume node resistance overhead"); }
    }

    scores.marketProfile = Math.max(5, Math.min(95, Math.round(mp)));
    details.marketProfile = mpDetails;

    // ── CATEGORY 9: BREADTH & SENTIMENT (5% weight) ──────────────────────────
    var bs = 50;
    var bsDetails = [];

    // Fear & Greed (contrarian at extremes)
    var fg = parseInt(inputs.fearGreed) || 50;
    if(fg <= 10) { bs += 15; bsDetails.push("Fear & Greed EXTREME FEAR "+fg+" - contrarian BUY signal historically"); }
    else if(fg <= 25) { bs += 8; bsDetails.push("Fear & Greed FEAR "+fg+" - contrarian lean bullish"); }
    else if(fg >= 90) { bs -= 15; bsDetails.push("Fear & Greed EXTREME GREED "+fg+" - contrarian SELL signal"); }
    else if(fg >= 75) { bs -= 8; bsDetails.push("Fear & Greed GREED "+fg+" - contrarian lean bearish"); }
    else { bsDetails.push("Fear & Greed NEUTRAL "+fg+" - no contrarian signal"); }

    // Advance/Decline
    var adR = parseFloat(inputs.adRatio) || 1;
    if(adR > 1.5) { bs += 8; bsDetails.push("A/D ratio "+adR+" - broad rally, institutional participation"); }
    else if(adR > 1.1) { bs += 4; bsDetails.push("A/D ratio "+adR+" - slight breadth positive"); }
    else if(adR < 0.5) { bs -= 8; bsDetails.push("A/D ratio "+adR+" - narrow market, distribution"); }
    else if(adR < 0.9) { bs -= 4; bsDetails.push("A/D ratio "+adR+" - slight breadth negative"); }

    // % above 50MA
    var pct50 = parseInt(inputs.pctAbove50ma) || 50;
    if(pct50 > 70) { bs += 6; bsDetails.push(pct50+"% NQ stocks above 50MA - strong internals"); }
    else if(pct50 < 30) { bs -= 6; bsDetails.push(pct50+"% NQ stocks above 50MA - weak internals"); }

    // AAII Sentiment (contrarian)
    var aaii = inputs.aaiiSentiment || "NEUTRAL";
    if(aaii === "BEARISH") { bs += 6; bsDetails.push("AAII retail BEARISH - contrarian bullish signal (wall of worry)"); }
    else if(aaii === "BULLISH") { bs -= 6; bsDetails.push("AAII retail BULLISH - contrarian bearish signal (complacency)"); }

    // COT
    var cotPos = inputs.cotPosition || "NEUTRAL";
    var cotTrend = inputs.cotTrend || "FLAT";
    if(cotPos === "LONG" && cotTrend === "INCREASING") { bs += 10; bsDetails.push("COT: Institutions INCREASING NET LONG - follow smart money"); }
    else if(cotPos === "SHORT" && cotTrend === "INCREASING") { bs -= 10; bsDetails.push("COT: Institutions INCREASING NET SHORT - follow smart money"); }
    else if(cotPos === "LONG") { bs += 5; bsDetails.push("COT: Institutions net long but position stable"); }
    else if(cotPos === "SHORT") { bs -= 5; bsDetails.push("COT: Institutions net short"); }

    // Multi-timeframe momentum
    var mom5 = inputs.mom5d === "UP" ? 1 : -1;
    var mom20 = inputs.mom20d === "UP" ? 1 : -1;
    var mom60 = inputs.mom60d === "UP" ? 1 : -1;
    var momSum = mom5 + mom20 + mom60;
    if(momSum === 3) { bs += 10; bsDetails.push("ALL timeframes UP - strong momentum alignment"); }
    else if(momSum === -3) { bs -= 10; bsDetails.push("ALL timeframes DOWN - strong momentum alignment"); }
    else if(momSum > 0) { bs += 4; bsDetails.push("Momentum mostly UP ("+((momSum+3)/6*100).toFixed(0)+"% aligned)"); }
    else { bs -= 4; bsDetails.push("Momentum mostly DOWN"); }

    scores.breadthSentiment = Math.max(5, Math.min(95, Math.round(bs)));
    details.breadthSentiment = bsDetails;

    // ── VALIDATED COMPOSITE SCORE ────────────────────────────────────────────
    // Weights based on 20-session spot check results:
    // VIX direction: 100% win rate -> Order Flow boosted to 25%
    // MAG7 alignment: 100% win rate -> Order Flow boosted
    // Gap direction: 85% win rate -> Price Structure boosted to 20%
    // Oil direction: 71% win rate -> moderate weight
    // GEX regime: 78% validated by SpotGamma research -> 12%
    // VWAP at open: only 17% in recent sessions -> reduced in Inst Levels
    // Session/Time: negligible predictive value -> removed
    // VIX + OIL COMBINED BONUS - Backtest: 83.3% win rate
    // When both VIX direction AND oil direction agree = highest confidence signal
    // Increased from 3pts to 12pts based on validated 83% win rate
    var vixOilChg = (liveData.OIL.chgPct || 0);
    var vixDir = vixChg < -1.5 ? 1 : vixChg > 1.5 ? -1 : 0;
    var oilDir = vixOilChg > 2 ? -1 : vixOilChg < -2 ? 1 : 0;  // oil inverse NQ
    var vixMag7Bonus = 0;
    if(vixDir === 1 && oilDir === 1) {
      vixMag7Bonus = 12;  // VIX falling + oil falling = STRONG BULL - 83% validated
    } else if(vixDir === -1 && oilDir === -1) {
      vixMag7Bonus = -12; // VIX rising + oil rising = STRONG BEAR - 83% validated
    } else if(vixDir === 1 || oilDir === 1) {
      vixMag7Bonus = 4;   // One bullish signal
    } else if(vixDir === -1 || oilDir === -1) {
      vixMag7Bonus = -4;  // One bearish signal
    }

    var composite = Math.round(
      scores.priceStructure  * 0.20 +  // 85% gap, solid weekly pos
      scores.orderFlow       * 0.25 +  // 100% VIX + MAG7 = highest confidence
      scores.instLevels      * 0.12 +  // VWAP at open only 17% - reduced
      scores.correlation     * 0.10 +  // Cross-market, less validated
      scores.gammaExposure   * 0.12 +  // 78% SpotGamma validated
      scores.marketProfile   * 0.07 +  // Volume profile, moderate
      scores.breadthSentiment* 0.10 +  // COT + momentum + sentiment
      scores.newsMacro       * 0.04    // Context only, not predictive alone
    ) + vixMag7Bonus;

    // Data quality adjustment - reduce confidence when inputs are sparse
    var filledInputs = 0;
    var keyInputs = ["prevHigh","prevLow","prevClose","weekHigh","weekLow",
      "dxy","yield10","goldChg","gexRegime","gexFlip","vah","val","fearGreed"];
    keyInputs.forEach(function(k){ if(inputs[k] && inputs[k].length > 0 && inputs[k] !== "NONE") filledInputs++; });
    var dataQuality = filledInputs / keyInputs.length;
    // If less than 60% of key inputs filled, pull score toward neutral
    if(dataQuality < 0.6) {
      composite = Math.round(composite * dataQuality + 50 * (1 - dataQuality));
    }

    // ── CONVICTION LABEL ──────────────────────────────────────────────────────
    var conviction, convColor;
    if(composite >= 75) { conviction = "STRONG LONG"; convColor = "#00ff9f"; }
    else if(composite >= 65) { conviction = "LEAN LONG"; convColor = "#00e676"; }
    else if(composite >= 55) { conviction = "MILD LONG BIAS"; convColor = "#7ec8e3"; }
    else if(composite >= 45) { conviction = "NEUTRAL - WAIT"; convColor = "#fbbf24"; }
    else if(composite >= 35) { conviction = "MILD SHORT BIAS"; convColor = "#ff9f1c"; }
    else if(composite >= 25) { conviction = "LEAN SHORT"; convColor = "#ff6b35"; }
    else { conviction = "STRONG SHORT"; convColor = "#ff3d57"; }

    // ── TRADE RECOMMENDATION ──────────────────────────────────────────────────
    var recommendation = "";
    var recColor = "#555";
    if(composite >= 70 && activeKZ) {
      recommendation = "HIGH PROBABILITY LONG SETUP - Kill zone active, score "+composite+". Watch for ORB break above + VWAP + FVG entry.";
      recColor = "#00ff9f";
    } else if(composite <= 30 && activeKZ) {
      recommendation = "HIGH PROBABILITY SHORT SETUP - Kill zone active, score "+composite+". Watch for ORB break below + VWAP + FVG entry.";
      recColor = "#ff3d57";
    } else if(composite >= 65) {
      recommendation = "LONG BIAS - Wait for kill zone. Pre-position watch list: ORB high retest.";
      recColor = "#00e676";
    } else if(composite <= 35) {
      recommendation = "SHORT BIAS - Wait for kill zone. Pre-position watch list: ORB low retest.";
      recColor = "#ff6b35";
    } else {
      recommendation = "NEUTRAL - No clear edge. Sit on hands. Wait for kill zone + ORB confirmation.";
      recColor = "#fbbf24";
    }

    return {
      composite: composite,
      conviction: conviction,
      convColor: convColor,
      recommendation: recommendation,
      recColor: recColor,
      scores: scores,
      details: details,
      activeKZ: activeKZ,
      weekPos: weekPos,
      prevPos: prevPos,
      monthPos: monthPos,
      gap: gap,
      gapPct: gapPct,
      trend: ps > 50 ? "BULL" : "BEAR",
      dataPoints: 44
    };
  }
};


var TABS = [
  {id:"signal",  label:"SIGNAL",  color:"#a78bfa"},
  {id:"entry",   label:"ENTRY",   color:"#00ff9f"},
  {id:"live",    label:"LIVE",    color:"#00d4aa"},
  {id:"scalp",   label:"SCALP",   color:"#fbbf24"},
  {id:"orb",     label:"ORB",     color:"#ff6b35"},
  {id:"journal", label:"JOURNAL", color:"#00ff9f"},
  {id:"prices",  label:"PRICES",  color:"#fbdd74"},
  {id:"news",    label:"NEWS",    color:"#ff6b35"},
  {id:"charts",  label:"CHARTS",  color:"#00d4aa"},
  {id:"social",  label:"SOCIAL",  color:"#1d9bf0"}
];

function setMarket(m){
  activeMarket = m;
  mktInputs.activeMarket = m;
  renderMktSwitcher();
  if(state.tab === "signal") renderContent();
}

function renderMktSwitcher(){
  var el = document.getElementById("mktSwitcher");
  if(!el) return;
  el.innerHTML = Object.keys(marketState).map(function(m){
    var ms = marketState[m];
    var act = activeMarket === m;
    return '<button onclick="setMarket(\''+m+'\')" style="background:'+(act?ms.color+"22":"transparent")+';border:1px solid '+(act?ms.color+"55":"#111")+';color:'+(act?ms.color:"#444")+';padding:4px 10px;border-radius:4px;cursor:pointer;font-size:8px;font-family:monospace;font-weight:'+(act?"700":"400")+'">'+(act?"* ":"")+ms.emoji+" "+m+'</button>';
  }).join("");
}

// ── HELPERS ──────────────────────────────────────────────────────────────────
function c(color){ return color >= 0 ? "#00e676" : "#ff3d57"; }
function pct(v){ return (v>=0?"^":"")+Math.abs(v).toFixed(2)+"%" }
function green(v){ return v>=0?"#00e676":"#ff3d57"; }
function getOilAlert(){
  var chg = Math.abs(LIVE.OIL.chgPct||0);
  var dir = (LIVE.OIL.chgPct||0) >= 0 ? "up" : "down";
  if(chg>=2) return dir==="up"?{level:"SPIKE UP",color:"#ff3d57",action:"AVOID LONGS"}:{level:"SPIKE DOWN",color:"#00ff9f",action:"LEAN LONG"};
  if(chg>=1) return dir==="up"?{level:"MOVING UP",color:"#fbbf24",action:"TIGHTEN STOPS"}:{level:"MOVING DOWN",color:"#00d4aa",action:"MILD TAILWIND"};
  return {level:"QUIET",color:"#888",action:"IGNORE OIL"};
}
function calcEMA(data, period){
  if(data.length<period) return [];
  var k=2/(period+1), emas=[];
  var sum=data.slice(0,period).reduce(function(a,b){return a+b.close;},0);
  emas.push({i:period-1,v:sum/period});
  for(var i=period;i<data.length;i++) emas.push({i:i,v:data[i].close*k+emas[emas.length-1].v*(1-k)});
  return emas;
}
function calcVWAP(data){
  var ct=0,cv=0;
  return data.map(function(c){ct+=(c.high+c.low+c.close)/3*(c.volume||1);cv+=(c.volume||1);return ct/cv;});
}
function detectFVGs(data){
  var fvgs=[];
  for(var i=2;i<data.length;i++){
    var p=data[i-2],m=data[i-1],c=data[i];
    if(c.low>p.high) fvgs.push({type:"bull",top:c.low,bot:p.high,idx:i,filled:false});
    if(c.high<p.low) fvgs.push({type:"bear",top:p.low,bot:c.high,idx:i,filled:false});
  }
  fvgs.forEach(function(f){
    for(var j=f.idx+1;j<data.length;j++){
      if(f.type==="bull"&&data[j].low<=f.top){f.filled=true;break;}
      if(f.type==="bear"&&data[j].high>=f.bot){f.filled=true;break;}
    }
  });
  return fvgs.slice(-20);
}

// ── CLOCK ─────────────────────────────────────────────────────────────────────
function updateClock(){
  var now=new Date();
  var h=now.getUTCHours(), dow=now.getUTCDay();
  var isFriClose=dow===5&&h>=21, isSat=dow===6, isSunBefore=dow===0&&h<22;
  var isWknd=isFriClose||isSat||isSunBefore;
  var sess=isWknd?{n:"WEEKEND - CLOSED",c:"#ff3d57"}:h>=22||h<3?{n:"ASIA",c:"#fbdd74"}:h>=3&&h<9?{n:"LONDON",c:"#7ec8e3"}:{n:"NEW YORK",c:"#ff6b35"};
  var el=document.getElementById("sessLabel");
  if(el){el.textContent=sess.n;el.style.color=sess.c;}
  var te=document.getElementById("clockTime");
  if(te) te.textContent=now.toLocaleTimeString([],{hour:"2-digit",minute:"2-digit",second:"2-digit"});
  var de=document.getElementById("clockDate");
  if(de) de.textContent=now.toLocaleDateString([],{weekday:"short",month:"short",day:"numeric"});
  var age=(now-new Date("2026-05-15T08:00:00-04:00"))/3600000;
  var sb=document.getElementById("staleBar");
  if(sb) sb.style.display=age>6?"block":"none";
}

// ── MAG7 STRIP ────────────────────────────────────────────────────────────────
function renderMag7(){
  var html="";
  var wtd=0, tw=0;
  MAG7.forEach(function(sym){
    var q=LIVE[sym]; if(!q) return;
    var up=q.chgPct>=0;
    html+='<div class="mag7-card"><div class="mag7-sym" style="color:'+q.color+'">'+sym+'</div><div class="mag7-price">$'+q.price.toFixed(2)+'</div><div class="mag7-pct" style="color:'+(up?"#00e676":"#ff3d57")+'">'+(up?"^":"v")+Math.abs(q.chgPct).toFixed(1)+'%</div></div>';
    wtd+=q.chgPct*q.w; tw+=q.w;
  });
  var mc=document.getElementById("mag7Cards"); if(mc) mc.innerHTML=html;
  var wv=document.getElementById("wtdVal");
  if(wv){var w=wtd/tw;wv.textContent=(w>=0?"+":"")+w.toFixed(2)+"%";wv.style.color=w>=0?"#00e676":"#ff3d57";}
}

// ── TABS ──────────────────────────────────────────────────────────────────────
function renderTabs(){
  var html="";
  TABS.forEach(function(t){
    var act=state.tab===t.id;
    html+='<button class="tab-btn'+(act?" active":"")+'" style="--tc:'+t.color+';--tbg:'+t.color+'0a" onclick="setTab(\''+t.id+'\')">'+t.label+'</button>';
  });
  var tb=document.getElementById("tabBar"); if(tb) tb.innerHTML=html;
}
function setTab(id){ state.tab=id; renderTabs(); renderContent(); }

// ── RENDER CONTENT ────────────────────────────────────────────────────────────
function renderContent(){
  var el=document.getElementById("content"); if(!el) return;
  if(state.tab==="signal") el.innerHTML=renderSignal();
  else if(state.tab==="entry") el.innerHTML=renderEntry();
  else if(state.tab==="live") el.innerHTML=renderLive();
  else if(state.tab==="scalp") el.innerHTML=renderScalp();
  else if(state.tab==="orb") el.innerHTML=renderORB();
  else if(state.tab==="journal") el.innerHTML=renderJournal();
  else if(state.tab==="prices") el.innerHTML=renderPrices();
  else if(state.tab==="news") el.innerHTML=renderNews();
  else if(state.tab==="charts") el.innerHTML=renderCharts();
  else if(state.tab==="social") el.innerHTML=renderSocial();
  attachHandlers();
}


// ── ENTRY MODEL TAB ───────────────────────────────────────────────────────────
function renderEntry(){
  var steps = [
    {
      num:"01", time:"PRE-MARKET", color:"#a78bfa",
      title:"WARROOM BRIEF",
      items:[
        "Check SIGNAL tab - bias and composite score",
        "Check oil alert - SPIKE UP = avoid longs",
        "Check VIX - above 25 = skip session entirely",
        "Check NEWS tab - any CPI/PPI/Fed today?",
        "Check SOCIAL tab - @realDonaldTrump last 15 min",
        "Set your target and stop BEFORE open - write it down"
      ],
      rule:"If VIX > 25 or major data release in next 30 min = NO TRADING",
      ruleColor:"#ff3d57"
    },
    {
      num:"02", time:"9:30-9:35 AM ET", color:"#fbbf24",
      title:"WATCH - DO NOTHING",
      items:[
        "Do NOT enter any trade during this candle",
        "Watch the 5-min candle form on your platform",
        "Note if price is above or below VWAP",
        "Feel the energy - aggressive or choppy?",
        "Note the opening range developing"
      ],
      rule:"HANDS OFF THE KEYBOARD - observation only",
      ruleColor:"#fbbf24"
    },
    {
      num:"03", time:"9:35 AM ET", color:"#ff6b35",
      title:"MARK ORB LEVELS",
      items:[
        "5-min candle closes - immediately mark High and Low",
        "Enter ORB High and Low into ORB tab in warroom",
        "Levels and targets calculate automatically",
        "Note range size - less than 30 pts = skip session",
        "Note VWAP position relative to ORB"
      ],
      rule:"ORB range under 30 pts = choppy day = NO TRADING",
      ruleColor:"#fbbf24"
    },
    {
      num:"04", time:"9:35-9:50 AM ET", color:"#00d4aa",
      title:"VWAP FILTER - QUALIFY THE TRADE",
      items:[
        "ORB breaks UP + price ABOVE VWAP = LONG bias confirmed",
        "ORB breaks UP + price BELOW VWAP = SKIP - fighting VWAP",
        "ORB breaks DOWN + price BELOW VWAP = SHORT bias confirmed",
        "ORB breaks DOWN + price ABOVE VWAP = SKIP - fighting VWAP",
        "Wait for candle BODY to close beyond ORB - wicks dont count"
      ],
      rule:"VWAP must be on same side as your trade - no exceptions",
      ruleColor:"#00d4aa"
    },
    {
      num:"05", time:"RETEST", color:"#00ff9f",
      title:"ENTRY TRIGGER - 30s CHART",
      items:[
        "Drop to 30-second chart after ORB breakout confirmed",
        "Wait for price to RETEST the ORB boundary it just broke",
        "At retest - look for 3-candle FVG forming at ORB level",
        "FVG = gap between candle 1 high and candle 3 low (bullish)",
        "Enter on FVG fill - not before - this is your trigger",
        "Stop just beyond ORB boundary (20-25 ticks)"
      ],
      rule:"No FVG at retest = no trade - wait for next setup",
      ruleColor:"#00ff9f"
    },
    {
      num:"06", time:"IN TRADE", color:"#00ff9f",
      title:"TRADE MANAGEMENT",
      items:[
        "5 contracts enter - never add more",
        "At T1 (0.5x range) - close 3 contracts, move stop to breakeven",
        "At T2 (1x range) - close remaining 2 contracts",
        "If stop hits - DONE FOR DAY - platform closes immediately",
        "Maximum 2 trades per day - win or lose",
        "Daily stop loss $400 - if hit, done for day"
      ],
      rule:"ONE STOP HIT = DONE FOR DAY - no revenge, no exceptions",
      ruleColor:"#ff3d57"
    }
  ];

  var disqualifiers = [
    ["VIX ABOVE 25", "Skip entire session - too volatile for scalping"],
    ["OIL SPIKE UP alert", "Avoid longs - NQ headwind. Short only with confirmation"],
    ["CPI/PPI/Fed day", "Wait until AFTER print - never trade into data"],
    ["Trump tweet in last 15 min", "Wait 2 full candles before entering"],
    ["ORB range under 30 pts", "Too tight - no momentum, skip session"],
    ["First candle massive spike", "Too volatile - wait for range to develop"],
    ["Already hit daily $400 loss", "Done for day - close platform"],
    ["Already took 2 trades today", "Done for day - regardless of outcome"]
  ];

  var vwapRules = [
    ["LONG SETUP", "ORB breaks UP", "Price ABOVE VWAP", "#00ff9f", "TAKE IT"],
    ["LONG SKIP", "ORB breaks UP", "Price BELOW VWAP", "#ff3d57", "SKIP IT"],
    ["SHORT SETUP", "ORB breaks DOWN", "Price BELOW VWAP", "#00ff9f", "TAKE IT"],
    ["SHORT SKIP", "ORB breaks DOWN", "Price ABOVE VWAP", "#ff3d57", "SKIP IT"]
  ];

  var stepHtml = steps.map(function(s){
    var items = s.items.map(function(i){
      return '<div style="display:flex;gap:6px;padding:3px 0;border-bottom:1px solid #0d0d0d"><span style="color:'+s.color+';font-size:9px;flex-shrink:0">></span><span style="font-size:9px;color:#666;line-height:1.4">'+i+'</span></div>';
    }).join('');
    return '<div style="background:#070707;border:1px solid #111;border-left:3px solid '+s.color+';border-radius:5px;padding:10px 12px;margin-bottom:8px">'
      +'<div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:6px">'
      +'<div style="display:flex;gap:8px;align-items:center">'
      +'<span style="font-size:16px;color:'+s.color+';font-weight:700;font-family:monospace">'+s.num+'</span>'
      +'<div><div style="font-size:10px;color:'+s.color+';font-weight:700">'+s.title+'</div>'
      +'<div style="font-size:7px;color:#333">'+s.time+'</div></div>'
      +'</div></div>'
      +items
      +'<div style="margin-top:6px;background:'+s.ruleColor+'11;border:1px solid '+s.ruleColor+'33;border-radius:3px;padding:4px 8px">'
      +'<span style="font-size:8px;color:'+s.ruleColor+';font-weight:700">! RULE: '+s.rule+'</span>'
      +'</div></div>';
  }).join('');

  var vwapHtml = '<div style="background:#070707;border:1px solid #00d4aa22;border-radius:5px;padding:10px;margin-bottom:8px">'
    +'<div style="font-size:8px;color:#00d4aa;font-weight:700;letter-spacing:1px;margin-bottom:8px">VWAP FILTER - THE ONE RULE THAT SAVES ACCOUNTS</div>'
    +vwapRules.map(function(r){
      return '<div style="display:flex;justify-content:space-between;align-items:center;padding:5px 0;border-bottom:1px solid #0d0d0d">'
        +'<div style="display:flex;gap:6px;align-items:center">'
        +'<span style="font-size:7px;color:#333;min-width:70px">'+r[0]+'</span>'
        +'<span style="font-size:8px;color:#aaa">'+r[1]+'</span>'
        +'<span style="font-size:7px;color:#333">+</span>'
        +'<span style="font-size:8px;color:#aaa">'+r[2]+'</span>'
        +'</div>'
        +'<span style="font-size:9px;color:'+r[3]+';font-weight:700;border:1px solid '+r[3]+'44;border-radius:2px;padding:1px 6px">'+r[4]+'</span>'
        +'</div>';
    }).join('')
    +'</div>';

  var dqHtml = '<div style="background:#ff3d5708;border:1px solid #ff3d5722;border-radius:5px;padding:10px;margin-bottom:8px">'
    +'<div style="font-size:8px;color:#ff3d57;font-weight:700;letter-spacing:1px;margin-bottom:6px">[X] DISQUALIFIERS - ANY OF THESE = NO TRADE</div>'
    +disqualifiers.map(function(d){
      return '<div style="display:flex;gap:8px;padding:4px 0;border-bottom:1px solid #1a1a1a">'
        +'<span style="font-size:8px;color:#ff3d57;font-weight:700;min-width:140px;flex-shrink:0">'+d[0]+'</span>'
        +'<span style="font-size:8px;color:#444;line-height:1.4">'+d[1]+'</span>'
        +'</div>';
    }).join('')
    +'</div>';

  var rulesHtml = '<div style="background:#00ff9f08;border:1px solid #00ff9f22;border-radius:5px;padding:10px;margin-bottom:8px">'
    +'<div style="font-size:8px;color:#00ff9f;font-weight:700;letter-spacing:1px;margin-bottom:6px">YOUR DAILY RULES - READ EVERY MORNING</div>'
    +['5 CONTRACTS MAXIMUM - never add, never increase',
      '2 TRADES PER DAY - win or lose, done after 2',
      '$400 DAILY STOP LOSS - if hit, platform closes',
      'ONE STOP HIT = DONE FOR DAY - no revenge ever',
      'NO TRADING INTO DATA - CPI, PPI, Fed = wait for print',
      'CHECK WARROOM BEFORE EVERY SINGLE ENTRY'].map(function(r, i){
      return '<div style="display:flex;gap:8px;padding:4px 0;border-bottom:1px solid #0d0d0d;align-items:center">'
        +'<span style="font-size:10px;color:#00ff9f;font-weight:700;flex-shrink:0">'+(i+1)+'.</span>'
        +'<span style="font-size:9px;color:#777;font-weight:700">'+r+'</span>'
        +'</div>';
    }).join('')
    +'</div>';

  return '<div style="font-family:monospace">'
    +'<div style="font-size:9px;color:#00ff9f;font-weight:700;letter-spacing:1px;margin-bottom:2px">ENTRY MODEL - ORB + VWAP + FVG</div>'
    +'<div style="font-size:8px;color:#333;margin-bottom:10px">5-min ORB . VWAP filter . 30s FVG entry . 5 contracts max</div>'
    +rulesHtml
    +vwapHtml
    +stepHtml
    +dqHtml
    +'</div>';
}

// ── SIGNAL TAB ────────────────────────────────────────────────────────────────
// Manual inputs state
var mktInputs = {
  // ── PRE-FILLED BY WARROOM - Updated May 15 2026 EOD ──
  // All data sourced from Yahoo Finance, TradingEconomics, Barchart

  // PRICE STRUCTURE - MNQ
  prevHigh:     "29733",   // Fri May 15 session high
  prevLow:      "29090",   // Fri May 15 session low
  prevClose:    "29232",   // Fri May 15 close -1.54%
  weekHigh:     "29734",   // Week of May 11-15 high (Thu ATH)
  weekLow:      "28861",   // Week of May 11-15 low (Mon CPI dump)
  prevWeekHigh: "29456",   // Week of May 4-8 high
  prevWeekLow:  "28500",   // Week of May 4-8 low
  prevWeekOpen: "28700",   // Week of May 4-8 Monday open
  monthHigh:    "29734",   // May 2026 high so far
  monthLow:     "28700",   // May 2026 low so far
  monthOpen:    "29333",   // May 1 open
  ma50:         "28400",   // Approximate 50-day MA
  ma200:        "26800",   // Approximate 200-day MA
  ath:          "29734",   // All time high (set Thu May 14)
  day1High:     "29500",   // Thu May 14 high (ATH session)
  day1Low:      "29050",   // Thu May 14 low
  day2High:     "29456",   // Wed May 13 high
  day2Low:      "29100",   // Wed May 13 low

  // ORDER FLOW & INTERNALS
  dxy:          "99.27",   // DXY Fri close - dollar strengthening
  dxyPrev:      "98.87",   // DXY Thu close
  yield10:      "4.60",    // 10Y yield Fri - rose 10bps to 1Y high
  yield10Prev:  "4.50",    // 10Y yield Thu
  pcr:          "0.92",    // Put/call ratio - mild fear
  volRatio:     "1.4",     // Volume above average on selloff

  // CORRELATION
  goldChg:      "-3.02",   // Gold MASSIVE selloff Fri -3.02%
  jpyChg:       "-0.50",   // USD/JPY up = yen weakening = risk off BUT dollar bid
  eurChg:       "-0.40",   // EUR/USD down = dollar strengthening
  goldPrice:    "4544",    // Gold $4,544 after -3% selloff
  jpyPrice:     "145.20",  // USD/JPY 145.20
  eurPrice:     "1.1180",  // EUR/USD 1.1180
  techVsDefensive: "-0.8", // Tech underperforming defensives on fear day
  crossAlign:   "-0.6",    // Most markets aligned bearish Friday

  // INSTITUTIONAL LEVELS
  fvgPresent: "YES",        // FVG left from Thu dump on Friday
  fvgDir:     "BEAR",       // Bearish FVG - unfilled gap from selloff
  mss:        "NONE",       // No confirmed market structure shift yet

  // NEWS & MACRO
  dataToday:    "NONE",     // No major data Monday May 18
  fedDays:      "21",       // Next FOMC ~June 17-18
  geopolScore:  "25",       // Low - oil +3%, no Iran deal, yields rising
  earningsDays: "99",       // Next major earnings TBD
  opexDays:     "4",        // Monthly OpEx was Friday - now rolling forward
  cbSpeech:     "NONE",     // No CB speech Monday
  newsAgeHours: "0",        // Just updated

  goldPrice:    "4544",
  jpyPrice:     "145.20",
  eurPrice:     "1.1180",

  // ── GAMMA EXPOSURE - Pre-filled from SpotGamma/GEXmetrix research
  // Post-OpEx Friday = gamma unpin = negative gamma, amplified moves
  gexRegime:    "NEGATIVE",  // Post-OpEx = gamma unpin = trending/amplified
  gexFlip:      "29400",     // Key flip level - above=stabilize, below=amplify
  callWall:     "29750",     // Call wall from Thu ATH session
  putWall:      "28500",     // Put wall = strong institutional floor
  gexMagnitude: "MODERATE",  // Post-OpEx moderate - fresh gamma building
  zerodte:      "LOW",       // Post-OpEx 0DTE mostly expired - rebuilding

  // ── MARKET PROFILE - Pre-filled from weekly volume analysis
  vah:          "29500",     // Value Area High - Thu ATH week
  val:          "29050",     // Value Area Low - where volume concentrated
  poc:          "29250",     // Point of Control - highest volume node this week
  vaPosition:   "BELOW",     // Friday close 29,232 below VAL = bearish

  // ── COT POSITIONING - Pre-filled from CFTC Friday report
  cotPosition:  "LONG",      // Large specs still net long NQ
  cotTrend:     "DECREASING",// Net longs being trimmed post-CPI + summit

  // ── MULTI-TIMEFRAME MOMENTUM - Pre-filled
  mom5d:        "DOWN",      // 5-day: Mon CPI dump, Thu ATH, Fri selloff = mixed but down net
  mom20d:       "UP",        // 20-day: strong uptrend intact from April lows
  mom60d:       "UP",        // 60-day: major bull trend from March lows

  // ── VOLATILITY STRUCTURE - Pre-filled
  vixVix3m:     "NORMAL",    // VIX 18.43 vs VIX3M ~20 = normal contango
  vvix:         "98",        // VVIX elevated - fear of volatility rising

  // ── MARKET BREADTH - Pre-filled
  adRatio:      "0.55",      // Friday breadth weak - broad selloff
  pctAbove50ma: "61",        // Still majority above 50MA despite pullback
  hiLoRatio:    "0.65",      // More new highs than lows but ratio narrowing

  // ── SENTIMENT - Pre-filled
  fearGreed:    "32",        // CNN Fear & Greed - Fear territory post-CPI
  aaiiSentiment:"BEARISH",   // Retail bearish after rate hike fears return

  // ── DARK POOL / FLOW - Pre-filled
  darkPoolBias: "NEUTRAL",   // Dark pool neutral - institutional not showing hand
  unusualOptions:"PUTS",     // Unusual put buying Friday on NQ pullback

  // Market open (9:30 AM ET only - leave blank)
  todayOpen: "",
  activeMarket: "MNQ",
  loaded: true
};

// Multi-market state
var marketState = {
  MNQ: { name:"MNQ FUTURES", color:"#00ff9f", emoji:"NQ" },
  GOLD:{ name:"GOLD XAU/USD", color:"#fbbf24", emoji:"AU" },
  JPY: { name:"JPY/USD",      color:"#7ec8e3", emoji:"JP" },
  EUR: { name:"EUR/USD",      color:"#a78bfa", emoji:"EU" }
};
var activeMarket = "MNQ";

function calcInstitutional(){
  return SIGNAL_ENGINE.calculate(mktInputs, activeMarket, LIVE, SIGNAL);
}



var _morningBriefCache = null;
var _morningBriefInputsHash = "";

function getMorningBriefHTML(){
  var hash = JSON.stringify(mktInputs);
  if(_morningBriefCache && hash === _morningBriefInputsHash) return _morningBriefCache;
  _morningBriefInputsHash = hash;

  var totalFields = 67;
  var filledCount = 0;
  var allKeys = ["prevHigh","prevLow","prevClose","weekHigh","weekLow","prevWeekHigh","prevWeekLow",
    "prevWeekOpen","monthHigh","monthLow","monthOpen","ma50","ma200","ath",
    "day1High","day1Low","day2High","day2Low","dxy","dxyPrev","yield10","yield10Prev",
    "pcr","volRatio","goldChg","jpyChg","eurChg","goldPrice","jpyPrice","eurPrice",
    "techVsDefensive","crossAlign","fvgPresent","fvgDir","mss","dataToday","fedDays",
    "geopolScore","earningsDays","opexDays","cbSpeech","newsAgeHours"];
  allKeys.forEach(function(k){
    if(mktInputs[k] && mktInputs[k].length > 0 && mktInputs[k] !== "NONE" && mktInputs[k] !== "NO") filledCount++;
  });
  var completePct = Math.round(filledCount/totalFields*100);
  var barColor = completePct>70?"#00ff9f":completePct>40?"#fbbf24":"#ff3d57";

  var statusDots=["prevHigh:PDH","prevLow:PDL","prevClose:PDC","weekHigh:WKH","weekLow:WKL",
    "prevWeekHigh:PWH","ma50:50M","ma200:200M","dxy:DXY","yield10:10Y",
    "goldChg:GLD","jpyChg:JPY","eurChg:EUR","todayOpen:OPEN"
  ].map(function(item){
    var parts = item.split(":");
    var filled = mktInputs[parts[0]] && mktInputs[parts[0]].length > 0;
    return "<span style='margin-right:4px;font-size:7px;color:"+(filled?"#00ff9f":"#1a1a1a")+"'>"+(filled?"v":"x")+" "+parts[1]+"</span>";
  }).join("");

  var html = "<div style='background:#0a0a0a;border:1px solid #00ff9f22;border-radius:6px;padding:10px;margin-bottom:10px'>"
    + "<div style='display:flex;justify-content:space-between;align-items:center;margin-bottom:4px'>"
    + "<div><div style='font-size:9px;color:#00ff9f;font-weight:700;letter-spacing:1px'>INSTITUTIONAL MORNING BRIEF</div>"
    + "<div style='font-size:7px;color:#333'>44 data points . enter pre-market . signal updates instantly</div></div>"
    + "<div style='text-align:right'><div style='font-size:14px;color:"+barColor+";font-weight:700'>"+completePct+"%</div>"
    + "<div style='font-size:7px;color:#333'>"+filledCount+"/44</div></div></div>"
    + "<div style='height:3px;background:#111;border-radius:2px;margin-bottom:6px;overflow:hidden'>"
    + "<div style='height:100%;width:"+completePct+"%;background:"+barColor+";transition:width 0.3s'></div></div>"
    + "<div style='margin-bottom:6px'>"+statusDots+"</div>";

  // Section 1: Price Structure
  html += buildInputGroup("PRICE STRUCTURE", "#00ff9f", "Barchart/TradingView daily+weekly charts", [
    ["prevHigh","PREV DAY HIGH","e.g. 29500"],
    ["prevLow","PREV DAY LOW","e.g. 28980"],
    ["prevClose","PREV CLOSE","e.g. 29420"],
    ["weekHigh","WEEK HIGH","e.g. 29500"],
    ["weekLow","WEEK LOW","e.g. 28700"],
    ["prevWeekHigh","PREV WK HIGH","e.g. 29456"],
    ["prevWeekLow","PREV WK LOW","e.g. 28500"],
    ["prevWeekOpen","PREV WK OPEN","e.g. 29000"],
    ["monthHigh","MONTH HIGH","e.g. 29650"],
    ["monthLow","MONTH LOW","e.g. 28200"],
    ["monthOpen","MONTH OPEN","e.g. 29100"],
    ["ma50","50-DAY MA","e.g. 28800"],
    ["ma200","200-DAY MA","e.g. 27500"],
    ["ath","ALL TIME HIGH","e.g. 29650"],
    ["day1High","2D AGO HIGH","e.g. 29456"],
    ["day1Low","2D AGO LOW","e.g. 28861"],
    ["day2High","3D AGO HIGH","e.g. 29420"],
    ["day2Low","3D AGO LOW","e.g. 28700"]
  ], 0);

  // Section 2: Order Flow
  html += buildInputGroup("ORDER FLOW & INTERNALS", "#7ec8e3", "CNBC, TradingView, finviz.com", [
    ["dxy","DXY TODAY","e.g. 104.20"],
    ["dxyPrev","DXY YESTERDAY","e.g. 103.90"],
    ["yield10","10Y YIELD","e.g. 4.52"],
    ["yield10Prev","10Y YIELD PREV","e.g. 4.48"],
    ["pcr","PUT/CALL RATIO","e.g. 0.85"],
    ["volRatio","VOL VS AVG","e.g. 1.2"]
  ], 1);

  // Section 3: Correlation
  html += buildInputGroup("CORRELATION", "#a78bfa", "Your broker or TradingView", [
    ["goldChg","GOLD % CHG","e.g. 0.8"],
    ["jpyChg","JPY/USD % CHG","e.g. -0.3"],
    ["eurChg","EUR/USD % CHG","e.g. 0.2"],
    ["goldPrice","GOLD PRICE","e.g. 3285"],
    ["jpyPrice","JPY/USD","e.g. 0.00685"],
    ["eurPrice","EUR/USD","e.g. 1.0850"],
    ["techVsDefensive","TECH VS DEF","e.g. 1.5"],
    ["crossAlign","CROSS ALIGN","e.g. 0.7"]
  ], 2);

  // Section 4: Institutional Levels
  html += buildInputGroup("INSTITUTIONAL LEVELS", "#ff6b35", "Mark on your chart each morning", [
    ["fvgPresent","FVG PRESENT","YES or NO"],
    ["fvgDir","FVG DIRECTION","BULL/BEAR/NONE"],
    ["mss","MKT STRUCTURE","BULL/BEAR/NONE"]
  ], 3);

  // Section 5: News & Macro
  html += buildInputGroup("NEWS & MACRO", "#ff3d57", "investing.com/economic-calendar", [
    ["dataToday","DATA TODAY","CPI/PPI/JOBS/NONE"],
    ["fedDays","DAYS TO FED","e.g. 21"],
    ["geopolScore","GEOPOL SCORE","0-100 (50=neutral)"],
    ["earningsDays","DAYS TO EARN","e.g. 3"],
    ["opexDays","DAYS TO OPEX","e.g. 7"],
    ["cbSpeech","CB SPEECH","FED/BOJ/ECB/NONE"],
    ["newsAgeHours","NEWS AGE HRS","e.g. 8"]
  ], 4);

  // Section 6: Gamma Exposure (GEX) - INSTITUTIONAL EDGE
  html += buildInputGroup("GAMMA EXPOSURE - DEALER POSITIONING", "#ff6b35", "SpotGamma.com / MenthorQ.com / GEXmetrix.com (free tier)", [
    ["gexRegime",   "GEX REGIME",    "POSITIVE or NEGATIVE"],
    ["gexFlip",     "GEX FLIP LEVEL","e.g. 29400"],
    ["callWall",    "CALL WALL",     "e.g. 29500"],
    ["putWall",     "PUT WALL",      "e.g. 28500"],
    ["gexMagnitude","GEX MAGNITUDE", "STRONG/MODERATE/WEAK"],
    ["zerodte",     "0DTE LEVEL",    "EXTREME/HIGH/NORMAL/LOW"]
  ], 5);

  // Section 7: Market Profile
  html += buildInputGroup("MARKET PROFILE - VOLUME NODES", "#00d4aa", "TradingView Volume Profile indicator (free)", [
    ["vah",       "VALUE AREA HIGH","e.g. 29450"],
    ["val",       "VALUE AREA LOW", "e.g. 28950"],
    ["poc",       "POINT OF CTRL",  "e.g. 29200"],
    ["vaPosition","VA POSITION",    "INSIDE/ABOVE/BELOW"]
  ], 6);

  // Section 8: Breadth, Sentiment & COT
  html += buildInputGroup("BREADTH + SENTIMENT + COT", "#a78bfa", "finviz.com | money.cnn.com/fear-greed | aaii.com | barchart.com/cot", [
    ["fearGreed",    "FEAR & GREED",  "0-100 (CNN Money)"],
    ["adRatio",      "ADVANCE/DECLINE","e.g. 0.8"],
    ["pctAbove50ma", "% ABOVE 50MA",  "e.g. 62"],
    ["hiLoRatio",    "HIGH/LOW RATIO","e.g. 0.7"],
    ["aaiiSentiment","AAII SENTIMENT","BULLISH/BEARISH/NEUTRAL"],
    ["cotPosition",  "COT POSITION",  "LONG/SHORT/NEUTRAL"],
    ["cotTrend",     "COT TREND",     "INCREASING/DECREASING"],
    ["mom5d",        "5D MOMENTUM",   "UP or DOWN"],
    ["mom20d",       "20D MOMENTUM",  "UP or DOWN"],
    ["mom60d",       "60D MOMENTUM",  "UP or DOWN"],
    ["vixVix3m",     "VIX TERM STRUCT","NORMAL or INVERTED"],
    ["vvix",         "VVIX",          "e.g. 95"],
    ["darkPoolBias", "DARK POOL BIAS","BULLISH/BEARISH/NEUTRAL"],
    ["unusualOptions","UNUSUAL OPT",  "CALLS/PUTS/NONE"]
  ], 7);

  // Today open
  html += "<div style='background:#00d4aa08;border:1px solid #00d4aa33;border-radius:4px;padding:6px 8px;margin-top:6px;margin-bottom:8px'>"
    + "<div style='display:flex;justify-content:space-between;margin-bottom:4px'>"
    + "<span style='font-size:8px;color:#00d4aa;font-weight:700'>TODAY OPEN - ENTER AT 9:30 AM ET ONLY</span>"
    + (mktInputs.todayOpen ? "<span style='font-size:7px;color:#00ff9f;font-weight:700'>v SET</span>" : "<span style='font-size:7px;color:#fbbf24;font-weight:700'>! WAIT FOR OPEN</span>")
    + "</div>"
    + "<input value=\"" + (mktInputs.todayOpen||"") + "\" placeholder=\"First print at 9:30 AM ET\" "
    + "style=\"width:100%;background:#111;border:1px solid #00d4aa33;color:#00d4aa;padding:6px;border-radius:3px;font-size:11px;font-family:monospace;font-weight:700\" "
    + "oninput=\"mktInputs.todayOpen=this.value;updateSignalMeter()\"/></div>";

  html += "<button onclick='updateSignalMeter()' style='width:100%;background:#00ff9f11;border:1px solid #00ff9f33;color:#00ff9f;padding:7px 0;border-radius:3px;cursor:pointer;font-size:9px;font-family:monospace;font-weight:700;letter-spacing:1px'>UPDATE SIGNAL METER ("+filledCount+"/44 inputs)</button>";
  html += "</div>";

  _morningBriefCache = html;
  return html;
}

function buildInputGroup(label, color, note, fields, idx){
  var html = "<div style='margin-bottom:5px'>"
    + "<div onclick='toggleSection("+idx+")' style='display:flex;justify-content:space-between;align-items:center;padding:5px 8px;background:#080808;border:1px solid "+color+"33;border-radius:4px;cursor:pointer;margin-bottom:3px'>"
    + "<div><span style='font-size:8px;color:"+color+";font-weight:700'>"+label+"</span>"
    + "<span style='font-size:7px;color:#333;margin-left:6px'>"+note+"</span></div>"
    + "<span style='font-size:7px;color:"+color+"' id='secToggle"+idx+"'>v</span></div>"
    + "<div id='secBody"+idx+"' style='display:grid;grid-template-columns:repeat(3,1fr);gap:3px'>";
  fields.forEach(function(fi){
    var val = mktInputs[fi[0]]||"";
    var filled = val.length > 0 && val !== "NONE" && val !== "NO";
    html += "<div style='background:#080808;border:1px solid "+(filled?color+"44":"#0d0d0d")+";border-radius:3px;padding:4px 5px'>"
      + "<div style='font-size:6.5px;color:"+(filled?color:"#333")+";font-weight:700;margin-bottom:2px'>"+fi[1]+"</div>"
      + "<input value=\""+val+"\" placeholder=\""+fi[2]+"\" "
      + "style=\"width:100%;background:#0d0d0d;border:none;color:"+color+";padding:3px;border-radius:2px;font-size:9px;font-family:monospace;font-weight:700\" "
      + "oninput=\"mktInputs."+fi[0]+"=this.value;_morningBriefCache=null;updateSignalMeter()\"/></div>";
  });
  html += "</div></div>";
  return html;
}

function renderSignal(){
  var inst=calcInstitutional();
  var pct2=Math.max(5,Math.min(95,inst.composite));
  var col=pct2>=62?"#00ff9f":pct2<=38?"#ff3d57":"#fbbf24";
  var now=new Date(); var h=now.getUTCHours(); var dow=now.getUTCDay();
  var isWknd=(dow===5&&h>=21)||dow===6||(dow===0&&h<22);

  // Session clock
  var sessHtml="";
  if(isWknd){
    sessHtml='<div class="card-sm"><div class="lbl">SESSION CLOCK</div><div style="background:#ff3d5722;border:1px solid #ff3d5555;border-radius:3px;padding:3px 8px;display:inline-block"><span style="font-size:8px;color:#ff3d57;font-weight:700">[||] MARKETS CLOSED</span></div></div>';
  } else {
    var sessions=[{name:"ASIA OPEN",utcH:19},{name:"LONDON OPEN",utcH:3},{name:"NY OPEN",utcH:13,utcM:30},{name:"NY CLOSE",utcH:20}];
    var nowMin=h*60+now.getUTCMinutes();
    var upcoming=sessions.map(function(s){var sm=(s.utcH||0)*60+(s.utcM||0);var d=sm-nowMin;if(d<-120)d+=1440;return{name:s.name,diff:d};}).filter(function(s){return s.diff>=0;}).slice(0,3);
    sessHtml='<div class="card-sm"><div class="lbl">SESSION CLOCK</div><div style="display:flex;gap:8px;flex-wrap:wrap;align-items:center">';
    upcoming.forEach(function(u){sessHtml+='<span style="font-size:7px;color:#555">'+u.name+'</span><span style="font-size:9px;color:#fbbf24;font-weight:700">in '+(u.diff<60?u.diff+"m":Math.floor(u.diff/60)+"h "+u.diff%60+"m")+'</span>';});
    sessHtml+='</div></div>';
  }

  // Oil alert
  var oilAlert=getOilAlert();
  var oilHtml="";
  if(Math.abs(LIVE.OIL.chgPct||0)>=1){
    oilHtml='<div style="background:'+oilAlert.color+'11;border:1px solid '+oilAlert.color+'44;border-radius:5px;padding:8px 10px;margin-bottom:8px"><div style="display:flex;justify-content:space-between;align-items:center"><span style="font-size:9px;color:'+oilAlert.color+';font-weight:700">OIL ALERT: '+oilAlert.level+' - $'+LIVE.OIL.price+' ('+pct(LIVE.OIL.chgPct)+')</span><span style="font-size:8px;color:'+oilAlert.color+';border:1px solid '+oilAlert.color+'44;border-radius:2px;padding:0 5px;font-weight:700">'+oilAlert.action+'</span></div></div>';
  }

  // Morning brief inputs - split by availability
  // ── ALL 44 DATA POINT INPUTS ───────────────────────────────────────────────
  // Organized into sections - all pre-market except today open

  var inputSections = [
    {
      label: "PRICE STRUCTURE",
      color: "#00ff9f",
      avail: "NOW",
      note: "From Barchart or TradingView daily/weekly charts",
      fields: [
        {id:"prevHigh",     label:"PREV DAY HIGH",    ph:"e.g. 29500",   tip:"Yesterday high"},
        {id:"prevLow",      label:"PREV DAY LOW",     ph:"e.g. 28980",   tip:"Yesterday low"},
        {id:"prevClose",    label:"PREV DAY CLOSE",   ph:"e.g. 29420",   tip:"Yesterday 5PM ET close"},
        {id:"weekHigh",     label:"WEEK HIGH",        ph:"e.g. 29500",   tip:"This week high so far"},
        {id:"weekLow",      label:"WEEK LOW",         ph:"e.g. 28700",   tip:"This week low so far"},
        {id:"prevWeekHigh", label:"PREV WEEK HIGH",   ph:"e.g. 29456",   tip:"Last week high"},
        {id:"prevWeekLow",  label:"PREV WEEK LOW",    ph:"e.g. 28500",   tip:"Last week low"},
        {id:"prevWeekOpen", label:"PREV WEEK OPEN",   ph:"e.g. 29000",   tip:"Last Monday open"},
        {id:"monthHigh",    label:"MONTH HIGH",       ph:"e.g. 29650",   tip:"This month high"},
        {id:"monthLow",     label:"MONTH LOW",        ph:"e.g. 28200",   tip:"This month low"},
        {id:"monthOpen",    label:"MONTH OPEN",       ph:"e.g. 29100",   tip:"First day of month open"},
        {id:"ma50",         label:"50-DAY MA",        ph:"e.g. 28800",   tip:"50-day moving average"},
        {id:"ma200",        label:"200-DAY MA",       ph:"e.g. 27500",   tip:"200-day moving average"},
        {id:"ath",          label:"ALL TIME HIGH",    ph:"e.g. 29650",   tip:"All time high price"},
        {id:"day1High",     label:"2 DAYS AGO HIGH",  ph:"e.g. 29456",   tip:"High from 2 sessions ago"},
        {id:"day1Low",      label:"2 DAYS AGO LOW",   ph:"e.g. 28861",   tip:"Low from 2 sessions ago"},
        {id:"day2High",     label:"3 DAYS AGO HIGH",  ph:"e.g. 29420",   tip:"High from 3 sessions ago"},
        {id:"day2Low",      label:"3 DAYS AGO LOW",   ph:"e.g. 28700",   tip:"Low from 3 sessions ago"}
      ]
    },
    {
      label: "ORDER FLOW & MARKET INTERNALS",
      color: "#7ec8e3",
      avail: "NOW",
      note: "From CNBC, TradingView, finviz.com/forex.html",
      fields: [
        {id:"dxy",              label:"DXY TODAY",        ph:"e.g. 104.20",  tip:"Dollar index current"},
        {id:"dxyPrev",          label:"DXY YESTERDAY",    ph:"e.g. 103.90",  tip:"Dollar index yesterday"},
        {id:"yield10",          label:"10Y YIELD TODAY",  ph:"e.g. 4.52",    tip:"US 10-year yield now"},
        {id:"yield10Prev",      label:"10Y YIELD PREV",   ph:"e.g. 4.48",    tip:"10-year yield yesterday"},
        {id:"pcr",              label:"PUT/CALL RATIO",   ph:"e.g. 0.85",    tip:"Options PCR - cboe.com"},
        {id:"volRatio",         label:"VOLUME VS AVG",    ph:"e.g. 1.2",     tip:"Today vol vs 20-day avg"}
      ]
    },
    {
      label: "CORRELATION INTELLIGENCE",
      color: "#a78bfa",
      avail: "NOW",
      note: "Cross-market moves - TradingView or your broker",
      fields: [
        {id:"goldChg",          label:"GOLD % CHANGE",    ph:"e.g. 0.8",     tip:"Gold today % change"},
        {id:"jpyChg",           label:"JPY/USD % CHANGE", ph:"e.g. -0.3",    tip:"USD/JPY today % change"},
        {id:"eurChg",           label:"EUR/USD % CHANGE", ph:"e.g. 0.2",     tip:"EUR/USD today % change"},
        {id:"goldPrice",        label:"GOLD PRICE",       ph:"e.g. 3285",    tip:"Current gold XAU/USD"},
        {id:"jpyPrice",         label:"JPY/USD PRICE",    ph:"e.g. 0.00685", tip:"Current USD/JPY inverse"},
        {id:"eurPrice",         label:"EUR/USD PRICE",    ph:"e.g. 1.0850",  tip:"Current EUR/USD"},
        {id:"techVsDefensive",  label:"TECH VS DEFENSIVE",ph:"e.g. 1.5",     tip:"+= tech leading, -= defensive. Check QQQ vs XLU ratio"},
        {id:"crossAlign",       label:"CROSS MKT ALIGN",  ph:"e.g. 0.7",     tip:"+1=all bull, -1=all bear, 0=mixed"}
      ]
    },
    {
      label: "INSTITUTIONAL LEVELS",
      color: "#ff6b35",
      avail: "NOW",
      note: "Mark these on your chart each morning",
      fields: [
        {id:"fvgPresent",  label:"FVG PRESENT?",      ph:"YES or NO",    tip:"Is there a FVG near key level"},
        {id:"fvgDir",      label:"FVG DIRECTION",     ph:"BULL/BEAR/NONE",tip:"Direction of the FVG"},
        {id:"mss",         label:"MKT STRUCTURE SHIFT",ph:"BULL/BEAR/NONE",tip:"Has last swing high/low broken"}
      ]
    },
    {
      label: "NEWS & MACRO",
      color: "#ff3d57",
      avail: "NOW",
      note: "Check economic calendar - investing.com/economic-calendar",
      fields: [
        {id:"dataToday",    label:"DATA RELEASE TODAY", ph:"CPI/PPI/JOBS/NONE",tip:"Major data release today"},
        {id:"fedDays",      label:"DAYS TO FED MEETING",ph:"e.g. 21",           tip:"Days until next FOMC"},
        {id:"geopolScore",  label:"GEOPOLITICAL SCORE", ph:"0-100 (50=neutral)",tip:"0=max fear, 100=max peace"},
        {id:"earningsDays", label:"DAYS TO MAJ EARNINGS",ph:"e.g. 3",           tip:"Days to next MAG7 earnings"},
        {id:"opexDays",     label:"DAYS TO OPEX",       ph:"e.g. 7",            tip:"Days to options expiration"},
        {id:"cbSpeech",     label:"CB SPEECH TODAY",    ph:"FED/BOJ/ECB/NONE",  tip:"Central bank speaker today"},
        {id:"newsAgeHours", label:"WARROOM DATA AGE",   ph:"e.g. 8",            tip:"Hours since last warroom update"}
      ]
    }
  ];

  var statusDots=[["prevHigh","PDH"],["prevLow","PDL"],["prevClose","PDC"],
    ["weekHigh","WKH"],["weekLow","WKL"],["prevWeekHigh","PWH"],["prevWeekLow","PWL"],
    ["ma50","50MA"],["ma200","200MA"],["dxy","DXY"],["yield10","10Y"],
    ["goldChg","GLD"],["jpyChg","JPY"],["eurChg","EUR"],["todayOpen","OPEN"]
  ].map(function(f){
    var filled=mktInputs[f[0]]&&mktInputs[f[0]].length>0;
    return '<span style="margin-right:4px;font-size:7px;color:'+(filled?"#00ff9f":"#1a1a1a")+'">'+(filled?"v":"x")+" "+f[1]+'</span>';
  }).join("");

  // Count filled inputs
  var totalFields = 67;
  var filledCount = Object.keys(mktInputs).filter(function(k){
    return k !== "loaded" && k !== "activeMarket" && k !== "todayOpen" &&
           mktInputs[k] && mktInputs[k].length > 0 && mktInputs[k] !== "NONE" && mktInputs[k] !== "NO";
  }).length;
  var completePct = Math.round(filledCount/totalFields*100);

  // Build expandable input sections
  var inputSectionsHtml = inputSections.map(function(sec, secIdx){
    var sFields = sec.fields.map(function(f){
      var val = mktInputs[f.id]||"";
      var filled = val.length > 0 && val !== "NONE" && val !== "NO";
      return '<div style="background:#080808;border:1px solid '+(filled?sec.color+"44":"#111")+';border-radius:3px;padding:4px 6px">'
        +'<div style="display:flex;justify-content:space-between;margin-bottom:2px">'
        +'<span style="font-size:6.5px;color:'+(filled?sec.color:"#333")+';font-weight:700">'+f.label+'</span>'
        +(filled?'<span style="font-size:6px;color:#00ff9f">v</span>':'<span style="font-size:6px;color:#1a1a1a">--</span>')
        +'</div>'
        +'<input value="'+val+'" placeholder="'+f.ph+'" '
        +'style="width:100%;background:#0d0d0d;border:none;color:'+sec.color+';padding:3px 4px;border-radius:2px;font-size:9px;font-family:monospace;font-weight:700" '
        +'oninput="mktInputs.'+ f.id +'=this.value;updateSignalMeter()"/>'
        +'<div style="font-size:6px;color:#1a1a1a;margin-top:1px">'+f.tip+'</div>'
        +'</div>';
    }).join("");

    var colCount = sec.fields.length > 8 ? 3 : 2;

    return '<div style="margin-bottom:6px">'
      +'<div onclick="toggleSection('+ secIdx +')" style="display:flex;justify-content:space-between;align-items:center;padding:5px 8px;background:#080808;border:1px solid '+ sec.color +'33;border-radius:4px;cursor:pointer;margin-bottom:4px">'
      +'<div style="display:flex;gap:6px;align-items:center">'
      +'<span style="font-size:8px;color:'+sec.color+';font-weight:700">'+sec.label+'</span>'
      +'<span style="font-size:7px;color:#333">'+sec.note+'</span>'
      +'</div>'
      +'<span style="font-size:7px;color:'+ sec.color +'" id="secToggle'+secIdx+'">v</span>'
      +'</div>'
      +'<div id="secBody'+secIdx+'" style="display:grid;grid-template-columns:repeat('+colCount+',1fr);gap:4px">'+sFields+'</div>'
      +'</div>';
  }).join("");

  var inputsHtml = getMorningBriefHTML();

  var instCtx='<div style="background:#0a0a0a;border:1px solid #a78bfa22;border-radius:6px;padding:10px;margin-bottom:10px">'
    +'<div style="font-size:8px;color:#a78bfa;font-weight:700;letter-spacing:1px;margin-bottom:8px">INSTITUTIONAL CONTEXT</div>'
    +'<div style="display:grid;grid-template-columns:1fr 1fr;gap:4px;margin-bottom:8px">'
    +[
      ["WEEKLY RANGE", inst.weekPos+"%", inst.weekPos>65?"#ff3d57":inst.weekPos<35?"#00ff9f":"#fbbf24",
       inst.weekPos>80?"Near weekly HIGH - institutional resistance":inst.weekPos<20?"Near weekly LOW - institutional support":"Mid weekly range - wait for direction"],
      ["GAP", inst.gapDir+" "+(Math.abs(inst.gapPts)||0).toFixed(0)+" pts", inst.gapDir==="GAP UP"?"#00ff9f":inst.gapDir==="GAP DOWN"?"#ff3d57":"#888",
       inst.gapDir==="GAP UP"?"Gap up = bullish if holds, bearish if fills":inst.gapDir==="GAP DOWN"?"Gap down = bearish if holds, bullish if fills":"Flat open - wait for ORB direction"],
      ["PREV DAY POS", inst.prevPos+"%", inst.prevPos>65?"#ff3d57":inst.prevPos<35?"#00ff9f":"#fbbf24",
       inst.prevPos>80?"Above PDH - breakout territory":inst.prevPos<20?"Below PDL - breakdown territory":"Inside prev day range - wait for break"],
      ["STRUCTURE", inst.trend, inst.trend==="BULL"?"#00ff9f":"#ff3d57",
       inst.trend==="BULL"?"Above prev close - buyers control":"Below prev close - sellers control"]
    ].map(function(item){
      return '<div style="background:#070707;border:1px solid #111;border-radius:4px;padding:6px 8px">'
        +'<div style="font-size:7px;color:#333;margin-bottom:2px">'+item[0]+'</div>'
        +'<div style="font-size:11px;color:'+item[2]+';font-weight:700;margin-bottom:2px">'+item[1]+'</div>'
        +'<div style="font-size:7.5px;color:#444;line-height:1.3">'+item[3]+'</div></div>';
    }).join("")
    +'</div>'
    +'<div style="margin-bottom:6px"><div style="font-size:7px;color:#a78bfa;margin-bottom:4px;letter-spacing:1px">ORDER BLOCKS</div>'
    +SIGNAL.institutional.orderBlocks.map(function(ob){
      var c=ob.type.indexOf("BEAR")>=0?"#ff3d57":"#00ff9f";
      return '<div style="display:flex;justify-content:space-between;padding:3px 0;border-bottom:1px solid #111">'
        +'<div><span style="font-size:9px;color:'+c+';font-weight:700">'+ob.level.toLocaleString()+'</span>'
        +'<span style="font-size:7px;color:'+c+'88;margin-left:5px">'+ob.type+'</span></div>'
        +'<span style="font-size:7.5px;color:#444;max-width:55%;text-align:right;line-height:1.3">'+ob.note+'</span></div>';
    }).join("")+'</div>'
    +'<div><div style="font-size:7px;color:#fbbf24;margin-bottom:4px;letter-spacing:1px">LIQUIDITY POOLS - WHERE STOPS CLUSTER</div>'
    +SIGNAL.institutional.liquidityLevels.map(function(ll){
      var c=ll.type.indexOf("BUY")>=0?"#00ff9f":"#ff3d57";
      return '<div style="display:flex;justify-content:space-between;padding:3px 0;border-bottom:1px solid #111">'
        +'<div><span style="font-size:9px;color:'+c+';font-weight:700">'+ll.level.toLocaleString()+'</span>'
        +'<span style="font-size:7px;color:'+c+'88;margin-left:5px">'+ll.type+'</span></div>'
        +'<span style="font-size:7.5px;color:#444;max-width:55%;text-align:right;line-height:1.3">'+ll.note+'</span></div>';
    }).join("")+'</div></div>';

  // Kill zones
  var killHtml='<div style="background:#0a0a0a;border:1px solid #fbbf2422;border-radius:6px;padding:10px;margin-bottom:10px">'
    +'<div style="font-size:8px;color:#fbbf24;font-weight:700;letter-spacing:1px;margin-bottom:6px">KILL ZONES - WHEN INSTITUTIONS ARE ACTIVE</div>'
    +SIGNAL.institutional.killZones.map(function(kz){
      return '<div style="display:flex;justify-content:space-between;align-items:center;padding:5px 0;border-bottom:1px solid #111">'
        +'<div><div style="font-size:9px;color:'+(kz.active?"#fbbf24":"#333")+';font-weight:700">'+kz.name+'</div>'
        +'<div style="font-size:7.5px;color:#444">'+kz.time+'</div></div>'
        +'<div style="text-align:right;max-width:55%"><div style="font-size:7.5px;color:#555;line-height:1.3">'+kz.note+'</div></div></div>';
    }).join("")+'</div>';

  // Gauge
  var R=80,CX=106,CY=102;
  var ang=Math.PI*(1-pct2/100);
  var nX=(CX+(R-14)*Math.cos(ang)).toFixed(1),nY=(CY-(R-14)*Math.sin(ang)).toFixed(1);
  var fX=(CX+R*Math.cos(ang)).toFixed(1),fY=(CY-R*Math.sin(ang)).toFixed(1);

  var scoreKeys=[
    ["priceStructure","PRICE STRUCTURE","30%"],
    ["orderFlow","ORDER FLOW","25%"],
    ["instLevels","INST LEVELS","25%"],
    ["newsMacro","NEWS/MACRO","20%"]
  ];
  var scoreHtml=scoreKeys.map(function(item){
    var v=inst.scores[item[0]]||50;
    var sc=v>=60?"#00ff9f":v<=40?"#ff3d57":"#fbbf24";
    var reasoning={
      priceStructure:"Wk pos "+inst.weekPos+"%. "+inst.gapDir+". Prev pos "+inst.prevPos+"%.",
      orderFlow:"VIX "+pct(LIVE.VIX.chgPct||0)+". Oil "+pct(LIVE.OIL.chgPct||0)+". MAG7 "+["AAPL","MSFT","NVDA","AMZN","GOOGL","META","TSLA"].filter(function(s){return (LIVE[s]&&LIVE[s].chgPct||0)>0;}).length+"/7 green.",
      instLevels:"VWAP dist "+(LIVE.MNQ.price-SIGNAL.scalperLevels.vwap).toFixed(0)+" pts. "+SIGNAL.institutional.bias,
      newsMacro:SIGNAL.reasoning.newsAndMacro
    }[item[0]]||"";
    return '<div style="margin-bottom:6px">'
      +'<div style="display:flex;justify-content:space-between;margin-bottom:1px">'
      +'<span style="font-size:7.5px;color:#2a2a2a">'+item[1]+' '+item[2]+'</span>'
      +'<span style="font-size:9px;color:'+sc+';font-weight:700">'+v+'</span></div>'
      +'<div class="bar-wrap"><div class="bar-fill" style="width:'+v+'%;background-position:'+(100-v)+'%"></div></div>'
      +(reasoning?'<div style="font-size:7.5px;color:#444;line-height:1.3;margin-top:1px">'+reasoning+'</div>':"")
      +'</div>';
  }).join("");

  var gaugeHtml='<div class="card"><div style="font-size:7.5px;color:#2a2a2a;letter-spacing:2px;margin-bottom:4px">INSTITUTIONAL SIGNAL</div>'
    +'<div style="display:flex;gap:12px;flex-wrap:wrap;align-items:flex-start">'
    +'<div style="min-width:212px;flex:0 0 212px">'
    +'<svg viewBox="0 0 212 120" style="width:100%;display:block">'
    +'<path d="M '+(CX-R)+' '+CY+' A '+R+' '+R+' 0 0 1 '+(CX+R)+' '+CY+'" fill="none" stroke="#1a1a1a" stroke-width="12" stroke-linecap="round"/>'
    +'<path d="M '+(CX-R)+' '+CY+' A '+R+' '+R+' 0 0 1 '+fX+' '+fY+'" fill="none" stroke="'+col+'" stroke-width="12" stroke-linecap="round" style="filter:drop-shadow(0 0 5px '+col+'88)"/>'
    +'<line x1="'+CX+'" y1="'+(CY+1)+'" x2="'+nX+'" y2="'+(+nY+1)+'" stroke="#00000077" stroke-width="3" stroke-linecap="round"/>'
    +'<line x1="'+CX+'" y1="'+CY+'" x2="'+nX+'" y2="'+nY+'" stroke="#fff" stroke-width="2.5" stroke-linecap="round"/>'
    +'<circle cx="'+CX+'" cy="'+CY+'" r="5" fill="#111" stroke="#444" stroke-width="1.5"/>'
    +'<circle cx="'+CX+'" cy="'+CY+'" r="2.5" fill="'+col+'"/>'
    +'<text x="'+(CX-R)+'" y="'+(CY+15)+'" fill="#ff3d57aa" font-size="9" font-family="monospace" text-anchor="middle">SHORT</text>'
    +'<text x="'+(CX+R)+'" y="'+(CY+15)+'" fill="#00ff9faa" font-size="9" font-family="monospace" text-anchor="middle">LONG</text>'
    +'<text x="'+CX+'" y="'+(CY-19)+'" fill="'+col+'" font-size="21" font-family="monospace" font-weight="bold" text-anchor="middle">'+pct2+'%</text>'
    +'<text x="'+CX+'" y="'+(CY-5)+'" fill="'+col+'" font-size="7.5" font-family="monospace" text-anchor="middle">'+inst.conviction+'</text>'
    +'</svg>'
    +'<div style="display:flex;height:4px;border-radius:2px;overflow:hidden;margin-top:2px">'
    +'<div style="width:'+(100-pct2)+'%;background:#ff3d57"></div>'
    +'<div style="width:'+pct2+'%;background:#00ff9f"></div></div>'
    +'<div style="display:flex;justify-content:space-between;margin-top:2px">'
    +'<span style="font-size:7px;color:#ff3d57">SHORT '+(100-pct2)+'%</span>'
    +'<span style="font-size:7px;color:#00ff9f">LONG '+pct2+'%</span></div>'
    +'<div style="margin-top:8px;background:#0a0a0a;border:1px solid #111;border-radius:4px;padding:7px 9px">'
    +'<div style="font-size:7px;color:#fbbf24;margin-bottom:5px;letter-spacing:1px">! SCALPER LEVELS</div>'
    +[["R3",SIGNAL.scalperLevels.r3,"#ff3d5766"],["R2",SIGNAL.scalperLevels.r2,"#ff3d5799"],["R1",SIGNAL.scalperLevels.r1,"#ff4444bb"],["VWAP",SIGNAL.scalperLevels.vwap,"#fbbf24"],["S1",SIGNAL.scalperLevels.s1,"#00ff9fbb"],["S2",SIGNAL.scalperLevels.s2,"#00ff9f99"],["S3",SIGNAL.scalperLevels.s3,"#00ff9f66"]].map(function(item){
      return '<div class="level-row"><span style="font-size:8px;color:'+item[2]+';font-weight:700">'+item[0]+'</span><span style="font-size:9px;color:'+item[2]+';font-weight:700">'+item[1].toLocaleString()+'</span></div>';
    }).join("")+'</div></div>'
    +'<div style="flex:1;min-width:130px">'+scoreHtml+'</div></div>'
    +'<div style="margin-top:8px;background:'+col+'0d;border:1px solid '+col+'22;border-radius:5px;padding:7px 9px">'
    +'<div style="font-size:7px;color:'+col+';margin-bottom:2px">DOMINANT THESIS</div>'
    +'<div style="font-size:10px;color:#888;line-height:1.5">'+SIGNAL.thesis+'</div></div>'
    +'<div style="margin-top:5px;background:#fbbf2408;border:1px solid #fbbf2422;border-radius:5px;padding:7px 9px">'
    +'<div style="font-size:7px;color:#fbbf24;margin-bottom:2px">! SCALP ENTRY NOTES</div>'
    +'<div style="font-size:10px;color:#777;line-height:1.5">'+SIGNAL.entryNotes+'</div></div>'
    +'<div style="margin-top:5px;background:#ff3d5708;border:1px solid #ff3d5722;border-radius:5px;padding:7px 9px">'
    +'<div style="font-size:7px;color:#ff3d57;margin-bottom:2px">[!] TOP RISK</div>'
    +'<div style="font-size:10px;color:#555;line-height:1.5">'+SIGNAL.mainRisk+'</div></div>'
    +'</div>';

  // ── PROMINENT RECOMMENDATION BOX ─────────────────────────────────────────
  var recScore = inst.composite;
  var recCol = inst.convColor || col;
  var recBg = recScore >= 65 ? "#00ff9f" : recScore <= 35 ? "#ff3d57" : "#fbbf24";
  var recIcon = recScore >= 65 ? "LONG" : recScore <= 35 ? "SHORT" : "WAIT";
  var recAction = recScore >= 75 ? "STRONG " + recIcon + " - HIGH CONVICTION"
    : recScore >= 65 ? "LEAN " + recIcon + " - CONFIRMED BIAS"
    : recScore <= 25 ? "STRONG " + recIcon + " - HIGH CONVICTION"
    : recScore <= 35 ? "LEAN " + recIcon + " - CONFIRMED BIAS"
    : recScore >= 55 ? "MILD LONG BIAS - A+ SETUPS ONLY"
    : recScore <= 45 ? "MILD SHORT BIAS - A+ SETUPS ONLY"
    : "NEUTRAL - NO TRADE ZONE";

  var tradeInstruction = "";
  if(recScore >= 65 && inst.activeKZ) {
    tradeInstruction = "Kill zone ACTIVE. Watch for ORB HIGH break + VWAP above + FVG retest -> LONG 5 contracts";
  } else if(recScore <= 35 && inst.activeKZ) {
    tradeInstruction = "Kill zone ACTIVE. Watch for ORB LOW break + VWAP below + FVG retest -> SHORT 5 contracts";
  } else if(recScore >= 65) {
    tradeInstruction = "Wait for kill zone + 9:35 ORB. Long bias confirmed. Only trade ORB high breakout with VWAP above.";
  } else if(recScore <= 35) {
    tradeInstruction = "Wait for kill zone + 9:35 ORB. Short bias confirmed. Only trade ORB low breakdown with VWAP below.";
  } else {
    tradeInstruction = "Score "+recScore+" is in the NO-TRADE ZONE (35-65). Sit on hands. No edge today. Wait for score to clear 65 or drop below 35.";
  }

  // Score bar segments
  var noTradeWidth = 30; // 35-65 is 30 points
  var longWidth = recScore > 65 ? Math.min(recScore - 65, 35) : 0;
  var shortWidth = recScore < 35 ? Math.min(35 - recScore, 35) : 0;

  var recHtml = "<div style='background:" + recBg + "18;border:2px solid " + recBg + "66;border-radius:8px;padding:12px 14px;margin-bottom:10px'>"
    // Top row - score and label
    + "<div style='display:flex;justify-content:space-between;align-items:center;margin-bottom:8px'>"
    + "<div>"
    + "<div style='font-size:7px;color:" + recBg + ";letter-spacing:2px;font-weight:700;margin-bottom:2px'>INSTITUTIONAL SIGNAL</div>"
    + "<div style='font-size:18px;color:" + recBg + ";font-weight:700;line-height:1;letter-spacing:1px'>" + recAction + "</div>"
    + "</div>"
    + "<div style='text-align:center;background:" + recBg + "22;border:1px solid " + recBg + "44;border-radius:6px;padding:6px 12px'>"
    + "<div style='font-size:28px;color:" + recBg + ";font-weight:700;line-height:1'>" + recScore + "</div>"
    + "<div style='font-size:7px;color:" + recBg + "99;margin-top:2px'>/100</div>"
    + "</div>"
    + "</div>"

    // Score bar with zones
    + "<div style='margin-bottom:8px'>"
    + "<div style='display:flex;justify-content:space-between;margin-bottom:2px'>"
    + "<span style='font-size:7px;color:#ff3d57'>SHORT &lt;35</span>"
    + "<span style='font-size:7px;color:#fbbf24'>NO TRADE 35-65</span>"
    + "<span style='font-size:7px;color:#00ff9f'>LONG &gt;65</span>"
    + "</div>"
    + "<div style='height:8px;background:#0d0d0d;border-radius:4px;overflow:hidden;position:relative;display:flex'>"
    + "<div style='width:35%;background:#ff3d5733;border-right:1px solid #ff3d5566'></div>"
    + "<div style='width:30%;background:#fbbf2422'></div>"
    + "<div style='width:35%;background:#00ff9f22;border-left:1px solid #00ff9f44'></div>"
    + "</div>"
    // Needle position
    + "<div style='position:relative;height:6px;margin-top:1px'>"
    + "<div style='position:absolute;left:calc(" + recScore + "% - 3px);top:0;width:6px;height:6px;background:" + recBg + ";border-radius:50%;border:1px solid #000'></div>"
    + "</div>"
    + "<div style='display:flex;justify-content:space-between;margin-top:1px'>"
    + "<span style='font-size:6px;color:#333'>0</span>"
    + "<span style='font-size:6px;color:#333'>25</span>"
    + "<span style='font-size:6px;color:#333'>50</span>"
    + "<span style='font-size:6px;color:#333'>75</span>"
    + "<span style='font-size:6px;color:#333'>100</span>"
    + "</div>"
    + "</div>"

    // Trade instruction
    + "<div style='background:" + recBg + "11;border:1px solid " + recBg + "33;border-radius:5px;padding:8px 10px;margin-bottom:6px'>"
    + "<div style='font-size:7px;color:" + recBg + ";font-weight:700;margin-bottom:3px;letter-spacing:1px'>WHAT TO DO RIGHT NOW</div>"
    + "<div style='font-size:10px;color:#aaa;line-height:1.5'>" + tradeInstruction + "</div>"
    + "</div>"

    // Kill zone status
    + "<div style='display:flex;gap:6px;align-items:center'>"
    + (inst.activeKZ
      ? "<div style='background:#00ff9f22;border:1px solid #00ff9f44;border-radius:3px;padding:2px 8px'><span style='font-size:8px;color:#00ff9f;font-weight:700'>* " + inst.activeKZ.name + " ACTIVE</span></div>"
      : "<div style='background:#11111122;border:1px solid #222;border-radius:3px;padding:2px 8px'><span style='font-size:8px;color:#333'>No kill zone active</span></div>")
    + "<div style='font-size:7px;color:#444'>"
    + (mktInputs.todayOpen
      ? "<span style='color:#00ff9f'>v Today open set: " + mktInputs.todayOpen + "</span>"
      : "<span style='color:#fbbf24'>! Enter today open at 9:30 AM ET for full score</span>")
    + "</div>"
    + "</div>"
    + "</div>";

  return sessHtml + oilHtml + recHtml + inputsHtml + gaugeHtml + instCtx + killHtml;
}


function toggleSection(idx){
  var body = document.getElementById("secBody"+idx);
  var toggle = document.getElementById("secToggle"+idx);
  if(!body) return;
  if(body.style.display === "none"){
    body.style.display = "grid";
    if(toggle) toggle.textContent = "v";
  } else {
    body.style.display = "none";
    if(toggle) toggle.textContent = ">";
  }
}

function updateSignalMeter(){
  if(state.tab==="signal") renderContent();
}


function renderScalp(){
  var score=PRETRADE.filter(function(i){return state.checks[i.id]==="yes";}).length;
  var allDone=Object.keys(state.checks).length===PRETRADE.length;
  var gng=score>=6?"GO":score>=4?"CAUTION":"NO GO";
  var gc=score>=6?"#00ff9f":score>=4?"#fbbf24":"#ff3d57";
  var items=PRETRADE.map(function(item){
    var ans=state.checks[item.id]||"";
    return '<div class="check-item"><div class="check-q">'+item.q+'</div><div class="check-btns"><button class="check-btn'+(ans==="yes"?" yes":"")+'" onclick="setCheck(\''+item.id+'\',\'yes\')">v '+item.bull+'</button><button class="check-btn'+(ans==="no"?" no":"")+'" onclick="setCheck(\''+item.id+'\',\'no\')">x '+item.bear+'</button></div></div>';
  }).join("");
  var result=allDone?'<div style="margin-top:8px;background:'+gc+'11;border:1px solid '+gc+'33;border-radius:5px;padding:8px 10px;text-align:center"><div style="font-size:14px;color:'+gc+';font-weight:700">'+gng+' - '+score+'/8 CONDITIONS MET</div><div style="font-size:9px;color:#555;margin-top:3px">'+(score>=6?"Conditions favorable. Use stops.":score>=4?"Proceed with caution. Reduce size 50%.":"Do not enter. Wait for better conditions.")+'</div></div>':"";
  return '<div class="card"><div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:8px"><div><div style="font-size:9px;color:#fbbf24;font-weight:700;letter-spacing:1px">! PRE-TRADE CHECKLIST</div><div style="font-size:7px;color:#333">Complete before every scalp entry</div></div><div style="text-align:right"><div class="gonogo" style="color:'+gc+'">'+gng+'</div><div style="font-size:8px;color:#444">'+score+'/'+PRETRADE.length+' checks</div></div></div>'+items+result+'<button onclick="resetChecks()" style="background:transparent;border:1px solid #111;color:#333;padding:4px 12px;border-radius:3px;cursor:pointer;font-size:7px;font-family:monospace;margin-top:6px;display:block;width:100%">reset RESET CHECKLIST</button></div>';
}
function setCheck(id,val){state.checks[id]=val;renderContent();}
function resetChecks(){state.checks={};renderContent();}

// ── ORB TAB ───────────────────────────────────────────────────────────────────
function renderORB(){
  var typeBtns=['<div style="margin-bottom:10px"><div style="font-size:7px;color:#444;margin-bottom:4px">ORB TIMEFRAME</div><div style="display:flex;gap:6px">',
    [["5","5-MIN ORB"],["15","15-MIN ORB"]].map(function(item){var act=state.orbType===item[0];return '<button onclick="setOrbType(\''+item[0]+'\')" style="flex:1;background:'+(act?"#ff6b3522":"transparent")+';border:1px solid '+(act?"#ff6b3555":"#1a1a1a")+';color:'+(act?"#ff6b35":"#333")+';padding:6px 0;border-radius:4px;cursor:pointer;font-size:9px;font-family:monospace;font-weight:700">'+item[1]+(act?" v":"")+'</button>';}).join(""),
    '</div><div style="font-size:7.5px;color:#2a2a2a;margin-top:4px">'+(state.orbType==="5"?"5-min ORB: opens 9:30, closes 9:35 AM ET. Best for scalp style.":"15-min ORB: opens 9:30, closes 9:45 AM ET. Fewer fakeouts.")+'</div></div>'].join("");
  var inputs='<div class="grid2" style="margin-bottom:8px"><div><div style="font-size:7px;color:#00ff9f;margin-bottom:3px">ORB HIGH ('+(state.orbType==="5"?"9:35 close":"9:45 close")+')</div><input id="orbHiInput" value="'+state.orbHigh+'" placeholder="e.g. 29420" class="orb-input hi" style="width:100%" oninput="state.orbHigh=this.value;state.orbSetup=null"/></div><div><div style="font-size:7px;color:#ff3d57;margin-bottom:3px">ORB LOW ('+(state.orbType==="5"?"9:35 close":"9:45 close")+')</div><input id="orbLoInput" value="'+state.orbLow+'" placeholder="e.g. 29180" class="orb-input lo" style="width:100%" oninput="state.orbLow=this.value;state.orbSetup=null"/></div></div>';
  var calcBtn='<button onclick="calcORB()" style="width:100%;background:#ff6b3511;border:1px solid #ff6b3533;color:#ff6b35;padding:8px 0;border-radius:4px;cursor:pointer;font-size:9px;font-family:monospace;font-weight:700;letter-spacing:1px;margin-bottom:8px">! CALCULATE ORB LEVELS</button>';
  var setup=state.orbSetup;
  var resultsHtml="";
  if(setup){
    var cp=parseFloat(state.currentPrice)||0;
    var isAbove=cp>parseFloat(setup.high),isBelow=cp<parseFloat(setup.low);
    var statusHtml="";
    if(cp>0){var sc=isAbove?"#00ff9f":isBelow?"#ff3d57":"#fbbf24";var st=isAbove?"ABOVE ORB - BULLISH BREAKOUT":isBelow?"BELOW ORB - BEARISH BREAKDOWN":"INSIDE ORB - WAIT FOR BREAK";statusHtml='<div style="background:'+sc+'11;border:1px solid '+sc+'33;border-radius:6px;padding:8px 12px;margin-bottom:8px;text-align:center"><div style="font-size:11px;color:'+sc+';font-weight:700">'+st+'</div></div>';}
    var summaryHtml='<div style="background:#0a0a0a;border:1px solid #222;border-radius:6px;padding:8px 12px;margin-bottom:8px"><div style="font-size:7px;color:#ff6b35;letter-spacing:1px;margin-bottom:6px">'+state.orbType+'-MIN ORB RANGE</div><div class="grid3">'+[["HIGH",setup.high,"#00ff9f"],["MID",setup.mid,"#fbbf24"],["LOW",setup.low,"#ff3d57"],["RANGE",setup.range+" pts","#aaa"],["L-STOP",setup.longStop,"#ff3d5788"],["S-STOP",setup.shortStop,"#00ff9f88"]].map(function(item){return '<div class="stat-box" style="text-align:center;border-color:'+item[2]+'22"><div class="stat-lbl" style="color:'+item[2]+'88">'+item[0]+'</div><div style="font-size:11px;color:'+item[2]+';font-weight:700">'+item[1]+'</div></div>';}).join("")+'</div></div>';
    var longHtml='<div style="background:#00ff9f06;border:1px solid #00ff9f22;border-radius:6px;padding:8px 12px;margin-bottom:8px"><div style="font-size:7px;color:#00ff9f;letter-spacing:1px;margin-bottom:6px">[UP] LONG TARGETS (breakout above '+setup.high+')</div><div style="font-size:8px;color:#444;margin-bottom:6px">Entry: retest ORB high on 30s + FVG fill -> long</div>'+[["T1 (+0.5R)",setup.lt1,"#00ff9f"],["T2 (+1R)",setup.lt2,"#00e676"],["T3 (+1.5R)",setup.lt3,"#00cc66"],["T4 (+2R)",setup.lt4,"#009944"]].map(function(item){var hit=cp>0&&cp>=parseFloat(item[1]);return '<div class="target-row"><div><span style="font-size:9px;color:'+item[2]+';font-weight:700">'+item[0]+'</span></div><div style="display:flex;align-items:center;gap:5px">'+(hit?'<span class="hit-badge" style="color:#00ff9f;background:#00ff9f11;border:1px solid #00ff9f33">v HIT</span>':'')+'<span style="font-size:11px;color:'+item[2]+';font-weight:700">'+item[1]+'</span></div></div>';}).join("")+'</div>';
    var shortHtml='<div style="background:#ff3d5706;border:1px solid #ff3d5722;border-radius:6px;padding:8px 12px;margin-bottom:8px"><div style="font-size:7px;color:#ff3d57;letter-spacing:1px;margin-bottom:6px">[DN] SHORT TARGETS (breakdown below '+setup.low+')</div><div style="font-size:8px;color:#444;margin-bottom:6px">Entry: retest ORB low on 30s + FVG fill -> short</div>'+[["T1 (-0.5R)",setup.st1,"#ff3d57"],["T2 (-1R)",setup.st2,"#ff2244"],["T3 (-1.5R)",setup.st3,"#cc1133"],["T4 (-2R)",setup.st4,"#990022"]].map(function(item){var hit=cp>0&&cp<=parseFloat(item[1]);return '<div class="target-row"><div><span style="font-size:9px;color:'+item[2]+';font-weight:700">'+item[0]+'</span></div><div style="display:flex;align-items:center;gap:5px">'+(hit?'<span class="hit-badge" style="color:#ff3d57;background:#ff3d5711;border:1px solid #ff3d5733">v HIT</span>':'')+'<span style="font-size:11px;color:'+item[2]+';font-weight:700">'+item[1]+'</span></div></div>';}).join("")+'</div>';
    var fvgHtml='<div style="background:#a78bfa08;border:1px solid #a78bfa22;border-radius:6px;padding:8px 12px;margin-bottom:8px"><div style="font-size:7px;color:#a78bfa;letter-spacing:1px;margin-bottom:6px">[FVG] FVG NOTES (30s chart)</div><div style="display:flex;gap:6px;margin-bottom:6px"><input id="fvgInput" value="'+state.fvgInput+'" placeholder="e.g. Bullish FVG at 29,410" style="flex:1;background:#111;border:1px solid #a78bfa33;color:#ddd;padding:6px 8px;border-radius:4px;font-size:9px;font-family:monospace" oninput="state.fvgInput=this.value"/><button onclick="addFVG()" style="background:#a78bfa11;border:1px solid #a78bfa33;color:#a78bfa;padding:0 10px;border-radius:4px;cursor:pointer;font-size:8px;font-family:monospace">+ ADD</button></div>'+(state.fvgNotes.length===0?'<div style="font-size:8px;color:#1a1a1a">No FVGs logged yet</div>':state.fvgNotes.map(function(n,i){return '<div style="display:flex;justify-content:space-between;padding:4px 0;border-bottom:1px solid #111"><span style="font-size:8px;color:#666">'+n.text+'</span><span style="font-size:7px;color:#222">'+n.time+'</span></div>';}).join(""))+'</div>';
    var flowHtml='<div style="background:#fbbf2408;border:1px solid #fbbf2422;border-radius:6px;padding:8px 12px"><div style="font-size:7px;color:#fbbf24;letter-spacing:1px;margin-bottom:5px">! YOUR ORB ENTRY FLOW</div>'+["1. At 9:30 AM ET the "+state.orbType+"-min candle OPENS - do not enter yet","2. Wait for candle to close ("+(state.orbType==="5"?"9:35 AM ET":"9:45 AM ET")+")","3. Mark high ("+setup.high+") and low ("+setup.low+") as your ORB","4. Drop to 30-second chart","5. Wait for price to retest the ORB high OR low","6. Look for 3-candle FVG at that level - entry signal","7. Enter on FVG fill, stop beyond ORB (long stop: "+setup.longStop+")","8. First target T1, then trail or close at T2"].map(function(s){return '<div style="font-size:8px;color:#555;padding:3px 0;border-bottom:1px solid #111;line-height:1.4">'+s+'</div>';}).join("")+'</div>';
    var cpHtml='<div style="margin-bottom:8px"><div style="font-size:7px;color:#444;margin-bottom:3px">CURRENT PRICE (optional)</div><input value="'+state.currentPrice+'" placeholder="e.g. 29450" style="width:100%;background:#111;border:1px solid #222;color:#ddd;padding:6px 8px;border-radius:4px;font-size:10px;font-family:monospace" oninput="state.currentPrice=this.value;renderContent()"/></div>';
    resultsHtml=cpHtml+statusHtml+summaryHtml+longHtml+shortHtml+fvgHtml+flowHtml+'<button onclick="resetORB()" style="width:100%;background:transparent;border:1px solid #111;color:#222;padding:6px 0;border-radius:4px;cursor:pointer;font-size:7px;font-family:monospace;margin-top:8px">reset RESET ORB</button>';
  }
  return '<div style="font-family:monospace"><div class="card"><div style="font-size:9px;color:#ff6b35;font-weight:700;letter-spacing:1px;margin-bottom:2px">! ORB TRACKER</div><div style="font-size:8px;color:#333;margin-bottom:10px">Opening Range Breakout - enter the 9:30 candle high and low</div>'+typeBtns+inputs+calcBtn+resultsHtml+'</div></div>';
}
function setOrbType(t){state.orbType=t;state.orbSetup=null;renderContent();}
function calcORB(){
  var h=parseFloat(state.orbHigh),l=parseFloat(state.orbLow);
  if(!h||!l||h<=l) return;
  var r=h-l,e1=r*.5,e2=r,e3=r*1.5,e4=r*2;
  state.orbSetup={high:h.toFixed(2),low:l.toFixed(2),range:r.toFixed(2),mid:((h+l)/2).toFixed(2),lt1:(h+e1).toFixed(2),lt2:(h+e2).toFixed(2),lt3:(h+e3).toFixed(2),lt4:(h+e4).toFixed(2),st1:(l-e1).toFixed(2),st2:(l-e2).toFixed(2),st3:(l-e3).toFixed(2),st4:(l-e4).toFixed(2),longStop:(l-r*.25).toFixed(2),shortStop:(h+r*.25).toFixed(2)};
  renderContent();
}
function resetORB(){state.orbHigh="";state.orbLow="";state.orbSetup=null;state.fvgNotes=[];state.currentPrice="";renderContent();}
function addFVG(){if(state.fvgInput.trim()){state.fvgNotes=[{text:state.fvgInput,time:new Date().toLocaleTimeString([],{hour:"2-digit",minute:"2-digit"})},...state.fvgNotes].slice(0,5);state.fvgInput="";renderContent();}}

// ── JOURNAL TAB ───────────────────────────────────────────────────────────────
function renderJournal(){
  var trades=state.trades;
  var totalPnl=trades.reduce(function(s,t){return s+parseFloat(t.pnl);},0);
  var wins=trades.filter(function(t){return parseFloat(t.pnl)>0;}).length;
  var wr=trades.length>0?Math.round(wins/trades.length*100):0;
  var statsHtml=trades.length>0?'<div class="grid3" style="grid-template-columns:1fr 1fr 1fr 1fr;margin-bottom:10px">'+[["TRADES",trades.length,"#aaa"],["WIN RATE",wr+"%",wr>=50?"#00ff9f":"#ff3d57"],["P&L","$"+totalPnl.toFixed(0),totalPnl>=0?"#00ff9f":"#ff3d57"],["AVG","$"+(trades.length>0?(totalPnl/trades.length).toFixed(0):"--"),(totalPnl/trades.length)>=0?"#00e676":"#ff3d57"]].map(function(item){return '<div class="journal-stat"><div style="font-size:7px;color:#333">'+item[0]+'</div><div style="font-size:13px;color:'+item[2]+';font-weight:700">'+item[1]+'</div></div>';}).join("")+'</div>':"";
  var formHtml=state.addingTrade?'<div style="background:#0a0a0a;border:1px solid #00ff9f22;border-radius:5px;padding:10px;margin-bottom:10px"><div style="font-size:8px;color:#00ff9f;margin-bottom:8px">LOG NEW TRADE</div><div class="grid2" style="margin-bottom:6px"><div><div style="font-size:7px;color:#444;margin-bottom:3px">SIDE</div><div style="display:flex;gap:4px">'+["LONG","SHORT"].map(function(side){return '<button onclick="setTradeSide(\''+side+'\')" style="flex:1;background:'+(state.tradeForm.side===side?(side==="LONG"?"#00ff9f22":"#ff3d5722"):"transparent")+';border:1px solid '+(state.tradeForm.side===side?(side==="LONG"?"#00ff9f44":"#ff3d5744"):"#222")+';color:'+(state.tradeForm.side===side?(side==="LONG"?"#00ff9f":"#ff3d57"):"#444")+';padding:5px 0;border-radius:3px;cursor:pointer;font-size:8px;font-family:monospace">'+side+'</button>';}).join("")+'</div></div><div><div style="font-size:7px;color:#444;margin-bottom:3px">CONTRACTS</div><input value="'+state.tradeForm.size+'" style="width:100%;background:#111;border:1px solid #222;color:#ddd;padding:5px 8px;border-radius:3px;font-size:10px;font-family:monospace" oninput="state.tradeForm.size=this.value" placeholder="1"/></div><div><div style="font-size:7px;color:#444;margin-bottom:3px">ENTRY</div><input value="'+state.tradeForm.entry+'" style="width:100%;background:#111;border:1px solid #222;color:#ddd;padding:5px 8px;border-radius:3px;font-size:10px;font-family:monospace" oninput="state.tradeForm.entry=this.value" placeholder="29200"/></div><div><div style="font-size:7px;color:#444;margin-bottom:3px">EXIT</div><input value="'+state.tradeForm.exit+'" style="width:100%;background:#111;border:1px solid #222;color:#ddd;padding:5px 8px;border-radius:3px;font-size:10px;font-family:monospace" oninput="state.tradeForm.exit=this.value" placeholder="29250"/></div></div><div style="margin-bottom:8px"><div style="font-size:7px;color:#444;margin-bottom:3px">NOTES</div><input value="'+state.tradeForm.notes+'" style="width:100%;background:#111;border:1px solid #222;color:#ddd;padding:5px 8px;border-radius:3px;font-size:9px;font-family:monospace" oninput="state.tradeForm.notes=this.value" placeholder="e.g. VWAP reclaim, MAG7 green"/></div>'+(state.tradeForm.entry&&state.tradeForm.exit?'<div style="margin-bottom:8px;padding:6px 9px;background:#111;border-radius:4px"><span style="font-size:9px;color:#555">Est. P&L: </span><span style="font-size:11px;color:'+(((state.tradeForm.side==="LONG"?parseFloat(state.tradeForm.exit)-parseFloat(state.tradeForm.entry):parseFloat(state.tradeForm.entry)-parseFloat(state.tradeForm.exit))*(parseInt(state.tradeForm.size)||1)*2)>=0?"#00ff9f":"#ff3d57")+';font-weight:700">$'+(((state.tradeForm.side==="LONG"?parseFloat(state.tradeForm.exit)-parseFloat(state.tradeForm.entry):parseFloat(state.tradeForm.entry)-parseFloat(state.tradeForm.exit))*(parseInt(state.tradeForm.size)||1)*2)).toFixed(0)+'</span></div>':'')+'<div style="display:flex;gap:6px"><button onclick="saveTrade()" style="flex:2;background:#00ff9f11;border:1px solid #00ff9f33;color:#00ff9f;padding:7px 0;border-radius:3px;cursor:pointer;font-size:9px;font-family:monospace;font-weight:700">v SAVE TRADE</button><button onclick="state.addingTrade=false;renderContent()" style="flex:1;background:transparent;border:1px solid #111;color:#333;padding:7px 0;border-radius:3px;cursor:pointer;font-size:8px;font-family:monospace">CANCEL</button></div></div>':"";
  var tradeList=trades.slice(0,10).map(function(t){var win=parseFloat(t.pnl)>=0;return '<div class="trade-row" style="border:1px solid '+(win?"#00ff9f18":"#ff3d5718")+'"><div style="display:flex;justify-content:space-between;align-items:center"><div style="display:flex;gap:6px;align-items:center"><span style="font-size:9px;color:'+(t.side==="LONG"?"#00ff9f":"#ff3d57")+';font-weight:700">'+t.side+'</span><span style="font-size:8px;color:#555">'+t.size+'ct @ '+t.entry+' -> '+t.exit+'</span><span style="font-size:7px;color:#222">'+t.time+'</span></div><div style="text-align:right"><div style="font-size:12px;color:'+(win?"#00ff9f":"#ff3d57")+';font-weight:700">$'+t.pnl+'</div><div style="font-size:7px;color:#333">'+t.pts+' pts</div></div></div>'+(t.notes?'<div style="font-size:8px;color:#333;margin-top:3px;line-height:1.3">'+t.notes+'</div>':'')+'</div>';}).join("");
  return '<div class="card"><div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:10px"><div><div style="font-size:9px;color:#00ff9f;font-weight:700;letter-spacing:1px">TRADE JOURNAL</div><div style="font-size:7px;color:#333">MNQ scalp log - $2/tick/contract</div></div><button onclick="state.addingTrade=true;renderContent()" style="background:#00ff9f11;border:1px solid #00ff9f33;color:#00ff9f;padding:4px 10px;border-radius:3px;cursor:pointer;font-size:8px;font-family:monospace">+ LOG TRADE</button></div>'+statsHtml+formHtml+(trades.length===0&&!state.addingTrade?'<div style="font-size:9px;color:#2a2a2a;text-align:center;padding:20px 0">No trades logged yet. Tap + LOG TRADE after each scalp.</div>':tradeList)+(trades.length>0?'<button onclick="clearTrades()" style="background:transparent;border:1px solid #111;color:#222;padding:4px 12px;border-radius:3px;cursor:pointer;font-size:7px;font-family:monospace;margin-top:4px;display:block;width:100%">reset CLEAR ALL TRADES</button>':"")+'</div>';
}
function setTradeSide(s){state.tradeForm.side=s;renderContent();}
function saveTrade(){
  var f=state.tradeForm;
  if(!f.entry||!f.exit) return;
  var en=parseFloat(f.entry),ex=parseFloat(f.exit),sz=parseInt(f.size)||1;
  var pnl=f.side==="LONG"?(ex-en)*sz*2:(en-ex)*sz*2;
  var pts=f.side==="LONG"?(ex-en):(en-ex);
  state.trades=[{id:Date.now(),side:f.side,entry:en,exit:ex,size:sz,notes:f.notes,pnl:pnl.toFixed(0),pts:pts.toFixed(2),time:new Date().toLocaleTimeString([],{hour:"2-digit",minute:"2-digit"})},...state.trades].slice(0,50);
  state.tradeForm={side:"LONG",entry:"",exit:"",size:"1",notes:""};
  state.addingTrade=false;
  renderContent();
}
function clearTrades(){if(confirm("Clear all trades?")) {state.trades=[];renderContent();}}

// ── PRICES TAB ────────────────────────────────────────────────────────────────
function renderPrices(){
  var mnq=LIVE.MNQ;
  var oilAlert=getOilAlert();
  var mag7html=MAG7.map(function(sym){var q=LIVE[sym];if(!q)return"";var up=q.chgPct>=0;return '<div style="background:#070707;border:1px solid #0d0d0d;border-radius:5px;padding:8px 10px"><div style="display:flex;justify-content:space-between"><div><div style="font-size:10px;color:'+q.color+';font-weight:700">'+sym+' w'+q.w+'</div><div style="font-size:15px;color:#e0e0e0;font-weight:700">$'+q.price.toFixed(2)+'</div></div><div style="font-size:12px;color:'+(up?"#00e676":"#ff3d57")+';font-weight:700;text-align:right">'+(up?"^":"v")+Math.abs(q.chgPct).toFixed(2)+'%</div></div></div>';}).join("");
  return '<div style="background:#00ff9f0a;border:1px solid #00ff9f22;border-radius:6px;padding:10px;margin-bottom:10px"><div style="font-size:8px;color:#00ff9f;margin-bottom:6px">MNQ FUTURES - '+LIVE.dataTimestamp+'</div><div class="grid3" style="margin-bottom:8px">'+[["PRICE",mnq.price.toLocaleString(),"#00ff9f"],["CHANGE","+"+mnq.chg,"#00e676"],["CHG%","+"+mnq.chgPct.toFixed(2)+"%","#00e676"],["HIGH",mnq.high.toLocaleString(),"#00ff9f"],["LOW",mnq.low.toLocaleString(),"#ff3d57"],["OPEN",mnq.open.toLocaleString(),"#888"]].map(function(item){return '<div class="stat-box"><div class="stat-lbl">'+item[0]+'</div><div class="stat-val" style="color:'+item[2]+'">'+item[1]+'</div></div>';}).join("")+'</div><div style="font-size:9px;color:#666;line-height:1.5">'+LIVE.NOTE+'</div></div>'
  +'<div class="grid2" style="margin-bottom:10px"><div style="background:#0a0a0a;border:1px solid #111;border-radius:5px;padding:8px 10px"><div style="font-size:8px;color:#a78bfa;margin-bottom:3px;font-weight:700">VIX - FEAR GAUGE</div><div style="font-size:18px;color:'+(LIVE.VIX.price<20?"#00ff9f":LIVE.VIX.price<25?"#fbbf24":"#ff3d57")+';font-weight:700">'+LIVE.VIX.price+'</div><div style="font-size:8px;color:#ff3d5777;margin-bottom:4px">^'+Math.abs(LIVE.VIX.chgPct).toFixed(2)+'%</div><div style="font-size:8px;color:#444;line-height:1.4">'+(LIVE.VIX.price<15?"Low fear - scalp friendly":LIVE.VIX.price<20?"Moderate - normal":LIVE.VIX.price<25?"Elevated - widen stops":"HIGH - reduce size")+'</div><div style="font-size:8px;color:#333;margin-top:3px;line-height:1.3">'+LIVE.VIX.note+'</div></div><div style="background:#0a0a0a;border:1px solid '+oilAlert.color+'44;border-radius:5px;padding:8px 10px"><div style="font-size:8px;color:#ff9f1c;margin-bottom:3px;font-weight:700">WTI OIL - NQ INVERSE</div><div style="font-size:18px;color:'+(LIVE.OIL.price<100?"#00ff9f":"#ff3d57")+';font-weight:700">$'+LIVE.OIL.price+'</div><div style="font-size:8px;color:#ff3d5777;margin-bottom:4px">^'+Math.abs(LIVE.OIL.chgPct).toFixed(2)+'%</div><div style="font-size:8px;color:#444;line-height:1.4">'+(LIVE.OIL.price<90?"Low oil = bullish NQ":LIVE.OIL.price<100?"Moderate - watch Iran":"Elevated - NQ headwind")+'</div><div style="font-size:8px;color:#333;margin-top:3px;line-height:1.3">'+LIVE.OIL.note+'</div></div></div>'
  +'<div style="font-size:8px;color:#fbdd74;letter-spacing:1px;margin-bottom:8px">MAG7 DETAIL</div><div class="grid2">'+mag7html+'</div>';
}

// ── NEWS TAB ──────────────────────────────────────────────────────────────────
function renderNews(){
  var biasc=NEWS.overallBias==="BULL"?"#00ff9f":NEWS.overallBias==="BEAR"?"#ff3d57":"#888";
  var srcs=NEWS.sources.map(function(src){var bc=src.bias==="BULL"?"#00ff9f":src.bias==="BEAR"?"#ff3d57":"#666";return '<div class="news-src"><div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:4px"><div style="display:flex;gap:5px;align-items:center"><span style="font-size:9px;color:'+src.color+';font-weight:700;border:1px solid '+src.color+'44;border-radius:2px;padding:0 5px">'+src.name+'</span><span style="font-size:8px;color:'+bc+';font-weight:700">* '+src.bias+'</span><span style="font-size:7px;color:#222">'+src.publishedAt+'</span></div><a href="'+src.url+'" target="_blank" style="text-decoration:none;font-size:8px;color:#333">-></a></div><div class="news-hl" style="border-color:'+src.color+'44">'+src.headline+'</div><div class="news-sum">'+src.summary+'</div></div>';}).join("");
  return '<div style="background:#0a0a0a;border:1px solid #111;border-radius:5px;padding:8px 10px;margin-bottom:10px"><div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:4px"><span style="font-size:8px;color:#333">'+NEWS.asOf+'</span><span style="background:'+biasc+'1a;color:'+biasc+';border:1px solid '+biasc+'33;border-radius:3px;padding:1px 6px;font-size:8px;font-weight:700">'+NEWS.overallBias+'</span></div><div style="font-size:10px;color:#777;line-height:1.5;margin-bottom:5px">'+NEWS.mnqImplication+'</div><div style="font-size:9px;color:#ff3d5788">[!] '+NEWS.keyRisk+'</div><div style="font-size:9px;color:#ff6b3577;margin-top:3px">[BOMB] '+NEWS.tweetRisk+'</div></div>'+srcs+'<div style="background:#a78bfa08;border:1px solid #a78bfa22;border-radius:5px;padding:7px 10px"><div style="font-size:7.5px;color:#a78bfa;margin-bottom:3px">FED WATCH</div><div style="font-size:10px;color:#666;line-height:1.5">'+NEWS.fedWatch+'</div></div>';
}

// ── CHARTS TAB ────────────────────────────────────────────────────────────────
function renderCharts(){
  var sl=SIGNAL.scalperLevels;
  return '<div style="font-size:9px;color:#00d4aa;font-weight:700;letter-spacing:1px;margin-bottom:8px">LIVE MNQ CHARTS - TAP TO OPEN</div>'
  +'<div style="background:#00ff9f0a;border:1px solid #00ff9f22;border-radius:5px;padding:7px 10px;margin-bottom:10px;display:flex;justify-content:space-between"><span style="font-size:8px;color:#555">MNQ ('+LIVE.dataTimestamp+')</span><span style="font-size:16px;color:#00ff9f;font-weight:700">'+LIVE.MNQ.price.toLocaleString()+' <span style="font-size:10px;color:#00e676">+'+LIVE.MNQ.chgPct.toFixed(2)+'%</span></span></div>'
  +CHART_LINKS.map(function(l){return '<a href="'+l.url+'" target="_blank" class="chart-link" style="border:1px solid '+l.color+'33"><div><div style="font-size:10px;color:'+l.color+';font-weight:700">'+l.label+'</div><div style="font-size:8px;color:#444;margin-top:2px">'+l.desc+'</div></div><span style="font-size:14px;color:'+l.color+'">-></span></a>';}).join("")
  +'<div style="background:#0a0a0a;border:1px solid #111;border-radius:5px;padding:10px;margin-top:4px"><div style="font-size:8px;color:#fbbf24;margin-bottom:6px">KEY LEVELS</div><div class="grid3" style="margin-bottom:8px">'+[["RESISTANCE",SIGNAL.keyLevels.resistance,"#ff4444"],["SUPPORT",SIGNAL.keyLevels.support,"#00ff9f"],["PIVOT",SIGNAL.keyLevels.pivot,"#fbbf24"]].map(function(item){return '<div class="stat-box" style="border-color:'+item[2]+'22"><div class="stat-lbl">'+item[0]+'</div><div style="font-size:11px;color:'+item[2]+';font-weight:700">'+item[1]+'</div></div>';}).join("")+'</div><div style="font-size:8px;color:#fbbf24;margin-bottom:6px">SCALPER LEVELS</div><div style="display:grid;grid-template-columns:repeat(4,1fr);gap:4px">'+[["R2",sl.r2,"#ff3d57"],["R1",sl.r1,"#ff6b35"],["VWAP",sl.vwap,"#fbbf24"],["S1",sl.s1,"#00ff9f"],["S2",sl.s2,"#00d4aa"]].map(function(item){return '<div class="stat-box" style="border-color:'+item[2]+'33;text-align:center"><div style="font-size:7px;color:'+item[2]+';font-weight:700">'+item[0]+'</div><div style="font-size:11px;color:'+item[2]+';font-weight:700">'+item[1].toLocaleString()+'</div></div>';}).join("")+'</div></div>';
}

// ── SOCIAL TAB ────────────────────────────────────────────────────────────────
function renderSocial(){
  var traders=NQ_TRADERS.map(function(a){return '<a href="https://x.com/'+a.h+'" target="_blank" class="social-row"><div style="flex-shrink:0;min-width:118px"><div style="font-size:9px;color:#1d9bf0;font-weight:700">@'+a.h+' -></div><div style="font-size:8px;color:#00ff9f;font-weight:700;margin-top:1px">'+a.label+'</div></div><div style="font-size:9px;color:#444;line-height:1.5">'+a.why+'</div></a>';}).join("");
  var bombList=BOMBS.map(function(a){return '<a href="https://x.com/'+a.h+'" target="_blank" class="bomb-row"><div style="flex-shrink:0;min-width:118px"><div style="font-size:9px;color:#ff3d57;font-weight:700">@'+a.h+' -></div><div style="font-size:8px;color:#ff1a1a;font-weight:700;margin-top:1px">'+a.label+'</div></div><div style="font-size:9px;color:#663333;line-height:1.5">'+a.why+'</div></a>';}).join("");
  var schedule=[["7:00-9:30 AM ET","PRE-MARKET PREP","Check all NQ traders + bombs. Plan levels. No trades until 9:30."],["9:30-10:30 AM ET","BEST SCALP WINDOW","Highest volume, clearest moves. First hour is king."],["10:30 AM-12 PM","CHOP ZONE","Often choppy. Reduce size or sit out."],["2:00-4:00 PM ET","AFTERNOON WINDOW","Second best window. Follow MAG7 + VWAP."],["3:00-4:00 AM ET","LONDON OPEN","Best overnight session for scalps. High vol."]].map(function(s){return '<div style="display:flex;gap:8px;padding:5px 0;border-bottom:1px solid #1a1a1a"><div style="flex-shrink:0;min-width:110px"><div style="font-size:8px;color:#fbbf24;font-weight:700">'+s[0]+'</div><div style="font-size:7px;color:#333">'+s[1]+'</div></div><div style="font-size:9px;color:#444;line-height:1.5">'+s[2]+'</div></div>';}).join("");
  return '<div style="font-size:9px;color:#1d9bf0;font-weight:700;letter-spacing:1px;margin-bottom:4px">NQ SOCIAL SENTIMENT</div><div style="font-size:8px;color:#2a2a2a;margin-bottom:10px;line-height:1.5">Check 3+ traders before entry. Check BOMBS before every single trade.</div><div style="font-size:7.5px;color:#00ff9f;letter-spacing:1px;margin-bottom:6px">> NQ/FUTURES TRADERS</div>'+traders+'<div style="font-size:7.5px;color:#ff3d57;letter-spacing:1px;margin-bottom:6px;margin-top:12px">[BOMB] CHECK BEFORE EVERY SCALP</div>'+bombList+'<div style="background:#111;border:1px solid #222;border-radius:5px;padding:10px;margin-top:12px"><div style="font-size:7.5px;color:#fbbf24;margin-bottom:6px">[CLK] SCALPER SESSION GUIDE</div>'+schedule+'</div>';
}

// ── MISC ──────────────────────────────────────────────────────────────────────
function copyRefresh(){
  if(navigator.clipboard) navigator.clipboard.writeText("Requesting refresh").then(function(){alert("Copied! Paste into Claude chat.");}).catch(function(){alert('Type: "Requesting refresh" in Claude chat');});
  else alert('Type: "Requesting refresh" in Claude chat');
}

function attachHandlers(){
  if(state.tab==="live"&&state.dbConnected){
    setTimeout(drawChart,50);
    if(!window._dbInterval){
      window._dbInterval=setInterval(function(){
        if(state.dbConnected&&state.tab==="live") fetchDatabento(state.dbKey,state.tf);
      },5000);
    }
  }
}

// -- LOCALSTORAGE - save/load API key -----------------------------------------
function saveKey(key){
  try{ localStorage.setItem("db_api_key", key); } catch(e){}
}
function loadKey(){
  try{ return localStorage.getItem("db_api_key")||""; } catch(e){ return ""; }
}
function clearKey(){
  try{ localStorage.removeItem("db_api_key"); } catch(e){}
}

// -- INIT ----------------------------------------------------------------------
// Load saved API key on startup
// Auto-connect disabled
var savedKey = loadKey();
if(savedKey){ state.dbKey = savedKey; }
state.dbConnected = false;

renderMag7();
renderTabs();
renderMktSwitcher();
renderContent();
setInterval(updateClock, 1000);
updateClock();
renderMag7();
renderTabs();
renderMktSwitcher();
renderContent();
setInterval(updateClock, 1000);
updateClock();
</script>
</body>
</html>
