linkhub-3d | صانع الصور | 2026-09-23 | ready

# مصادر كل نص ورقم وصورة في الحزمة

المصدر الأصلي الوحيد: مستودع github.com/moain2028/linkhub-3d (commit abd0989، 2026-08-21) مستنسخاً ومقيساً محلياً 2026-09-23 (project/tech.md) + فحص حي عبر Playwright (project/screenshots/linkhub-audit.json). كل رقم في README أُعيد قياسه هنا؛ لا رقم من README وحده.

## A. التصاميم (24 PNG) + B. الكاروسيل/البطاقة/البانر (14 PNG)
| العنصر | المصدر |
|---|---|
| العنوان "LinkHub 3D" | README H1 |
| اسم المستودع linkhub-3d | التكليف |
| الجملة التعريفية «صفحة روابط ببطاقات ثلاثية الأبعاد حقيقية بلا أي إطار» / "A link-in-bio page with real 3D cards and no framework" | brief.ar/en.md H1 ← README «بطاقات ثلاثية الأبعاد حقيقية … بلا أي إطار» |
| الوصف (ملف واحد، بطاقة مادية بسُمك ولمعة، انقلاب 3D، حلقة 900ms، تحوّل الصفحة، يعمل بلا JS) | brief الحل ← README «التفاعل» 1–3 و«الخامة» و«المبادئ»؛ audit flip_transform/body_bg |
| 8.4 KB الصفحة كاملة مضغوطة | tech.md: `gzip -9 -c keif/index.html \| wc -c` = 8,448 B (أصول 7,961 B = 8.0 KB) — يطابق README |
| 0 طلبات خارجية | linkhub-audit.json external_requests = [] للصفحتَين (6/7 طلبات كلها محلية) |
| 15 طبقة خامة على وجه البطاقة | audit face_bg_layers (كيف) = 15 — يطابق README؛ أصول 17 |
| 4.64:1 أدنى تباين — الكل يمرّ WCAG | `python3 keif/contrast-v2.py` من المستودع → ALL PASS، الأدنى 4.64 (instagram accent2 على السطح) |
| 844=844 شاشة واحدة بلا تمرير | audit one_screen scrollH 844 = viewportH 844 (390×844) |
| السطر الخافت «انقلاب rotateY حقيقي · شاشة واحدة بلا تمرير · تباين WCAG يمرّ كله · يعمل بلا JS» | audit flip_transform matrix3d(-1,…) · one_screen · contrast scripts · cards_with_href 8/8 و6/6 |
| التاجات Vanilla JS · CSS 3D · SVG inline · AVIF | README «التقنية»، «الشعارات SVG inline»؛ `<picture>` AVIF في index.html |
| شارة الشريحة «مشاريع صغيرة» / "Small business" ولونها #F4A62A | التكليف + 02-brand/README.md |
| الفوتر github.com/moain2028/linkhub-3d (يسار) و«CSS 3D · 0 requests · no framework» (يمين) | التكليف (مستودع عام) · tech.md؛ لا رابط حي (links.md) |
| شريط عنوان إطار المتصفح «linkhub-3d · keif / asoul» | تسمية وصفية لا نطاقاً حياً |
| كاروسيل 1 (المشكلة) | brief المشكلة ← docs/00 «الطلب» + research §2 |
| كاروسيل 2 (الحل: تنقلب وتُلوّن الصفحة) | README «التفاعل» + audit |
| كاروسيل 3 (rotateY/perspective/preserve-3d/backface، translateZ ±3.5px، specular بلا rAF، feTurbulence، `<a href>` بلا JS) | README «التفاعل» 1، «الخامة»، «المبادئ»؛ `grep` index.html (3 rotateY، 2 preserve-3d، 2 backface، 2 feTurbulence) |
| كاروسيل 4 الأرقام (8.4 KB · 0 · 15 · 4.64:1) | tech.md الأرقام ومصادرها |
| كاروسيل 5 الدعوة «صفحة روابطك قالب مثل الجميع؟ راسلني…» | brief.ar/en للتواصل |
| بطاقة الرقم الواحد «0 طلبات خارجية» + «صفحة روابط كاملة بـ 8.4 KB مضغوطة» + السطر (woff2 محلية · SVG مضمّنة · AVIF/WebP محلية) | audit + README «الخطوط woff2 محلية»، «الشعارات SVG inline»؛ `ls keif/img` |
| الاسم النصّي «معين العباسي / Moain Al-Abbasi» في نسخة logo فقط | معيار v2 §A |
| النص الخافت #A3B1C0 | معيار v2 (تحديث 2026-09-23) |

