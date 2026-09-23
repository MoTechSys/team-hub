keif-aldiafa-app | صانع الفيديو | 2026-09-23 | draft

# keif-aldiafa-app — بحث السوق والتموضع (مع ملخص EN في الأسفل)

تاريخ الوصول لكل الروابط: 2026-09-23. كل ادعاء عن مشروعنا من tech.md/README؛ كل ادعاء عن المنافسين من الصفحة المذكورة.

## 1) من يشتري هذا
- مؤسسات ضيافة ومناسبات صغيرة (قهوة سعودية، بوفيهات، تجهيز فعاليات) يديرها المالك بنفسه، ولديها ثلاثة موارد تتحرك معاً: مضيفون بالساعة/الفعالية، معدّات تُسلَّم وتُرجَع (كاسات، دلال، ثلاجات، طاولات)، وعملاء شركات يدفعون بالتحويل البنكي على مراحل.
- حجم الفئة: يُستكمل — لم أجد رقماً رسمياً موثوقاً لعدد مؤسسات الضيافة/المناسبات الصغيرة في السعودية خلال هذا البحث، ولن يُعرض رقم بلا مصدر.
- إشارة على النشاط: دعم منشآت (مزايا) يُدرج برامج المحاسبة السحابية للمنشآت الصغيرة بخصومات — أي أن الشريحة مُستهدَفة رسمياً بأدوات عامة، لا بأدوات تخصّ الضيافة الميدانية.

## 2) ثلاث بدائل حقيقية
| البديل | ما هو | ما يقوله | الرابط |
|---|---|---|---|
| **Rentman** (هولندا) | برنامج تأجير معدّات وفعاليات: مخزون، جدولة طاقم، عروض وفواتير | «يمنع الحجز المزدوج، يبسّط التسعير ويؤتمت الفواتير»؛ المنصة من €39/شهر + إضافات المخزون والطاقم من €14 لكل مستخدم/شهر + التسعير والفواتير €9 لكل مستخدم/شهر | https://rentman.io/industries/party-rental · https://rentman.io/pricing |
| **دفترة Daftra** (سحابي، عربي) | إدارة أعمال ومحاسبة لأكثر من 50 نشاطاً: فواتير إلكترونية معتمدة (ZATCA)، مخزون، مواعيد وجداول موظفين، تطبيقات جوال «تعمل حتى بدون إنترنت» | تجربة مجانية بلا بطاقة؛ الباقات بالدولار على صفحة الخطط، وعلى مزايا منشآت الأساسية 1,440 ر.س/سنة قبل الخصم | https://www.daftra.com/ · https://www.daftra.com/plans · https://mazaya.monshaat.gov.sa/mazaya/13871 |
| **قيود Qoyod** (سعودي) | محاسبة سحابية ونقاط بيع، متوافق مع ZATCA، «+25 ألف عميل»، 14 يوم تجربة | الباقة الأساسية: مستخدم واحد، موقع واحد، مبيعات ومنتجات ومحاسبة وربط ZATCA؛ الأسعار على صفحة الاشتراك (على مزايا منشآت: 2,070 ر.س/سنة قبل الخصم) | https://www.qoyod.com/ · https://www.qoyod.com/knowledge-base/باقات-قيود-للاشتراك-qoyod-2025/ · https://mazaya.monshaat.gov.sa/mazaya/12984 |

بديل رابع للسياق: **أعزم aezm.app** — منصة سعودية لحجز أماكن وبوفيهات الضيافة (جهة العميل النهائي، ليست أداة تشغيل للمؤسسة)؛ الصفحة لم تُقرأ آلياً، فلا تُقتبس تفاصيلها.

## 3) التموضع
- ما يقوله المنافس: Rentman يحلّ مشكلتنا نفسها (منع الحجز المزدوج + مخزون + طاقم) لكن بالإنجليزية وباليورو ولكل مستخدم، وبنموذج سحابي؛ دفترة وقيود أدوات محاسبة عامة قوية في الفوترة الإلكترونية وZATCA، لكن الضيافة الميدانية (حجز مضيفين متداخل، تسليم/إرجاع معدّات لفعاليتين متزامنتين، دفتر مستحقات المضيفين) ليست في قلبهما.
- أين يتفوّق مشروعنا (من tech.md فقط): (أ) القيود في قاعدة البيانات نفسها — TRIGGER يرفض التداخل الزمني والتسليم الزائد، لا فحص في الواجهة؛ (ب) المخزون محجوز زمنياً فيظهر النقص الصحيح عند تزامن فعاليتَين؛ (ج) يعمل بلا إنترنت بالكامل وبلا اشتراك لكل مستخدم — ملف SQLite على الجهاز ونسخة إلى Google Drive؛ (د) مبني من مدخلات العميل الحرفية (قائمة 15 مشروباً، 11 صنفاً، 6 بنود جاهزة من نماذجه).
- أين يتفوّق المنافس (صريح): الفوترة الإلكترونية ZATCA (دفترة/قيود)، تعدد المستخدمين والأدوار، التقارير المحاسبية، الدعم والتحديثات المستمرة، والنشر الفعلي على المتاجر.

