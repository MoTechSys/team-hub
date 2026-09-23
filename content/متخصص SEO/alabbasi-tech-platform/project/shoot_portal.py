#!/usr/bin/env python3
# Portal dashboard shots with seeded demo admin (demo@example.test) — seed data only, no real clients.
import os, time
from playwright.sync_api import sync_playwright
OUT = os.path.expanduser('~/agent-state/work/alabbasi-tech-platform/screenshots')
BASE = 'http://127.0.0.1:3210'
with sync_playwright() as p:
    b = p.chromium.launch()
    for prefix, vp, mob in (('desktop', {'width': 1440, 'height': 900}, False), ('mobile', {'width': 390, 'height': 844}, True)):
        ctx = b.new_context(viewport=vp, device_scale_factor=2, is_mobile=mob, has_touch=mob, locale='ar')
        pg = ctx.new_page()
        pg.goto(BASE + '/portal/', wait_until='networkidle')
        pg.fill('#fLogin input[name=email]', 'demo@example.test')
        pg.fill('#fLogin input[name=password]', 'Demo-Pass-2026!')
        pg.click('#bLogin')
        pg.wait_for_url('**/portal/app.html', timeout=10000); pg.wait_for_load_state('networkidle'); time.sleep(0.8)
        n = 13 if not mob else 8
        pg.screenshot(path=f'{OUT}/{prefix}-{n:02d}-portal-projects.png'); print(prefix, 'projects')
        for k, v in (('tickets', 1), ('requests', 2)):
            btn = pg.query_selector(f'.tab[data-v={k}]')
            if btn and btn.is_visible():
                btn.click(); time.sleep(0.6)
                pg.screenshot(path=f'{OUT}/{prefix}-{n+v:02d}-portal-{k}.png'); print(prefix, k)
        ctx.close()
    b.close()
