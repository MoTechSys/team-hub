electricity-billing-pwa-v2 | كاتب المحتوى | 2026-09-23 | ready

# electricity-billing-pwa-v2 — Technical Sheet (نظام فواتير الكهرباء V2)

- **Repo:** moain2028/electricity-billing-pwa-v2 (public، أُنشئ على هذا الحساب 2026-09-23) — نسخة مطابقة (نفس HEAD `9ee69cb`) لـ MoTechSys/electricity-billing-pwa-v2 المعتمد في portfolio-hub/01-projects/electricity-billing-pwa. package.json name `webapp` v0.1.0. V1: moain2026/electricity-billing-pwa (public، Prisma + SQLite + JWT، آخر push 2026-06-09).
- **Primary language / stack:** TypeScript 5 · Next.js 16.2.2 (App Router) · React 19.2.4 · Tailwind CSS 4 · Dexie 4.4 (IndexedDB) + dexie-react-hooks · pdf-lib + @pdf-lib/fontkit + arabic-reshaper + bidi-js (PDF عربي نصّي) · jspdf / pdfmake / html-to-image · Service Worker يدوي (بلا Workbox) · خط IBM Plex Sans Arabic مضمَّن (`public/fonts`) — المصدر: package.json، src/lib/db.ts، src/lib/pdf-arabic.ts، public/sw.js.
- **Problem:** محطات الكهرباء الأهلية الصغيرة والمتوسطة تُصدر فواتير الاستهلاك يدوياً؛ والنسخة الأولى احتاجت خادماً وقاعدة بيانات ومصادقة، بينما العميل يريد تطبيقاً يُثبَّت على جوال الموظف ويعمل بلا إنترنت (README «نظرة عامة»؛ docs/PIVOT_LOCAL_PWA.md قرار 2026-06-09).
- **Solution / core features:** PWA محلي بالكامل: قاعدة البيانات في الجهاز (IndexedDB عبر Dexie: subscribers / invoices / settings)، بلا باك-إند ولا API ولا مزامنة. بوابة تهيئة (تثبيت PWA + رمز ترخيص)، شاشة بداية، إدارة المشتركين (إضافة/بحث مؤجَّل/تفعيل-تعطيل/حذف متسلسل بقائمة ⋮)، إصدار فاتورة بحساب فوري (استهلاك × سعر + خدمات + متأخرات − مدفوع) وتفقيط عربي، أرشيف مع تصفية حسب الحالة، فاتورة A4 أفقية تُطبع كنص قابل للتحديد وتُشارك كـ PDF عربي حقيقي (pdf-lib + fontkit)، تصدير/استيراد قاعدة البيانات JSON كنسخة احتياطية، واجهة جوال بشبكة 2×2 وشريط سفلي عائم ذهبي (docs/OMAR_FEEDBACK.md)، تحسينات أداء (عدّادات مفهرسة، حد 200 صف) — git log 2026-06-09/10.
- **Architecture notes:** `src/app/{dashboard,subscribers,subscribers/new,invoices,invoices/new,invoices/archive,invoices/[id]/print,settings}` (9 page.tsx) · `src/components` (10) · `src/lib/db.ts` (Dexie schema v1، تصدير/استيراد) · `src/lib/invoice-utils.ts` (حسابات + تفقيط) · `src/lib/pdf-arabic.ts` · `public/sw.js` (cache v20) · `docs/` 8 وثائق قرار ومراجعة + DECISIONS.md + DOCUMENTATION.md (845 سطراً). **تعارض موثَّق:** README وDECISIONS.md وDOCUMENTATION.md يصفون النسخة القديمة (Prisma + SQLite + JWT + Puppeteer + بيانات دخول admin/clerk)؛ الكود الفعلي بلا أيّ منها — commit `ab40e56` (2026-06-09 «complete pivot to on-device IndexedDB app») حذف 16 ملفاً (prisma/، 10 مسارات api/، auth.ts، prisma.ts، middleware.ts): 46 ملفاً، +682/−3,169 سطراً. المصدر الصحيح للحالة: docs/PIVOT_LOCAL_PWA.md + package.json + src/lib/db.ts.
- **Status:** beta — يعمل محلياً بالكامل (بُني وشُغّل 2026-09-23: `next build` 11 صفحة ثابتة + مسار طباعة ديناميكي، صفر أخطاء TypeScript). رابط Vercel المعلن **404** (2026-09-23). لا اختبارات ولا CI. رمز الترخيص ثابت في الكود (`OnboardingGate.tsx`) — حماية شكلية لا أمنية.
- **Last commit:** 2026-06-10 «SW v20» — 31 commit من 2026-04-06.
- **Live URL:** https://electricity-billing-pwa-v2.vercel.app — 404 وقت الفحص.

