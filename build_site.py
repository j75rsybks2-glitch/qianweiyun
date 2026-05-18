#!/usr/bin/env python3
"""Generate index.html for 扬州千味韵食品有限公司"""
from pathlib import Path

t = "motion"  # placeholder - will be replaced
TAG = "div"

def T(open_attr="", close=False, self_close=False):
    if self_close:
        return f"<{TAG}{open_attr} />"
    if close:
        return f"</{TAG}>"
    return f"<{TAG}{open_attr}>"

out = []
a = out.append

a("<!DOCTYPE html>")
a('<html lang="zh-CN">')
a("<head>")
a('  <meta charset="UTF-8" />')
a('  <meta name="viewport" content="width=device-width, initial-scale=1.0" />')
a('  <meta name="description" content="扬州千味韵食品有限公司 — 专业烘焙类休闲食品，以现代技术做好中华传统糕点" />')
a("  <title>扬州千味韵食品 | 中华传统糕点 · 现代匠心制作</title>")
a('  <link rel="preconnect" href="https://fonts.googleapis.com" />')
a('  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />')
a('  <link href="https://fonts.googleapis.com/css2?family=Noto+Sans+SC:wght@300;400;500;600;700&family=Playfair+Display:wght@600;700&display=swap" rel="stylesheet" />')
a('  <link rel="stylesheet" href="css/styles.css" />')
a("</head>")
a("<body>")

a('  <header class="header" id="header">')
a('    <nav class="nav container">')
a('      <a href="#home" class="logo"><span class="logo-icon" aria-hidden="true">🥮</span><span class="logo-text">千味韵食品</span></a>')
a('      <button class="nav-toggle" id="navToggle" aria-label="打开菜单" aria-expanded="false"><span></span><span></span><span></span></button>')
a('      <ul class="nav-menu" id="navMenu">')
for href, label, extra in [
    ("about", "公司简介", ""),
    ("history", "发展历程", ""),
    ("products", "主要产品", ""),
    ("partners", "合作伙伴", ""),
    ("contact", "联系我们", " nav-link--cta"),
]:
    a(f'        <li><a href="#{href}" class="nav-link{extra}">{label}</a></li>')
a("      </ul>")
a("    </nav>")
a("  </header>")
a("  <main>")

a('    <section class="hero" id="home">')
a('      <motion class="hero-bg" aria-hidden="true"></motion>'.replace("motion", TAG))
a('      <motion class="hero-overlay" aria-hidden="true"></motion>'.replace("motion", TAG))
a('      <motion class="hero-content container">'.replace("motion", TAG))
a('        <p class="hero-tag">扬州 · 专业烘焙糕点</p>')
a("        <h1 class=\"hero-title\">以现代技术<br /><em>做好传统糕点</em></h1>")
a(
    "        <p class=\"hero-desc\">扬州千味韵食品有限公司坚守中华糕点匠心，蜂蜜黑芝麻饼、蔓越莓混色绿豆冰糕等明星产品畅销全国，携手三只松鼠、味滋源等知名伙伴服务千家万户。</p>"
)
a('        <motion class="hero-actions">'.replace("motion", TAG))
a('          <a href="#products" class="btn btn-primary">查看产品</a>')
a('          <a href="#about" class="btn btn-outline">了解我们</a>')
a(f"        </{TAG}>")
a(f'        <motion class="hero-stats">'.replace("motion", TAG))
for n, lbl in [(4, "糕点品类"), (7, "明星产品"), (100, "覆盖全国")]:
    a(
        f'          <motion class="stat"><span class="stat-num" data-count="{n}">0</span><span class="stat-label">{lbl}</span></{TAG}>'.replace(
            "motion", TAG
        )
    )
a(f"        </{TAG}>")
a(f"      </{TAG}>")
a('      <a href="#about" class="hero-scroll" aria-label="向下滚动"><span></span></a>')
a("    </section>")

