# 华链 AI 企业官网

企业 AI 业务落地与内生能力建设。展示真实服务、产品与应用方向、精选参考价、公开宣传册，以及见舟微信咨询入口。

**[访问官网](https://hualian-ai.pages.dev)** · [服务参考价](https://hualian-ai.pages.dev/pricing/) · [品牌资料中心](https://github.com/tangchengjiao/hualian-ai-brand-center)

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

正式官网由 **Cloudflare Pages** 托管：[https://hualian-ai.pages.dev](https://hualian-ai.pages.dev)。项目名为 `hualian-ai`，生产分支为 `main`，发布目录为 `dist/`。

本 GitHub 仓库保留完整源码、生成页面、公开资源、版本历史与部署说明，后续换服务器或托管平台可直接重新部署。当前采用 Direct Upload，推送 GitHub 本身不触发线上更新。

修改内容后，先根据品牌中心生成页面并提交源码，再用已登录的 Wrangler 发布：

```powershell
python scripts/build_site.py --brand-center "品牌中心目录"
pnpm dlx wrangler@4.152.0 pages deploy dist --project-name hualian-ai --branch main
```

也可通过 `--site-url` 指定已确认的新域名，以更新规范链接、分享图片地址和 sitemap。部署并验证成功后，将品牌中心与各项目的统一联系区同步为新地址。

原 `.openai/hosting.json` 及最初的 Sites 发布历史保留作为归档；正式官网的页面、联系图片和宣传册均由 Cloudflare 域名提供，完整服务报价不进入公开部署目录。

品牌及企业资料保留相应权利，具体产品与第三方组件权利归各自所有者。

<!-- JIANZHOU-PUBLIC-INFO:START -->
## 企业服务与联系

**华链 AI** · 企业 AI 业务落地与内生能力建设

培训与 FDE 培养 · 场景验证 · 智能体定制 · 企业实施 · 产品应用支持

[华链 AI 官网](https://hualian-ai.pages.dev) · [企业服务](https://hualian-ai.pages.dev/services/) · [服务参考价](https://hualian-ai.pages.dev/pricing/) · [企业宣传册](https://hualian-ai.pages.dev/downloads/company-brochure.pdf) · [合作咨询](https://hualian-ai.pages.dev/contact/)

咨询联系人：**见舟** · 微信：**`DST10209`**

<img src="https://hualian-ai.pages.dev/assets/contact/wechat-qr.png" alt="见舟微信二维码" width="200">

抖音：`74683161410` · 视频号：见舟AI赋能
<!-- JIANZHOU-PUBLIC-INFO:END -->
