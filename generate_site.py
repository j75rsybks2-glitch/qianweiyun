#!/usr/bin/env python3
"""Generate index.html for 扬州千味韵食品有限公司."""
from pathlib import Path
from urllib.parse import quote as urlquote

D = "motion"  # replaced below
D = "d" + "iv"

PRODUCTS = [
    {
        "id": "gao",
        "name": "蔓越莓混色绿豆冰糕",
        "hot": True,
        "images": ["p01.jpg", "p02.jpg"],
        "slogan": "巧食清爽一整夏 · 雅致小食，冰爽一夏",
        "desc": "改良传统绿豆糕，黄绿混色、花纹雅致。清新的绿豆气息醇正细腻、软糯怡人；蔓越莓酸甜与绿豆清香融合，口感清新、酸甜细滑，入口即化。",
        "features": ["口感清新 微甜不腻", "入口即化 细润绵柔", "一口软糯 夹杂嚼劲", "丝丝凉爽 自然而美好"],
    },
    {
        "id": "mooncake",
        "name": "桃山皮流心月饼",
        "hot": False,
        "images": ["p03.jpg"],
        "slogan": "匠心制作 多种口味 · 入口润滑 甜而不腻",
        "desc": "桃山皮细腻柔滑，多种口味流心——奶白、金黄、莓红等色彩饱满。切开可见浓稠流心缓缓溢出，花香造型款与经典款兼具仪式感与美味。",
        "features": ["桃山皮酥软", "流心饱满", "甜而不腻", "中秋礼盒首选"],
    },
    {
        "id": "futuan",
        "name": "纯可可脂爆浆福团",
        "hot": False,
        "images": ["p04.jpg", "p05.jpg"],
        "slogan": "醇香诱惑 爆浆流心 · 一口就爱上的小福团",
        "desc": "Q 弹软糯雪媚娘外衣，裹挟纯可可脂巧克力爆浆内馅。外裹可可粉，醇香浓郁、微苦丝滑，多重口感层层推进，更醇滑、更放心、更 Q 弹。",
        "features": ["纯可可脂", "爆浆流心", "Q 弹外皮", "微苦丝滑"],
    },
    {
        "id": "dagee",
        "name": "元气打糕",
        "hot": False,
        "images": ["p06.jpg", "p07.jpg"],
        "slogan": "外酥里软 口感软糯 · 软糯夹心 口感细腻",
        "desc": "浓郁软曲奇包裹 Q 弹雪媚娘夹心，抹茶、巧克力、草莓等多口味。曲奇表面点缀巧克力豆，口感顺滑、轻柔绵软有嚼劲，香甜细腻、味道浓郁、不粘牙。",
        "features": ["外酥里软", "雪媚娘夹心", "多口味可选", "香甜不腻"],
    },
    {
        "id": "paste",
        "name": "黑芝麻核桃软膏",
        "hot": False,
        "images": ["p08.png", "p09.png"],
        "slogan": "看得见的好料 · 营养滋补",
        "desc": "黑芝麻与大块核桃仁、枸杞等科学配比，切块方正、质地紧实。芝麻香浓、核桃酥脆，是老少皆宜的养生糕点零食。",
        "features": ["大块核桃", "黑芝麻香", "营养滋补", "手工质感"],
    },
    {
        "id": "ball",
        "name": "九蒸九晒芝麻丸",
        "hot": False,
        "images": ["p10.jpg", "p11.jpg"],
        "slogan": "营养丰富 无腹担放肆吃 · 随时随地 尽享好味",
        "desc": "遵循九蒸九晒古法，黑芝麻为主，辅以枸杞、核桃等。丸体圆润、芝香浓郁，以黑养黑、口口芝香，方便随时享用的健康小食。",
        "features": ["九蒸九晒", "以黑养黑", "口口芝香", "随时享用"],
    },
    {
        "id": "bing",
        "name": "蜂蜜黑芝麻饼",
        "hot": True,
        "images": ["p12.png", "p13.png", "p14.png"],
        "slogan": "黑芝麻做的饼！ · 老师傅手工匠心制作",
        "desc": "传统手艺纯手工，蜂蜜粘合饱满黑芝麻，酥脆香浓。颗粒均匀、圆润饱满，甄选优质原料；酥、脆、香、浓四感兼具，轻吸收、原滋原味，是许多家庭年货首选。",
        "features": ["0 添加香精", "0 添加色素", "0 添加白砂糖", "0 添加防腐剂"],
    },
]