a('    <section class="section about" id="about">')
a(f'      <motion class="container">'.replace("motion", TAG))
a('        <header class="section-header">')
a('          <span class="section-tag">About Us</span>')
a("          <h2 class=\"section-title\">公司简介</h2>")
a('          <p class="section-subtitle">诚信为主 · 用户至上 · 优质服务 · 信守合同</p>')
a("        </header>")
a(f'        <motion class="about-grid">'.replace("motion", TAG))
a(f'          <motion class="about-image">'.replace("motion", TAG))
a('            <motion class="about-image-main"></motion>'.replace("motion", TAG))
a(f'            <motion class="about-badge">'.replace("motion", TAG))
a('              <span class="about-badge-num">HACCP</span>')
a('              <span class="about-badge-text">危害分析与关键控制点认证</span>')
a(f"            </{TAG}>")
a(f"          </{TAG}>")
a(f'          <motion class="about-content">'.replace("motion", TAG))
a(
    "            <p><strong>扬州千味韵食品有限公司</strong>位于江苏省扬州市，是一家专业的烘焙类休闲食品公司，主要经营食品生产、食品销售及食品互联网销售业务。</p>"
)
a(
    "            <p>公司坚守「以现代新型技术做好中华传统糕点」的企业理念，主营酥类、酥皮类、烘糕类和水油皮类等烘焙糕点。除桃酥、蛋糕、麻花等传统产品外，还研发了蔓越莓绿豆冰糕、蜂蜜黑芝麻饼等深受年轻人喜爱的创新糕点，产品保质保量，畅销全国。</p>"
)
a("            <ul class=\"about-features\">")
for title, desc in [
    ("传统与创新并重", "传承中式糕点技艺，持续推出年轻化新品"),
    ("绿色健康理念", "黑芝麻饼等传统手艺制作，无食品添加剂"),
    ("全渠道触达", "线下门店与线上电商平台，送达千家万户"),
]:
    a(
        f'              <li><span class="feature-icon">✓</span><motion><strong>{title}</strong><span>{desc}</span></{TAG}></li>'.replace(
            "motion", TAG
        )
    )
a("            </ul>")
a(f"          </{TAG}>")
a(f"        </{TAG}>")
a(f"      </{TAG}>")
a("    </section>")

a('    <section class="section history" id="history">')
a(f'      <motion class="container">'.replace("motion", TAG))
a('        <header class="section-header section-header--light">')
a('          <span class="section-tag">Our Journey</span>')
a("          <h2 class=\"section-title\">发展历程</h2>")
a('          <p class="section-subtitle">扎根扬州，匠心做好每一块糕点</p>')
a("        </header>")
a(f'        <motion class="timeline">'.replace("motion", TAG))
milestones = [
    ("创立", "扎根扬州", "公司在江苏扬州成立，专注烘焙类休闲食品的生产与销售。"),
    ("品质", "通过 HACCP 认证", "建立危害分析与关键控制点体系，以过硬技术保障产品保质保量。"),
    ("创新", "明星产品问世", "蔓越莓混色绿豆冰糕、蜂蜜黑芝麻饼等创新糕点上市，口碑迅速攀升。"),
    ("拓展", "畅销全国", "产品通过线下门店与互联网电商渠道覆盖全国，客户遍布各地。"),
    ("合作", "携手知名品牌", "与三只松鼠、味滋源等知名企业建立合作，持续拓展市场版图。"),
]
for when, title, desc in milestones:
    a("          <article class=\"timeline-item\">")
    a('            <motion class="timeline-dot"></motion>'.replace("motion", TAG))
    a(f'            <motion class="timeline-card">'.replace("motion", TAG))
    a(f"              <time>{when}</time><h3>{title}</h3><p>{desc}</p>")
    a(f"            </{TAG}>")
    a("          </article>")
a(f"        </{TAG}>")
a(f"      </{TAG}>")
a("    </section>")

a('    <section class="section products" id="products">')
a(f'      <motion class="container">'.replace("motion", TAG))
a('        <header class="section-header">')
a('          <span class="section-tag">Products</span>')
a("          <h2 class=\"section-title\">主要产品</h2>")
a('          <p class="section-subtitle">酥类 · 酥皮类 · 烘糕类 · 水油皮类</p>')
a("        </header>")

