scam2027 | كاتب المحتوى | 2026-09-23 | ready

# scam2027 — Technical Sheet (Smart Course & Assessment Manager)

- **Repo:** moain2028/scam2027 (public) — main HEAD `c761778` (2026-09-07)؛ الفرع genspark_ai_developer على نفس الـ commit. README/STATUS يشيران إلى MoTechSys/scam2027 كأصل. الرخصة: «جميع الحقوق محفوظة © 2026 MoTechSys (تُحدَّد الرخصة النهائية من المالك)» — ليس مفتوح المصدر.
- **Primary language / stack:** TypeScript strict · Next.js 16.3.4 (App Router, Server Actions) · React 19.2.3 · Tailwind 4 + shadcn/ui · Prisma 6.19 · PostgreSQL 16 مع Row Level Security · Auth.js v5 (Credentials + Argon2id + جلسات DB) · Zod 4 · next-intl (ar/en) · Vitest · Playwright · axe-core · pnpm 10 — المصدر: app/package.json، README «الحزمة التقنية».
- **Problem:** 9 مستودعات تراثية لنظام إدارة مقررات جامعي (واجهة خضراء شبه مكتملة + 3 خلفيات جزئية) بلا تعددية مستأجرين ولا اختبارات ولا CI ولا امتثال PDPL — README «لماذا هذا المستودع؟»؛ docs/00-analysis (GAP-01..27).
- **Solution / core features (المنجَز فعلاً — P0 + P1-01..08):** منصة متعددة المستأجرين (مخطط مشترك + tenantId + RLS على 30 جدولاً) · Auth.js بجلسات قابلة للإبطال وقفل حساب وrate-limit · RBAC بـ 114 صلاحية منقّطة في 14 فئة و5 أدوار نظام + أدوار مخصّصة · إدارة المستخدمين · البنية الأكاديمية (أعوام/فصول/كليات/أقسام/تخصصات/مستويات) · المقررات والشُعب والتسجيل · الملفات (تخزين محلي أو S3، فحص magic bytes، تنزيل موقَّع) · الإشعارات (إرسال موجَّه، fan-out، جرس) · سلة محذوفات موحّدة باحتفاظ 30 يوماً · واجهة RTL جوال-أولاً بقشرة تطبيق (ADR-0007/0008) · سجل تدقيق AuditLog (البيانات منذ P0؛ واجهته P1-09 التالية).
- **Architecture notes:** `app/src/app` (auth) + (dashboard) route groups · `src/features/*` (schemas/queries/actions) · `src/lib/auth` (requireUser/assertPermission/permissions.ts المولَّد) · `src/lib/db` (Prisma + GUC `app.current_tenant_id`؛ `app_user` بلا BYPASSRLS) · `prisma/` (34 نموذجاً، 4 هجرات، seed) · `e2e/` Playwright (desktop 1280×800 + iPhone 12) · `tests/` unit+integration · `docs/` 33 وثيقة (تحليل، بحث، منتج، معمارية، خطة، جودة، 9 ADR، handoff) · `.github/ci.yml.template` (CI غير مفعَّل).
- **Status:** **قيد البناء — الأساس مكتمل.** 24/65 مهمة (37٪): P0 16/16 DONE، P1 8/15 IN_PROGRESS، P2–P5 لم تبدأ (STATUS.json 2026-09-06). محلياً 2026-09-23: `pnpm typecheck` 0 أخطاء، Vitest 181/181 PASS، البناء ناجح (28 مساراً)، `/api/health` db up. المهمة التالية P1-09 سجل التدقيق.
- **Last commit:** 2026-09-07 — 23 commits (21 عبر PR) بين 2026-09-04 و2026-09-07.
- **Live URL:** none (لا رابط حيّ في README؛ لم يُفحص نشر).

## الأرقام ومصادرها / Numbers & sources
| Metric | Value | Source |
|---|---|---|
| Roadmap tasks done | 24 / 65 (37%) | docs/90-handoff/STATUS.json `progress` |
| P0 Foundation | 16 / 16 DONE | STATUS.json `phases.P0` |
| P1 Core LMS | 8 / 15 IN_PROGRESS | STATUS.json `phases.P1` |
| Permissions | 114 (14 categories) | `SELECT count(*) FROM "Permission"` بعد seed = 114؛ src/lib/auth/permissions.ts؛ docs/20-product/02-PERMISSIONS-MATRIX.md |
| System roles | 5 | README «الأدوار»؛ prisma/seed.ts ROLE_META |
| Prisma models | 34 | `grep -c "^model " app/prisma/schema.prisma` |
| Tables with RLS enabled | 30 of 34 | `pg_class.relrowsecurity` على scam2027 محلياً |
| RLS policies | 30 | `SELECT count(*) FROM pg_policies` |
| Migrations | 4 | `ls app/prisma/migrations` |
| Vitest tests | 181 PASS (25 files) | `pnpm test` محلياً 2026-09-23 |
| Playwright e2e | 41 test() × 2 projects (desktop-chromium 1280×800, mobile iPhone 12) — README يقول 80 ✅ | `grep -c "test(" e2e/*.spec.ts`؛ playwright.config.ts — لم تُشغَّل هنا |
| Typecheck | 0 errors | `pnpm typecheck` محلياً 2026-09-23 |
| Routes (build) | 28 (22 صفحة + 6 API/static) | `pnpm build` output |
| TS/TSX files / LOC | 216 / 27,925 | `find app/src -name "*.ts*" \| xargs cat \| wc -l` |
| shadcn/ui components | 61 | `ls app/src/components/ui` |
| i18n message keys (ar) | 1,042 | app/messages/ar.json |
| Docs | 33 Markdown + 9 ADR | `find docs -name "*.md"`؛ docs/60-adr |
| Gap analysis items | GAP-01..27 | docs/00-analysis/04-GAP-ANALYSIS.md |
| Seed demo data | 1 tenant · 34 users (4 staff + 30 students) · 6 courses · 4 offerings · 68 enrolments | prisma/seed.ts output محلياً |
| Commits / PRs | 23 / 21 | `git log --oneline` |
| GitHub stars | 0 | GitHub API 2026-09-23 |
| CI | غير مفعَّل (قالب فقط) | .github/ci.yml.template؛ AGENTS.md §7 |

## ملاحظات التنظيف / Cleanup notes
- README يحوي رقم هاتف المطوّر وصفحة `/developer` تعرضه داخل المنتج — لم تُستخدم لقطة `/developer`، والرقم لا يظهر في أي مادة.
- README يوجّه clone إلى MoTechSys/scam2027 بينما المستودع المكلَّف moain2028 — يُوحَّد.
- CI غير مفعَّل على GitHub (القالب موجود؛ التوكن بلا صلاحية workflows) — يُنقل القالب إلى .github/workflows.
- «Playwright 80 ✅» في README = 40 اختباراً × مشروعَين تقريباً؛ لم تُعاد هنا فلا تُعرض على التصاميم.
- «68 نموذجاً» في خريطة التوثيق (نموذج البيانات المخطَّط) مقابل 34 نموذجاً في schema.prisma الفعلي — يُعرض 34 فقط.
- الرخصة النهائية غير محدَّدة.
