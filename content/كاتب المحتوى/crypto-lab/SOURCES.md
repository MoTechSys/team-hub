crypto-lab | كاتب المحتوى | 2026-09-23 | project-pack v2

# crypto-lab project pack v2 — مصادر كل نص ورقم وصورة

المصدر الوحيد: portfolio-hub → 01-projects/crypto-lab/ (brief.ar.md · brief.en.md · tech.md · links.md · readme-source.md · screenshots/) + 02-brand/README.md. المستودع الأصلي MoTechSys/ahammad_manajy عام (200 بتاريخ 2026-09-23).

## A. التصاميم (24 PNG)
| العنصر | AR | EN | المصدر |
|---|---|---|---|
| العنوان / الثانوي | مختبر التشفير / Crypto Lab | Crypto Lab / مختبر التشفير | brief H1 |
| السطر التعريفي | تطبيق أندرويد يشرح أربع خوارزميات خطوة بخطوة | An Android app that explains four ciphers step by step | brief H1 |
| الشارة | يعمل بلا خادم | No server | brief «الحل» / «Solution» |
| الميزات (X/Hero/Story) | Caesar · Vigenère · RSA · AES-256-GCM بصرياً · حساب بتحقق OTP عبر البريد · دفتر تجارب SQLite مع سلة مهملات · قفل PIN أو بصمة وتصدير مشفّر | (مقابلها) | brief «الحل» |
| الأرقام الثلاثة | 4 خوارزميات · 54 اختباراً ناجحاً · 1.2.0 الإصدار | 4 ciphers · 54 passing tests · 1.2.0 release | brief «النتيجة»؛ tech.md «الأرقام» |
| شارة الشريحة | طلاب | Students | تكليف مدير المنتج؛ لون #8B5CF6 من 02-brand |
| التقنيات (فوتر) | Flutter · Dart · pointycastle · SQLite | | tech.md «التقنيات» |
| الرابط (فوتر) | github.com/MoTechSys/ahammad_manajy | | links.md — المستودع الأصلي العام؛ لا بديل عام آخر. اسم المستودع يحمل اسم شخص — إعادة التسمية (مثلاً crypto-lab) «يُستكمل من معين» (ملاحظة مدير المنتج 2026-09-23) |
| wordmark (logo فقط) | معين العباسي | Moain Al-Abbasi | معيار v2 §A |
| النص الخافت | #A3B1C0 | | معيار v2 «قواعد ثابتة» |

## B. تصاميم النشر (14 PNG)
- كاروسيل 5×AR + 5×EN: 1 المشكلة (brief «المشكلة») · 2 الحل (brief «الحل») · 3 كيف يعمل — الخطوات الأربع (brief «الحل»: جدول الإزاحة، تمديد المفتاح، توليد n وe وd، PBKDF2 والـ nonce وعلامة GCM) · 4 الأرقام: 4 · 54 · 1.2.0 موقّع · ~9 MB (brief «النتيجة») · 5 لمن/الدعوة (brief «لمن يفيد» + «تواصل»).
- بطاقة «رقم واحد» AR/EN: 4 — Caesar · Vigenère · RSA · AES-256-GCM + جملة من brief «الحل».
- بانر مقال 1600×840 AR/EN: kicker «مشروع طلابي · أمن سيبراني» (tech.md الشريحة) · عنوان من brief «لمن يفيد» · سطر من brief H1 + «الحل».

## C. الفيديو
- crypto-lab-reel-ar.mp4 · crypto-lab-reel-en.mp4 — 1080×1920، 30fps، H.264+AAC، 19.6 ث، 6 مشاهد، بلا شعار. + غلافان PNG.
- كل جملة في المشاهد من brief «الحل»/«النتيجة»/«لمن يفيد»/«تواصل»؛ «اشتقاق المفتاح بـ PBKDF2 مع الـ nonce وعلامة GCM» من brief؛ «~9 MB» من brief/tech.md.
- الموسيقى: 02-brand/scripts/reels/bgm-tech-minimal.mp3 — مولّدة آلياً بلا حقوق طرف ثالث (README خط الريلز، صانع الفيديو 2026-09-11).
- لا مشاهد خطأ/404: اللقطات حقيقية من screenshots/ (docs/screenshots في المستودع) بلا أي تعديل.

## الصور (كل ما استُخدم)
| الملف | الشاشة | أين |
|---|---|---|
| mobile-10-algorithm-picker.png | اختيار الخوارزمية (الأربع) | مركز المروحة في A، كاروسيل 1، ريل 00/01 |
| mobile-11-aes.png | AES-256-GCM بالخطوات | A، كاروسيل 2/3، بانر، ريل 00/02 |
| mobile-12-passphrase-meter.png | مقياس قوة كلمة السر | A، كاروسيل 5، بانر، ريل 02/99 |
| mobile-05-otp.png | تحقق OTP | ريل 03 |
- مصدر اللقطات: screenshots/index.md — «الأصلية من المستودع نفسه (يوثّقها README)»، 500×757. لم تُشغَّل نسخة محلية ولم تُولَّد أي لقطة.
- استُبعدت عمداً: splash (01)، home (06/07)، drawer (08/09) — تحمل اسم الطالب «أحمد مناجي» الذي ينبّه brief وtech.md إلى عدم ذكره قبل إقرار معين.

## D/E/F. النصوص
- explainer AR/EN: كل جملة من brief + tech.md + readme-source.md (المصادر في تذييل كل ملف). 430/450 كلمة.
- research.md: 3 تطبيقات Play Store فعلية (Nitramite · Softecks · Creofakur) بأرقام التنزيلات والتقييم وآخر تحديث من صفحاتها بتاريخ 2026-09-23، + 3 بدائل مرجعية (CrypTool، cryptii، CryptoTools)؛ كل الروابط ردّت 200؛ ادعاءات مشروعنا من tech.md فقط.
- copy AR/EN: LinkedIn 104/108 كلمة · X 232/236 حرفاً · IG 118/112 كلمة · نص الريل — كلها من brief. حالة draft-for-editor.

## ما لم يُذكر عمداً
أرقام مستخدمين/تنزيلات (tech.md: يُستكمل) · اسم الطالب ودور معين (بانتظار الإقرار) · «Android 6.0/API 23» (متضارب مع tech.md API 24 لـ v1.2.0 — اعتُمد الأحدث ولم يُعرض على التصاميم) · «صفر تحذيرات» على التصاميم (ضيق مساحة؛ موجود في النصوص).

## الأدوات
packgen.py + project.py (Pillow + raqm فوق 02-brand/scripts/brand.py) · reelgen.py (ffmpeg، خط الإنتاج مقتبس من 02-brand/scripts/reels/reel.py) — مرفقة في tools/ لإعادة التوليد.
