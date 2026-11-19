#!/usr/bin/env python3
"""Add scenario field to catalog resources based on content analysis."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# Scenario mapping based on actual content
SCENARIO_MAP = {
    # Email & Communication Workflows
    'use-cases-uc03': 'email-communication',
    'use-cases-uc04': 'email-communication',
    'use-cases-uc05': 'email-communication',
    'use-cases-uc11': 'email-communication',
    'use-cases-town-routines': 'email-communication',
    'use-cases-today-recording': 'email-communication',
    'use-cases-meeting-brief-context': 'email-communication',
    
    # Family & Daily Life
    'use-cases-uc01': 'family-daily',
    'use-cases-uc10': 'family-daily',
    'use-cases-uc12': 'family-daily',
    'use-cases-uc13': 'family-daily',
    'use-cases-xiaobu-phone': 'family-daily',
    'use-cases-poke-recipes': 'family-daily',
    'use-cases-reconnect-reminders': 'family-daily',
    'use-cases-group-chat-filter': 'family-daily',
    'use-cases-birthday-gift-memory': 'family-daily',
    'use-cases-reconnect-past-contacts': 'family-daily',
    'use-cases-group-coordination': 'family-daily',
    'use-cases-family-mental-load': 'family-daily',
    'use-cases-intent-introductions': 'family-daily',
    
    # Travel & Shopping
    'use-cases-uc06': 'travel-shopping',
    'use-cases-uc14': 'travel-shopping',
    
    # Research & Learning
    'use-cases-uc09': 'research-learning',
    
    # Limits & Cautions
    'use-cases-uc02': 'limits-cautions',
    'use-cases-uc07': 'limits-cautions',
    'use-cases-uc08': 'limits-cautions',
    'use-cases-dots-handoffs': 'limits-cautions',
}

# Products by scenario
PRODUCT_SCENARIO = {
    # Messaging products → email-communication
    'products-instinct': 'email-communication',
    'products-poke': 'email-communication',
    'products-town': 'email-communication',
    'products-dot-new-computer': 'email-communication',
    'products-pi-inflection': 'email-communication',
    
    # Family-goals products → family-daily
    'products-tomo-mapo': 'family-daily',
    'products-ollie': 'family-daily',
    'products-heycue-life-admin': 'family-daily',
    
    # Computer/ecosystem/adjacent → tools-reference
    'products-today-ai': 'tools-reference',
    'products-meta-muse': 'tools-reference',
    'products-chatgpt-dots': 'tools-reference',
    'products-grok-bot': 'tools-reference',
    'products-manus-cue': 'tools-reference',
    'products-gemini-spark': 'tools-reference',
    'products-siri-ai': 'tools-reference',
    'products-manus': 'tools-reference',
    'products-claude-cowork': 'tools-reference',
    'products-since-kindly-today-ai': 'tools-reference',
    'products-cue-desktop': 'tools-reference',
    'products-limitless': 'tools-reference',
    'products-friend-wearable': 'tools-reference',
    'products-microsoft-365-copilot': 'tools-reference',
    'products-muse-connectors': 'tools-reference',
    'products-spell-bytedance': 'tools-reference',
    'products-lightvela-tencent': 'tools-reference',
}

# All projects → tools-reference
# All research → tools-reference
# All collections → tools-reference

def add_scenarios():
    data = json.loads((ROOT / 'data/catalog.json').read_text())
    
    for r in data['resources']:
        # Check explicit mappings first
        if r['id'] in SCENARIO_MAP:
            r['scenario'] = SCENARIO_MAP[r['id']]
        elif r['id'] in PRODUCT_SCENARIO:
            r['scenario'] = PRODUCT_SCENARIO[r['id']]
        # All projects, research, collections → tools-reference
        elif r['section'] in ['projects', 'research', 'collections']:
            r['scenario'] = 'tools-reference'
        # Remaining articles → tools-reference
        elif r['section'] == 'articles':
            r['scenario'] = 'tools-reference'
        else:
            # Should not happen, but default to tools-reference
            r['scenario'] = 'tools-reference'
    
    # Write updated catalog
    (ROOT / 'data/catalog.json').write_text(json.dumps(data, ensure_ascii=False, indent=2))
    print(f"Added scenarios to {len(data['resources'])} resources")

if __name__ == '__main__':
    add_scenarios()
