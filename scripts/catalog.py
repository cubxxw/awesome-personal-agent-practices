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

def page(section, items, lang, checked):
 n = 1 if lang == 'zh' else 0
 suffix = '.zh-CN' if n else ''
 back = '../README.zh-CN.md' if n else '../README.md'
 title = SECTIONS[section][n]
 lines = [f'# {title}', '', f'[首页]({back}) · [English]({section}.md)' if n else f'[Home]({back}) · [简体中文]({section}.zh-CN.md)', '',
  f'收录 {len(items)} 条资源，内容读取截至 {checked}。' if n else f'{len(items)} resources. Content read as of {checked}.', '',
  '这里聚合公开资源；作者自报、项目说明和研究结果各自保留背景，本库未复跑所有产品。' if n else 'Public resources with their source context preserved. Author reports and project claims are not independent product tests.', '']
 groups = list(dict.fromkeys(r['category'] for r in items))
 lines += [' · '.join(f'[{GROUPS[g][n]}](#{g})' for g in groups),'']
 for g in groups:
  lines += [f'<a id="{g}"></a>', f'## {GROUPS[g][n]}', '']
  for r in items:
   if r['category'] != g: continue
   lines += [f'<a id="{r["id"]}"></a>',f'- **[{r.get("name_zh",r["name"]) if n else r["name"]}]({r["url"]})** — {r[lang]}',f'  <sub>{EVIDENCE[r["evidence"]][n]}</sub>', '']
 lines += ['<details>', '<summary>读取范围与来源记录</summary>' if n else '<summary>Reading scope and source notes</summary>', '',
  '说明正文、摘要和媒体的实际读取范围。未读的图片或视频不作为体验证据。' if n else 'Scope distinguishes article text, abstracts and media. Unread images or videos are not treated as experience evidence.', '']
 for r in items:
  refs = list(dict.fromkeys([r['url'], *r['source_urls']]))
  links = ' · '.join(f'[Source{i+1}]({u})' for i,u in enumerate(refs))
  lines += [f'- **{r["name"]}** ({r["checked_on"]}): {r["scope"]} {links}', '']
 lines += ['</details>', '', '[贡献资源](../CONTRIBUTING.md)' if n else '[Suggest a resource](../CONTRIBUTING.md)', '']
 return '\n'.join(lines)

def homepage(data, lang):
 n=1 if lang=='zh' else 0
 suffix='.zh-CN' if n else ''
 counts=Counter(r['section'] for r in data['resources'])
 title='# Awesome Personal Agents'
 intro='个人Agent资源聚合：产品、开源项目、用户案例与玩法，附精选文章和论文。' if n else 'A curated resource hub for personal AI agents: products, open-source projects, use cases, playbooks, articles and research.'
 lines=[title,'','[English](README.md) · [简体中文](README.zh-CN.md)','','> '+intro,'',
 f'**{len(data["resources"])} 条精选资源** · 最近整理：{data["checked_on"]}。' if n else f'**{len(data["resources"])} curated resources** · Last curated: {data["checked_on"]}.','',
 '从你感兴趣的入口开始。完整目录和读取记录放在分类页。' if n else 'Start with what you want to explore. Full lists and reading notes live in the category pages.','',
 '## 三个主要入口' if n else '## Three ways in','',
 '| 入口 | 内容 |' if n else '| Explore | Find |', '|---|---|']
 descriptions=[('看看产品与形态','Explore available assistants'),('找开源实现和接入组件','Find runtimes and integration components'),('看别人怎么用，以及哪些步骤仍需自己处理','See what people do and what still needs a person')]
 for i,s in enumerate(('products','projects','use-cases')):
  lines.append(f'| [{SECTIONS[s][n]}](docs/{s}{suffix}.md) · {counts[s]} | {descriptions[i][0 if n else 1]} |')
 lines+=['','## 先看这些' if n else '## A few starting points','']
 needles=['Poke','Hermes Agent','OpenMuse','六邮箱','Six inbox','Weekly knowledge','知识复习']
 picked=[]
 for needle in needles:
  found=next((r for r in data['resources'] if needle.casefold() in r['name'].casefold() and r not in picked),None)
  if found:picked.append(found)
 if len(picked)<5:
  picked+= [r for r in data['resources'] if r['section']=='use-cases' and r not in picked][:5-len(picked)]
 for r in picked[:5]:
  lines.append(f'- [{r.get("name_zh",r["name"]) if n else r["name"]}](docs/{r["section"]}{suffix}.md#{r["id"]}) — {r[lang]}')
 lines+=['','## 深入阅读' if n else '## Read further','']
 for s in ('articles','research','collections'):
  lines.append(f'- [{SECTIONS[s][n]}](docs/{s}{suffix}.md) · {counts[s]}')
 lines+=['','## 怎样使用这份目录' if n else '## How to read the list','',
 '按任务选择资源。产品条目依据官方说明；用例区分官方玩法与作者自报，论文注明模拟或研究条件。收录用于发现和学习，不给产品作统一排名。可用地区和接入条件以原站为准。' if n else 'Choose by task. Product entries reflect official descriptions; use cases distinguish official guides from author reports, and research keeps its experimental context. Inclusion supports discovery and learning, not a universal ranking. Check the original source for availability and account requirements.','',
 '[贡献或更正资源](CONTRIBUTING.md) · [提交建议](https://github.com/cubxxw/awesome-personal-agent-practices/issues/new/choose) · [目录数据](data/catalog.json)' if n else '[Contribute or correct a resource](CONTRIBUTING.md) · [Suggest a link](https://github.com/cubxxw/awesome-personal-agent-practices/issues/new/choose) · [Catalog data](data/catalog.json)','',
 '原创注释采用[CC0](LICENSE)；所链接内容保留各自权利。' if n else 'Original annotations are released under [CC0](LICENSE). Linked works retain their own rights.','']
 return '\n'.join(lines)

def render(data):
 result={}
 for lang in ('en','zh'):
  suffix='.zh-CN' if lang=='zh' else ''
  result['README'+suffix+'.md']=homepage(data,lang)
  for section in SECTIONS:
   items=[r for r in data['resources'] if r['section']==section]
   result[f'docs/{section}{suffix}.md']=page(section,items,lang,data['checked_on'])
 return result

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
 for relative,text in files.items():
  anchors=re.findall(r'<a id="([^"]+)"></a>',text)
  assert len(anchors)==len(set(anchors)), f'Duplicate navigation anchors: {relative}'
 for relative,text in files.items():
  p=ROOT/relative
  if args.check: assert p.exists() and p.read_text()==text, f'Stale generated page: {relative}'
  else:p.write_text(text)
 for relative in ('README.md','README.zh-CN.md'):assert len(files[relative].splitlines())<=100
 local_links()
 print(json.dumps({'resources':len(data['resources']),'sections':dict(Counter(r['section'] for r in data['resources'])),'generated_pages':len(files),'check':'passed'},ensure_ascii=False))
if __name__=='__main__':main()
