royal-coffee-hospitality | مخطط التسويق | 2026-09-23 | final

# royal-coffee-hospitality — القهوة الملكية (ROYAL COFFEE) — Technical Sheet

- **Repo:** moain2028/royal-coffee-hospitality (public) · 6 commits · 226 ملفاً متعقَّباً · آخر commit 2026-08-21 (`7a60aa4`)
- **Primary language / stack:** TypeScript · Hono 4.13 + hono/jsx (SSR) · Vite 8 · Wrangler 4 · Cloudflare Pages/Workers (هدف بديل: Vercel Edge عبر `BUILD_TARGET`) · CSS خالص · Vanilla JS
- **Problem:** موقع ضيافة وقهوجيين سعودي قديم (15 صفحة على GitHub Pages) بلا هوية موحّدة ولا SEO مهيكل ولا تجربة جوال — الفئة 95% جوال (README «الأصل» + DIAFA_ANALYSIS §8)
- **Solution / core features:** إعادة بناء SSR على الحافة بهوية Onyx + Gold وRTL أصيل؛ طبقة بيانات واحدة `src/data.ts` + `src/cities.ts` تولّد 73 صفحة (8 خدمات، 6 مناسبات، 8 تصنيفات قائمة بـ 71 صنفاً، أسعار، FAQ، 10 مدن + صفحات تركيبية خدمة×مدينة)، 49 أيقونة SVG يدوية، 13 بانياً لـ JSON-LD، نموذج حجز → رسالة واتساب، قائمة جوال Bottom Sheet، صفحة QR/سوشيال ثلاثية الأبعاد
- **Architecture notes:** `data.ts`/`cities.ts` → `views.tsx` (الأقسام) → `layout.tsx` (القشرة + SEO) → `index.tsx` (18 مسار Hono + robots + sitemap + 404) → HTML على الحافة. لا قاعدة بيانات ولا حالة خادم. رؤوس أمان وتخزين في `public/_headers` و`vercel.json`
- **Status:** prototype مكتمل محلياً — غير منشور (README «النشر»: يعمل محلياً ❌ لم يُنشر)
- **Last commit:** 2026-08-21
- **Live URL:** none

## الأرقام ومصادرها / Numbers & sources
| Metric | Value | Source |
|---|---|---|
| الصفحات في sitemap | 73 عنواناً | `curl /sitemap.xml` من التشغيل المحلي 2026-09-23 (73 `<loc>`) · README الجولة 4 «كل الـ73 رابطاً» |
| مسارات Hono | 18 `app.get` | `src/index.tsx` (grep) |
| الخدمات | 8 | `src/data.ts` SERVICES |
| المناسبات | 6 | `src/data.ts` OCCASIONS |
| تصنيفات القائمة / الأصناف | 8 تصنيفات · 71 صنفاً | `src/data.ts` MENU (عدّ `{ n:`) |
| المدن | 10 | `src/cities.ts` CITIES |
| الأيقونات SVG اليدوية | 49 | `src/icons.tsx` (عدّ `: S(`) |
| بانيات JSON-LD | 13 | `src/ld.ts` (export) — README يقول 11 في جولة سابقة؛ العدد الحالي 13 |
| حجم الـWorker | 179.65 kB · gzip 52.59 kB | `npm run build` 2026-09-23 (مطابق لـ README الجولة 5) |
| CSS | 82.3 kB خام · 17.7 kB gzip | `public/static/style.css` + gzip -c (مطابق README) |
| JS العميل | 16.1 kB خام · 4.8 kB gzip | `public/static/app.js` + gzip -c (مطابق README) |
| الصور | 204 ملفاً (198 WebP) · 12.8 MB إجمالاً | `public/static/img` (du) — README القديم «21 أصلاً 936 KB» يعود لجولة أولى |
| صورة الهيرو | جوال 23 KB · ديسكتوب 72 KB | README الجولة 5 §2 و§6 |
| مكتبات وقت التشغيل | صفر (dependency واحدة: hono) | `package.json` |
| طلبات خارجية | 1 (Google Fonts: Amiri + Tajawal) | `src/layout.tsx` سطر 61–65 |
| تجاوز أفقي | 0 على 32 لقطة (16 صفحة × 390/1440) | فحص Playwright 2026-09-23 (`_meta.json` overflowX=0) — يطابق README |
| معايير فهرسة Google | 73/73 · issues 0 | README الجولة 4 و5 (`qa/seo.py`) — السكربت غير موجود في المستودع، لا يمكن إعادة التشغيل |
| أهداف اللمس | 0 مقصوص · 0 تحت 44px (13 مشهداً) | README الجولة 4 (`qa/btn.py`) — غير قابل لإعادة التشغيل |
| اختبار المسارات | 68/68 | README الجولة 5 (`routes.sh`) — غير موجود في المستودع |
| Tests | لا اختبارات وحدات؛ لا CI | فحص المستودع |
| Users / clients | غير موثّق | — |

