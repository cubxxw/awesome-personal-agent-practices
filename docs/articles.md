# Articles & engineering

[Home](../README.md) · [简体中文](articles.zh-CN.md)

13 resources. Content read as of 2026-10-07.

Public resources with their source context preserved. Author reports and project claims are not independent product tests.

[Practitioner accounts](#practitioner) · [Engineering explanations](#engineering)

<a id="practitioner"></a>
## Practitioner accounts

<a id="articles-ar01"></a>
- **[OpenPoke: Recreating Poke’s Architecture](https://www.shloked.com/openpoke)** — Shlok Khemani walks through his local prototype: interaction and execution agents, email tools, triggers and layered memory. It is a reverse engineering account based on usage and leaked prompts, with explicit cost, latency and feature gaps; it is not Poke’s official architecture.
  <sub>Implementation account</sub>

<a id="articles-ar02"></a>
- **[On the Interaction Acquisition](https://www.shloked.com/interaction-acquisition)** — The OpenPoke author explains why he stopped paying for Poke after a month despite liking it: too little email/calendar work and effort needed to invent automations. His broader retention and acquisition explanations are speculation, and he discloses a brief contractor relationship.
  <sub>Author report</sub>

<a id="articles-ar03"></a>
- **[Trying (another) AI assistant — Tanisha Srivatsa](https://tanishasrivatsa.substack.com/p/i-spent-30-minutes-arguing-with-a)** — A Poke user combines onboarding experience with an edited interview about messaging, personality and context. The text includes a messaging outage and the team’s explanation; it is useful product commentary, not a measured reliability study.
  <sub>Author report</sub>

<a id="articles-ar04"></a>
- **[Building 4shClaw — Sylvain Cau](https://4sh.dev/posts/2026/building-4shclaw/)** — Sylvain Cau explains a Telegram system with per-agent containers, capabilities, shared ledgers and gated proactive check-ins. The proposed GLORP project illustrates the handoffs, but the closing section says its implementation pipeline is only ready to begin.
  <sub>Implementation account</sub>

<a id="articles-ar05"></a>
- **[Five OpenClaw workflows — Corey Ganim](https://www.coreyganim.com/blog/5-openclaw-workflows-that-made-me-say-wait-it-can-do-that-by-itself/)** — An operator lists triggers, integrations and review steps for podcast production, inbox triage, repurposing, guest research and meeting preparation. Time-saving and percentage claims are author-reported, and the post also promotes services and a lead magnet.
  <sub>Author report</sub>

<a id="articles-ar06"></a>
- **[Personal Agents Have Gone Mainstream — Sajal Sharma](https://sajalsharma.com/posts/personal-agents-have-gone-mainstream/)** — A long-term tinkerer discusses the shift from asking questions to delegating errands, including account access and memory portability. Read it as product analysis; market figures and competitive claims are not independently checked by this collection.
  <sub>Implementation account</sub>

<a id="articles-nicolas-stack"></a>
- **[My Agent Stack For Automating My Personal Life](https://www.nicolasbustamante.com/blog/how-agents-run-my-personal-life)** — Nicolas describes a cross-app introduction email and his personal tools, files and reusable skills. Includes approval before important messages and the ongoing work of repairing connectors and instructions.
  <sub>Author report</sub>

<a id="articles-talal-calendar"></a>
- **[Managing Time With an Agent](https://talalakkari.com/blog/managing-time-with-an-agent/)** — Talal's account of a shared busy/free calendar, human-accepted invitations and quiet hours. A useful design story about coordinating across calendars without handing over every decision.
  <sub>Author report</sub>

<a id="articles-tbpn-delegation"></a>
- **[Ben Thompson on tasks people may not want to delegate](https://x.com/tbpn/status/2102529303212970099)** — TBPN's published text of Ben Thompson's argument about choosing flights and enjoying shopping. A demand-side counterpoint to automating everything; the interview video was not watched.
  <sub>Author report</sub>

<a id="engineering"></a>
## Engineering explanations

<a id="articles-context-engineering"></a>
- **[Effective context engineering for AI agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)** — Anthropic's guide to selecting context, compacting conversations and keeping persistent notes. Useful for understanding why an assistant loses track during long tasks.
  <sub>Official description</sub>

<a id="articles-building-effective-agents"></a>
- **[Building effective agents](https://www.anthropic.com/engineering/building-effective-agents)** — A foundation for choosing fixed workflows or model-directed agents. Read for the design patterns; the original 2024 article flags that its tooling has since changed.
  <sub>Official description</sub>

<a id="articles-muse-safety"></a>
- **[How We Built Safety Into Muse](https://research.meta.ai/blog/security-and-safety-for-ai-agents-our-approach-with-muse)** — Meta's explanation of Muse's credential handling, isolated execution and action approval. A vendor architecture account, not an independent security audit.
  <sub>Official description</sub>

<a id="articles-manus-context"></a>
- **[Context Engineering for AI Agents: Lessons from Building Manus](https://manus.im/blog/Context-Engineering-for-AI-Agents-Lessons-from-Building-Manus)** — Manus's engineering account of tool context, cache reuse, external state and learning from failed actions. Useful beyond its own product; reported lessons are not a comparative benchmark.
  <sub>Official description</sub>

<details>
<summary>Reading scope and source notes</summary>

Scope distinguishes article text, abstracts and media. Unread images or videos are not treated as experience evidence.

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

[Suggest a resource](../CONTRIBUTING.md)
