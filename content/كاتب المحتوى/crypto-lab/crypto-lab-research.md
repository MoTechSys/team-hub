crypto-lab | كاتب المحتوى | 2026-09-23 | v1

# مختبر التشفير — بحث وتحليل (Research & positioning)

تاريخ البحث: 2026-09-23 (بحث ويب + فتح الصفحات والتحقق من استجابتها 200). كل ادعاء عن مشروعنا من tech.md/brief؛ كل ادعاء عن منافس من رابطه المذكور.

## 1. من يشتري هذا؟ (تحليل سوق مختصر)
- المستخدم: طالب مقرر أمن سيبراني أو مشروع تخرج يحتاج أداة تُظهر خطوات الخوارزمية لا نتيجتها؛ والمدرّس الذي يريد أداة عرض صفّية بالعربية (tech.md «المشكلة»).
- المشتري الفعلي في المحفظة: ليس الطالب، بل من يطلب من معين بناء مشروع تخرج/مقرر مشابه (brief «لمن يفيد» + cta الريل السابق). الشريحة: طلاب.
- حجم الفئة: لا رقم موثّق لدينا لعدد طلاب الأمن السيبراني العرب — «يُستكمل». مؤشر غير مباشر: تطبيق Cryptography (Softecks) على Google Play يتجاوز 5,000 تنزيل مع إعلانات (رابط أدناه) — فئة موجودة لكنها صغيرة.

## 2. المنافسون والبدائل (بروابط حقيقية، وصول 2026-09-23)

### 2أ. تطبيقات تعليم التشفير الفعلية على Google Play (المنافس المباشر — نفس المنصة)
| # | التطبيق | المطوّر | التنزيلات | التقييم | آخر تحديث | ماذا يقدّم (من صفحته) | الرابط |
|---|---|---|---|---|---|---|---|
| 1 | Cryptography | Nitramite | 500K+ | 4.5 | 2026-07-22 | «all-in-one toolkit for exploring, learning, and experimenting» — عشرات الشفرات الكلاسيكية (Caesar، Vigenère، Playfair، Adfgvx…) + هاش وترميز؛ مفتوح المصدر؛ يحتوي إعلانات ومشتريات داخلية؛ أداة نتائج لا شرح خطوات | https://play.google.com/store/apps/details?id=com.nitramite.cryptography |
| 2 | Cryptography (Softecks) | Softecks | 5K+ | 4.6 | 2026-09-12 | «educational security app for students… structured cryptography lessons» — دروس نصية مهيكلة (كلاسيكي، AES، RSA، PKI، هاش) + أدوات؛ إعلانات؛ تعلّم بالقراءة لا بتصوير الخطوات | https://play.google.com/store/apps/details?id=in.softecks.cryptography |
| 3 | Kriptografi | Creofakur | 1K+ | — | 2026-07-26 | «classical cryptographic algorithms… encryption and decryption» — Caesar، Vigenère، Playfair، Hill، Enigma، AES، DES؛ إعلانات؛ تشفير/فك فقط | https://play.google.com/store/apps/details?id=com.creofakur.kriptografi |

الأرقام (تنزيلات/تقييم/تاريخ) قُرئت من صفحات Play Store بتاريخ 2026-09-23 وتتغيّر مع الوقت.

### 2ب. بدائل خارج Play Store (مرجعية)
| البديل | ماذا هو | الرابط | ماذا يقول عن نفسه |
|---|---|---|---|
| CrypTool 2 / CrypTool-Online | برنامج تعليمي مفتوح المصدر لتصوير التشفير وتحليله (Windows) + نسخة ويب فيها «RSA خطوة بخطوة» | https://www.cryptool.org/en/ct2/ · https://www.cryptool.org/en/cto/ | «modern learning program for Windows that visualizes cryptography and cryptanalysis» |
| cryptii | تطبيق ويب مفتوح المصدر (MIT): Caesar، Vigenère، Enigma… بلا خادم | https://cryptii.com/ | «Open Source project, code licensed MIT» — نتائج لا خطوات |
| أدوات التشفير — CryptoTools (إيهاب قهواتي) | منصة ويب عربية مفتوحة المصدر: AES، RSA، Hash، Base64 محلياً في المتصفح | https://devehab.github.io/CryptoTools/ | «مصممة خصيصاً للمتحدثين باللغة العربية لتعلم أساسيات التشفير» |

ملاحظة: dCode.fr بديل شهير لكن صفحته ردّت 403 على الفحص الآلي فلم أعتمده كمصدر.

## 3. التموضع
ماذا يقول المنافس: على Play Store، Nitramite هو الأكبر (500K+) وهو «صندوق أدوات» بعشرات الشفرات لكنه يُعطي النتيجة لا الخطوات وفيه إعلانات؛ Softecks «دروس مهيكلة» — تعلّم بالقراءة والمراجعة، لا بتشغيل الخوارزمية أمامك؛ Kriptografi آلة تشفير/فك للشفرات الكلاسيكية. خارج المتجر: CrypTool أقوى أكاديمياً لكنه Windows/ويب وبالإنجليزية والألمانية أساساً؛ cryptii «أداة نتيجة»؛ CryptoTools عربي لكنه ويب دون الخوارزميات الكلاسيكية ودون شرح الخطوات. لم أجد في البحث تطبيق أندرويد عربي RTL يعرض خطوات الخوارزمية بصرياً.