## الحالة الفعلية للمحتوى
- **بيانات التواصل placeholders:** `+966 50 000 0000` و`hello@example.com` وروابط سوشيال عامة (README ⚠️ + `src/data.ts` BRAND). تظهر في اللقطات — ليست بيانات حقيقية، لذا لا تحتاج طمساً لكن **لا تُستخدم كأرقام**.
- **أرقام الهيرو داخل الموقع** (+6500 مناسبة، +60 صنف، 10 مدن، 24/7) وREVIEWS و«أكثر من 70 صنفاً بصور حقيقية» في عناوين الصفحات: محتوى تسويقي في `data.ts`، ليست مقاييس — لا تُستخدم كإنجاز. (10 مدن و71 صنفاً مؤكَّدة من الكود فقط كعدد كيانات.)
- **الصور:** مولّدة أصلاً حسب README («مُولَّدة أصلاً، مُدقّقة آلياً») — أي أن «صور حقيقية من مناسباتنا» في عنوان المعرض وصف داخل الموقع لا يُعاد على تصاميمنا.

## التشغيل والتصوير (2026-09-23 — مخطط التسويق)
- `npm install` → `npm run build` (ناجح، 89ms) → `npx wrangler pages dev dist --port 3000` (Ready). لم يحتج أي متغير بيئة.
- Playwright Chromium headless، `reduced_motion=reduce`، locale ar-SA، DPR 2: 16 مساراً × (1440×900 + 390×844) = 32 لقطة PNG في `screenshots/`. المسارات: الرئيسية، الخدمات، خدمة (qahwajiin)، المناسبات، مناسبة (weddings)، القائمة، القائمة/coffee، الأسعار، المعرض، عن، FAQ، المدن، مدينة (riyadh)، تواصل، social، 404.
- ملاحظة: README «مسارات الموقع» (7 صفحات، `/services/men`…) قديم — المسارات الحالية `qahwajiin/qahwajiat/zamzam/offerings/buffet/equipment/royal/extras`؛ `/services/men` يعطي 404 مصمّمة.

## ملاحظات التنظيف / Cleanup notes
- README يجمع 5 جولات متعاقبة بأرقام متضاربة (7 صفحات → 73؛ 21 صورة/936 KB → 204/12.8 MB؛ 11 → 13 بانياً؛ 40+ → 49 أيقونة). يحتاج توحيداً في نسخة واحدة حالية.
- سكربتات QA المذكورة (`qa/seo.py`، `qa/btn.py`، `qa/cine.py`، `routes.sh`) غير موجودة في المستودع — أرقامها من README فقط.
- «GitHub: لم يُربط بعد» في README — صار مربوطاً (moain2028).
- الصور 12.8 MB في المستودع رغم أن كل صفحة تحمّل القليل — يمكن نقلها لـ R2/CDN.
- `DIAFA_ANALYSIS.md` يقارن keifaldiafa.com وasoulaldiafa.com كأصل للتحليل — كلاهما من مشاريع معين (keif-aldiafa-web، osoul-aldiafa في portfolio-hub)؛ لا يُقدَّمان كمنافسين.
