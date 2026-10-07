# 开源项目

[首页](../README.zh-CN.md) · [English](projects.md)

收录 20 条资源，内容读取截至 2026-10-07。

这里聚合公开资源；作者自报、项目说明和研究结果各自保留背景，本库未复跑所有产品。

[个人Agent运行框架](#core) · [记忆与接入组件](#component)

<a id="core"></a>
## 个人Agent运行框架

<a id="projects-openclaw"></a>
- **[OpenClaw](https://github.com/openclaw/openclaw)** — 把消息渠道、工具、记忆和定时任务接在一起的自托管个人助手，适合从日常工作流开始探索。工具访问和渠道权限需要按自己的部署配置。
  <sub>项目文档</sub>

<a id="projects-hermes-agent"></a>
- **[Hermes Agent](https://github.com/NousResearch/hermes-agent)** — Nous Research 的个人Agent，结合持久记忆、可复用技能、消息入口和定时工作，可在本机或远程环境运行。定时结果送达需要持续运行的 gateway 或已配置的托管调度。
  <sub>项目文档</sub>

<a id="projects-letta-code"></a>
- **[Letta Code](https://github.com/letta-ai/letta-code)** — 用 Git 管理记忆，支持后台整理、消息渠道及本地或云端运行，适合探索跨对话保留上下文的助手。当前源码在 letta-code；原 Letta V1 API server 已另行归档。
  <sub>项目文档</sub>

<a id="projects-nanoclaw"></a>
- **[NanoClaw](https://github.com/nanocoai/nanoclaw)** — 以容器运行助手，提供按 Agent 划分的工作文件、记忆、消息集成和定时任务。仓库已从 qwibitai 迁到 nanocoai；出网限制是可选配置，容器隔离不代表所有动作都有权限保护。
  <sub>项目文档</sub>

<a id="projects-openmuse"></a>
- **[OpenMuse](https://github.com/CopilotKit/openmuse)** — CopilotKit 的个人Agent 应用模板，把邮件、日历、持久浏览器、任务进展和动作审批放在同一工作面。当前为适合自托管和二次开发的 alpha，相关集成需要单独配置。
  <sub>项目文档</sub>

<a id="projects-nanobot"></a>
- **[nanobot](https://github.com/HKUDS/nanobot)** — HKUDS 的 Python 个人Agent 框架，提供网页界面、聊天集成、工具、记忆和自动化，适合读源码和自行扩展。定时结果送达需要 gateway 持续运行，源码版与稳定包可能不同。
  <sub>项目文档</sub>

<a id="projects-zeroclaw"></a>
- **[ZeroClaw](https://github.com/zeroclaw-labs/zeroclaw)** — Rust 编写的个人助手运行时，支持可替换模型、消息渠道、工具和事件触发流程，适合探索可配置的常驻助手。自主等级和沙箱选项会影响它能访问哪些资源。
  <sub>项目文档</sub>

<a id="projects-picoclaw"></a>
- **[PicoClaw](https://github.com/sipeed/picoclaw)** — Sipeed 独立开发的 Go 个人助手，面向小型设备和多种硬件架构，提供聊天渠道与工具集成。适合边缘设备实验；README 提醒项目仍在快速开发，资源占用会随版本变化。
  <sub>项目文档</sub>

<a id="projects-ironclaw"></a>
- **[IronClaw](https://github.com/nearai/ironclaw)** — NEAR AI 的个人助手，重点包括工具沙箱、凭据处理、持久记忆和后台例程，适合了解围绕安全边界的设计。实际保护范围仍取决于模型服务、工具和策略配置。
  <sub>项目文档</sub>

<a id="projects-qwenpaw"></a>
- **[QwenPaw (formerly CoPaw)](https://github.com/agentscope-ai/QwenPaw)** — AgentScope 的个人助手，结合可编辑记忆、技能、定时任务以及钉钉、飞书等渠道。原 CoPaw 仓库已重定向至这里，集成及本地或云端模型需要配置。
  <sub>项目文档</sub>

<a id="projects-rowboat"></a>
- **[Rowboat](https://github.com/rowboatlabs/rowboat)** — 桌面个人助手，用工作知识图谱连接邮件、笔记、浏览器任务和后台 Agent，适合探索如何利用工作上下文及团队空间。共享空间与模型服务的数据边界需要分别了解。
  <sub>项目文档</sub>

<a id="projects-khoj"></a>
- **[Khoj](https://github.com/khoj-ai/khoj)** — 可自托管的个人 AI，支持查询文档与网络、创建自定义 Agent，以及定期研究和通知。适合以个人知识为起点，文档问答能力本身不能证明外部操作可靠。
  <sub>项目文档</sub>

<a id="component"></a>
## 记忆与接入组件

<a id="projects-mem0"></a>
- **[Mem0](https://github.com/mem0ai/mem0)** — 为助手跨对话保留用户偏好和上下文的记忆层，提供库、自托管和托管服务选项。README 明确托管平台包含开源 SDK 未提供的优化，相关成绩不能直接视为开源版表现。
  <sub>项目文档</sub>

<a id="projects-hindsight"></a>
- **[Hindsight](https://github.com/vectorize-io/hindsight)** — 围绕保存、召回和反思组织 Agent 记忆，提供独立记忆库与时间相关检索，适合需要回顾经验的助手。它增加存储和模型依赖，对简单定时脚本可能过重。
  <sub>项目文档</sub>

<a id="projects-graphiti"></a>
- **[Graphiti](https://github.com/getzep/graphiti)** — 跟踪事实、关系及其来源如何变化的时间知识图谱框架，可用于个人关系或项目上下文。需要自行配置图数据库和模型，Zep 的托管服务是另一项产品。
  <sub>项目文档</sub>

<a id="projects-e2b"></a>
- **[E2B](https://github.com/e2b-dev/E2B)** — 供助手运行代码、命令和桌面操作的沙箱基础设施与 SDK，可把执行环境与用户主电脑分开。托管执行需要账号，自托管另有部署要求；沙箱本身不决定助手的授权策略。
  <sub>项目文档</sub>

<a id="projects-browser-use"></a>
- **[Browser Use](https://github.com/browser-use/browser-use)** — 用于查找信息、填写表单等网页任务的开源浏览器 Agent，提供本地库及独立托管选项，适合作为电脑操作的起点。模型、浏览器账号和托管服务各有访问及费用要求。
  <sub>项目文档</sub>

<a id="projects-playwright-mcp"></a>
- **[Playwright MCP](https://github.com/microsoft/playwright-mcp)** — Microsoft 提供的 Playwright MCP 接口，让助手通过结构化信息查看和操作网页。README 明确它不是安全边界，浏览器访问范围需要另外限定。
  <sub>项目文档</sub>

<a id="projects-google-workspace-cli"></a>
- **[Google Workspace CLI (gws)](https://github.com/googleworkspace/cli)** — 提供结构化输出及 Agent 技能的 Workspace 命令行工具，可用于 Gmail、Calendar、Drive 等邮件和日程工作流。虽然仓库位于 googleworkspace 组织，README 明确它不是 Google 官方支持的产品，并需要配置 OAuth。
  <sub>项目文档</sub>

<a id="projects-agentmail-python"></a>
- **[AgentMail Python SDK](https://github.com/agentmail-to/agentmail-python)** — AgentMail 官方 Python 客户端，用于创建和操作 Agent 收件箱，适合需要独立邮箱及程序化通信的助手。SDK 开源，邮件服务需要 AgentMail 账号和 API key。
  <sub>项目文档</sub>

<details>
<summary>读取范围与来源记录</summary>

说明正文、摘要和媒体的实际读取范围。未读的图片或视频不作为体验证据。

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

[贡献资源](../CONTRIBUTING.md)
