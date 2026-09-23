keif-blins-invoices | متخصص SEO | 2026-09-23 | v2

# SOURCES — مصدر كل نص ورقم وصورة في keif-blins-invoices-project-pack-v2

المرجع: https://github.com/moain2028/portfolio-hub → `01-projects/keif-blins-invoices/` (brief.ar.md · brief.en.md · tech.md · links.md · tech-designer.md · screenshots/) + README المستودع الأصلي https://github.com/moain2028/keif_blins (نسخة عامة من MoTechSys/keif_blins) + `02-brand/README.md`.

## الصور (كلها حقيقية من المستودع — لا شيء مولّد)
| الملف في الحزمة | الأصل | ملاحظة |
|---|---|---|
| الفاتورة (البطل في كل التصاميم والريل) | `screenshots/doc-01-invoice.jpg` ← `docs/renders/invoice_p1.jpg` في المستودع | معاينة PDF حقيقية من اختبارات المشروع؛ البيانات فيها **بيانات اختبار/seed** (اسم عميل تجريبي «شركة هنفرستيشن» وأرقام تجريبية) كما هي في المستودع — ليست عميلاً حقيقياً |
| عرض السعر (مشهد المشكلة في الريل، خافت) | `screenshots/doc-02-quotation.jpg` | seed كذلك |
| الكشف التفصيلي | `screenshots/doc-04-statement-detailed.jpg` ← `docs/renders/statement_detailed_*.jpg` | seed |
| سند القبض A5 | `screenshots/doc-05-receipt.jpg` ← `docs/renders/receipt_*.jpg` | seed |
| لقطات واجهة التطبيق | — | غير موجودة في المستودع (tech.md «يُستكمل») فلم تُستخدم ولم تُولَّد |

## النصوص والأرقام
| العنصر | AR / EN | المصدر |
|---|---|---|
| العنوان H1 (A، B، C، D) | «فاتورة وعرض سعر وسند قبض رسمي من الجوال» / “Official invoices, quotes, and receipts from a phone” | brief.ar.md / brief.en.md — عنوان الملف |
| اسم المشروع | فواتير كيف الضيافة / Keif Al-Diafa Invoices · keif-blins-invoices | brief.ar/en.md |
| السطر التعريفي | «تطبيق أندرويد بـ Flutter يعمل محلياً بلا خادم: فواتير وعروض أسعار ببنود، سندات قبض، كشوف حساب، كلها بصيغة PDF رسمية مع تفقيط عربي ومشاركة عبر واتساب.» / EN equivalent | brief «الحل / Solution» (مقتطع دون تغيير كلمات) |
| 2.2.0 — الإصدار المنشور (APK) | brief «النتيجة/Result» · README (2.2.0+4) · pubspec |
| 32 — اختباراً ناجحاً / passing tests | brief · README «All tests passed (32)» · tech.md |
| 0 — تحذيرات في فحص الكود / analyzer issues | brief «صفر تحذيرات» · README «flutter analyze: No issues found» |
| 10.9 MB — حجم APK تقريباً | brief · README «arm64 ≈ 10.9 MB» |
| 5.6k — سطر Dart (B شريحة الأرقام، بطاقة الرقم، C) | brief «5.6 ألف سطر Dart» · README «5.6k سطر Dart» |
| 4 — أنواع مستندات PDF (B، C) | tech.md «Document types: 4» · README جدول المستندات |
| تاجات التقنيات | Flutter 3.35 · Dart · Hive · pdf 3.12 · Android | tech.md «Primary language / stack» |
| الدعوة للتواصل | «حمّل APK من صفحة الإصدارات وجرّبه.» / “Download the APK from the releases page and try it.” | brief «تواصل / Contact» |
| الرابط على التصاميم | github.com/moain2028/keif_blins | مهمة #19 (المستودع moain2028/keif_blins) · تحقق HTTP 200 في 2026-09-23. صفحة الإصدار الفعلية: github.com/MoTechSys/keif_blins/releases/tag/v2.2.0 (links.md) |
| شارة الشريحة | أفراد / Individuals · #22B08A | مهمة #19 · 02-brand/README.md |
| الشعار النصّي (نسخة logo فقط في A) | «معين العباسي» / “Moain Al-Abbasi” نصاً بلا أيقونة | project-pack-standard-v2 §A |
| الكاروسيل — شريحة المشكلة | «فواتير وعروض وسندات تُكتب باليد» + 3 بطاقات (فاتورة باليد · دفعة لم تُسجَّل · كشف من الذاكرة) | إعادة صياغة مباشرة لجملة brief «تُصدر … يدوياً، وتنسى المدفوعات، وتحتاج كشف حساب لكل عميل في نهاية الشهر» — لا معلومة جديدة |
| الكاروسيل — كيف يعمل | تفقيط، ضريبة اختيارية، PIN، سلة محذوفات، JSON، واتساب، مجلد بالنوع والسنة | brief «الحل» + «النتيجة» |
| الشرح D | كل الجمل | brief + tech.md + README + tech-designer.md (مذكورة داخل الملف) |
| البحث E | أسعار وحدود Zoho Invoice / Invoice Simple / Wafeq | روابط مؤرّخة 2026-09-23 داخل الملف |
| النصوص F | LinkedIn / X / IG / نص الريل | brief حرفياً + tech.md (5.6k، 4) |

## الهوية
- الألوان والخطوط من 02-brand/README.md؛ لون الشريحة أفراد #22B08A؛ النص الخافت #A3B1C0 (تحديث v2 بدل Slate). التباين: Sand على Navy ≈ 13:1 · Amber ≈ 7.5:1 · Mist ≈ 10:1 · #A3B1C0 ≈ 6.9:1 — كلها فوق AA.
- nologo: مساحة أمان 12% من العرض خالية أعلى-يمين (AR) / أعلى-يسار (EN)؛ لا شعار ولا أيقونة. نسخة logo: الاسم نصاً فقط.
- الموسيقى في الريل: `02-brand/scripts/reels/bgm-tech-minimal.mp3` — مولّدة داخلياً (Lyria) بلا حقوق طرف ثالث (02-brand/scripts/reels/README.md).

## ما لم يُستخدم عن قصد
- اسم عميل حقيقي — لا يوجد على أي تصميم (اسم «كيف الضيافة» هو اسم المشروع نفسه بحسب brief؛ البيانات داخل المستندات seed).
- الأرقام المتضاربة: tech-designer يذكر ≈9.7k سطر شامل الاختبارات مقابل 5.6k في README/brief — عُرض 5.6k فقط (المعتمد في brief المختوم).
- رابط حي — لا يوجد (تطبيق أندرويد).

## الأداة (tools/)
`make_pack_kb.py` (A) · `make_extras.py` (B) · `make_reel.py` (C) — Python 3 + Pillow/raqm + ffmpeg، مبنية على `02-brand/scripts/brand.py`؛ تُعيد إخراج كل شيء بأمر واحد بعد أي ملاحظة.
