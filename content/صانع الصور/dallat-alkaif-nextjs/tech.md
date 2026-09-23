dallat-alkaif-nextjs | صانع الصور | 2026-09-23 | ready

# دلة الكيف (Dallat Al-Kaif) — Technical Sheet

- **Repo:** moain2028/dallat-alkaif-nextjs (public) · README يشير إلى moain2026/dallat-alkaif-nextjs في أمر الاستنساخ
- **Primary language / stack:** TypeScript strict · Next.js 16.3.0 (App Router, Turbopack) · React 19.2.8 · CSS Modules + `@layer` وتوكنات — بلا Tailwind · `output: 'export'` (HTML ثابت) · خطوط محلية Amiri + Almarai (12 woff2) (المصدر: package.json، next.config.ts، README)
- **Problem:** شركة ضيافة عربية فاخرة تخدم جنوب المملكة (عسير · جازان · نجران · الباحة · الطائف) تحتاج موقعاً تعريفياً عربياً RTL بالكامل يحوّل الزائر إلى واتساب، بصدق مطلق: لا مدن خارج النطاق، لا إحصائيات مختلقة، لا شعارات شركاء، لا أسعار رقمية. (README «نظرة عامة» و«قواعد المحتوى»)
- **Solution / core features:** 16 صفحة HTML ثابتة: الرئيسية، كتالوج 8 خدمات وصفحة SSG لكل خدمة (`generateStaticParams` + `dynamicParams=false` ⇒ 404 حقيقي لأي slug مجهول)، 3 باقات (فضية/ذهبية/ملكية) بنص «السعر حسب المناسبة»، نموذج حجز مُتحقَّق منه، معرض أعمال، 404 عربية. مصدر حقيقة واحد `lib/site.ts` لكل الثوابت (العلامة، الواتساب، 8 خدمات، 13 مدينة، 5 مناطق، المعرض). تنقّل يتبدّل عند 860px: شريط سفلي (جوال) ⇄ قائمة علوية. (README «المسارات» و«مصدر الحقيقة الواحد»، lib/site.ts)
- **Architecture notes:** تصدير ثابت لا SSR (ADR-001)؛ CSS Modules لا Tailwind لأن كلاساته فيزيائية تقاوم RTL (ADR-002)؛ خطوط محلية لا CDN (ADR-003)؛ مُحمِّل صور مخصص يضيف basePath لأن التصدير الثابت لا يطبّقه على الصور (ADR-004). خصائص CSS منطقية حصراً، قواعد احتياطية خارج `@layer` لمتصفحات Android WebView/Chrome < 99، كل الأحجام `clamp()` من 360→1440px، أهداف لمس 48px (WCAG 2.2 SC 2.5.8)، لا `maximum-scale` (WCAG 2.1 SC 1.4.4)، `prefers-reduced-motion`، `aria-expanded` وaria-live في النموذج. (README «نظام التصميم»، «المعايير الهندسية»، «الوصولية»، ADR)
- **Status:** beta — يُبنى وينشر ثابتاً، لكن كل الصور الحالية مولّدة بالذكاء الاصطناعي، والأسعار وسنة التأسيس وعدد المناسبات والنطاق النهائي «ما زال مطلوباً» من المالك. (README «ما زال مطلوباً»)
- **Last commit:** 2026-08-07 (`git log -1`) — المستودع 2 commit (2026-08-06 → 2026-08-07)
- **Live URL:** none — `SITE_URL` الافتراضي في lib/site.ts هو `https://dallat-alkaif.com` (غير مُتحقَّق منه؛ README يقول النطاق النهائي لم يُحدَّد). يُنشر حالياً على مسار فرعي `/dallat` (next.config.ts basePath)

