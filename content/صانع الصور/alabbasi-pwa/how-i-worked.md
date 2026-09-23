alabbasi-pwa | صانع الصور | 2026-09-23 | ready

# كيف أُنجز هذا المجلد (لمن يكمل بعدي)

1. الاستنساخ: `git clone --filter=blob:none --single-branch https://github.com/moain2028/alabbasi-pwa` (عام، 19 ملفاً، لا package.json).
2. التشغيل: لا build — `python3 -m http.server 8791` من جذر المستودع؛ كل المسارات الثمانية الأساسية 200.
3. التصوير: Playwright + Chromium headless (`scripts/shoot.py <out> desktop|mobile|pwa`)، معامل 2x، سياقان 1440×900 و390×844. قبل كل لقطة يُمرَّر المستند بالكامل لتشغيل العدّادات والكشف التدريجي، ثم تُضاف فئة `in` لكل `.rv` يدوياً (IntersectionObserver لا يلتقط دائماً في الوضع الخفي). لقطات إضافية: حالة تحقق النموذج (إرسال فارغ)، القائمة المفتوحة على الجوال، offline.html.
4. فحص PWA فعلي (`shoot.py <out> pwa`): تسجيل الـ SW وحالته، مفاتيح الكاش وقائمة precache، قراءة manifest، إطلاق `beforeinstallprompt` لإظهار لافتة التثبيت الحقيقية من app.js، ثم `context.set_offline(True)` وإعادة تحميل الرئيسية (200 من الـ SW) وطلب مسار غير محفوظ (offline.html من الـ SW). النتائج في `screenshots/pwa-audit.json`.
5. الكتابة: tech.md من README + index.html + js/app.js + sw.js + manifest + قياسات `wc`/`gzip`/`du`/`git ls-files` على النسخة المستنسخة + pwa-audit.json؛ brief من tech.md فقط.

ما بقي: الرابط الحي، ربط النموذج بباكند، الصفحات الداخلية — كلها «معلّقة» في docs/00-INDEX.md. Lighthouse غير متاح في البيئة — يُستكمل إن أراد المالك رقماً رسمياً.
