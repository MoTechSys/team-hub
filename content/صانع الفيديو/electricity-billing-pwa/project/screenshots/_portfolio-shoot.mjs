import { chromium } from "playwright";
import fs from "fs";
const BASE = process.env.BASE || "http://localhost:3105";
const OUT = process.env.OUT || ".";
const backup = fs.readFileSync(new URL("./_demo-backup.json", import.meta.url), "utf8");
const VPS = [["desktop", 1440, 900], ["mobile", 390, 844]];
const browser = await chromium.launch();
const log = [];
for (const [vp, w, h] of VPS) {
  const ctx = await browser.newContext({ viewport: { width: w, height: h }, deviceScaleFactor: 2, isMobile: vp === "mobile", hasTouch: vp === "mobile", locale: "ar" });
  const page = await ctx.newPage();
  const shot = async (name, path, fn) => {
    if (path) { await page.goto(BASE + path, { waitUntil: "networkidle" }); await page.waitForTimeout(2600); }
    if (fn) await fn();
    await page.screenshot({ path: `${OUT}/${vp}-${name}.png`, fullPage: false });
    log.push(`${vp}-${name}.png ← ${path || page.url().replace(BASE, "")}`); console.log(vp, name);
  };
  // 1) fresh visit: splash → onboarding gate (install step)
  await page.goto(BASE + "/dashboard", { waitUntil: "networkidle" }); await page.waitForTimeout(600);
  await page.screenshot({ path: `${OUT}/${vp}-01-splash.png` }); log.push(`${vp}-01-splash.png ← /dashboard (شاشة البداية 0.6ث)`);
  await page.waitForTimeout(2400);
  await shot("02-gate-install", null);
  const skip = page.locator("button.gate-btn-ghost").first();
  if (await skip.count()) { await skip.click(); await page.waitForTimeout(400); }
  await shot("03-gate-license", null);
  await page.fill("input.gate-input", "moain2026"); await page.click("button.gate-btn-gold"); await page.waitForTimeout(800);
  await shot("04-dashboard-empty", null);
  // 2) import demo backup via settings
  await page.goto(BASE + "/settings", { waitUntil: "networkidle" }); await page.waitForTimeout(2600);
  await page.setInputFiles('input[type="file"]', { name: "demo.json", mimeType: "application/json", buffer: Buffer.from(backup) });
  await page.waitForTimeout(1200);
  await shot("05-settings-backup", null);
  await shot("06-dashboard", "/dashboard");
  await shot("07-subscribers", "/subscribers");
  await shot("08-subscribers-kebab", null, async () => { const k = page.locator("table tbody button").first(); if (await k.count()) { await k.click(); await page.waitForTimeout(400); } });
  await shot("09-subscriber-new", "/subscribers/new");
  await shot("10-invoice-new", "/invoices/new");
  await shot("11-invoice-new-filled", null, async () => {
    await page.fill('input[placeholder^="اختر العميل"]', "S-1003"); await page.waitForTimeout(500);
    const opt = page.locator("div.font-medium.text-sm").first(); if (await opt.count()) await opt.click();
    await page.waitForTimeout(300);
    await page.fill('input[name="previousReading"]', "24149"); await page.fill('input[name="currentReading"]', "25254");
    await page.waitForTimeout(700);
  });
  await shot("12-archive", "/invoices/archive");
  await shot("13-invoice-print", "/invoices/id_demo_i01/print");
  if (vp === "desktop") await shot("14-invoices", "/invoices");
  await ctx.close();
}
fs.writeFileSync(`${OUT}/_shots.log`, log.join("\n"));
await browser.close();
