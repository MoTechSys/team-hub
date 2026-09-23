alabbasi-pwa | صانع الصور | 2026-09-23 | draft

# مؤسسة العباسي PWA — بحث وتحليل السوق

تاريخ البحث: 2026-09-23 (بحث ويب + فتح صفحات البدائل في اليوم نفسه، كلها 200). ادعاءات البدائل من صفحاتها/منتدياتها؛ ادعاءات مشروعنا من README/tech.md/pwa-audit.json فقط.

## 1. من يشتري هذا
- المشتري النهائي لخدمات المؤسسة: أصحاب شركات ومؤسسات في اليمن والسعودية والإمارات يريدون تدوير موقع قائم أو حملات أو أتمتة (index.html: «نعمل الآن · اليمن · السعودية · الإمارات»، JSON-LD areaServed YE/SA/AE).
- مشتري «المنتج» (طريقة البناء نفسها) لمحفظة معين: شركات تريد صفحة تعريفية عربية تُفتح كتطبيق وتعمل في ضعف الشبكة بلا اشتراك منصة ولا فريق frontend. (brief.ar لمن يفيد)
- حجم الفئة: يُستكمل — لا رقم موثّق. مؤشر كيفي: البحث العربي عن «موقع تعريفي PWA يعمل دون اتصال» يعيد شروحات تقنية (ورشة itqan، siwane) ومنصات بناء مواقع عامة (Canva، Appy Pie)، لا منتجات عربية متخصصة — الفئة شبه فارغة عربياً.

## 2. البدائل والمنافسون (3)
| # | البديل | ماذا يقدّم | حدّه في الأوفلاين/PWA (من مصدره) | الرابط (وصول 2026-09-23) |
|---|---|---|---|---|
| 1 | Wix (بانٍ مواقع) + تطبيق «Convert to App (PWA)» من سوق التطبيقات | صفحات شركات بلا كود، قوالب، استضافة مدمجة | التطبيق الطرفي يعِد بـ«offline functionality» وإشعارات؛ أما تطبيق Wix الأصلي (Branded App) فمركز المساعدة يقول صراحة إنه «يتطلب اتصالاً — لا يمكن استخدامه دون اتصال» | https://www.wix.com/app-market/pwa · https://support.wix.com/en/article/wix-mobile-apps-faqs-about-building-your-own-app |
| 2 | Webflow (بانٍ مواقع احترافي) | تصميم بصري متقدّم، CMS، استضافة | منتدى Webflow: يمكن إضافة manifest لحفظ الموقع على الشاشة الرئيسية لكن «لا يسمح بأي شيء من Service Worker (تشغيل الـ PWA دون اتصال)» لأن الاستضافة لا تخدم ملف SW من الجذر | https://webflow.com/ · https://discourse.webflow.com/t/pwas-on-webflow-hosted-sites/80089 |
| 3 | PWABuilder (Microsoft، مفتوح المصدر) | أداة تغليف موقع قائم إلى PWA/متجر تطبيقات، ومولّد SW/manifest | يفترض موقعاً موجوداً ويُضيف إليه الطبقة؛ لا يبني الصفحة ولا محتواها ولا يحل مشكلة RTL/الأرقام | https://www.pwabuilder.com/ · https://github.com/pwa-builder/PWABuilder |

ظهرت أيضاً بلا فتح صفحاتها: Mobirise (منتداه يشكو «PWA لا يعمل دون اتصال كما ينبغي»)، قوالب PWA على Envato Elements، ودروس Vanilla-JS PWA (LoginRadius، dev.to، MDN js13kGames) — الأخيرة تثبت أن النهج معروف لكنه يُقدَّم كدرس لا كمنتج عربي.

## 3. التموضع
| المحور | ماذا تقول البدائل | أين يتفوّق مشروعنا (من README/tech.md فقط) |
|---|---|---|
| العمل دون اتصال | Wix: التطبيق الأصلي يحتاج اتصالاً؛ Webflow: لا Service Worker على الاستضافة؛ PWABuilder: يضيف SW لموقع موجود | SW مكتوب يدوياً بثلاث استراتيجيات، 7 ملفات precache، والرئيسية تُعاد وهي offline من الـ SW — مقيس فعلياً |
| التبعيات والملكية | اشتراك منصة + استضافة مقيّدة (Wix/Webflow)؛ PWABuilder يعتمد على الموقع الأصلي | 0 تبعية، 19 ملفاً، النشر نسخُ ملفات إلى أي خادم ثابت؛ الملكية كاملة |
| العربية RTL | قوالب غالباً LTR أصلاً تُقلَب يدوياً (غير مُتحقَّق تفصيلياً) | `dir="rtl" lang="ar"` من الجذر، أرقام هندية في كل عدّاد، manifest بـ `dir: rtl`، خط IBM Plex Sans Arabic |
| الأيقونات | إيموجي أو مكتبات أيقونات خارجية | 18 أيقونة SVG مضمّنة بتدرّج مشترك — لا اعتماد على خط إيموجي في الخادم |
| الوزن | صفحات البُناة عادةً مئات KB من JS (غير مقيس هنا) | ~18.6 KB مضغوطة لكل النصوص؛ 5 keyframes وreduced-motion |
| القابلية للتثبيت | Wix عبر تطبيق طرفي؛ Webflow يدوياً؛ PWABuilder نعم | manifest مستقل بـ 3 أيقونات و3 اختصارات ولافتة تثبيت مخصصة — تكافؤ مع PWABuilder، تفوّق على البانِيَين |
| النموذج/الباكند | مدمج في Wix/Webflow | **فجوة**: النموذج يحاكي الإرسال ولا يصل لأي خادم |

