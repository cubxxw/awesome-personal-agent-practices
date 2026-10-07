# Open-source projects

[Home](../README.md) · [简体中文](projects.zh-CN.md)

20 resources. Content read as of 2026-10-07.

Public resources with their source context preserved. Author reports and project claims are not independent product tests.

[Personal-agent runtimes](#core) · [Memory, tools & integrations](#component)

<a id="core"></a>
## Personal-agent runtimes

<a id="projects-openclaw"></a>
- **[OpenClaw](https://github.com/openclaw/openclaw)** — Self-hosted personal assistant with messaging channels, tools, memory, and scheduled automations; a useful starting point for everyday assistant workflows. Tool access and channel permissions depend on your deployment configuration.
  <sub>Project documentation</sub>

<a id="projects-hermes-agent"></a>
- **[Hermes Agent](https://github.com/NousResearch/hermes-agent)** — Nous Research's personal agent combines persistent memory, reusable skills, messaging, and scheduled work across local or remote environments. Scheduled delivery needs an active gateway or a configured managed scheduler.
  <sub>Project documentation</sub>

<a id="projects-letta-code"></a>
- **[Letta Code](https://github.com/letta-ai/letta-code)** — Stateful agents with Git-backed memory, background dreaming, channels, and local or cloud backends; useful for exploring assistants that carry context between conversations. This is the current source repository; the former Letta V1 API server is archived separately.
  <sub>Project documentation</sub>

<a id="projects-nanoclaw"></a>
- **[NanoClaw](https://github.com/nanocoai/nanoclaw)** — Container-based assistant with per-agent working files, memory, messaging integrations, and scheduled tasks. The repository moved from qwibitai to nanocoai; network lockdown is optional, so container isolation should not be read as blanket permission protection.
  <sub>Project documentation</sub>

<a id="projects-openmuse"></a>
- **[OpenMuse](https://github.com/CopilotKit/openmuse)** — CopilotKit's personal-agent application template brings together email, calendar, a persistent browser, visible task progress, and action approvals. It is an alpha for self-hosting and building on, with integrations that require their own configuration.
  <sub>Project documentation</sub>

<a id="projects-nanobot"></a>
- **[nanobot](https://github.com/HKUDS/nanobot)** — HKUDS's Python personal-agent framework provides a WebUI, chat integrations, tools, memory, and automation in a readable core. A gateway must remain running for scheduled delivery, and source builds may differ from stable packages.
  <sub>Project documentation</sub>

<a id="projects-zeroclaw"></a>
- **[ZeroClaw](https://github.com/zeroclaw-labs/zeroclaw)** — Rust personal-assistant runtime with pluggable models, messaging channels, tools, and event-triggered routines. Worth exploring for a configurable always-on setup; autonomy and sandbox choices change what it can access.
  <sub>Project documentation</sub>

<a id="projects-picoclaw"></a>
- **[PicoClaw](https://github.com/sipeed/picoclaw)** — Sipeed's independent Go assistant targets small devices and multiple hardware architectures, with chat channels and tool integrations. Useful for edge-device experiments; the README flags rapid development and changing resource usage.
  <sub>Project documentation</sub>

<a id="projects-ironclaw"></a>
- **[IronClaw](https://github.com/nearai/ironclaw)** — NEAR AI's personal assistant emphasizes sandboxed tools, credential handling, persistent memory, and background routines. A useful security-oriented design reference; protection still depends on the configured provider, tools, and policies.
  <sub>Project documentation</sub>

<a id="projects-qwenpaw"></a>
- **[QwenPaw (formerly CoPaw)](https://github.com/agentscope-ai/QwenPaw)** — AgentScope's personal assistant combines editable memory, skills, scheduled tasks, and channels including DingTalk and Lark. The former CoPaw repository now redirects here; integrations and local or cloud models need configuration.
  <sub>Project documentation</sub>

<a id="projects-rowboat"></a>
- **[Rowboat](https://github.com/rowboatlabs/rowboat)** — Desktop personal assistant that connects a work knowledge graph with email, notes, browser tasks, and background agents. Useful for work-context and team-space ideas; shared spaces and model providers have separate data boundaries to consider.
  <sub>Project documentation</sub>

<a id="projects-khoj"></a>
- **[Khoj](https://github.com/khoj-ai/khoj)** — Self-hostable personal AI for querying documents and the web, creating custom agents, and delivering recurring research or notifications. A useful entry point for a knowledge-focused assistant; document answers alone do not establish reliable external actions.
  <sub>Project documentation</sub>

<a id="component"></a>
## Memory, tools & integrations

<a id="projects-mem0"></a>
- **[Mem0](https://github.com/mem0ai/mem0)** — Memory layer for retaining user preferences and context across assistant conversations, with library, self-hosted, and managed options. The README distinguishes managed-platform optimizations from the open-source SDK, so their reported performance should not be treated as identical.
  <sub>Project documentation</sub>

<a id="projects-hindsight"></a>
- **[Hindsight](https://github.com/vectorize-io/hindsight)** — Agent memory organized around retain, recall, and reflect operations, with separate memory banks and time-aware retrieval. Useful for assistants that revisit experiences; it adds storage and model dependencies, and may be excessive for simple scheduled scripts.
  <sub>Project documentation</sub>

<a id="projects-graphiti"></a>
- **[Graphiti](https://github.com/getzep/graphiti)** — Temporal knowledge-graph framework for tracking changing facts, relationships, and their source episodes. Useful for personal relationship or project context; you provide the graph database and model setup, while Zep's managed service is a separate product.
  <sub>Project documentation</sub>

<a id="projects-e2b"></a>
- **[E2B](https://github.com/e2b-dev/E2B)** — Sandbox infrastructure and SDKs for running assistant code, commands, and desktop interactions away from the user's main machine. Hosted execution requires an account, while self-hosting has its own setup; a sandbox does not define the assistant's authorization policy.
  <sub>Project documentation</sub>

<a id="projects-browser-use"></a>
- **[Browser Use](https://github.com/browser-use/browser-use)** — Open-source browser agent for web tasks such as finding information and filling forms, with local-library and separate hosted options. A practical computer-use starting point; models, browser accounts, and hosted services have their own access and cost requirements.
  <sub>Project documentation</sub>

<a id="projects-playwright-mcp"></a>
- **[Playwright MCP](https://github.com/microsoft/playwright-mcp)** — Microsoft's MCP interface exposes structured browser interaction through Playwright, useful for assistants that inspect and operate web pages. Its README explicitly states that it is not a security boundary; browser access must be scoped separately.
  <sub>Project documentation</sub>

<a id="projects-google-workspace-cli"></a>
- **[Google Workspace CLI (gws)](https://github.com/googleworkspace/cli)** — CLI with structured output and agent skills for Gmail, Calendar, Drive, and other Workspace APIs, useful for email and scheduling workflows. Despite the repository organization, the README says it is not an officially supported Google product; OAuth setup is required.
  <sub>Project documentation</sub>

<a id="projects-agentmail-python"></a>
- **[AgentMail Python SDK](https://github.com/agentmail-to/agentmail-python)** — Official Python client for AgentMail's inbox APIs, useful when an assistant needs its own email inbox and programmatic communication. The SDK is open source, while the email service requires an AgentMail account and API key.
  <sub>Project documentation</sub>

<details>
<summary>Reading scope and source notes</summary>

Scope distinguishes article text, abstracts and media. Unread images or videos are not treated as experience evidence.

- **OpenClaw** (2026-10-07): Self-hosted assistant and automation runtime [Source1](https://github.com/openclaw/openclaw) · [Source2](https://github.com/openclaw/openclaw/blob/0dc20916873149b6f6803d1eae711c8d44f3de9e/README.md) · [Source3](https://github.com/openclaw/openclaw/blob/0dc20916873149b6f6803d1eae711c8d44f3de9e/docs/automation/index.md)

- **Hermes Agent** (2026-10-07): Personal agent, skills, memory, and scheduled work [Source1](https://github.com/NousResearch/hermes-agent) · [Source2](https://github.com/NousResearch/hermes-agent/blob/a50406d9b7474b060450d2dcaff8743c977d296a/README.md) · [Source3](https://github.com/NousResearch/hermes-agent/blob/a50406d9b7474b060450d2dcaff8743c977d296a/website/docs/user-guide/features/cron.md)

- **Letta Code** (2026-10-07): Stateful personal agents and editable memory [Source1](https://github.com/letta-ai/letta-code) · [Source2](https://github.com/letta-ai/letta-code/blob/4b028fab07c69edaac2ddb4f7b9a43573ff20d81/README.md) · [Source3](https://github.com/letta-ai/letta/blob/5bcdd177d70fa2b31a754cfcd801e77b2e1ab16a/README.md)

- **NanoClaw** (2026-10-07): Container-based personal assistant [Source1](https://github.com/nanocoai/nanoclaw) · [Source2](https://github.com/nanocoai/nanoclaw/blob/66f0823a693bd9cca4123e72f8ccee05f5e7e1c5/README.md) · [Source3](https://github.com/nanocoai/nanoclaw/blob/66f0823a693bd9cca4123e72f8ccee05f5e7e1c5/docs/SECURITY.md)

- **OpenMuse** (2026-10-07): Personal-agent application template [Source1](https://github.com/CopilotKit/openmuse) · [Source2](https://github.com/CopilotKit/openmuse/blob/1ac68f3909f2478ab6280883f1ab5ea65eb5719d/README.md) · [Source3](https://github.com/CopilotKit/openmuse/blob/1ac68f3909f2478ab6280883f1ab5ea65eb5719d/apps/server/src/actions.ts)

- **nanobot** (2026-10-07): Lightweight Python personal-agent runtime [Source1](https://github.com/HKUDS/nanobot) · [Source2](https://github.com/HKUDS/nanobot/blob/main/README.md) · [Source3](https://github.com/HKUDS/nanobot/blob/main/docs/automations.md)

- **ZeroClaw** (2026-10-07): Rust personal-assistant runtime [Source1](https://github.com/zeroclaw-labs/zeroclaw) · [Source2](https://github.com/zeroclaw-labs/zeroclaw/blob/master/README.md)

- **PicoClaw** (2026-10-07): Personal assistant for small and edge devices [Source1](https://github.com/sipeed/picoclaw) · [Source2](https://github.com/sipeed/picoclaw/blob/main/README.md)

- **IronClaw** (2026-10-07): Personal assistant with sandboxed tool execution [Source1](https://github.com/nearai/ironclaw) · [Source2](https://github.com/nearai/ironclaw/blob/main/README.md)

- **QwenPaw (formerly CoPaw)** (2026-10-07): Personal assistant with Chinese workplace channels [Source1](https://github.com/agentscope-ai/QwenPaw) · [Source2](https://github.com/agentscope-ai/QwenPaw/blob/main/README.md) · [Source3](https://github.com/agentscope-ai/CoPaw)

- **Rowboat** (2026-10-07): Desktop work assistant and shared spaces [Source1](https://github.com/rowboatlabs/rowboat) · [Source2](https://github.com/rowboatlabs/rowboat/blob/main/README.md)

- **Khoj** (2026-10-07): Knowledge-focused personal AI and research automation [Source1](https://github.com/khoj-ai/khoj) · [Source2](https://github.com/khoj-ai/khoj/blob/master/README.md)

- **Mem0** (2026-10-07): Assistant memory component [Source1](https://github.com/mem0ai/mem0) · [Source2](https://github.com/mem0ai/mem0/blob/main/README.md)

- **Hindsight** (2026-10-07): Persistent assistant memory and reflection [Source1](https://github.com/vectorize-io/hindsight) · [Source2](https://github.com/vectorize-io/hindsight/blob/main/README.md)

- **Graphiti** (2026-10-07): Temporal context and relationship memory [Source1](https://github.com/getzep/graphiti) · [Source2](https://github.com/getzep/graphiti/blob/main/README.md)

- **E2B** (2026-10-07): Agent execution sandbox and cloud desktop [Source1](https://github.com/e2b-dev/E2B) · [Source2](https://github.com/e2b-dev/E2B/blob/main/README.md)

- **Browser Use** (2026-10-07): Browser tasks and web automation [Source1](https://github.com/browser-use/browser-use) · [Source2](https://github.com/browser-use/browser-use/blob/main/README.md)

- **Playwright MCP** (2026-10-07): Structured browser tools for assistants [Source1](https://github.com/microsoft/playwright-mcp) · [Source2](https://github.com/microsoft/playwright-mcp/blob/main/README.md)

- **Google Workspace CLI (gws)** (2026-10-07): Email, calendar, and Workspace tools [Source1](https://github.com/googleworkspace/cli) · [Source2](https://github.com/googleworkspace/cli/blob/main/README.md)

- **AgentMail Python SDK** (2026-10-07): Agent-owned email inbox client [Source1](https://github.com/agentmail-to/agentmail-python) · [Source2](https://github.com/agentmail-to/agentmail-python/blob/main/README.md)

</details>

[Suggest a resource](../CONTRIBUTING.md)
