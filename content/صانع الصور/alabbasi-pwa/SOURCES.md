alabbasi-pwa | صانع الصور | 2026-09-23 | ready

# مصادر كل نص ورقم وصورة في الحزمة

المصدر الأصلي الوحيد: مستودع github.com/moain2028/alabbasi-pwa (commit f766852، 2026-08-11) مستنسخاً ومقيساً محلياً 2026-09-23 (project/tech.md) + فحص PWA فعلي عبر Playwright (project/screenshots/pwa-audit.json). لا رقم من README لم يُقَس محلياً إلا ما أُشير إليه.

## A. التصاميم (24 PNG) + B. الكاروسيل/البطاقة/البانر (14 PNG)
| العنصر | المصدر |
|---|---|
| العنوان «مؤسسة العباسي» / "Alabbasi" | README H1 · manifest name/short_name · JSON-LD alternateName "Alabbasi" |
| اسم المستودع alabbasi-pwa | التكليف |
| الجملة التعريفية «تطبيق ويب تقدّمي يعمل دون اتصال بصفر تبعيات» / "An offline-first company PWA with zero dependencies" | brief.ar/en.md H1 ← README «المواصفات» (PWA · بلا إطار/build/CDN JS) + tech.md التبعيات |
| الوصف (HTML/CSS/JS خام، RTL بأرقام هندية، SW بثلاث استراتيجيات، يُثبَّت كتطبيق، 18 أيقونة SVG) | brief الحل ← README المواصفات/استراتيجية الكاش · sw.js · manifest · js/icons.js (18 مفتاحاً في P) |
| 0 تبعية · بلا خطوة بناء | tech.md: لا package.json في `git ls-files` (19 ملفاً)؛ index.html سكربتان محليان فقط؛ README «بلا build» |
| 18.6 KB كل الأصول النصية مضغوطة | tech.md: `gzip -c | wc -c` لـ index 4007 + css 5803 + app.js 5226 + icons.js 1843 + sw 1163 + offline 1151 + manifest 542 = 19,735 B ≈ 18.6 KiB (مقرّب لأسفل) |
| 7 ملفات في الكاش المسبق | sw.js PRECACHE (7 عناصر) · pwa-audit.json precached_core (7) |
| 0 أخطاء في الكونسول | pwa-audit.json console_errors_online = [] · docs/00-INDEX.md «console errors = 0» |
| 19 ملفاً في المستودع | `git ls-files | wc -l` |
| السطر الخافت «يعمل دون اتصال · قابل للتثبيت · RTL كامل · 0 أخطاء في الكونسول» | pwa-audit.json (offline_reload from_sw=true، manifest display standalone، html dir=rtl، console_errors_online=[]) |
| التاجات Vanilla JS · Service Worker · Web Manifest · CSS3 | README «التقنية» · sw.js · manifest.webmanifest · css/main.css |
| شارة الشريحة «شركات» / "Companies" ولونها #3B82F6 | التكليف + 02-brand/README.md |
| الفوتر github.com/moain2028/alabbasi-pwa (يسار) و«PWA · offline-first · 0 deps» (يمين) | التكليف (مستودع عام) · tech.md؛ لا رابط حي لأن الرابط المباشر لا يستجيب (links.md) |
| شريط عنوان إطار المتصفح «alabbasi-pwa · offline-ready» | تسمية وصفية لا نطاقاً حياً |
| كاروسيل 1 (المشكلة) | brief المشكلة ← README المواصفات/الأيقونات |
| كاروسيل 2 (الحل) | brief الحل |
| كاروسيل 3 (precache 7 · network-first → كاش → offline.html · SWR · 7 أقسام من بيانات واحدة · 18 SVG) | sw.js · README استراتيجية الكاش · js/app.js · js/icons.js |
| كاروسيل 4 الأرقام (0 · 18.6 KB · 7 · 0) | tech.md الأرقام ومصادرها |
| كاروسيل 5 الدعوة «موقع شركتك يحتاج إنترنت قوياً ليظهر؟ راسلني…» | brief.ar/en للتواصل |
| بطاقة الرقم الواحد «0 تبعية» + «بلا خطوة بناء · بلا CDN JS · يعمل دون اتصال» + سطر 19 ملفاً/18.6 KB/7/0 | tech.md |
| الاسم النصّي «معين العباسي / Moain Al-Abbasi» في نسخة logo فقط | معيار v2 §A |
| النص الخافت #A3B1C0 | معيار v2 (تحديث 2026-09-23) |

