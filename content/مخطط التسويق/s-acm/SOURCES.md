s-acm | مخطط التسويق | 2026-09-23 | v2

# SOURCES.md — مصدر كل نص ورقم وصورة في s-acm-project-pack-v2

المصادر الأساسية: `01-projects/s-acm/brief.ar.md` · `brief.en.md` · `tech.md` · `links.md` · `screenshots/` في https://github.com/moain2028/portfolio-hub، وREADME المستودع العام https://github.com/moain2028/s-acm (تحقق مباشر 2026-09-23: 70+ صلاحية على 12 قسماً؛ جدول الحالة 95/60/40/0%).

## A. النصوص والأرقام على التصاميم (24 PNG + كاروسيل + بطاقة + بانر + ريل)
| العنصر | AR | EN | المصدر |
|---|---|---|---|
| الاسم | S-ACM | S-ACM | brief (العنوان) |
| slug | s-acm | — | اسم المستودع |
| العنوان | نظام إدارة محتوى أكاديمي ذكي — مشروع تخرج بكود مفتوح | A smart academic content management system — an open graduation project | brief.ar/en H1 |
| السطر الوصفي | Monorepo بـ Turborepo: React 19 وTailwind 4 في الواجهة، Hono وPostgreSQL وDrizzle في الخادم — نظام صلاحيات ديناميكي بالكامل | Turborepo monorepo: React 19 and Tailwind 4 up front, Hono, PostgreSQL and Drizzle behind — fully dynamic permissions | brief «الحل» + tech.md «التقنيات» |
| 70+ صلاحية ديناميكية | | | README «نظام الصلاحيات» + tech.md جدول الأرقام |
| 12 قسماً · 3 مستويات | | | README «70+ صلاحية موزعة على 12 قسم» + tech.md |
| 19 صفحة | | | tech.md (s-acm-frontend/client/src/pages) |
| 13 جدولاً | | | tech.md (apps/api/src/db/schema.ts) |
| 14 وحدة API | | | tech.md (apps/api/src/routes) |
| 7 وحدات | | | brief «7 وحدات وظيفية» (README: 7 ميزات رئيسية) |
| 95% واجهة مكتملة | | | README جدول الحالة + tech.md |
| تاجات: React 19 · TypeScript · Tailwind 4 · Hono · PostgreSQL · Drizzle · Turborepo | | | tech.md «التقنيات (كما في المستودع)» |
| شارة الشريحة: طلاب / Students (#8B5CF6) | | | تكليف مدير المنتج msg 4606678 + 02-brand/README.md |
| الفوتر github.com/moain2028/s-acm | | | النسخة العامة (GitHub API: visibility=public، 2026-09-23). قرار مدير المنتج في task #6: يبقى رابط GitHub للنسخ العامة |
| wordmark «معين العباسي / Moain Al-Abbasi» (نسخ logo فقط) | | | project-pack-standard-v2 §A — نص فقط، بلا أيقونة |
| نصوص الكاروسيل 1–5 (المشكلة/الحل/كيف يعمل/الأرقام/الدعوة) | | | brief.ar/en (المشكلة، الحل، لمن، تواصل) + tech.md |
| بطاقة الرقم الواحد «70+» | | | README «نظام الصلاحيات» |
| البانر «كيف تبني مشروع تخرج على Monorepo حديث بصلاحيات ديناميكية» | | | تركيب من brief «لمن يفيد» + tech.md — عنوان مقال مقترح (زاوية 1 في research) |
| الريل: 6 مشاهد نصية | | | s-acm-copy.ar/en.md «نص الريل» ← brief + tech.md |

## B. الصور
| الملف/الاستخدام | المصدر | ملاحظة |
|---|---|---|
| desktop-02-dashboard.png + mobile-02-dashboard.png (القطع الست، الكاروسيل 2، الريل 3) | 01-projects/s-acm/screenshots/ | حقيقية من تشغيل محلي للواجهة (tech.md «التشغيل والتصوير» 2026-09-11) على بيانات تجريبية: الأسماء والأرقام داخل اللقطات (12 مستخدماً، 8 مقررات، 18 ملفاً، «د. أحمد الحمادي»…) seed وليست جامعة حقيقية — مُعلَن هنا حسب المعيار |
| desktop-01-home / mobile-01-home (كاروسيل 1، غلاف الريل، الريل 2) | نفسه | صفحة الدخول |
| desktop-06-academic / mobile-06-academic (كاروسيل 3، الريل 5) | نفسه | البيانات الأكاديمية |
| desktop-08-reports (كاروسيل 4) | نفسه | التقارير |
| mobile-07-ai (كاروسيل 5) | نفسه | صفحة الذكاء الاصطناعي — واجهة فقط؛ الميزة مخططة 0% (README) ولم تُسوَّق كموجودة |
| desktop-04-users / mobile-04-users (البانر، الريل 4) | نفسه | إدارة المستخدمين |
| الخلفيات/التوهج/الشبكة | مولّدة برمجياً من 02-brand/scripts/brand.py | لا صور مخزون |
| لا لقطة مولّدة بالذكاء الاصطناعي | — | — |

## C. الصوت
- `_music.mp3` داخل الريلَين: موسيقى آلية مولّدة (CassetteAI/music-generator، 24 ث، 2026-09-23) — بلا حقوق طرف ثالث، بلا كلمات.

## D. ملفات البحث والنص
- `s-acm-research.md`: كل ادعاء خارجي برابط وتاريخ وصول 2026-09-23 (القسم 7).
- `s-acm-explainer.ar/en.md`، `s-acm-copy.ar/en.md`: كل جملة من brief/tech/README؛ حالة draft حتى ختم المحرر.

## E. ما لم يُستخدم عمداً
- ميزات الذكاء الاصطناعي (تلخيص/توليد أسئلة) كميزة موجودة — مخططة 0%.
- رابط حي أو فيديو — links.md: يُستكمل.
- أي اسم جامعة أو عميل.
- تضارب brief («7 وحدات وظيفية») مع tech.md («14 ملف مسارات API»): عُرضا كرقمَين مختلفَين بتسميتَين مختلفتَين (وحدات وظيفية vs وحدات API)، لا كرقم واحد.

## F. التباين (WCAG)
Sand #F7F5F0 على Navy 13.4:1 · Mist #DCE3EA على Navy 11.3:1 · Amber على Navy 7.2:1 · #A3B1C0 (النص الخافت المعتمد) على Navy 6.7:1 · Sand على شريحة #1C3B5E 10.5:1 · Ink على شارة الطلاب #8B5CF6 = 4.25:1 (نص 20px Bold = Large Text، حد AA للنص الكبير 3:1 ✓).

## G. التوليد
`make/packlib.py` + `make/build.py` (Pillow + raqm، خطوط 02-brand/fonts، مبني على 02-brand/scripts/brand.py للمصمم) يعيدان إنتاج كل الصور؛ الريل بـ ffmpeg من إطارات `_reel_ar/` و`_reel_en/`.
