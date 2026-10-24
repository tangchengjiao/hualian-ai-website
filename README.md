# 华链 AI 企业官网

企业 AI 业务落地与内生能力建设。展示真实服务、产品与应用方向、精选参考价、公开宣传册，以及见舟微信咨询入口。

**[访问官网](https://hualian-ai.fondmule128.chatgpt.site)** · [服务参考价](https://hualian-ai.fondmule128.chatgpt.site/pricing/) · [品牌资料中心](https://github.com/tangchengjiao/hualian-ai-brand-center)

## 页面

首页、企业服务、产品与场景、服务参考价、企业宣传册、联系见舟、关于我们、品牌与项目资源，共 8 页。

咨询功能为微信二维码、微信号复制和咨询提纲复制，不包含在线表单提交。完整服务报价不在网站源码和部署文件中。

## 源码与内容

- `dist/`：直接发布的静态 HTML、CSS、JavaScript 与公开素材。
- `content/company-content.json`：从企业宣传册整理的内容及来源页码。
- `scripts/build_site.py`：按品牌中心配置生成静态页面。
- `.openai/hosting.json`：Sites 托管身份和发布目录。

首页主视觉来自华链 AI 宣传册原图，保留透明通道。应用方向与已交付客户案例分开表述。

## 本地预览

```powershell
python -m http.server 4387 --bind 127.0.0.1 --directory dist
```

生成页面时指定本地品牌中心：

```powershell
python scripts/build_site.py --brand-center "品牌中心目录"
```

只从品牌中心 public/ 读取联系素材和企业宣传册；参考价格在生成脚本中维护对应的公开精选服务范围。

## 发布

本仓库是用户 GitHub 下的网站源码镜像，公开网站通过 Sites 发布。修改或推送本 GitHub 仓库不会自动改变线上网站；发布时需同步相同版本至 Sites 并部署。

品牌及企业资料保留相应权利，具体产品与第三方组件权利归各自所有者。

<!-- JIANZHOU-PUBLIC-INFO:START -->
## 企业服务与联系

**华链 AI** · 企业 AI 业务落地与内生能力建设

培训与 FDE 培养 · 场景验证 · 智能体定制 · 企业实施 · 产品应用支持

[华链 AI 官网](https://hualian-ai.fondmule128.chatgpt.site) · [企业服务](https://hualian-ai.fondmule128.chatgpt.site/services/) · [服务参考价](https://hualian-ai.fondmule128.chatgpt.site/pricing/) · [企业宣传册](https://hualian-ai.fondmule128.chatgpt.site/downloads/company-brochure.pdf) · [合作咨询](https://hualian-ai.fondmule128.chatgpt.site/contact/)

咨询联系人：**见舟** · 微信：**`DST10209`**

<img src="https://raw.githubusercontent.com/tangchengjiao/hualian-ai-brand-center/main/public/assets/contact/wechat-qr.png" alt="见舟微信二维码" width="200">

抖音：`74683161410` · 视频号：见舟AI赋能
<!-- JIANZHOU-PUBLIC-INFO:END -->
