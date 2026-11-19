#!/usr/bin/env python3
"""Validate one resource catalog and render its English/Chinese reading pages."""
import argparse
from collections import Counter
from datetime import date
import json
from pathlib import Path
import re
from urllib.parse import urlsplit, unquote

ROOT = Path(__file__).resolve().parents[1]

# Scenario definitions (ordered for display)
SCENARIOS = {
    'email-communication': ('Email & Communication Workflows', '邮件与沟通工作流'),
    'family-daily': ('Family & Daily Life', '家庭与日常生活'),
    'travel-shopping': ('Travel & Shopping', '旅行与购物'),
    'research-learning': ('Research & Learning', '研究与学习'),
    'limits-cautions': ('Understanding Limits & Cautions', '了解限制与边界'),
    'tools-reference': ('Tools & Research Reference', '工具与研究参考'),
}

SCENARIO_DESCRIPTIONS = {
    'email-communication': {
        'en': 'Practical use cases for email triage, calendar management, and communication workflows, with products and articles on messaging assistants.',
        'zh': '邮件分拣、日程管理与沟通工作流的实际用例，以及消息助手类产品和相关文章。'
    },
    'family-daily': {
        'en': 'Real-world accounts of family coordination, household tasks, reminders, and relationship management, with tools designed for everyday life.',
        'zh': '家庭协调、日常任务、提醒与关系管理的真实案例，以及面向日常生活的工具。'
    },
    'travel-shopping': {
        'en': 'Travel planning and shopping assistance use cases, including itinerary generation and product research.',
        'zh': '旅行规划与购物辅助用例，包括行程生成和产品研究。'
    },
    'research-learning': {
        'en': 'Learning and study workflows with AI assistants, including knowledge recall and content synthesis.',
        'zh': '学习与研究工作流，包括知识回顾和内容整合。'
    },
    'limits-cautions': {
        'en': 'Failure stories, practical limitations, and cautionary accounts that help set realistic expectations.',
        'zh': '失败经验、实际限制与警示案例，帮助建立现实预期。'
    },
    'tools-reference': {
        'en': 'Personal agent platforms, open-source frameworks, engineering articles, research papers, and resource collections for builders and researchers.',
        'zh': '个人Agent平台、开源框架、工程文章、研究论文与资源集合，面向构建者与研究人员。'
    }
}

# Legacy section and group definitions (preserved for stable IDs and anchors)
SECTIONS = {
    'products': ('Products', '产品'),
    'projects': ('Open-source projects', '开源项目'),
    'use-cases': ('Use cases & playbooks', '用例与玩法'),
    'articles': ('Articles & engineering', '文章与技术'),
    'research': ('Papers & evaluations', '论文与评测'),
    'collections': ('Collections & discovery', '资源集合'),
}

GROUPS = {
    'messaging': ('Messaging assistants', '消息入口的助手'),
    'computer': ('Computer & browser assistants', '电脑与浏览器助手'),
    'ecosystem': ('Platform assistants', '平台生态的助手'),
    'family-goals': ('Family & personal goals', '家庭与个人目标'),
    'adjacent': ('Adjacent tools', '邻近工具'),
    'core': ('Personal-agent runtimes', '个人Agent运行框架'),
    'component': ('Memory, tools & integrations', '记忆与接入组件'),
    'email-calendar': ('Email & calendar', '邮件与日历'),
    'research-learning': ('Research & learning', '研究与学习'),
    'travel-shopping': ('Travel & shopping', '旅行与购物'),
    'family-workflows': ('Family & everyday workflows', '家庭与日常流程'),
    'cautions': ('Failure stories & practical limits', '失败经验与使用限制'),
    'practitioner': ('Practitioner accounts', '开发者实践'),
    'engineering': ('Engineering explanations', '工程解释'),
    'memory': ('Memory & personalization', '记忆与个性化'),
    'proactivity': ('Proactivity & continuity', '主动性与任务续接'),
    'evaluation': ('Evaluation methods', '评测方法'),
    'collection': ('Curated collections', '精选集合'),
}

