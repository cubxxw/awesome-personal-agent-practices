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
  for k in ('name', 'en', 'zh', 'scope'):
   assert isinstance(r[k], str) and r[k].strip() and '\n' not in r[k], (r['id'],k)
  assert len(r['en']) <= 700 and len(r['zh']) <= 450, r['id']
  date.fromisoformat(r['checked_on'])
  safe_url(r['url'])
  for u in r['source_urls']: safe_url(u)
 return data

def resource_name(resource, lang):
 return resource.get('name_zh', resource['name']) if lang == 'zh' else resource['name']


def catalog_section(section, items, lang):
 n = 1 if lang == 'zh' else 0
 lines = [f'<a id="{section}"></a>', '', f'## {SECTIONS[section][n]} · {len(items)}', '']
 groups = [g for g in GROUPS if any(r['category'] == g for r in items)]
 for g in groups:
  lines += [f'<a id="{section}-{g}"></a>', '', f'### {GROUPS[g][n]}', '']
  for r in items:
   if r['category'] != g:
    continue
   lines += [f'<a id="{r["id"]}"></a>', '',
             f'- **[{resource_name(r, lang)}]({r["url"]})** — {r[lang]} <sub>{EVIDENCE[r["evidence"]][n]}</sub>', '']
 return lines


def reading_notes(data, lang):
 n = 1 if lang == 'zh' else 0
 lines = ['<a id="reading-notes"></a>', '',
          '## 读取与来源说明' if n else '## Reading and source notes', '',
          '<details>', '<summary>展开核读范围与原始来源</summary>' if n else '<summary>Reading scope and original sources</summary>', '',
          '正文、摘要与媒体按实际读取范围记录。' if n else 'Text, abstract and media coverage follows the actual reading scope.', '']
 for section in SECTIONS:
  lines += [f'### {SECTIONS[section][n]}', '']
  for r in data['resources']:
   if r['section'] != section:
    continue
   refs = list(dict.fromkeys([r['url'], *r['source_urls']]))
   links = ' · '.join(f'[{"来源" if n else "Source"} {i+1}]({u})' for i, u in enumerate(refs))
   lines += [f'- **{resource_name(r, lang)}** ({r["checked_on"]}): {r["scope"]} {links}', '']
 lines += ['</details>', '']
 return lines


def homepage(data, lang):
 n = 1 if lang == 'zh' else 0
 counts = Counter(r['section'] for r in data['resources'])
 intro = ('个人Agent资源聚合：产品、开源项目、用户案例与玩法，附精选文章和论文。' if n else
          'A curated resource hub for personal AI agents: products, open-source projects, use cases, playbooks, articles and research.')
 lines = ['# Awesome Personal Agents', '', '[English](README.md) · [简体中文](README.zh-CN.md)', '',
          '> ' + intro, '',
          f'**{len(data["resources"])} 条精选资源** · 最近整理：{data["checked_on"]}。' if n else
          f'**{len(data["resources"])} curated resources** · Last curated: {data["checked_on"]}.', '',
          '完整资源直接列在本页。用目录跳到感兴趣的分类，点击资源名称打开原始来源。' if n else
          'The full collection is on this page. Jump to a category below, then open a resource to read its original source.', '',
          '## 目录' if n else '## Contents', '',
          '| 分类 | 找什么 |' if n else '| Category | Find |', '|---|---|']
 descriptions = {
  'products': ('看看产品与助手形态', 'Explore available assistants'),
  'projects': ('找运行框架和接入组件', 'Find runtimes and integration components'),
  'use-cases': ('看实际用法、官方教程与使用限制', 'Explore user workflows, official guides and practical limits'),
  'articles': ('理解产品与工程取舍', 'Understand product and engineering choices'),
  'research': ('找记忆、主动性及评测研究', 'Find memory, proactivity and evaluation research'),
  'collections': ('继续发现相关资料', 'Discover adjacent collections'),
 }
 for section in SECTIONS:
  lines.append(f'| [{SECTIONS[section][n]}](#{section}) · {counts[section]} | {descriptions[section][0 if n else 1]} |')
 lines += ['',
           '产品保留官方说明，用例区分作者自报和官方玩法，研究注明读取范围。可用地区与接入条件以原站为准。' if n else
           'Products retain official context, cases distinguish author reports from official guides, and research records its reading scope. Check the original source for availability and account requirements.', '']
 for section in SECTIONS:
  items = [r for r in data['resources'] if r['section'] == section]
  lines += catalog_section(section, items, lang)
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
 print(json.dumps({'resources':len(data['resources']),'sections':dict(Counter(r['section'] for r in data['resources'])),'generated_pages':len(files),'check':'passed'},ensure_ascii=False))
if __name__=='__main__':main()
