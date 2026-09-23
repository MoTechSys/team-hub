moain-promoter-ai | كاتب المحتوى | 2026-09-23 | ready

# moain-promoter-ai — فهرس اللقطات (17 لقطة حقيقية، 2x)

التقاط: تشغيل محلي للمستودع moain2028/moain-promoter-ai (commit 4d1a567، main): الباك-إند `pip install` (المتطلبات الأساسية) → `pytest tests/` (82 passed) → `uvicorn src.core.api:app --port 8000`؛ اللوحة `cd dashboard && npm install && npm run build && next start -p 3200` (تُوجِّه /api/backend/* إلى FastAPI). ثم Playwright/Chromium بـ deviceScaleFactor=2: ديسكتوب 1440×900 (2880×1800) وجوال 390×844 (780×1688). **بلا أي مفتاح**: `.env` نسخة فارغة من `.env.example` — لذا قائمة المستودعات تعرض بيانات demo المضمّنة في `ReposPanel.tsx` (10 بطاقات)، والمحادثة تُظهر رد الخادم الحقيقي بلا نموذج، والمعرض والتقويم فارغان كما هما فعلياً. لا مفاتيح ولا أسماء حسابات سوشيال في أي لقطة (حقول كلمة المرور فارغة). سكربت الالتقاط: `_portfolio-shoot.mjs`.

| الملف | اللوحة | ملاحظة | استخدام مقترح |
|---|---|---|---|
| desktop-01-chat-empty | Chat — شاشة الترحيب: 3 بطاقات (Browse Repos · Generate Content · Plan Campaign) + سطر الوكلاء السبعة | | **اللقطة الرئيسية (ديسكتوب)** |
| desktop-02-chat-typed | Chat — رسالة عربية مكتوبة | | |
| desktop-03-chat-response | Chat — ردّ OrchestratorAgent الفعلي (بلا نموذج ولا مستودع مختار) | يُظهر التوجيه بالكلمات المفتاحية | |
| desktop-04-repos | Repositories — بحث + فلاتر لغة + بطاقات | بيانات demo (لا GITHUB_TOKEN) — مذكور في toast | لقطة ثانية |
| desktop-06-gallery | Screenshots — فارغ مع أمر CLI للالتقاط | | |
| desktop-07-schedule | Schedule — فارغ + زر Build New Campaign | | |
| desktop-08-settings | Settings — تنبيه أمني + 5 مزوّدين مع حقول مفاتيح مخفية فارغة + Test | | زاوية «مزوّد قابل للتبديل» |
| desktop-09-settings-scrolled | Settings — GitHub Access والناشرون | | |
| mobile-00-sidebar | الشريط الجانبي مفتوحاً (الحالة الافتراضية على الجوال) | | |
| mobile-01-chat-empty | Chat — الترحيب | | **اللقطة الرئيسية (جوال)** |
| mobile-02-chat-typed | Chat — رسالة مكتوبة | | |
| mobile-03-chat-response | Chat — ردّ الوكيل | | مروحة |
| mobile-04-repos | Repositories | demo | مروحة |
| mobile-06-gallery | Screenshots فارغ | | |
| mobile-07-schedule | Schedule فارغ | | |
| mobile-08-settings | Settings — المزوّدون | | مروحة |
| mobile-09-settings-scrolled | Settings — GitHub/الناشرون | | |

ملاحظة صدق: هذه لقطات الواجهة كما تعمل بلا مفاتيح؛ لا يُدّعى في التصاميم أن منشوراً نُشر أو لقطة التُقطت آلياً.