SECTION_GROUPS = {
    'products': {'messaging','computer','ecosystem','family-goals','adjacent'},
    'projects': {'core','component'},
    'use-cases': {'email-calendar','research-learning','travel-shopping','family-workflows','cautions'},
    'articles': {'practitioner','engineering'},
    'research': {'memory','proactivity','evaluation'},
    'collections': {'collection'},
}

EVIDENCE = {
    'official': ('Official description', '官方说明'),
    'official-partial': ('Official source, partially read', '官方来源，部分核读'),
    'open-source': ('Project documentation', '项目文档'),
    'reported': ('Author report', '作者自报'),
    'research': ('Research reading', '研究材料'),
    'collection': ('Resource collection', '资源集合'),
    'implementation-account': ('Implementation account', '实现记录'),
}

def safe_url(value):
    p = urlsplit(value)
    assert p.scheme == 'https' and p.netloc and not p.username and not p.password, value
    assert not any(c.isspace() for c in value), value
    assert not any(k in p.query.lower() for k in ('token=', 'xsec_', 'signature=', 'api_key=', 'access_key=')), value
    assert 'app.notion.com' not in p.netloc and not p.path.startswith('/private/'), value

def load():
    data = json.loads((ROOT / 'data/catalog.json').read_text())
    assert data['schema_version'] == 1
    date.fromisoformat(data['checked_on'])
    ids, urls = set(), set()
    for r in data['resources']:
        assert re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', r['id']), r['id']
        assert r['id'] not in ids and r['url'] not in urls, r['id']
        ids.add(r['id']); urls.add(r['url'])
        assert r['section'] in SECTIONS and r['category'] in GROUPS, r['id']
        assert r['category'] in SECTION_GROUPS[r['section']], (r['id'], 'category does not fit section')
        assert r['evidence'] in EVIDENCE, r['id']
        assert 'scenario' in r and r['scenario'] in SCENARIOS, (r['id'], 'missing or invalid scenario')
        for k in ('name', 'en', 'zh', 'scope'):
            assert isinstance(r[k], str) and r[k].strip() and '\n' not in r[k], (r['id'],k)
            assert len(r['en']) <= 700 and len(r['zh']) <= 450, r['id']
        date.fromisoformat(r['checked_on'])
        safe_url(r['url'])
        for u in r['source_urls']: safe_url(u)
    return data

def resource_name(resource, lang):
    return resource.get('name_zh', resource['name']) if lang == 'zh' else resource['name']


def catalog_scenario(scenario, items, lang):
    """Render one scenario section with use cases first, then tools/articles."""
    n = 1 if lang == 'zh' else 0
    use_cases = [r for r in items if r['section'] == 'use-cases']
    others = [r for r in items if r['section'] != 'use-cases']
    
    lines = [f'<a id="{scenario}"></a>', '', f'## {SCENARIOS[scenario][n]} · {len(items)}', '']
    lines.append(SCENARIO_DESCRIPTIONS[scenario]['zh' if n else 'en'])
    lines.append('')
    
    # Show use cases first
    if use_cases:
        lines += [f'### {"用例" if n else "Use Cases"} · {len(use_cases)}', '']
        for r in use_cases:
            lines += [f'<a id="{r["id"]}"></a>', '',
                      f'- **[{resource_name(r, lang)}]({r["url"]})** — {r[lang]} <sub>{EVIDENCE[r["evidence"]][n]}</sub>', '']
    
    # Show related tools and articles
    if others:
        lines += [f'### {"相关工具与材料" if n else "Related Tools & Articles"} · {len(others)}', '']
        for r in others:
            lines += [f'<a id="{r["id"]}"></a>', '',
                      f'- **[{resource_name(r, lang)}]({r["url"]})** — {r[lang]} <sub>{EVIDENCE[r["evidence"]][n]}</sub>', '']
    
    return lines


