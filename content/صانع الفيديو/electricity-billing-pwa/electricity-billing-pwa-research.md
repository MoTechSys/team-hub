electricity-billing-pwa | صانع الفيديو | 2026-09-23 | v1 — بحث وتحليل (عربي + ملخص EN)

# نظام فواتير الكهرباء — بحث وتحليل

## 1. تحليل سوق مختصر
- **من يشتري هذا؟** أصحاب المولدات الأهلية ومحطات الكهرباء الصغيرة والمحصّلون في اليمن ومناطق مشابهة، حيث الفوترة بخط اليد والإنترنت غير مضمون (brief.ar.md، case-study.ar.md). القرار الحاسم في المشروع جاء من عميل فعلي (docs/OMAR_FEEDBACK.md، PIVOT_LOCAL_PWA.md).
- **حجم الفئة:** لا رقم موثّق لعدد المولدات الأهلية أو المحطات الصغيرة — يُستكمل. المؤشّر المتاح: وجود منتجات سحابية عربية مخصّصة لهذه الفئة بالذات («أصحاب مشاريع المولدات الكهربائية» بحسب E-Bill) يدلّ على طلب معروف.

### المنافسون/البدائل الثلاثة (وصول 2026-09-23)
| البديل | ما هو | ما يعلنه | الرابط |
|---|---|---|---|
| **E-Bill (e-bill.site)** | نظام عربي سحابي لإدارة اشتراكات الخدمات القائمة على العدادات (كهرباء، مياه، غاز، مولدات) | مزودو الكهرباء وأصحاب مشاريع المولدات؛ قراءات دورية، تحصيل، **تسجيل بلا إنترنت مع مزامنة عند الاتصال**؛ نظام سحابي بالاشتراك (عرض توضيحي/نسخة تجريبية بحسب الخطة؛ السعر غير معلن على الصفحة) | https://e-bill.site/ |
| **Zoho Invoice** | فوترة سحابية عامة للمشاريع الصغيرة | مجاني (بلا إعلانات أو رسوم مخفية بحسب صفحة التسعير)؛ يحتاج حساباً وإنترنت؛ لا حساب استهلاك عدادات | https://www.zoho.com/us/invoice/pricing/ |
| **Wave Invoicing** | فوترة ومحاسبة سحابية عامة | Starter مجاني بفواتير غير محدودة؛ Pro 19 دولاراً/شهر؛ رسوم بطاقات 2.9% + 0.60 دولار؛ إنترنت مطلوب | https://www.waveapps.com/pricing |
| (بديل شائع) **Invoiso** | برنامج فواتير مفتوح المصدر يعمل أوفلاين | سطح مكتب (Windows/Linux/Mac) لا جوال؛ PDF؛ بلا إنترنت | https://invoiso.co.in/ · https://sourceforge.net/projects/invoiso/ (2026-08-21) |
| (أداة جزئية) **تفقيط** | تطبيقات/مواقع لتحويل المبلغ إلى حروف عربية | تحلّ جزءاً واحداً فقط (التفقيط) دون فوترة | https://tafqit.net/ · https://tafqit.com/ |

## 2. التموضع
**ماذا يقول المنافس؟** E-Bill يقول: «نظام سحابي متكامل لمزودي الخدمات» مع وضع أوفلاين مؤقت يزامن لاحقاً — أي أن الخادم والحساب والاشتراك هم الأساس. Zoho وWave يقولان: «فوترة مجانية» — لكنها عامة، إنجليزية أولاً، سحابية، وبلا مفهوم «قراءة عداد». Invoiso يعمل أوفلاين لكن على سطح المكتب فقط.

**أين يتفوّق مشروعنا (من tech.md/brief/case-study فقط):**
- **أوفلاين أولاً بالكامل لا مؤقتاً:** لا خادم ولا حساب ولا مزامنة — IndexedDB في الجهاز، والنسخة الاحتياطية JSON بيد المستخدم. صفر تكلفة تشغيل.
- **مصمَّم لمحطة كهرباء تحديداً:** القراءة السابقة/الحالية، سعر الكيلووات، الخدمات، المتأخرات، المدفوع — معادلة المحصّل نفسها، لا فاتورة عامة.
- **عربي RTL حتى في PDF:** تشكيل وbidi وتفقيط داخل المتصفح (pdf-lib/jsPDF + arabic-reshaper + bidi-js) — ما يحتاج في البدائل العامة إلى أدوات خارجية.
- **يُثبَّت على الجوال كتطبيق (PWA)** بواجهة صمّمها المستخدم النهائي (شبكة 2×2 + شريط سفلي).

