"""Build the public Hualian AI website from approved brochure content and brand assets."""
import argparse
import json
import shutil
from html import escape as e
from pathlib import Path
from urllib.parse import quote

ROOT=Path(__file__).resolve().parents[1]
parser=argparse.ArgumentParser()
parser.add_argument('--brand-center',type=Path,default=ROOT.parent/'见舟品牌与发布中心')
args=parser.parse_args()
CENTER=args.brand_center
OUT=ROOT/'dist'
brand=json.loads((CENTER/'public/brand.json').read_text(encoding='utf-8'))
data=json.loads((ROOT/'content/company-content.json').read_text(encoding='utf-8'))
contact=brand['contact']
SITE='https://hualian-ai.fondmule128.chatgpt.site'
REPO='https://github.com/tangchengjiao/hualian-ai-brand-center'
def copy_public(source,destination):
    target=Path(destination)
    if target.exists():
        target.chmod(0o666)
    return shutil.copy2(source,destination)
for name in ['assets/contact','downloads']:
    shutil.copytree(CENTER/'public'/name,OUT/name,dirs_exist_ok=True,copy_function=copy_public)
shutil.copy2(CENTER/'public/brand.json',OUT/'brand.json')
ARROW='<span aria-hidden="true">↗</span>'
def button(text,href='/contact/',secondary=False):
    return f'<a class="button{" secondary" if secondary else ""}" href="{href}">{text}{ARROW}</a>'
def head(kicker,title,description):
    return f'<section class="page-head"><div class="wrap"><p class="eyebrow">{kicker}</p><h1>{title}</h1><p>{description}</p></div></section>'
def section_title(kicker,title,description=''):
    return f'<div class="section-head"><div><p class="eyebrow">{kicker}</p><h2>{title}</h2></div><p>{description}</p></div>'
def steps():
    items=[('了解需求','从实际工作、资料和卡点开始，明确希望改善的结果。'),('明确方案','选择服务方式，约定范围、阶段成果与参与人员。'),('开展实践','用真实任务搭建、试跑、反馈和调整。'),('交付与使用','交付应用与使用资料，帮助人员接续日常工作。')]
    return '<div class="steps">'+''.join(f'<div class="step"><span class="number">0{i}</span><h3>{t}</h3><p>{d}</p></div>' for i,(t,d) in enumerate(items,1))+'</div>'
def cta():
    return '<section class="cta-band"><div class="wrap cta-inner"><div><h2>从一个真实业务需求开始。</h2><p>说说你现在怎样工作，我们一起判断适合从哪里推进。</p></div>'+button('联系见舟，聊聊需求')+'</div></section>'