NEWS_URL = "https://finance.sina.com.cn/wm/2026-02-26/doc-inhpcyyc0411244.shtml?froms=ggmp"
COMPANY_ADDRESS = "江苏省扬州市仪征市荣能路1号"


def showcase(p, reverse=False):
    imgs = "".join(
        f'              <img src="assets/products/{fn}" alt="{p["name"]}" loading="lazy" />\n'
        for fn in p["images"]
    )
    hot = f'              <span class="product-tag product-tag--hot">热销</span>\n' if p.get("hot") else ""
    feats = "".join(f"                <li>{f}</li>\n" for f in p["features"])
    rev = " product-showcase--reverse" if reverse else ""
    return f"""        <article class="product-showcase{rev}" id="product-{p['id']}">
          <{D} class="product-showcase-grid">
            <{D} class="product-showcase-gallery">
{imgs}            </{D}>
            <{D} class="product-showcase-content">
{hot}              <h3 class="product-showcase-title">{p['name']}</h3>
              <p class="product-showcase-slogan">{p['slogan']}</p>
              <p class="product-showcase-desc">{p['desc']}</p>
              <ul class="product-showcase-features">
{feats}              </ul>
            </{D}>
          </{D}>
        </article>
"""


def hot_card(p):
    img = p["images"][0]
    short = p["slogan"].split("·")[0].strip()
    return f"""            <a href="#product-{p['id']}" class="product-hot-card">
              <img src="assets/products/{img}" alt="{p['name']}" loading="lazy" />
              <{D} class="product-hot-card-body">
                <span class="product-tag product-tag--hot">热销</span>
                <h3>{p['name']}</h3>
                <p>{short}</p>
              </{D}>
            </a>"""


lines = []
w = lines.append

w("<!DOCTYPE html>")
w('<html lang="zh-CN">')
w("<head>")
w('  <meta charset="UTF-8" />')
w('  <meta name="viewport" content="width=device-width, initial-scale=1.0" />')
w('  <meta name="description" content="扬州千味韵食品有限公司 — 专业烘焙糕点，蜂蜜黑芝麻饼、蔓越莓绿豆冰糕热销全国" />')
w("  <title>扬州千味韵食品 | 中华传统糕点 · 现代匠心制作</title>")
w('  <link rel="preconnect" href="https://fonts.googleapis.com" />')
w('  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />')
w('  <link href="https://fonts.googleapis.com/css2?family=Noto+Sans+SC:wght@300;400;500;600;700&family=Playfair+Display:wght@600;700&display=swap" rel="stylesheet" />')
w('  <link rel="stylesheet" href="css/styles.css" />')
w("</head>")
w("<body>")

w(f'  <header class="header" id="header">')
w(f'    <nav class="nav container">')
w('      <a href="#home" class="logo"><span class="logo-icon" aria-hidden="true">🥮</span><span class="logo-text">千味韵食品</span></a>')
w('      <button class="nav-toggle" id="navToggle" aria-label="打开菜单" aria-expanded="false"><span></span><span></span><span></span></button>')
w('      <ul class="nav-menu" id="navMenu">')
nav = [
    ("about", "公司简介", ""),
    ("history", "发展历程", ""),
    ("products", "主要产品", ""),
    ("news", "企业动态", ""),
    ("partners", "合作伙伴", ""),
    ("contact", "联系我们", " nav-link--cta"),
]
for href, label, extra in nav:
    w(f'        <li><a href="#{href}" class="nav-link{extra}">{label}</a></li>')