**أين يتفوّق المنافس (بصراحة):** E-Bill يقدّم تعدّد المستخدمين والفروع والتحصيل الميداني والتقارير المركزية والمزامنة — مشروعنا جهاز واحد مستقل بلا تعدّد مستخدمين بقرار العميل. Zoho/Wave تقدّمان الدفع الإلكتروني والتقارير المحاسبية والتكاملات. Invoiso مفتوح المصدر بمجتمع.

## 3. الكلمات المفتاحية
**عربي (10):** نظام فواتير الكهرباء · برنامج فواتير مولدات · فاتورة كهرباء بدون إنترنت · تطبيق فواتير للمحصّلين · حساب استهلاك الكهرباء تلقائياً · تفقيط المبلغ بالعربية · فاتورة A4 من الجوال · نظام فواتير بدون خادم · نسخة احتياطية JSON للفواتير · تطبيق ويب تقدّمي عربي
**English (10):** electricity billing PWA · offline invoicing app · meter reading invoice app · generator billing software · no-server billing app · IndexedDB Dexie invoicing · in-browser Arabic PDF invoice · amount in words Arabic · offline-first Next.js app · small utility billing system

## 4. ثلاث زوايا محتوى مقترحة
1. **«من خادم كامل إلى تطبيق يعيش في الجوال»** — قصة التحوّل 2026-06-09 (Prisma/JWT → Dexie/IndexedDB) وما أُلغي وما بقي؛ منشور LinkedIn + كاروسيل «قبل/بعد».
2. **«PDF عربي داخل المتصفح بلا خادم»** — الدرس التقني: تشكيل + bidi + تفقيط بـ pdf-lib/jsPDF؛ Thread على X + ريل تقني.
3. **«الواجهة التي صمّمها المحصّل»** — كيف تحوّلت ملاحظات العميل الصوتية إلى شبكة 2×2 وشريط سفلي موثّقة في docs/؛ مقال مدوّنة + بانر.

## 5. الفجوات (صريحة)
- **تقنياً:** لا اختبارات آلية (0 ملفات)؛ README يصف النسخة القديمة (Prisma/SQLite/JWT/بيانات دخول لا وجود لها) ويوجّه إلى المستودع القديم؛ عدد الصفحات متضارب (brief 7 / tech.md 9)؛ Zustand غير مذكور لكن لا إدارة حالة موثّقة؛ لا تعدّد مستخدمين ولا مزامنة (بقرار، لكنه يحدّ من المحطات ذات أكثر من محصّل).
- **تسويقياً:** رابط Vercel المعلن 404 — لا نسخة تجريبية عامة يمكن للزائر تجربتها؛ عدد المحطات/المستخدمين الفعليين غير موثّق؛ لقطات المحفظة من بيانات تجريبية بأسماء أشخاص (تُتجنّب في التصاميم)؛ 4 نسخ للمشروع عبر حسابَين تشوّش الزائر — تُوسم القديمة archived.

## English summary
The project targets small Yemeni power stations and private generator operators who invoice by hand without reliable internet. Alternatives: E-Bill (Arabic cloud subscription platform for meter-based utilities and generator owners, offline capture with sync), Zoho Invoice (free, cloud, generic), Wave (free Starter, $19/mo Pro, cloud, generic), Invoiso (open-source offline, desktop only). Our position: a fully offline-first PWA on the phone — no server, no account, no sync, zero running cost — purpose-built around the collector's meter formula, with Arabic RTL PDF and amount-in-words generated in-browser. Honest gaps: no tests, outdated README, dead Vercel link, single-device only, no documented user count. All links accessed 2026-09-23.

## المصادر
- brief.ar/en.md · case-study.ar.md · tech.md · links.md — portfolio-hub/01-projects/electricity-billing-pwa (2026-09-11)
- https://e-bill.site/ (وصول 2026-09-23)
- https://www.zoho.com/us/invoice/pricing/ (وصول 2026-09-23) · https://www.zoho.com/us/invoice/
- https://www.waveapps.com/pricing (وصول 2026-09-23)
- https://invoiso.co.in/ · https://sourceforge.net/projects/invoiso/ (2026-08-21)
- https://tafqit.net/ · https://tafqit.com/ (وصول 2026-09-23)
