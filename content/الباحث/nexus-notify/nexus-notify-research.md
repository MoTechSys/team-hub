nexus-notify | الباحث | 2026-09-23 | v2

# Nexus Notify — بحث وتحليل (Research & Analysis)
تاريخ الوصول لكل الروابط: 2026-09-23 (HTTP 200 ما لم يُذكر). أرقام المشروع من tech.md / docs/PROJECT_STATUS.md فقط.

## 1. من يشتري هذا؟
- الشريحة في الـ brief: الشركات التي تشغّل عدة أنظمة (فوترة، تحصيل، ERP) وتريد إشعار عملائها ومحادثتهم من مكان واحد. (brief.ar.md · tech.md)
- السياق المحلي: المنصة مبنية حول مشغّلي اليمن (بادئات 70/71/73/77/78) وهواتف أندرويد ثنائية الشريحة كقناة إرسال — أي حل للأسواق التي تكون فيها بوابات SMS السحابية مكلفة أو غير متاحة. (docs/PROJECT_STATUS.md #3 · reference/YEMEN-CARRIERS.md)
- حجم الفئة الأم: رسائل A2P/الأعمال عالمياً — Juniper Research: 51.7 مليار دولار إيرادات المشغّلين في 2025 (https://www.juniperresearch.com/research/telecoms-connectivity/messaging/a2p-research-report/)؛ MarketsandMarkets: 73.1 مليار في 2024 → 84.8 مليار في 2029 (https://www.marketsandmarkets.com/Market-Reports/a2p-messaging-market-44.html). التقديرات متباعدة فتُذكر كنطاق.
- حجم الفئة المحلية (شركات يمنية تحتاج بوابة SMS داخلية): لا رقم موثوق — يُستكمل.

## 2. المنافسون / البدائل
| البديل | ما هو | الرابط | ماذا يقول عن نفسه | أين يتفوّق مشروعنا (من tech.md/PROJECT_STATUS فقط) |
|---|---|---|---|---|
| Twilio Programmable Messaging | API سحابي لإرسال/استلام SMS وواتساب بأسعار لكل رسالة | https://www.twilio.com/en-us/pricing/messaging | «SMS and RCS… start at $0.0083 per outbound/inbound message, plus carrier fees» | لا يحتاج حساباً دولياً ولا تغطية مشغّل سحابية؛ يستخدم شرائح الشركة نفسها وهواتفها، ويحفظ المحادثات مركزياً محلياً. الثمن: الاعتماد على أجهزة أندرويد فعلية (failover داخل المجموعة موثّق). |
| Novu | بنية إشعارات مفتوحة المصدر متعددة القنوات (Inbox/Push/Email/SMS/Chat) بمحرك workflows | https://github.com/novuhq/novu · https://novu.co/ | «unified API to send notifications through multiple channels» | Novu يوجّه إلى مزوّدي SMS خارجيين ولا يملك قناة إرسال خاصة؛ مشروعنا يملك القناة نفسها (تطبيق أندرويد ثنائي الشريحة) مع محادثات ثنائية الاتجاه وتوجيه حسب بادئة المشغّل. |
| Traccar SMS Gateway | تطبيق أندرويد مجاني يعرض HTTP API لإرسال SMS من الهاتف | https://www.traccar.org/sms-gateway/ | «Turn an Android phone into an SMS gateway with an HTTP API» | جهاز واحد بلا خادم مركزي؛ مشروعنا متعدد المستأجرين، مع مجموعات أجهزة وfailover وOutbox وidempotency ولوحة محادثات و163 اختباراً. |
| SMS Gateway for Android (capcom6 / sms-gate.app) | بوابة SMS مفتوحة المصدر لأندرويد مع REST API وwebhooks وخادم سحابي اختياري | https://github.com/capcom6/android-sms-gateway · https://sms-gate.app/ | «send and receive SMS… via REST API, webhooks… No registration required» | الأقرب وظيفياً في طبقة الجهاز. الفرق الموثّق عندنا: طبقة المنصة (المستأجرون، المحادثات المركزية، قواعد التوجيه بالبادئة، لوحة عربية RTL، WebSocket) — وهي ما لا يقدّمه تطبيق بوابة وحده. |

## 3. التموضع المقترح
«مركز إشعارات ومحادثات داخلي يملك قناته: API واحد لأنظمتك، وهواتف شركتك هي البوابة.»
- للشركات: لا اشتراك سحابي لكل رسالة، ولا تكرار للأرقام، وسجل واحد لكل عميل.
- ما لا نقوله: أرقام حجم إنتاجي (لا توجد)، أو أن WhatsApp متاح (مؤجّل).

## 4. الكلمات المفتاحية
AR (10): منصة إشعارات مركزية · بوابة SMS أندرويد · إشعارات متعددة المستأجرين · نظام محادثات SMS للشركات · API إشعارات موحّد · بوابة رسائل ثنائية الشريحة · إشعارات الفوترة SMS · لوحة تحكم إشعارات عربية · توجيه الرسائل حسب المشغّل · بديل Twilio محلي
EN (10): multi-tenant notification platform · Android SMS gateway · self-hosted SMS gateway · dual-SIM SMS gateway · notification hub API · NestJS notification service · Angular RTL dashboard · SMS conversation management · carrier prefix routing · Twilio alternative self-hosted
(مصطلحات المشروع + صياغة SEO؛ حجم البحث لم يُقَس — يُستكمل مع متخصص SEO.)

## 5. ثلاث زوايا محتوى
1. «14 ملاحظة من اختبار ميداني حقيقي»: قصة الاختبار على Samsung بشريحة Yemen Mobile وكيف أُصلح كل خطأ بتشخيص جذري — مادة مصداقية للشركات (FIELD-TESTING-FIXES.md).
2. «لماذا idempotency؟»: شرح تقني قصير لكيف يمنع مفتاح واحد إرسال الفاتورة مرتين (ARCHITECTURE.md §6).
3. «هاتفك هو البوابة»: مقارنة تكلفة/تحكم بين بوابة SMS سحابية وقناة أندرويد داخلية — بلا أرقام تكلفة مخترعة (تُحسب لكل عميل).

## 6. الفجوات (صريحة)
تقنياً:
- لا نشر إنتاجي موثّق ولا أرقام استخدام (رسائل/أجهزة). (tech.md)
- WhatsApp/الوكيل مؤجّل؛ التوسّع خارج SMS غير موجود بعد. (README)
- تطبيع الأرقام الدولية جزئي (بلا جدول بلدان كامل). (PROJECT_STATUS.md #10)
- README يحوي بيانات دخول تطوير افتراضية — يُنظَّف قبل أي عرض عام. (tech.md)
- المستودع كان خاصاً (license: private)؛ النسخة العامة على moain2028 بلا ملف ترخيص واضح — يُحسم قبل الترويج كمفتوح. 
تسويقياً:
- اللقطات ببيانات تجريبية (معلَنة)؛ لا لقطة من بيئة حقيقية.
- لا فيديو ديمو حقيقي ولا رابط حي.
- الشريحة الأولية «شركات» لكن القيمة الأوضح للسوق اليمني/الأسواق المشابهة — يُقرَّر هل يُسوَّق محلياً أولاً.

## 7. المصادر
- المستودع: https://github.com/moain2028/nexus-notify (200) — README.md · ARCHITECTURE.md · docs/PROJECT_STATUS.md
- portfolio-hub: 01-projects/nexus-notify/{brief.ar.md, brief.en.md, tech.md, links.md}
- روابط البدائل والسوق أعلاه (200 عند الوصول؛ mordorintelligence.com أعاد 403 فاستُبعد).

## Summary (EN)
Buyers: companies running several internal systems that must notify and converse with customers from one place — especially in markets like Yemen where the platform routes by local carrier prefix through the company's own dual-SIM Android phones. Parent A2P market: USD 51.7B (Juniper, operator revenue 2025) to 73–85B (MarketsandMarkets 2024–29). Alternatives: Twilio (per-message cloud API), Novu (open-source orchestration without its own channel), Traccar SMS Gateway and capcom6 SMS Gateway (single-device Android gateways). Our documented edge: the platform layer — multi-tenancy, central two-way conversations, prefix routing, outbox/idempotency/failover, RTL dashboard, WebSocket, 163 tests. Gaps: no production numbers, WhatsApp deferred, partial international normalization, default dev credentials in README, unclear public license.
