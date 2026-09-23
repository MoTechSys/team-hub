unicore-os | كاتب المحتوى | 2026-09-23 | ready

# UniCore-OS — فهرس اللقطات (22 لقطة حقيقية، 2x)

التقاط: تشغيل محلي للمستودع moain2028/UniCore-OS-V2 (commit 618d180، main) — `pnpm install` → `prisma migrate deploy` → `prisma db seed` → `next dev`، ثم Playwright/Chromium بـ deviceScaleFactor=2: ديسكتوب 1440×900 (ملف 2880×1800) وجوال 390×844 (780×1688)، locale ar. البيانات هي بيانات seed التجريبية من `prisma/seed.ts` (3 حسابات: مدير النظام، عضو هيئة تدريس، طالب؛ مقرر CS101؛ كويز واحد) — لا بيانات حقيقية لأشخاص حقيقيين. الأسماء الظاهرة (سارة محمد، أحمد العلي) وهمية من seed.ts. سكربت الالتقاط: `tools/_portfolio-shoot.mjs`.

| الملف | الدور | الصفحة | استخدام مقترح |
|---|---|---|---|
| desktop-01-admin-dashboard | مدير | /dashboard — لوحة حيّة + حالة النظام | **اللقطة الرئيسية** |
| desktop-02-users | مدير | /users — إدارة المستخدمين | بطاقة RBAC |
| desktop-03-roles | مدير | /roles — الأدوار و52 صلاحية | بطاقة «رقم واحد» |
| desktop-04-academic | مدير | /academic — كليات/أقسام/تخصصات | |
| desktop-05-courses | مدير | /courses | |
| desktop-06-offerings | مدير | /offerings — الشُعب | |
| desktop-07-quizzes | مدرس | /quizzes — إدارة الكويزات | **لقطة ثانية** |
| desktop-08-grades | مدرس | /grades — سجل الدرجات | |
| desktop-09-ai | مدير | /ai — مركز الذكاء الاصطناعي (غير مفعّل بلا مفتاح) | زاوية AI |
| desktop-10-reports | مدير | /reports | |
| desktop-11-trash | مدير | /trash — سلة المهملات (soft delete) | |
| desktop-12-student-dashboard | طالب | /dashboard | |
| desktop-13-student-quizzes | طالب | /quizzes/my | |
| desktop-14-login | — | /login | غلاف |
| mobile-01..08 | مدير/مدرس/طالب | اللوحة، الكويزات، لوحة الطالب، المستخدمون، كويزاتي، الدخول، الأدوار، AI | إطار الجوال |

ملاحظة: /logs أعاد 404 لحساب المدير في هذا التشغيل رغم أن HANDOFF يذكره ضمن المسارات — استُبعد ووُثّق في tech.md.
