alabbasi-pwa | صانع الصور | 2026-09-23 | ready

# مؤسسة العباسي — PWA (alabbasi-pwa) — Technical Sheet

- **Repo:** moain2028/alabbasi-pwa (public) · docs/00-INDEX.md يشير إلى `moain2026/alabbasi-pwa` (يوحَّد)
- **Primary language / stack:** HTML5 + CSS3 + Vanilla JavaScript — **بلا إطار، بلا خطوة بناء، بلا تبعيات npm، بلا CDN JS** (لا package.json في المستودع) · Service Worker + Web App Manifest · خط IBM Plex Sans Arabic من Google Fonts (المصدر الخارجي الوحيد، ويُخزَّن في كاش الـ SW) · مولّد هوية بـ Python/PIL (`make_icons.py`) (المصدر: README «المواصفات»، index.html، sw.js)
- **Problem:** مؤسسة خدمات رقمية (تدوير المواقع · الحملات الإعلانية · الأتمتة · الذكاء الاصطناعي) تحتاج صفحة تعريفية عربية RTL بالكامل تُفتح كتطبيق، تعمل دون اتصال، وتُثبَّت على الجوال — على خادم بلا خط إيموجي وبأقل قدر ممكن من الاعتماديات. (README «المواصفات»، «الأيقونات»)
- **Solution / core features:** صفحة واحدة بـ 7 أقسام (الهيرو بمدار دوّار من 6 عقد، 4 خدمات، تدوير المواقع بـ 4 خطوات، 6 حلول ذكاء اصطناعي، 5 مراحل عمل، 3 حالات أعمال، نموذج تواصل بـ 6 حقول وتحقق فوري) + صفحة `offline.html`. Service Worker بثلاث استراتيجيات: precache لـ 7 ملفات أساسية، network-first للصفحات مع رجوع للكاش ثم offline.html، stale-while-revalidate للأصول والخطوط. Manifest بـ `display: standalone` و3 أيقونات (192/512/maskable) و3 اختصارات. لافتة تثبيت مخصصة على `beforeinstallprompt`، شريط «أنت غير متصل» على حدثَي online/offline، أرقام هندية عربية في كل العدّادات. 18 أيقونة SVG مضمّنة بتدرّج مشترك. (index.html، js/app.js، js/icons.js، sw.js، manifest.webmanifest)
- **Architecture notes:** المحتوى كله بيانات في `js/app.js` تُرندَر في DOM عند التحميل (SERVICES/REC/AI/PROC/WORK/MARQ/NODES) — لا HTML مكرّر. `dir="rtl" lang="ar"` على الجذر، `color-scheme: dark`، `theme-color #070b14`. نظام تصميم «aurora» (cyan→indigo→violet + ذهب) بـ 18 متغيّر CSS و5 keyframes و3 نقاط استجابة (1000/768/430px) و`prefers-reduced-motion`. IntersectionObserver للكشف التدريجي وللعدّادات. نموذج التواصل يتحقق محلياً بـ 6 قواعد لكن **لا يُرسل إلى أي خادم** (setTimeout يولّد رقم مرجع وهمي). cache-busting بـ `?v=` على CSS/JS وثابت `V` في sw.js (README يحذّر من نسيانه — حصل فعلاً v1→v2). (js/app.js، css/main.css، sw.js، README «استراتيجية الكاش»)
- **Status:** prototype/beta — صفحة واحدة مكتملة تعمل دون اتصال، لكن النموذج غير مربوط بباكند، والصفحات الداخلية (خدمات مفصّلة، أعمال، مدونة) «معلّقة» بحسب docs/00-INDEX.md، والرابط المباشر لا يستجيب (2026-09-23).
- **Last commit:** 2026-08-11 (`git log -1`) — المستودع 2 commit في يوم واحد (feat ثم fix cache-busting)
- **Live URL:** none — README وdocs يذكران `suppdizl.gensparkclaw.com/abbasi/` لكنه **لا يستجيب** (curl: لا اتصال، 2026-09-23؛ تحقّق منه مدير المنتج في اليوم نفسه) → يُعامل كـ «لا رابط حي»

