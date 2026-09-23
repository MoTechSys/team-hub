#!/usr/bin/env python3
# project: portfolio-hub | author-agent: متخصص SEO | date: 2026-09-23 | status: v1
"""Real 2x screenshots of alabbasi-tech-platform (site static export + portal) served locally on :3210.
Desktop 1440x900 @2x, mobile 390x844 @2x. Portal shots use a seeded demo admin (demo@example.test) — no real data."""
import os, sys, time
from playwright.sync_api import sync_playwright

OUT = os.path.expanduser('~/agent-state/work/alabbasi-tech-platform/screenshots'); os.makedirs(OUT, exist_ok=True)
BASE = 'http://127.0.0.1:3210'
SITE = [
    ('01-home', '/'), ('02-work', '/work/'), ('03-systems', '/systems/'), ('04-erp-pos', '/systems/erp-pos/'),
    ('05-alternatives', '/alternatives/'), ('06-alt-onyx', '/alternatives/yemensoft-onyx-pro/'), ('07-services', '/services/'),
    ('08-process', '/process/'), ('09-about', '/about/'), ('10-contact', '/contact/'), ('11-zero-trust', '/systems/zero-trust/'),
]
MOBILE = [('01-home', '/'), ('02-work', '/work/'), ('03-systems', '/systems/'), ('04-erp-pos', '/systems/erp-pos/'), ('05-contact', '/contact/'), ('06-alt-onyx', '/alternatives/yemensoft-onyx-pro/')]


def shot(pg, path, name, w, h, prefix, full=False):
    pg.goto(BASE + path, wait_until='networkidle'); time.sleep(0.6)
    pg.evaluate("window.scrollTo(0,0)")
    pg.screenshot(path=f'{OUT}/{prefix}-{name}.png', full_page=full)
    print(prefix, name, pg.title())


with sync_playwright() as p:
    b = p.chromium.launch()
    # desktop
    ctx = b.new_context(viewport={'width': 1440, 'height': 900}, device_scale_factor=2, locale='ar')
    pg = ctx.new_page()
    for name, path in SITE:
        shot(pg, path, name, 1440, 900, 'desktop')
    # portal: login page, then dashboard tabs
    pg.goto(BASE + '/portal/', wait_until='networkidle'); time.sleep(0.5)
    pg.screenshot(path=f'{OUT}/desktop-12-portal-login.png'); print('desktop 12 portal-login', pg.title())
    ctx.close()
    # mobile
    ctx = b.new_context(viewport={'width': 390, 'height': 844}, device_scale_factor=2, is_mobile=True, has_touch=True, locale='ar')
    pg = ctx.new_page()
    for name, path in MOBILE:
        shot(pg, path, name, 390, 844, 'mobile')
    pg.goto(BASE + '/portal/', wait_until='networkidle'); time.sleep(0.5)
    pg.screenshot(path=f'{OUT}/mobile-07-portal-login.png'); print('mobile 07 portal-login')
    ctx.close()
    b.close()