## الأرقام ومصادرها / Numbers & sources
(قياس 2026-09-23 على نسخة مستنسخة من GitHub، Node 22.23 / npm 10.9)
| Metric | Value | Source |
|---|---|---|
| الإطار | Next.js 16.3.0 · React 19.2.8 · TypeScript ^5 | package.json |
| البناء | `next build` ينجح — 16/16 صفحة ثابتة (6 Static + 8 SSG + 404 + _not-found) في 673 ms توليد | تشغيل محلي 2026-09-23 (سجل البناء) |
| فحص الأنواع | `npx tsc --noEmit` → نظيف (exit 0) | تشغيل محلي |
| اللينت | `npx eslint .` → نظيف (exit 0) | تشغيل محلي |
| بوابات الجودة الأربع | خصائص فيزيائية 0 · tracking سالب 0 · مدن خارج النطاق/انتحال علامات 0 · رقم جوال خارج lib/site.ts 0 | أوامر grep من README «بوابات الجودة»، تشغيل محلي |
| الصفحات | 16 ملف HTML في `out/` | `find out -name '*.html'` |
| الخدمات | 8 (coffee · sweets · hospitality · events · zamzam · art · equipment · coverage) | lib/site.ts SERVICES |
| المدن / المناطق | 13 مدينة · 5 مناطق جنوبية | lib/site.ts CITIES / REGIONS |
| الباقات | 3 (فضية · ذهبية مميّزة · ملكية) — بلا أسعار رقمية | app/packages/page.tsx، README |
| الخطوط | 12 ملف woff2 محلي (Amiri + Almarai، عربي/لاتيني منفصلان) · 452 KB · 12 `@font-face` | public/fonts، app/fonts.css |
| الصور | 12 ملف في public/img · 972 KB — **كلها مولّدة بالذكاء الاصطناعي** | public/img، README «ما زال مطلوباً» |
| حجم الكود | 34 ملف ts/tsx · 17 ملف css · 6,065 سطراً | `wc -l` محلياً |
| أكبر ملف | sections.module.css — 691 سطراً (يتجاوز معيار README «ملفات ≤ 400 سطر») | `wc -l` |
| حجم المخرجات | out/ = 5.4 MB · JS chunks 636 KB | `du` |
| الالتزامات | 2 commit (2026-08-06، 2026-08-07) | `git log` |
| أهداف اللمس / ارتفاع السطر | `--tap: 48px` · `--lh-ar: 1.9` | app/globals.css:63,67 |
| اختبارات آلية | لا يوجد إطار اختبار (لا Vitest/Playwright في package.json) — البوابات هي tsc + eslint + grep + بناء | package.json |
| مستخدمون / عملاء / مناسبات | يُستكمل — README يمنع أي إحصائية لأن المالك لم يوفّرها | README «قواعد المحتوى» |
| أداء (LCP/CLS) | يُستكمل — لا قياس موثّق في المستودع ولا نطاق حي لقياسه | — |

## ملاحظات التنظيف / Cleanup notes
- README يذكر رابط الاستنساخ `moain2026/dallat-alkaif-nextjs` بينما المستودع العام المعتمد `moain2028/dallat-alkaif-nextjs` — يوحَّد.
- رقم الواتساب/الجوال مكتوب صريحاً في README (جدول «نظرة عامة») وفي lib/site.ts ويظهر في الواجهة — طُمس في كل اللقطات هنا، ولا يظهر على أي تصميم.
- كل الصور مولّدة بالذكاء الاصطناعي (README نفسه) — في التصاميم استُخدمت لقطات الموقع الحقيقية كما تُعرض، لا الصور منفردة، مع الإشارة إلى ذلك في SOURCES.
- sections.module.css بـ 691 سطراً يخالف معيار «≤ 400 سطر» المذكور في README.
- بقايا `create-next-app` في public/ (file.svg · window.svg · globe.svg · vercel.svg) غير مستخدمة على الأرجح.
- `SITE_URL` الافتراضي `dallat-alkaif.com` غير مُتحقَّق كنطاق فعلي — لا يُذكر كرابط حي.
- الاسم القديم «كيف الضيافة» ممنوع في هذا المشروع (README) — لا يُربط بمشروع keif-aldiafa-web في أي نص تسويقي.

## اللقطات
`screenshots/` — 18 لقطة حقيقية من البناء الثابت المحلي (`npm run build` → `out/` مخدوم على `/dallat` بـ http.server، Chromium headless عبر Playwright، 2x): 8 ديسكتوب 1440×900 + 8 جوال 390×844 (الرئيسية، الخدمات، القهوة المختصة، خدمات الضيافة، تغطية الجنوب، الباقات، الحجز، المعرض) + صفحتان كاملتان طويلتان. رقم الواتساب مطموس قبل التصوير (`scripts/shoot.py`). طريقة العمل في `how-i-worked.md`.
