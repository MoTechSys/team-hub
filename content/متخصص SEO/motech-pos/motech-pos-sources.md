motech-pos | متخصص SEO | 2026-09-23 | v1

# مصادر كل نص ورقم على تصاميم motech-pos (design-pack v1)

المستودع المرجعي: https://github.com/moain2028/portfolio-hub → 01-projects/motech-pos/ و02-brand/README.md

| العنصر على التصميم | النص AR / EN | المصدر |
|---|---|---|
| العنوان H1 | «نقطة بيع ويب تحلّ محلّ نظام سطح مكتب قديم دون أن تكسره» / “A web point of sale that replaces a legacy desktop system without breaking it” | brief.ar.md / brief.en.md — عنوان الملف |
| اسم المشروع | Motech POS · motech-pos | brief.ar/en.md + tech.md |
| السطر التعريفي | «تطبيق ويب تقدّمي بـ React 19 على خادم NestJS يقرأ مخطط Oracle الحقيقي ويكتب في مخططه الخاص فقط، فيبقى الإنتاج للقراءة.» / “A React 19 PWA on a NestJS backend that reads the real Oracle schema and writes only to its own schema, so production stays untouched.” | brief.ar.md / brief.en.md — فقرة «الحل / Solution» (مقتطعة دون تغيير كلمات) |
| 348 — اختبار وحدة ناجحاً / unit tests green | brief «النتيجة/Result» · tech.md جدول الأرقام: docs/QA_SWEEP.md §6 · numbers-bank.md (348 يُوحَّد بدل 306) |
| 420 ms — نسخة احتياطية حيّة لـ 59 جدولاً / live backup of 59 tables | brief «النتيجة/Result» · tech.md: docs/PROGRESS.md Lane G proof (59 جدولاً / 2819 صفاً / 420ms) |
| 12 — كود صلاحية تُفرض وقت الطلب / permission codes enforced per request | brief «النتيجة/Result» · tech.md مصادر brief (docs/PROGRESS.md) |
| 0 — تمرير أفقي على 390 / 820 / 1440 / horizontal overflow at 390/820/1440 px | brief «النتيجة/Result» · tech.md: docs/QA_SWEEP.md §2 (160/160، 0 overflow) |
| تاجات التقنيات | React 19 · NestJS 10 · Oracle · TypeScript · PWA | tech.md «Primary language / stack» |
| الدعوة للتواصل (الفوتر) | «أُقدّم دراسة لترحيل نقطة البيع لديك — راسلني.» / “Let's scope your POS migration — DM or email.” | brief.ar.md / brief.en.md — سطر «تواصل / Contact» |
| الرابط (فوتر + شريط المتصفح) | github.com/moain2028/motech-pos | مهمة #10 (المستودع moain2028/motech-pos) · links.md؛ تحقق HTTP 200 في 2026-09-23. لا رابط حي: الدومين في الوثائق لا يستجيب (tech.md «Live URL: none») |
| شارة الشريحة | شركات / Companies · #3B82F6 | مهمة #10 · 02-brand/README.md ألوان الشرائح |
| الشعار النصّي (نسخة logo فقط) | «معين العباسي» / “Moain Al-Abbasi” — نص فقط بلا أيقونة | design-pack-standard-v1.md §2 |

## اللقطات (حقيقية من المستودع — لا شيء مولّد)
- ديسكتوب: `01-projects/motech-pos/screenshots/desktop-02-cart.png` (1440×900) — شاشة البيع مع سلة وفاتورة، داخل إطار متصفح.
- جوال: `01-projects/motech-pos/screenshots/mobile-04-cashier-expanded.png` (390×844) — قائمة الكاشير، داخل إطار جوال.
- الأصل: `pos-audit-shots/` في مستودع motech-pos (tech.md «Screenshots in repo»).

## الهوية
- الألوان Navy/Ink/Amber/Sand/Mist/Slate والخطوط IBM Plex Sans Arabic · Inter · JetBrains Mono من 02-brand/README.md + fonts/.
- التباين: Sand على Navy ≈ 13:1 · Amber على Navy ≈ 7.5:1 · Mist على Navy ≈ 10:1 — كلها فوق AA (02-brand/README.md §1).
- النسخة nologo: مساحة أمان خالية 12% من العرض أعلى-يسار (EN) / أعلى-يمين (AR)؛ لا شعار ولا أيقونة (standard §2).

## ما لم يُستخدم عن قصد
- اسم النظام القديم (YemenSoft Onyx Pro) — يبقى في tech.md، لا على التصاميم (قرار brief + numbers-bank).
- عبارة «بديل كامل» — ممنوعة بحسب numbers-bank.md (FINAL_AUDIT: pilot).
- الدومين الحي — معطّل.
- لا اسم عميل ولا شعار عميل.

## الأداة
`make_pack.py` (Python 3 + Pillow/raqm) مبني على `02-brand/scripts/brand.py`؛ يولّد الـ24 ملفاً بالمقاسات الدقيقة بأمر واحد — مرفق في الحزمة لإعادة التوليد بعد أي تعديل.