## الأرقام ومصادرها / Numbers & sources
| Metric | Value | Source |
|---|---|---|
| Pages (page.tsx) | 9 | `find src/app -name page.tsx \| wc -l` |
| Static routes at build | 11 (10 ○ + /invoices/[id]/print ƒ) | مخرجات `npm run build` 2026-09-23 |
| IndexedDB tables | 3 (subscribers · invoices · settings) | `src/lib/db.ts` سطر `this.version(1).stores` |
| API routes | **0** (V1: 10) | `find src -path '*api*'` = 0؛ V1 `find src/app/api -name route.ts` = 10 |
| Server dependencies removed | Prisma · @prisma/client · bcryptjs · jsonwebtoken · cookie · Puppeteer | `git show ab40e56 -- package.json` |
| Runtime dependencies | 13 (V1: 10) | `package.json` dependencies |
| React components | 10 | `ls src/components` |
| TS/TSX LOC (src/) | 2,370 (V1: 2,650) | `find src -name '*.ts*' \| xargs cat \| wc -l` |
| Tracked files | 89 (V1: 93) | `git ls-files \| wc -l` |
| Commits | 31 (V1: 12) — 2026-04-06 → 2026-06-10 | `git log --oneline \| wc -l` |
| Pivot commit | 46 files, +682 / −3,169 | `git show --stat ab40e56` |
| Service Worker cache version | v20 | `public/sw.js` سطر 1 |
| Decision/review docs | 8 في docs/ + DECISIONS.md (33) + DOCUMENTATION.md (845) | `ls docs/*.md`، `wc -l` |
| Screenshots in repo | 11 (shots/) | `ls shots` |
| Default unit price | 220 ريال/kWh | `src/lib/db.ts` DEFAULT_SETTINGS؛ DECISIONS.md §9 |
| README example | 24,149 → 25,254 = 1,105 kWh × 220 = 243,100 ريال | README «الحسابات التلقائية»؛ أُعيد إنتاجه في اللقطة desktop-11 |
| Tests | 0 | `find . -name '*.test.*' -o -name '*.spec.*'` (خارج node_modules) = 0 |
| CI | none | لا `.github/` |
| Render cap | 200 صف | git log 2026-06-10 «200-row render cap» |
| GitHub stars | 0 | api.github.com/repos/moain2028/electricity-billing-pwa-v2 (2026-09-23) |
| Users / stations | غير موثَّق | docs/OMAR_FEEDBACK.md يشير إلى عميل واحد (عمر) بلا أرقام — لا يُعرض |

## V1 → V2 (مقاس من المستودعَين 2026-09-23)
| | V1 moain2026/electricity-billing-pwa | V2 moain2028/electricity-billing-pwa-v2 |
|---|---|---|
| التخزين | SQLite عبر Prisma (5 models: User, Subscriber, Invoice, AuditLog, Setting) | IndexedDB عبر Dexie (3 جداول) في الجهاز |
| الخادم | Next.js API routes ×10 + middleware + JWT | لا شيء — 0 مسارات API |
| PDF | Puppeteer على الخادم | داخل المتصفح (pdf-lib + fontkit، خط مضمَّن) |
| المصادقة | admin/clerk + bcrypt + JWT cookie | بوابة رمز ترخيص محلية (localStorage) |
| النسخ الاحتياطي | — | تصدير/استيراد JSON |
| Commits | 12 (2026-04-06 → 2026-06-09) | 31 (→ 2026-06-10) |
| LOC src/ | 2,650 | 2,370 |

## ملاحظات التنظيف / Cleanup notes
- README/DECISIONS/DOCUMENTATION تصف النسخة القديمة (Prisma/SQLite/JWT/Puppeteer، بيانات دخول لا وجود لها، وأمر clone إلى موقع moain2026 القديم) — تُعاد كتابتها وفق PIVOT_LOCAL_PWA.md (أعلى أولوية).
- رابط Vercel 404 — إعادة النشر أو حذفه من README وdescription.
- رمز الترخيص مكتوب في الكود العام — يُذكر كـ«بوابة تهيئة» لا «حماية».
- `OnboardingGate.tsx` يستورد خط Cairo من Google Fonts (يتعارض مع العمل offline في أول تشغيل).
- لا اختبارات ولا CI — لا يُدّعى «مختبَر».
- `docs/OMAR_FEEDBACK.md` وMASTER_PLAN تحمل اسم عميل وتخطيطاً مُلغى (multi-user) — لا تُستخدم كمنجز.
