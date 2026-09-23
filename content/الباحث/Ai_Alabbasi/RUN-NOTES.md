Ai_Alabbasi | الباحث | 2026-09-23 | ready

# RUN-NOTES — ماذا شُغّل فعليًا (بلا مفتاح API)

**البيئة:** Ubuntu · Python 3.12.3 · pytest 9.1.1 · PyYAML 6.0.3 · fastapi/uvicorn/python-multipart ثُبّتت للواجهة · لا مفتاح API في البيئة.

| الأمر | النتيجة | مطابقة README؟ |
|---|---|---|
| `python3 -m pytest -q` | **74 passed in 2.18s** · `--co` = 74 محصاة | ✅ «74 اختبار ناجح» |
| `python3 run.py` ثم `/kb` `/help` `/skills فواتير` `/brain` | تعمل؛ `/kb` قبل التغذية: docs 0 · search «hybrid (hashing)» (لا sentence-transformers → البديل المضمّن) | ✅ الأوامر الستة كما في README |
| `python3 run.py` ثم مهمة نصية | «الخطوة 1/25» ثم حدث خطأ صريح: المفتاح غير موجود في متغير البيئة — لا انهيار | ✅ CHANGELOG «أخطاء العقل الصامتة تُبثّ كحدث error» |
| `python3 knowledge/ingest.py` | **87 مقطع مفهرس** لثلاث تقنيات (react-native/nextjs/angular)؛ يُنشئ `knowledge/index/knowledge.db` (300 KB، مستثنى من git) | — (docs/02_STATUS يقول 85 في 2026-06-01؛ المقاس الآن 87) |
| `python3 web/server.py` → `GET /` `/api/brains` `/api/skills` | 200؛ الواجهة RTL تعمل، اختيار العقل، لوحة المهارات (5 seed)، إرسال مهمة → بطاقة خطأ واضحة «لا يوجد مفتاح API» مع حلّ | ✅ |
| فحص المفاتيح المرفوعة | شجرة العمل + تاريخ git كاملًا (`git log --all -p`) بأنماط sk-/ghp_/AIza/hf_/AKIA/xox/PRIVATE KEY + أسماء المتغيرات → **صفر**؛ الملف الوحيد `config/.env.example` قالب نصي | — |

**لم يُشغَّل:** استدعاء نموذج فعلي (يحتاج مفتاحًا)؛ `sentence-transformers` (اختياري)؛ صندوقا Daytona/E2B (اختياريان، السقوط إلى local مُختبر في `tests/test_cloud_sandbox.py`).

## اللقطات (23 ملفًا في `screenshots/`)
- ديسكتوب 1440×900 @2x: `desktop-01-home` (+full)، `02-select` (اختيار العقل)، `07-button` (لوحة المهارات)، `08-composer`، `09-no-key-response` (بطاقة خطأ غياب المفتاح)، `api-brains`، `api-skills`، `github-repo` (+full).
- جوال 390×844 @2x: `mobile-00-sidebar-open` (الحالة الافتراضية عند التحميل)، `01-home` (+full) **يُظهر خلل الواجهة**: بعد طيّ القائمة يُدفع المحتوى خارج الشاشة (المستند 670px) — لقطة حقيقية أُبقيت كدليل ووُثّق الخلل في tech.md، `02-select`، `07-button`، `08-composer`، `09-no-key-response`، `github-repo` (+full).
- طرفية (4): مخرجات حقيقية من الأوامر أعلاه (`pytest`، `/kb`+`/brain`، مهمة بلا مفتاح، `ingest`) رُندرت من ملفات النص إلى PNG بإطار طرفية — لا تعديل في المحتوى سوى الطمس.

## الطمس المطبَّق
- اسم الشخص: في الواجهة (JS blur قبل اللقطة)، وفي الطرفية (استبدال «عبّاس» بـ ▒▒▒▒)، وفي لقطة GitHub (سطر «صُنع لـ…»).
- أسماء المزوّدين/النماذج: شارة العقل وقائمة الاختيار في الواجهة (CSS blur)، وفي الطرفية (regex blur على claude-*/gpt-*/deep-seek-*/qwen*/genspark_*/openrouter_*/local_ollama/GENSPARK_API_KEY).
- مسارات: `/home/user` → `~`.
- محادثات الواجهة: قاعدة `web/conversations.db` حُذفت قبل اللقطات وبعدها (تُنشأ داخل المستودع عند التشغيل).

## تحقّق الروابط (2026-09-23)
- `github.com/moain2028/Ai_Alabbasi` → 200 · `/blob/main/LICENSE` → 200 (MIT) · نسخة الحساب القديم `Moain2026/Ai_Alabbasi` → 200.
