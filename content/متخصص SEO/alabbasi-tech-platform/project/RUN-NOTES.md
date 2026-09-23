alabbasi-tech-platform | متخصص SEO | 2026-09-23 | البند 0 — تشغيل محلي ولقطات

# كيف شُغّل المشروع محلياً (2026-09-23)
- الاستنساخ: `git clone https://github.com/moain2028/alabbasi-tech-platform` (commit واحد 2026-08-07).
- الموقع: `cd site && npm install` → `npm run typecheck` (0 أخطاء) → `npm run build` (Generating static pages 19/19 → `out/`) → `npx vitest run` (11/11).
- المنصة: `cd portal && npm install` → `node scripts/seed-admin.js demo@example.test '<pass>' 'مدير تجريبي'` (طبّق ترحيلَي 001-init و002-ticket-attachments وأنشأ مديراً تجريبياً) → `node src/app.js` (يعمل على 127.0.0.1:3100/api؛ `/api/health` → `{"ok":true}`).
- بديل Caddy محلياً: خادم Python صغير على :3210 يقدّم `site/out` على `/`، و`portal/public` على `/portal/*`، ويمرّر `/api/*` إلى :3100 مع `Sec-Fetch-Site: same-origin` (المنصة تفحصه ضد CSRF). ملاحظة: يلزم فكّ ترميز المسارات (`%5Bslug%5D`) وإلا فشل تحميل chunk صفحات `[slug]`.
- اللقطات: Playwright/Chromium بدقة 2x — ديسكتوب 1440×900 (→ 2880×1800) وجوال 390×844 (→ 780×1688)، 25 لقطة: 12 صفحة موقع + دخول المنصة + 3 تبويبات لوحة (مشاريع/تذاكر/طلبات) × ديسكتوب، و7 جوال + 3 تبويبات.
- بيانات المنصة في اللقطات: حساب تجريبي واحد (demo@example.test / «مدير تجريبي») بلا مشاريع أو تذاكر أو طلبات (العدّادات 0) — لا بيانات حقيقية.
- الطمس: رقم واتساب في `/contact/` (ديسكتوب وجوال) طُمس بـGaussian blur على الزر؛ لم تُلتقط صفحة أخرى تعرض الرقم بارزاً (الفوتر يحمل الرقم بحجم صغير في بعض الصفحات — يُراجع قبل النشر).
- ما لم يعمل: لا شيء فشل. الروابط الحية في الوثائق (gensparkclaw) لا تستجيب من هنا، والدومين alabbasi.tech غير مسجَّل — لذلك التصوير محلي بالكامل.
