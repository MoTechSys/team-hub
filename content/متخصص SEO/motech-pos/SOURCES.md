motech-pos | متخصص SEO | 2026-09-23 | v2 addendum (B–F) — يكمّل motech-pos-sources.md من حزمة v1

# SOURCES — ملحق motech-pos (B–F)

المرجع: https://github.com/moain2028/portfolio-hub → `01-projects/motech-pos/` (brief.ar.md · brief.en.md · tech.md · links.md · screenshots/) + `03-content/numbers-bank.md` + `02-brand/README.md`.

## الصور (حقيقية من المستودع — لا شيء مولّد)
| الاستخدام | الملف | ملاحظة |
|---|---|---|
| البطل (كاروسيل 2، بانر، ريل 1) | `screenshots/desktop-02-cart.png` 1440×900 | شاشة البيع مع سلة |
| ريل 3 | `screenshots/desktop-01-pos.png` | شاشة البيع |
| كاروسيل 5، ريل 6 | `screenshots/desktop-03-pay-dialog.png` | نافذة الدفع |
| كاروسيل 1، ريل 2 (خافتة) | `screenshots/desktop-05-admin-nav.png` | قائمة الإدارة |
| كاروسيل 3، ريل 4، بانر | `screenshots/mobile-04-cashier-expanded.png` · `mobile-05-cashier-drawer.png` 390×844 | قائمة الكاشير على الجوال |
| الأصل | `pos-audit-shots/` في مستودع motech-pos (tech.md) | لقطات تدقيق فنية، ليست @2x؛ البيانات فيها بيانات المنشأة الحية للقراءة (YSPOS23) بأسماء أصناف حقيقية وبلا أسماء أشخاص |

## النصوص والأرقام
| العنصر | المصدر |
|---|---|
| العنوان، سطر الحل، لمن يفيد، الدعوة — في B وC وD وF | brief.ar.md / brief.en.md المختوم (حرفياً أو مقتطعاً دون تغيير كلمات) |
| 348 اختباراً · 420 ms لـ 59 جدولاً · 12 كود صلاحية · 0 تمرير أفقي | brief «النتيجة» · tech.md (docs/QA_SWEEP.md §6، docs/PROGRESS.md Lane G) |
| 160/160 فحصاً حياً (3 أدوار × 3 مقاسات) | tech.md «Live QA checks» (docs/QA_SWEEP.md §2) |
| 215 نقطة REST · 26 وحدة خلفية · 27 وحدة واجهة · 33 هجرة · 71/71 و88.75% | tech.md جدول الأرقام (docs/MATCHING_SCREENS.md، db/migrations) |
| 2391 صنفاً في ~966ms | tech.md «Catalog sync» (docs/PROGRESS.md Lane C) |
| Bixolon SPP-R310 ✅ · Xprinter USB ❌ | tech.md «Real-hardware print test» (docs/PRINT_FIELD_TEST_2026-07-13.md) |
| حالة pilot، تدقيق مستقل، 4 عيوب P0، 9 شاشات ADR | tech.md «Status» (docs/FINAL_AUDIT_FABLE5.md 2026-07-03) |
| 170 commit · آخر commit 2026-07-13 | tech.md |
| شريحة المشكلة في الكاروسيل/الريل (3 بطاقات) | إعادة صياغة مباشرة لجملة brief «مقيّدة بعميل سطح مكتب فوق Oracle، وكل تعديل يهدّد قاعدة الإنتاج» — لا معلومة جديدة |
| البحث E — أسعار Foodics/Rewaa/Odoo وصفحات Onyx | روابط مؤرّخة 2026-09-23 داخل motech-pos-research.md |
| الرابط | github.com/moain2028/motech-pos (مهمة #10؛ HTTP 200 في 2026-09-23). لا رابط حي (tech.md) |

## ما لم يُستخدم عن قصد
- اسم النظام القديم (YemenSoft Onyx Pro) على أي تصميم أو نص نشر — يبقى في tech.md وفي ملف البحث فقط كمنافس (قرار brief + numbers-bank).
- «بديل كامل» — ممنوعة (numbers-bank: FINAL_AUDIT يقول pilot).
- الرقم القديم 306 اختباراً — يُوحَّد على 348.

## الهوية
02-brand/README.md؛ الشريحة شركات #3B82F6؛ النص الخافت #A3B1C0 (تحديث v2). بلا شعار في كل ملفات الملحق. الموسيقى: bgm-tech-minimal (داخلية، بلا حقوق طرف ثالث).

## الأداة (tools/)
`make_pack.py` (A، من v1 مع تحديث #A3B1C0) · `make_extras.py` (B) · `make_reel.py` (C).