w("      </ul>")
w("    </nav>")
w("  </header>")
w("  <main>")

w('    <section class="hero" id="home">')
w(f'      <{D} class="hero-bg" aria-hidden="true"></{D}>')
w(f'      <{D} class="hero-overlay" aria-hidden="true"></{D}>')
w(f'      <{D} class="hero-content container">')
w('        <p class="hero-tag">扬州 · 专业烘焙糕点</p>')
w("        <h1 class=\"hero-title\">以现代技术<br /><em>做好传统糕点</em></h1>")
w("        <p class=\"hero-desc\">扬州千味韵食品有限公司坚守中华糕点匠心，蜂蜜黑芝麻饼、蔓越莓混色绿豆冰糕等明星产品畅销全国，携手三只松鼠、味滋源等知名伙伴服务千家万户。</p>")
w(f'        <{D} class="hero-actions">')
w('          <a href="#products" class="btn btn-primary">查看产品</a>')
w('          <a href="#news" class="btn btn-outline">企业动态</a>')
w(f"        </{D}>")
w(f'        <{D} class="hero-stats">')
w(f'          <{D} class="stat"><span class="stat-num" data-count="4">0</span><span class="stat-label">糕点品类</span></{D}>')
w(f'          <{D} class="stat"><span class="stat-num" data-count="7">0</span><span class="stat-label">明星产品</span></{D}>')
w(f'          <{D} class="stat"><span class="stat-num stat-num--text">全国</span><span class="stat-label">畅销各地</span></{D}>')
w(f"        </{D}>")
w(f"      </{D}>")
w('      <a href="#about" class="hero-scroll" aria-label="向下滚动"><span></span></a>')
w("    </section>")

w('    <section class="section about" id="about">')
w(f'      <{D} class="container">')
w('        <header class="section-header">')
w('          <span class="section-tag">About Us</span>')
w("          <h2 class=\"section-title\">公司简介</h2>")
w('          <p class="section-subtitle">诚信为主 · 用户至上 · 优质服务 · 信守合同</p>')
w("        </header>")
w(f'        <{D} class="about-grid">')
w(f'          <{D} class="about-image">')
w(f'            <{D} class="about-image-main"></{D}>')
w(f'            <{D} class="about-badge">')
w('              <span class="about-badge-num">HACCP</span>')
w('              <span class="about-badge-text">危害分析与关键控制点认证</span>')
w(f"            </{D}>")
w(f"          </{D}>")
w(f'          <{D} class="about-content">')
w(f"            <p><strong>扬州千味韵食品有限公司</strong>位于{COMPANY_ADDRESS}，是一家专业的烘焙类休闲食品公司，主要经营食品生产、食品销售及食品互联网销售业务。</p>")
w("            <p>公司坚守「以现代新型技术做好中华传统糕点」的企业理念，主营酥类、酥皮类、烘糕类和水油皮类等烘焙糕点。除桃酥、蛋糕、麻花等传统产品外，还研发了蔓越莓绿豆冰糕、蜂蜜黑芝麻饼等深受年轻人喜爱的创新糕点，产品保质保量，畅销全国。</p>")
w("            <ul class=\"about-features\">")
for title, desc in [
    ("传统与创新并重", "传承中式糕点技艺，持续推出年轻化新品"),
    ("绿色健康理念", "黑芝麻饼等传统手艺制作，无食品添加剂"),
    ("全渠道触达", "线下门店与线上电商平台，送达千家万户"),
]:
    w(f'              <li><span class="feature-icon">✓</span><{D}><strong>{title}</strong><span>{desc}</span></{D}></li>')
w("            </ul>")
w(f"          </{D}>")
w(f"        </{D}>")
w(f"      </{D}>")
w("    </section>")

