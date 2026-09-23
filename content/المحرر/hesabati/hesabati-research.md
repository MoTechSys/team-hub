hesabati | المحرر | 2026-09-23 | final

# حساباتي — بحث وتحليل (Research & analysis)

## 1. من يشتري هذا وحجم الفئة
المشتري: صاحب مشروع صغير يدير أكثر من نشاط (محلّان أو ثلاثة) ويريد أرصدته وديونه ورواتبه في شاشة واحدة، بواجهة عربية. المستخدم اليومي: المالك أو محاسب واحد. الفئة التجارية المقابلة هي «برامج المحاسبة السحابية العربية للمنشآت الصغيرة والمتوسطة» وهي فئة قائمة ومزدحمة (أدناه). حجم الفئة بالأرقام: يُستكمل — لا مصدر موثوق نعتمده، ولا نقدّره.

## 2. ثلاثة منافسون حقيقيون (تاريخ الوصول 2026-09-23)
| المنتج | ما يفعله | مؤشرات | الرابط |
|---|---|---|---|
| قيود Qoyod | محاسبة سحابية للمنشآت السعودية، فوترة إلكترونية متوافقة مع زاتكا، اشتراك، تجربة 14 يوماً | تطبيق Android 50K+ تنزيل، آخر تحديث 2026-09-03 | https://play.google.com/store/apps/details?id=com.qoyod.mobile · https://www.qoyod.com/ |
| دفترة Daftra | ERP/محاسبة سحابية شاملة للمنشآت الصغيرة والمتوسطة (حسابات، مخزون، خزينة، رواتب)، اشتراك | تطبيق Android 500K+ تنزيل · 3.9، آخر تحديث 2026-08-25 | https://play.google.com/store/apps/details?id=com.daftra.app · https://www.daftra.com/en/ |
| وفق Wafeq | محاسبة سحابية للمنطقة العربية: فواتير، مخزون، رواتب، «أكثر من 30 تقريراً»، اشتراك | موقع رسمي وتطبيق iOS | https://www.wafeq.com/en |

ملاحظة منهجية: الأرقام كما تعرضها صفحات Google Play والمواقع الرسمية يوم الوصول؛ ما لم يظهر (تقييم قيود، تنزيلات وفق) لم يُدرج.

## 3. التموضع
ما يقوله المنافس: سحابي، اشتراك شهري، امتثال ضريبي (زاتكا)، «الأفضل/الأشمل». كلها خدمات SaaS بخوادم المزوّد وبياناتك عنده.

أين يقف حساباتي (من tech.md فقط):
- أعمال متعددة في حساب واحد كفكرة مركزية، لا إضافة مدفوعة.
- استضافة ذاتية بأمر Docker واحد: بياناتك على خادمك، بلا اشتراك.
- كود مفتوح على GitHub (324 commit) يمكن لعميل تقني قراءته وتعديله.
- تغطية واسعة في نسخة واحدة: 50 شاشة، 84 جدولاً، 154 مسار API، 23 محرّكاً، 158/158 اختباراً.
- ما لا نقوله: لا ادعاء امتثال زاتكا أو فوترة إلكترونية (غير موجودَين في tech.md)، ولا مقارنة بعدد العملاء أو التنزيلات.

الجملة التموضعية: «محاسبة كاملة لأكثر من نشاط، على خادمك أنت، برقم واحد صحيح».

## 4. الكلمات المفتاحية
AR (10): برنامج محاسبة عربي · نظام محاسبي للمشاريع الصغيرة · محاسبة أكثر من نشاط تجاري · برنامج محاسبة مفتوح المصدر · نظام مالي Angular · سندات قبض وصرف · قيود يومية · إدارة صناديق وبنوك · رواتب موظفين برنامج · نظام محاسبة Docker
EN (10): Arabic accounting software · multi-business accounting system · open-source accounting Angular · Hono PostgreSQL accounting · small business finance system · vouchers and journal entries software · self-hosted accounting Docker · real-time accounting dashboard · RTL accounting app · Drizzle ORM PostgreSQL example

## 5. ثلاث زوايا محتوى
1. «ثلاثة محلات، رقم واحد»: كيف يجمع حساب واحد أرصدة وديون ورواتب أنشطة متعددة — للمالك لا للمحاسب.
2. «على خادمك أنت»: أمر Docker واحد يقابل اشتراكاً شهرياً وبيانات عند مزوّد — لمن يهمّه التحكم والتكلفة.
3. «من الكود إلى الرقم»: كيف قِسنا 50 شاشة و84 جدولاً و158 اختباراً، ولماذا صحّحنا README (ApexCharts لا Chart.js) — للجمهور التقني.

## 6. الفجوات (صريحة)
تقنياً:
- عطلان يمنعان تجربة نظيفة من الصفر: ترتيب الترحيلات يفشل على قاعدة فارغة، وخطأ أنواع يمنع ng build دون إصلاح يدوي.
- لا رابط حي ولا نسخة تجريبية عامة؛ الديمو يتطلّب Docker محلياً.
- README يبالغ في مكتبات الرسوم (Chart.js وThree.js غير مستخدمَين) والجذر مزدحم بـ30+ ملف تقارير وكوكيز.
- آخر تطوير 2026-04-13؛ لا CI ظاهر في tech.md.
تسويقياً:
- لا امتثال ضريبي (زاتكا/فوترة إلكترونية) وهو أول ما تسأل عنه المنشآت السعودية.
- لا عملاء معلنون ولا أرقام استخدام؛ كل الأرقام تقنية.
- لا فيديو ديمو ولا دراسة حالة (links.md: يُستكمل).

## Summary (EN)
Hesabati targets small-business owners running several activities who want one correct number, in Arabic. The category (Arabic cloud accounting for SMEs) is crowded: Qoyod (50K+ Android installs), Daftra (500K+, 3.9), and Wafeq, all subscription SaaS with tax-compliance messaging (accessed 2026-09-23). Positioning from tech.md only: multi-business by design, self-hosted with one Docker command, open code, and broad coverage (50 screens, 84 tables, 158/158 tests). Gaps: two setup defects, no public demo, no tax-compliance features, no announced customers, and last commit in April 2026.

## المصادر
- brief.ar/en.md، tech.md، links.md — `01-projects/hesabati/` في moain2028/portfolio-hub.
- المستودع — https://github.com/moain2028/hesabati (HTTP 200، 2026-09-23).
- Qoyod — Google Play com.qoyod.mobile وqoyod.com (2026-09-23).
- Daftra — Google Play com.daftra.app وdaftra.com/en (2026-09-23).
- Wafeq — wafeq.com/en (2026-09-23).
