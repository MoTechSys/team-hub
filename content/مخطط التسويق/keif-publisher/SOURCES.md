keif-publisher | مخطط التسويق | 2026-09-23 | v2

# SOURCES.md — مصدر كل نص ورقم وصورة في keif-publisher-project-pack-v2

المشروع لم يكن في portfolio-hub؛ البند 0 أنتج `project/` (brief.ar/en.md · tech.md · links.md · screenshots/ 17 لقطة) — المصدر الأساسي لكل ما يلي، مع الكود في https://github.com/moain2028/keif-publisher (commit d969916، 2026-08-11) وتشغيل محلي dry-run بتاريخ 2026-09-23.

## A. النصوص والأرقام على التصاميم
| العنصر | المصدر |
|---|---|
| الاسم «keif-publisher» | اسم المستودع (README: «محرّك نشر تلقائي لكيف الضيافة» — اسم العلامة لم يوضع في العنوان عمداً) |
| العنوان «نشر آلي على 8 منصات لا ينشر شيئاً قبل موافقة إنسان» | README «بوابة موافقة بشرية» + «الافتراضي الآمن» + `db.PLATFORMS` (8) |
| السطر الوصفي (توليد → 14 قاعدة → 3 طبقات → مجدول → مفتاح إيقاف) | README السطر 3 + «بوابة الموافقة — 3 طبقات» + «كيف يُوقف النظام» |
| 210 اختباراً | `pytest -p no:cacheprovider -rN` 2026-09-23 → «210 passed in 25.19s» (لقطة desktop-11-cli-pytest) |
| 8 ناشرين | `ls keifpub/publishers` (8 ملفات منصة) · `db.PLATFORMS` |
| 3 طبقات موافقة | README + الكود: `generate.py` (يكتب pending_review فقط) · `web/app.py approve` (يرفض errors) · `cli.py cmd_publish --live` (kill switch/حالة/أخطاء) |
| 14 قاعدة علامة | `brand.py BANNED_PATTERNS` (14 صفاً) |
| 7 حالات منشور | `db.STATUSES` |
| 3 محاولات ثم فشل | `publishers/base.py max_attempts = 3` · README «failed (بعد 3 محاولات)» |
| 9:16 | `base.py MediaSpec.aspect` · README |
| «رفع بالواو · سعر · بلا مدينة · بلا جوال → مرفوض» (كاروسيل 3/ريل 3) | مخرجات `cli brandcheck` الحقيقية (لقطة desktop-08) + `brand.py` |
| تاجات: Python · FastAPI · SQLite · APScheduler · ffmpeg | 02-TECH-FACTS «الحزم» + `web/app.py` + `scheduler.py` + `media/vertical.py` |
| شارة الشريحة: شركات / Companies | تكليف مدير المنتج msg 4617110 + 02-brand SEGMENTS |
| الفوتر github.com/moain2028/keif-publisher | تكليف مدير المنتج |
| wordmark «معين العباسي / Moain Al-Abbasi» (نسخ logo فقط) | project-pack-standard-v2 §A |
| بطاقة الرقم «3 طبقات موافقة لا تُتجاوز» | README «بوابة الموافقة — 3 طبقات لا تُتجاوز» |
| البانر «أتمتة النشر بلا مخاطرة…» | عنوان مقال مقترح (زاوية 1 في research) |
| 9,271 سطر · 5 جداول · 11 مساراً · 7 أوامر (brief/explainer فقط) | `git ls-files '*.py' \| xargs wc -l` · `db.py` · `web/app.py` · `cli.py` |