w('    <section class="section history" id="history">')
w(f'      <{D} class="container">')
w('        <header class="section-header section-header--light">')
w('          <span class="section-tag">Our Journey</span>')
w("          <h2 class=\"section-title\">发展历程</h2>")
w('          <p class="section-subtitle">扎根扬州，匠心做好每一块糕点</p>')
w("        </header>")
w(f'        <{D} class="timeline">')
milestones = [
    ("创立", "扎根扬州", "公司在江苏扬州成立，专注烘焙类休闲食品的生产与销售。"),
    ("品质", "通过 HACCP 认证", "建立危害分析与关键控制点体系，以过硬技术保障产品保质保量。"),
    ("创新", "明星产品问世", "蔓越莓混色绿豆冰糕、蜂蜜黑芝麻饼等创新糕点上市，口碑迅速攀升。"),
    ("拓展", "畅销全国", "产品通过线下门店与互联网电商渠道覆盖全国，客户遍布各地。"),
    ("合作", "携手知名品牌", "与三只松鼠、味滋源等知名企业建立合作，持续拓展市场版图。"),
]
for when, title, desc in milestones:
    w("          <article class=\"timeline-item\">")
    w(f'            <{D} class="timeline-dot"></{D}>')
    w(f'            <{D} class="timeline-card">')
    w(f"              <time>{when}</time><h3>{title}</h3><p>{desc}</p>")
    w(f"            </{D}>")
    w("          </article>")
w(f"        </{D}>")
w(f"      </{D}>")
w("    </section>")

# Products
w('    <section class="section products" id="products">')
w(f'      <{D} class="container">')
w('        <header class="section-header">')
w('          <span class="section-tag">Products</span>')
w("          <h2 class=\"section-title\">主要产品</h2>")
w('          <p class="section-subtitle">七大明星产品 · 传统糕点与现代工艺融合</p>')
w("        </header>")

w(f'        <{D} class="products-hot">')
w('          <h3 class="products-hot-title">🔥 热销产品</h3>')
w(f'          <{D} class="products-hot-grid">')
for p in PRODUCTS:
    if p.get("hot"):
        w(hot_card(p))
w(f"        </{D}>")
w(f"      </{D}>")

w(f'        <{D} class="product-showcase-list">')
for i, p in enumerate(PRODUCTS):
    w(showcase(p, reverse=(i % 2 == 1)))
w(f"        </{D}>")

w(f'        <p class="products-image-note">产品图片请放置于 <code>assets/products/</code> 目录，命名为 p01.jpg–p14.jpg（与物料 P1–P14 对应）。</p>')
w(f"      </{D}>")
w("    </section>")

# News
w('    <section class="section news" id="news">')
w(f'      <{D} class="container">')
w('        <header class="section-header">')
w('          <span class="section-tag">News</span>')
w("          <h2 class=\"section-title\">企业动态</h2>")
w('          <p class="section-subtitle">媒体报道 · 品质守护</p>')
w("        </header>")
w(f'        <article class="news-card">')
w(f'          <{D} class="news-card-meta">')
w('            <time datetime="2026-02-26">2026年2月26日</time>')
w('            <span class="news-source">新浪财经 · 转载《中国市场监管报》</span>')
w(f"          </{D}>")
w('          <h3 class="news-card-title"><a href="' + NEWS_URL + '" target="_blank" rel="noopener noreferrer">江苏扬州：「老味道」热腾腾</a></h3>')
w(f'          <{D} class="news-card-excerpt">')
w("            <p>大年初一早晨，江苏扬州千味韵食品有限公司刚装满货的货车缓缓驶出厂区。负责人肖立明表示：「过年期间我们开足马力生产年货，为的就是让大家过个红红火火的年，再累也值。」</p>")
w("            <p>走进生产车间，热腾腾的酥香味扑面而来。刚出炉的花生酥、芝麻饼在传送带上缓缓前行，工人们熟练操作。春节期间订单比平时多了不少，许多产品作为年货礼品发往各地。「过年嘛大家图的就是一个放心，咱们心里这道关一定要守住。」肖立明说。</p>")
w("            <p>仪征市市场监管局马集分局执法人员现场巡查原料台账与生产参数，强调「越是节前忙，越要按标准来，年货安全不能有一点马虎」。肖立明坦言：「执法人员经常来，我们反而更踏实。把风险消除在源头，才能让每一份年货都更加安全放心。」</p>")
w(f"          </{D}>")
w(f'          <a href="{NEWS_URL}" class="news-card-link" target="_blank" rel="noopener noreferrer">阅读全文 →</a>')
w("        </article>")
w(f"      </{D}>")
w("    </section>")