أين يتفوّق مختبر التشفير (من tech.md فقط):
- الوحيد بين ما وُجد كتطبيق أندرويد عربي RTL كامل يعرض خطوات الخوارزمية (جدول الإزاحة، تمديد المفتاح، p·q·n·φ·e·d، PBKDF2/nonce/GCM tag).
- يجمع الكلاسيكي (Caesar، Vigenère) والحديث (RSA، AES-256-GCM حقيقي عبر pointycastle) في تطبيق واحد.
- «مختبر» لا «آلة حاسبة»: دفتر تجارب SQLite، سلة مهملات، تصدير مشفّر، حساب OTP، قفل PIN/بصمة — يحاكي منتجاً حقيقياً لا تمريناً.
- مفتوح المصدر، بلا خادم، بلا إعلانات، 54 اختباراً وصفر تحذيرات.

أين يتأخر (صريح): 4 خوارزميات مقابل عشرات في Nitramite/Kriptografi ومئات في CrypTool · لا تحليل شفرات حقيقي (Caesar brute-force فقط) · غير منشور على Play Store أصلاً (APK من GitHub فقط) مقابل 500K+ تنزيل للمنافس الأكبر · أندرويد فقط بلا ويب/iOS · لا مجتمع ولا تنزيلات موثّقة.

## 4. الكلمات المفتاحية
AR (10): تعلم التشفير · خوارزميات التشفير خطوة بخطوة · تطبيق تشفير تعليمي · مشروع تخرج أمن سيبراني · شرح خوارزمية RSA · شرح AES-256 · شيفرة قيصر · شيفرة فيجينير · تطبيق Flutter عربي · مشروع مقرر أمن المعلومات
EN (10): learn cryptography app · cipher visualizer · RSA step by step · AES-256-GCM explained · Caesar cipher app · Vigenère cipher tutorial · cryptography capstone project · Flutter security app · offline encryption learning · Arabic cryptography app

## 5. ثلاث زوايا محتوى
1. «لماذا يحفظ الطالب التشفير بدل أن يفهمه؟» — زاوية المشكلة التعليمية، تنتهي بلقطة خطوات RSA.
2. «AES حقيقي في تطبيق طلابي: PBKDF2 بعشرة آلاف دورة، nonce 96 بت، tag 128 بت» — زاوية تقنية للمهندسين والمدرّسين.
3. «مشروع تخرج يبدو كمنتج: OTP، قفل بصمة، سلة مهملات، تصدير مشفّر» — زاوية لطلاب يريدون مشروع تخرج يُدافع عنه أمام اللجنة.

## 6. الفجوات (بلا تجميل)
تقنياً: README/CHANGELOG عند 1.0.0 والكود عند 1.2.0 · لا لقطات 2x · اسم المستودع باسم الطالب (ahammad_manajy) لا المنتج · لا ويب/iOS · RSA نموذج مدرسي (أعداد أولية 257–1000) لا يصلح لتشفير فعلي (وهذا مُعلَن) · لا اختبارات واجهة.
تسويقياً: دور معين غير موثّق (README ينسب التطوير للطالب) — لا يُكتب «بنيتُ» قبل إقراره · لا أرقام مستخدمين/تنزيلات · لا صفحة/متجر · لا فيديو تشغيل حقيقي على جهاز.

## 7. المصادر
- المشروع: https://github.com/MoTechSys/ahammad_manajy (200) · https://github.com/MoTechSys/ahammad_manajy/releases/tag/v1.2.0 (200) · portfolio-hub/01-projects/crypto-lab/{brief.ar.md, brief.en.md, tech.md, links.md, readme-source.md}
- المنافسون: الروابط في الجداول أعلاه، كلها ردّت 200 بتاريخ 2026-09-23؛ أرقام Play Store (التنزيلات، التقييم، آخر تحديث، الإعلانات) قُرئت من صفحة كل تطبيق بـ hl=en في نفس التاريخ.

## EN summary
Crypto Lab targets Arabic-speaking cybersecurity students and capstone teams. Direct Play Store competitors (accessed 2026-09-23): Nitramite's Cryptography (500K+, 4.5★, dozens of ciphers, results-only, ads + IAP), Softecks' Cryptography (5K+, 4.6★, structured text lessons, ads), Creofakur's Kriptografi (1K+, classical encrypt/decrypt, ads). Reference alternatives: CrypTool 2 / CrypTool-Online (academic, Windows/web, English-first), cryptii (MIT web tool, output-only), CryptoTools by Ehab Kahwati (Arabic web, AES/RSA/hash, no step-by-step). Crypto Lab is the only Android, Arabic-RTL, step-by-step visualizer covering both classical and modern ciphers with real AES-256-GCM, a SQLite notebook, OTP accounts and PIN/biometric lock, open source, no server, 54 tests. Gaps: not on Play Store (APK via GitHub only), docs lag the code (1.0.0 vs 1.2.0), repo named after the student, Moain's role undocumented, no user numbers, Android-only, toy RSA, 4 ciphers vs dozens in competitors.
