hafawa-events-app | صانع العروض | 2026-09-23 | draft

# hafawa-events-app — بحث وتحليل / Research & analysis

> كل رقم عن المشروع من tech.md؛ كل رقم خارجي برابط وتاريخ وصول 2026-09-23. ما لم أقسه قلته صراحة.

## 1) تحليل سوق مختصر / Market snapshot
- **من يشتري هذا:** مؤسسات الضيافة والمناسبات الصغيرة في السعودية (قهوجية وصبّابون، كوش، تأجير جلسات) التي تريد «تطبيقاً» على شاشة الزبون الرئيسية لطلب عرض سعر بلمسة — بلا متجر تطبيقات ولا اشتراك شهري.
- **حجم الفئة (خارجي):** سوق تطبيقات الويب التقدّمية العالمي قُدّر بـ **2.08 مليار دولار في 2024** ويُتوقَّع **21.24 مليار دولار بحلول 2033** بمعدل نمو سنوي مركّب **29.9٪ (2025–2033)** — Grand View Research: https://www.grandviewresearch.com/industry-analysis/progressive-web-apps-pwa-market-report (وصول 2026-09-23). لا أعرف حجم الفئة السعودية تحديداً — «يُستكمل».
- **الحاجة الملموسة في المشروع نفسه:** موقع العلامة (hafawa-riyadh-events، 32 صفحة) موجود للبحث والتصفّح؛ التطبيق يغطّي مسار «افتح → اطلب» من الشاشة الرئيسية (brief.ar «المشكلة»).

## 2) ثلاث بدائل / منافسون حقيقيون
| البديل | ما يقدّمه | التكلفة المنشورة (وصول 2026-09-23) | المصدر |
|---|---|---|---|
| **Glide** (GlideOS) | بناء تطبيق بلا كود من جدول بيانات، يُنشر كـ PWA | Free $0 (مشروعان/10 مشاريع محدودة الرصيد) · Basic $25/شهر · Plus $50 · Pro $125 · Business من $199/شهر سنوياً (30 مستخدماً، $5 لكل مستخدم إضافي، 5,000 تحديث/شهر ثم $0.02) | https://www.glideapps.com/pricing · https://bilt.me/blog/glide-pricing |
| **Bubble** | منصّة بلا كود لتطبيقات ويب/جوال كاملة بقاعدة بيانات | Starter $29/شهر (175K وحدة عمل) · Growth $119–129 · Team $349–399 — تختلف الأرقام بين مصادر 2026؛ صفحة Bubble الرسمية لم تُعد الجدول لأداتي | https://bubble.io/pricing · https://goodspeed.studio/blog/understanding-bubble-new-pricing-model · https://vp0.com/blogs/bubble-pricing-plans-2026 |
| **Wix Branded App** | تطبيق أصلي بعلامة العميل على App Store/Google Play من موقع Wix | خطة Mobile App Premium شهرية/سنوية (السعر يُعرض داخل الحساب فقط) **+ رسوم مطوّر Apple وGoogle غير مشمولة** | https://support.wix.com/en/article/wix-mobile-apps-purchasing-a-mobile-app-premium-plan-for-your-own-app |

## 3) التموضع / Positioning
- **ماذا يقول المنافس:** «ابنِ تطبيقك بلا كود في دقائق» (Glide/Bubble)، «تطبيقك على المتجرين» (Wix). كلها اشتراك شهري، وبياناتك على منصّتهم، وWix يضيف رسوم متجرين.
- **أين يتفوّق المشروع (من tech.md فقط):**
  - **صفر اشتراك وصفر تبعية:** ملفات HTML/CSS/JS خام (47.6 + 67.9 + 13.5 KB) تُستضاف على أي خادم ثابت.
  - **خفيف مقيس:** FCP 324 ms على جوال محلي، الكود مضغوطاً 28.4 KB، 27 طلباً/562 KB للصفحة كاملة.
  - **يعمل بلا إنترنت فعلاً:** Service Worker يخبّئ 22 ملفاً ويسقط إلى offline.html (مُختبَر بـ set_offline).
  - **تثبيت بلا متجر:** manifest standalone + اختصاران (عرض سعر / الضيافة) + شريط تثبيت beforeinstallprompt.
  - **RTL وعربي أصيل:** 43 سمة aria، أصغر خط 12px، 7 بلوكات prefers-reduced-motion.
- **أين يتفوّق المنافس (صريح):** لوحة إدارة وقاعدة بيانات وتحليلات وإشعارات Push — المشروع لا يملك أياً منها؛ هو واجهة طلب وليس نظاماً.