# Partners
w('    <section class="section partners" id="partners">')
w(f'      <{D} class="container">')
w('        <header class="section-header">')
w('          <span class="section-tag">Partners</span>')
w("          <h2 class=\"section-title\">合作伙伴</h2>")
w('          <p class="section-subtitle">与行业领先品牌携手，将好味道带给更多消费者</p>')
w("        </header>")
w("        <p class=\"partners-intro\">凭借高质量产品与过硬专业技术、良好信誉与优质服务，千味韵客户范围遍布全国。公司与三只松鼠、味滋源等知名企业建立深度合作，并通过线上线下多渠道将产品送达千家万户。</p>")
w(f'        <{D} class="partners-grid">')
for name, brand in [
    ("三只松鼠", True),
    ("味滋源", True),
    ("连锁商超", False),
    ("电商平台", False),
    ("互联网零售", False),
    ("线下门店", False),
    ("经销代理", False),
    ("食品供应链", False),
]:
    cls = "partner-logo partner-logo--brand" if brand else "partner-logo"
    w(f'          <{D} class="{cls}">{name}</{D}>')
w(f"        </{D}>")
w(f'        <{D} class="partners-metrics">')
for val, lbl in [("HACCP", "体系认证"), ("全国", "客户覆盖"), ("4 类", "主营糕点品类")]:
    w(f'          <{D} class="metric-card"><span class="metric-value">{val}</span><span class="metric-label">{lbl}</span></{D}>')
w(f"        </{D}>")
w(f"      </{D}>")
w("    </section>")

# Contact
w('    <section class="section contact" id="contact">')
w(f'      <{D} class="container">')
w('        <header class="section-header section-header--light">')
w('          <span class="section-tag">Contact</span>')
w("          <h2 class=\"section-title\">联系我们</h2>")
w('          <p class="section-subtitle">欢迎洽谈产品合作、渠道代理与 OEM 定制</p>')
w("        </header>")
w(f'        <{D} class="contact-grid">')
w(f'          <{D} class="contact-info">')
contacts = [
    ("📍", "公司地址", COMPANY_ADDRESS),
    ("🏭", "主营业务", "食品生产 · 食品销售 · 食品互联网销售"),
    ("🥮", "主营产品", "烘焙糕点、绿豆冰糕、流心月饼、黑芝麻系列等"),
    ("🤝", "商务合作", "欢迎渠道经销商及 OEM 定制洽谈"),
]
for icon, title, text in contacts:
    w(f'            <{D} class="contact-item"><span class="contact-icon" aria-hidden="true">{icon}</span><{D}><strong>{title}</strong><p>{text}</p></{D}></{D}>')