def catalog_tools_reference(items, lang):
    """Render tools-reference section organized by original sections."""
    n = 1 if lang == 'zh' else 0
    lines = [f'<a id="tools-reference"></a>', '', 
             f'## {SCENARIOS["tools-reference"][n]} · {len(items)}', '']
    lines.append(SCENARIO_DESCRIPTIONS['tools-reference']['zh' if n else 'en'])
    lines.append('')
    
    # Group by original section
    sections_order = ['products', 'projects', 'articles', 'research', 'collections']
    for section in sections_order:
        section_items = [r for r in items if r['section'] == section]
        if not section_items:
            continue
        
        lines += [f'<a id="{section}"></a>', '', f'### {SECTIONS[section][n]} · {len(section_items)}', '']
        
        # Group by category within section
        groups = [g for g in GROUPS if any(r['category'] == g for r in section_items)]
        for g in groups:
            group_items = [r for r in section_items if r['category'] == g]
            if len(groups) > 1:  # Only show subheadings if multiple groups
                lines += [f'<a id="{section}-{g}"></a>', '', f'#### {GROUPS[g][n]}', '']
            for r in group_items:
                lines += [f'<a id="{r["id"]}"></a>', '',
                          f'- **[{resource_name(r, lang)}]({r["url"]})** — {r[lang]} <sub>{EVIDENCE[r["evidence"]][n]}</sub>', '']
    
    return lines


def reading_notes(data, lang):
    n = 1 if lang == 'zh' else 0
    lines = ['<a id="reading-notes"></a>', '',
             '## 读取与来源说明' if n else '## Reading and source notes', '',
             '<details>', '<summary>展开核读范围与原始来源</summary>' if n else '<summary>Reading scope and original sources</summary>', '',
             '正文、摘要与媒体按实际读取范围记录。' if n else 'Text, abstract and media coverage follows the actual reading scope.', '']
    
    # Group by scenario
    for scenario in SCENARIOS:
        scenario_items = [r for r in data['resources'] if r['scenario'] == scenario]
        if not scenario_items:
            continue
        lines += [f'### {SCENARIOS[scenario][n]}', '']
        for r in scenario_items:
            refs = list(dict.fromkeys([r['url'], *r['source_urls']]))
            links = ' · '.join(f'[{"来源" if n else "Source"} {i+1}]({u})' for i, u in enumerate(refs))
            lines += [f'- **{resource_name(r, lang)}** ({r["checked_on"]}): {r["scope"]} {links}', '']
    
    lines += ['</details>', '']
    return lines


