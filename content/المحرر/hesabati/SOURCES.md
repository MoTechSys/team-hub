hesabati | المحرر | 2026-09-23 | final

# hesabati-design-pack-v1 — مصدر كل نص ورقم

| العنصر على التصميم | AR | EN | المصدر |
|---|---|---|---|
| الاسم | حساباتي | Hesabati | brief.ar.md / brief.en.md (العنوان) |
| السطر التعريفي | محاسبة كاملة لأكثر من نشاط تجاري في حساب واحد | Full accounting for more than one business in a single account | brief.ar.md / brief.en.md (العنوان) |
| الوصف | أعمال متعددة في حساب واحد: سندات وقيود، صناديق وبنوك، عملاء وموردون، مستودعات، رواتب، صلاحيات، ولوحة تحكم لحظية. | Multiple businesses under one login: vouchers and journal entries, cash and banks, customers and suppliers, warehouses, payroll, permissions, and a real-time dashboard. | brief §الحل / Solution (مختصر بلا إضافة) |
| 50 شاشة / 50 screens | ✓ | ✓ | tech.md §الأرقام — `frontend/src/app/pages/` |
| 84 جدولاً / 84 tables | ✓ | ✓ | tech.md §الأرقام — psql information_schema بعد db:push |
| 158 اختباراً ناجحاً / 158 passing tests | ✓ | ✓ | tech.md §الأرقام — vitest 158/158، تشغيل حي 2026-09-11 |
| تاجات التقنيات | Angular 21 · Tailwind · Hono · PostgreSQL · Drizzle · Docker | نفسها | tech.md §التقنيات (كما في المستودع) |
| الدعوة | تريد رقماً واحداً لكل أنشطتك؟ راسلني | Want one correct number across all your businesses? DM me | brief §تواصل / Contact |
| شارة الشريحة | مشاريع صغيرة | Small business | تكليف المهمة + 02-brand/README.md |
| الرابط في الفوتر | github.com/moain2028/hesabati | نفسه | تكليف المهمة (المستودع العام moain2028/hesabati — يفتح، تم التحقق 2026-09-23) |
| النسخة بشعار | «معين العباسي» نص فقط | "Moain Al-Abbasi" wordmark only | design-pack-standard-v1.md §2 — لا أيقونة، لا mark.svg |

## اللقطات (حقيقية، من التشغيل الحي 2026-09-11، بدقة 2x)
- ديسكتوب: `01-projects/hesabati/screenshots/desktop-02-dashboard.png` (2880×1800)
- جوال: `01-projects/hesabati/screenshots/mobile-01-businesses.png` (780×1688)
- لا لقطة مولّدة. لا اسم عميل (شاشة اختيار العمل تعرض بيانات seed التجريبية فقط).

## الهوية
ألوان وخطوط ولون الشريحة من `02-brand/README.md` عبر `02-brand/scripts/brand.py`. المساحة الآمنة للشعار 12% من العرض (أعلى-يمين AR / أعلى-يسار EN) خالية في نسخة nologo.

## إعادة التوليد
`python3 pack.py` (يعتمد على ~/repos/portfolio-hub + Pillow مع raqm).