def page(path,title,description,body):
    navs=[('/','首页'),('/services/','企业服务'),('/products/','产品与场景'),('/pricing/','服务参考价'),('/brochure/','企业宣传册'),('/about/','关于我们')]
    nav=''.join(f'<a href="{url}"'+(' aria-current="page"' if path==url else '')+f'>{name}</a>' for url,name in navs)
    footer=f'''<footer class="footer"><div class="wrap"><div class="footer-main"><div><a class="logo" href="/">华链<span>AI</span></a><p>企业 AI 业务落地与内生能力建设</p><p>连接知识 · 激活应用 · 成就团队</p></div><div class="footer-links"><strong>服务与资料</strong><a href="/services/">企业 AI 服务</a><a href="/pricing/">服务参考价</a><a href="/brochure/">企业宣传册</a><a href="/brand/">品牌与项目资源</a></div><div class="footer-links"><strong>合作咨询 · {e(contact['name'])}</strong><a href="/contact/">微信：{e(contact['wechat'])}</a><a href="tel:075586372525">{e(contact['company_phone'])}</a><a href="/contact/#social">更多关注方式</a></div><div class="footer-qr"><img src="/assets/contact/wechat-qr.png" alt="见舟微信二维码" width="100" height="100" loading="lazy"><small>微信扫码联系见舟</small></div></div><div class="footer-bottom"><span>© 2026 华链 AI · 企业 AI 服务</span><span>完整服务报价请联系见舟获取</span></div></div></footer>'''
    html=f'''<!doctype html><html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{e(title)}｜华链 AI</title><meta name="description" content="{e(description)}"><meta name="theme-color" content="#124bb2"><link rel="canonical" href="{SITE}{path}"><meta property="og:title" content="{e(title)}｜华链 AI"><meta property="og:description" content="{e(description)}"><meta property="og:image" content="{SITE}/assets/company-hero.png"><link rel="icon" href="/favicon.svg" type="image/svg+xml"><link rel="stylesheet" href="/styles.css"><script src="/app.js" defer></script></head><body data-wechat="{e(contact['wechat'])}"><a class="sr-only" href="#main">跳至正文</a><header class="header"><div class="wrap header-inner"><a class="brand-lockup" href="/" aria-label="华链 AI 首页"><div class="logo">华链<span>AI</span></div><small>BUSINESS IN PRACTICE</small></a><button class="menu-toggle" aria-label="展开导航菜单" aria-expanded="false" aria-controls="site-nav">菜单</button><nav class="nav" id="site-nav" aria-label="主导航">{nav}</nav>{button('咨询见舟')}</div></header><main id="main">{body}</main>{cta()}{footer}<button class="button floating-contact" data-contact>微信咨询</button><dialog class="contact-dialog" id="wechat-dialog" aria-labelledby="contact-title"><button class="close" aria-label="关闭">×</button><p class="eyebrow">LET’S TALK</p><h2 id="contact-title">联系见舟</h2><p>企业 AI 服务咨询 · 获取完整服务报价</p><img src="/assets/contact/wechat-qr.png" alt="见舟微信二维码" width="210" height="210"><p>手机端可长按保存二维码，再用微信扫一扫识别。</p><button class="button" data-copy-wechat>复制微信号 {e(contact['wechat'])}</button></dialog></body></html>'''
    dest=OUT/path.strip('/')/'index.html' if path!='/' else OUT/'index.html'
    dest.parent.mkdir(parents=True,exist_ok=True)
    dest.write_text(html,encoding='utf-8')

service_rows=''.join(f'<div class="service-row"><span class="number">0{i}</span><h3>{e(s["name"])}</h3><p>{e(s["tagline"])}</p><a class="text-link" href="/services/#{s["id"]}">了解服务 ↗</a></div>' for i,s in enumerate(data['services'],1))
home=f'''<section class="hero"><div class="wrap hero-grid"><div><p class="eyebrow">企业 AI 业务落地与内生能力建设</p><h1>业务说清楚，<br>应用做出来，<br><em>团队用起来。</em></h1><p class="lead">从企业已有的资料、规则与经验出发，把 AI 接进真实任务，让应用落地，也让团队拥有持续推进的能力。</p><div class="actions">{button('咨询见舟')}{button('查看服务与参考价','/pricing/',True)}</div><div class="hero-foot">技术 × 场景 × 人才 · 从实际需求开始</div></div><div class="hero-visual"><img src="/assets/company-hero.png" alt="企业知识、数据与业务应用连接示意，来自华链 AI 宣传册" width="1536" height="1024" fetchpriority="high"><div class="visual-note"><span>企业知识</span><span>业务应用</span><span>内部人才</span></div></div></div></section>
<section class="section"><div class="wrap need-layout"><div><p class="eyebrow">START WITH YOUR BUSINESS</p><h2>你想先解决<br>哪一个问题？</h2><p>不必先决定买哪种工具。<br>先把任务、目标和使用的人讲清楚。</p></div><div><a class="need-row" href="/services/#scenario-validation"><span class="number">01</span><div><h3>想知道，哪里值得用 AI</h3><p>用样本和真实任务验证想法，判断下一步是否值得投入。</p></div><span>↗</span></a><a class="need-row" href="/services/#enterprise-implementation"><span class="number">02</span><div><h3>想把具体工作交给 AI</h3><p>构建智能体与应用，接入岗位、业务流程和现有系统。</p></div><span>↗</span></a><a class="need-row" href="/services/#fde-training"><span class="number">03</span><div><h3>想让内部人员继续推进</h3><p>让懂业务的人学会搭建、试用和改进，形成自己的落地力量。</p></div><span>↗</span></a></div></div></section>
<section class="section tinted"><div class="wrap">{section_title('WHAT WE DO','围绕业务，选择合适的服务。','从验证想法到建设应用，从带着团队使用到培养内部人才。')}<div>{service_rows}</div></div></section>
<section class="section"><div class="wrap">{section_title('HOW WE WORK','从需求到实际使用。','共同明确目标、服务方式与阶段成果。')}{steps()}</div></section>
<section class="section"><div class="wrap book-panel"><img src="/assets/brochure-cover.png" alt="华链 AI 企业服务宣传册封面" width="165" loading="lazy"><div><p class="eyebrow">COMPANY BROCHURE</p><h2>把服务与合作方式，讲得更具体。</h2><p>8 页企业服务手册，了解华链 AI 的业务方法、产品应用与合作流程。可在线阅读，也可下载后转发给团队。</p><div class="actions">{button('阅读企业宣传册','/brochure/')}{button('查看产品与应用','/products/',True)}</div></div></div></section>'''
page('/','企业 AI 服务与业务落地','华链 AI 提供场景验证、智能体定制、FDE 企业实施、业务人才培养与产品应用支持。联系见舟了解服务与参考报价。',home)

