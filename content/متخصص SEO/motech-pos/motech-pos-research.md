motech-pos | متخصص SEO | 2026-09-23 | v2 addendum · بحث وتحليل (بحث ويب مؤرَّخ: 2026-09-23)

# motech-pos — بحث وتحليل السوق والتموضع
English summary at the end.

## 1. من يشتري هذا؟
- المشتري: شركة تجارية (تجزئة/جملة) تعمل أصلاً على نظام نقاط بيع قديم فوق قاعدة Oracle محلية، عندها بيانات سنوات في تلك القاعدة، وتريد واجهة ويب عربية حديثة على الجوال/التابلت/الديسكتوب دون ترحيل قاعدة الإنتاج أو المس بها. (المصدر: brief.ar.md «المشكلة/لمن يفيد»، tech.md «Problem»)
- ما يريده: الاستمرار على بياناته الحية مع شاشة بيع سريعة على الجوال، ورديات وتصفية نقد، صلاحيات، طباعة حرارية عربية، وفوترة إلكترونية QR (tech.md «Solution / core features»).
- حجم الفئة: أقرب مؤشر عام في البحث: اشتراكات نقاط البيع السحابية للمنشآت الصغيرة والمتوسطة في السعودية تتراوح 200–1500 ر.س/شهر (azdan.com، تاريخ الوصول 2026-09-23) — مؤشر على سوق نشط، لكن عدد المنشآت العاملة على Oracle POS قديم تحديداً **يُستكمل** (لا رقم مؤرّخ).

## 2. ثلاثة منافسين/بدائل حقيقية (تاريخ الوصول 2026-09-23)
| البديل | ماذا يقول عن نفسه | السعر المعلن | الرابط |
|---|---|---|---|
| **Onyx Pro / Onyx POS** (Ultimate Solutions — النظام القائم الذي يُستبدل) | نقاط بيع فوق Oracle متعددة اللغات، تطبيق جوال أوفلاين | غير معلن على الموقع (ترخيص/عرض سعر) | https://onyxproerp.com/onyxpro-summery/ · https://play.google.com/store/apps/details?id=com.ultimate.onyxpos&hl=ar |
| **Foodics** (POS سحابي سعودي) | نظام نقاط بيع وإدارة للمطاعم والتجزئة | Starter من 199 ر.س/شهر (مصدر مقارنة: onlineemenu.com) وحتى 392–1133 ر.س/شهر للمطاعم بحسب ontabee/ordegate — الصفحة الرسمية لا تُظهر الأرقام بلا تفاعل | https://www.foodics.com/pricing/ |
| **Rewaa** (POS + مخزون سحابي سعودي) | نظام نقاط بيع ومخزون للتجزئة | من 275 ر.س/شهر بدفع سنوي مقدّم بلا ضريبة (snad.io نقلاً عن rewaa.com/pricing، أغسطس 2026؛ Capterra: Launch plan) | https://www.capterra.com/p/10037838/Rewaa/ · https://www.snad.io/en/alternatives/rewaa |
| **Odoo Point of Sale** (مفتوح المصدر/سحابي عالمي) | POS ضمن منظومة ERP | Standard نحو 8.95$/مستخدم/شهر في الشرق الأوسط سنوياً (oec.sh) وحتى 31–39$/مستخدم في مناطق أخرى؛ Community مجاني | https://www.odoo.com/pricing |

## 3. التموضع: ماذا يقول المنافس، وأين يتفوّق مشروعنا (من tech.md/brief فقط)
| ما يقوله المنافس | ما عندنا (المصدر) |
|---|---|
| Foodics/Rewaa: ابدأ من الصفر على سحابتنا باشتراك شهري + عتاد | يعمل على بيانات المنشأة الحية نفسها: يقرأ مخطط Oracle الحقيقي (YSPOS23) للقراءة فقط ويكتب في مخططه المستقل (MOTECH_POS) — لا ترحيل ولا كسر للإنتاج (brief «الحل»، tech.md «Architecture notes») |
| Onyx: عميل سطح مكتب (Forms) فوق Oracle | PWA ويب عربي RTL mobile-first: عملية بيع كاملة على 390 بكسل، سلة sheet سفلية، أهداف لمس ≥48px (tech.md «Solution») |
| Odoo: POS عام يحتاج تخصيصاً | تغطية 71/71 شاشة قابلة للبناء من شاشات النظام القائم (88.75% من 80) بتوثيق ADR للمغلقة معمارياً (tech.md «Status»، docs/MATCHING_SCREENS.md) |
| — | جودة مُثبتة: 348 اختبار وحدة، 160/160 فحصاً حياً على 3 أدوار × 3 مقاسات، 0 تمرير أفقي، 33 هجرة SQL، 215 نقطة REST (tech.md جدول الأرقام) |
| — | أمن: JWT في httpOnly cookies، CSP، throttle للدخول، 12 كود صلاحية تُفرض وقت الطلب، Swagger مغلق في الإنتاج (tech.md، brief) |
| — | طباعة حرارية عربية عبر Web Serial/WebUSB/Bluetooth؛ اختبار حقيقي ناجح على Bixolon SPP-R310 (tech.md) |

**نقطة صدق:** المنافسون السحابيون يتفوّقون في النضج التجاري (دعم، تحديثات، قاعدة عملاء، تكامل زاتكا كامل، تقارير)، وOnyx يتفوّق بكونه النظام الأصل بكل شاشاته الـ80. مشروعنا في حالة beta/pilot: تدقيق مستقل (docs/FINAL_AUDIT 2026-07-03) حكم «صالح كنظام تجريبي موازٍ لا بديلاً كاملاً» وسجّل 4 عيوب P0 عولج جزء منها (tech.md «Status») — لذلك لا يُقال «بديل كامل» (numbers-bank.md).

