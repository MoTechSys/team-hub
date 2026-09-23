espreso | صانع الفيديو | 2026-09-23 | draft

# espreso — بحث السوق والتموضع (مع ملخص EN)

تاريخ الوصول لكل الروابط: 2026-09-23. ادعاءات مشروعنا من tech.md والكود؛ ادعاءات البدائل من الصفحة المذكورة فقط.

## 1) من يشتري هذا
- مقاهٍ ومحامص ومشاريع غذائية صغيرة (1–5 فروع) يديرها المالك، حضورها الرقمي حساب إنستغرام أو «رابط في البايو»، وتريد قائمة وفروعاً وحكاية في موقع يليق بهويتها ويعمل من الهاتف.
- حجم الفئة: يُستكمل — لا رقم رسمي موثوق لعدد المقاهي المستقلة في اليمن/الخليج وجدته في هذا البحث؛ لن يُعرض رقم بلا مصدر.

## 2) ثلاث بدائل حقيقية
| البديل | ما هو | ما يقوله / السعر | الرابط |
|---|---|---|---|
| **Squarespace** | منشئ مواقع بقوالب مطاعم ومقاهٍ (قائمة، حجز، فعاليات) | «ابدأ بقالب مصمَّم احترافياً وأضف قائمتك»؛ الأسعار بالفوترة السنوية: Basic $19 · Core $29 · Plus $49 · Advanced $99 شهرياً | https://www.squarespace.com/tour/restaurant-websites · https://www.squarespace.com/pricing |
| **Wix Restaurants** | تطبيق قوائم داخل منشئ Wix: أقسام وأصناف وأسعار وصور وملصقات غذائية، مع إمكانية إخفاء الأسعار | «أنشئ قوائم بلا حد، أضف أقساماً وأصنافاً بأسمائها وأسعارها» (صفحة الأسعار لم تُقرأ آلياً فلا يُقتبس سعر) | https://www.wix.com/app-market/wix-restaurants-menus-new · https://support.wix.com/en/article/wix-restaurants-setting-up-wix-restaurants-menus-new |
| **Linktree** | صفحة «رابط في البايو» — البديل الفعلي الذي تستخدمه المقاهي الصغيرة بدل الموقع | خطة مجانية دائمة بروابط بلا حد؛ باقات مدفوعة (صفحة الأسعار لم تُظهر أرقاماً آلياً؛ مصدر ثانوي يذكر $5/$9/$24 شهرياً — غير مؤكَّد من المصدر الأول) | https://linktr.ee/s/pricing · https://www.theleap.co/blog/linktree-pricing/ |

## 3) التموضع
- ما يقوله المنافس: Squarespace وWix يبيعان السرعة والقوالب مقابل اشتراك شهري دائم ولغة واحدة أساساً (العربية RTL تحتاج عملاً إضافياً)؛ Linktree يبيع البساطة لكنه صفحة روابط لا موقعاً.
- أين يتفوّق مشروعنا (من tech.md): (أ) صفر اشتراك وصفر تبعيات تشغيل — ملفات ثابتة تُنشر على أي استضافة مجانية؛ (ب) عربي أولاً RTL مع إنجليزية من قاموس واحد؛ (ج) هوية فاخرة مخصّصة بخطوط محلية لا قالب مشترك؛ (د) صور حقيقية من الحساب والفرع مع خط أنابيب AVIF/WebP وLQIP — أداء لا يقدّمه منشئ مواقع بالافتراض؛ (هـ) PWA قابل للتثبيت.
- أين يتفوّق المنافس (صريح): التحرير بلا مطوّر، الحجز والطلب والدفع، الاستضافة والنطاق والدعم في باقة واحدة، وتحليلات مدمجة.

## 4) الكلمات المفتاحية
- AR: موقع مقهى فاخر · تصميم موقع كوفي شوب · قائمة مشروبات إلكترونية · موقع ثابت بلا خادم · موقع عربي إنجليزي RTL · PWA للمقاهي · صور AVIF WebP · موقع بديل عن إنستغرام · موقع فروع المقهى · تصميم فاخر داكن ذهبي
- EN: luxury café website · coffee shop static site · Vite multi-page site · bilingual Arabic English RTL · installable PWA café · AVIF WebP image pipeline · zero-dependency website · framework-free landing pages · self-hosted fonts performance · Instagram to website

## 5) ثلاث زوايا محتوى
1. «فاخر بلا وزن»: كيف تبني هوية داكنة ذهبية بخطوط محلية ومتغيّرات CSS بلا إطار ولا مكتبة حركة — مع أرقام الحزمة (69.5 KB JS / 62 KB CSS).
2. «الصور الحقيقية أسرع من المولّدة»: خط أنابيب Sharp → 139 AVIF + 139 WebP + LQIP، ولماذا يهمّ زائر الهاتف.
3. «من رابط في البايو إلى موقع»: ما الذي يخسره المقهى حين يبقى على إنستغرام فقط (قائمة، فروع، حكاية، بحث).

## 6) الفجوات (صريحة)
- تقنياً: لا README؛ فرع واحد باسم أداة (genspark_ai_developer) بلا main؛ لا اختبارات آلية؛ لا رابط حي (Cloudflare Pages المُشار إليه لا يستجيب)؛ لا نموذج تواصل أو حجز (زر «راسلنا» → إنستغرام فقط)؛ أرقام إنستغرام ثابتة في الكود.
- حقوقياً/تسويقياً: 8 صور مخزون بلا ترخيص موثّق؛ صور الحساب مأخوذة عبر عارض عام (Imginn) — تحتاج إذناً صريحاً من العلامة قبل النشر التجاري؛ صفحة الحكاية وبعض صور المعرض تُظهر المؤسس وباريستا (لا تُستخدم في مواد المحفظة).

## 7) المصادر
- مشروعنا: package.json · vite.config.js · src/js/content.js · src/js/i18n.js · src/data/images.json · src/data/brand-pack.json · public/ · ناتج `npm run build` · Playwright run (moain2028/espreso، 2026-09-23).
- Squarespace: https://www.squarespace.com/pricing · https://www.squarespace.com/tour/restaurant-websites (2026-09-23)
- Wix: https://www.wix.com/app-market/wix-restaurants-menus-new · https://support.wix.com/en/article/wix-restaurants-setting-up-wix-restaurants-menus-new (2026-09-23)
- Linktree: https://linktr.ee/s/pricing · https://www.theleap.co/blog/linktree-pricing/ (2026-09-23)

---
## EN summary
Buyers: owner-run cafés and roasters (1–5 branches) living on Instagram or a link-in-bio page. Category size: TBD (no reliable official figure found). Alternatives (accessed 2026-09-23): Squarespace (restaurant templates; $19–$99/mo annual), Wix Restaurants (menu app inside Wix; price not confirmed from first-party page), Linktree (free plan; the de-facto substitute for a site). Positioning: zero subscription and zero runtime dependencies, Arabic-first RTL with English from one dictionary, a bespoke luxury identity with self-hosted fonts, real photos through an AVIF/WebP + LQIP pipeline, installable PWA. Competitors win on no-developer editing, reservations/ordering/payments, bundled hosting and analytics. Gaps: no README, no main branch, no tests, no live URL, no contact form, static Instagram numbers, 8 undocumented stock photos, brand photos pulled via a public viewer, founder/barista faces in story and gallery.
