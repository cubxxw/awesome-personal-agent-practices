# Use cases & playbooks

[Home](../README.md) · [简体中文](use-cases.zh-CN.md)

19 resources. Content read as of 2026-10-07.

Public resources with their source context preserved. Author reports and project claims are not independent product tests.

[Family & everyday workflows](#family-workflows) · [Failure stories & practical limits](#cautions) · [Email & calendar](#email-calendar) · [Travel & shopping](#travel-shopping) · [Research & learning](#research-learning)

<a id="family-workflows"></a>
## Family & everyday workflows

<a id="use-cases-uc01"></a>
- **[WhatsApp website updates for a dance school](https://www.reddit.com/r/openclaw/comments/1ta7294/what_are_you_actually_using_openclaw_for_that/)** — A developer reports connecting a small dance-school website to WhatsApp through a GitHub repository. Initial permissions and reliable recovery still required technical help.
  <sub>Author report</sub>

<a id="use-cases-uc10"></a>
- **[Sebastian: a family Matrix assistant](https://ataary.com/meet-sebastian-how-i-built-a-self-learning-ai-assistant-on-openclaw/)** — A builder describes a family-of-four assistant with Matrix rooms, email monitoring and source-checked news digests. The post documents rate-limit and encryption-session failures; E2EE does not make data sent to external models local.
  <sub>Author report</sub>

<a id="use-cases-uc12"></a>
- **[Zoho appointment email to a confirmed family event](https://www.linkedin.com/pulse/from-setup-errors-working-personal-ai-assistant-my-openclaw-tarala-xwszf)** — Ganesh Tarala describes reading appointment email over IMAP, checking availability through ICS and creating the event over CalDAV after confirmation. It uses local helper scripts rather than a ready-made Google connector; ongoing reliability and costs are not reported.
  <sub>Author report</sub>

<a id="use-cases-uc13"></a>
- **[Three weeks of Hermes through Telegram](https://www.reddit.com/r/hermesagent/comments/1tfrilq/genuinely_blown_away/)** — A three-week user reports sending voice notes and screenshots from a phone to build a small-business Telegram bot. A script rotates available free models, but the author admits failed cron jobs and commenters report inconsistent results and extra review.
  <sub>Author report</sub>

<a id="use-cases-xiaobu-phone"></a>
- **[Two months with Xiaobu Next: phone workflows and limits](https://www.xiaohongshu.com/explore/6a964eec000000002b0257a5)** — A co-creation-tagged account of reminders and information capture. Author replies acknowledge limited third-party app control; useful for exploring phone-assistant expectations, not an independent long-term test.
  <sub>Author report</sub>

<a id="use-cases-poke-recipes"></a>
- **[Poke Recipes: package and share a workflow](https://poke.com/docs/creating-recipes)** — Official instructions for packaging onboarding context and required integrations into a shareable recipe. Requires Kitchen access; a local integration tunnel must remain running. This is a guide, not a tested user outcome.
  <sub>Official description</sub>

<a id="cautions"></a>
## Failure stories & practical limits

<a id="use-cases-uc02"></a>
- **[OpenClaw cost spike and deterministic-workflow split](https://www.reddit.com/r/openclaw/comments/1t2fd8o/spent_850_on_openclaw_in_a_month_350_in_one_day/)** — A multi-agent operator reports a $850 month and describes moving repeatable work to n8n while shortening context and adding limits. The claimed savings lack comparable bills or workload logs.
  <sub>Author report</sub>

<a id="use-cases-uc07"></a>
- **[Muse travel-advisor workflow after twelve days](https://www.reddit.com/r/MetaAI/comments/1wpdcdd/it_was_great_until_it_wasnt/)** — A travel advisor reports missing spreadsheet details and repeated rule failures after an initially useful start, creating extra review work. Shopping-site blocks and account issues are allegations, without logs proving their cause.
  <sub>Author report</sub>

<a id="use-cases-uc08"></a>
- **[When a plain workflow plus one model call is enough](https://www.reddit.com/r/automation/comments/1w9duly/what_are_people_actually_using_ai_agents_for_on_a/)** — A weekly-use discussion describes log summaries, inbox drafts and page diffs with deterministic fetching and routing. These are reported alternatives to a general agent; sending and money-sensitive actions remain approved by a person.
  <sub>Author report</sub>

<a id="use-cases-dots-handoffs"></a>
- **[Dots after a few days: agent handoffs and calls](https://x.com/telegram_man/status/2107498869571633273)** — The author's report of friction when delegating to other agents and using calls. A friend's travel success is second-hand; useful for thinking about handoffs rather than comparing completion rates.
  <sub>Author report</sub>

<a id="email-calendar"></a>
## Email & calendar

<a id="use-cases-uc03"></a>
- **[Months of Hermes: six inboxes and reusable routines](https://www.reddit.com/r/hermesagent/comments/1w7dtpp/what_i_learned_after_running_hermes_as_my/)** — A user reports triaging six inboxes and maintaining reusable routines over several months, while retaining control of sending. The account also covers outdated memory and costly automatic model fallback.
  <sub>Author report</sub>

<a id="use-cases-uc04"></a>
- **[One week with Poke: schedules and late-meeting messages](https://www.producthunt.com/p/poke-by-interaction-co/a-week-with-poke-review-a-promising-start-for-a-proactive-ai-assistant)** — A one-week account describes daily briefings and a location-triggered rescheduling workflow using Workers, Shortcuts and webhooks. Setup effort and integration problems are part of the recipe, with no published reliability log.
  <sub>Author report</sub>

<a id="use-cases-uc05"></a>
- **[Today interview invitation with next-day follow-up](https://www.pingwest.com/a/317164)** — A journalist reports approving an interview email, checking it in the inbox, and receiving an unsolicited follow-up after the reply the next day. This is a one-week account without a final interview outcome or long-term measurements.
  <sub>Author report</sub>

<a id="use-cases-uc11"></a>
- **[Semantic email mining with Gmail API and Claude](https://moontowermeta.com/unlocking-my-email-with-ai/amp/)** — Kris reports retrieving email candidates with fourteen keyword searches, fetching bodies through Gmail API, then classifying them with a model. The reusable script workflow needed caching, retries and resumable writes after rate limits and failed API calls.
  <sub>Author report</sub>

<a id="use-cases-town-routines"></a>
- **[Town Routines: recurring email and meeting jobs](https://www.town.com/docs/features/routines)** — Official examples include morning briefings, inbox triage, meeting preparation and reply drafts. Explore the read-only, approval-required and autonomous modes; examples are vendor-described workflows.
  <sub>Official description</sub>

<a id="use-cases-today-recording"></a>
- **[Today Recording: meeting notes and follow-up](https://today.ai/articles/blog/introducing-today-recording)** — A vendor explanation of connecting meeting capture, existing project context and follow-up tasks. Useful for exploring the path from a transcript to action; the demonstration was not reproduced.
  <sub>Official description</sub>

<a id="travel-shopping"></a>
## Travel & shopping

<a id="use-cases-uc06"></a>
- **[Instinct flight monitoring and shopping stress test](https://www.reddit.com/r/AI_Agents/comments/1wak4is/ive_been_stresstesting_instinct_with_reallife/)** — A tester reports flight checks roughly three times daily and several shopping tasks, alongside slow steps, inaccessible sites and manual OTP handling. Payment approval remains a separate trust decision.
  <sub>Author report</sub>

<a id="use-cases-uc14"></a>
- **[Kashmir itinerary test: overview versus details](https://www.reddit.com/r/travelindia/comments/1jcjr8h/i_have_made_this_travel_planner_ai_agent_i_do_lot/)** — A Trip Planner builder explains a search-plus-model itinerary workflow, and a Kashmir traveler reports useful day-level ideas but hallucinated details and weak date-specific hotel prices. Other comments report a search rate-limit error; no booking or completed trip is verified.
  <sub>Author report</sub>

<a id="research-learning"></a>
## Research & learning

<a id="use-cases-uc09"></a>
- **[OpenClaw study recall from an Obsidian vault](https://sajalsharma.com/posts/openclaw-experiments/)** — Sajal Sharma reports a twice-weekly cron that quizzes him from the articles and courses logged in Obsidian. His one-week account also explains separate accounts, sender allowlisting and duplicate-email fixes; learning gains are not measured.
  <sub>Author report</sub>

<details>
<summary>Reading scope and source notes</summary>

Scope distinguishes article text, abstracts and media. Unread images or videos are not treated as experience evidence.

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

[Suggest a resource](../CONTRIBUTING.md)
