motech-platform | مهندس | 2026-09-23 | project-pack v2 (A مُعاد توليده + B–G)

# مصادر كل نص ورقم على التصاميم (قاعدة الحقيقة — المعيار §4)

المستودع المرجعي: github.com/moain2028/portfolio-hub → 01-projects/motech-platform/ و02-brand/README.md

| العنصر على التصميم | AR | EN | المصدر |
|---|---|---|---|
| السطر التمهيدي | منصة Motech | Motech Platform | brief.ar.md / brief.en.md — H1 |
| العنوان | وصول آمن عن بُعد لأجهزة العملاء، والمفاتيح بيد الخادم | Secure remote access to client machines, keys owned by the backend | brief.ar.md / brief.en.md — H1 |
| اسم المستودع | motech-platform + motech-cli | نفسه | tech.md — «المستودعات» |
| الوصف | زوج مفاتيح ed25519 لكل عميل، مشفّر بـ AES-256-GCM، ووكيل موقّع ينضم إلى شبكة NetBird — تثبيت من رابط واحد وسجل نشاط كامل. | An ed25519 keypair per client, encrypted with AES-256-GCM, pushed to a signed agent on a NetBird mesh — one-link install, full activity log. | brief — «الحل / Solution» |
| رقم 1 | 3 → 1000+ عميل — بنية مصمّمة للتوسّع | 3 → 1,000+ clients — built to scale | brief — «النتيجة / Result» + tech.md «الأرقام» (هدف تصميمي من README، ليس قياساً) |
| رقم 2 | 20 ثانية بين كل نبضة heartbeat من الوكيل | 20 s heartbeat from every agent | tech.md — «الأرقام» (README مخطط المعمارية) + «تحقّق تشغيلي»: heartbeat_secs = 20 — handlers.go:780 |
| رقم 3 | 3 أنظمة تشغيل بأمر واحد: Windows · Linux · macOS | 3 OS — Windows · Linux · macOS, one command | brief — «الحل / Solution» + tech.md «الأرقام» (motech-cli README) |
| تاجات التقنيات | Go · chi · PostgreSQL 16 · NetBird · ed25519 · AES-256-GCM · Tailwind · Alpine.js | نفسها | tech.md — «التقنيات» |
| الجمهور | لفرق تقنية المعلومات ومورّدي البرمجيات الذين يدعمون أجهزة Windows عن بُعد | For IT teams and software vendors supporting remote Windows fleets | brief — «لمن يفيد / Who it's for» |
| CTA (تذييل) | نحدّد معاً نطاق إعداد الوصول لديك | Let's scope your access setup | brief — «تواصل / Contact» |
| شارة الشريحة | شركات | Companies | tech.md — «الشريحة: شركات» · لونها #3B82F6 من 02-brand |
| الرابط (تذييل) | github.com/moain2028/motech_V2 | نفسه | الحساب الموحّد moain2028 (قرار مدير المنتج 2026-09-23). الرابط الأصلي في التكليف moain2028/MoTechSys-motech-platform صار HTTP 404 بتاريخ 2026-09-23 ~04:00 UTC؛ motech_V2 هو نفس الكود (README «Motech Platform — نظام إدارة الوصول الآمن عن بُعد»، مجلدات backend/agent/dashboard/docs) بنسخة أحدث (آخر commit 2026-06-24)، ويستجيب 200 — أُعيد توليد الـ24 تصميمًا به |
| عنوان شريط المتصفح | لوحة التحكم — نظرة عامة | Dashboard — Overview | screenshots/README.md — الصف 01 |
| الشعار النصي (نسخة logo فقط) | معين العباسي | Moain Al-Abbasi | المعيار §2 |

## اللقطات (حقيقية 100% — لا لقطة مولّدة)
- المتصفح: `screenshots/desktop-01-overview.png` (2880×1800، تشغيل محلي حقيقي — screenshots/README.md)
- الجوال: `screenshots/mobile-02-clients.png` (780×1688، نفس المصدر)
- أسماء العملاء الظاهرة داخل اللقطات بيانات تجريبية وهمية (screenshots/README.md) — لا اسم عميل حقيقي.