details=''
for i,s in enumerate(data['services'],1):
    deliverables=s.get('deliverables',s.get('formats',['上手指导与使用支持','按具体产品明确服务范围']))
    activities=s.get('activities',[])
    details+=f'<article class="service-detail" id="{s["id"]}"><span class="number">0{i}</span><div><h2>{e(s["name"])}</h2><strong>{e(s["tagline"])}</strong><p>{e(s["description"])}</p>'
    if activities: details+='<p>'+' → '.join(e(x) for x in activities)+'</p>'
    details+=f'<a class="text-link" href="/contact/?service={quote(s["name"])}">咨询这项服务 ↗</a></div><aside><h3>你能得到什么</h3><ul class="clean">'+''.join(f'<li>{e(x)}</li>' for x in deliverables)+'</ul></aside></article>'
page('/services/','企业服务','培训与陪跑、场景验证、智能体定制、企业 AI 实施及产品应用支持，围绕真实业务任务明确交付。',head('ENTERPRISE SERVICES','把业务能力，变成可使用的 AI 应用。','服务围绕实际任务展开。先了解资料、规则、岗位和目标，再选择适合的建设与学习方式。')+'<section class="section"><div class="wrap"><p class="intro-note">FDE 是深入业务现场的实施方式：了解人怎样工作，把应用接进流程，并带着团队试用与改进。</p>'+details+'</div></section><section class="section tinted"><div class="wrap">'+section_title('COOPERATION','每一步，都明确阶段成果。')+steps()+'</div></section>')