## 4) الكلمات المفتاحية
**AR (10):** تطبيق ضيافة الرياض · قهوجية وصبابين الرياض · كوش أفراح الرياض · تأجير جلسات عربية · تعهد حفلات الرياض · طلب عرض سعر ضيافة · تطبيق ويب تقدمي عربي · تطبيق بدون متجر · تطبيق يعمل بدون إنترنت · حفاوة للأفراح
**EN (10):** progressive web app Riyadh · hospitality PWA Saudi · events catering app Riyadh · Arabic coffee service Riyadh · wedding kosha Riyadh · installable web app no app store · offline-first business app · vanilla JS PWA · RTL progressive web app · quote request app

## 5) ثلاث زوايا محتوى
1. **«تطبيق بلا متجر»:** كيف يُثبَّت زبونك التطبيق من المتصفّح خلال ثانيتين — لقطة شريط التثبيت + صفحة الأوفلاين.
2. **«28.4 KB مقابل اشتراك شهري»:** مقارنة صريحة بتكلفة Glide/Bubble/Wix السنوية مقابل ملفات ثابتة تُستضاف بمجّان تقريباً.
3. **«القياس قبل الادّعاء»:** مجلد audit/ في المستودع فيه تدقيق مستقل كشف 3 أخطاء في ادّعاءات المطوّر وصحّح أحدها (أرضية الخط 8px → 13px) — درس في الأمانة الهندسية.

## 6) فجوات صريحة / Gaps
- **README لا يصف المشروع** (منسوخ من keif-aldiafa-mobile-ui) — أول ما يراه زائر GitHub خاطئ.
- **خلل تخطيط على الشاشات >520px:** شريط البلاطات يدفع إطار الهاتف خارج الشاشة (x=−809 عند 1440px). إصلاحه سطران CSS. **لقطات الديسكتوب في هذه الحزمة مأخوذة بتصحيح CSS للتصوير فقط (4 قواعد، مُعلَنة في SOURCES) — الموقع ليس هكذا أصلاً.**
- **لا رابط حي مؤكَّد؛** عنوان JSON-LD يشير إلى VM مؤقت لا يستجيب.
- **خطوط Google من CDN (11 طلباً خارجياً)** — تناقض «يعمل بلا إنترنت»: بلا شبكة تسقط الخطوط إلى النظام.
- **لا نموذج حجز فعلي:** «اطلب عرض سعر» = زرّا واتساب/اتصال؛ لا حقول ولا تخزين طلبات.
- **صور المعرض مولّدة بالذكاء الاصطناعي** (assets/gen) — يجب استبدالها بصور تنفيذ حقيقية قبل أي استخدام تجاري.
- **بيانات حساسة في الكود:** رقم هاتف حقيقي وبريد واسم قانوني في JSON-LD/الروابط.
- **لا اختبارات، لا CI، لا LICENSE، 7 commits في يوم واحد ثم توقّف (2026-08-09).**
- **~1.5 MB أصول ميتة** (assets/logo/emblem-*) + manifest.json مكرّر.

## 7) المصادر
- tech.md (هذه الحزمة) — كل أرقام المشروع.
- Grand View Research, PWA market report — https://www.grandviewresearch.com/industry-analysis/progressive-web-apps-pwa-market-report — 2026-09-23
- Glide pricing — https://www.glideapps.com/pricing — 2026-09-23 · Bilt blog Glide pricing — https://bilt.me/blog/glide-pricing — 2026-09-23
- Bubble pricing — https://bubble.io/pricing (الجدول لم يُحمَّل) · https://goodspeed.studio/blog/understanding-bubble-new-pricing-model · https://vp0.com/blogs/bubble-pricing-plans-2026 — 2026-09-23
- Wix Mobile App Premium — https://support.wix.com/en/article/wix-mobile-apps-purchasing-a-mobile-app-premium-plan-for-your-own-app — 2026-09-23
- audit/v5-verify.md في المستودع (تدقيق مستقل 2026-08-09).

---
### English summary
Target buyer: small Saudi hospitality/events firms that want an installable "app" for one-tap quote requests without an app store or subscription. Global PWA market: USD 2.08B (2024) → 21.24B (2033), 29.9% CAGR (Grand View Research, accessed 2026-09-23). Alternatives: Glide ($0–$199+/mo), Bubble ($29–$399/mo, figures vary by source), Wix Branded App (monthly plan + Apple/Google developer fees). Project edge (tech.md): zero subscription, 28.4 KB gzipped code, FCP 324 ms, 22 files cached offline with a real offline fallback, install without a store, native RTL. Gaps: wrong README, >520px layout bug, no confirmed live URL, Google Fonts from CDN, no real form/back-end, AI-generated gallery, sensitive data in code, no tests/CI/license.