## ما لم يُستخدم عمداً
- «أرقام النشر الفعلي: يُستكمل» (brief) — لا يوجد رقم عملاء فعلي، فلم يُكتب أي رقم نشر.
- الرابط الحي qfetmfdn.gensparkclaw.com — لا يستجيب (tech.md) — لم يُوضع على التصميم.
- mark.svg / أيقونة M — ممنوعة في هذه الدفعة (المعيار §2).

## الهوية المطبّقة (02-brand/README.md)
- ألوان: Navy #0E2A47 · Ink #08172B · Amber #F4A62A · Sand #F7F5F0 · Mist #DCE3EA · شريحة شركات #3B82F6.
- خطوط: IBM Plex Sans Arabic (AR) · Inter (EN) · JetBrains Mono (التاجات/الروابط/اسم المستودع). أرقام غربية.
- انحراف واحد مُعلَن: النص الخافت (Slate) رُفع من #7A8A9C إلى #A3B1C0 لأن الأصل يعطي 4.1:1 على Navy (أقل من AA 4.5:1 للنص الصغير)؛ الجديد 6.7:1.
- التباين المقيس: Sand/Navy 13.4:1 · Amber/Navy 7.2:1 · Mist/Navy 11.3:1 · نص الشارة #DBEAFE على خلفيتها ≥ 7:1.
- مساحة أمان الشعار في نسخة nologo: 12% من العرض أعلى-يمين (AR) / أعلى-يسار (EN) — فارغة تماماً.

## التحقق الآلي قبل التسليم
- 24 ملفاً بالمقاسات الدقيقة (فُحصت بـ Pillow).
- فحص DOM لكل قطعة: لا عنصر نصي خارج اللوحة، لا تداخل بين كتلة النص والأجهزة، لا تداخل بين الجوال والتذييل، لا نص مقطوع داخل الشارات/التاجات/الأرقام.

## ملف الشرح (explainer.ar/.en) — مصادر إضافية
- brief.ar.md / brief.en.md: المشكلة · الحل · النتيجة · لمن يفيد · تواصل.
- tech.md: التقنيات · الأرقام (3→1000+ هدف تصميمي، heartbeat 20 ث، 6 أوامر CLI، 3 منصات × 2 معماريات، 12 وثيقة) · التحقّق التشغيلي (5 محاولات/دقيقة، migrations 001–005، /health، تدفّق E2E).
- README moain2026/motech-platform: المكونات · المميزات · المبادئ المعمارية · DATABASE_URL / NETBIRD_API_URL.
- README moain2026/motech-cli: الأوامر الستة · cosign keyless · SHA256SUMS · رمز التفعيل لا يُقبل كوسيط.
- لا رقم نشر فعلي (brief: «يُستكمل»). الخلاصة التنفيذية 5 نقاط أعلى كل ملف.


---

# ملحق v2 — البنود B–G

## B) تصاميم النشر (14 PNG)
| الملف | النص | المصدر |
|---|---|---|
| carousel-1of5 (AR/EN) | المشكلة: عشرات الأجهزة، كلمات مرور مشتركة، ولا سجل | brief — المشكلة · tech.md — المشكلة · لقطة desktop-02-clients |
| carousel-2of5 | الحل: المفاتيح بيد الخادم — ed25519 / AES-256-GCM / وكيل موقّع / NetBird | brief — الحل · لقطتا desktop-03 + mobile-03 (معلومات الاتصال) |
| carousel-3of5 | كيف يعمل: /setup/{token} مرة واحدة · heartbeat كل 20 ث · نسخ معلومات الاتصال | tech.md — الحل · screenshots/README #03 #07 · لقطتا mobile-07 + mobile-03 |
| carousel-4of5 | بالأرقام: 3→1000+ (هدف تصميمي) · 20 ث · 6 أوامر CLI · 3 أنظمة تشغيل | brief — النتيجة · tech.md — الأرقام · لقطة desktop-01-overview |
| carousel-5of5 | الدعوة: تدعم أجهزة Windows عن بُعد؟ | brief — لمن يفيد · تواصل · لقطتا mobile-01 + desktop-04 (سجل العمليات) |
| number-card (AR/EN) | «0 مفتاح خاص يلمس جهاز العميل» | README motech_V2 — «Backend-owned keys: private keys never touch the client machine» · brief — الحل · لقطة mobile-01 |
| blog-banner 1600×840 (AR/EN) | عنوان المقال + سطر الدراسة (Go + PostgreSQL 16 + NetBird · ed25519) | tech.md — التقنيات · brief H1 · لقطتا desktop-03 + mobile-03 |