products=''.join(f'<article class="product"><span class="product-index">PRODUCT / 0{i}</span><h2>{e(p["name"])}</h2><h3>{e(p["category"])}</h3><p>{e(p["description"])}</p><a class="text-link" href="/contact/?service={quote(p["name"])}">咨询应用支持 ↗</a></article>' for i,p in enumerate(data['products'],1))
scenario_items=[('销售报价生成','结合客户需求、产品资料与价格规则，辅助生成报价方案。'),('经营分析与决策辅助','连接企业数据，辅助查询、分析与行动安排。'),('ERP 产品设计与建单','辅助形成产品、物料和工艺方案，人工确认后接续业务。'),('电商素材与铺货','围绕产品资料组织图文生成、翻译与草稿处理。'),('销售经验复用','将优秀人员的经验用于新人陪练和实战支持。'),('应用与业务系统','围绕订单、项目、生产和售后等实际流程建设应用。')]
scenarios=''.join(f'<article class="scenario"><h3>{e(t)}</h3><p>{e(d)}</p></article>' for t,d in scenario_items)
page('/products/','产品与应用方向','了解领势、智汇中枢、探流、PSD 智能工作台，以及企业 AI 的可探索应用方向。',head('PRODUCTS & APPLICATIONS','让产品，接到你的日常任务。','围绕已有产品开展应用支持，也可以从具体业务需求出发，探索适合的智能体与专属应用。')+'<section class="section"><div class="wrap"><div class="product-grid">'+products+'</div><p class="intro-note">产品订阅与配置、培训、定制服务分别明确范围；具体版本、额度和支持内容在方案中确认。</p></div></section><section class="section tinted"><div class="wrap">'+section_title('APPLICATION DIRECTIONS','从业务任务看应用机会。','以下为宣传册中的应用方向，具体可行性与实施范围需结合实际资料评估。')+'<div class="scenario-list">'+scenarios+'</div></div></section>')

prices=[('岗位 AI 主题工作坊','¥14,800–24,800','场','1 天、30 人以内、1 类岗位。','岗位任务练习与行动建议。'),('轻量场景验证','¥19,800–39,800','验证包','1 个明确假设、1 个场景，资料就绪；约 1–3 周。','代表性样本、原型、验证记录与后续建议。'),('单任务智能体配置／定制','¥19,800–49,800','任务包','基于已有平台，1 个明确任务、1 个使用入口及约定资料范围。','智能体／工作流配置、样本评测与操作说明。'),('轻量企业应用实施','¥39,800–98,000','项目','单场景，复用已有平台；约定工作流与最多 2 个已有可用接口。','建设、测试、业务试用、培训与交接。'),('专属应用建设','¥98,000–298,000','首期项目','1 条业务流程；按需配置专属页面、权限及系统对接。','约定应用、测试记录、部署与交接材料。')]
price_rows=''.join(f'<article class="price-row"><div><span class="tag">参考服务档位</span><h2>{e(name)}</h2><p>{e(scope)}</p><p><strong>主要交付：</strong>{e(delivery)}</p></div><div><div class="price">{price}</div><span class="unit">／{unit}</span><a class="text-link" href="/contact/?service={quote(name)}">咨询这项服务，获取完整报价 ↗</a></div></article>' for name,price,unit,scope,delivery in prices)
faq='''<div class="faq"><details><summary>这里的价格是最终报价吗？</summary><p>这是 2026 年 10 月试行报价中的精选参考档位，适用于所列标准范围。正式报价按实际任务、资料准备、系统对接和交付要求确认。</p></details><details><summary>软件订阅、模型调用和其他费用如何计算？</summary><p>软件授权、模型调用、硬件、异地差旅及税费是否包含，在具体服务方案和正式报价中列明。产品订阅与实施服务分别说明。</p></details><details><summary>培训、长期陪跑和产品支持怎样了解？</summary><p>可联系见舟说明团队人数、岗位、场景与希望获得的成果，我们会提供适合的服务方式和完整报价。活动价以具体班期或活动说明为准。</p></details><details><summary>验证之后继续建设，会重复计算费用吗？</summary><p>根据已完成、可复用的成果核算后续工作；具体阶段范围和费用在方案中明确。</p></details></div>'''
page('/pricing/','服务参考价','查看华链 AI 工作坊、场景验证、智能体配置与企业应用建设的参考预算。完整报价联系见舟微信获取。',head('SERVICE PRICING · 2026.10','先了解预算，再讨论具体方案。','以下为精选服务参考档位，帮助你判断投入范围。每个价格都对应具体的任务和交付范围，完整服务报价请联系见舟获取。')+'<section class="section"><div class="wrap"><div class="price-list">'+price_rows+'</div><p class="intro-note">参考价格版本：2026-10-09 / v1。实际范围、周期、税费和相关费用以正式方案为准。</p></div></section><section class="section tinted"><div class="wrap">'+section_title('BEFORE WE START','报价前，你可能还想了解。')+faq+'</div></section>')