amap = "https://uri.amap.com/search?keyword=" + urlquote(COMPANY_ADDRESS)
baidu = "https://map.baidu.com/search/" + urlquote(COMPANY_ADDRESS + "/")
w(f'            <{D} class="contact-map">')
w(f'              <{D} class="location-map" role="img" aria-label="公司位置：{COMPANY_ADDRESS}">')
w(f'                <{D} class="location-map-visual">')
w('                  <svg class="location-map-grid" viewBox="0 0 320 180" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">')
w('                    <rect width="320" height="180" fill="#e8e0d4"/>')
w('                    <path d="M0 45h320M0 90h320M0 135h320M64 0v180M128 0v180M192 0v180M256 0v180" stroke="#d4c9b8" stroke-width="1"/>')
w('                    <path d="M40 120 Q120 80 200 100 T280 60" fill="none" stroke="#b8c9a8" stroke-width="8" stroke-linecap="round" opacity="0.6"/>')
w("                  </svg>")
w(f'                  <{D} class="location-pin" aria-hidden="true">')
w('                    <svg viewBox="0 0 24 36" width="48" height="72" xmlns="http://www.w3.org/2000/svg">')
w('                      <path d="M12 0C5.4 0 0 5.4 0 12c0 9 12 24 12 24s12-15 12-24c0-6.6-5.4-12-12-12z" fill="#c45c26"/>')
w('                      <circle cx="12" cy="12" r="5" fill="#fff"/>')
w("                    </svg>")
w(f"                  </{D}>")
w(f"                </{D}>")
w(f'                <{D} class="location-map-info">')
w("                  <strong>扬州千味韵食品有限公司</strong>")
w(f"                  <p>{COMPANY_ADDRESS}</p>")
w('                  <p class="location-hint">仪征市 · 高德地图暂未收录该点位</p>')
w(f'                  <{D} class="location-actions">')
w(f'                    <a href="{amap}" target="_blank" rel="noopener noreferrer" class="location-btn">高德地图搜索</a>')
w(f'                    <a href="{baidu}" target="_blank" rel="noopener noreferrer" class="location-btn location-btn--outline">百度地图搜索</a>')
w(f"                  </{D}>")
w(f"                </{D}>")
w(f"              </{D}>")
w(f"            </{D}>")
w(f"          </{D}>")
w('          <form class="contact-form" id="contactForm" novalidate>')
w("            <h3>在线留言</h3>")
w(f'            <{D} class="form-group"><label for="name">姓名 <span>*</span></label><input type="text" id="name" name="name" required placeholder="请输入您的姓名" /></{D}>')
w(f'            <{D} class="form-row">')
w(f'              <{D} class="form-group"><label for="phone">电话 <span>*</span></label><input type="tel" id="phone" name="phone" required placeholder="手机或座机" /></{D}>')
w(f'              <{D} class="form-group"><label for="email">邮箱</label><input type="email" id="email" name="email" placeholder="选填" /></{D}>')
w(f"            </{D}>")
w(f'            <{D} class="form-group"><label for="subject">咨询类型</label><select id="subject" name="subject">')
for v, l in [("product", "产品咨询"), ("channel", "渠道代理"), ("oem", "代工定制"), ("cooperation", "商务合作"), ("other", "其他")]:
    w(f'                <option value="{v}">{l}</option>')
w("              </select></{D}>".replace("{D}", D))
w(f'            <{D} class="form-group"><label for="message">留言内容 <span>*</span></label><textarea id="message" name="message" rows="4" required placeholder="请描述您的合作或采购需求…"></textarea></{D}>')
w('            <button type="submit" class="btn btn-primary btn-block">提交留言</button>')
w('            <p class="form-note" id="formNote" role="status" aria-live="polite"></p>')
w("          </form>")
w(f"        </{D}>")
w(f"      </{D}>")
w("    </section>")
w("  </main>")

w('  <footer class="footer">')
w(f'    <{D} class="container footer-inner">')
w(f'      <{D} class="footer-brand"><span class="logo-icon" aria-hidden="true">🥮</span><span>扬州千味韵食品有限公司</span></{D}>')
w("      <p class=\"footer-copy\">© 2026 扬州千味韵食品 版权所有</p>")
w(f'      <{D} class="footer-links"><a href="#about">关于我们</a><a href="#products">产品中心</a><a href="#news">企业动态</a><a href="#contact">联系我们</a></{D}>')
w(f"    </{D}>")
w("  </footer>")
w('  <script src="js/main.js"></script>')
w("</body>")
w("</html>")

html = "\n".join(lines)
Path(__file__).parent.joinpath("index.html").write_text(html, encoding="utf-8")
print("OK", len(html))