a(f'        <motion class="products-hot">'.replace("motion", TAG))
a('          <h3 class="products-hot-title">🔥 热销产品</h3>')
a(f'          <motion class="products-hot-grid">'.replace("motion", TAG))
hot = [
    ("bing", "蜂蜜黑芝麻饼", "传统手艺纯手工制作，无任何食品添加剂。营养高钙、口感酥脆、芝麻香浓郁，老少皆宜，是许多家庭年货首选。"),
    ("gao", "蔓越莓混色绿豆冰糕", "改良传统绿豆糕，口感清甜丝滑、入口即化。绿豆气息醇正细腻，蔓越莓的加入令层次更加丰富。"),
]
for img, name, desc in hot:
    a("            <article class=\"product-card product-card--featured\">")
    a(f'              <motion class="product-card-img product-card-img--{img}"></motion>'.replace("motion", TAG))
    a(f'              <motion class="product-card-body">'.replace("motion", TAG))
    a(f"                <h3>{name}</h3><p>{desc}</p>")
    a('                <span class="product-tag product-tag--hot">热销</span>')
    a(f"              </{TAG}>")
    a("            </article>")
a(f"          </{TAG}>")
a(f"        </{TAG}>")

a(f'        <motion class="product-tabs" role="tablist">'.replace("motion", TAG))
a('          <button class="product-tab active" role="tab" aria-selected="true" data-tab="pastry">糕点系列</button>')
a('          <button class="product-tab" role="tab" aria-selected="false" data-tab="sesame">芝麻养生</button>')
a(f"        </{TAG}>")

a(f'        <motion class="product-panels">'.replace("motion", TAG))
pastry = [
    ("mooncake", "桃山皮流心月饼", "酥皮细腻，流心饱满，中秋佳节与家人共享的精致之选。"),
    ("futuan", "纯可可脂爆浆福团", "选用纯可可脂，外糯内滑，一口爆浆，巧克力爱好者的治愈零食。"),
    ("dagee", "元气打糕", "软糯 Q 弹，甜而不腻，休闲时刻补充能量的元气小食。"),
]
sesame = [
    ("paste", "黑芝麻核桃软膏", "黑芝麻与核桃科学配比，香浓绵密，营养滋补的养生糕点。"),
    ("ball", "九蒸九晒芝麻丸", "遵循九蒸九晒古法工艺，浓缩芝麻精华，方便即食的健康小丸。"),
]

a('          <motion class="product-panel active" id="panel-pastry" role="tabpanel">'.replace("motion", TAG))
a(f'            <motion class="product-grid">'.replace("motion", TAG))
for img, name, desc in pastry:
    a("              <article class=\"product-card\">")
    a(f'                <motion class="product-card-img product-card-img--{img}"></motion>'.replace("motion", TAG))
    a(f'                <motion class="product-card-body"><h3>{name}</h3><p>{desc}</p></{TAG}>'.replace("motion", TAG))
    a("              </article>")
a(f"            </{TAG}>")
a(f"          </{TAG}>")

a('          <motion class="product-panel" id="panel-sesame" role="tabpanel" hidden>'.replace("motion", TAG))
a(f'            <motion class="product-grid">'.replace("motion", TAG))
for img, name, desc in sesame:
    a("              <article class=\"product-card\">")
    a(f'                <motion class="product-card-img product-card-img--{img}"></motion>'.replace("motion", TAG))
    a(f'                <motion class="product-card-body"><h3>{name}</h3><p>{desc}</p></{TAG}>'.replace("motion", TAG))
    a("              </article>")
a(f"            </{TAG}>")
a(f"          </{TAG}>")
a(f"        </{TAG}>")
a(f"      </{TAG}>")
a("    </section>")

a('    <section class="section partners" id="partners">')
a(f'      <motion class="container">'.replace("motion", TAG))
a('        <header class="section-header">')
a('          <span class="section-tag">Partners</span>')
a("          <h2 class=\"section-title\">合作伙伴</h2>")
a('          <p class="section-subtitle">与行业领先品牌携手，将好味道带给更多消费者</p>')
a("        </header>")
a(
    '        <p class="partners-intro">凭借高质量产品与过硬专业技术、良好信誉与优质服务，千味韵客户范围遍布全国。公司与三只松鼠、味滋源等知名企业建立深度合作，并通过线上线下多渠道将产品送达千家万户。</p>'
)
a(f'        <motion class="partners-grid">'.replace("motion", TAG))
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
    a(f'          <motion class="{cls}">{name}</{TAG}>'.replace("motion", TAG))
a(f"        </{TAG}>")
a(f'        <motion class="partners-metrics">'.replace("motion", TAG))
for val, lbl in [("HACCP", "体系认证"), ("全国", "客户覆盖"), ("4 类", "主营糕点品类")]:
    a(f'          <motion class="metric-card"><span class="metric-value">{val}</span><span class="metric-label">{lbl}</span></{TAG}>'.replace("motion", TAG))