## C) الريلان (video/)
- motech-platform-reel-ar.mp4 · motech-platform-reel-en.mp4 — 1080×1920، 30fps، h264 + aac، 21.6 ث، 7 مشاهد (غلاف، المشكلة، الحل، كيف يعمل، السجل، بالأرقام، الدعوة)، بلا شعار (مساحة الأمان أعلى-يسار فارغة)، لا مشهد خطأ/404.
- اللقطات داخل الريل: desktop-01/02/03/04 + mobile-01/02/03/07 — كلها حقيقية من screenshots/ (تشغيل محلي، أسماء العملاء وهمية — screenshots/README.md).
- الموسيقى: 02-brand/scripts/reels/bgm-tech-minimal.mp3 (أصل الفريق، بلا حقوق). لا تعليق صوتي (النص مقترح في copy §4).
- المولّد: tools/reel/reel_nologo.py + motech-ar.json / motech-en.json. الأغلفة: video/*-cover.png.
- نصوص المشاهد: كلها من brief/tech (انظر copy.ar/.en §4 سطراً بسطر).

## D) الشرح — motech-platform-explainer.ar.md / .en.md
- 398 / 467 كلمة + خلاصة تنفيذية 5 نقاط أعلى كل ملف؛ المصادر في تذييل كل ملف.

## E) البحث — motech-platform-research.md
- 3 بدائل بروابط مؤرَّخة 2026-09-23: Tailscale (tailscale.com/pricing · kb/1193) · Teleport (goteleport.com/pricing · docs/faq · docs/feature-matrix) · MeshCentral (github.com/Ylianst/MeshCentral) + مرجع NetBird (netbird.io/pricing).
- كل رقم سعر منقول حرفياً من صفحة المصدر؛ تقدير Vendr لـ Teleport مُعلَّم «غير رسمي». حجم الفئة: يُستكمل (لا مصدر).
- التموضع من tech.md فقط. الفجوات صريحة (لا أرقام نشر، لا رابط حي، releases غير متحقَّق، لا نشاط منذ يونيو، الكانوني غير محسوم).

## F) النصوص — motech-platform-copy.ar.md / .en.md (draft للمحرر)
- LinkedIn ≈115/114 كلمة · X ≈235/≈270 حرفاً · IG ≈110/≈115 كلمة · نص الريل 7 مشاهد + VO اختياري ≈55 كلمة. كل جملة من brief/tech؛ الرابط github.com/moain2028/motech_V2.

## screenshots/ (16 لقطة + README)
- نسخة من portfolio-hub/01-projects/motech-platform/screenshots/ (صانع العروض 2026-09-11) — لم أُعِد التصوير لأن اللقطات الحالية 2x حقيقية وكاملة (8+8) ولا يوجد رابط حي، والتشغيل المحلي يحتاج Go + PostgreSQL 16 (موثّق في screenshots/README.md).

## ما لم يُستخدم عمداً (v2)
- أرقام العدّادات داخل لقطة «نظرة عامة» (5 إجمالي / 0 متصل / 2 بانتظار / 0 معطّل) — بيانات تجريبية للتشغيل المحلي (screenshots/README.md)، لا تظهر في أي نص أو شريحة أرقام.
- أسماء العملاء داخل اللقطات (مكتب المحاسبة المتحدة، سوبر ماركت الوفاء…) — وهمية بحسب screenshots/README.md؛ لم تُنقل إلى النصوص.
- الرابط الحي qfetmfdn.gensparkclaw.com — لا يستجيب (tech.md) — غير موجود على أي تصميم أو ريل.
- رقم إصدار Go — README motech_V2 يذكر «Go toolchain 1.26.4» وtech.md يذكر «Go 1.23.4» في التحقّق التشغيلي — تعارض، فلم يُعرض أي إصدار.