options=[s['name'] for s in data['services']]+[p['name'] for p in data['products']]+[p[0] for p in prices]
select=''.join(f'<option value="{e(x)}">{e(x)}</option>' for x in dict.fromkeys(options))
socials=[('微信','wechat-qr.png',contact['wechat']),('抖音','douyin-qr.png',contact['douyin_id']),('视频号','channels-qr.png',contact['channels_name']),('公众号','official-account-qr.jpg','扫码关注')]
social_html=''.join(f'<div class="social"><img src="/assets/contact/{file}" alt="见舟{name}二维码" width="160" height="160" loading="lazy"><strong>{name}</strong><p>{e(account)}</p></div>' for name,file,account in socials)
contact_body=f'''<section class="section"><div class="wrap contact-layout"><div><div class="contact-primary"><img src="/assets/contact/wechat-qr.png" alt="见舟微信二维码" width="180" height="180"><div><h2>见舟</h2><p>企业 AI 服务咨询</p><div class="wechat">{e(contact['wechat'])}</div><button class="button" data-copy-wechat>复制微信号</button></div></div><p class="intro-note">手机端可长按保存二维码，打开微信扫一扫，从相册识别。完整服务报价请加微信获取。</p><p class="muted">企业电话：<a href="tel:075586372525">{e(contact['company_phone'])}</a></p></div><div class="contact-brief"><p class="eyebrow">PREPARE YOUR CONVERSATION</p><h2>带着一个具体任务来聊。</h2><label for="interest">你想了解什么？</label><select id="interest">{select}</select><label for="business-need">说说你的业务任务（选填）</label><textarea id="business-need" placeholder="例如：销售需要根据客户需求，从产品资料中整理报价；希望减少反复查找和手工录入。"></textarea><button class="button secondary" id="copy-brief">复制咨询提纲</button><p>内容仅在当前浏览器整理，点击复制后可自行粘贴到微信发送。</p></div></div></section><section class="section tinted" id="social"><div class="wrap">{section_title('FOLLOW & CONNECT','持续关注见舟。','AI 工具、企业应用与内容工作流实践。')}<div class="social-grid">{social_html}</div></div></section>'''
page('/contact/','联系见舟','微信联系见舟，咨询华链 AI 企业服务、培训陪跑、应用定制和完整服务报价。',head('CONTACT','从真实业务需求开始。','告诉我们你在什么岗位、怎样工作、希望改善哪个任务，共同明确适合的服务方式与阶段成果。')+contact_body)

outline=['关于华链 AI','场景验证与智能体定制','FDE 企业 AI 落地','业务 FDE 人才培养','AI 产品与应用支持','企业 AI 应用方向']
brochure=f'''<section class="section"><div class="wrap"><div class="brochure-layout"><img src="/assets/brochure-cover.png" alt="华链 AI 企业服务宣传册封面" width="250"><div><span class="tag">企业服务手册 · 8 页</span><h2>连接知识，激活应用，成就团队。</h2><p class="muted">了解华链 AI 如何从企业的资料、规则与员工经验出发，开展场景验证、应用建设和人才培养。</p><div class="brochure-outline">{''.join(f'<p><span class="number">0{i}</span>　{t}</p>' for i,t in enumerate(outline,1))}</div><div class="actions">{button('打开原版 PDF','/downloads/company-brochure.pdf')}<a class="button secondary" href="/downloads/company-brochure.pdf" download="华链AI-企业服务宣传册.pdf">下载宣传册 ↓</a></div><p class="intro-note">宣传册可公开阅读和转发。服务参考价见独立报价页，完整报价联系见舟获取。</p></div></div><iframe class="brochure-viewer" src="/downloads/company-brochure.pdf" title="华链 AI 企业服务宣传册在线阅读" loading="lazy"></iframe></div></section>'''
page('/brochure/','企业宣传册','在线阅读与下载华链 AI 企业服务宣传册，了解场景验证、智能体定制、FDE 企业实施与人才培养。',head('COMPANY BROCHURE','一份手册，了解华链 AI。','保留原版宣传册，方便你与团队一起讨论实际需求。')+brochure)