## 4) الكلمات المفتاحية
- AR: إدارة مؤسسة ضيافة · تطبيق حجز مضيفين · جدول تعارض المضيفين · إدارة مخزون فعاليات · ورقة تجهيز فعالية · عرض سعر ضيافة · فاتورة ضيافة PDF · مستحقات المضيفين · تطبيق يعمل بدون إنترنت · React Native عربي
- EN: hospitality operations app · host scheduling app · double-booking prevention · event equipment inventory · time-reserved inventory · offline-first mobile app · SQLite triggers constraints · Expo React Native Arabic RTL · quote to invoice workflow · Google Drive appDataFolder backup

## 5) ثلاث زوايا محتوى
1. «إخفاء زر ليس حماية»: لماذا وُضعت قيود التعارض والنقص داخل SQLite بـ TRIGGER + RAISE(ABORT) — مع مثال حجز مضيف مرفوض.
2. «المخزون المحجوز زمنياً»: كيف يظهر النقص الصحيح عند تزامن فعاليتَين (المتاح = المملوك − التالف − المسلَّم لفعاليات متداخلة).
3. «مزامنة بلا سحابة»: نسخة احتياطية إلى appDataFolder بنطاق drive.appdata فقط، ولماذا `wal_checkpoint` قبل الرفع.

## 6) الفجوات (صريحة)
- تقنياً: لا اختبارات آلية (0)؛ لا APK منشور وآخر بناء GitHub Actions فشل (2026-09-22)؛ مستخدم واحد بلا أدوار رغم بحث RBAC كامل؛ لا إشعارات؛ لا فوترة إلكترونية ZATCA؛ ADR #3 يذكر PostgreSQL بينما التنفيذ SQLite؛ بيانات اتصال وIBAN المؤسسة مضمّنة في seed.ts.
- تسويقياً: لا رابط حي ولا صفحة متجر؛ لا لقطات في المستودع قبل هذه الحزمة؛ README يذكر أسماء عملاء في جدول التحقق؛ لا رقم مستخدمين أو فعاليات مُدارة يمكن الاستشهاد به.

## 7) المصادر
- مشروعنا: README.md · app/src/db/schema.sql · app/src/db/repo.ts · app/src/db/seed.ts · app/src/lib/backup.ts · 03-architecture/00-decisions.md · docs/USER-GUIDE.md (moain2028/keif-aldiafa-app، قراءة 2026-09-23) · GitHub API releases=0 · actions run 2026-09-22 failure.
- Rentman: https://rentman.io/industries/party-rental · https://rentman.io/pricing (2026-09-23)
- دفترة: https://www.daftra.com/ · https://www.daftra.com/plans · https://mazaya.monshaat.gov.sa/mazaya/13871 (2026-09-23)
- قيود: https://www.qoyod.com/ · https://www.qoyod.com/knowledge-base/باقات-قيود-للاشتراك-qoyod-2025/ · https://mazaya.monshaat.gov.sa/mazaya/12984 (2026-09-23)

---
## EN summary
Buyers: owner-run hospitality/events businesses juggling hosts, returnable equipment and corporate clients. Category size: TBD (no reliable official figure found). Alternatives (accessed 2026-09-23): Rentman (rental/events software; prevents overbooking, inventory + crew + quoting; platform €39/mo plus €14/user add-ons), Daftra (Arabic cloud business suite, ZATCA e-invoicing, staff schedules, offline mobile; free trial), Qoyod (Saudi cloud accounting + POS, ZATCA; Basic = 1 user/1 site). Positioning: our app enforces double-booking and over-issue constraints in SQLite triggers, computes time-reserved availability across concurrent events, works fully offline with no per-user fee, and is built from the client's verbatim inputs. Competitors win on ZATCA e-invoicing, multi-user roles, reporting, support and actual store distribution. Gaps: 0 tests, no published APK (last CI build failed 2026-09-22), single-user, no notifications, no ZATCA, sensitive org contact data seeded in code, no live link or usage numbers.