def homepage(data, lang):
    n = 1 if lang == 'zh' else 0
    scenario_counts = Counter(r['scenario'] for r in data['resources'])
    use_case_count = len([r for r in data['resources'] if r['section'] == 'use-cases'])
    
    intro = ('个人Agent资源聚合：按使用场景索引的用例、产品与研究材料。' if n else
             'A curated resource hub for personal AI agents: organized by practical scenarios with use cases, products, and research.')
    
    lines = ['# Awesome Personal Agents', '', '[English](README.md) · [简体中文](README.zh-CN.md)', '',
             '> ' + intro, '',
             f'**{len(data["resources"])} 条精选资源**（含 {use_case_count} 个用例） · 最近整理：{data["checked_on"]}。' if n else
             f'**{len(data["resources"])} curated resources** ({use_case_count} use cases) · Last curated: {data["checked_on"]}.', '',
             '完整资源直接列在本页。按场景跳转，先看实际用例，再看相关工具与材料。' if n else
             'The full collection is on this page. Jump to a scenario to see use cases first, then related tools and articles.', '',
             '## 目录' if n else '## Contents', '',
             '| 场景 | 用例 | 全部 |' if n else '| Scenario | Use Cases | Total |', '|---|---|---|']
    
    for scenario in SCENARIOS:
        if scenario == 'tools-reference':
            continue  # Skip tools-reference in scenario list
        count = scenario_counts.get(scenario, 0)
        use_cases = len([r for r in data['resources'] if r['scenario'] == scenario and r['section'] == 'use-cases'])
        lines.append(f'| [{SCENARIOS[scenario][n]}](#{scenario}) | {use_cases} | {count} |')
    
    # Add tools-reference at the end
    tools_count = scenario_counts.get('tools-reference', 0)
    lines.append(f'| [{SCENARIOS["tools-reference"][n]}](#tools-reference) | — | {tools_count} |')
    
    lines += ['',
              '用例区分作者自报和官方玩法，产品保留官方说明，研究注明读取范围。可用地区与接入条件以原站为准。' if n else
              'Use cases distinguish author reports from official guides, products retain official context, and research records its reading scope. Check the original source for availability and account requirements.', '']
    
    # Render scenario sections
    for scenario in SCENARIOS:
        if scenario == 'tools-reference':
            continue
        items = [r for r in data['resources'] if r['scenario'] == scenario]
        if items:
            lines += catalog_scenario(scenario, items, lang)
    
    # Render tools-reference section
    tools_items = [r for r in data['resources'] if r['scenario'] == 'tools-reference']
    if tools_items:
        lines += catalog_tools_reference(tools_items, lang)
    
    lines += reading_notes(data, lang)
    lines += ['## 贡献与更正' if n else '## Contribute and correct', '',
              '[提交资源或纠错](https://github.com/cubxxw/awesome-personal-agent-practices/issues/new/choose) · [贡献指南](CONTRIBUTING.md)' if n else
              '[Suggest a resource or correction](https://github.com/cubxxw/awesome-personal-agent-practices/issues/new/choose) · [Contributing](CONTRIBUTING.md)', '',
              '原创注释采用[CC0](LICENSE)；所链接内容保留各自权利。' if n else
              'Original annotations are released under [CC0](LICENSE). Linked works retain their own rights.', '']
    return '\n'.join(lines)


def render(data):
    return {'README.md': homepage(data, 'en'), 'README.zh-CN.md': homepage(data, 'zh')}


def validate_publication(data, files):
    """Every catalog entry must be directly readable on each README."""
    expected = {r['id'] for r in data['resources']}
    for relative, text in files.items():
        anchors = re.findall(r'<a id="([^"]+)"></a>', text)
        assert len(anchors) == len(set(anchors)), f'Duplicate navigation anchors: {relative}'
        visible = re.sub(r'<details>.*?</details>', '', text, flags=re.S)
        visible_ids = set(re.findall(r'<a id="([^"]+)"></a>', visible)) & expected
        assert visible_ids == expected, f'Resources hidden or missing: {relative}'
        assert not re.search(r'\]\((?:\./)?docs/', visible), f'Catalog requires a child page: {relative}'
        for r in data['resources']:
            assert f']({r["url"]})' in visible, f'Original source missing: {r["id"]}'


def local_links():
    for p in [*ROOT.glob('*.md'),*ROOT.joinpath('docs').glob('*.md')]:
        for link in re.findall(r'\]\(([^)]+)\)',p.read_text()):
            if urlsplit(link).scheme:continue
            part,_,anchor=link.partition('#'); target=(p.parent/unquote(part)).resolve() if part else p
            assert target.is_relative_to(ROOT) and target.is_file(), (p.name,link)
            if anchor:
                assert f'id="{anchor}"' in target.read_text(),(p.name,link)

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check',action='store_true',help='validate catalog, generation parity and local links without writing')
    args=parser.parse_args();data=load();files=render(data)
    validate_publication(data,files)
    for relative,text in files.items():
        p=ROOT/relative
        if args.check: assert p.exists() and p.read_text()==text, f'Stale generated page: {relative}'
        else:p.write_text(text)
    local_links()
    
    # Enhanced statistics output
    stats = {
        'resources': len(data['resources']),
        'use_cases': len([r for r in data['resources'] if r['section'] == 'use-cases']),
        'scenarios': dict(Counter(r['scenario'] for r in data['resources'])),
        'sections': dict(Counter(r['section'] for r in data['resources'])),
        'generated_pages': len(files),
        'check': 'passed'
    }
    print(json.dumps(stats, ensure_ascii=False, indent=2))

if __name__=='__main__':main()