## 4. الكلمات المفتاحية
**عربي (10):** نظام نقاط بيع ويب · نقاط بيع تعمل مع Oracle · بديل نظام نقاط البيع القديم · نقاط بيع عربي RTL · نظام كاشير على الجوال · ترحيل نقاط البيع · تصفية الوردية نقاط البيع · طباعة حرارية عربية بلوتوث · فاتورة إلكترونية QR نقاط بيع · نقاط بيع PWA
**English (10):** web POS on Oracle database · legacy POS modernization · React NestJS point of sale · PWA point of sale · mobile-first checkout 390px · Arabic RTL POS · POS shift cash reconciliation · web serial thermal printing ESC/POS · read-only production schema integration · POS migration study
(بلا أحجام بحث — لا أداة بيانات كلمات مفتاحية هنا؛ الاختيار من صياغات ظهرت في نتائج البحث المؤرّخة ومن وظائف المنتج الموثّقة.)

## 5. ثلاث زوايا محتوى مقترحة
1. **«لا تستبدله — ابنِ بجانبه»**: كيف تُحدّث نقاط البيع دون ترحيل قاعدة Oracle: قراءة من مخطط الإنتاج وكتابة في مخطط مستقل (للشركات؛ من CLAUDE.md/ARCHITECTURE عبر tech.md).
2. **«348 اختباراً و160 فحصاً حياً قبل أول عملية بيع»**: قصة الجودة — Vitest، Playwright، 3 أدوار × 3 مقاسات، 0 تمرير أفقي (للمجتمع التقني؛ docs/QA_SWEEP.md).
3. **«طباعة عربية من المتصفح على طابعة بلوتوث»**: اختبار ميداني Bixolon SPP-R310 عبر Web Bluetooth/raster GS v 0 — ولماذا فشلت Xprinter على USB/Windows (docs/PRINT_FIELD_TEST_2026-07-13.md؛ صدق تقني يبني الثقة).

## 6. الفجوات (صريحة)
- **تقنية:** حالة pilot لا إنتاج؛ 4 عيوب P0 من التدقيق المستقل لم تُغلق كلها (tech.md) · 9 شاشات مغلقة معمارياً لم تُبنَ · الدومين الحي في الوثائق معطّل (tech.md «Live URL: none») · لا README في جذر المستودع · طباعة USB على Windows فاشلة (قيد usbprint.sys) · اللقطات ليست @2x · CLAUDE.md يذكر مسارات محلية وأسماء schema إنتاجية تحتاج تنقية قبل العرض العلني.
- **تسويقية:** بلا عملاء موثّقين (منشأة واحدة، بلا رقم) · لا رابط تجريبي حي يمكن للشركة تجربته · المقارنة الصريحة بـ Onyx Pro في الوثائق تحتاج قراراً من معين قبل النشر (tech.md «الأسماء التسويقية») · تعارض أرقام قديم (306 مقابل 348) يُوحَّد في كل النصوص على 348.

## 7. المصادر
- brief.ar.md / brief.en.md / tech.md / links.md — portfolio-hub `01-projects/motech-pos/` · 03-content/numbers-bank.md
- المستودع: https://github.com/moain2028/motech-pos (نسخة عامة) · الأصل moain2026/motech-pos
- Onyx: https://onyxproerp.com/onyxpro-summery/ · Play: https://play.google.com/store/apps/details?id=com.ultimate.onyxpos&hl=ar (2026-09-23)
- Foodics: https://www.foodics.com/pricing/ · مقارنة onlineemenu.com · ontabee.com/foodics-alternative · ordegate.com (2026-09-23)
- Rewaa: https://www.capterra.com/p/10037838/Rewaa/ · https://www.snad.io/en/alternatives/rewaa (2026-09-23)
- Odoo: https://www.odoo.com/pricing · https://oec.sh/odoo-pricing (2026-09-23)
- نطاق أسعار POS السعودية: https://www.azdan.com/blog/top-20-pos-software-providers-in-the-ksa (2026-09-23)

---
## English summary
Buyer: a retail/wholesale company already running a legacy Oracle-backed desktop POS with years of data, wanting a modern Arabic web POS on phone/tablet/desktop without migrating or touching the live database. Saudi SME cloud POS subscriptions run roughly SAR 200–1,500/month (azdan.com, accessed 2026-09-23); the count of legacy-Oracle-POS businesses is left "to be completed".
Alternatives (accessed 2026-09-23): Onyx Pro/Onyx POS (the incumbent; pricing not public), Foodics (Saudi cloud POS, from about SAR 199/month up to SAR 392–1,133 for restaurants per comparison sites), Rewaa (Saudi retail POS + inventory, from SAR 275/month billed annually), Odoo POS (from about $8.95/user/month in the Middle East; Community free).
Positioning (from tech.md/brief only): runs on the company's live Oracle data read-only and writes to its own schema; mobile-first RTL PWA with a full sale on 390 px; 71/71 buildable legacy screens covered; 348 unit tests, 160/160 live checks, 12 permission codes, real Bluetooth thermal print test passed. Honest gaps: beta/pilot status with open P0s from an independent audit, dead demo domain, no root README, no documented customers, and an unresolved decision on naming the incumbent in marketing.