## B. الصور (كلها لقطات حقيقية من تشغيل محلي 2026-09-23، Playwright Chromium، DPR 2)
| الاستخدام | الملف | ملاحظة |
|---|---|---|
| القطع الست، كاروسيل 1–2، البانر، غلاف الريل، الريل 2 | desktop-01-queue / mobile-01-queue | طابور اللوحة |
| كاروسيل 3، كاروسيل 5، الريل 3 | desktop-03-post-rejected / mobile-03-post-rejected | تفاصيل منشور مرفوض بأخطاء العلامة الأربعة |
| كاروسيل 4 | desktop-07-cli-status | مخرجات `cli status` الحقيقية (kill switch مفعّل، 8 منصات بقدراتها) في بطاقة طرفية |
| الريل 4، 5 | mobile-02-queue-pending / mobile-06-log | |
| **بيانات داخل اللقطات** | 7 منشورات «منشور تجريبي N»، حسابات `demo.*`، `demo-batch-01`، `demo-01.mp4`/`demo-02.jpg`، الجوال `05XXXXXXXX`، «user:reviewer»، أوقات 2026-09-23 | **بيانات عرض** من `make/seed_demo.py` — قاعدة البيانات تبدأ فارغة؛ الأصلان ملفان مولَّدان بـ ffmpeg/Pillow (لون أزرق ثابت) **ليسا من أرشيف العميل**؛ لا رقم منها على أي تصميم |
| «كيف الضيافة · لوحة النشر» في رأس اللوحة | `web/templates/base.html` الأصلي | اسم جهة معروفة على المنصة — مسموح؛ لا أشخاص |
| أسماء متغيرات المفاتيح (FB_PAGE_TOKEN…) في بطاقة status | مخرجات الأمر الحقيقية | أسماء متغيرات فقط — لا قيمة سرّية موجودة أصلاً (لم يُدخل أي مفتاح) |
| كابشن «قهوجيون محترفون يبدأ من 500 ريال» | من `tests/test_web_scheduler.py BAD_CAPTION` (نص اختبار في المستودع) | مثال رفض مقصود |
| بطاقات الطرفية | قالب HTML داكن في shoot.py يعرض المخرجات بايت-ببايت (`make/_cli_outputs.json`) | لا نص مُختلق |
| الخلفيات/الشبكة/التوهج | مولّدة برمجياً (02-brand/scripts/brand.py) | لا صور مخزون، لا لقطة مولّدة بالذكاء الاصطناعي |

## C. الصوت
- الريلان: نفس المقطع الموسيقي الآلي المولّد (CassetteAI/music-generator، 24 ث، 2026-09-23) المستخدم في حزمي السابقة لتوحيد صوت المحفظة؛ بلا حقوق طرف ثالث. التذييل على كل مشهد (packlib.reel_frame، منذ v1.1 لـ #49).

## D. ملفات البحث والنص
- `research.md`: Buffer، Postiz (+GitHub AGPL-3.0)، n8n — بروابط وتاريخ وصول 2026-09-23؛ قيود منصات النشر من 02-TECH-FACTS (وثيقة المستودع).
- `explainer.ar/en.md`، `copy.ar/en.md`: كل جملة من brief/tech/README/الكود؛ draft حتى ختم المحرر.

## E. طريقة التشغيل (make/)
- `seed_demo.py`: بيانات العرض. `shoot.py`: التصوير (اللوحة على :8770 + بطاقات CLI). `build.py` + `packlib.py`: التصاميم. `make_reel.sh`: الريل. `_cli_outputs.json`: المخرجات الخام المستخدمة في البطاقات. `pytest-summary.txt`: سطر نتيجة الاختبارات.
- البيئة: `.env` من `.env.example` + `KEIFPUB_LLM=offline` + مسارات محلية؛ `KEIFPUB_PUBLISHING_ENABLED=0` طوال العمل. **لم يُغيَّر أي ملف في المستودع** (ملفا العرض أُنشئا في tests/reels و tests/photos داخل نسخة العمل المحلية فقط، غير متعقَّبين).

## F. ما لم يُستخدم عمداً
- «10 ناشرين» (التكليف) و«183 اختباراً» (عدّ الدوال) — الفعلي 8 و210.
- أي ادعاء «ينشر على المنصات» كمنجَز — لم يُربط حساب؛ الصياغة «ناشرين بقدرات معلنة».
- أرقام الجوال التجريبية في الكود (0555…) — استُخدم placeholder README `05XXXXXXXX` فقط.
- أي صورة/فيديو من أرشيف العميل الحقيقي؛ أي اسم شخص أو مفتاح.
- مسارات VM المطوّر.

## G. التباين
- النصوص على الخلفية الداكنة: White/#F2F2F2 و#A3B1C0 (الخافت المعتمد) على Navy — AA فأعلى؛ الشارة الصفراء الوسطى للشريحة بنص Navy؛ لا نص مقطوع (فحص بصري لـ LinkedIn AR، كاروسيل 3 AR، مقاسات الـ40 آلياً).
