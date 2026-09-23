moain-promoter-ai | كاتب المحتوى | 2026-09-23 | v1

# Moain Promoter AI — بحث وتحليل (Research & positioning)

تاريخ البحث: 2026-09-23 (فتح صفحات الأسعار + GitHub API + بحث ويب). كل ادعاء عن مشروعنا من tech.md؛ كل ادعاء عن بديل من رابطه بتاريخ الوصول. لا يُسمّى أي مزوّد نماذج بالاسم في نصوص النشر (قيد مدير المنتج).

## 1. من يشتري هذا؟
- المستخدم: مطوّر أو مستقل أو استوديو صغير لديه محفظة GitHub كبيرة ويريد أن تُسوَّق بلغتين على عدة منصات دون أن يتوقف عن البناء (README «عربي»).
- المشتري في المحفظة: الشريحة «شركات» — استوديوهات التطوير والوكالات الصغيرة التي تدير حسابات تقنية؛ وثانياً مطوّرون مستقلون يبنون علامتهم الشخصية.
- حجم الفئة: لا رقم موثّق لدينا. مؤشر غير مباشر: Postiz (بديل مفتوح المصدر في نفس الفئة) عند 36,216 نجمة على GitHub وآخر push 2026-09-23 — الفئة نشطة وكبيرة.

## 2. البدائل الحقيقية (وصول 2026-09-23)
| # | البديل | ماذا هو | السعر المعلن | الرابط | ملاحظة |
|---|---|---|---|---|---|
| 1 | Buffer | جدولة ونشر لعدة منصات، تسعير بالقناة | Free · Essentials $5/شهر للقناة · Team $10/شهر للقناة (سنوي: $60 / $120 للقناة) | https://buffer.com/pricing | «Only pay for the channels you use» — للمنشئين حتى الوكالات |
| 2 | Hootsuite | إدارة سوشيال للفرق والمؤسسات | Standard $99 · Professional $199 · Advanced $399 /شهر · Enterprise بالتواصل | https://www.hootsuite.com/plans | Standard: حتى 10 حسابات من تقويم واحد |
| 3 | Typefully | كتابة وجدولة للمنشئين (X/LinkedIn وغيرها) مع AI وتحليلات | Free · ثم خطط مدفوعة تبدأ ≈ $10–12.5/شهر (صفحة الأسعار تُحمَّل بـ JS؛ الأرقام من مراجعات 2025–2026: efficient.app، kleo.so، voicemoat.com) | https://typefully.com/pricing | «Start for free, then upgrade for higher publishing limits, analytics, AI, and collaboration» |
| 4 | Postiz | إدارة سوشيال مفتوحة المصدر بوكيل AI للجدولة والتوليد | Standard $29 · Team $39 · Pro $49 · Ultimate $99 /شهر (السحابي)؛ الاستضافة الذاتية مجانية | https://postiz.com/pricing · https://github.com/gitroomhq/postiz-app | 36,216★ · TypeScript · AGPL-3.0 · آخر push 2026-09-23 |

ملاحظات: أسعار Typefully لم تُقرأ من صفحتها مباشرة (المحتوى يُرسم بـ JavaScript) فوُسمت «≈» بمصادرها؛ تتغيّر الأسعار — كلها بتاريخ 2026-09-23.

## 3. التموضع
ماذا يقول المنافسون: أدوات جدولة ونشر ناضجة، مستضافة، بتكاملات رسمية وتحليلات وفرق دعم؛ يكتب المستخدم المنشور (أو يساعده AI عام) ثم تجدوله الأداة. Postiz وحده مفتوح المصدر وبه وكيل AI عام.

أين يتميّز Moain Promoter AI (من tech.md فقط):
- يبدأ من **المستودع لا من المنشور**: وكيل يقرأ README والكود، وآخر يشغّل المشروع ويلتقط لقطاته بـ Playwright (11 viewport)، وثالث يولّد بديلاً بصرياً عند الفشل — لا أداة في القائمة تفعل هذا.
- **ثنائي اللغة عربي/إنجليزي بشخصية محلية** و27 قالباً، وحملات 30/60/90 يوماً لست منصات.
- **مستقل عن المزوّد**: 27 مزوّد نماذج في سجل واحد، اكتشاف نوع المفتاح من بصمته وفحصه قبل الاستخدام، وحدود معدل لكل مزوّد.
- مفتوح المصدر MIT، يعمل على جهازك، `default_dry_run: true` — لا نشر حيّ بالخطأ.

