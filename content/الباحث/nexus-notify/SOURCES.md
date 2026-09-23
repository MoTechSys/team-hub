nexus-notify | الباحث | 2026-09-23 | v2-addendum

# nexus-notify project pack v2 — الملحق (B–F) — مصدر كل نص ورقم وصورة
يكمّل nexus-notify-design-pack-v1.zip (البند A، معتمد 2026-09-23). المصدر الحي: https://github.com/moain2028/portfolio-hub → 01-projects/nexus-notify/ + https://github.com/moain2028/nexus-notify (README · ARCHITECTURE.md · docs/PROJECT_STATUS.md).

## B — كاروسيل (5 AR + 5 EN) · بطاقة رقم · بانر
| العنصر | النص/الرقم | المصدر |
|---|---|---|
| كاروسيل 1 المشكلة | نص brief «المشكلة» حرفياً | brief.ar/en |
| كاروسيل 2 الحل + التاجات | نص brief «الحل» · NestJS/PostgreSQL 17/Prisma/Redis-BullMQ/Angular 22/Kotlin | brief.ar/en · tech.md «التقنيات» |
| كاروسيل 3 كيف يعمل | X-API-Key + idempotency → توجيه حسب بادئة المشغّل إلى جهاز المجموعة → حفظ مركزي → WebSocket | ARCHITECTURE.md §1 و§5–6 · PROJECT_STATUS.md (WebSocket ✅، بادئات المشغّلين #3) |
| كاروسيل 4 الأرقام | 163 · 12/12 · 7 · 85% · 11 اختبار أندرويد | tech.md ← docs/PROJECT_STATUS.md؛ brief «النتيجة» |
| كاروسيل 5 لمن | نص brief «لمن يفيد» + «تواصل» | brief.ar/en |
| بطاقة الرقم | 163 اختباراً للخادم + 12/12 · 11 · 85% | docs/PROJECT_STATUS.md «الحصيلة» |
| البانر | العنوان + السطر التعريفي + التاجات كما في الحزمة A | brief · tech.md |
| الشريحة/اللون | شركات #3B82F6؛ النص الخافت #A3B1C0 | مهمة #9 · v2 standard |
| التذييل | github.com/moain2028/nexus-notify (200) | المهمة #9 |

## C — الريل (AR + EN، 25.5 ث، 1080×1920، بلا شعار) + غلافان
| المشهد | النص على الشاشة | المصدر |
|---|---|---|
| 1 | خمسة أماكن لبيانات عملائك؟ / كل نظام يرسل رسائله بنفسه | brief «المشكلة» |
| 2 | منصة واحدة لكل أنظمتك / NestJS · PostgreSQL 17 · Angular 22 · Kotlin | brief «الحل» · tech.md |
| 3 | API واحد، محادثة محفوظة مركزياً / X-API-Key + idempotency · WebSocket | brief · ARCHITECTURE.md §6 · PROJECT_STATUS (WebSocket) |
| 4 | هاتف الشريحتين قناة SMS / توجيه حسب بادئة المشغّل | brief · ARCHITECTURE.md §1 · PROJECT_STATUS #3 |
| 5 | 163 · 12/12 · 85% / 7 صفحات · 11 اختبار أندرويد | docs/PROJECT_STATUS.md |
| 6 | أُقدّم دراسة لمركز إشعاراتك / الرابط | brief «تواصل» |
بلا موسيقى (لا مصدر خالٍ من الحقوق محلياً — تُضاف من صانع الفيديو عند النشر). لا مشهد خطأ/404.

## الصور
| الملف | ماذا يعرض | معالجة |
|---|---|---|
| screenshots/desktop-02.png | لوحة التحكم | بلا تعديل |
| screenshots/desktop-04.png | المحادثات (محادثة مفتوحة) | بلا تعديل |
| screenshots/desktop-05.png | الإشعارات | بلا تعديل |
| screenshots/desktop-06.png | قواعد التوجيه | بلا تعديل |
| screenshots/mobile-02.png | لوحة التحكم — جوال (في البانر) | بلا تعديل |
كلها التقاط حقيقي 2026-09-11 (Playwright) للواجهة الفعلية أمام API تجريبي — بيانات تجريبية معلَنة في links.md؛ لا رقم من داخل اللقطة مُقتبس (1284 / 97.3% تجريبية). لا لقطة مولَّدة.

## D/E/F — الملفات النصية
- nexus-notify-explainer.ar/en.md — كل فقرة بمصدرها (README/ARCHITECTURE/PROJECT_STATUS/tech/brief).
- nexus-notify-research.md — 4 بدائل بروابط (200 بتاريخ 2026-09-23) + نطاق سوق A2P بمصدرَين + كلمات مفتاحية + زوايا + فجوات.
- nexus-notify-copy.ar/en.md — من brief المختوم + tech/ARCHITECTURE؛ draft للمحرر.

## التحقق
- 16 PNG مطابقة للمقاسات (10 كاروسيل 1080×1080 · 2 بطاقة رقم 1080×1080 · 2 بانر 1600×840 · 2 غلاف ريل 1080×1920).
- ريلان 1080×1920 · 30fps · 25.5 ث.
- الأدوات في tools/ (make_carousel.py · make_reel.py · make_pack.py · spec.json) فوق 02-brand/scripts/brand.py.
