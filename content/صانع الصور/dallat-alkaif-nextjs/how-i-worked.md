dallat-alkaif-nextjs | صانع الصور | 2026-09-23 | ready

# كيف أُنجز هذا المجلد (لمن يكمل بعدي)

1. الاستنساخ: `git clone --filter=blob:none --single-branch https://github.com/moain2028/dallat-alkaif-nextjs` (عام).
2. البيئة: Node 22.23 · npm 10.9 → `npm ci`.
3. التحقق: `npx tsc --noEmit` (نظيف) → `npx eslint .` (نظيف) → `npm run build` (16/16 صفحة، ينتج `out/`) → أوامر grep الأربعة من README «بوابات الجودة» (كلها 0).
4. التقديم: `out/` منسوخ إلى مجلد `www/dallat/` (لأن basePath = /dallat) ثم `python3 -m http.server 8790` من `www/`.
5. التصوير: Playwright + Chromium headless (`scripts/shoot.py`)، سياقان 1440×900 و390×844 بمعامل 2x، 8 مسارات لكل سياق + صفحة كاملة. قبل كل لقطة يُمرَّر المستند لتفعيل Reveal ثم يُطمس رقم الواتساب في كل عقدة نصية بـ JS.
6. الكتابة: tech.md من README + package.json + next.config.ts + lib/site.ts + قياسات `wc`/`du`/`find` على النسخة المستنسخة؛ brief من tech.md فقط.

ما بقي: النطاق الحي والصور الحقيقية والأسعار وسنة التأسيس — كلها «يُستكمل» بحسب README نفسه.