## الصور (كلها لقطات حقيقية من تشغيل محلي للمستودع — لا صورة مولّدة أُضيفت)
| الملف | ماذا يعرض | كيف أُخذ |
|---|---|---|
| desktop-02-services.png | قسم الخدمات (4 بطاقات) 1440×900 @2x — لقطة الديسكتوب الأساسية في A/B/C | shoot.py desktop، http.server محلي، Playwright/Chromium |
| pwa-05-install-banner-services.png | لافتة التثبيت الحقيقية (app.js) فوق قسم الخدمات 390×844 @2x — لقطة الجوال الأساسية | shoot.py pwa: إطلاق beforeinstallprompt ثم التمرير إلى #services |
| pwa-06-offline-services.png | شريط «أنت غير متصل — تُعرض نسخة محفوظة» + الخدمات، والصفحة مُعادة من الـ SW وهي offline | shoot.py pwa: set_offline(True) → reload (200 from_service_worker) |
| pwa-03-offline-fallback.png | offline.html مُعادة من الـ SW لمسار غير محفوظ | shoot.py pwa: goto مسار غير موجود وهي offline |
| mobile-10-offline-page.png | offline.html مباشرة (متصل) | shoot.py mobile |
| desktop-04-ai.png · desktop-07-contact.png | قسم الذكاء الاصطناعي · نموذج التواصل | shoot.py desktop |
| بقية الـ 27 لقطة في project/screenshots | 7 أقسام ديسكتوب وجوال + تحقق النموذج + القائمة المفتوحة + صفحتان كاملتان + install/offline | shoot.py (الوسيط الثاني desktop/mobile/pwa) |
| **لم تُستخدم عمداً كلقطة رئيسية**: desktop-01-hero / mobile-01-hero / pwa-01-install-banner / pwa-02-offline-home | تعرض عدّادات الهيرو (84+ · 3.4× · 97/100) وهي بيانات عرض — موجودة في project/screenshots للتوثيق فقط | تنبيه مدير المنتج + tech.md |

## C. الفيديو
video/alabbasi-pwa-reel-ar.mp4 و-en.mp4 (18.0 ث، 1080×1920، بلا شعار، ساحة أمان 12%): غلاف + 3 مشاهد + أرقام + دعوة. كل نص من brief/tech.md؛ اللقطات من الجدول أعلاه (services، install-banner-services، ai، offline-services، offline-fallback، offline-page). لا مشهد خطأ. الموسيقى 02-brand/scripts/reels/bgm-tech-minimal.mp3. الأداة tools/reel_nologo.py + reel-ar/en.json.

## D. الشروحات
alabbasi-pwa-explainer.ar.md (551 كلمة) و.en.md (≈560) + خلاصة 5 نقاط — كل فقرة تحمل مصدرها بين قوسين (README/tech.md/sw.js/manifest/pwa-audit.json).

## E. البحث
alabbasi-pwa-research.md — 3 بدائل بروابط فُتحت 2026-09-23 (Wix app-market + مركز مساعدة Wix، Webflow + منتداه، PWABuilder + GitHub)، تموضع، 10+10 كلمات، 3 زوايا، فجوات صريحة. ادعاءات البدائل من صفحاتها؛ ادعاءات مشروعنا من tech.md فقط.

## F. نصوص النشر
alabbasi-pwa-copy.ar/en.md — LinkedIn 96/≈110 كلمة، X 210/238 حرفاً، IG 91/119 كلمة، نص الريل كما رُندر. draft حتى ختم المحرر.

## التباين (WCAG)
Sand/Navy 13.4 · Mist/Navy 11.3 · Amber/Navy 7.2 · Ink/Amber 8.9 · #A3B1C0/Navy ≈ 7.0 · Ink/#3B82F6 (شارة الشريحة) ≈ 4.6 — كلها AA فأعلى.

## ما لم يُعرض عمداً
- عدّادات الهيرو «84+ مشروع · 3.4× نمو · 97/100 أداء» وأرقام «أعمالنا» (324ms، 99.9%…) — بيانات عرض في index.html/js/app.js بلا مصدر؛ غائبة عن كل تصميم ونص.
- الرابط «المباشر» suppdizl.gensparkclaw.com/abbasi/ — لا يستجيب؛ لا يُعرض كرابط حي (canonical/og:url في الكود تشير إليه).
- أي اسم شخص أو رقم هاتف: README لا يحوي أيّاً منهما؛ placeholder النموذج «أحمد العباسي» و«+967 7XX XXX XXX» مثالان لا بيانات حقيقية، ويظهران في لقطة قسم التواصل فقط بحجم صغير.
- عبارة «19 أيقونة» من README — الكود يحوي 18، فاعتُمد 18.
- Lighthouse PWA — غير متاح في البيئة؛ استُبدل بفحص Playwright موثّق.
