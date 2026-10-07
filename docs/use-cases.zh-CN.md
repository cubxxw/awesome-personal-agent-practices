# 用例与玩法

[首页](../README.zh-CN.md) · [English](use-cases.md)

收录 19 条资源，内容读取截至 2026-10-07。

这里聚合公开资源；作者自报、项目说明和研究结果各自保留背景，本库未复跑所有产品。

[家庭与日常流程](#family-workflows) · [失败经验与使用限制](#cautions) · [邮件与日历](#email-calendar) · [旅行与购物](#travel-shopping) · [研究与学习](#research-learning)

<a id="family-workflows"></a>
## 家庭与日常流程

<a id="use-cases-uc01"></a>
- **[用WhatsApp更新舞蹈学校网站](https://www.reddit.com/r/openclaw/comments/1ta7294/what_are_you_actually_using_openclaw_for_that/)** — 作者自报把小型舞校网站连到WhatsApp和GitHub，母亲可通过聊天更新。初始化权限与可靠回滚仍需技术熟手帮忙。
  <sub>作者自报</sub>

<a id="use-cases-uc10"></a>
- **[家庭Matrix消息助手Sebastian](https://ataary.com/meet-sebastian-how-i-built-a-self-learning-ai-assistant-on-openclaw/)** — 作者描述供四口之家使用的Matrix助手，处理邮件监测和核来源的新闻简报。正文记录限流、加密会话与升级故障；聊天端加密不等于外部模型不会收到上下文。
  <sub>作者自报</sub>

<a id="use-cases-uc12"></a>
- **[邮件中的家庭预约确认后写入日历](https://www.linkedin.com/pulse/from-setup-errors-working-personal-ai-assistant-my-openclaw-tarala-xwszf)** — Ganesh Tarala描述通过IMAP读预约邮件、ICS查空闲，在确认后用CalDAV建家庭日历事件。依靠本地辅助脚本，未报告持续可靠性和费用。
  <sub>作者自报</sub>

<a id="use-cases-uc13"></a>
- **[Hermes三周Telegram工作流](https://www.reddit.com/r/hermesagent/comments/1tfrilq/genuinely_blown_away/)** — 三周使用者自报通过手机语音与截图开发小企业Telegram机器人，另用脚本轮换可用免费模型。作者承认失败的定时任务，评论也有结果不一致和多轮复核。
  <sub>作者自报</sub>

<a id="use-cases-xiaobu-phone"></a>
- **[小布Next两个月体验与第三方应用限制](https://www.xiaohongshu.com/explore/6a964eec000000002b0257a5)** — 带共创活动标签的提醒与信息归档体验；作者评论承认第三方应用控制有限，适合了解手机助手的期望和现实边界。
  <sub>作者自报</sub>

<a id="use-cases-poke-recipes"></a>
- **[Poke Recipe：打包与分享一个工作流](https://poke.com/docs/creating-recipes)** — 官方教程把首次上下文和所需集成打包成可分享Recipe。需要Kitchen权限，本地接入隧道需持续运行；属于玩法指南，没有本库实跑结果。
  <sub>官方说明</sub>

<a id="cautions"></a>
## 失败经验与使用限制

<a id="use-cases-uc02"></a>
- **[成本暴涨后拆分确定性流程](https://www.reddit.com/r/openclaw/comments/1t2fd8o/spent_850_on_openclaw_in_a_month_350_in_one_day/)** — 多代理操作者自报一个月花费$850，说明如何把确定性步骤移给n8n、缩短上下文并限额。降费幅度没有同负载账单或调用日志佐证。
  <sub>作者自报</sub>

<a id="use-cases-uc07"></a>
- **[Muse十二天后：复核负担上升](https://www.reddit.com/r/MetaAI/comments/1wpdcdd/it_was_great_until_it_wasnt/)** — 旅行顾问自报最初有用，约12天后开始漏填表格、反复忘规则，复核负担增加。购物网站阻拦与账号异常未有日志证明因果。
  <sub>作者自报</sub>

<a id="use-cases-uc08"></a>
- **[规则流程加一次模型判断的对照](https://www.reddit.com/r/automation/comments/1w9duly/what_are_people_actually_using_ai_agents_for_on_a/)** — 周常讨论提供日志摘要、邮件拟稿、网页差异等规则抓取与路由的做法。它们是通用代理的自报替代方案，发送和涉及金钱的步骤仍由人批准。
  <sub>作者自报</sub>

<a id="use-cases-dots-handoffs"></a>
- **[Dots几天体验：权限交接与通话](https://x.com/telegram_man/status/2107498869571633273)** — 作者报告把任务转给其他Agent及通话时遇到的阻碍。朋友的旅行成功是转述，适合思考交接条件，不能用于成功率比较。
  <sub>作者自报</sub>

<a id="email-calendar"></a>
## 邮件与日历

<a id="use-cases-uc03"></a>
- **[Hermes数月使用：六邮箱与复用流程](https://www.reddit.com/r/hermesagent/comments/1w7dtpp/what_i_learned_after_running_hermes_as_my/)** — 用户自报数月用Hermes分拣六个邮箱、积累可复用流程，发送仍由本人控制。记录同时包含过时记忆维护与昂贵模型自动回退的教训。
  <sub>作者自报</sub>

<a id="use-cases-uc04"></a>
- **[Poke一周体验：日程与迟到改约](https://www.producthunt.com/p/poke-by-interaction-co/a-week-with-poke-review-a-promising-start-for-a-proactive-ai-assistant)** — 一周使用记录包含日程简报，以及通过Workers、Shortcuts和webhooks搭出的迟到改约流程。需要配置调试，也有接入问题，未公开可靠性日志。
  <sub>作者自报</sub>

<a id="use-cases-uc05"></a>
- **[Today采访邀约与次日续办](https://www.pingwest.com/a/317164)** — 记者自报确认采访邀约后在邮箱看到已发邮件，次日收到对方回复时Today主动续办。只有一周体验，未交代最终采访落实或长期效果。
  <sub>作者自报</sub>

<a id="use-cases-uc11"></a>
- **[邮件语义检索与资料挖掘](https://moontowermeta.com/unlocking-my-email-with-ai/amp/)** — Kris自报先用14组关键词取候选邮件，再通过Gmail API读正文并让模型分类。缓存、重试和可续跑保存处理限流与失败调用，属于可复用脚本流程。
  <sub>作者自报</sub>

<a id="use-cases-town-routines"></a>
- **[Town Routine：周期邮件与会议任务](https://www.town.com/docs/features/routines)** — 官方示例包含晨报、邮件分拣、会前准备及回复草稿，适合学习只读、需审批与自主运行的设置。属于厂商介绍的流程。
  <sub>官方说明</sub>

<a id="use-cases-today-recording"></a>
- **[Today Recording：会议记录与后续跟进](https://today.ai/articles/blog/introducing-today-recording)** — 厂商介绍如何把会议记录、已有项目上下文和后续任务连接起来。适合探索转录之后怎样推进事情，演示尚未复跑。
  <sub>官方说明</sub>

<a id="travel-shopping"></a>
## 旅行与购物

<a id="use-cases-uc06"></a>
- **[Instinct机票监控与购物测试](https://www.reddit.com/r/AI_Agents/comments/1wak4is/ive_been_stresstesting_instinct_with_reallife/)** — 试用者自报每天约三次机票检查和多项购物任务，也报告步骤慢、部分网站不通与OTP接管。是否允许付款需要单独决定。
  <sub>作者自报</sub>

<a id="use-cases-uc14"></a>
- **[克什米尔行程测试与细节幻觉](https://www.reddit.com/r/travelindia/comments/1jcjr8h/i_have_made_this_travel_planner_ai_agent_i_do_lot/)** — Trip Planner作者介绍搜索加模型的行程流程，Kashmir旅行用户反馈按天概览有用，细节却有幻觉、酒店报价未按日期落实。另有搜索限流错误，没有已验证的预订或旅程结果。
  <sub>作者自报</sub>

<a id="research-learning"></a>
## 研究与学习

<a id="use-cases-uc09"></a>
- **[从Obsidian笔记发起复习提问](https://sajalsharma.com/posts/openclaw-experiments/)** — Sajal Sharma自报每周两次根据Obsidian中的文章和课程记录主动提问，帮助检查记忆与理解。一周记录也交代独立账号、发件人白名单及重复邮件修复，未测学习成绩。
  <sub>作者自报</sub>

<details>
<summary>读取范围与来源记录</summary>

说明正文、摘要和媒体的实际读取范围。未读的图片或视频不作为体验证据。

- **WhatsApp website updates for a dance school** (2026-10-07): 主帖；舞校评论链（网页125–277行）；关键质疑与作者回应；未展开全部回复；Reddit 搜索结果绝对日期；选定评论日期可不同；未读媒体：该帖其他图片/外链项目未核看 [Source1](https://www.reddit.com/r/openclaw/comments/1ta7294/what_are_you_actually_using_openclaw_for_that/)

- **OpenClaw cost spike and deterministic-workflow split** (2026-10-07): 主帖；成本质疑、作者两次澄清、n8n替代讨论（网页21–305行）；Reddit 搜索结果绝对日期；未读媒体：作者提及的费用截图未核看 [Source1](https://www.reddit.com/r/openclaw/comments/1t2fd8o/spent_850_on_openclaw_in_a_month_350_in_one_day/)

- **Months of Hermes: six inboxes and reusable routines** (2026-10-07): 主帖主要全文（网页21–84行）；首个评论中5个月使用者的本地memory维护/高投入提醒（124–127行）；2026-10-07读取时缓存显示28d ago；不据缓存反推准确日；未读媒体：评论所链记忆项目和模型未审源码 [Source1](https://www.reddit.com/r/hermesagent/comments/1w7dtpp/what_i_learned_after_running_hermes_as_my/)

- **One week with Poke: schedules and late-meeting messages** (2026-10-07): 主帖；自定义流程与一周体验段；Daniel MCP接入质疑及作者回复（224–235行）；网页显示1yr ago；公开HTML日期字段均为2025-09，本轮未锁定帖级精确日；未读媒体：入门截图与MCP连接截图未核看 [Source1](https://www.producthunt.com/p/poke-by-interaction-co/a-week-with-poke-review-a-promising-start-for-a-proactive-ai-assistant)

- **Today interview invitation with next-day follow-up** (2026-10-07): 原站公开HTML正文完整提取；工具web首开有目录、后续Internal Error，以免费HTTP正文恢复；未读截图；页面可见0评论；原站9月9日，聚合页交叉确认2026-09-09；未读媒体：产品截图未核看 [Source1](https://www.pingwest.com/a/317164)

- **Instinct flight monitoring and shopping stress test** (2026-10-07): 主帖全文；虚拟卡建议与作者反问（125–134行）；OTP/速度讨论；iMessage读权限误认后自纠（248–300行）；Reddit 搜索结果绝对日期，既有来源卡一致；未读媒体：评论外链视频、Instagram及媒体未逐一核读 [Source1](https://www.reddit.com/r/AI_Agents/comments/1wak4is/ive_been_stresstesting_instinct_with_reallife/)

- **Muse travel-advisor workflow after twelve days** (2026-10-07): Public post and selected discussion read, including repeated-task failures and claimed verification. Exact publication date not independently rechecked; images, videos and linked threads not read. [Source1](https://www.reddit.com/r/MetaAI/comments/1wpdcdd/it_was_great_until_it_wasnt/)

- **When a plain workflow plus one model call is enough** (2026-10-07): 主帖；Total_Drag7439三项实际周用例（128–138行）；规则/模型边界反问；其他每周例子与在建声明；本轮缓存显示23d ago；既有研究2026-09-29已读，不反推准确日；未读媒体：评论所链工具产品未逐一读 [Source1](https://www.reddit.com/r/automation/comments/1w9duly/what_are_people_actually_using_ai_agents_for_on_a/)

- **OpenClaw study recall from an Obsidian vault** (2026-10-07): 2026-02-16；主文全文，重点Studying与技术失败；图片未读，未来看房功能为计划。 [Source1](https://sajalsharma.com/posts/openclaw-experiments/)

- **Sebastian: a family Matrix assistant** (2026-10-07): 2026-04-10；主文全文，含新闻步骤、家人重新验证与失败；图片未读，技能加速倍率未经独立测试。 [Source1](https://ataary.com/meet-sebastian-how-i-built-a-self-learning-ai-assistant-on-openclaw/)

- **Semantic email mining with Gmail API and Claude** (2026-10-07): 公开正文全文；步骤1–3、结果与故障均已读；发布时间页面只显示相对日期，未核绝对日；未查私有邮件或脚本。 [Source1](https://moontowermeta.com/unlocking-my-email-with-ai/amp/)

- **Zoho appointment email to a confirmed family event** (2026-10-07): 2026-05-05；公开LinkedIn作者正文全文与可见感谢评论；截图未读，链接ganesht.de未进一步读取。 [Source1](https://www.linkedin.com/pulse/from-setup-errors-working-personal-ai-assistant-my-openclaw-tarala-xwszf)

- **Three weeks of Hermes through Telegram** (2026-10-07): 2026-05-17；主帖及OP关于脚本、失败cron、个人数据隔离的回复；模型不稳定评论；机器人摘要与操作代码不作独立证据，未读图片。 [Source1](https://www.reddit.com/r/hermesagent/comments/1tfrilq/genuinely_blown_away/)

- **Kashmir itinerary test: overview versus details** (2026-10-07): 主帖与旅行测试、作者回应、500限流评论均已读；页面关联2025-03-16，精确发表时间未核；外链产品未登录或试用。 [Source1](https://www.reddit.com/r/travelindia/comments/1jcjr8h/i_have_made_this_travel_planner_ai_agent_i_do_lot/)

- **Two months with Xiaobu Next: phone workflows and limits** (2026-10-07): TikHub text detail and18 returned comment/reply records read on2026-10-07. Images and video not read; no pagination or product test. [Source1](https://www.xiaohongshu.com/explore/6a964eec000000002b0257a5)

- **Dots after a few days: agent handoffs and calls** (2026-10-07): TikHub returned long-form post text read; image and replies not read. No independent reproduction. [Source1](https://x.com/telegram_man/status/2107498869571633273)

- **Poke Recipes: package and share a workflow** (2026-10-07): Current official guide/article text read; linked demonstrations and live workflow not tested. [Source1](https://poke.com/docs/creating-recipes)

- **Town Routines: recurring email and meeting jobs** (2026-10-07): Current official guide/article text read; linked demonstrations and live workflow not tested. [Source1](https://www.town.com/docs/features/routines)

- **Today Recording: meeting notes and follow-up** (2026-10-07): Current official guide/article text read; linked demonstrations and live workflow not tested. [Source1](https://today.ai/articles/blog/introducing-today-recording)

</details>

[贡献资源](../CONTRIBUTING.md)
