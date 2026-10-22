import base64
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))
def read_b64(path):
    with open(path, 'rb') as f:
        return base64.b64encode(f.read()).decode('ascii')

kisa_b64 = read_b64('real_samples/KISAKOL-MI03.wav')
uzun_b64 = read_b64('real_samples/KARA-DUZEN04.wav')
cura_b64 = read_b64('real_samples/bozuki1.wav')
ud_b64   = read_b64('real_samples/EMREUD4A3.wav')

html_content = f'''<!DOCTYPE html>
<html lang="tr">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Dizek 7 | Türk Halk Müziği & Bağlama Nota Editörü</title>
  <link rel="icon" type="image/x-icon" href="favicon.ico">
  <link rel="shortcut icon" href="favicon.ico">
  <link rel="icon" type="image/svg+xml" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E%3Ccircle cx='16' cy='16' r='15' fill='%230b0f17' stroke='%230284c7' stroke-width='1.5'/%3E%3Cline x1='21' y1='5' x2='21' y2='27' stroke='%2338bdf8' stroke-width='2.4' stroke-linecap='round'/%3E%3Cpath d='M 21 14 L 10 18.5 L 21 24 Z M 21 16.5 L 14.5 18.5 L 21 21.5 Z' fill='%2338bdf8'/%3E%3Ctext x='22' y='12' font-family='sans-serif' font-size='8.5' font-weight='900' fill='%23f97316'%3E2%3C/text%3E%3C/svg%3E">
  <style>
    :root {{
      --bg-main: #0b0f17;
      --bg-panel: #131b2e;
      --bg-panel-alt: #0f1626;
      --bg-card: #1e293b;
      --bg-hover: #334155;
      --border-color: #334155;
      --border-accent: #0284c7;
      --text-main: #f8fafc;
      --text-dim: #94a3b8;
      --text-muted: #64748b;
      --stave-bg: #0f172a;
      --stave-line: #475569;
      --stave-note: #f8fafc;
      --tezene-down: #38bdf8;
      --tezene-up: #fbbf24;
      --b2-color: #f97316;
      --senyo-color: #f59e0b;
      --ropriz-color: #f43f5e;
      --dolap-color: #a855f7;
      --ornament-color: #ec4899;
      --solfege-color: #38bdf8;
      --lyric-color: #cbd5e1;
    }}

    body[data-theme="parchment"] {{
      --bg-main: #f4efe6;
      --bg-panel: #eae2d3;
      --bg-panel-alt: #dfd5c3;
      --bg-card: #f9f6f0;
      --bg-hover: #e2d8c7;
      --border-color: #cfc2ad;
      --border-accent: #b45309;
      --text-main: #1f2937;
      --text-dim: #4b5563;
      --text-muted: #6b7280;
      --stave-bg: #fffdf9;
      --stave-line: #374151;
      --stave-note: #111827;
      --tezene-down: #0284c7;
      --tezene-up: #d97706;
      --b2-color: #ea580c;
      --senyo-color: #d97706;
      --ropriz-color: #e11d48;
      --dolap-color: #7e22ce;
      --ornament-color: #db2777;
      --solfege-color: #0369a1;
      --lyric-color: #374151;
    }}

    * {{ box-sizing: border-box; margin: 0; padding: 0; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; }}
    body {{ background: var(--bg-main); color: var(--text-main); display: flex; flex-direction: column; min-height: 100vh; overflow-x: hidden; user-select: none; }}

    header {{ background: var(--bg-panel); border-bottom: 1px solid var(--border-color); padding: 8px 16px; display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 8px; }}
    .logo-box {{ display: flex; align-items: center; gap: 10px; }}
    .logo-icon {{ width: 32px; height: 32px; border-radius: 8px; background: linear-gradient(135deg, #0284c7, #b45309); display: flex; align-items: center; justify-content: center; box-shadow: 0 2px 8px rgba(0,0,0,0.3); font-weight: bold; font-size: 16px; }}
    .logo-title {{ font-size: 15px; font-weight: 700; display: flex; align-items: center; gap: 8px; }}
    .badge-mimari {{ font-size: 10px; font-weight: 600; background: var(--border-color); color: var(--text-dim); padding: 2px 8px; border-radius: 9999px; text-transform: uppercase; }}

    .header-actions {{ display: flex; align-items: center; gap: 6px; flex-wrap: wrap; }}
    .btn {{ display: inline-flex; align-items: center; gap: 5px; padding: 3px 6.5px; border-radius: 5px; font-size: 10.5px; font-weight: 600; cursor: pointer; border: 1px solid transparent; transition: all 0.15s ease; }}
    .btn-play {{ background: #059669; border-color: #047857; color: #fff; }}
    .btn-play:hover {{ background: #047857; }}
    .btn-play.playing {{ background: #0284c7; border-color: #0369a1; }}
    .btn-primary {{ background: #0284c7; border-color: #0369a1; color: #fff; }}
    .btn-primary:hover {{ background: #0369a1; }}
    .btn-secondary {{ background: var(--bg-card); border-color: var(--border-color); color: var(--text-main); }}
    .btn-secondary:hover {{ background: var(--bg-hover); }}
    .btn-danger {{ background: rgba(239, 68, 68, 0.15); border-color: rgba(239, 68, 68, 0.35); color: #f87171; }}
    .btn-danger:hover {{ background: rgba(239, 68, 68, 0.25); }}

    .view-tabs {{ display: inline-flex; background: var(--bg-main); border: 1px solid var(--border-color); border-radius: 6px; padding: 2px; }}
    .tab-btn {{ background: transparent; border: none; color: var(--text-dim); padding: 4px 10px; border-radius: 4px; font-size: 11px; font-weight: 700; cursor: pointer; }}
    .tab-btn.active {{ background: var(--border-accent); color: #fff; }}

    .toolbar-container {{ background: var(--bg-panel); border-bottom: 1px solid var(--border-color); padding: 4px 8px; display: flex; flex-direction: column; gap: 3px; }}
    .toolbar-row {{ display: flex; align-items: center; gap: 3px; flex-wrap: nowrap; overflow-x: auto; scrollbar-width: none; }}
    .toolbar-row::-webkit-scrollbar {{ display: none; }}
    .tool-section {{ display: inline-flex; align-items: center; gap: 2px; flex-shrink: 0; }}
    .section-label {{ font-size: 9.5px; font-weight: 700; color: var(--text-dim); text-transform: uppercase; white-space: nowrap; }}
    .v-divider {{ width: 1px; height: 14px; background: var(--border-color); flex-shrink: 0; margin: 0 1px; }}

    .btn-toggle-group {{ display: inline-flex; border: 1px solid var(--border-color); border-radius: 4px; overflow: hidden; flex-shrink: 0; }}
    .btn-toggle {{
      background: var(--bg-card); color: var(--text-main); border: none; border-right: 1px solid var(--border-color);
      padding: 2.5px 5.5px; font-size: 10.5px; font-weight: 500; cursor: pointer; display: inline-flex; align-items: center; gap: 2px; white-space: nowrap;
    }}
    .btn-toggle:last-child {{ border-right: none; }}
    .btn-toggle:hover {{ background: var(--bg-hover); }}
    .btn-toggle.active {{ background: var(--border-accent); color: #fff; font-weight: 700; }}
    .btn-toggle .kbd-hint {{ font-size: 9px; opacity: 0.85; font-family: monospace; font-weight: bold; background: rgba(0,0,0,0.25); padding: 1px 3px; border-radius: 3px; }}

    select.tool-select {{
      background: var(--bg-card); border: 1px solid var(--border-color); color: var(--text-main);
      border-radius: 4px; padding: 4px 8px; font-size: 11px; font-weight: 700; cursor: pointer; outline: none;
    }}

    input.lyric-input {{
      background: var(--bg-card); border: 1px solid var(--border-color); color: var(--text-main);
      border-radius: 4px; padding: 3px 6px; font-size: 11px; width: 58px; outline: none;
    }}

    .selected-note-badge {{
      display: inline-flex; align-items: center; gap: 6px; margin-left: auto;
      background: rgba(56, 189, 248, 0.15); border: 1px solid var(--tezene-down); border-radius: 6px; padding: 2px 7px;
    }}

    .status-bar {{
      background: var(--bg-panel-alt); border-bottom: 1px solid var(--border-color);
      padding: 6px 16px; display: flex; align-items: center; justify-content: space-between; gap: 12px; font-size: 11px; flex-wrap: wrap;
    }}
    .status-left {{ display: flex; align-items: center; gap: 12px; flex-wrap: wrap; }}
    .progress-bar-bg {{ width: 90px; height: 7px; background: var(--bg-main); border-radius: 4px; overflow: hidden; border: 1px solid var(--border-color); }}
    .progress-bar-fill {{ height: 100%; transition: width 0.15s ease; }}
    .warning-alert {{
      display: inline-flex; align-items: center; gap: 6px; padding: 2px 8px; border-radius: 4px;
      background: rgba(239, 68, 68, 0.15); border: 1px solid #ef4444; color: #f87171; font-weight: 700; font-size: 11px;
    }}

    main {{ flex: 1; padding: 16px; overflow-x: auto; display: flex; flex-direction: column; align-items: center; }}
    #editorView {{ width: 100%; display: flex; justify-content: center; }}
    .score-card {{
      background: var(--stave-bg); border: 1px solid var(--border-color); border-radius: 12px;
      box-shadow: 0 10px 30px rgba(0,0,0,0.3); padding: 16px; min-width: 1020px; position: relative;
    }}

    #printView {{ display: none; width: 100%; max-width: 950px; flex-direction: column; gap: 16px; align-items: center; }}
    .a4-page {{
      background: #ffffff; color: #111827; width: 850px; min-height: 1150px; padding: 40px 45px;
      box-shadow: 0 12px 40px rgba(0,0,0,0.45); border-radius: 4px; position: relative;
    }}
    .a4-header {{
      display: grid;
      grid-template-columns: 200px 1fr 200px;
      align-items: center;
      margin-bottom: 20px;
      border-bottom: 2px solid #111827;
      padding-bottom: 10px;
      font-family: "Times New Roman", serif;
    }}
    .a4-meta-left {{
      text-align: left;
      font-size: 11px;
      line-height: 1.5;
      color: #374151;
      outline: none;
    }}
    .a4-meta-center {{
      text-align: center;
    }}
    .a4-title {{
      font-size: 21px;
      font-weight: 800;
      letter-spacing: 0.5px;
      outline: none;
    }}
    .a4-meta-right {{
      text-align: right;
      font-size: 11px;
      line-height: 1.5;
      color: #374151;
      outline: none;
    }}
    .a4-stave-row {{ display: flex; align-items: center; margin-bottom: 24px; gap: 10px; position: relative; }}
    .row-measure-control {{
      display: flex; flex-direction: column; align-items: center; justify-content: center;
      background: #f3f4f6; border: 1px solid #d1d5db; border-radius: 4px; padding: 2px 4px; font-size: 10px; font-weight: bold; width: 34px;
    }}
    .row-btn {{ background: none; border: none; cursor: pointer; font-size: 10px; line-height: 1; padding: 2px; }}
    .row-btn:hover {{ color: #0284c7; }}
    
    .lyrics-container {{
      margin-top: 30px; border-top: 1px dashed #9ca3af; padding-top: 16px; font-family: "Times New Roman", serif;
    }}
    .lyrics-grid {{ display: grid; grid-template-columns: 1fr 1fr; gap: 20px; font-size: 13px; line-height: 1.6; }}
    .lyrics-textarea {{
      width: 100%; height: 120px; border: 1px solid #d1d5db; border-radius: 4px; padding: 8px; font-family: serif; font-size: 13px; resize: vertical;
    }}

    footer {{
      background: var(--bg-panel); border-top: 1px solid var(--border-color);
      padding: 6px 16px; display: flex; align-items: center; justify-content: space-between; gap: 10px; font-size: 11px; flex-wrap: wrap;
    }}
    .shortcut-pill {{ font-family: monospace; background: var(--bg-card); border: 1px solid var(--border-color); padding: 1px 5px; border-radius: 4px; font-weight: 700; }}
  </style>
</head>
<body>

  <header>
        <div class="logo-box">
      <div class="logo-icon" style="background:#0f172a; border:1px solid #0284c7; border-radius:8px; display:flex; align-items:center; justify-content:center; width:30px; height:30px; padding:0;">
          <svg viewBox="0 0 512 512" width="24" height="24">
            <g transform="translate(110, 335) scale(0.51)">
              <path d="M 47.0 81.0 C 47.0 81.0 44.0 21.0 44.0 -19.0 C 44.0 -35.0 45.0 -47.0 46.0 -51.0 C 50.0 -63.0 76.0 -85.0 90.0 -93.0 C 99.0 -98.0 108.0 -100.0 116.0 -100.0 C 126.0 -100.0 135.0 -96.0 141.0 -89.0 C 151.0 -78.0 157.0 -61.0 157.0 -42.0 C 157.0 -24.0 152.0 -3.0 140.0 18.0 C 127.0 42.0 98.0 74.0 68.0 93.0 C 64.0 95.0 61.0 96.0 58.0 96.0 C 49.0 96.0 47.0 86.0 47.0 81.0 Z M 12.0 170.0 C 15.0 174.0 18.0 175.0 21.0 175.0 C 24.0 175.0 27.0 173.0 27.0 173.0 C 57.0 156.0 81.0 129.0 106.0 112.0 C 195.0 50.0 226.0 -11.0 226.0 -57.0 C 226.0 -114.0 182.0 -150.0 136.0 -153.0 C 129.0 -153.0 122.0 -152.0 115.0 -150.0 C 104.0 -147.0 92.0 -143.0 81.0 -136.0 C 75.0 -131.0 64.0 -122.0 59.0 -122.0 C 57.0 -122.0 56.0 -122.0 54.0 -123.0 C 47.0 -126.0 43.0 -133.0 43.0 -140.0 C 44.0 -162.0 50.0 -402.0 50.0 -422.0 C 50.0 -433.0 41.0 -439.0 31.0 -439.0 C 17.0 -439.0 1.0 -429.0 0.0 -411.0 C 0.0 -411.0 4.0 160.0 12.0 170.0 Z" fill="#38bdf8"/>
            </g>
            <g transform="translate(255, 205) scale(0.35)">
              <path d="M 421.0 -204.0 C 421.0 -231.0 421.0 -244.0 404.0 -244.0 C 403.0 -244.0 387.0 -240.0 383.0 -233.0 C 376.0 -221.0 362.0 -164.0 337.0 -164.0 C 312.0 -164.0 265.0 -249.0 182.0 -249.0 C 124.0 -249.0 109.0 -226.0 95.0 -213.0 C 81.0 -200.0 75.0 -196.0 68.0 -195.0 C 60.0 -195.0 47.0 -209.0 42.0 -219.0 C 40.0 -223.0 35.0 -226.0 30.0 -226.0 C 25.0 -226.0 20.0 -223.0 20.0 -214.0 L 20.0 -49.0 C 20.0 -49.0 21.0 -33.0 31.0 -33.0 C 39.0 -33.0 42.0 -42.0 46.0 -53.0 C 56.0 -78.0 69.0 -136.0 114.0 -136.0 C 154.0 -136.0 202.0 -61.0 260.0 -61.0 C 288.0 -61.0 302.0 -76.0 310.0 -82.0 C 313.0 -84.0 317.0 -86.0 319.0 -86.0 C 323.0 -86.0 325.0 -83.0 326.0 -77.0 C 326.0 -49.0 249.0 7.0 189.0 78.0 C 151.0 122.0 120.0 180.0 120.0 219.0 C 120.0 240.0 120.0 250.0 139.0 250.0 C 157.0 250.0 179.0 241.0 204.0 241.0 C 229.0 241.0 276.0 250.0 286.0 250.0 C 296.0 250.0 302.0 242.0 302.0 213.0 C 302.0 46.0 421.0 -97.0 421.0 -200.0 Z" fill="#38bdf8"/>
            </g>
          </svg>
        </div>
      <div>
        <div class="logo-title">
          Dizek 7
          <span class="badge-mimari">Akustik Ses &amp; SMuFL Dizgi</span>
        </div>
      </div>
    </div>

    <div class="view-tabs">
      <button id="tabEditor" class="tab-btn active">Yazım / Düzenleme</button>
      <button id="tabPrint" class="tab-btn">A4 Sayfa / Baskı Önizleme</button>
    </div>

    <div class="header-actions">
      <div class="tool-section">
        <span class="section-label" style="color:var(--tezene-up);">Ses Bankası:</span>
        <select id="soundPresetSelect" class="tool-select">
          <option value="kisa_sap" selected>🎵 Kısa Sap Bağlama (Stüdyo Kaydı)</option>
          <option value="uzun_sap">🎵 Kara Düzen / Uzun Sap Saz</option>
          <option value="cura">🎵 Bozuk / Cura</option>
          <option value="ud">🎵 Ud (Akustik Kayıt)</option>
        </select>
      </div>

      <button id="playBtn" class="btn btn-play" title="Röpriz ve Dolap Takibiyle Çal (P)">
        <span id="playIcon">▶</span> <span id="playText">Çal / Dinle</span>
      </button>

      <button id="saveProjectBtn" class="btn btn-secondary" title="Projeyi Bilgisayara İndir (.bglm)">💾 Kaydet</button>
      <button id="loadProjectBtn" class="btn btn-secondary" title="Daha Önce Kaydedilen Projeyi Aç">📂 Aç</button>
      <input type="file" id="projectFileInput" accept=".bglm,.baglama,.json" style="display: none;" />

      <button id="exportSvgBtn" class="btn btn-secondary" title="Saf Vektörel SVG İndir (Siyah Kutusuz)">⬇ SVG İndir</button>
      <button id="themeBtn" class="btn btn-secondary">☀ Nota Kağıdı</button>
    </div>
  </header>

  <div class="toolbar-container">
    <div class="toolbar-row">
      <div class="tool-section">
        <span class="section-label" style="color:var(--b2-color);">Donanım:</span>
        <select id="keySigSelect" class="tool-select" style="color:var(--b2-color); max-width:130px;">
          <option value="none">Doğal (Arızasız)</option>
          <option value="b2_si" selected>Si♭2</option>
          <option value="b2_si_fa_sharp">Si♭2 + Fa♯</option>
          <option value="b2_si_mi">Si♭2 + Mi♭2</option>
          <option value="b2_si_fa_sharp_do_sharp">Si♭2 + Fa♯ + Do♯</option>
          <option value="flat_si">Si♭</option>
          <option value="flat_si_mi">Si♭ + Mi♭</option>
          <option value="flat_si_mi_la">Si♭ + Mi♭ + La♭</option>
          <option value="sharp_fa">Fa♯</option>
          <option value="sharp_fa_do">Fa♯ + Do♯</option>
          <option value="sharp_fa_do_sol">Fa♯ + Do♯ + Sol♯</option>
          <option value="sharp_do">Do♯</option>
          <option value="b2_mi">Mi♭2</option>
          <option value="flat_mi">Mi♭</option>
          <option value="b1_si">Si♭1</option>
          <option value="b4_si">Si♭4</option>
        </select>
      </div>

      <div class="v-divider"></div>

      <div class="tool-section">
        <span class="section-label">Ölçü:</span>
        <select id="meterNum" class="tool-select" style="padding:2px 3px; font-weight:900; width:42px;" title="Ölçü Vuruş Sayısı (Pay)">
          <option value="1">1</option>
          <option value="2">2</option>
          <option value="3">3</option>
          <option value="4" selected>4</option>
          <option value="5">5</option>
          <option value="6">6</option>
          <option value="7">7</option>
          <option value="8">8</option>
          <option value="9">9</option>
          <option value="10">10</option>
          <option value="11">11</option>
          <option value="12">12</option>
          <option value="13">13</option>
          <option value="14">14</option>
          <option value="15">15</option>
          <option value="16">16</option>
          <option value="17">17</option>
          <option value="18">18</option>
          <option value="19">19</option>
          <option value="20">20</option>
          <option value="21">21</option>
          <option value="22">22</option>
          <option value="23">23</option>
          <option value="24">24</option>
          <option value="25">25</option>
          <option value="26">26</option>
          <option value="27">27</option>
          <option value="28">28</option>
          <option value="29">29</option>
          <option value="30">30</option>
          <option value="31">31</option>
          <option value="32">32</option>
        </select>
        <span style="font-weight:900; opacity:0.6;">/</span>
        <select id="meterDenom" class="tool-select" style="padding:2px 3px; font-weight:900; width:44px;" title="Ölçü Birim Değeri (Payda)">
          <option value="1">1</option>
          <option value="2">2</option>
          <option value="4" selected>4</option>
          <option value="8">8</option>
          <option value="9">9</option>
          <option value="16">16</option>
          <option value="32">32</option>
        </select>
      </div>

      <div class="v-divider"></div>

      <div class="tool-section">
        <span class="section-label" style="color:var(--ropriz-color);">Röpriz:</span>
        <div class="btn-toggle-group">
          <button id="repeatStartBtn" class="btn-toggle">|: Baş</button>
          <button id="repeatEndBtn" class="btn-toggle">:| Son</button>
        </div>
      </div>

      <div class="v-divider"></div>

      <div class="tool-section">
        <span class="section-label" style="color:#60a5fa;">Çizgi:</span>
        <div class="btn-toggle-group">
          <button id="doubleBarBtn" class="btn-toggle" title="Kıta / Bölüm Geçişi Çift Çizgi (𝄁)">𝄁 Çift</button>
          <button id="finalBarBtn" class="btn-toggle" title="Eser Bitiş Çizgisi (İnce-Kalın 𝄂)">𝄂 Bitiş</button>
        </div>
      </div>

      <div class="v-divider"></div>

      <div class="tool-section">
        <span class="section-label" style="color:var(--senyo-color);">Senyo:</span>
        <div class="btn-toggle-group">
          <button id="senyoStartBtn" class="btn-toggle" style="color:var(--senyo-color);">𝄋 Başa</button>
          <button id="senyoEndBtn" class="btn-toggle" style="color:var(--senyo-color);">𝄋 Sona</button>
        </div>
      </div>

      <div class="v-divider"></div>

      <div class="tool-section">
        <span class="section-label" style="color:#c084fc; font-weight:bold;">Perde:</span>
        <div class="btn-toggle-group" id="perdeGroup">
          <button class="btn-toggle active" data-val="none">Yok</button>
          <button class="btn-toggle" data-val="1P">1P</button>
          <button class="btn-toggle" data-val="2P">2P</button>
          <button class="btn-toggle" data-val="3P">3P</button>
          <button class="btn-toggle" data-val="4P">4P</button>
          <button class="btn-toggle" data-val="5P">5P</button>
          <button class="btn-toggle" data-val="6P">6P</button>
          <button class="btn-toggle" data-val="7P">7P</button>
          <button class="btn-toggle" data-val="8P">8P</button>
          <button class="btn-toggle" data-val="9P">9P</button>
        </div>
      </div>

      <div class="v-divider"></div>

      <div class="tool-section">
        <span class="section-label" style="color:var(--dolap-color);">Dolap:</span>
        <div class="btn-toggle-group" id="dolapGroup">
          <button class="btn-toggle active" data-val="none">Yok</button>
          <button class="btn-toggle" data-val="1">1. Dolap</button>
          <button class="btn-toggle" data-val="2">2. Dolap</button>
        </div>
      </div>

    </div>

    <div class="toolbar-row">
      <div class="tool-section">
        <span class="section-label">Süre:</span>
        <div class="btn-toggle-group" id="durGroup">
          <button class="btn-toggle" data-val="1/1">1/1 <span class="kbd-hint">A</span></button>
          <button class="btn-toggle" data-val="1/2">1/2 <span class="kbd-hint">S</span></button>
          <button class="btn-toggle active" data-val="1/4">1/4 <span class="kbd-hint">D</span></button>
          <button class="btn-toggle" data-val="1/8">1/8 <span class="kbd-hint">F</span></button>
          <button class="btn-toggle" data-val="1/16">1/16 <span class="kbd-hint">G</span></button>
          <button class="btn-toggle" data-val="1/32">1/32 <span class="kbd-hint">H</span></button>
          <button class="btn-toggle" data-val="1/64">1/64 <span class="kbd-hint">J</span></button>
        </div>
      </div>

      <button id="dotBtn" class="btn-toggle" style="font-weight:900; font-size:13px; border-radius:6px; border:1px solid var(--border-color); background:var(--bg-card); color:var(--text-main); padding:3px 9px;" title="Noktalı Nota / Es (Süreyi 1.5 katına uzatır - L)">
        • Nokta <span class="kbd-hint">L</span>
      </button>

      <button id="restBtn" class="btn btn-secondary" style="font-weight:bold; border-color:var(--border-accent);" title="Seçili Sürede Es / Sus Koy veya Seçiliyi Es Yap (K)">
        𝄽 Es (Sus) <span class="kbd-hint" style="background:#0284c7; color:#fff; padding:1px 4px; border-radius:3px;">K</span>
      </button>

      <div class="v-divider"></div>

      <div class="tool-section">
        <span class="section-label" style="color:#eab308; font-weight:bold;">Parmak:</span>
        <div class="btn-toggle-group" id="fingerGroup">
          <button class="btn-toggle" data-val="0">0 <span class="kbd-hint">0</span></button>
          <button class="btn-toggle active" data-val="1">1 <span class="kbd-hint">1</span></button>
          <button class="btn-toggle" data-val="2">2 <span class="kbd-hint">2</span></button>
          <button class="btn-toggle" data-val="3">3 <span class="kbd-hint">3</span></button>
          <button class="btn-toggle" data-val="4">4 <span class="kbd-hint">4</span></button>
          <button class="btn-toggle" data-val="5">5 <span class="kbd-hint">5</span></button>
        </div>
      </div>

      <div class="v-divider"></div>

      <div class="tool-section">
        <span class="section-label">Tezene:</span>
        <div class="btn-toggle-group" id="tezGroup">
          <button class="btn-toggle active" data-val="down" style="color:var(--tezene-down); font-weight:bold;">↓ Üst <span class="kbd-hint">W</span></button>
          <button class="btn-toggle" data-val="up" style="color:var(--tezene-up); font-weight:bold;">↑ Alt <span class="kbd-hint">E</span></button>
          <button class="btn-toggle" data-val="none">Yok <span class="kbd-hint">R</span></button>
        </div>
      </div>

      <div class="v-divider"></div>

      <div class="tool-section">
        <span class="section-label">Değiştirici:</span>
        <div class="btn-toggle-group" id="accGroup">
          <button class="btn-toggle active" data-val="natural">♮ Nat <span class="kbd-hint">Y</span></button>
          <button class="btn-toggle" data-val="b2" style="color:var(--b2-color); font-weight:bold;">♭2 Koma <span class="kbd-hint">U</span></button>
          <button class="btn-toggle" data-val="flat">♭ Bemol <span class="kbd-hint">I</span></button>
          <button class="btn-toggle" data-val="sharp">♯ Diyez <span class="kbd-hint">O</span></button>
          <button class="btn-toggle" data-val="sharp3" style="color:#10b981; font-weight:bold;">♯3 <span class="kbd-hint">P</span></button>
        </div>
        <select id="comaSelect" class="tool-select" style="font-size:11px; padding:3px 5px; margin-left:4px;" title="Koma Sayısı Seçici (1-8 Koma Bemol/Diyez)">
          <option value="">Koma Seç...</option>
          <option value="b1">♭1</option>
          <option value="b2">♭2</option>
          <option value="b3">♭3</option>
          <option value="b4">♭4</option>
          <option value="b5">♭5</option>
          <option value="b6">♭6</option>
          <option value="b7">♭7</option>
          <option value="b8">♭8</option>
          <option value="sharp1">♯1</option>
          <option value="sharp2">♯2</option>
          <option value="sharp3">♯3</option>
          <option value="sharp4">♯4</option>
          <option value="sharp5">♯5</option>
          <option value="sharp6">♯6</option>
          <option value="sharp7">♯7</option>
          <option value="sharp8">♯8</option>
        </select>
      </div>
    </div>

    <div class="toolbar-row">
      <div class="tool-section">
        <span class="section-label">Süsleme:</span>
        <div class="btn-toggle-group" id="ornGroup">
          <button class="btn-toggle active" data-val="none">Yok <span class="kbd-hint">Z</span></button>
          <button class="btn-toggle" data-val="carpma">Çarpma (v) <span class="kbd-hint">X</span></button>
          <button class="btn-toggle" data-val="cekme">Çekme (^) <span class="kbd-hint">C</span></button>
          <button class="btn-toggle" data-val="takma">Takma (▲) <span class="kbd-hint">V</span></button>
          <button class="btn-toggle" data-val="slash" style="color:#f59e0b; font-weight:bold;">Çentik (//) <span class="kbd-hint">B</span></button>
        </div>
      </div>

      <div class="v-divider"></div>

      <div class="tool-section">
        <span class="section-label" style="color:var(--border-accent);">Bağlar:</span>
        <div class="btn-toggle-group">
          <button id="btnBeamSingle" class="btn-toggle" title="Seçili Notaları 1/8 Kirişiyle Bağla">Tek Kiriş <span class="kbd-hint">N</span></button>
          <button id="btnBeamDouble" class="btn-toggle" title="Seçili Notaları 1/16 Kirişiyle Bağla">Çift Kiriş <span class="kbd-hint">M</span></button>
          <button id="btnTriplet" class="btn-toggle" title="Seçili Notalara Üçleme Rozeti Ekle/Kaldır">Üçleme <span class="kbd-hint">Ö</span></button>
          <button id="btnBeamBreak" class="btn-toggle" title="Seçili Notaların Bağını Çöz">Bağı Çöz <span class="kbd-hint">Ç</span></button>
        </div>
      </div>

      <div class="v-divider"></div>

      <div class="tool-section">
        <span class="section-label">Söz:</span>
        <input type="text" id="lyricInput" class="lyric-input" placeholder="Hece (boşsa boş kalır)" />
      </div>

      <button id="commitBtn" class="btn btn-primary" style="padding: 3px 8px; font-weight: bold; font-size: 11px;">
        <span>✓ Onayla (Space)</span>
      </button>

      <div class="v-divider"></div>

      <div class="tool-section">
        <button id="prevNoteBtn" class="btn btn-secondary" style="font-size:11px; padding:4px 8px;" title="Önceki Notaya Git (Sol Ok ◀)">◀ <span class="kbd-hint">←</span></button>
        <button id="nextNoteBtn" class="btn btn-secondary" style="font-size:11px; padding:4px 8px;" title="Sonraki Notaya Git (Sağ Ok ▶)"><span class="kbd-hint">→</span> ▶</button>
      </div>

      <div class="v-divider"></div>

      <div class="tool-section">
        <button id="insertMeasureBtn" class="btn btn-secondary" style="font-size:11px; padding:4px 9px;" title="Yeni Ölçü Ekle (Enter)">+ Yeni Ölçü Ekle <span class="kbd-hint">Enter</span></button>
        <button id="deleteMeasureBtn" class="btn btn-danger" style="font-size:11px; padding:4px 9px;" title="Ölçüyü Sil">✕ Ölçüyü Sil</button>
      </div>

      <div id="selectedNoteBox" class="selected-note-badge" style="display: none;">
        <span id="selectedNoteText" style="color:var(--tezene-down); font-weight:bold; font-size:11px;">Seçili: Si♭2 (1/4)</span>
        <button id="deleteNoteBtn" class="btn btn-danger" style="padding: 2px 6px; font-size: 10px;">Sil</button>
        <button id="deselectBtn" class="btn btn-secondary" style="padding: 2px 6px; font-size: 10px;">✕ Bırak (Esc)</button>
      </div>
    </div>
  </div>

  <div class="status-bar">
    <div class="status-left">
      <div><b>Ölçü:</b> <span id="measureNumText" style="color:var(--border-accent); font-weight:bold;">1 / 2</span></div>
      <div style="display: flex; align-items: center; gap: 8px;">
        <span style="color:var(--text-muted); font-size:11px;">Kapasite:</span>
        <div class="progress-bar-bg">
          <div id="capacityProgress" class="progress-bar-fill" style="width: 100%; background: #10b981;"></div>
        </div>
        <span id="capacityText" style="font-weight:bold; font-size:11px;">1.000 / 1.000 (100%)</span>
      </div>
      <div id="candidateNoteText" style="color:var(--tezene-down); font-weight:600; font-size:11px;">
        Aday Perde: <strong>Re4</strong> [1/4]
      </div>
      <div id="warningAlert" class="warning-alert" style="display: none;">
        ⚠️ <span id="warningMsgText">Ölçü kapasitesi aşıldı!</span>
      </div>
    </div>

  </div>

  <main>
    <div id="editorView">
      <div class="score-card">
        <svg id="scoreSvg" height="280" width="1050" viewBox="0 0 1050 280" style="display:block; cursor:crosshair;"></svg>
      </div>
    </div>

    <div id="printView">
      <div style="display:flex; justify-content:space-between; width:100%; align-items:center;">
        <div style="font-size:13px; color:var(--text-dim);">
          Her satırın başındaki <b>[ ▲ / ▼ ]</b> oklarıyla satırdaki ölçü sayısını ayarlayabilirsiniz.
        </div>
        <button id="printBtn" class="btn btn-primary" onclick="window.print()">🖨 Sayfayı Yazdır (A4)</button>
      </div>

      <div class="a4-page" id="a4PageContainer">
        <div class="a4-header">
          <div class="a4-meta-left" contenteditable="true">
            <div><b>Yöre:</b> Sivas / Divriği</div>
            <div><b>Kaynak Kişi:</b> Âşık Veysel</div>
            <div><b>Süre:</b> 3:45</div>
          </div>
          <div class="a4-meta-center">
            <div class="a4-title" contenteditable="true">KARA TOPRAK</div>
          </div>
          <div class="a4-meta-right" contenteditable="true">
            <div><b>Derleyen:</b> TRT THM</div>
            <div><b>Hazırlayan:</b> Nota Editörü</div>
          </div>
        </div>

        <div id="a4StaveRows"></div>

        <div class="lyrics-container">
          <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:8px;">
            <b style="font-size:13px;">TÜRKÜ SÖZLERİ (KITALAR)</b>
            <span style="font-size:11px; color:#6b7280;">(Düzenlenebilir)</span>
          </div>
          <div class="lyrics-grid">
            <textarea class="lyrics-textarea" placeholder="1. Kıta:&#10;Güzelliğin on par'etmez&#10;Şu bendeki aşk olmasa&#10;Eğlenecek yer bulaman&#10;Gönlümdeki köşk olmasa"></textarea>
            <textarea class="lyrics-textarea" placeholder="2. Kıta / Bağlantı:&#10;Kim okurdu kim yazardı&#10;Bu düğümü kim çözerdi&#10;Koyun kurt ile gezerdi&#10;Fikir başka başk'olmasa"></textarea>
          </div>
        </div>
      </div>
    </div>
  </main>

  <footer>
    <div style="display: flex; gap: 8px; align-items: center; flex-wrap: wrap;">
      <span style="font-weight: 700;">KISAYOLLAR:</span>
      <div><span class="shortcut-pill">A-S-D-F-G-H-J</span> Süre (1/1 - 1/16)</div>
      <div><span class="shortcut-pill" style="background:#0284c7; color:#fff;">K</span> Es</div>
      <div><span class="shortcut-pill" style="background:#eab308; color:#000; font-weight:900;">0 - 5</span> Parmak No</div>
      <div><span class="shortcut-pill">W / E / R</span> Tezene (↓/↑/Yok)</div>
      <div><span class="shortcut-pill">Y-U-I-O-P</span> Arıza (♮, ♭2, ♭, ♯, ♯3)</div>
      <div><span class="shortcut-pill">Z-X-C-V-B</span> Süsleme (Yok/v/^/▲/Çentik)</div>
    </div>
    <div style="display: flex; gap: 8px; align-items: center; flex-wrap: wrap;">
      <div><span class="shortcut-pill">Shift + Tık</span> Grup Seç</div>
      <div><span class="shortcut-pill">N / M / Ö / Ç</span> Bağ (Tek/Çift/Üçleme/Çöz)</div>
      <div><span class="shortcut-pill" style="background:#0284c7; color:#fff;">Space</span> Onayla</div>
      <div><span class="shortcut-pill" style="background:#059669; color:#fff;">Enter</span> Yeni Ölçü</div>
      <div style="color:var(--text-dim); font-size:10px;">(Röpriz, Senyo ve 1P-9P Perde fare ile seçilir)</div>
    </div>
  </footer>

  <script>
    // --- GÖMÜLÜ GERÇEK AKUSTİK ENSTRÜMAN SESLERİ (BASE64) ---
    const AUDIO_SAMPLES_B64 = {{
      kisa_sap: "{kisa_b64}",
      uzun_sap: "{uzun_b64}",
      cura: "{cura_b64}",
      ud: "{ud_b64}"
    }};

    // Temel ses perdesi (Root MIDI Note)
    const SAMPLE_ROOT_PITCH = {{
      kisa_sap: 64, // E4 (Kisakol Mi)
      uzun_sap: 62, // D4 (Kara Duzen Re)
      cura: 69,     // A4 (Bozuki La)
      ud: 57        // A3 (Emre Ud La)
    }};

    const DIATONIC_NAMES = ['Do', 'Re', 'Mi', 'Fa', 'Sol', 'La', 'Si'];
    const STEP_SEMITONES = {{
      '-5': -17, '-4': -15, '-3': -14, '-2': -12, '-1': -10, '0': -9, '1': -7, '2': -5, '3': -4,
      '4': -2, '5': 0, '6': 2, '7': 3, '8': 5, '9': 7, '10': 8, '11': 10, '12': 12, '13': 14, '14': 15, '15': 17, '16': 19
    }};
    const DURATION_VALUES = {{
      '1/1': 1.0, '1/2': 0.5, '1/4': 0.25, '1/8': 0.125, '1/16': 0.0625, '1/32': 0.03125, '1/64': 0.015625
    }};

    function getNoteDurationValue(note) {{
      if (!note) return 0.25;
      const base = DURATION_VALUES[note.duration] || 0.25;
      return note.isDotted ? base * 1.5 : base;
    }}
    function getMeterCapacity(meterStr) {{
      if (!meterStr || typeof meterStr !== 'string') return 1.0;
      const parts = meterStr.split('/');
      if (parts.length === 2) {{
        const num = parseFloat(parts[0]) || 4;
        const den = parseFloat(parts[1]) || 4;
        return (num / den); // 4/4 = 1.0, 5/8 = 0.625, 9/8 = 1.125 vs.
      }}
      return 1.0;
    }}

    function getStepY(step) {{
      return 130 - (step - 6) * 5;
    }}

    function getDefaultFingerNumber(step, accidental = 'natural', isRest = false) {{
      if (isRest) return 0;
      const noteNames = ['do', 're', 'mi', 'fa', 'sol', 'la', 'si'];
      const normIndex = ((step % 7) + 7) % 7;
      const noteName = noteNames[normIndex];
      const acc = accidental || 'natural';

      // 1. Re, Sol -> 0. parmak
      if (noteName === 're' && (acc === 'natural' || !acc)) return 0;
      if (noteName === 'sol' && (acc === 'natural' || !acc)) return 0;
      if (step === -2 && (acc === 'natural' || !acc)) return 0; // Alt tel boş tel La3

      // 2. Do -> 5. parmak (doğal)
      if (noteName === 'do' && (acc === 'natural' || !acc)) return 5;

      // 3. Do diyez 3 -> 3. parmak, Do diyez (normal) -> 4. parmak
      if (noteName === 'do' && acc === 'sharp3') return 3;
      if (noteName === 'do' && (acc === 'sharp' || acc.startsWith('sharp'))) return 4;

      // 4. Mi, Mi bemol, Mi bemol 2 -> 1. parmak
      if (noteName === 'mi') return 1;

      // 5. La, La bemol, La bemol 2 -> 1. parmak (alt tel 1. perde La)
      if (noteName === 'la') return 1;

      // 6. Fa, Si bemol -> 2. parmak
      if (noteName === 'fa' && (acc === 'natural' || !acc)) return 2;
      if (noteName === 'si' && (acc === 'flat' || acc === 'b1')) return 2;

      // 7. Si bemol 2, Fa diyez 3, Do diyez 3 -> 3. parmak
      if (noteName === 'si' && (acc === 'b2' || acc === 'b4')) return 3;
      if (noteName === 'fa' && acc === 'sharp3') return 3;

      // 8. Fa diyez, Si (doğal), Do diyez -> 4. parmak
      if (noteName === 'fa' && (acc === 'sharp' || acc.startsWith('sharp'))) return 4;
      if (noteName === 'si' && (acc === 'natural' || !acc)) return 4;

      return 1;
    }}

    function getDiatonicPitchInfo(step, accidental, isRest) {{
      if (isRest) return {{ baseName: "Es", octave: 0, solfege: "Es" }};
      const normalized = (step % 7 + 7) % 7;
      const baseName = DIATONIC_NAMES[normalized];
      const octave = Math.floor(step / 7) + 4;
      let accSymbol = '';
      if (accidental === 'b2') accSymbol = '♭2';
      else if (accidental === 'flat') accSymbol = '♭';
      else if (accidental === 'sharp') accSymbol = '♯';
      else if (accidental === 'sharp3') accSymbol = '♯3';
      return {{ baseName, octave, solfege: `${{baseName}}${{accSymbol}}` }};
    }}

    function getNotePitches(note) {{
      const list = [{{ step: note.step, accidental: note.accidental }}];
      if (Array.isArray(note.extraPitches)) {{
        note.extraPitches.forEach(p => list.push(p));
      }}
      return list;
    }}

    function getNoteFrequencies(note) {{
      return getNotePitches(note).map(p => calculateFrequency(p.step, p.accidental));
    }}
    function calculateFrequency(step, accidental) {{
      const baseSemitone = STEP_SEMITONES[step] !== undefined ? STEP_SEMITONES[step] : (step - 5) * 1.7;
      let centsOffset = 0;
      const comaCent = 22.64; // Türk Müziği 1 Koma (Holder koması ≈ 22.64 cent)
      if (accidental === 'sharp') centsOffset = 100;
      else if (accidental === 'flat') centsOffset = -100;
      else if (typeof accidental === 'string' && accidental.startsWith('b')) {{
        const cNum = parseInt(accidental.replace('b', ''), 10) || 2;
        centsOffset = -cNum * comaCent;
      }} else if (typeof accidental === 'string' && accidental.startsWith('sharp')) {{
        const cNum = parseInt(accidental.replace('sharp', ''), 10) || 3;
        centsOffset = cNum * comaCent;
      }}
      const freq = 440 * Math.pow(2, (baseSemitone * 100 + centsOffset) / 1200);
      return (isNaN(freq) || !isFinite(freq)) ? 440 : Math.max(80, Math.min(2400, freq));
    }}

    function getMeasureDurationSum(measure) {{
      return measure.notes.reduce((sum, n) => sum + getNoteDurationValue(n), 0);
    }}

    // --- GERÇEK SES ÖRNEKLERİNİ ÇALMA MOTORU ---
    let globalAudioCtx = null;
    const decodedBuffers = {{}};

    function getAudioContext() {{
      if (!globalAudioCtx) {{
        const AudioClass = window.AudioContext || window.webkitAudioContext;
        globalAudioCtx = new AudioClass();
      }}
      if (globalAudioCtx.state === 'suspended') {{
        globalAudioCtx.resume().catch(() => {{}});
      }}
      return globalAudioCtx;
    }}

    async function loadAudioSample(presetKey) {{
      if (decodedBuffers[presetKey]) return decodedBuffers[presetKey];
      const ctx = getAudioContext();
      const b64 = AUDIO_SAMPLES_B64[presetKey];
      if (!b64) return null;

      try {{
        const binaryString = atob(b64);
        const len = binaryString.length;
        const bytes = new Uint8Array(len);
        for (let i = 0; i < len; i++) bytes[i] = binaryString.charCodeAt(i);
        const buffer = await ctx.decodeAudioData(bytes.buffer);
        decodedBuffers[presetKey] = buffer;
        return buffer;
      }} catch (err) {{
        console.warn("Audio decode error:", err);
        return null;
      }}
    }}

    // Önceden hazırla
    window.addEventListener("load", () => {{
      setTimeout(() => {{
        loadAudioSample('kisa_sap');
        loadAudioSample('uzun_sap');
        loadAudioSample('cura');
        loadAudioSample('ud');
      }}, 500);
    }});

    async function playInstrumentSound(frequency, duration = 0.35) {{
      try {{
        const ctx = getAudioContext();
        const preset = appState.soundPreset;
        let buffer = decodedBuffers[preset];
        if (!buffer) buffer = await loadAudioSample(preset);

        const freqs = Array.isArray(frequency) ? frequency : [frequency];

        freqs.forEach(freq => {{
          if (buffer) {{
            // Gerçek Akustik Örnek Çalma (Polifonik / Karar sesleri desteği)
            const rootMidi = SAMPLE_ROOT_PITCH[preset] || 60;
            const rootFreq = 440 * Math.pow(2, (rootMidi - 69) / 12);
            const rate = freq / rootFreq;

            const src = ctx.createBufferSource();
            src.buffer = buffer;
            src.playbackRate.value = Math.max(0.2, Math.min(5.0, rate));

            const gain = ctx.createGain();
            const now = ctx.currentTime;
            gain.gain.setValueAtTime(0.75, now);
            gain.gain.exponentialRampToValueAtTime(0.001, now + Math.max(0.4, duration * 1.5));

            src.connect(gain);
            gain.connect(ctx.destination);
            src.start(now);
            src.stop(now + Math.max(0.4, duration * 1.5));
          }} else {{
            // Yedek osilatör
            const osc = ctx.createOscillator();
            const gain = ctx.createGain();
            osc.frequency.value = freq;
            gain.gain.setValueAtTime(0.25, ctx.currentTime);
            gain.gain.exponentialRampToValueAtTime(0.001, ctx.currentTime + duration);
            osc.connect(gain); gain.connect(ctx.destination);
            osc.start(); osc.stop(ctx.currentTime + duration);
          }}
        }});
      }} catch (e) {{}}
    }}

    // --- UYGULAMA DURUMU (APP STATE) ---
    const appState = {{
      viewMode: 'editor',
      theme: 'dark',
      soundPreset: 'kisa_sap',
      meter: '4/4',
      keySignature: 'b2_si',
      activeMeasureIndex: 0,
      selectedNoteId: null,
      rangeSelection: [],
      hideGhost: false,
      isPlaying: false,
      playingNoteId: null,

      candidateStep: 6,
      inputDuration: '1/4',
      inputAccidental: 'natural',
      inputTezene: 'down',
      inputOrnament: 'none',
      inputFinger: 1,
      inputLyric: '',

      printRowCapacities: [4, 4, 4, 4, 4],

      measures: [
        {{
          id: 'm-1', meter: '4/4', repeatStart: true, repeatEnd: false, senyoStart: true, senyoEnd: false, dolap: 'none', perde: '1P',
          notes: [
            {{ id: 'n-1-1', step: 6, duration: '1/4', accidental: 'b2', tezene: 'down', ornament: 'none', finger: 1, isRest: false, beam: 'none', lyric: 'Ka-' }},
            {{ id: 'n-1-2', step: 7, duration: '1/8', accidental: 'natural', tezene: 'down', ornament: 'carpma', finger: 2, isRest: false, beam: 'none', lyric: 'ti-' }},
            {{ id: 'n-1-3', step: 8, duration: '1/8', accidental: 'natural', tezene: 'up', ornament: 'none', finger: 0, isRest: false, beam: 'none', lyric: 'bim' }},
            {{ id: 'n-1-4', step: 9, duration: '1/4', accidental: 'natural', tezene: 'down', ornament: 'slash', finger: 1, isRest: false, beam: 'none', lyric: 'göz-' }},
            {{ id: 'n-1-5', step: 0, duration: '1/4', accidental: 'natural', tezene: 'none', ornament: 'none', finger: 0, isRest: true, beam: 'none', lyric: '' }}
          ]
        }},
        {{
          id: 'm-2', meter: '4/4', repeatStart: false, repeatEnd: true, senyoStart: false, senyoEnd: true, dolap: '1', perde: 'none',
          notes: [
            {{ id: 'n-2-1', step: 6, duration: '1/4', accidental: 'b2', tezene: 'down', ornament: 'none', finger: 1, isRest: false, beam: 'none', lyric: 'ay-' }},
            {{ id: 'n-2-2', step: 5, duration: '1/8', accidental: 'natural', tezene: 'up', ornament: 'cekme', finger: 0, isRest: false, beam: 'none', lyric: 'dın' }},
            {{ id: 'n-2-3', step: 4, duration: '1/8', accidental: 'natural', tezene: 'down', ornament: 'none', finger: 2, isRest: false, beam: 'none', lyric: 'ol-' }},
            {{ id: 'n-2-4', step: 3, duration: '1/4', accidental: 'natural', tezene: 'up', ornament: 'none', finger: 1, isRest: false, beam: 'none', lyric: 'sun' }},
            {{ id: 'n-2-5', step: 2, duration: '1/4', accidental: 'natural', tezene: 'down', ornament: 'none', finger: 0, isRest: false, beam: 'none', lyric: 'hey' }}
          ]
        }}
      ]
    }};

    let warningTimer = null;
    function showWarning(msg) {{
      const alertBox = document.getElementById("warningAlert");
      document.getElementById("warningMsgText").textContent = msg;
      alertBox.style.display = "inline-flex";
      if (warningTimer) clearTimeout(warningTimer);
      warningTimer = setTimeout(() => {{ alertBox.style.display = "none"; }}, 3500);
    }}

    // DOM Elementleri
    const scoreSvg = document.getElementById("scoreSvg");
    const editorView = document.getElementById("editorView");
    const printView = document.getElementById("printView");
    const tabEditor = document.getElementById("tabEditor");
    const tabPrint = document.getElementById("tabPrint");

    const soundPresetSelect = document.getElementById("soundPresetSelect");
    const playBtn = document.getElementById("playBtn");
    const saveProjectBtn = document.getElementById("saveProjectBtn");
    const loadProjectBtn = document.getElementById("loadProjectBtn");
    const projectFileInput = document.getElementById("projectFileInput");
    const exportSvgBtn = document.getElementById("exportSvgBtn");
    const themeBtn = document.getElementById("themeBtn");

    const keySigSelect = document.getElementById("keySigSelect");
    const meterNum = document.getElementById("meterNum");
    const meterDenom = document.getElementById("meterDenom");
    const repeatStartBtn = document.getElementById("repeatStartBtn");
    const repeatEndBtn = document.getElementById("repeatEndBtn");
    const senyoStartBtn = document.getElementById("senyoStartBtn");
    const senyoEndBtn = document.getElementById("senyoEndBtn");
    const insertMeasureBtn = document.getElementById("insertMeasureBtn");
    const deleteMeasureBtn = document.getElementById("deleteMeasureBtn");

    const lyricInput = document.getElementById("lyricInput");
    const commitBtn = document.getElementById("commitBtn");
    const restBtn = document.getElementById("restBtn");
    const btnBeamSingle = document.getElementById("btnBeamSingle");
    const btnBeamDouble = document.getElementById("btnBeamDouble");
    const btnBeamBreak = document.getElementById("btnBeamBreak");

    const selectedNoteBox = document.getElementById("selectedNoteBox");
    const selectedNoteText = document.getElementById("selectedNoteText");
    const deleteNoteBtn = document.getElementById("deleteNoteBtn");
    const deselectBtn = document.getElementById("deselectBtn");

    const measureNumText = document.getElementById("measureNumText");
    const capacityProgress = document.getElementById("capacityProgress");
    const capacityText = document.getElementById("capacityText");
    const candidateNoteText = document.getElementById("candidateNoteText");

    // --- RENDER MOTORU ---
        function scrollToActiveMeasure() {{
      if (appState.viewMode !== 'editor') return;
      const container = document.querySelector('main');
      if (!container) return;
      const svgElem = document.getElementById('scoreSvg');
      if (!svgElem) return;

      const mIdx = appState.activeMeasureIndex;
      const count = appState.measures.length;
      if (count === 0) return;

      // Ölçülerin X konumlarını hesapla
      let curX = 110 + 46 + 48 + 42; // startX + clef + keysig + timesig
      for (let i = 0; i < mIdx; i++) {{
        const m = appState.measures[i];
        const mCount = Math.max(m.notes.length, 1);
        curX += Math.max(220, mCount * 64 + 48) + 24;
      }}
      const curM = appState.measures[mIdx];
      const curWidth = curM ? Math.max(220, Math.max(curM.notes.length, 1) * 64 + 48) : 220;
      const targetCenterX = curX + (curWidth / 2);

      const contWidth = container.clientWidth;
      const scrollTarget = targetCenterX - (contWidth / 2);
      container.scrollTo({{ left: Math.max(0, scrollTarget), behavior: 'smooth' }});
    }}

    function render() {{
      if (appState.viewMode === 'editor') {{
        renderEditorSingleStave();
      }} else {{
        renderPrintMultiStave();
      }}
      updateStatusPanel();
      scrollToActiveMeasure();
    }}

    function renderEditorSingleStave() {{
      while (scoreSvg.firstChild) scoreSvg.removeChild(scoreSvg.firstChild);

      const staveLinesY = [110, 120, 130, 140, 150];
      const startX = 110;
      const clefWidth = 46;
      const keySigCounts = {{
        none: 0, b2_si: 1, b1_si: 1, b4_si: 1, flat_si: 1, sharp_fa: 1, sharp_do: 1, b2_mi: 1, flat_mi: 1,
        b2_si_fa_sharp: 2, b2_si_mi: 2, flat_si_mi: 2, sharp_fa_do: 2,
        b2_si_fa_sharp_do_sharp: 3, flat_si_mi_la: 3, sharp_fa_do_sol: 3
      }};
      const accCnt = keySigCounts[appState.keySignature] !== undefined ? keySigCounts[appState.keySignature] : (appState.keySignature === 'none' ? 0 : 1);
      const keySigWidth = accCnt === 0 ? 0 : accCnt * 16 + 12;
      const timeSigX = startX + clefWidth + keySigWidth + 12;
      const firstMeasureX = timeSigX + 30;
      const measureSpacing = 24;

      let currentMeasureX = firstMeasureX;
      const measureLayouts = appState.measures.map((m, mIdx) => {{
        const count = Math.max(m.notes.length, 1);
        const mWidth = Math.max(220, count * 64 + 48);
        const layout = {{
          measure: m,
          mIdx,
          startX: currentMeasureX,
          endX: currentMeasureX + mWidth,
          width: mWidth,
          isActive: mIdx === appState.activeMeasureIndex
        }};
        currentMeasureX += mWidth + measureSpacing;
        return layout;
      }});

      const totalWidth = Math.max(currentMeasureX + 80, 1050);
      scoreSvg.setAttribute("width", totalWidth);
      scoreSvg.setAttribute("viewBox", `0 0 ${{totalWidth}} 280`);

      renderCleanLayerLabels(scoreSvg, 8);

      // Porte Çizgileri
      const staveG = document.createElementNS("http://www.w3.org/2000/svg", "g");
      staveLinesY.forEach(y => {{
        const line = document.createElementNS("http://www.w3.org/2000/svg", "line");
        line.setAttribute("x1", startX - 15); line.setAttribute("y1", y);
        line.setAttribute("x2", totalWidth - 30); line.setAttribute("y2", y);
        line.setAttribute("stroke", "var(--stave-line)"); line.setAttribute("stroke-width", "1.3");
        staveG.appendChild(line);
      }});
      scoreSvg.appendChild(staveG);

      // ESTETİK SMUFL SOL ANAHTARI (Merkez helezonu tam 2. Sol çizgisi y=140 etrafında)
      renderAuthenticTrebleClef(scoreSvg, startX - 6, 140, 1.82);

      renderKeySignature(scoreSvg, startX + clefWidth + 6, appState.keySignature);
      renderTimeSignature(scoreSvg, timeSigX, 110, appState.meter);

      measureLayouts.forEach(layout => {{
        renderMeasureGroup(scoreSvg, layout, staveLinesY);
      }});

      if (!appState.hideGhost && !appState.selectedNoteId) {{
        renderGhostNote(scoreSvg, measureLayouts);
      }}
    }}

    function renderPrintMultiStave() {{
      const container = document.getElementById("a4StaveRows");
      container.innerHTML = "";

      let measureIdx = 0;
      let rowIdx = 0;

      while (measureIdx < appState.measures.length || rowIdx < 5) {{
        const rowCapacity = appState.printRowCapacities[rowIdx] || 4;
        const rowMeasures = appState.measures.slice(measureIdx, measureIdx + rowCapacity);

        const rowDiv = document.createElement("div");
        rowDiv.className = "a4-stave-row";

        const controlDiv = document.createElement("div");
        controlDiv.className = "row-measure-control";
        controlDiv.innerHTML = `
          <button class="row-btn" onclick="changeRowCapacity(${{rowIdx}}, 1)">▲</button>
          <span>${{rowCapacity}}</span>
          <button class="row-btn" onclick="changeRowCapacity(${{rowIdx}}, -1)">▼</button>
        `;
        rowDiv.appendChild(controlDiv);

        const rowSvg = document.createElementNS("http://www.w3.org/2000/svg", "svg");
        rowSvg.setAttribute("width", "770");
        rowSvg.setAttribute("height", "150");
        rowSvg.setAttribute("viewBox", "0 0 770 150");
        rowSvg.style.display = "block";

        renderPrintRowSvg(rowSvg, rowMeasures, measureIdx, rowIdx === 0);
        rowDiv.appendChild(rowSvg);
        container.appendChild(rowDiv);

        measureIdx += rowCapacity;
        rowIdx++;
        if (measureIdx >= appState.measures.length && rowIdx >= 4) break;
      }}
    }}

    window.changeRowCapacity = function(rowIdx, delta) {{
      const cur = appState.printRowCapacities[rowIdx] || 4;
      appState.printRowCapacities[rowIdx] = Math.max(1, Math.min(8, cur + delta));
      render();
    }};

    function renderPrintRowSvg(svg, measures, startMeasureIdx, isFirstRow) {{
      const staveLinesY = [55, 65, 75, 85, 95];
      const totalWidth = 760;

      staveLinesY.forEach(y => {{
        const line = document.createElementNS("http://www.w3.org/2000/svg", "line");
        line.setAttribute("x1", "10"); line.setAttribute("y1", y);
        line.setAttribute("x2", totalWidth); line.setAttribute("y2", y);
        line.setAttribute("stroke", "#1f2937"); line.setAttribute("stroke-width", "1.2");
        svg.appendChild(line);
      }});

      renderAuthenticTrebleClef(svg, 14, 85, 1.45, "#1f2937");

      let currentX = 55;
      if (isFirstRow) {{
        renderKeySignature(svg, currentX, appState.keySignature, true);
        currentX += 30;
        renderTimeSignature(svg, currentX, 55, appState.meter, "#1f2937");
        currentX += 30;
      }}

      if (measures.length === 0) return;
      const mWidth = (totalWidth - currentX) / measures.length;

      measures.forEach((m, idx) => {{
        const mStartX = currentX + idx * mWidth;
        const mEndX = mStartX + mWidth;

        if (m.dolap && m.dolap !== 'none') {{
          renderDolapBracket(svg, mStartX, mEndX, m.dolap, 18, "#7e22ce");
        }}

        if (m.senyoStart) renderAuthenticSegno(svg, mStartX + 20, 32, "#d97706");
        if (m.perde && m.perde !== 'none') {{
          const pX = m.senyoStart ? mStartX + 42 : mStartX + 20;
          renderPerdeBadge(svg, pX, 32, m.perde, true);
        }}
        if (m.senyoEnd) renderAuthenticSegno(svg, mEndX - 20, 32, "#d97706");

        if (m.repeatStart) {{
          renderRepeatBar(svg, mStartX, 55, 95, true, "#1f2937", "#e11d48");
        }} else if (idx > 0) {{
          const bl = document.createElementNS("http://www.w3.org/2000/svg", "line");
          bl.setAttribute("x1", mStartX); bl.setAttribute("y1", "55"); bl.setAttribute("x2", mStartX); bl.setAttribute("y2", "95");
          bl.setAttribute("stroke", "#1f2937"); bl.setAttribute("stroke-width", "1.2");
          svg.appendChild(bl);
        }}

        const noteCount = Math.max(m.notes.length, 1);
        const noteSlot = (mWidth - 24) / noteCount;
        const notePositions = [];

        const printBeamedIds = new Set();
        const printBeamStemDir = new Map();
        let tempPrintGroup = [];
        for (let i = 0; i < m.notes.length; i++) {{
          const n = m.notes[i];
          if (!n.isRest && (n.beam === 'single' || n.beam === 'double')) {{
            tempPrintGroup.push(n);
          }} else {{
            if (tempPrintGroup.length >= 2) {{
              let upC = 0, downC = 0;
              tempPrintGroup.forEach(it => (it.step <= 6 ? upC++ : downC++));
              const gStemUp = upC >= downC;
              tempPrintGroup.forEach(it => {{
                printBeamedIds.add(it.id);
                printBeamStemDir.set(it.id, gStemUp);
              }});
            }}
            tempPrintGroup = [];
          }}
        }}
        if (tempPrintGroup.length >= 2) {{
          let upC = 0, downC = 0;
          tempPrintGroup.forEach(it => (it.step <= 6 ? upC++ : downC++));
          const gStemUp = upC >= downC;
          tempPrintGroup.forEach(it => {{
            printBeamedIds.add(it.id);
            printBeamStemDir.set(it.id, gStemUp);
          }});
        }}

        m.notes.forEach((n, nIdx) => {{
          const colX = mStartX + 16 + nIdx * noteSlot;
          notePositions.push({{ note: n, colX }});
          const isPrintBeamed = printBeamedIds.has(n.id);
          const forcedPrintStemUp = printBeamStemDir.has(n.id) ? printBeamStemDir.get(n.id) : null;
          renderPrintNote(svg, n, colX, isPrintBeamed, forcedPrintStemUp);
        }});

        renderBeamsForPrint(svg, notePositions);
        renderTripletBrackets(svg, notePositions, true);

        const isLastM = (startMeasureIdx + idx) === appState.measures.length - 1;
        if (m.repeatEnd) {{
          renderRepeatBar(svg, mEndX, 55, 95, false, "#1f2937", "#e11d48");
        }} else if (m.barType === 'final' || isLastM) {{
          const l1 = document.createElementNS("http://www.w3.org/2000/svg", "line");
          l1.setAttribute("x1", mEndX - 3.5); l1.setAttribute("y1", "55"); l1.setAttribute("x2", mEndX - 3.5); l1.setAttribute("y2", "95");
          l1.setAttribute("stroke", "#1f2937"); l1.setAttribute("stroke-width", "1.2");
          const l2 = document.createElementNS("http://www.w3.org/2000/svg", "line");
          l2.setAttribute("x1", mEndX); l2.setAttribute("y1", "55"); l2.setAttribute("x2", mEndX); l2.setAttribute("y2", "95");
          l2.setAttribute("stroke", "#1f2937"); l2.setAttribute("stroke-width", "3.0");
          svg.appendChild(l1); svg.appendChild(l2);
        }} else if (m.barType === 'double') {{
          const l1 = document.createElementNS("http://www.w3.org/2000/svg", "line");
          l1.setAttribute("x1", mEndX - 3); l1.setAttribute("y1", "55"); l1.setAttribute("x2", mEndX - 3); l1.setAttribute("y2", "95");
          l1.setAttribute("stroke", "#1f2937"); l1.setAttribute("stroke-width", "1.2");
          const l2 = document.createElementNS("http://www.w3.org/2000/svg", "line");
          l2.setAttribute("x1", mEndX); l2.setAttribute("y1", "55"); l2.setAttribute("x2", mEndX); l2.setAttribute("y2", "95");
          l2.setAttribute("stroke", "#1f2937"); l2.setAttribute("stroke-width", "1.2");
          svg.appendChild(l1); svg.appendChild(l2);
        }} else {{
          const bl = document.createElementNS("http://www.w3.org/2000/svg", "line");
          bl.setAttribute("x1", mEndX); bl.setAttribute("y1", "55"); bl.setAttribute("x2", mEndX); bl.setAttribute("y2", "95");
          bl.setAttribute("stroke", "#1f2937"); bl.setAttribute("stroke-width", "1.2");
          svg.appendChild(bl);
        }}
      }});
    }}

    function renderBeamsForPrint(parent, notePositions) {{
      let currentGroup = [];
      for (let i = 0; i < notePositions.length; i++) {{
        const item = notePositions[i];
        if (!item.note.isRest && (item.note.beam === 'single' || item.note.beam === 'double')) {{
          currentGroup.push(item);
        }} else {{
          if (currentGroup.length >= 2) drawBeamGroupPrint(parent, currentGroup);
          currentGroup = [];
        }}
      }}
      if (currentGroup.length >= 2) drawBeamGroupPrint(parent, currentGroup);
    }}

    function drawBeamGroupPrint(parent, group) {{
      if (!group || group.length < 2) return;
      let upC = 0, downC = 0;
      group.forEach(it => {{ if (it.note.step <= 6) upC++; else downC++; }});
      const stemUp = upC >= downC;

      const pts = group.map(it => {{
        const allP = getNotePitches(it.note);
        const steps = allP.map(p => p.step);
        const minStep = Math.min(...steps);
        const maxStep = Math.max(...steps);
        const stemX = stemUp ? it.colX + 4.8 : it.colX - 4.8;
        const bottomPitchY = 75 - (minStep - 6) * 5;
        const topPitchY = 75 - (maxStep - 6) * 5;
        const stemEndY = stemUp ? topPitchY - 26 : bottomPitchY + 26;
        return {{ x: stemX, y: stemEndY, note: it.note }};
      }});

      const startPt = pts[0];
      const endPt = pts[pts.length - 1];

      function getBeamY(x) {{
        if (Math.abs(endPt.x - startPt.x) < 0.001) return startPt.y;
        const t = (x - startPt.x) / (endPt.x - startPt.x);
        return startPt.y + t * (endPt.y - startPt.y);
      }}

      // Sap boylarını kiriş çizgisiyle pürüzsüz kesiştirmek için sap uçlarına uzatıcı çizgi
      pts.forEach(p => {{
        const targetBeamY = getBeamY(p.x);
        if (Math.abs(targetBeamY - p.y) > 0.5) {{
          const extLine = document.createElementNS("http://www.w3.org/2000/svg", "line");
          extLine.setAttribute("x1", p.x); extLine.setAttribute("y1", p.y);
          extLine.setAttribute("x2", p.x); extLine.setAttribute("y2", targetBeamY);
          extLine.setAttribute("stroke", "#111827"); extLine.setAttribute("stroke-width", "1.5");
          parent.appendChild(extLine);
        }}
      }});

      const beamOffset = stemUp ? 4.8 : -4.8;

      // Kirişleri ardışık çiftler (1-2, 2-3, 3-4...) halinde çiz!
      for (let i = 0; i < pts.length - 1; i++) {{
        const cur = pts[i];
        const next = pts[i + 1];

        // 1. Ana Kiriş (1/8 veya 1/16 olan tüm bağlı komşular arasına):
        const b1 = document.createElementNS("http://www.w3.org/2000/svg", "line");
        b1.setAttribute("x1", cur.x); b1.setAttribute("y1", getBeamY(cur.x));
        b1.setAttribute("x2", next.x); b1.setAttribute("y2", getBeamY(next.x));
        b1.setAttribute("stroke", "#111827"); b1.setAttribute("stroke-width", "3.2");
        parent.appendChild(b1);

        // 2. İkinci Kiriş (1/16):
        const curIs16 = (cur.note.duration === '1/16' || cur.note.beam === 'double');
        const nextIs16 = (next.note.duration === '1/16' || next.note.beam === 'double');

        if (curIs16 && nextIs16) {{
          const b2 = document.createElementNS("http://www.w3.org/2000/svg", "line");
          b2.setAttribute("x1", cur.x); b2.setAttribute("y1", getBeamY(cur.x) + beamOffset);
          b2.setAttribute("x2", next.x); b2.setAttribute("y2", getBeamY(next.x) + beamOffset);
          b2.setAttribute("stroke", "var(--stave-note)"); b2.setAttribute("stroke-width", "2.5");
          parent.appendChild(b2);
        }} else if (curIs16 && !nextIs16) {{
          const b2 = document.createElementNS("http://www.w3.org/2000/svg", "line");
          const beamletX = cur.x + Math.min(16, (next.x - cur.x) * 0.4);
          b2.setAttribute("x1", cur.x); b2.setAttribute("y1", getBeamY(cur.x) + beamOffset);
          b2.setAttribute("x2", beamletX); b2.setAttribute("y2", getBeamY(beamletX) + beamOffset);
          b2.setAttribute("stroke", "var(--stave-note)"); b2.setAttribute("stroke-width", "2.5");
          parent.appendChild(b2);
        }} else if (!curIs16 && nextIs16) {{
          const b2 = document.createElementNS("http://www.w3.org/2000/svg", "line");
          const beamletX = next.x - Math.min(16, (next.x - cur.x) * 0.4);
          b2.setAttribute("x1", beamletX); b2.setAttribute("y1", getBeamY(beamletX) + beamOffset);
          b2.setAttribute("x2", next.x); b2.setAttribute("y2", getBeamY(next.x) + beamOffset);
          b2.setAttribute("stroke", "var(--stave-note)"); b2.setAttribute("stroke-width", "2.5");
          parent.appendChild(b2);
        }}
      }}
    }}

    function renderPrintNote(svg, note, x, isActuallyBeamed, forcedStemUp = null) {{
      const pitchY = 75 - (note.step - 6) * 5;

      if (note.isRest) {{
        renderRestGlyph(svg, x, 75, note.duration, "#111827", !!note.isDotted);
        const solfTxt = document.createElementNS("http://www.w3.org/2000/svg", "text");
        solfTxt.setAttribute("x", x); solfTxt.setAttribute("y", "114"); solfTxt.setAttribute("font-size", "10"); solfTxt.setAttribute("font-weight", "bold"); solfTxt.setAttribute("text-anchor", "middle"); solfTxt.setAttribute("fill", "#6b7280");
        solfTxt.textContent = "Es";
        svg.appendChild(solfTxt);
        return;
      }}

      if (note.tezene === 'down') renderArrow(svg, x, 22, 'down', "#0284c7");
      else if (note.tezene === 'up') renderArrow(svg, x, 22, 'up', "#d97706");

      if (note.ornament && note.ornament !== 'none') {{
        renderOrnamentDisplay(svg, x, 46, note.ornament, "#db2777");
      }}

      const allPitches = getNotePitches(note);
      const isHollow = note.duration === '1/1' || note.duration === '1/2' || note.duration === '3/4';

      allPitches.forEach(p => {{
        const pY = 75 - (p.step - 6) * 5;
        renderLedgerLines(svg, x, p.step, 55, 95, 10, "#1f2937");
        if (shouldRenderAccidental(p.step, p.accidental, appState.keySignature)) {{
          renderAccidentalGlyph(svg, x - 13, pY, p.accidental, true);
        }}
      }});

      allPitches.forEach(p => {{
        const pY = 75 - (p.step - 6) * 5;
        const head = document.createElementNS("http://www.w3.org/2000/svg", "ellipse");
        head.setAttribute("cx", x); head.setAttribute("cy", pY); head.setAttribute("rx", "5.5"); head.setAttribute("ry", "4.2");
        head.setAttribute("transform", `rotate(-25, ${{x}}, ${{pY}})`);
        head.setAttribute("fill", isHollow ? "#ffffff" : "#111827");
        head.setAttribute("stroke", "#111827"); head.setAttribute("stroke-width", "1.8");
        svg.appendChild(head);

        if (note.isDotted || note.duration === '3/4' || note.duration === '3/8') {{
          const dot = document.createElementNS("http://www.w3.org/2000/svg", "circle");
          dot.setAttribute("cx", x + 8.5); dot.setAttribute("cy", pY); dot.setAttribute("r", "2"); dot.setAttribute("fill", "#111827");
          svg.appendChild(dot);
        }}
      }});

      if (note.duration !== '1/1') {{
        const steps = allPitches.map(p => p.step);
        const minStep = Math.min(...steps);
        const maxStep = Math.max(...steps);
        const stemUp = (forcedStemUp !== null) ? forcedStemUp : (maxStep <= 6);
        const stemX = stemUp ? x + 4.8 : x - 4.8;

        const bottomPitchY = 75 - (minStep - 6) * 5;
        const topPitchY = 75 - (maxStep - 6) * 5;

        const stemStartY = stemUp ? bottomPitchY : topPitchY;
        const stemEndY = stemUp ? topPitchY - 26 : bottomPitchY + 26;

        const stem = document.createElementNS("http://www.w3.org/2000/svg", "line");
        stem.setAttribute("x1", stemX); stem.setAttribute("y1", stemStartY);
        stem.setAttribute("x2", stemX); stem.setAttribute("y2", stemEndY);
        stem.setAttribute("stroke", "#111827"); stem.setAttribute("stroke-width", "1.5");
        svg.appendChild(stem);

        if (note.ornament === 'slash') {{
          renderStemSlashes(svg, stemX, stemUp ? topPitchY - 14 : bottomPitchY + 14, "#111827");
        }}

        if (!isActuallyBeamed) {{
          renderFlagGlyph(svg, stemX, stemEndY, note.duration, stemUp, "#111827");
        }}
      }}

      const printPitches = getNotePitches(note);
      const printSolfLabel = printPitches.map(p => getDiatonicPitchInfo(p.step, p.accidental, false).solfege).join('/');
      const sInfo = {{ solfege: printSolfLabel }};
      // 1. Satır: Nota okunuşu (Solfej)
      const solfTxt = document.createElementNS("http://www.w3.org/2000/svg", "text");
      solfTxt.setAttribute("x", x); solfTxt.setAttribute("y", "114"); solfTxt.setAttribute("font-size", "10"); solfTxt.setAttribute("font-weight", "bold"); solfTxt.setAttribute("text-anchor", "middle"); solfTxt.setAttribute("fill", "#0369a1");
      solfTxt.textContent = sInfo.solfege;
      svg.appendChild(solfTxt);

      // 2. Satır: Tele basan parmak numarası
      let fNum = note.finger !== undefined ? note.finger : getDefaultFingerNumber(note.step);
      if (fNum === -1) fNum = 3;
      const fTxt = document.createElementNS("http://www.w3.org/2000/svg", "text");
      fTxt.setAttribute("x", x); fTxt.setAttribute("y", "128"); fTxt.setAttribute("font-size", "10"); fTxt.setAttribute("font-weight", "bold"); fTxt.setAttribute("text-anchor", "middle");
      fTxt.setAttribute("fill", "#b45309");
      fTxt.textContent = fNum;
      svg.appendChild(fTxt);

      // 3. Satır: Türkü sözü
      if (note.lyric && note.lyric.trim() !== '') {{
        const lyrTxt = document.createElementNS("http://www.w3.org/2000/svg", "text");
        lyrTxt.setAttribute("x", x); lyrTxt.setAttribute("y", "143"); lyrTxt.setAttribute("font-size", "11"); lyrTxt.setAttribute("font-style", "italic"); lyrTxt.setAttribute("text-anchor", "middle"); lyrTxt.setAttribute("fill", "#374151");
        lyrTxt.textContent = note.lyric;
        svg.appendChild(lyrTxt);
      }}
    }}

    function shouldRenderAccidental(step, accidental, keySig) {{
      if (!accidental || accidental === 'natural') return false;
      const isSi = (step % 7 + 7) % 7 === 6;
      const isFa = (step % 7 + 7) % 7 === 3;
      const isMi = (step % 7 + 7) % 7 === 2;
      const isDo = (step % 7 + 7) % 7 === 0;

      if (keySig.includes('si') && isSi) {{
        if (keySig.startsWith('b2_') && accidental === 'b2') return false;
        if (keySig.startsWith('b1_') && accidental === 'b1') return false;
        if (keySig.startsWith('b4_') && accidental === 'b4') return false;
        if (keySig.startsWith('flat_') && accidental === 'flat') return false;
      }}
      if (keySig.includes('fa_sharp') && isFa) {{
        if (keySig.includes('fa_sharp4') && accidental === 'sharp4') return false;
        if (!keySig.includes('fa_sharp4') && accidental === 'sharp') return false;
      }}
      if (keySig === 'sharp_fa' && isFa && accidental === 'sharp') return false;
      if (keySig.includes('mi') && isMi) {{
        if (keySig.includes('mi_b2') && accidental === 'b2') return false;
        if (keySig.includes('flat_si_mi') && accidental === 'flat') return false;
      }}
      if (keySig.includes('do_sharp') && isDo && accidental === 'sharp') return false;
      if (keySig.includes('sharp_fa_do') && (isFa || isDo) && accidental === 'sharp') return false;

      return true;
    }}

    // --- GERÇEK STANDART SOL ANAHTARI (G-CLEF) ---
    // Resmi SMuFL/Wikimedia G-Clef: 15.186 x 40.768, helezon 2. çizgide (y=26.0)
    function renderAuthenticTrebleClef(parent, x, y, scale = 1.82, color = "var(--stave-line)") {{
      const g = document.createElementNS("http://www.w3.org/2000/svg", "g");
      const translateY = y - 26.0 * scale;
      g.setAttribute("transform", `translate(${{x}}, ${{translateY}}) scale(${{scale}})`);
      const path = document.createElementNS("http://www.w3.org/2000/svg", "path");
      path.setAttribute("d", "m12.049 3.5296c0.305 3.1263-2.019 5.6563-4.0772 7.7014-0.9349 0.897-0.155 0.148-0.6437 0.594-0.1022-0.479-0.2986-1.731-0.2802-2.11 0.1304-2.6939 2.3198-6.5875 4.2381-8.0236 0.309 0.5767 0.563 0.6231 0.763 1.8382zm0.651 16.142c-1.232-0.906-2.85-1.144-4.3336-0.885-0.1913-1.255-0.3827-2.51-0.574-3.764 2.3506-2.329 4.9066-5.0322 5.0406-8.5394 0.059-2.232-0.276-4.6714-1.678-6.4836-1.7004 0.12823-2.8995 2.156-3.8019 3.4165-1.4889 2.6705-1.1414 5.9169-0.57 8.7965-0.8094 0.952-1.9296 1.743-2.7274 2.734-2.3561 2.308-4.4085 5.43-4.0046 8.878 0.18332 3.334 2.5894 6.434 5.8702 7.227 1.2457 0.315 2.5639 0.346 3.8241 0.099 0.2199 2.25 1.0266 4.629 0.0925 6.813-0.7007 1.598-2.7875 3.004-4.3325 2.192-0.5994-0.316-0.1137-0.051-0.478-0.252 1.0698-0.257 1.9996-1.036 2.26-1.565 0.8378-1.464-0.3998-3.639-2.1554-3.358-2.262 0.046-3.1904 3.14-1.7356 4.685 1.3468 1.52 3.833 1.312 5.4301 0.318 1.8125-1.18 2.0395-3.544 1.8325-5.562-0.07-0.678-0.403-2.67-0.444-3.387 0.697-0.249 0.209-0.059 1.193-0.449 2.66-1.053 4.357-4.259 3.594-7.122-0.318-1.469-1.044-2.914-2.302-3.792zm0.561 5.757c0.214 1.991-1.053 4.321-3.079 4.96-0.136-0.795-0.172-1.011-0.2626-1.475-0.4822-2.46-0.744-4.987-1.116-7.481 1.6246-0.168 3.4576 0.543 4.0226 2.184 0.244 0.577 0.343 1.197 0.435 1.812zm-5.1486 5.196c-2.5441 0.141-4.9995-1.595-5.6343-4.081-0.749-2.153-0.5283-4.63 0.8207-6.504 1.1151-1.702 2.6065-3.105 4.0286-4.543 0.183 1.127 0.366 2.254 0.549 3.382-2.9906 0.782-5.0046 4.725-3.215 7.451 0.5324 0.764 1.9765 2.223 2.7655 1.634-1.102-0.683-2.0033-1.859-1.8095-3.227-0.0821-1.282 1.3699-2.911 2.6513-3.198 0.4384 2.869 0.9413 6.073 1.3797 8.943-0.5054 0.1-1.0211 0.143-1.536 0.143z");
      path.setAttribute("fill", color);
      g.appendChild(path);
      parent.appendChild(g);
    }}

    // --- GERÇEK MÜZİKAL SENYO (SEGNO 𝄋) ---
    // Standart Segno vektörü: 29 x 44
    function renderAuthenticSegno(parent, x, y, color = "var(--senyo-color)") {{
      const g = document.createElementNS("http://www.w3.org/2000/svg", "g");
      const scale = 0.58;
      g.setAttribute("transform", `translate(${{x - 14.5 * scale}}, ${{y - 22.0 * scale}}) scale(${{scale}})`);
      const path = document.createElementNS("http://www.w3.org/2000/svg", "path");
      path.setAttribute("d", "m 0.9,8.8 c -0.1,1.1 -0.1,2.2 0.2,3.4 0.4,1.6 1.2,3.1 2,4.3 1.3,1.7 2.9,3.2 4.5,4.3 1.4,1.1 2.8,1.8 4.1,2.7 -3.5,6 -7.6,13.3 -10.9,19.1 l 3.9,0 c 3.3,-5.7 6.9,-12.3 9.9,-17.3 1.2,0.6 2.3,1.5 3.3,2.3 1.1,0.9 1.9,1.8 2.8,2.8 0.9,1.1 1.5,2.3 2.1,3.5 0.7,1.9 1.1,4.2 -0.5,6 -1,0.9 -2,1 -3,0.7 -1.1,-0.3 -1.8,-1.1 -2.1,-1.9 0.1,-0.4 0.8,-0.4 1.3,-1.2 0.7,-1.1 1,-2.2 0.8,-3.5 -0.2,-1.2 -0.8,-2.1 -1.7,-2.8 -0.6,-0.4 -1.3,-0.4 -1.9,-0.4 -0.6,-0.1 -1.4,0.1 -1.8,0.3 -0.5,0.3 -0.9,0.8 -1.2,1.4 -0.3,0.6 -0.4,1.4 -0.4,2.2 0.1,1.3 0.4,2.5 1,3.7 0.6,1.1 1.4,2 2.5,2.8 1.6,1.1 3.3,1.5 5.1,1.4 1.8,-0.2 3.4,-0.9 4.8,-2.3 C 27.1,38.8 28,37 28.2,34.9 28.3,33.8 28.3,32.7 28,31.5 27.8,30.6 27.5,29.8 27.2,29.1 26.7,27.6 25.3,26.2 24.3,25.2 23.5,24.4 22.6,23.6 21.5,22.8 20.1,21.7 18.7,21 17.4,20.1 20.9,14.1 25,6.8 28.3,1 L 24.4,1 C 21.2,6.6 17.4,13.2 14.5,18.3 13.4,17.9 12.1,16.8 11.1,16 10,15.1 9.1,14.3 8.3,13.2 7.4,12.1 6.8,11.1 6.2,9.7 5.9,8.9 5.7,8.1 5.6,7.2 5.4,5.7 5.7,4.7 6.7,3.6 c 1,-0.9 1.8,-1 3,-0.7 1.1,0.3 1.8,1 2.1,1.9 -0.4,0.5 -1,0.6 -1.3,1.2 -0.7,1.1 -1,2.2 -0.8,3.5 0.2,1.2 0.8,2.1 1.7,2.8 0.6,0.4 1.3,0.4 1.9,0.4 0.8,0 1.2,-0.1 1.8,-0.3 C 15.6,12.1 16,11.6 16.3,11 16.6,10.4 16.7,9.6 16.7,8.7 16.6,7.4 16.3,6.2 15.7,5.1 15.1,4 14.3,3.1 13.2,2.3 12.5,1.8 11.7,1.5 11,1.3 9.9,1 8.7,1 7.6,1.1 6.9,1.2 6.1,1.4 5.3,1.8 4.5,2.2 4,2.7 3.3,3.4 1.9,4.9 1.1,6.9 0.9,8.8 Z m 20.7,8.9 c 0,0.7 0.4,1.5 1.1,1.8 0.6,0.3 1.4,0.1 2,-0.2 0.5,-0.4 0.7,-1 0.7,-1.5 0,-1 -0.6,-1.7 -1.4,-1.9 -0.5,-0.1 -1.2,0 -1.75,0.4 -0.55,0.4 -0.55,0.9 -0.65,1.4 z M 4.2,27 c 0.3,0.5 0.9,0.9 1.7,1 0.8,0.1 1.4,-0.4 1.7,-1.1 C 8,26.2 7.8,25.3 7.3,24.7 6.8,24 6,24 5.2,24.2 4.6,24.3 4.3,24.8 4.05,25.35 3.8,25.9 3.9,26.5 4.2,27 Z");
      path.setAttribute("fill", color);
      g.appendChild(path);
      parent.appendChild(g);
    }}

    // --- TEK VE ÇİFT KUYRUKLAR (FLAGS / ÇENGEL) ---
    function renderFlagGlyph(parent, stemX, stemY, duration, stemUp, color = "var(--stave-note)") {{
      const flagCounts = {{ '1/8': 1, '1/16': 2, '1/32': 3, '1/64': 4 }};
      const count = flagCounts[duration] || 0;
      if (count === 0) return;
      const g = document.createElementNS("http://www.w3.org/2000/svg", "g");
      for (let i = 0; i < count; i++) {{
        const offset = stemUp ? i * 6 : -i * 6;
        const flag = document.createElementNS("http://www.w3.org/2000/svg", "path");
        if (stemUp) {{
          flag.setAttribute("d", `M ${{stemX}} ${{stemY + offset}} C ${{stemX + 8}} ${{stemY + offset + 6}} ${{stemX + 11}} ${{stemY + offset + 14}} ${{stemX + 3}} ${{stemY + offset + 20}}`);
        }} else {{
          flag.setAttribute("d", `M ${{stemX}} ${{stemY + offset}} C ${{stemX + 8}} ${{stemY + offset - 6}} ${{stemX + 11}} ${{stemY + offset - 14}} ${{stemX + 3}} ${{stemY + offset - 20}}`);
        }}
        flag.setAttribute("fill", "none"); flag.setAttribute("stroke", color); flag.setAttribute("stroke-width", "2.5"); flag.setAttribute("stroke-linecap", "round");
        g.appendChild(flag);
      }}
      parent.appendChild(g);
      return;
      // legacy branch
      const isSixteenth = (duration === '1/16');

      if (stemUp) {{
        // Sap yukarı bakıyorsa: Çentik sağa doğru açılıp aşağı kavis çizer
        const flag1 = document.createElementNS("http://www.w3.org/2000/svg", "path");
        flag1.setAttribute("d", `M ${{stemX}} ${{stemY}} C ${{stemX + 8}} ${{stemY + 6}} ${{stemX + 11}} ${{stemY + 14}} ${{stemX + 3}} ${{stemY + 20}}`);
        flag1.setAttribute("fill", "none"); flag1.setAttribute("stroke", color); flag1.setAttribute("stroke-width", "2.5"); flag1.setAttribute("stroke-linecap", "round");
        g.appendChild(flag1);

        if (isSixteenth) {{
          const flag2 = document.createElementNS("http://www.w3.org/2000/svg", "path");
          flag2.setAttribute("d", `M ${{stemX}} ${{stemY + 6}} C ${{stemX + 8}} ${{stemY + 12}} ${{stemX + 11}} ${{stemY + 20}} ${{stemX + 3}} ${{stemY + 26}}`);
          flag2.setAttribute("fill", "none"); flag2.setAttribute("stroke", color); flag2.setAttribute("stroke-width", "2.5"); flag2.setAttribute("stroke-linecap", "round");
          g.appendChild(flag2);
        }}
      }} else {{
        // Sap aşağı bakıyorsa: Çentik sağa doğru açılıp yukarı kavis çizer
        const flag1 = document.createElementNS("http://www.w3.org/2000/svg", "path");
        flag1.setAttribute("d", `M ${{stemX}} ${{stemY}} C ${{stemX + 8}} ${{stemY - 6}} ${{stemX + 11}} ${{stemY - 14}} ${{stemX + 3}} ${{stemY - 20}}`);
        flag1.setAttribute("fill", "none"); flag1.setAttribute("stroke", color); flag1.setAttribute("stroke-width", "2.5"); flag1.setAttribute("stroke-linecap", "round");
        g.appendChild(flag1);

        if (isSixteenth) {{
          const flag2 = document.createElementNS("http://www.w3.org/2000/svg", "path");
          flag2.setAttribute("d", `M ${{stemX}} ${{stemY - 6}} C ${{stemX + 8}} ${{stemY - 12}} ${{stemX + 11}} ${{stemY - 20}} ${{stemX + 3}} ${{stemY - 26}}`);
          flag2.setAttribute("fill", "none"); flag2.setAttribute("stroke", color); flag2.setAttribute("stroke-width", "2.5"); flag2.setAttribute("stroke-linecap", "round");
          g.appendChild(flag2);
        }}
      }}

      parent.appendChild(g);
    }}

    function renderPerdeBadge(parent, x, y, perdeText, isPrint = false) {{
      if (!perdeText || perdeText === 'none') return;
      const g = document.createElementNS("http://www.w3.org/2000/svg", "g");
      g.setAttribute("transform", `translate(${{x}}, ${{y}})`);
      const color = isPrint ? "#7e22ce" : "#c084fc";
      const bg = isPrint ? "#f3e8ff" : "rgba(168, 85, 247, 0.18)";

      const rect = document.createElementNS("http://www.w3.org/2000/svg", "rect");
      rect.setAttribute("x", "-13"); rect.setAttribute("y", "-10");
      rect.setAttribute("width", "26"); rect.setAttribute("height", "18");
      rect.setAttribute("rx", "4"); rect.setAttribute("fill", bg);
      rect.setAttribute("stroke", color); rect.setAttribute("stroke-width", "1.3");

      const txt = document.createElementNS("http://www.w3.org/2000/svg", "text");
      txt.setAttribute("x", "0"); txt.setAttribute("y", "3.5");
      txt.setAttribute("font-size", "11"); txt.setAttribute("font-weight", "900");
      txt.setAttribute("font-family", "sans-serif");
      txt.setAttribute("text-anchor", "middle"); txt.setAttribute("fill", color);
      txt.textContent = perdeText;

      g.appendChild(rect); g.appendChild(txt);
      parent.appendChild(g);
    }}

    function renderCleanLayerLabels(parent, x) {{
      const g = document.createElementNS("http://www.w3.org/2000/svg", "g");
      g.setAttribute("opacity", "0.85");
      const items = [
        {{ y: 22, h: 22, text: "Tezene (↓/↑)", color: "var(--tezene-down)" }},
        {{ y: 52, h: 22, text: "Süsleme", color: "var(--ornament-color)" }},
        {{ y: 115, h: 30, text: "Porte", color: "var(--text-main)" }},
        {{ y: 180, h: 22, text: "1. Nota (Solfej)", color: "var(--solfege-color)" }},
        {{ y: 206, h: 22, text: "2. Parmak No", color: "#eab308" }},
        {{ y: 234, h: 22, text: "3. Türkü Sözü", color: "var(--lyric-color)" }}
      ];
      items.forEach(it => {{
        const rect = document.createElementNS("http://www.w3.org/2000/svg", "rect");
        rect.setAttribute("x", x); rect.setAttribute("y", it.y); rect.setAttribute("width", "94"); rect.setAttribute("height", it.h);
        rect.setAttribute("rx", "4"); rect.setAttribute("fill", "var(--bg-card)"); rect.setAttribute("stroke", "var(--border-color)");
        const txt = document.createElementNS("http://www.w3.org/2000/svg", "text");
        txt.setAttribute("x", x + 47); txt.setAttribute("y", it.y + it.h / 2 + 3.5); txt.setAttribute("font-size", "9.5"); txt.setAttribute("font-weight", "700");
        txt.setAttribute("text-anchor", "middle"); txt.setAttribute("fill", it.color);
        txt.textContent = it.text;
        g.appendChild(rect); g.appendChild(txt);
      }});
      parent.appendChild(g);
    }}

    function renderKeySignature(parent, x, keySig, isPrint = false) {{
      const yOffset = isPrint ? -55 : 0;
      if (keySig === 'b2_si') {{
        renderAccidentalGlyph(parent, x, 130 + yOffset, 'b2', isPrint);
      }} else if (keySig === 'b1_si') {{
        renderAccidentalGlyph(parent, x, 130 + yOffset, 'b1', isPrint);
      }} else if (keySig === 'b4_si') {{
        renderAccidentalGlyph(parent, x, 130 + yOffset, 'b4', isPrint);
      }} else if (keySig === 'flat_si') {{
        renderAccidentalGlyph(parent, x, 130 + yOffset, 'flat', isPrint);
      }} else if (keySig === 'sharp_fa') {{
        renderAccidentalGlyph(parent, x, 110 + yOffset, 'sharp', isPrint);
      }} else if (keySig === 'sharp_do') {{
        renderAccidentalGlyph(parent, x, 125 + yOffset, 'sharp', isPrint);
      }} else if (keySig === 'b2_mi') {{
        renderAccidentalGlyph(parent, x, 115 + yOffset, 'b2', isPrint);
      }} else if (keySig === 'flat_mi') {{
        renderAccidentalGlyph(parent, x, 115 + yOffset, 'flat', isPrint);
      }} else if (keySig === 'b2_si_fa_sharp') {{
        renderAccidentalGlyph(parent, x, 130 + yOffset, 'b2', isPrint);
        renderAccidentalGlyph(parent, x + 16, 110 + yOffset, 'sharp', isPrint);
      }} else if (keySig === 'b2_si_mi') {{
        renderAccidentalGlyph(parent, x, 130 + yOffset, 'b2', isPrint);
        renderAccidentalGlyph(parent, x + 16, 115 + yOffset, 'b2', isPrint);
      }} else if (keySig === 'b2_si_fa_sharp_do_sharp') {{
        renderAccidentalGlyph(parent, x, 130 + yOffset, 'b2', isPrint);
        renderAccidentalGlyph(parent, x + 15, 110 + yOffset, 'sharp', isPrint);
        renderAccidentalGlyph(parent, x + 30, 125 + yOffset, 'sharp', isPrint);
      }} else if (keySig === 'flat_si_mi') {{
        renderAccidentalGlyph(parent, x, 130 + yOffset, 'flat', isPrint);
        renderAccidentalGlyph(parent, x + 16, 115 + yOffset, 'flat', isPrint);
      }} else if (keySig === 'flat_si_mi_la') {{
        renderAccidentalGlyph(parent, x, 130 + yOffset, 'flat', isPrint);
        renderAccidentalGlyph(parent, x + 15, 115 + yOffset, 'flat', isPrint);
        renderAccidentalGlyph(parent, x + 30, 135 + yOffset, 'flat', isPrint);
      }} else if (keySig === 'sharp_fa_do') {{
        renderAccidentalGlyph(parent, x, 110 + yOffset, 'sharp', isPrint);
        renderAccidentalGlyph(parent, x + 16, 125 + yOffset, 'sharp', isPrint);
      }} else if (keySig === 'sharp_fa_do_sol') {{
        renderAccidentalGlyph(parent, x, 110 + yOffset, 'sharp', isPrint);
        renderAccidentalGlyph(parent, x + 15, 125 + yOffset, 'sharp', isPrint);
        renderAccidentalGlyph(parent, x + 30, 105 + yOffset, 'sharp', isPrint);
      }}
    }}

    function renderTimeSignature(parent, x, y, meter, color = "var(--text-main)") {{
      const parts = meter.split('/');
      const g = document.createElementNS("http://www.w3.org/2000/svg", "g");
      g.setAttribute("transform", `translate(${{x}}, ${{y}})`);
      const t1 = document.createElementNS("http://www.w3.org/2000/svg", "text");
      t1.setAttribute("x", "0"); t1.setAttribute("y", "16"); t1.setAttribute("font-size", "18"); t1.setAttribute("font-weight", "900"); t1.setAttribute("font-family", "serif"); t1.setAttribute("text-anchor", "middle"); t1.setAttribute("fill", color);
      t1.textContent = parts[0];
      const t2 = document.createElementNS("http://www.w3.org/2000/svg", "text");
      t2.setAttribute("x", "0"); t2.setAttribute("y", "36"); t2.setAttribute("font-size", "18"); t2.setAttribute("font-weight", "900"); t2.setAttribute("font-family", "serif"); t2.setAttribute("text-anchor", "middle"); t2.setAttribute("fill", color);
      t2.textContent = parts[1];
      g.appendChild(t1); g.appendChild(t2);
      parent.appendChild(g);
    }}

    function renderDolapBracket(parent, startX, endX, dolapNum, y = 24, color = "var(--dolap-color)") {{
      const g = document.createElementNS("http://www.w3.org/2000/svg", "g");
      const p = document.createElementNS("http://www.w3.org/2000/svg", "path");
      p.setAttribute("d", `M ${{startX + 4}} ${{y + 12}} L ${{startX + 4}} ${{y}} L ${{endX - 4}} ${{y}} L ${{endX - 4}} ${{y + 12}}`);
      p.setAttribute("fill", "none"); p.setAttribute("stroke", color); p.setAttribute("stroke-width", "2");
      const txt = document.createElementNS("http://www.w3.org/2000/svg", "text");
      txt.setAttribute("x", startX + 12); txt.setAttribute("y", y + 10); txt.setAttribute("font-size", "11"); txt.setAttribute("font-weight", "900"); txt.setAttribute("fill", color);
      txt.textContent = `${{dolapNum}}.`;
      g.appendChild(p); g.appendChild(txt);
      parent.appendChild(g);
    }}

    function renderRepeatBar(parent, x, y1, y2, isStart, lineColor = "var(--stave-line)", dotColor = "var(--ropriz-color)") {{
      const g = document.createElementNS("http://www.w3.org/2000/svg", "g");
      if (isStart) {{
        const l1 = document.createElementNS("http://www.w3.org/2000/svg", "line");
        l1.setAttribute("x1", x); l1.setAttribute("y1", y1); l1.setAttribute("x2", x); l1.setAttribute("y2", y2); l1.setAttribute("stroke", lineColor); l1.setAttribute("stroke-width", "3.5");
        const l2 = document.createElementNS("http://www.w3.org/2000/svg", "line");
        l2.setAttribute("x1", x + 4); l2.setAttribute("y1", y1); l2.setAttribute("x2", x + 4); l2.setAttribute("y2", y2); l2.setAttribute("stroke", lineColor); l2.setAttribute("stroke-width", "1.5");
        const c1 = document.createElementNS("http://www.w3.org/2000/svg", "circle");
        c1.setAttribute("cx", x + 9); c1.setAttribute("cy", y1 + 15); c1.setAttribute("r", "2.2"); c1.setAttribute("fill", dotColor);
        const c2 = document.createElementNS("http://www.w3.org/2000/svg", "circle");
        c2.setAttribute("cx", x + 9); c2.setAttribute("cy", y1 + 25); c2.setAttribute("r", "2.2"); c2.setAttribute("fill", dotColor);
        g.appendChild(l1); g.appendChild(l2); g.appendChild(c1); g.appendChild(c2);
      }} else {{
        const c1 = document.createElementNS("http://www.w3.org/2000/svg", "circle");
        c1.setAttribute("cx", x - 9); c1.setAttribute("cy", y1 + 15); c1.setAttribute("r", "2.2"); c1.setAttribute("fill", dotColor);
        const c2 = document.createElementNS("http://www.w3.org/2000/svg", "circle");
        c2.setAttribute("cx", x - 9); c2.setAttribute("cy", y1 + 25); c2.setAttribute("r", "2.2"); c2.setAttribute("fill", dotColor);
        const l1 = document.createElementNS("http://www.w3.org/2000/svg", "line");
        l1.setAttribute("x1", x - 4); l1.setAttribute("y1", y1); l1.setAttribute("x2", x - 4); l1.setAttribute("y2", y2); l1.setAttribute("stroke", lineColor); l1.setAttribute("stroke-width", "1.5");
        const l2 = document.createElementNS("http://www.w3.org/2000/svg", "line");
        l2.setAttribute("x1", x); l2.setAttribute("y1", y1); l2.setAttribute("x2", x); l2.setAttribute("y2", y2); l2.setAttribute("stroke", lineColor); l2.setAttribute("stroke-width", "3.5");
        g.appendChild(c1); g.appendChild(c2); g.appendChild(l1); g.appendChild(l2);
      }}
      parent.appendChild(g);
    }}

    function renderAccidentalGlyph(parent, x, y, accidental, isPrint = false) {{
      const isComaB = typeof accidental === 'string' && accidental.startsWith('b');
      const isComaSharp = typeof accidental === 'string' && accidental.startsWith('sharp');
      const color = isComaB ? (isPrint ? "#ea580c" : "var(--b2-color)") : (isComaSharp ? (isPrint ? "#059669" : "#10b981") : (isPrint ? "#1f2937" : "var(--text-main)"));
      const g = document.createElementNS("http://www.w3.org/2000/svg", "g");

      if (isComaB || accidental === 'flat') {{
        // Otantik Sarısözen Köşeli / Sert Bemol Standardı:
        const stem = document.createElementNS("http://www.w3.org/2000/svg", "line");
        stem.setAttribute("x1", x); stem.setAttribute("y1", y - 16);
        stem.setAttribute("x2", x); stem.setAttribute("y2", y + 4.5);
        stem.setAttribute("stroke", color); stem.setAttribute("stroke-width", "1.8");
        stem.setAttribute("stroke-linecap", "round");
        g.appendChild(stem);

        // Tipik Köşeli Açılı Gövde (Sarısözen Ekolü Açılı İç-Boşluklu Sert Karın):
        const bowl = document.createElementNS("http://www.w3.org/2000/svg", "path");
        bowl.setAttribute("d", `M ${{x}},${{y - 5.5}} L ${{x + 9}},${{y - 1}} L ${{x}},${{y + 4.5}} Z M ${{x}},${{y - 2.8}} L ${{x + 5.5}},${{y - 1}} L ${{x}},${{y + 2}} Z`);
        bowl.setAttribute("fill", color);
        g.appendChild(bowl);

        let cNum = '';
        if (isComaB) cNum = accidental.replace('b', '');
        if (cNum) {{
          const txt = document.createElementNS("http://www.w3.org/2000/svg", "text");
          txt.setAttribute("x", x + 3.2); txt.setAttribute("y", y - 7.5);
          txt.setAttribute("font-size", "9.5"); txt.setAttribute("font-weight", "900");
          txt.setAttribute("font-family", "system-ui, -apple-system, sans-serif");
          txt.setAttribute("fill", color);
          txt.textContent = cNum;
          g.appendChild(txt);
        }}
      }} else if (isComaSharp || accidental === 'sharp') {{
        const l1 = document.createElementNS("http://www.w3.org/2000/svg", "line");
        l1.setAttribute("x1", x + 1); l1.setAttribute("y1", y - 11); l1.setAttribute("x2", x + 1); l1.setAttribute("y2", y + 8);
        l1.setAttribute("stroke", color); l1.setAttribute("stroke-width", "1.6");
        const l2 = document.createElementNS("http://www.w3.org/2000/svg", "line");
        l2.setAttribute("x1", x + 6); l2.setAttribute("y1", y - 13); l2.setAttribute("x2", x + 6); l2.setAttribute("y2", y + 6);
        l2.setAttribute("stroke", color); l2.setAttribute("stroke-width", "1.6");
        const l3 = document.createElementNS("http://www.w3.org/2000/svg", "line");
        l3.setAttribute("x1", x - 2); l3.setAttribute("y1", y - 3); l3.setAttribute("x2", x + 9); l3.setAttribute("y2", y - 6);
        l3.setAttribute("stroke", color); l3.setAttribute("stroke-width", "2.2");
        const l4 = document.createElementNS("http://www.w3.org/2000/svg", "line");
        l4.setAttribute("x1", x - 2); l4.setAttribute("y1", y + 3); l4.setAttribute("x2", x + 9); l4.setAttribute("y2", y);
        l4.setAttribute("stroke", color); l4.setAttribute("stroke-width", "2.2");
        g.appendChild(l1); g.appendChild(l2); g.appendChild(l3); g.appendChild(l4);

        let sharpNum = '';
        if (isComaSharp) sharpNum = accidental.replace('sharp', '');
        if (sharpNum) {{
          const txt = document.createElementNS("http://www.w3.org/2000/svg", "text");
          txt.setAttribute("x", x + 9.5); txt.setAttribute("y", y - 8);
          txt.setAttribute("font-size", "9"); txt.setAttribute("font-weight", "900");
          txt.setAttribute("font-family", "system-ui, -apple-system, sans-serif");
          txt.setAttribute("fill", color);
          txt.textContent = sharpNum;
          g.appendChild(txt);
        }}
      }} else if (accidental === 'natural') {{
        const l1 = document.createElementNS("http://www.w3.org/2000/svg", "line");
        l1.setAttribute("x1", x + 1); l1.setAttribute("y1", y - 12); l1.setAttribute("x2", x + 1); l1.setAttribute("y2", y + 4);
        l1.setAttribute("stroke", color); l1.setAttribute("stroke-width", "1.6");
        const l2 = document.createElementNS("http://www.w3.org/2000/svg", "line");
        l2.setAttribute("x1", x + 6); l2.setAttribute("y1", y - 4); l2.setAttribute("x2", x + 6); l2.setAttribute("y2", y + 12);
        l2.setAttribute("stroke", color); l2.setAttribute("stroke-width", "1.6");
        const l3 = document.createElementNS("http://www.w3.org/2000/svg", "line");
        l3.setAttribute("x1", x + 1); l3.setAttribute("y1", y - 3); l3.setAttribute("x2", x + 6); l3.setAttribute("y2", y - 5);
        l3.setAttribute("stroke", color); l3.setAttribute("stroke-width", "2");
        const l4 = document.createElementNS("http://www.w3.org/2000/svg", "line");
        l4.setAttribute("x1", x + 1); l4.setAttribute("y1", y + 3); l4.setAttribute("x2", x + 6); l4.setAttribute("y2", y + 1);
        l4.setAttribute("stroke", color); l4.setAttribute("stroke-width", "2");
        g.appendChild(l1); g.appendChild(l2); g.appendChild(l3); g.appendChild(l4);
      }}
      parent.appendChild(g);
    }}

    function renderArrow(parent, x, y, dir, color) {{
      const g = document.createElementNS("http://www.w3.org/2000/svg", "g");
      // Ok sapı kısaltılmış (10px), süslemelerle çakışmayı önler
      if (dir === 'down') {{
        const line = document.createElementNS("http://www.w3.org/2000/svg", "line");
        line.setAttribute("x1", x); line.setAttribute("y1", y); line.setAttribute("x2", x); line.setAttribute("y2", y + 10);
        line.setAttribute("stroke", color); line.setAttribute("stroke-width", "2.2"); line.setAttribute("stroke-linecap", "round");
        const poly = document.createElementNS("http://www.w3.org/2000/svg", "polygon");
        poly.setAttribute("points", `${{x - 3.8}},${{y + 7}} ${{x + 3.8}},${{y + 7}} ${{x}},${{y + 12}}`); poly.setAttribute("fill", color);
        g.appendChild(line); g.appendChild(poly);
      }} else if (dir === 'up') {{
        const line = document.createElementNS("http://www.w3.org/2000/svg", "line");
        line.setAttribute("x1", x); line.setAttribute("y1", y + 10); line.setAttribute("x2", x); line.setAttribute("y2", y);
        line.setAttribute("stroke", color); line.setAttribute("stroke-width", "2.2"); line.setAttribute("stroke-linecap", "round");
        const poly = document.createElementNS("http://www.w3.org/2000/svg", "polygon");
        poly.setAttribute("points", `${{x - 3.8}},${{y + 3}} ${{x + 3.8}},${{y + 3}} ${{x}},${{y - 2}}`); poly.setAttribute("fill", color);
        g.appendChild(line); g.appendChild(poly);
      }}
      parent.appendChild(g);
    }}

    function renderStemSlashes(parent, stemX, y, color) {{
      const g = document.createElementNS("http://www.w3.org/2000/svg", "g");
      const l1 = document.createElementNS("http://www.w3.org/2000/svg", "line");
      l1.setAttribute("x1", stemX - 5); l1.setAttribute("y1", y + 3); l1.setAttribute("x2", stemX + 5); l1.setAttribute("y2", y - 3);
      l1.setAttribute("stroke", color); l1.setAttribute("stroke-width", "2"); l1.setAttribute("stroke-linecap", "round");
      const l2 = document.createElementNS("http://www.w3.org/2000/svg", "line");
      l2.setAttribute("x1", stemX - 5); l2.setAttribute("y1", y + 8); l2.setAttribute("x2", stemX + 5); l2.setAttribute("y2", y + 2);
      l2.setAttribute("stroke", color); l2.setAttribute("stroke-width", "2"); l2.setAttribute("stroke-linecap", "round");
      g.appendChild(l1); g.appendChild(l2);
      parent.appendChild(g);
    }}

    function renderOrnamentDisplay(parent, x, y, ornament, color) {{
      if (ornament === 'slash') return;
      const g = document.createElementNS("http://www.w3.org/2000/svg", "g");
      const baseLineY = y; // Ortak taban çizgisi
      if (ornament === 'takma') {{
        // ▲ Dolu üçgen: taban baseLineY, tepe baseLineY - 8
        const poly = document.createElementNS("http://www.w3.org/2000/svg", "polygon");
        poly.setAttribute("points", `${{x - 4.5}},${{baseLineY}} ${{x + 4.5}},${{baseLineY}} ${{x}},${{baseLineY - 8}}`);
        poly.setAttribute("fill", color);
        g.appendChild(poly);
      }} else if (ornament === 'carpma') {{
        // ▼ / v Çarpma: ▲ ile birebir aynı üçgen geometri ve ebatta, tabanı üstte (baseLineY - 8), sivri ucu taban çizgisinde (baseLineY)
        const poly = document.createElementNS("http://www.w3.org/2000/svg", "polygon");
        poly.setAttribute("points", `${{x - 4.5}},${{baseLineY - 8}} ${{x + 4.5}},${{baseLineY - 8}} ${{x}},${{baseLineY}}`);
        poly.setAttribute("fill", color);
        g.appendChild(poly);
      }} else if (ornament === 'cekme') {{
        // ∧ / ^ Çekme: ▲ ile birebir aynı üçgen geometri ve ebatta (içi oyuk temiz üçgen şapka)
        const poly = document.createElementNS("http://www.w3.org/2000/svg", "polygon");
        poly.setAttribute("points", `${{x - 4.5}},${{baseLineY}} ${{x + 4.5}},${{baseLineY}} ${{x}},${{baseLineY - 8}}`);
        poly.setAttribute("fill", "none");
        poly.setAttribute("stroke", color);
        poly.setAttribute("stroke-width", "1.6");
        poly.setAttribute("stroke-linejoin", "round");
        g.appendChild(poly);
      }}
      parent.appendChild(g);
    }}

    function renderRestGlyph(parent, x, y, duration, color = "var(--text-main)", isDotted = false) {{
      const g = document.createElementNS("http://www.w3.org/2000/svg", "g");
      let dotX = x + 12;
      let dotY = y;

      if (duration === '1/1') {{
        const rect = document.createElementNS("http://www.w3.org/2000/svg", "rect");
        rect.setAttribute("x", x - 7); rect.setAttribute("y", y); rect.setAttribute("width", "14"); rect.setAttribute("height", "6.5"); rect.setAttribute("fill", color);
        g.appendChild(rect);
        dotY = y + 3;
      }} else if (duration === '1/2') {{
        const rect = document.createElementNS("http://www.w3.org/2000/svg", "rect");
        rect.setAttribute("x", x - 7); rect.setAttribute("y", y - 6.5); rect.setAttribute("width", "14"); rect.setAttribute("height", "6.5"); rect.setAttribute("fill", color);
        g.appendChild(rect);
        dotY = y - 3;
      }} else if (duration === '1/4') {{
        const txt = document.createElementNS("http://www.w3.org/2000/svg", "text");
        txt.setAttribute("x", x); txt.setAttribute("y", y + 10); txt.setAttribute("font-size", "28"); txt.setAttribute("font-family", "serif"); txt.setAttribute("font-weight", "bold"); txt.setAttribute("text-anchor", "middle"); txt.setAttribute("fill", color);
        txt.textContent = "𝄽";
        g.appendChild(txt);
        dotY = y;
      }} else if (duration === '1/8') {{
        const txt = document.createElementNS("http://www.w3.org/2000/svg", "text");
        txt.setAttribute("x", x); txt.setAttribute("y", y + 8); txt.setAttribute("font-size", "26"); txt.setAttribute("font-family", "serif"); txt.setAttribute("font-weight", "bold"); txt.setAttribute("text-anchor", "middle"); txt.setAttribute("fill", color);
        txt.textContent = "𝄾";
        g.appendChild(txt);
        dotY = y - 2;
      }} else if (duration === '1/16') {{
        const txt = document.createElementNS("http://www.w3.org/2000/svg", "text");
        txt.setAttribute("x", x); txt.setAttribute("y", y + 9); txt.setAttribute("font-size", "26"); txt.setAttribute("font-family", "serif"); txt.setAttribute("font-weight", "bold"); txt.setAttribute("text-anchor", "middle"); txt.setAttribute("fill", color);
        txt.textContent = "𝄿";
        g.appendChild(txt);
        dotY = y - 2;
      }} else if (duration === '1/32') {{
        const txt = document.createElementNS("http://www.w3.org/2000/svg", "text");
        txt.setAttribute("x", x); txt.setAttribute("y", y + 10); txt.setAttribute("font-size", "26"); txt.setAttribute("font-family", "serif"); txt.setAttribute("font-weight", "bold"); txt.setAttribute("text-anchor", "middle"); txt.setAttribute("fill", color);
        txt.textContent = "𝅀";
        g.appendChild(txt);
        dotY = y - 2;
      }} else {{
        // 1/64
        const txt = document.createElementNS("http://www.w3.org/2000/svg", "text");
        txt.setAttribute("x", x); txt.setAttribute("y", y + 10); txt.setAttribute("font-size", "26"); txt.setAttribute("font-family", "serif"); txt.setAttribute("font-weight", "bold"); txt.setAttribute("text-anchor", "middle"); txt.setAttribute("fill", color);
        txt.textContent = "𝅁";
        g.appendChild(txt);
        dotY = y - 2;
      }}

      if (isDotted) {{
        const dot = document.createElementNS("http://www.w3.org/2000/svg", "circle");
        dot.setAttribute("cx", dotX); dot.setAttribute("cy", dotY);
        dot.setAttribute("r", "2.2"); dot.setAttribute("fill", color);
        g.appendChild(dot);
      }}

      parent.appendChild(g);
    }}

    function renderLedgerLines(parent, x, step, topY, bottomY, lineSpacing, color = "var(--stave-line)") {{
      if (step >= 12) {{
        for (let s = 12; s <= step; s += 2) {{
          const ly = topY - ((s - 10) / 2) * lineSpacing;
          const l = document.createElementNS("http://www.w3.org/2000/svg", "line");
          l.setAttribute("x1", x - 11); l.setAttribute("y1", ly); l.setAttribute("x2", x + 11); l.setAttribute("y2", ly);
          l.setAttribute("stroke", color); l.setAttribute("stroke-width", "1.4");
          parent.appendChild(l);
        }}
      }}
      if (step <= 0) {{
        for (let s = 0; s >= step; s -= 2) {{
          const ly = bottomY + ((2 - s) / 2) * lineSpacing;
          const l = document.createElementNS("http://www.w3.org/2000/svg", "line");
          l.setAttribute("x1", x - 11); l.setAttribute("y1", ly); l.setAttribute("x2", x + 11); l.setAttribute("y2", ly);
          l.setAttribute("stroke", color); l.setAttribute("stroke-width", "1.4");
          parent.appendChild(l);
        }}
      }}
    }}

    function renderMeasureGroup(parent, layout, staveLinesY) {{
      const {{ measure, mIdx, startX: mStartX, endX: mEndX, width: mWidth, isActive }} = layout;
      const mG = document.createElementNS("http://www.w3.org/2000/svg", "g");

      if (isActive) {{
        const actRect = document.createElementNS("http://www.w3.org/2000/svg", "rect");
        actRect.setAttribute("x", mStartX); actRect.setAttribute("y", "20"); actRect.setAttribute("width", mWidth); actRect.setAttribute("height", "240");
        actRect.setAttribute("rx", "8"); actRect.setAttribute("fill", "rgba(56, 189, 248, 0.05)");
        actRect.setAttribute("stroke", "var(--border-accent)"); actRect.setAttribute("stroke-dasharray", "4 2"); actRect.setAttribute("stroke-width", "1.5");
        mG.appendChild(actRect);
      }}

      const hG = document.createElementNS("http://www.w3.org/2000/svg", "g");
      hG.style.cursor = "pointer";
      hG.onclick = (e) => {{
        e.stopPropagation();
        appState.activeMeasureIndex = mIdx;
        appState.selectedNoteId = null;
        appState.rangeSelection = [];
        syncToolbar();
        render();
      }};
      const hRect = document.createElementNS("http://www.w3.org/2000/svg", "rect");
      hRect.setAttribute("x", mStartX + 8); hRect.setAttribute("y", "4"); hRect.setAttribute("width", "75"); hRect.setAttribute("height", "16");
      hRect.setAttribute("rx", "3"); hRect.setAttribute("fill", "var(--bg-card)"); hRect.setAttribute("stroke", isActive ? "var(--tezene-down)" : "var(--border-color)");
      const hText = document.createElementNS("http://www.w3.org/2000/svg", "text");
      hText.setAttribute("x", mStartX + 45); hText.setAttribute("y", "15"); hText.setAttribute("font-size", "9.5"); hText.setAttribute("font-weight", "bold");
      hText.setAttribute("fill", isActive ? "var(--tezene-down)" : "var(--text-dim)"); hText.setAttribute("text-anchor", "middle");
      hText.textContent = `ÖLÇÜ ${{mIdx + 1}}`;
      hG.appendChild(hRect); hG.appendChild(hText);
      mG.appendChild(hG);

      if (measure.dolap && measure.dolap !== 'none') {{
        renderDolapBracket(mG, mStartX, mEndX, measure.dolap, 24);
      }}

      // GERÇEK SENYO VE PERDE SAYISI
      // Aynı ölçüye gelirse: Önce Senyo sonra P!
      let startSignX = mStartX + 26;
      if (measure.senyoStart) {{
        renderAuthenticSegno(mG, startSignX, 48);
        startSignX += 28;
      }}
      if (measure.perde && measure.perde !== 'none') {{
        renderPerdeBadge(mG, startSignX, 48, measure.perde, false);
      }}
      if (measure.senyoEnd) renderAuthenticSegno(mG, mEndX - 26, 48);

      if (measure.repeatStart) {{
        renderRepeatBar(mG, mStartX, 110, 150, true);
      }} else if (mIdx > 0) {{
        const bl = document.createElementNS("http://www.w3.org/2000/svg", "line");
        bl.setAttribute("x1", mStartX); bl.setAttribute("y1", "110"); bl.setAttribute("x2", mStartX); bl.setAttribute("y2", "150");
        bl.setAttribute("stroke", "var(--stave-line)"); bl.setAttribute("stroke-width", "1.6");
        mG.appendChild(bl);
      }}

      let noteOffset = measure.repeatStart ? 44 : 36;
      if (measure.senyoStart && measure.perde && measure.perde !== 'none') {{
        noteOffset = Math.max(noteOffset, 68);
      }}
      const notePositions = [];

      // Hangi notaların bağlı bir kiriş grubuna ait olduğunu ve grubun sap yönünü tek bir merkezden hesapla
      const beamedIds = new Set();
      const beamGroupStemDir = new Map(); // noteId -> boolean (stemUp)
      let tempGroup = [];

      for (let i = 0; i < measure.notes.length; i++) {{
        const n = measure.notes[i];
        if (!n.isRest && (n.beam === 'single' || n.beam === 'double')) {{
          tempGroup.push(n);
        }} else {{
          if (tempGroup.length >= 2) {{
            const avgStep = tempGroup.reduce((sum, item) => sum + item.step, 0) / tempGroup.length;
            const groupStemUp = (avgStep < 6); // Ortalama perde Si(6)'nın altındaysa YUKARI, üstündeyse AŞAĞI
            tempGroup.forEach(item => {{
              beamedIds.add(item.id);
              beamGroupStemDir.set(item.id, groupStemUp);
            }});
          }}
          tempGroup = [];
        }}
      }}
      if (tempGroup.length >= 2) {{
        const avgStep = tempGroup.reduce((sum, item) => sum + item.step, 0) / tempGroup.length;
        const groupStemUp = (avgStep < 6);
        tempGroup.forEach(item => {{
          beamedIds.add(item.id);
          beamGroupStemDir.set(item.id, groupStemUp);
        }});
      }});
            const groupStemUp = upCount >= downCount;
            tempGroup.forEach(item => {{
              beamedIds.add(item.id);
              beamGroupStemDir.set(item.id, groupStemUp);
            }});
          }}
          tempGroup = [];
        }}
      }}
      if (tempGroup.length >= 2) {{
        let upCount = 0;
        let downCount = 0;
        tempGroup.forEach(item => {{
          if (item.step <= 6) upCount++;
          else downCount++;
        }});
        const groupStemUp = upCount >= downCount;
        tempGroup.forEach(item => {{
          beamedIds.add(item.id);
          beamGroupStemDir.set(item.id, groupStemUp);
        }});
      }}

      measure.notes.forEach((note, nIdx) => {{
        const colX = mStartX + noteOffset + nIdx * 62;
        notePositions.push({{ note, colX }});
        const isActuallyBeamed = beamedIds.has(note.id);
        const forcedStemUp = beamGroupStemDir.has(note.id) ? beamGroupStemDir.get(note.id) : null;
        renderInteractiveNoteColumn(mG, note, colX, mIdx, isActuallyBeamed, forcedStemUp);
      }});

      renderBeamsForMeasure(mG, notePositions);
      renderTripletBrackets(mG, notePositions, false);

      const isLast = mIdx === appState.measures.length - 1;
      if (measure.repeatEnd) {{
        renderRepeatBar(mG, mEndX, 110, 150, false);
      }} else if (measure.barType === 'final' || isLast) {{
        const l1 = document.createElementNS("http://www.w3.org/2000/svg", "line");
        l1.setAttribute("x1", mEndX - 4); l1.setAttribute("y1", "110"); l1.setAttribute("x2", mEndX - 4); l1.setAttribute("y2", "150");
        l1.setAttribute("stroke", "var(--stave-line)"); l1.setAttribute("stroke-width", "1.6");
        const l2 = document.createElementNS("http://www.w3.org/2000/svg", "line");
        l2.setAttribute("x1", mEndX); l2.setAttribute("y1", "110"); l2.setAttribute("x2", mEndX); l2.setAttribute("y2", "150");
        l2.setAttribute("stroke", "var(--stave-line)"); l2.setAttribute("stroke-width", "3.5");
        mG.appendChild(l1); mG.appendChild(l2);
      }} else if (measure.barType === 'double') {{
        const l1 = document.createElementNS("http://www.w3.org/2000/svg", "line");
        l1.setAttribute("x1", mEndX - 3.5); l1.setAttribute("y1", "110"); l1.setAttribute("x2", mEndX - 3.5); l1.setAttribute("y2", "150");
        l1.setAttribute("stroke", "var(--stave-line)"); l1.setAttribute("stroke-width", "1.5");
        const l2 = document.createElementNS("http://www.w3.org/2000/svg", "line");
        l2.setAttribute("x1", mEndX); l2.setAttribute("y1", "110"); l2.setAttribute("x2", mEndX); l2.setAttribute("y2", "150");
        l2.setAttribute("stroke", "var(--stave-line)"); l2.setAttribute("stroke-width", "1.5");
        mG.appendChild(l1); mG.appendChild(l2);
      }} else {{
        const bl = document.createElementNS("http://www.w3.org/2000/svg", "line");
        bl.setAttribute("x1", mEndX); bl.setAttribute("y1", "110"); bl.setAttribute("x2", mEndX); bl.setAttribute("y2", "150");
        bl.setAttribute("stroke", "var(--stave-line)"); bl.setAttribute("stroke-width", "1.6");
        mG.appendChild(bl);
      }}

      parent.appendChild(mG);
    }}

    function renderTripletBrackets(parent, notePositions, isPrint = false) {{
      let currentTriplet = [];
      notePositions.forEach(item => {{
        if (item.note.isTriplet) currentTriplet.push(item);
        else {{
          if (currentTriplet.length > 0) {{
            drawTripletBracket(parent, currentTriplet, isPrint);
            currentTriplet = [];
          }}
        }}
      }});
      if (currentTriplet.length > 0) drawTripletBracket(parent, currentTriplet, isPrint);
    }}

    function drawTripletBracket(parent, group, isPrint = false) {{
      if (group.length === 0) return;
      const x1 = group[0].colX;
      const x2 = group[group.length - 1].colX;
      const midX = (x1 + x2) / 2;
      const bracketY = isPrint ? 20 : 66;
      const color = isPrint ? "#1f2937" : "var(--border-accent)";

      const g = document.createElementNS("http://www.w3.org/2000/svg", "g");

      if (x1 !== x2) {{
        // Kemer çizgisi sol parça
        const l1 = document.createElementNS("http://www.w3.org/2000/svg", "line");
        l1.setAttribute("x1", x1 - 4); l1.setAttribute("y1", bracketY);
        l1.setAttribute("x2", midX - 6); l1.setAttribute("y2", bracketY);
        l1.setAttribute("stroke", color); l1.setAttribute("stroke-width", "1.4");
        g.appendChild(l1);

        // Kemer çizgisi sağ parça
        const l2 = document.createElementNS("http://www.w3.org/2000/svg", "line");
        l2.setAttribute("x1", midX + 6); l2.setAttribute("y1", bracketY);
        l2.setAttribute("x2", x2 + 4); l2.setAttribute("y2", bracketY);
        l2.setAttribute("stroke", color); l2.setAttribute("stroke-width", "1.4");
        g.appendChild(l2);

        // Sol uç çentiği
        const h1 = document.createElementNS("http://www.w3.org/2000/svg", "line");
        h1.setAttribute("x1", x1 - 4); h1.setAttribute("y1", bracketY);
        h1.setAttribute("x2", x1 - 4); h1.setAttribute("y2", bracketY + 4);
        h1.setAttribute("stroke", color); h1.setAttribute("stroke-width", "1.4");
        g.appendChild(h1);

        // Sağ uç çentiği
        const h2 = document.createElementNS("http://www.w3.org/2000/svg", "line");
        h2.setAttribute("x1", x2 + 4); h2.setAttribute("y1", bracketY);
        h2.setAttribute("x2", x2 + 4); h2.setAttribute("y2", bracketY + 4);
        h2.setAttribute("stroke", color); h2.setAttribute("stroke-width", "1.4");
        g.appendChild(h2);
      }}

      // Ortaya kemerli "3" rakamı
      const txt = document.createElementNS("http://www.w3.org/2000/svg", "text");
      txt.setAttribute("x", midX); txt.setAttribute("y", bracketY + 3.5);
      txt.setAttribute("font-size", isPrint ? "11" : "12"); txt.setAttribute("font-weight", "900");
      txt.setAttribute("font-family", "serif"); txt.setAttribute("text-anchor", "middle");
      txt.setAttribute("fill", color);
      txt.textContent = "3";
      g.appendChild(txt);

      parent.appendChild(g);
    }}

    function renderBeamsForMeasure(parent, notePositions) {{
      let currentGroup = [];

      for (let i = 0; i < notePositions.length; i++) {{
        const item = notePositions[i];
        if (!item.note.isRest && (item.note.beam === 'single' || item.note.beam === 'double')) {{
          currentGroup.push(item);
        }} else {{
          if (currentGroup.length >= 2) drawBeamGroup(parent, currentGroup);
          currentGroup = [];
        }}
      }}
      if (currentGroup.length >= 2) drawBeamGroup(parent, currentGroup);
    }}

    function drawBeamGroup(parent, group) {{
      if (!group || group.length < 2) return;
      // Grubun sap yönü: renderMeasureGroup ile birebir aynı kural!
      const avgStep = group.reduce((sum, it) => sum + it.note.step, 0) / group.length;
      const stemUp = (avgStep < 6);

      // Her notanın sap ucu koordinatını hesapla
      const pts = group.map(it => {{
        const allP = getNotePitches(it.note);
        const steps = allP.map(p => p.step);
        const minStep = Math.min(...steps);
        const maxStep = Math.max(...steps);
        const stemX = stemUp ? it.colX + 5.5 : it.colX - 5.5;
        const bottomPitchY = getStepY(minStep);
        const topPitchY = getStepY(maxStep);
        const stemEndY = stemUp ? topPitchY - 30 : bottomPitchY + 30;
        return {{ x: stemX, y: stemEndY, note: it.note }};
      }});

      // Başlangıç ve bitiş noktaları
      const startPt = pts[0];
      const endPt = pts[pts.length - 1];

      function getBeamY(x) {{
        if (Math.abs(endPt.x - startPt.x) < 0.001) return startPt.y;
        const t = (x - startPt.x) / (endPt.x - startPt.x);
        return startPt.y + t * (endPt.y - startPt.y);
      }}

      // Sap boylarını kiriş çizgisiyle pürüzsüz kesiştirmek için sap uzatma çizgisi
      pts.forEach(p => {{
        const targetBeamY = getBeamY(p.x);
        if (Math.abs(targetBeamY - p.y) > 0.5) {{
          const extLine = document.createElementNS("http://www.w3.org/2000/svg", "line");
          extLine.setAttribute("x1", p.x); extLine.setAttribute("y1", p.y);
          extLine.setAttribute("x2", p.x); extLine.setAttribute("y2", targetBeamY);
          extLine.setAttribute("stroke", "var(--stave-note)"); extLine.setAttribute("stroke-width", "1.8");
          parent.appendChild(extLine);
        }}
      }});

      const beamOffset = stemUp ? 5.5 : -5.5;

      // Kirişleri ardışık çiftler (1-2, 2-3, 3-4...) halinde çiz!
      for (let i = 0; i < pts.length - 1; i++) {{
        const cur = pts[i];
        const next = pts[i + 1];

        // 1. Ana Kiriş (1/8 veya 1/16 olan tüm bağlı komşular arasına):
        const b1 = document.createElementNS("http://www.w3.org/2000/svg", "line");
        b1.setAttribute("x1", cur.x); b1.setAttribute("y1", getBeamY(cur.x));
        b1.setAttribute("x2", next.x); b1.setAttribute("y2", getBeamY(next.x));
        b1.setAttribute("stroke", "var(--stave-note)"); b1.setAttribute("stroke-width", "3.6");
        parent.appendChild(b1);

        // 2. İkinci Kiriş (1/16):
        const curIs16 = (cur.note.duration === '1/16' || cur.note.beam === 'double');
        const nextIs16 = (next.note.duration === '1/16' || next.note.beam === 'double');

        if (curIs16 && nextIs16) {{
          const b2 = document.createElementNS("http://www.w3.org/2000/svg", "line");
          b2.setAttribute("x1", cur.x); b2.setAttribute("y1", getBeamY(cur.x) + beamOffset);
          b2.setAttribute("x2", next.x); b2.setAttribute("y2", getBeamY(next.x) + beamOffset);
          b2.setAttribute("stroke", "var(--stave-note)"); b2.setAttribute("stroke-width", "2.8");
          parent.appendChild(b2);
        }} else if (curIs16 && !nextIs16) {{
          const b2 = document.createElementNS("http://www.w3.org/2000/svg", "line");
          const beamletX = cur.x + Math.min(18, (next.x - cur.x) * 0.4);
          b2.setAttribute("x1", cur.x); b2.setAttribute("y1", getBeamY(cur.x) + beamOffset);
          b2.setAttribute("x2", beamletX); b2.setAttribute("y2", getBeamY(beamletX) + beamOffset);
          b2.setAttribute("stroke", "var(--stave-note)"); b2.setAttribute("stroke-width", "2.8");
          parent.appendChild(b2);
        }} else if (!curIs16 && nextIs16) {{
          const b2 = document.createElementNS("http://www.w3.org/2000/svg", "line");
          const beamletX = next.x - Math.min(18, (next.x - cur.x) * 0.4);
          b2.setAttribute("x1", beamletX); b2.setAttribute("y1", getBeamY(beamletX) + beamOffset);
          b2.setAttribute("x2", next.x); b2.setAttribute("y2", getBeamY(next.x) + beamOffset);
          b2.setAttribute("stroke", "var(--stave-note)"); b2.setAttribute("stroke-width", "2.8");
          parent.appendChild(b2);
        }}
      }}
    }}

    