about=f'''<section class="section"><div class="wrap"><div class="about-copy"><p>{e(data['about'])}</p><p>我们关注的成果，是应用能处理真实任务、人员能够确认结果，团队能够继续使用和改进。</p></div><div class="steps"><div class="step"><span class="number">KNOWLEDGE</span><h3>连接知识</h3><p>把资料、规则与经验组织起来。</p></div><div class="step"><span class="number">APPLICATION</span><h3>激活应用</h3><p>让 AI 进入具体任务与业务流程。</p></div><div class="step"><span class="number">PEOPLE</span><h3>成就团队</h3><p>让懂业务的人掌握使用与改进方法。</p></div><div class="step"><span class="number">PROGRESS</span><h3>共同推进</h3><p>以真实任务的反馈持续调整。</p></div></div></div></section><section class="section tinted"><div class="wrap">{section_title('WORK TOGETHER','企业服务，直接联系见舟。','华链 AI 提供企业服务介绍与合作入口，见舟作为咨询联系人与你沟通需求。')}<div class="actions">{button('联系见舟')}{button('阅读企业宣传册','/brochure/',True)}</div></div></section>'''
page('/about/','关于华链 AI','华链 AI 专注企业 AI 应用与业务 FDE 人才培养，以真实任务推动企业应用与内部能力建设。',head('ABOUT HUALIAN AI','技术 × 场景 × 人才。','企业 AI 业务落地与内生能力建设。')+about)

brand_body=f'''<section class="section"><div class="wrap"><div class="public-brand-grid"><article class="brand-resource"><h2>企业宣传册</h2><p>华链 AI 企业服务介绍，支持阅读与下载。</p><a class="text-link" href="/brochure/">阅读宣传册 ↗</a></article><article class="brand-resource"><h2>服务与参考预算</h2><p>了解具体服务的适用范围与精选参考价。</p><a class="text-link" href="/pricing/">查看服务参考价 ↗</a></article><article class="brand-resource"><h2>联系与关注</h2><p>见舟的微信、抖音、视频号和公众号入口。</p><a class="text-link" href="/contact/">查看全部联系方式 ↗</a></article><article class="brand-resource"><h2>GitHub 品牌资料</h2><p>统一使用的品牌联系素材、公开资料与仓库发布标准。</p><a class="text-link" href="{REPO}">打开品牌中心 ↗</a></article></div></div></section>'''
page('/brand/','品牌与项目资源','华链 AI 与见舟的企业宣传册、联系素材、服务入口和 GitHub 品牌资料中心。',head('BRAND & RESOURCES','资料与入口，在这里汇合。','从项目来到这里，可以继续了解企业服务、参考预算，或直接联系见舟。')+brand_body)

(OUT/'favicon.svg').write_text('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><rect width="64" height="64" rx="12" fill="#124bb2"/><text x="32" y="43" text-anchor="middle" font-size="32" font-family="sans-serif" font-weight="800" fill="white">AI</text></svg>',encoding='utf-8')
paths=['/','/services/','/products/','/pricing/','/brochure/','/contact/','/about/','/brand/']
(OUT/'sitemap.xml').write_text('<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'+''.join(f'<url><loc>{SITE}{p}</loc></url>' for p in paths)+'</urlset>',encoding='utf-8')
(OUT/'robots.txt').write_text('User-agent: *\nAllow: /\nSitemap: '+SITE+'/sitemap.xml\n',encoding='utf-8')
print('Built',len(paths),'public pages. Only public brand assets and selected reference prices are included.')
