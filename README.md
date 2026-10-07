# Awesome Personal Agents

[English](README.md) · [简体中文](README.zh-CN.md)

> A curated resource hub for personal AI agents: products, open-source projects, use cases, playbooks, articles and research.

**84 curated resources** · Last curated: 2026-10-07.

The full collection is on this page. Jump to a category below, then open a resource to read its original source.

## Contents

| Category | Find |
|---|---|
| [Products](#products) · 17 | Explore available assistants |
| [Open-source projects](#projects) · 20 | Find runtimes and integration components |
| [Use cases & playbooks](#use-cases) · 19 | Explore user workflows, official guides and practical limits |
| [Articles & engineering](#articles) · 13 | Understand product and engineering choices |
| [Papers & evaluations](#research) · 10 | Find memory, proactivity and evaluation research |
| [Collections & discovery](#collections) · 5 | Discover adjacent collections |

Products retain official context, cases distinguish author reports from official guides, and research records its reading scope. Check the original source for availability and account requirements.

<a id="products"></a>

## Products · 17

<a id="products-messaging"></a>

### Messaging assistants

<a id="products-instinct"></a>

- **[Instinct](https://instinct.com/)** — A personal assistant you can text or call, with phone and computer actions. Explore real-world errands such as appointments, groceries and travel planning. <sub>Official description</sub>

<a id="products-poke"></a>

- **[Poke](https://poke.com/)** — A messaging-first assistant connecting your apps and services. Explore reminders, connected-work routines and interaction through Messages, WhatsApp or Telegram. <sub>Official description</sub>

<a id="products-town"></a>

- **[Town](https://www.town.com/)** — An assistant that learns your working context and acts across email, calendar, documents and connected tools. Explore personalized work routines and reaching a Townie through different channels. <sub>Official description</sub>

<a id="products-computer"></a>

### Computer & browser assistants

<a id="products-today-ai"></a>

- **[Today](https://today.ai/)** — A personal agent combining living memory, recurring work and connected apps. Explore its calendar, mail, research and cross-device workflows. <sub>Official description</sub>

<a id="products-grok-bot"></a>

- **[Grok Bot](https://x.ai/bot)** — Persistent AI teammates with their own computers that can use connected tools and return finished work. Explore personal and team task delegation. <sub>Official description</sub>

<a id="products-manus-cue"></a>

- **[Cue by Manus](https://www.cue.im/)** — A standalone personal-agent app from Manus, with distinct agents, identities and recurring routines. Explore giving different agents clear responsibilities and reviewing work from your phone. <sub>Official description</sub>

<a id="products-manus"></a>

- **[Manus](https://manus.im/)** — A general task agent for research, deliverables and browser/computer work. Explore multi-step projects, connected local files and scheduled or event-triggered automations. <sub>Official description</sub>

<a id="products-claude-cowork"></a>

- **[Claude / Cowork](https://claude.com/product/cowork)** — Delegated knowledge work across files, connected tools and a built-in browser. Explore document, spreadsheet and recurring report workflows; the official page says Cowork is becoming Claude. <sub>Official description</sub>

<a id="products-cue-desktop"></a>

- **[Cue desktop (heycue.io)](https://heycue.io/)** — A Mac and Windows assistant for voice writing, screen-context questions, tasks and meeting notes. Distinct from Manus Cue and the life-admin service at heycue.ai. <sub>Official description</sub>

<a id="products-ecosystem"></a>

### Platform assistants

<a id="products-meta-muse"></a>

- **[Muse by Meta](https://ai.meta.com/muse/)** — Meta’s personal agent with its own cloud computer and browser, accessible through the Muse app or WhatsApp. Explore ongoing goals and connected-app tasks. <sub>Official description</sub>

<a id="products-chatgpt-dots"></a>

- **[Dots in ChatGPT](https://chatgpt.com/features/dots/)** — Always-on agents inside ChatGPT with a cloud computer, connected apps and ongoing responsibilities. Explore persistent delegation and the permissions you choose for your dot. <sub>Official description</sub>

<a id="products-gemini-spark"></a>

- **[Gemini Spark](https://gemini.google/overview/agent/spark/)** — Google’s background personal agent for tasks, skills and schedules across connected Google apps. Explore inbox, document and recurring Workspace workflows. <sub>Official description</sub>

<a id="products-siri-ai"></a>

- **[Siri / Siri AI](https://www.apple.com/apple-intelligence/)** — Apple’s system-integrated assistant for personal context and actions in supported apps. Explore how device context, voice and app actions fit everyday tasks. <sub>Official description</sub>

<a id="products-family-goals"></a>

### Family & personal goals

<a id="products-tomo-mapo"></a>

- **[Tomo by Mapo Labs](https://www.tomo.ai/)** — A text-based personal AI focused on goals and everyday life. Explore accountability, proactive reminders, group chats and calendar/email connections. <sub>Official description</sub>

<a id="products-ollie"></a>

- **[Ollie](https://ollie.ai/)** — A family-oriented assistant for shared calendars, inbox information and household coordination. Explore how a family assistant works through text and group conversations. <sub>Official source, partially read</sub>

<a id="products-heycue-life-admin"></a>

- **[HeyCue](https://heycue.ai/)** — A life-admin service for bills, renewals and local-service quotes, combining agents with human representatives. Explore the household job-and-quote workflow and its approval steps. <sub>Official description</sub>

<a id="products-adjacent"></a>

### Adjacent tools

<a id="products-since-kindly-today-ai"></a>

- **[today ai by Since Kindly](https://oneintent.today/)** — An adjacent daily-intention and reflection tool, rather than evidence of a general action agent. Explore goal-setting and reflective routines without confusing it with Today at today.ai. <sub>Official description</sub>

<a id="projects"></a>

## Open-source projects · 20

<a id="projects-core"></a>

### Personal-agent runtimes

<a id="projects-openclaw"></a>

- **[OpenClaw](https://github.com/openclaw/openclaw)** — Self-hosted personal assistant with messaging channels, tools, memory, and scheduled automations; a useful starting point for everyday assistant workflows. Tool access and channel permissions depend on your deployment configuration. <sub>Project documentation</sub>

<a id="projects-hermes-agent"></a>

- **[Hermes Agent](https://github.com/NousResearch/hermes-agent)** — Nous Research's personal agent combines persistent memory, reusable skills, messaging, and scheduled work across local or remote environments. Scheduled delivery needs an active gateway or a configured managed scheduler. <sub>Project documentation</sub>

<a id="projects-letta-code"></a>

- **[Letta Code](https://github.com/letta-ai/letta-code)** — Stateful agents with Git-backed memory, background dreaming, channels, and local or cloud backends; useful for exploring assistants that carry context between conversations. This is the current source repository; the former Letta V1 API server is archived separately. <sub>Project documentation</sub>

<a id="projects-nanoclaw"></a>

- **[NanoClaw](https://github.com/nanocoai/nanoclaw)** — Container-based assistant with per-agent working files, memory, messaging integrations, and scheduled tasks. The repository moved from qwibitai to nanocoai; network lockdown is optional, so container isolation should not be read as blanket permission protection. <sub>Project documentation</sub>

<a id="projects-openmuse"></a>

- **[OpenMuse](https://github.com/CopilotKit/openmuse)** — CopilotKit's personal-agent application template brings together email, calendar, a persistent browser, visible task progress, and action approvals. It is an alpha for self-hosting and building on, with integrations that require their own configuration. <sub>Project documentation</sub>

<a id="projects-nanobot"></a>

- **[nanobot](https://github.com/HKUDS/nanobot)** — HKUDS's Python personal-agent framework provides a WebUI, chat integrations, tools, memory, and automation in a readable core. A gateway must remain running for scheduled delivery, and source builds may differ from stable packages. <sub>Project documentation</sub>

<a id="projects-zeroclaw"></a>

- **[ZeroClaw](https://github.com/zeroclaw-labs/zeroclaw)** — Rust personal-assistant runtime with pluggable models, messaging channels, tools, and event-triggered routines. Worth exploring for a configurable always-on setup; autonomy and sandbox choices change what it can access. <sub>Project documentation</sub>

<a id="projects-picoclaw"></a>

- **[PicoClaw](https://github.com/sipeed/picoclaw)** — Sipeed's independent Go assistant targets small devices and multiple hardware architectures, with chat channels and tool integrations. Useful for edge-device experiments; the README flags rapid development and changing resource usage. <sub>Project documentation</sub>

<a id="projects-ironclaw"></a>

- **[IronClaw](https://github.com/nearai/ironclaw)** — NEAR AI's personal assistant emphasizes sandboxed tools, credential handling, persistent memory, and background routines. A useful security-oriented design reference; protection still depends on the configured provider, tools, and policies. <sub>Project documentation</sub>

<a id="projects-qwenpaw"></a>

- **[QwenPaw (formerly CoPaw)](https://github.com/agentscope-ai/QwenPaw)** — AgentScope's personal assistant combines editable memory, skills, scheduled tasks, and channels including DingTalk and Lark. The former CoPaw repository now redirects here; integrations and local or cloud models need configuration. <sub>Project documentation</sub>

<a id="projects-rowboat"></a>

- **[Rowboat](https://github.com/rowboatlabs/rowboat)** — Desktop personal assistant that connects a work knowledge graph with email, notes, browser tasks, and background agents. Useful for work-context and team-space ideas; shared spaces and model providers have separate data boundaries to consider. <sub>Project documentation</sub>

<a id="projects-khoj"></a>

- **[Khoj](https://github.com/khoj-ai/khoj)** — Self-hostable personal AI for querying documents and the web, creating custom agents, and delivering recurring research or notifications. A useful entry point for a knowledge-focused assistant; document answers alone do not establish reliable external actions. <sub>Project documentation</sub>

<a id="projects-component"></a>

### Memory, tools & integrations

<a id="projects-mem0"></a>

- **[Mem0](https://github.com/mem0ai/mem0)** — Memory layer for retaining user preferences and context across assistant conversations, with library, self-hosted, and managed options. The README distinguishes managed-platform optimizations from the open-source SDK, so their reported performance should not be treated as identical. <sub>Project documentation</sub>

<a id="projects-hindsight"></a>

- **[Hindsight](https://github.com/vectorize-io/hindsight)** — Agent memory organized around retain, recall, and reflect operations, with separate memory banks and time-aware retrieval. Useful for assistants that revisit experiences; it adds storage and model dependencies, and may be excessive for simple scheduled scripts. <sub>Project documentation</sub>

<a id="projects-graphiti"></a>

- **[Graphiti](https://github.com/getzep/graphiti)** — Temporal knowledge-graph framework for tracking changing facts, relationships, and their source episodes. Useful for personal relationship or project context; you provide the graph database and model setup, while Zep's managed service is a separate product. <sub>Project documentation</sub>

<a id="projects-e2b"></a>

- **[E2B](https://github.com/e2b-dev/E2B)** — Sandbox infrastructure and SDKs for running assistant code, commands, and desktop interactions away from the user's main machine. Hosted execution requires an account, while self-hosting has its own setup; a sandbox does not define the assistant's authorization policy. <sub>Project documentation</sub>

<a id="projects-browser-use"></a>

- **[Browser Use](https://github.com/browser-use/browser-use)** — Open-source browser agent for web tasks such as finding information and filling forms, with local-library and separate hosted options. A practical computer-use starting point; models, browser accounts, and hosted services have their own access and cost requirements. <sub>Project documentation</sub>

<a id="projects-playwright-mcp"></a>

- **[Playwright MCP](https://github.com/microsoft/playwright-mcp)** — Microsoft's MCP interface exposes structured browser interaction through Playwright, useful for assistants that inspect and operate web pages. Its README explicitly states that it is not a security boundary; browser access must be scoped separately. <sub>Project documentation</sub>

<a id="projects-google-workspace-cli"></a>

- **[Google Workspace CLI (gws)](https://github.com/googleworkspace/cli)** — CLI with structured output and agent skills for Gmail, Calendar, Drive, and other Workspace APIs, useful for email and scheduling workflows. Despite the repository organization, the README says it is not an officially supported Google product; OAuth setup is required. <sub>Project documentation</sub>

<a id="projects-agentmail-python"></a>

- **[AgentMail Python SDK](https://github.com/agentmail-to/agentmail-python)** — Official Python client for AgentMail's inbox APIs, useful when an assistant needs its own email inbox and programmatic communication. The SDK is open source, while the email service requires an AgentMail account and API key. <sub>Project documentation</sub>

<a id="use-cases"></a>

## Use cases & playbooks · 19

<a id="use-cases-email-calendar"></a>

### Email & calendar

<a id="use-cases-uc03"></a>

- **[Months of Hermes: six inboxes and reusable routines](https://www.reddit.com/r/hermesagent/comments/1w7dtpp/what_i_learned_after_running_hermes_as_my/)** — A user reports triaging six inboxes and maintaining reusable routines over several months, while retaining control of sending. The account also covers outdated memory and costly automatic model fallback. <sub>Author report</sub>

<a id="use-cases-uc04"></a>

- **[One week with Poke: schedules and late-meeting messages](https://www.producthunt.com/p/poke-by-interaction-co/a-week-with-poke-review-a-promising-start-for-a-proactive-ai-assistant)** — A one-week account describes daily briefings and a location-triggered rescheduling workflow using Workers, Shortcuts and webhooks. Setup effort and integration problems are part of the recipe, with no published reliability log. <sub>Author report</sub>

<a id="use-cases-uc05"></a>

- **[Today interview invitation with next-day follow-up](https://www.pingwest.com/a/317164)** — A journalist reports approving an interview email, checking it in the inbox, and receiving an unsolicited follow-up after the reply the next day. This is a one-week account without a final interview outcome or long-term measurements. <sub>Author report</sub>

<a id="use-cases-uc11"></a>

- **[Semantic email mining with Gmail API and Claude](https://moontowermeta.com/unlocking-my-email-with-ai/amp/)** — Kris reports retrieving email candidates with fourteen keyword searches, fetching bodies through Gmail API, then classifying them with a model. The reusable script workflow needed caching, retries and resumable writes after rate limits and failed API calls. <sub>Author report</sub>

<a id="use-cases-town-routines"></a>

- **[Town Routines: recurring email and meeting jobs](https://www.town.com/docs/features/routines)** — Official examples include morning briefings, inbox triage, meeting preparation and reply drafts. Explore the read-only, approval-required and autonomous modes; examples are vendor-described workflows. <sub>Official description</sub>

<a id="use-cases-today-recording"></a>

- **[Today Recording: meeting notes and follow-up](https://today.ai/articles/blog/introducing-today-recording)** — A vendor explanation of connecting meeting capture, existing project context and follow-up tasks. Useful for exploring the path from a transcript to action; the demonstration was not reproduced. <sub>Official description</sub>

<a id="use-cases-research-learning"></a>

### Research & learning

<a id="use-cases-uc09"></a>

- **[OpenClaw study recall from an Obsidian vault](https://sajalsharma.com/posts/openclaw-experiments/)** — Sajal Sharma reports a twice-weekly cron that quizzes him from the articles and courses logged in Obsidian. His one-week account also explains separate accounts, sender allowlisting and duplicate-email fixes; learning gains are not measured. <sub>Author report</sub>

<a id="use-cases-travel-shopping"></a>

### Travel & shopping

<a id="use-cases-uc06"></a>

- **[Instinct flight monitoring and shopping stress test](https://www.reddit.com/r/AI_Agents/comments/1wak4is/ive_been_stresstesting_instinct_with_reallife/)** — A tester reports flight checks roughly three times daily and several shopping tasks, alongside slow steps, inaccessible sites and manual OTP handling. Payment approval remains a separate trust decision. <sub>Author report</sub>

<a id="use-cases-uc14"></a>

- **[Kashmir itinerary test: overview versus details](https://www.reddit.com/r/travelindia/comments/1jcjr8h/i_have_made_this_travel_planner_ai_agent_i_do_lot/)** — A Trip Planner builder explains a search-plus-model itinerary workflow, and a Kashmir traveler reports useful day-level ideas but hallucinated details and weak date-specific hotel prices. Other comments report a search rate-limit error; no booking or completed trip is verified. <sub>Author report</sub>

<a id="use-cases-family-workflows"></a>

### Family & everyday workflows

<a id="use-cases-uc01"></a>

- **[WhatsApp website updates for a dance school](https://www.reddit.com/r/openclaw/comments/1ta7294/what_are_you_actually_using_openclaw_for_that/)** — A developer reports connecting a small dance-school website to WhatsApp through a GitHub repository. Initial permissions and reliable recovery still required technical help. <sub>Author report</sub>

<a id="use-cases-uc10"></a>

- **[Sebastian: a family Matrix assistant](https://ataary.com/meet-sebastian-how-i-built-a-self-learning-ai-assistant-on-openclaw/)** — A builder describes a family-of-four assistant with Matrix rooms, email monitoring and source-checked news digests. The post documents rate-limit and encryption-session failures; E2EE does not make data sent to external models local. <sub>Author report</sub>

<a id="use-cases-uc12"></a>

- **[Zoho appointment email to a confirmed family event](https://www.linkedin.com/pulse/from-setup-errors-working-personal-ai-assistant-my-openclaw-tarala-xwszf)** — Ganesh Tarala describes reading appointment email over IMAP, checking availability through ICS and creating the event over CalDAV after confirmation. It uses local helper scripts rather than a ready-made Google connector; ongoing reliability and costs are not reported. <sub>Author report</sub>

<a id="use-cases-uc13"></a>

- **[Three weeks of Hermes through Telegram](https://www.reddit.com/r/hermesagent/comments/1tfrilq/genuinely_blown_away/)** — A three-week user reports sending voice notes and screenshots from a phone to build a small-business Telegram bot. A script rotates available free models, but the author admits failed cron jobs and commenters report inconsistent results and extra review. <sub>Author report</sub>

<a id="use-cases-xiaobu-phone"></a>

- **[Two months with Xiaobu Next: phone workflows and limits](https://www.xiaohongshu.com/explore/6a964eec000000002b0257a5)** — A co-creation-tagged account of reminders and information capture. Author replies acknowledge limited third-party app control; useful for exploring phone-assistant expectations, not an independent long-term test. <sub>Author report</sub>

<a id="use-cases-poke-recipes"></a>

- **[Poke Recipes: package and share a workflow](https://poke.com/docs/creating-recipes)** — Official instructions for packaging onboarding context and required integrations into a shareable recipe. Requires Kitchen access; a local integration tunnel must remain running. This is a guide, not a tested user outcome. <sub>Official description</sub>

<a id="use-cases-cautions"></a>

### Failure stories & practical limits

<a id="use-cases-uc02"></a>

- **[OpenClaw cost spike and deterministic-workflow split](https://www.reddit.com/r/openclaw/comments/1t2fd8o/spent_850_on_openclaw_in_a_month_350_in_one_day/)** — A multi-agent operator reports a $850 month and describes moving repeatable work to n8n while shortening context and adding limits. The claimed savings lack comparable bills or workload logs. <sub>Author report</sub>

<a id="use-cases-uc07"></a>

- **[Muse travel-advisor workflow after twelve days](https://www.reddit.com/r/MetaAI/comments/1wpdcdd/it_was_great_until_it_wasnt/)** — A travel advisor reports missing spreadsheet details and repeated rule failures after an initially useful start, creating extra review work. Shopping-site blocks and account issues are allegations, without logs proving their cause. <sub>Author report</sub>

<a id="use-cases-uc08"></a>

- **[When a plain workflow plus one model call is enough](https://www.reddit.com/r/automation/comments/1w9duly/what_are_people_actually_using_ai_agents_for_on_a/)** — A weekly-use discussion describes log summaries, inbox drafts and page diffs with deterministic fetching and routing. These are reported alternatives to a general agent; sending and money-sensitive actions remain approved by a person. <sub>Author report</sub>

<a id="use-cases-dots-handoffs"></a>

- **[Dots after a few days: agent handoffs and calls](https://x.com/telegram_man/status/2107498869571633273)** — The author's report of friction when delegating to other agents and using calls. A friend's travel success is second-hand; useful for thinking about handoffs rather than comparing completion rates. <sub>Author report</sub>

<a id="articles"></a>

## Articles & engineering · 13

<a id="articles-practitioner"></a>

### Practitioner accounts

<a id="articles-ar01"></a>

- **[OpenPoke: Recreating Poke’s Architecture](https://www.shloked.com/openpoke)** — Shlok Khemani walks through his local prototype: interaction and execution agents, email tools, triggers and layered memory. It is a reverse engineering account based on usage and leaked prompts, with explicit cost, latency and feature gaps; it is not Poke’s official architecture. <sub>Implementation account</sub>

<a id="articles-ar02"></a>

- **[On the Interaction Acquisition](https://www.shloked.com/interaction-acquisition)** — The OpenPoke author explains why he stopped paying for Poke after a month despite liking it: too little email/calendar work and effort needed to invent automations. His broader retention and acquisition explanations are speculation, and he discloses a brief contractor relationship. <sub>Author report</sub>

<a id="articles-ar03"></a>

- **[Trying (another) AI assistant — Tanisha Srivatsa](https://tanishasrivatsa.substack.com/p/i-spent-30-minutes-arguing-with-a)** — A Poke user combines onboarding experience with an edited interview about messaging, personality and context. The text includes a messaging outage and the team’s explanation; it is useful product commentary, not a measured reliability study. <sub>Author report</sub>

<a id="articles-ar04"></a>

- **[Building 4shClaw — Sylvain Cau](https://4sh.dev/posts/2026/building-4shclaw/)** — Sylvain Cau explains a Telegram system with per-agent containers, capabilities, shared ledgers and gated proactive check-ins. The proposed GLORP project illustrates the handoffs, but the closing section says its implementation pipeline is only ready to begin. <sub>Implementation account</sub>

<a id="articles-ar05"></a>

- **[Five OpenClaw workflows — Corey Ganim](https://www.coreyganim.com/blog/5-openclaw-workflows-that-made-me-say-wait-it-can-do-that-by-itself/)** — An operator lists triggers, integrations and review steps for podcast production, inbox triage, repurposing, guest research and meeting preparation. Time-saving and percentage claims are author-reported, and the post also promotes services and a lead magnet. <sub>Author report</sub>

<a id="articles-ar06"></a>

- **[Personal Agents Have Gone Mainstream — Sajal Sharma](https://sajalsharma.com/posts/personal-agents-have-gone-mainstream/)** — A long-term tinkerer discusses the shift from asking questions to delegating errands, including account access and memory portability. Read it as product analysis; market figures and competitive claims are not independently checked by this collection. <sub>Implementation account</sub>

<a id="articles-nicolas-stack"></a>

- **[My Agent Stack For Automating My Personal Life](https://www.nicolasbustamante.com/blog/how-agents-run-my-personal-life)** — Nicolas describes a cross-app introduction email and his personal tools, files and reusable skills. Includes approval before important messages and the ongoing work of repairing connectors and instructions. <sub>Author report</sub>

<a id="articles-talal-calendar"></a>

- **[Managing Time With an Agent](https://talalakkari.com/blog/managing-time-with-an-agent/)** — Talal's account of a shared busy/free calendar, human-accepted invitations and quiet hours. A useful design story about coordinating across calendars without handing over every decision. <sub>Author report</sub>

<a id="articles-tbpn-delegation"></a>

- **[Ben Thompson on tasks people may not want to delegate](https://x.com/tbpn/status/2102529303212970099)** — TBPN's published text of Ben Thompson's argument about choosing flights and enjoying shopping. A demand-side counterpoint to automating everything; the interview video was not watched. <sub>Author report</sub>

<a id="articles-engineering"></a>

### Engineering explanations

<a id="articles-context-engineering"></a>

- **[Effective context engineering for AI agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)** — Anthropic's guide to selecting context, compacting conversations and keeping persistent notes. Useful for understanding why an assistant loses track during long tasks. <sub>Official description</sub>

<a id="articles-building-effective-agents"></a>

- **[Building effective agents](https://www.anthropic.com/engineering/building-effective-agents)** — A foundation for choosing fixed workflows or model-directed agents. Read for the design patterns; the original 2024 article flags that its tooling has since changed. <sub>Official description</sub>

<a id="articles-muse-safety"></a>

- **[How We Built Safety Into Muse](https://research.meta.ai/blog/security-and-safety-for-ai-agents-our-approach-with-muse)** — Meta's explanation of Muse's credential handling, isolated execution and action approval. A vendor architecture account, not an independent security audit. <sub>Official description</sub>

<a id="articles-manus-context"></a>

- **[Context Engineering for AI Agents: Lessons from Building Manus](https://manus.im/blog/Context-Engineering-for-AI-Agents-Lessons-from-Building-Manus)** — Manus's engineering account of tool context, cache reuse, external state and learning from failed actions. Useful beyond its own product; reported lessons are not a comparative benchmark. <sub>Official description</sub>

<a id="research"></a>

## Papers & evaluations · 10

<a id="research-memory"></a>

### Memory & personalization

<a id="research-memora"></a>

- **[Memora: From Recall to Forgetting](https://arxiv.org/html/2604.20006v1)** — Evaluates remembering, reasoning and recommendations as user information changes. Its forgetting-aware metric makes obsolete memories visible; conversation streams are simulated. <sub>Research reading</sub>

<a id="research-pasb"></a>

- **[PASB: Agents Don’t Just Agree, They Remember](https://arxiv.org/html/2607.10526v1)** — Examines how user claims can persist in an agent's memory and affect later sessions. A useful prompt for memory-write governance; controlled episodes are not a life-task reliability test. <sub>Research reading</sub>

<a id="research-longmint"></a>

- **[LongMINT](https://arxiv.org/html/2605.18565v1)** — Tests current facts, history and ordering in evolving information. Helps separate remembering an old fact from using the right fact now; this is offline question answering. <sub>Research reading</sub>

<a id="research-personalized-rag"></a>

- **[Awesome Personalized RAG Agent / survey](https://github.com/Applied-Machine-Learning-Lab/Awesome-Personalized-RAG-Agent)** — A research map linking personalized retrieval, agent methods, datasets and evaluation. Useful for finding papers; individual techniques require reading their original work. <sub>Resource collection</sub>

<a id="research-proactivity"></a>

### Proactivity & continuity

<a id="research-vitabench2"></a>

- **[VitaBench 2.0](https://arxiv.org/html/2605.27141v1)** — Studies evolving preferences and proactive information gathering across ordered user tasks, with comparable memory interfaces. Uses constructed histories rather than months of real account use. <sub>Research reading</sub>

<a id="research-pi-bench"></a>

- **[π-Bench](https://arxiv.org/html/2605.14678v3)** — Proactive personal-assistant tasks with hidden intent, dependencies and cross-session continuity. Simulated users and one shared agent scaffold limit generalization to deployed products. <sub>Research reading</sub>

<a id="research-vibelife"></a>

- **[VibeLifeBench](https://arxiv.org/abs/2608.10875v2)** — A paper on multi-week life-assistant scenarios in a changing simulated world, including timing and implicit constraints. This entry is based on the abstract, not full-method review. <sub>Research reading</sub>

<a id="research-evaluation"></a>

### Evaluation methods

<a id="research-recuris"></a>

- **[Recuris](https://arxiv.org/html/2608.24876v1)** — Connects verified task state, structured failure traces and targeted skill repair. Benchmark improvements do not establish unattended real-life reliability. <sub>Research reading</sub>

<a id="research-personal-agent-bench"></a>

- **[Personal Agent Bench](https://personalagentbench.com/)** — Runtime teardowns alongside state-based simulated task tests. The Zentor team discloses its own agent-business interest; some aggregate results lack complete public run records. <sub>Research reading</sub>

<a id="research-micro1-personalagentbench"></a>

- **[micro1 PersonalAgentBench launch](https://www.linkedin.com/posts/aliansarinik_which-personal-agent-is-the-best-life-assistant-activity-7513263537247457282-D1-5)** — Founder announcement of everyday-task and trust testing across four personal agents, inviting user contributions. Launch text only; linked results and scores were not verified. <sub>Official description</sub>

<a id="collections"></a>

## Collections & discovery · 5

<a id="collections-collection"></a>

### Curated collections

<a id="collections-awesome-personal-agents-selection"></a>

- **[Awesome Personal Agents — selection guide](https://github.com/upgundecha/awesome-personal-agents)** — A product discovery list with a detailed selection guide for task fit, deployment, memory, permissions and cost. <sub>Resource collection</sub>

<a id="collections-awesome-personal-agents-components"></a>

- **[Awesome Personal Agents — components](https://github.com/ahmadyan/awesome-personal-agents)** — A neighboring map of personal agents, memory layers, runtimes, sandboxes and messaging bridges. <sub>Resource collection</sub>

<a id="collections-awesome-personal-ai-assistants"></a>

- **[Awesome Personal AI Assistants](https://github.com/elyase/awesome-personal-ai-assistants)** — A self-hosted assistant catalogue with lightweight, security-focused and deployment-oriented sections. <sub>Resource collection</sub>

<a id="collections-awesome-openclaw-usecases"></a>

- **[Awesome OpenClaw Use Cases](https://github.com/hesamsheikh/awesome-openclaw-usecases)** — A community use-case library for OpenClaw; contribution rules require personally tested workflows. <sub>Resource collection</sub>

<a id="collections-awesome-openclaw-examples"></a>

- **[Awesome OpenClaw Examples](https://github.com/OthmaneBlial/awesome-openclaw-examples)** — Inspectable workflow starter packs with prompts, sample outputs and setup notes. Samples are not automatically evidence of production runs. <sub>Resource collection</sub>

<a id="reading-notes"></a>

## Reading and source notes

<details>
<summary>Reading scope and original sources</summary>

Text, abstract and media coverage follows the actual reading scope.

### Products

- **Today** (2026-10-07): Official download page lists Mac, Windows, Linux and mobile entry points; specific country eligibility not verified. Distinct from the Since Kindly app at oneintent.today. [Source 1](https://today.ai/) · [Source 2](https://today.ai/downloads) · [Source 3](https://today.ai/privacy)

- **Instinct** (2026-10-07): Text/call entry documented; current country, pricing and invitation eligibility not established on the inspected homepage. [Source 1](https://instinct.com/)

- **Poke** (2026-10-07): Messaging channels explicitly named on homepage; individual channel/account/region availability not independently tested. [Source 1](https://poke.com/)

- **Muse by Meta** (2026-10-07): Official launch page states US rollout on iOS, Android and muse.ai; current expansion outside the US not verified. [Source 1](https://ai.meta.com/muse/) · [Source 2](https://about.fb.com/news/2026/09/introducing-muse-personal-ai-agent/) · [Source 3](https://about.fb.com/news/2026/09/introducing-muse-small-business/)

- **Town** (2026-10-07): Official documentation covers connected services and work tasks; country eligibility not verified. [Source 1](https://www.town.com/) · [Source 2](https://www.town.com/docs/getting-started)

- **Tomo by Mapo Labs** (2026-10-07): Official About page names Mapo Labs; do not confuse with unrelated open-source tamnd/tomo. Region eligibility not verified. [Source 1](https://www.tomo.ai/) · [Source 2](https://www.tomo.ai/about)

- **Ollie** (2026-10-07): Official indexed homepage describes iOS/Android text access; country eligibility unknown. Full-page retrieval failed in this run. [Source 1](https://ollie.ai/) · [Source 2](https://www.ollie.ai/about/)

- **Dots in ChatGPT** (2026-10-07): Official Help Center describes initial Pro rollout excluding EEA/Switzerland/UK, Business Premium across supported ChatGPT regions, and admin-enabled Enterprise beta; eligibility varies. [Source 1](https://chatgpt.com/features/dots/) · [Source 2](https://help.openai.com/en/articles/20001530-getting-started-with-your-dot) · [Source 3](https://openai.com/index/introducing-dots/)

- **Grok Bot** (2026-10-07): Official page documents desktop/iOS interaction and persistent computer workspace; country eligibility not verified. [Source 1](https://x.ai/bot) · [Source 2](https://x.ai/bot/guides/grok-bot-101)

- **Cue by Manus** (2026-10-07): Official Manus help page says invitation code required, obtained through Agents (Cue!) in the Manus sidebar; mobile and desktop described. Distinct from heycue.ai and the desktop Cue at heycue.io. [Source 1](https://www.cue.im/) · [Source 2](https://help.manus.im/en/articles/17190150-what-is-new-in-manus-2-0)

- **HeyCue** (2026-10-07): Homepage states web/iOS/Android and English/Spanish. Human involvement explicitly disclosed. Country/service-area eligibility not established. [Source 1](https://heycue.ai/)

- **Gemini Spark** (2026-10-07): Official page says Google AI Pro/Ultra users over 18 in selected countries and selected business users; availability link provided rather than a complete region list. [Source 1](https://gemini.google/overview/agent/spark/) · [Source 2](https://support.google.com/gemini/answer/17094507)

- **Siri / Siri AI** (2026-10-07): Current official landing page says Siri AI rolling out in English; features depend on compatible devices, OS, language and region. Do not treat it as documented always-on background delegation. [Source 1](https://www.apple.com/apple-intelligence/) · [Source 2](https://www.apple.com/newsroom/2026/06/apple-introduces-siri-ai-a-profoundly-more-capable-and-personal-assistant/)

- **Manus** (2026-10-07): Official Manus 2.0 documentation inspected; distinct from its standalone personal-agent app Cue. Region eligibility not verified. [Source 1](https://manus.im/) · [Source 2](https://www.manus.im/) · [Source 3](https://help.manus.im/en/articles/17190150-what-is-new-in-manus-2-0)

- **Claude / Cowork** (2026-10-07): Paid-plan access and web/mobile rollout conditions documented; exact account eligibility varies. [Source 1](https://claude.com/product/cowork)

- **today ai by Since Kindly** (2026-10-07): Official terms identify Since Kindly Inc. and describe daily intention/reflection; iOS app named. Country eligibility not verified. [Source 1](https://oneintent.today/) · [Source 2](https://oneintent.today/terms.html) · [Source 3](https://apps.apple.com/us/app/today-ai-personal-agent/id6767525653)

- **Cue desktop (heycue.io)** (2026-10-07): Current official homepage text read; listed examples and demo video not treated as reproduced tasks. [Source 1](https://heycue.io/)

### Open-source projects

- **OpenClaw** (2026-10-07): Self-hosted assistant and automation runtime [Source 1](https://github.com/openclaw/openclaw) · [Source 2](https://github.com/openclaw/openclaw/blob/0dc20916873149b6f6803d1eae711c8d44f3de9e/README.md) · [Source 3](https://github.com/openclaw/openclaw/blob/0dc20916873149b6f6803d1eae711c8d44f3de9e/docs/automation/index.md)

- **Hermes Agent** (2026-10-07): Personal agent, skills, memory, and scheduled work [Source 1](https://github.com/NousResearch/hermes-agent) · [Source 2](https://github.com/NousResearch/hermes-agent/blob/a50406d9b7474b060450d2dcaff8743c977d296a/README.md) · [Source 3](https://github.com/NousResearch/hermes-agent/blob/a50406d9b7474b060450d2dcaff8743c977d296a/website/docs/user-guide/features/cron.md)

- **Letta Code** (2026-10-07): Stateful personal agents and editable memory [Source 1](https://github.com/letta-ai/letta-code) · [Source 2](https://github.com/letta-ai/letta-code/blob/4b028fab07c69edaac2ddb4f7b9a43573ff20d81/README.md) · [Source 3](https://github.com/letta-ai/letta/blob/5bcdd177d70fa2b31a754cfcd801e77b2e1ab16a/README.md)

- **NanoClaw** (2026-10-07): Container-based personal assistant [Source 1](https://github.com/nanocoai/nanoclaw) · [Source 2](https://github.com/nanocoai/nanoclaw/blob/66f0823a693bd9cca4123e72f8ccee05f5e7e1c5/README.md) · [Source 3](https://github.com/nanocoai/nanoclaw/blob/66f0823a693bd9cca4123e72f8ccee05f5e7e1c5/docs/SECURITY.md)

- **OpenMuse** (2026-10-07): Personal-agent application template [Source 1](https://github.com/CopilotKit/openmuse) · [Source 2](https://github.com/CopilotKit/openmuse/blob/1ac68f3909f2478ab6280883f1ab5ea65eb5719d/README.md) · [Source 3](https://github.com/CopilotKit/openmuse/blob/1ac68f3909f2478ab6280883f1ab5ea65eb5719d/apps/server/src/actions.ts)

- **nanobot** (2026-10-07): Lightweight Python personal-agent runtime [Source 1](https://github.com/HKUDS/nanobot) · [Source 2](https://github.com/HKUDS/nanobot/blob/main/README.md) · [Source 3](https://github.com/HKUDS/nanobot/blob/main/docs/automations.md)

- **ZeroClaw** (2026-10-07): Rust personal-assistant runtime [Source 1](https://github.com/zeroclaw-labs/zeroclaw) · [Source 2](https://github.com/zeroclaw-labs/zeroclaw/blob/master/README.md)

- **PicoClaw** (2026-10-07): Personal assistant for small and edge devices [Source 1](https://github.com/sipeed/picoclaw) · [Source 2](https://github.com/sipeed/picoclaw/blob/main/README.md)

- **IronClaw** (2026-10-07): Personal assistant with sandboxed tool execution [Source 1](https://github.com/nearai/ironclaw) · [Source 2](https://github.com/nearai/ironclaw/blob/main/README.md)

- **QwenPaw (formerly CoPaw)** (2026-10-07): Personal assistant with Chinese workplace channels [Source 1](https://github.com/agentscope-ai/QwenPaw) · [Source 2](https://github.com/agentscope-ai/QwenPaw/blob/main/README.md) · [Source 3](https://github.com/agentscope-ai/CoPaw)

- **Rowboat** (2026-10-07): Desktop work assistant and shared spaces [Source 1](https://github.com/rowboatlabs/rowboat) · [Source 2](https://github.com/rowboatlabs/rowboat/blob/main/README.md)

- **Khoj** (2026-10-07): Knowledge-focused personal AI and research automation [Source 1](https://github.com/khoj-ai/khoj) · [Source 2](https://github.com/khoj-ai/khoj/blob/master/README.md)

- **Mem0** (2026-10-07): Assistant memory component [Source 1](https://github.com/mem0ai/mem0) · [Source 2](https://github.com/mem0ai/mem0/blob/main/README.md)

- **Hindsight** (2026-10-07): Persistent assistant memory and reflection [Source 1](https://github.com/vectorize-io/hindsight) · [Source 2](https://github.com/vectorize-io/hindsight/blob/main/README.md)

- **Graphiti** (2026-10-07): Temporal context and relationship memory [Source 1](https://github.com/getzep/graphiti) · [Source 2](https://github.com/getzep/graphiti/blob/main/README.md)

- **E2B** (2026-10-07): Agent execution sandbox and cloud desktop [Source 1](https://github.com/e2b-dev/E2B) · [Source 2](https://github.com/e2b-dev/E2B/blob/main/README.md)

- **Browser Use** (2026-10-07): Browser tasks and web automation [Source 1](https://github.com/browser-use/browser-use) · [Source 2](https://github.com/browser-use/browser-use/blob/main/README.md)

- **Playwright MCP** (2026-10-07): Structured browser tools for assistants [Source 1](https://github.com/microsoft/playwright-mcp) · [Source 2](https://github.com/microsoft/playwright-mcp/blob/main/README.md)

- **Google Workspace CLI (gws)** (2026-10-07): Email, calendar, and Workspace tools [Source 1](https://github.com/googleworkspace/cli) · [Source 2](https://github.com/googleworkspace/cli/blob/main/README.md)

- **AgentMail Python SDK** (2026-10-07): Agent-owned email inbox client [Source 1](https://github.com/agentmail-to/agentmail-python) · [Source 2](https://github.com/agentmail-to/agentmail-python/blob/main/README.md)

### Use cases & playbooks

- **WhatsApp website updates for a dance school** (2026-10-07): 主帖；舞校评论链（网页125–277行）；关键质疑与作者回应；未展开全部回复；Reddit 搜索结果绝对日期；选定评论日期可不同；未读媒体：该帖其他图片/外链项目未核看 [Source 1](https://www.reddit.com/r/openclaw/comments/1ta7294/what_are_you_actually_using_openclaw_for_that/)

- **OpenClaw cost spike and deterministic-workflow split** (2026-10-07): 主帖；成本质疑、作者两次澄清、n8n替代讨论（网页21–305行）；Reddit 搜索结果绝对日期；未读媒体：作者提及的费用截图未核看 [Source 1](https://www.reddit.com/r/openclaw/comments/1t2fd8o/spent_850_on_openclaw_in_a_month_350_in_one_day/)

- **Months of Hermes: six inboxes and reusable routines** (2026-10-07): 主帖主要全文（网页21–84行）；首个评论中5个月使用者的本地memory维护/高投入提醒（124–127行）；2026-10-07读取时缓存显示28d ago；不据缓存反推准确日；未读媒体：评论所链记忆项目和模型未审源码 [Source 1](https://www.reddit.com/r/hermesagent/comments/1w7dtpp/what_i_learned_after_running_hermes_as_my/)

- **One week with Poke: schedules and late-meeting messages** (2026-10-07): 主帖；自定义流程与一周体验段；Daniel MCP接入质疑及作者回复（224–235行）；网页显示1yr ago；公开HTML日期字段均为2025-09，本轮未锁定帖级精确日；未读媒体：入门截图与MCP连接截图未核看 [Source 1](https://www.producthunt.com/p/poke-by-interaction-co/a-week-with-poke-review-a-promising-start-for-a-proactive-ai-assistant)

- **Today interview invitation with next-day follow-up** (2026-10-07): 原站公开HTML正文完整提取；工具web首开有目录、后续Internal Error，以免费HTTP正文恢复；未读截图；页面可见0评论；原站9月9日，聚合页交叉确认2026-09-09；未读媒体：产品截图未核看 [Source 1](https://www.pingwest.com/a/317164)

- **Instinct flight monitoring and shopping stress test** (2026-10-07): 主帖全文；虚拟卡建议与作者反问（125–134行）；OTP/速度讨论；iMessage读权限误认后自纠（248–300行）；Reddit 搜索结果绝对日期，既有来源卡一致；未读媒体：评论外链视频、Instagram及媒体未逐一核读 [Source 1](https://www.reddit.com/r/AI_Agents/comments/1wak4is/ive_been_stresstesting_instinct_with_reallife/)

- **Muse travel-advisor workflow after twelve days** (2026-10-07): Public post and selected discussion read, including repeated-task failures and claimed verification. Exact publication date not independently rechecked; images, videos and linked threads not read. [Source 1](https://www.reddit.com/r/MetaAI/comments/1wpdcdd/it_was_great_until_it_wasnt/)

- **When a plain workflow plus one model call is enough** (2026-10-07): 主帖；Total_Drag7439三项实际周用例（128–138行）；规则/模型边界反问；其他每周例子与在建声明；本轮缓存显示23d ago；既有研究2026-09-29已读，不反推准确日；未读媒体：评论所链工具产品未逐一读 [Source 1](https://www.reddit.com/r/automation/comments/1w9duly/what_are_people_actually_using_ai_agents_for_on_a/)

- **OpenClaw study recall from an Obsidian vault** (2026-10-07): 2026-02-16；主文全文，重点Studying与技术失败；图片未读，未来看房功能为计划。 [Source 1](https://sajalsharma.com/posts/openclaw-experiments/)

- **Sebastian: a family Matrix assistant** (2026-10-07): 2026-04-10；主文全文，含新闻步骤、家人重新验证与失败；图片未读，技能加速倍率未经独立测试。 [Source 1](https://ataary.com/meet-sebastian-how-i-built-a-self-learning-ai-assistant-on-openclaw/)

- **Semantic email mining with Gmail API and Claude** (2026-10-07): 公开正文全文；步骤1–3、结果与故障均已读；发布时间页面只显示相对日期，未核绝对日；未查私有邮件或脚本。 [Source 1](https://moontowermeta.com/unlocking-my-email-with-ai/amp/)

- **Zoho appointment email to a confirmed family event** (2026-10-07): 2026-05-05；公开LinkedIn作者正文全文与可见感谢评论；截图未读，链接ganesht.de未进一步读取。 [Source 1](https://www.linkedin.com/pulse/from-setup-errors-working-personal-ai-assistant-my-openclaw-tarala-xwszf)

- **Three weeks of Hermes through Telegram** (2026-10-07): 2026-05-17；主帖及OP关于脚本、失败cron、个人数据隔离的回复；模型不稳定评论；机器人摘要与操作代码不作独立证据，未读图片。 [Source 1](https://www.reddit.com/r/hermesagent/comments/1tfrilq/genuinely_blown_away/)

- **Kashmir itinerary test: overview versus details** (2026-10-07): 主帖与旅行测试、作者回应、500限流评论均已读；页面关联2025-03-16，精确发表时间未核；外链产品未登录或试用。 [Source 1](https://www.reddit.com/r/travelindia/comments/1jcjr8h/i_have_made_this_travel_planner_ai_agent_i_do_lot/)

- **Two months with Xiaobu Next: phone workflows and limits** (2026-10-07): TikHub text detail and18 returned comment/reply records read on2026-10-07. Images and video not read; no pagination or product test. [Source 1](https://www.xiaohongshu.com/explore/6a964eec000000002b0257a5)

- **Dots after a few days: agent handoffs and calls** (2026-10-07): TikHub returned long-form post text read; image and replies not read. No independent reproduction. [Source 1](https://x.com/telegram_man/status/2107498869571633273)

- **Poke Recipes: package and share a workflow** (2026-10-07): Current official guide/article text read; linked demonstrations and live workflow not tested. [Source 1](https://poke.com/docs/creating-recipes)

- **Town Routines: recurring email and meeting jobs** (2026-10-07): Current official guide/article text read; linked demonstrations and live workflow not tested. [Source 1](https://www.town.com/docs/features/routines)

- **Today Recording: meeting notes and follow-up** (2026-10-07): Current official guide/article text read; linked demonstrations and live workflow not tested. [Source 1](https://today.ai/articles/blog/introducing-today-recording)

### Articles & engineering

- **OpenPoke: Recreating Poke’s Architecture** (2026-10-07): 2025-09-22；作者正文全文；截图、视频未读，原型源码未审；泄漏prompt未作为权威产品保证。 [Source 1](https://www.shloked.com/openpoke)

- **On the Interaction Acquisition** (2026-10-07): 2026-07-30；短文全文；所链X讨论未读，不据单人经历估总体留存。 [Source 1](https://www.shloked.com/interaction-acquisition)

- **Trying (another) AI assistant — Tanisha Srivatsa** (2026-10-07): 2025-09-23；公开正文与编辑后的访谈全文；截图未读；团队解释未独立核事故。 [Source 1](https://tanishasrivatsa.substack.com/p/i-spent-30-minutes-arguing-with-a)

- **Building 4shClaw — Sylvain Cau** (2026-10-07): 2026-02-28；作者公开HTML正文全文已读；图的文本结构已读、图片与公开repo提交未核；威胁判断是作者论证。 [Source 1](https://4sh.dev/posts/2026/building-4shclaw/)

- **Five OpenClaw workflows — Corey Ganim** (2026-10-07): 2026-02-10；主文全文、五项How it works与制作步骤已读；未看任何YouTube视频或核查产物/工时账单。 [Source 1](https://www.coreyganim.com/blog/5-openclaw-workflows-that-made-me-say-wait-it-can-do-that-by-itself/)

- **Personal Agents Have Gone Mainstream — Sajal Sharma** (2026-10-07): 2026-09-30；作者正文全文；内链市场新闻未逐条核读，不采用其市场规模数字。 [Source 1](https://sajalsharma.com/posts/personal-agents-have-gone-mainstream/)

- **Effective context engineering for AI agents** (2026-10-07): Public article text; images and linked demonstrations not inspected. [Source 1](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)

- **Building effective agents** (2026-10-07): Public article text and its current update notice; examples not reproduced. [Source 1](https://www.anthropic.com/engineering/building-effective-agents)

- **How We Built Safety Into Muse** (2026-10-07): Public engineering article text; no product or security test performed. [Source 1](https://research.meta.ai/blog/security-and-safety-for-ai-agents-our-approach-with-muse)

- **Context Engineering for AI Agents: Lessons from Building Manus** (2026-10-07): Public article text; no implementation reproduction. [Source 1](https://manus.im/blog/Context-Engineering-for-AI-Agents-Lessons-from-Building-Manus)

- **My Agent Stack For Automating My Personal Life** (2026-10-07): Public article text read; screenshots and linked tools not tested. [Source 1](https://www.nicolasbustamante.com/blog/how-agents-run-my-personal-life)

- **Managing Time With an Agent** (2026-10-07): Public article text read; diagrams and linked implementation not tested. [Source 1](https://talalakkari.com/blog/managing-time-with-an-agent/)

- **Ben Thompson on tasks people may not want to delegate** (2026-10-07): TikHub post text read; video and replies not read. This is platform-published discussion text, not a full interview review. [Source 1](https://x.com/tbpn/status/2102529303212970099)

### Papers & evaluations

- **VitaBench 2.0** (2026-10-07): Benchmark, setup and limitations sections; not reproduced. [Source 1](https://arxiv.org/html/2605.27141v1)

- **π-Bench** (2026-10-07): Benchmark, implementation configuration and limitations; not reproduced. [Source 1](https://arxiv.org/html/2605.14678v3)

- **Memora: From Recall to Forgetting** (2026-10-07): Benchmark, experiments, limitations and memory-evaluation appendix; not reproduced. [Source 1](https://arxiv.org/html/2604.20006v1)

- **PASB: Agents Don’t Just Agree, They Remember** (2026-10-07): Sections3–5 and the human-gold appendix; not reproduced. [Source 1](https://arxiv.org/html/2607.10526v1)

- **LongMINT** (2026-10-07): Method and selected experimental sections; not reproduced. [Source 1](https://arxiv.org/html/2605.18565v1)

- **Recuris** (2026-10-07): Selected method, task-state and held-out evaluation sections; not reproduced. [Source 1](https://arxiv.org/html/2608.24876v1)

- **VibeLifeBench** (2026-10-07): arXiv abstract and version metadata only; not reproduced. [Source 1](https://arxiv.org/abs/2608.10875v2)

- **Awesome Personalized RAG Agent / survey** (2026-10-07): Official README and related survey sections4.4.5,5,6. [Source 1](https://github.com/Applied-Machine-Learning-Lab/Awesome-Personalized-RAG-Agent)

- **Personal Agent Bench** (2026-10-07): Homepage, about page, task index and exam methodology; scores not independently reproduced. [Source 1](https://personalagentbench.com/)

- **micro1 PersonalAgentBench launch** (2026-10-07): Public launch text and page-provided transcript; video not watched, linked result inaccessible. [Source 1](https://www.linkedin.com/posts/aliansarinik_which-personal-agent-is-the-best-life-assistant-activity-7513263537247457282-D1-5)

### Collections & discovery

- **Awesome Personal Agents — selection guide** (2026-10-07): Independent public curator/community collection; not an endorsement or benchmark. [Source 1](https://github.com/upgundecha/awesome-personal-agents)

- **Awesome Personal Agents — components** (2026-10-07): Independent public curator/community collection; not an endorsement or benchmark. [Source 1](https://github.com/ahmadyan/awesome-personal-agents)

- **Awesome Personal AI Assistants** (2026-10-07): Independent public curator/community collection; not an endorsement or benchmark. [Source 1](https://github.com/elyase/awesome-personal-ai-assistants)

- **Awesome OpenClaw Use Cases** (2026-10-07): Independent public curator/community collection; not an endorsement or benchmark. [Source 1](https://github.com/hesamsheikh/awesome-openclaw-usecases)

- **Awesome OpenClaw Examples** (2026-10-07): Independent public curator/community collection; not an endorsement or benchmark. [Source 1](https://github.com/OthmaneBlial/awesome-openclaw-examples)

</details>

## Contribute and correct

[Suggest a resource or correction](https://github.com/cubxxw/awesome-personal-agent-practices/issues/new/choose) · [Contributing](CONTRIBUTING.md)

Original annotations are released under [CC0](LICENSE). Linked works retain their own rights.