أين يتأخر (صريح): prototype لا SaaS — لا رابط حيّ، لا تحليلات، لا واجهة تقويم فعلية (`/schedule/list` يعيد `[]`), موجِّه المحادثة بسيط بالكلمات المفتاحية، يحتاج مفاتيح (نموذج + GitHub + كل ناشر) ليعمل فعلياً، 6 commits في يوم واحد، لا مستخدمون موثَّقون، لا لقطات أو منشورات ناتجة في المستودع.

## 4. الكلمات المفتاحية
AR (10): تسويق محفظة GitHub · نظام متعدد الوكلاء · أتمتة النشر على السوشيال · منشورات عربية إنجليزية تلقائية · وكيل ذكاء اصطناعي للتسويق · جدولة حملات 30 يوماً · التقاط لقطات المشروع تلقائياً · مفتوح المصدر MIT · FastAPI Playwright Next.js · تسويق المطوّر المستقل
EN (10): GitHub portfolio marketing automation · multi-agent AI system Python · bilingual social media posts Arabic English · developer personal branding automation · automated repo screenshots Playwright · open source social scheduler MIT · provider-agnostic LLM registry · FastAPI Next.js agent dashboard · 30-day content campaign generator · dry-run safe publishing

## 5. ثلاث زوايا محتوى
1. «من المستودع إلى المنشور دون أن تكتب حرفاً» — زاوية المنتج: الوكلاء التسعة كخط إنتاج (تحليل → التقاط → كتابة → جدولة → نشر).
2. «27 مزوّداً بمفتاح واحد» — زاوية هندسية للمطوّرين: سجل المزوّدين، بصمة المفتاح، الفحص، حدود المعدل — لا اعتماد على شركة.
3. «82 اختباراً وCI قبل أول منشور» — زاوية الصدق: ما يعمل فعلاً (الاختبارات، اللوحة، السجل) وما لم يُشغَّل بعد (النشر الحيّ) — مقابل أدوات SaaS تبيع الجاهز.

## 6. الفجوات (بلا تجميل)
تقنياً: لا رابط حيّ · README يوجّه clone إلى موقع 404 ويقول 7 وكلاء بينما الكود 9 · إصدار مبعثر (1.0.0 / 1.1.0 / v3.3) · Celery/Redis وLangChain في requirements بلا استخدام في src · `/schedule/list` قائمة فارغة ثابتة و`/agent/chat` موجِّه مبسّط (بتعليقات المؤلف) · قائمة المستودعات بلا توكن تسقط إلى 10 بطاقات demo بأسماء مستودعات المالك · `google.generativeai` مهجور · 6 commits في يوم واحد.
تسويقياً: «171+ مستودعاً» رقم عن حساب المالك لا عن المشروع — لا يُعرض · لا منشور نُشر ولا حملة نُفّذت موثَّقة · لا لقطات في المستودع (أُخذت هنا محلياً بلا مفاتيح) · اسم المنتج شخصي (Moain) يحدّ من إعادة استخدامه كمنتج عام.

## 7. المصادر
- المشروع: https://github.com/moain2028/moain-promoter-ai (200) · README.md · docs/PROVIDERS.md · src/agents/*.py · src/models/registry.py · src/core/api.py · configs/agent_defaults.yaml · pytest محلياً 2026-09-23 (82 passed).
- البدائل: صفحات الأسعار أعلاه (كلها 200 بتاريخ 2026-09-23) + GitHub API لـ gitroomhq/postiz-app.

## EN summary
Moain Promoter AI targets dev studios and freelancers who want a large GitHub portfolio marketed bilingually across six platforms. Real alternatives (accessed 2026-09-23): Buffer (Free / $5 / $10 per channel per month), Hootsuite ($99 / $199 / $399 per month), Typefully (free, paid from ≈$10–12.5/mo per reviews), and open-source Postiz (36.2K★, AGPL-3, cloud $29–$99/mo). Its edge: it starts from the repository — agents read the code, run it and capture real screenshots, write bilingual posts with a local persona, and plan 30/60/90-day campaigns — with 27 swappable model providers, MIT license and dry-run by default. Gaps: prototype, no live URL, schedule endpoint returns an empty list, chat router is keyword-based, needs keys for every publisher, README lags the code, no documented users or published posts.