## الصور (كلها لقطات/تسجيلات حقيقية من التشغيل المحلي — لا صورة مولّدة أُضيفت)
| الملف | ماذا يعرض | كيف أُخذ |
|---|---|---|
| desktop-keif-01-base.png | صفحة كيف 1440×900 @2x — لقطة الديسكتوب الأساسية في A/B | shoot.py desktop، http.server محلي، Playwright/Chromium؛ الهواتف مطموسة قبل الالتقاط |
| mobile-keif-flip-instagram-b-themed.png | بطاقة إنستقرام منقلبة + حلقة + الصفحة كاملة بثيم إنستقرام 390×844 @2x — لقطة الجوال الأساسية | shoot.py flip: نقر + إطالة الانتقالات + تعطيل مؤقّت الانتقال |
| mobile-asoul-01-base.png · mobile-asoul-flip-{snapchat,instagram}-b-themed.png · mobile-keif-flip-{tiktok,whatsapp}-b-themed.png · desktop-keif-02-hover-tilt.png | صفحة أصول قاعدة؛ ثيمات سناب/إنستقرام/تيك توك/واتساب؛ ميل hover على الديسكتوب | shoot.py mobile/flip/desktop |
| بقية الـ 18 لقطة في project/screenshots | قواعد وصفحات كاملة، منتصف الانقلاب (-a-mid)، الاستعادة بعد Escape | shoot.py |
| video/interaction-{keif,asoul}-390x844.mp4 (≈13.8 ث) | تسجيل Playwright فعلي: نقر → انقلاب + حلقة + ثيم → Escape، 3 منصات لكل علامة | shoot.py video → ffmpeg -ss 1.6 (قصّ ما قبل الطمس) → mp4 |
| **إفصاح**: صور الهيرو والشعاران داخل الصفحتَين | من أصول العلامتَين في المستودع (`assetsFrom` بطاقات VIP سابقة، logo-512.webp، SVG data-URI) — أصلها غير موثّق في المستودع؛ ليست مولّدة هنا | tech.md «ملاحظات التنظيف» |
| حسابات السوشيال (@handles) الظاهرة في اللقطات | هويات علنية للعلامتَين كما في HTML؛ لم تُطمس، ولا تُذكر في أي نص من الحزمة | تكليف مدير المنتج (نمط تقني) |

## C. الفيديو
video/linkhub-3d-reel-ar.mp4 و-en.mp4 (24.0 ث، 1080×1920، بلا شعار، ساحة أمان 12%): غلاف + المشكلة (لقطة) + الحل (**مقطع فيديو حقيقي** لكيف داخل إطار هاتف) + الخامة (**مقطع فيديو حقيقي** لأصول) + أرقام + دعوة «راسلني/DM me». المدد 3·3·6·6·4·4. لا مشهد خطأ. الموسيقى 02-brand/scripts/reels/bgm-tech-minimal.mp3. الأداة tools/reel_nologo.py (أُضيف دعم `clip` لتركيب فيديو داخل إطار الهاتف) + reel-ar/en.json.

## D. الشروحات
linkhub-3d-explainer.ar.md (≈600 كلمة) و.en.md (≈700) + خلاصة 5 نقاط — كل فقرة تحمل مصدرها (README/docs/02/tech.md/audit).

## E. البحث
linkhub-3d-research.md — 3 بدائل بروابط فُتحت 2026-09-23 (Linktree، Beacons، Later Link in Bio) باقتباسات من صفحاتها، تموضع، 10+10 كلمات، 3 زوايا، فجوات صريحة (commit واحد، لا تحليلات، روابط ميتة، تنظيف docs/03).

## F. نصوص النشر
linkhub-3d-copy.ar/en.md — LinkedIn 99/≈118 كلمة، X 201/236 حرفاً، IG 85/124 كلمة، نص الريل كما رُندر. زر الدعوة «راسلني/DM me». draft حتى ختم المحرر.

## التباين (WCAG) في تصاميمنا
Sand/Navy 13.4 · Mist/Navy 11.3 · Amber/Navy 7.2 · Ink/Amber 8.9 · #A3B1C0/Navy ≈ 7.0 — كلها AA فأعلى.

## ما لم يُعرض عمداً
- رقمَا الواتساب/الهاتف للعلامتَين (HTML، aria-label، JSON-LD، data.json) — مطموسان في كل لقطة وفيديو، غائبان عن كل نص.
- الرابطان «الحيّان» suppdizl.gensparkclaw.com/lnk/* — لا يستجيبان؛ لا يُعرضان.
- اسمَا العلامتَين في نصوص الحزمة — المشروع يُقدَّم كنمط تقني؛ يظهران داخل اللقطات فقط كما في الصفحة.
- محتوى docs/03-NEXT-TASK (توكنات مكشوفة سابقاً، مستودعات خاصة) — لا يُنقل؛ يُنبَّه المالك.
- «19 أيقونة»/«شاشة واحدة عند 932 و900» من README — لم تُقَس هنا فلم تُعرض.
- Lighthouse — غير متاح؛ استُبدل بفحص Playwright موثّق.
