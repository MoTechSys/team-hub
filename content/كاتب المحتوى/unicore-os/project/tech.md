unicore-os | كاتب المحتوى | 2026-09-23 | ready

# unicore-os — Technical Sheet (UniCore-OS)

- **Repo:** moain2028/UniCore-OS-V2 (public) — package name `unicore-os` v2.0.0؛ الوثائق تشير إلى الأصل MoTechSys/UniCore-OS-V2
- **Primary language / stack:** TypeScript 5 (strict) · Next.js 16.1.6 (App Router, Turbopack, Server Actions) · React 19.2 · Prisma 5.22 + SQLite (dev) / PostgreSQL (prod) · NextAuth v5 (JWT) · Tailwind 4 + shadcn/ui · Zod 4 · lucide-react · عربي RTL
- **Problem:** إدارة جامعية مجزّأة: مستخدمون وأدوار، هيكل أكاديمي (كليات → أقسام → تخصصات → مقررات → شُعب)، كويزات وتصحيح ودرجات — بلا نظام واحد بواجهة عربية وصلاحيات دقيقة (README «الميزات الرئيسية»، docs/MASTER_BLUEPRINT.md)
- **Solution / core features:** نظام إدارة جامعي واحد: RBAC بـ 52 صلاحية وأدوار مخصصة و Super Admin؛ هيكل أكاديمي كامل؛ محرك كويزات (MCQ / صح-خطأ / إجابة قصيرة / مؤقت) بحالات DRAFT→PUBLISHED→CLOSED؛ توليد أسئلة وتصحيح المقالي بالذكاء الاصطناعي (OpenAI أو Gemini، اختياري بمفتاح)؛ إدارة ملفات برفع وسحب وإفلات؛ إشعارات؛ تقارير وكشف درجات وتصدير CSV؛ سلة مهملات (soft delete)؛ سجل تدقيق؛ لوحة حيّة حسب الدور (README «الميزات»، docs/HANDOFF.md §3.3)
- **Architecture notes:** Feature-first `src/features/*` (15 وحدة: academic, ai, auth, enrollments, notifications, offerings, profile, quizzes, reports, resources, roles, semesters, settings, system, users)؛ الصفحات Server Components تستدعي `requirePermission`، والـ Server Actions بنمط `assert*/failure` تُرجع `ActionResult`؛ كل الأكواد من `src/lib/auth/constants.ts`؛ soft delete عبر `deletedAt`؛ `src/proxy.ts` كـ middleware (HANDOFF §3)
- **Status:** beta — 2.0.0-rc.4 (CHANGELOG 2026-09-04)؛ الوثائق تصف «إنعاش» v1 → v2: البناء والزحف سليمان، لا اختبارات وحدة ولا E2E ولا CI (HANDOFF §0)
- **Last commit:** 2026-09-04 (Merge PR #8) — 43 commit من 2026-02-02
- **Live URL:** none

## الأرقام ومصادرها / Numbers & sources
| Metric | Value | Source |
|---|---|---|
| Permissions | 52 | `app/src/lib/auth/constants.ts` PERMISSIONS (عدّ الأكواد `x.y` = 52)؛ README «52 صلاحية» |
| Prisma models | 22 | `grep -c '^model ' app/prisma/schema.prisma` (README يقول «20 جدول» — الأقدم) |
| Pages (routes) | 26 | `find app/src/app -name page.tsx` = 26؛ PROJECT_STATUS «26 صفحة» |
| Feature modules | 15 | `ls app/src/features` |
| TS/TSX files | 219 | `find app/src -name '*.ts*'` |
| Tracked files | 258 | `git ls-files | wc -l` (تكليف مدير المنتج ذكر 362 — رقم GitHub غير مُتحقَّق؛ اعتُمد git) |
| Commits | 43 | `git rev-list --count HEAD` (2026-02-02 → 2026-09-04) |
| `tsc --noEmit` | 0 errors | تشغيل محلي 2026-09-23 exit 0؛ HANDOFF §0 |
| ESLint | 0 errors / 1 warning | `npx eslint .` محلياً 2026-09-23؛ HANDOFF: 0 مشاكل بعد PR #7 |
| UI crawl | 102 صفحة × 3 أدوار × 2 viewport = 0 مشاكل | HANDOFF §0 / PROJECT_STATUS (قياس المؤلف، لم يُعَد هنا) |
| Roles (seed) | 3 (SUPER_ADMIN, INSTRUCTOR, STUDENT) | `prisma/seed.ts`؛ HANDOFF §2 |
| Quiz types | 3 (MCQ, True/False, Short answer) + timer | README «محرك الكويزات» |
| AI providers | 2 (OpenAI, Gemini) اختياري | `.env.example` AI_PROVIDER؛ README |
| Unit tests / E2E / CI | 0 / 0 / none | HANDOFF §0 (Vitest config غائب، لا playwright.config، لا workflows) |
| Version | 2.0.0 (package.json) · 2.0.0-rc.4 (CHANGELOG) | `app/package.json` L3؛ CHANGELOG |
| Users / clients | يُستكمل | غير موثّق |

## ملاحظات التنظيف / Cleanup notes
- README يذكر Next.js 15 في «التقنيات» بينما package.json = 16.1.6، و«20 جدول» بينما schema = 22 model، و«PROJECT_STATUS (100%)» بينما PROJECT_STATUS الحالي صادق بنِسب أقل — README يحتاج تحديث (HANDOFF يقرّ بذلك).
- README يشير لصور `docs/screenshots/*.png` غير موجودة في المستودع — اللقطات هنا التُقطت محلياً.
- README/HANDOFF ينشران بيانات دخول تجريبية ورقم هاتف واسم المطوّر في صفحة `/developer` — لا يُنقل أي منها إلى التصاميم.
- `/logs` أعاد 404 لمدير النظام في التشغيل المحلي (2026-09-23) رغم إدراجه في HANDOFF §3.3 — يُراجَع.
- بناء `next build` لم يُنفَّذ هنا (dev فقط)؛ HANDOFF يذكر نجاحه بعد PR #3.
- لا LICENSE ولا CONTRIBUTING.md رغم إشارة README إليهما.