a(f"        </{TAG}>")
a(f"      </{TAG}>")
a("    </section>")

a('    <section class="section contact" id="contact">')
a(f'      <motion class="container">'.replace("motion", TAG))
a('        <header class="section-header section-header--light">')
a('          <span class="section-tag">Contact</span>')
a("          <h2 class=\"section-title\">联系我们</h2>")
a('          <p class="section-subtitle">欢迎洽谈产品合作、渠道代理与 OEM 定制</p>')
a("        </header>")
a(f'        <motion class="contact-grid">'.replace("motion", TAG))
a(f'          <motion class="contact-info">'.replace("motion", TAG))
contacts = [
    ("📍", "公司地址", "江苏省扬州市"),
    ("🏭", "主营业务", "食品生产 · 食品销售 · 食品互联网销售"),
    ("🥮", "主营产品", "烘焙糕点、绿豆冰糕、流心月饼、黑芝麻系列等"),
    ("🤝", "商务合作", "欢迎渠道经销商及 OEM 定制洽谈"),
]
for icon, title, text in contacts:
    a(f'            <motion class="contact-item"><span class="contact-icon" aria-hidden="true">{icon}</span><motion><strong>{title}</strong><p>{text}</p></{TAG}></{TAG}>'.replace("motion", TAG))
a(f'            <motion class="contact-map"><motion class="map-placeholder"><span>江苏省扬州市</span><small>可嵌入百度/高德地图 iframe</small></{TAG}></{TAG}>'.replace("motion", TAG))
a(f"          </{TAG}>")

a('          <form class="contact-form" id="contactForm" novalidate>')
a("            <h3>在线留言</h3>")
a('            <motion class="form-group"><label for="name">姓名 <span>*</span></label><input type="text" id="name" name="name" required placeholder="请输入您的姓名" /></{TAG}>'.replace("motion", TAG))
a(f'            <motion class="form-row">'.replace("motion", TAG))
a('              <motion class="form-group"><label for="phone">电话 <span>*</span></label><input type="tel" id="phone" name="phone" required placeholder="手机或座机" /></{TAG}>'.replace("motion", TAG))
a('              <motion class="form-group"><label for="email">邮箱</label><input type="email" id="email" name="email" placeholder="选填" /></{TAG}>'.replace("motion", TAG))
a(f"            </{TAG}>")
a('            <motion class="form-group"><label for="subject">咨询类型</label>'.replace("motion", TAG))
a('              <select id="subject" name="subject">')
for v, l in [("product", "产品咨询"), ("channel", "渠道代理"), ("oem", "代工定制"), ("cooperation", "商务合作"), ("other", "其他")]:
    a(f'                <option value="{v}">{l}</option>')
a("              </select>")
a(f"            </{TAG}>")
a('            <motion class="form-group"><label for="message">留言内容 <span>*</span></label><textarea id="message" name="message" rows="4" required placeholder="请描述您的合作或采购需求…"></textarea></{TAG}>'.replace("motion", TAG))
a('            <button type="submit" class="btn btn-primary btn-block">提交留言</button>')
a('            <p class="form-note" id="formNote" role="status" aria-live="polite"></p>')
a("          </form>")
a(f"        </{TAG}>")
a(f"      </{TAG}>")
a("    </section>")
a("  </main>")

a('  <footer class="footer">')
a(f'    <motion class="container footer-inner">'.replace("motion", TAG))
a('      <motion class="footer-brand"><span class="logo-icon" aria-hidden="true">🥮</span><span>扬州千味韵食品有限公司</span></{TAG}>'.replace("motion", TAG))
a("      <p class=\"footer-copy\">© 2026 扬州千味韵食品 版权所有</p>")
a(f'      <motion class="footer-links"><a href="#about">关于我们</a><a href="#products">产品中心</a><a href="#contact">联系我们</a></{TAG}>'.replace("motion", TAG))
a(f"    </{TAG}>")
a("  </footer>")
a('  <script src="js/main.js"></script>')
a("</body>")
a("</html>")

html = "\n".join(out)
# Safety: ensure no stray placeholder
html = html.replace("motion", TAG)
path = Path(__file__).parent / "index.html"
path.write_text(html, encoding="utf-8")
print(f"Wrote {path} ({len(html)} bytes, {len(out)} lines)")
assert "motion" not in html