## الأرقام ومصادرها / Numbers & sources
(قياس 2026-09-23 على نسخة مستنسخة من GitHub، مخدومة محلياً بـ `python3 -m http.server`، Chromium headless عبر Playwright)
| Metric | Value | Source |
|---|---|---|
| التبعيات | **0** — لا package.json، لا node_modules، لا سكربت خارجي | `git ls-files` (19 ملفاً)، index.html: سكربتان محليان فقط |
| خطوة البناء | لا يوجد — الملفات تُنشر كما هي | README «التقنية: بلا build» |
| الملفات في المستودع | 19 (HTML 2 · CSS 1 · JS 2 · SW 1 · manifest 1 · brand 8 · py 1 · md 2 · gitignore) | `git ls-files` |
| حجم الكود المكتوب | 744 سطراً (css 305 · app.js 207 · index 184 · icons.js 48) · 1,049 سطراً مع sw/offline/manifest/make_icons | `wc -l` |
| وزن الصفحة (الأصول النصية) | 56.4 KB خام · **~18.6 KB مضغوط gzip** (index 4.0 · css 5.8 · app.js 5.2 · icons.js 1.8 · sw 1.2 · offline 1.2 · manifest 0.5) | `wc -c` + `gzip -c \| wc -c` |
| أصول الهوية | 8 ملفات · 496 KB (icon-192/512/maskable، favicon svg/png/ico، logo، og) — مولّدة بـ make_icons.py | `du -sk assets/brand` |
| أقسام الصفحة | 7 `<section>` داخل `<main>` | DOM count (pwa-audit.json) |
| البطاقات المرندرة | 13 (4 خدمات + 6 ذكاء اصطناعي + 3 أعمال) | DOM count · docs/00-INDEX.md «13 كارت» |
| الخطوات المرندرة | 9 (4 تدوير + 5 آلية عمل) | DOM count · docs «9 خطوات» |
| عقد المدار في الهيرو | 6 | js/app.js NODES · DOM count |
| الأيقونات SVG المضمّنة | **18** في `js/icons.js` (README يقول 19 — العدّ الفعلي في الكود 18) · 21 عنصر `<svg>` في DOM بعد الرندر | `js/icons.js` P{} · DOM count |
| حقول النموذج | 6 (اسم · جوال · مؤسسة · خدمة · رابط · هدف) بـ 6 قواعد تحقق | index.html #form · js/app.js RULES |
| Service Worker | مسجّل و**activated** على النطاق المحلي · كاش واحد `ab-v2-core` | pwa-audit.json (navigator.serviceWorker) |
| ملفات precache | 7 (`/`, index, offline, css, manifest, app.js, favicon.svg) | sw.js PRECACHE · pwa-audit.json |
| العمل دون اتصال | إعادة تحميل الرئيسية وهي offline → **200 من الـ SW**؛ مسار غير محفوظ offline → **offline.html من الـ SW** | pwa-audit.json (`set_offline(True)` + `from_service_worker`) |
| Manifest | `display: standalone` · `dir: rtl` · `lang: ar` · 3 أيقونات · 3 اختصارات | manifest.webmanifest |
| أخطاء الكونسول أثناء التحميل المتصل | **0** | pwa-audit.json console_errors_online · docs «console errors = 0» |
| متغيّرات CSS / keyframes / نقاط استجابة | 18 · 5 · 3 (1000px · 768px · 430px) + prefers-reduced-motion | `grep` css/main.css |
| سمات aria | 12 في index.html (labels، expanded، controls، live، invalid) | `grep -c aria-` |
| الالتزامات | 2 commit (2026-08-11) | `git log` |
| عدّادات الهيرو «84+ مشروع · 3.4× نمو · 97/100 أداء» وأرقام «أعمالنا» | **بيانات عرض** مكتوبة في HTML/JS (`data-c`, WORK[]) بلا مصدر — **لا تُنقل كأرقام إنجاز** | index.html hero-kpi · js/app.js WORK · تنبيه مدير المنتج |
| Lighthouse PWA | يُستكمل — لا Lighthouse في البيئة؛ استُبدل بفحص فعلي عبر Playwright (تسجيل SW، الكاش، الأوفلاين، لافتة التثبيت) | pwa-audit.json |
| مستخدمون / عملاء | يُستكمل — غير موثّق | — |

## ملاحظات التنظيف / Cleanup notes
- الرابط «المباشر» في README وindex.html (canonical، og:url، JSON-LD) لا يستجيب — يُحدَّث أو يُحذف؛ حتى ذلك: لا رابط حي في أي تصميم.
- docs/00-INDEX.md يذكر `moain2026/alabbasi-pwa` والمستودع المعتمد `moain2028/alabbasi-pwa` — يوحَّد.
- README يقول «19 أيقونة» والكود يحوي 18 — يُصحَّح README (أو تُضاف الأيقونة الناقصة).
- عدّادات الهيرو وأرقام قسم «أعمالنا» بيانات عرض (84+، 3.4×، 97/100، 324ms، 99.9%…) — إن نُشر الموقع فعلياً تُستبدل بأرقام حقيقية أو تُحذف؛ في حزمتنا لا تظهر كأرقام إنجاز.
- نموذج التواصل لا يُرسل شيئاً (محاكاة setTimeout) — docs تضعه «معلّقاً»؛ لا يُروَّج كنموذج يعمل.
- الاعتماد الخارجي الوحيد Google Fonts (preconnect + CSS) — يخالف حرف «بلا CDN» جزئياً (README يقول «بلا CDN **JS**» فهو دقيق)، ويُخزَّن في الـ SW بعد أول تحميل.
- `.gitignore` و`make_icons.py` يوحيان أن الهوية تُولَّد محلياً — assets/brand ملتزمة في المستودع (496 KB) وهذا مقصود للنشر بلا build.
- placeholder النموذج يحوي مثال اسم «أحمد العباسي» ونمط رقم يمني «+967 7XX» — ليس اسم شخص حقيقي ولا رقم حقيقي، لكنه ظاهر في لقطة قسم التواصل.

## اللقطات
`screenshots/` — 25 لقطة حقيقية 2x من النسخة المستنسخة المخدومة محلياً (Playwright + Chromium headless، `scripts/shoot.py`): 9 ديسكتوب 1440×900 (7 أقسام + حالة تحقق النموذج + offline.html) و10 جوال 390×844 (7 أقسام + تحقق النموذج + القائمة المفتوحة + offline.html) و2 صفحة كاملة طويلة و4 لقطات PWA فعلية (لافتة التثبيت، الرئيسية وهي offline جوال/ديسكتوب من الـ SW، صفحة الرجوع offline.html لمسار غير محفوظ). `pwa-audit.json` بجانبها يوثّق نتائج الفحص بالأرقام. لا اسم شخص حقيقي ولا رقم هاتف في أي لقطة.