## 4. الكلمات المفتاحية
AR (10): تطبيق ويب تقدّمي عربي · موقع شركة يعمل دون اتصال · Service Worker بالعربية · موقع تعريفي بدون إطار · صفحة شركة RTL · تثبيت الموقع كتطبيق · موقع خفيف بلا تبعيات · أيقونات SVG مضمّنة · أرقام هندية في المواقع · تدوير المواقع القديمة
EN (10): vanilla JS PWA company site · offline-first landing page · zero-dependency website · RTL Arabic PWA · service worker caching strategies · installable web app manifest · stale-while-revalidate vs network-first · no-build static site · Eastern Arabic numerals web · Webflow PWA offline alternative

## 5. ثلاث زوايا محتوى
1. «موقع شركة بصفر تبعيات: لماذا لا يحتاج كل شيء إلى إطار» — 19 ملفاً، 744 سطراً، النشر نسخُ ملفات، ولا سلسلة توريد تُراقَب.
2. «ثلاث استراتيجيات كاش في 70 سطراً» — تشريح sw.js: precache/network-first/SWR، وحادثة v1→v2 كدرس عن cache-busting.
3. «العربية أولاً لا ترجمةً»: من `dir="rtl"` إلى الأرقام الهندية إلى أيقونات SVG بدل الإيموجي — قائمة تدقيق لأي صفحة عربية.

## 6. الفجوات (صريحة)
تقنياً: نموذج التواصل غير مربوط بباكند (محاكاة setTimeout)؛ لا اختبارات آلية ولا Lighthouse موثّق؛ اعتماد خارجي واحد (Google Fonts) يخالف روح «بلا CDN» جزئياً؛ README يقول 19 أيقونة والكود 18؛ commitان فقط في يوم واحد. (tech.md)
تسويقياً: الرابط المباشر لا يستجيب فلا رابط حي ولا OG فعّال؛ عدّادات الهيرو وأرقام «أعمالنا» بيانات عرض قد تُقرأ كادعاءات إن نُشر الموقع دون تعديل؛ الصفحات الداخلية معلّقة؛ ازدواج اسم المستودع moain2026/moain2028.

## English summary
Alabbasi PWA is a single-page company profile built in plain HTML/CSS/JS with a hand-written Service Worker, an RTL Arabic manifest and inline SVG icons. Three verified alternatives (accessed 2026-09-23): Wix — whose own help center states its native branded app requires a connection, offline only via a third-party "Convert to App (PWA)" listing; Webflow — whose forum confirms hosted sites cannot run a Service Worker, so no offline; and Microsoft's PWABuilder — which wraps an existing site but builds neither the page nor its Arabic handling. The project's defensible edge, from README/tech.md: zero dependencies and no build, measured offline (home served from the SW, unknown routes to offline.html), 7 precached files, ~18.6 KB gzipped text assets, RTL from the root to numerals to icons. Gaps: the form reaches no backend, no live URL, demo counters in the hero, no automated tests or Lighthouse score, one external font dependency.

## المصادر
- README.md، index.html، js/app.js، js/icons.js، sw.js، manifest.webmanifest، docs/00-INDEX.md — moain2028/alabbasi-pwa (commit f766852، 2026-08-11) + قياسات محلية وفحص Playwright 2026-09-23 (tech.md، pwa-audit.json في هذه الحزمة)
- https://www.wix.com/app-market/pwa — 2026-09-23 (200)
- https://support.wix.com/en/article/wix-mobile-apps-faqs-about-building-your-own-app — 2026-09-23 (200)
- https://webflow.com/ — 2026-09-23 (200) · https://discourse.webflow.com/t/pwas-on-webflow-hosted-sites/80089 — 2026-09-23 (301 → الموضوع)
- https://www.pwabuilder.com/ — 2026-09-23 (200) · https://github.com/pwa-builder/PWABuilder — 2026-09-23 (200)
- ذُكرت بلا تحقق (نتائج بحث 2026-09-23): https://forums.mobirise.com/discussion/31907/ · https://elements.envato.com/web-templates/mobile+app+pwa · https://www.loginradius.com/blog/engineering/build-pwa-using-vanilla-javascript · https://developer.mozilla.org/en-US/docs/Web/Progressive_web_apps/Tutorials/js13kGames/Offline_Service_workers · https://community.itqan.dev/d/38
