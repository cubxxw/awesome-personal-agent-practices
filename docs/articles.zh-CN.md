# 文章与技术

[首页](../README.zh-CN.md) · [English](articles.md)

收录 13 条资源，内容读取截至 2026-10-07。

这里聚合公开资源；作者自报、项目说明和研究结果各自保留背景，本库未复跑所有产品。

[开发者实践](#practitioner) · [工程解释](#engineering)

<a id="practitioner"></a>
## 开发者实践

<a id="articles-ar01"></a>
- **[OpenPoke：复现Poke架构的分析](https://www.shloked.com/openpoke)** — Shlok Khemani拆解自己的本地原型：交互与执行代理、邮件工具、触发器和分层记忆。基于使用与泄漏提示词的逆向，明确有成本、延迟和功能缺口，并非Poke官方架构。
  <sub>实现记录</sub>

<a id="articles-ar02"></a>
- **[离开Poke后的个人反思](https://www.shloked.com/interaction-acquisition)** — OpenPoke作者解释为何喜欢Poke却一个月后停付费：本人邮件日历需求不多，自动化还得自己找。他对总体留存和出售原因的解释是猜测，文末披露短期承包关系。
  <sub>作者自报</sub>

<a id="articles-ar03"></a>
- **[Tanisha的消息式助手体验](https://tanishasrivatsa.substack.com/p/i-spent-30-minutes-arguing-with-a)** — Poke用户把入门经历与团队采访结合，讨论消息入口、性格与个人上下文。文中有消息停止响应及团队解释，适合读产品取舍，不能当可靠性测评。
  <sub>作者自报</sub>

<a id="articles-ar04"></a>
- **[构建4shClaw的过程](https://4sh.dev/posts/2026/building-4shclaw/)** — Sylvain Cau解释Telegram入口、每代理容器、能力声明、共享账本与有条件的主动提醒。GLORP用于说明交接，但结尾写明项目流水线正准备开始，不能当完整交付战绩。
  <sub>实现记录</sub>

<a id="articles-ar05"></a>
- **[五个OpenClaw工作流](https://www.coreyganim.com/blog/5-openclaw-workflows-that-made-me-say-wait-it-can-do-that-by-itself/)** — 作者列出播客制作、邮件分拣、内容拆解、嘉宾研究和会前准备的触发、工具与人审步骤。省时和比例均为自报，文章兼有服务与资料推广。
  <sub>作者自报</sub>

<a id="articles-ar06"></a>
- **[Personal Agent的产品与采用分析](https://sajalsharma.com/posts/personal-agents-have-gone-mainstream/)** — 长期使用者讨论从问问题到交办事务的变化，包括账号访问和记忆迁移。适合作为产品分析，文中的市场数字与竞争判断未在本清单独立核验。
  <sub>实现记录</sub>

<a id="articles-nicolas-stack"></a>
- **[跨应用处理个人事务：Nicolas的工具栈](https://www.nicolasbustamante.com/blog/how-agents-run-my-personal-life)** — Nicolas通过一封跨应用介绍邮件讲解个人工具栈，保留发信审批，也写出维护连接器和修订技能的劳动。效果属于作者自报。
  <sub>作者自报</sub>

<a id="articles-talal-calendar"></a>
- **[与Agent共同管理日历和精力预算](https://talalakkari.com/blog/managing-time-with-an-agent/)** — Talal介绍多个日历的共同忙闲视图、本人接受邀请以及安静时段，适合学习共享工作面怎样支持日常协作。
  <sub>作者自报</sub>

<a id="articles-tbpn-delegation"></a>
- **[哪些事情用户可能愿意自己做](https://x.com/tbpn/status/2102529303212970099)** — TBPN发布文字记录了Ben Thompson对航班选择和购物体验的看法，可用于思考用户愿不愿委托。未观看访谈视频。
  <sub>作者自报</sub>

<a id="engineering"></a>
## 工程解释

<a id="articles-context-engineering"></a>
- **[怎样管理Agent的上下文](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)** — Anthropic讲解上下文选择、会话压缩与持久笔记，适合理解助手为什么会在长任务中丢失重点。
  <sub>官方说明</sub>

<a id="articles-building-effective-agents"></a>
- **[构建有效Agent的基础模式](https://www.anthropic.com/engineering/building-effective-agents)** — 介绍固定工作流与模型自主决策的设计取舍。适合学习基础模式；原文已提醒2024年的工具环境发生变化。
  <sub>官方说明</sub>

<a id="articles-muse-safety"></a>
- **[Muse的安全设计说明](https://research.meta.ai/blog/security-and-safety-for-ai-agents-our-approach-with-muse)** — Meta介绍Muse的凭据处理、隔离执行和动作审批。属于厂商架构说明，没有经过本库独立安全审计。
  <sub>官方说明</sub>

<a id="articles-manus-context"></a>
- **[Manus的上下文工程经验](https://manus.im/blog/Context-Engineering-for-AI-Agents-Lessons-from-Building-Manus)** — Manus分享工具上下文、缓存利用与外部状态的工程经验，也讨论如何保留失败信息。可供其他实现参考，不能当跨产品评测。
  <sub>官方说明</sub>

<details>
<summary>读取范围与来源记录</summary>

说明正文、摘要和媒体的实际读取范围。未读的图片或视频不作为体验证据。

- **OpenPoke: Recreating Poke’s Architecture** (2026-10-07): 2025-09-22；作者正文全文；截图、视频未读，原型源码未审；泄漏prompt未作为权威产品保证。 [Source1](https://www.shloked.com/openpoke)

- **On the Interaction Acquisition** (2026-10-07): 2026-07-30；短文全文；所链X讨论未读，不据单人经历估总体留存。 [Source1](https://www.shloked.com/interaction-acquisition)

- **Trying (another) AI assistant — Tanisha Srivatsa** (2026-10-07): 2025-09-23；公开正文与编辑后的访谈全文；截图未读；团队解释未独立核事故。 [Source1](https://tanishasrivatsa.substack.com/p/i-spent-30-minutes-arguing-with-a)

- **Building 4shClaw — Sylvain Cau** (2026-10-07): 2026-02-28；作者公开HTML正文全文已读；图的文本结构已读、图片与公开repo提交未核；威胁判断是作者论证。 [Source1](https://4sh.dev/posts/2026/building-4shclaw/)

- **Five OpenClaw workflows — Corey Ganim** (2026-10-07): 2026-02-10；主文全文、五项How it works与制作步骤已读；未看任何YouTube视频或核查产物/工时账单。 [Source1](https://www.coreyganim.com/blog/5-openclaw-workflows-that-made-me-say-wait-it-can-do-that-by-itself/)

- **Personal Agents Have Gone Mainstream — Sajal Sharma** (2026-10-07): 2026-09-30；作者正文全文；内链市场新闻未逐条核读，不采用其市场规模数字。 [Source1](https://sajalsharma.com/posts/personal-agents-have-gone-mainstream/)

- **Effective context engineering for AI agents** (2026-10-07): Public article text; images and linked demonstrations not inspected. [Source1](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)

- **Building effective agents** (2026-10-07): Public article text and its current update notice; examples not reproduced. [Source1](https://www.anthropic.com/engineering/building-effective-agents)

- **How We Built Safety Into Muse** (2026-10-07): Public engineering article text; no product or security test performed. [Source1](https://research.meta.ai/blog/security-and-safety-for-ai-agents-our-approach-with-muse)

- **Context Engineering for AI Agents: Lessons from Building Manus** (2026-10-07): Public article text; no implementation reproduction. [Source1](https://manus.im/blog/Context-Engineering-for-AI-Agents-Lessons-from-Building-Manus)

- **My Agent Stack For Automating My Personal Life** (2026-10-07): Public article text read; screenshots and linked tools not tested. [Source1](https://www.nicolasbustamante.com/blog/how-agents-run-my-personal-life)

- **Managing Time With an Agent** (2026-10-07): Public article text read; diagrams and linked implementation not tested. [Source1](https://talalakkari.com/blog/managing-time-with-an-agent/)

- **Ben Thompson on tasks people may not want to delegate** (2026-10-07): TikHub post text read; video and replies not read. This is platform-published discussion text, not a full interview review. [Source1](https://x.com/tbpn/status/2102529303212970099)

</details>

[贡献资源](../CONTRIBUTING.md)
