alabbasi-tech-platform | متخصص SEO | 2026-09-23 | ready

# alabbasi-tech-platform — Technical Sheet (العباسي تِك — الموقع الرسمي ومنصة العملاء)

- **Repo:** moain2028/alabbasi-tech-platform (public) — مجلدان `site/` و`portal/` + `docs/`؛ commit واحد (2026-08-07) بمؤلف «Alabbasi Tech»
- **Primary language / stack:** TypeScript · **site:** Next.js 15.5.4 + React 19.1، `output: 'export'` ثابت بالكامل، TS strict + noUncheckedIndexedAccess، CSS خالص بـ`@layer` وخصائص منطقية (بلا Tailwind)، Vitest، ESLint، Stylelint (use-logical) · **portal:** Node/Express 5، better-sqlite3 (WAL)، zod، jsonwebtoken (HS256)، bcryptjs، helmet، multer، pino · واجهة المنصة HTML/CSS/JS خام تحت `/portal/`
- **Problem:** بيت هندسة برمجيات في صنعاء يحتاج موقعاً رسمياً يعمل على أندرويد رخيص وشبكة ضعيفة (كل بايت قابل للتخزين على الحافة)، يعرض أرقاماً مُتحقَّقة بأوامر git لا ادعاءات، ويستقبل طلبات العملاء ويتابع مشاريعهم وتذاكرهم (README الجذر، site/README «التموضع»، portal/README ADR-P001)
- **Solution / core features:** **الموقع:** 19 صفحة عربية RTL (رئيسية، أعمالنا، 4 أنظمة + فهرس، 5 خدمات، بديلان لأنظمة مغلقة، كيف نعمل، من نحن، تواصل، 404، sitemap، robots)، صفر صور (أيقونات SVG مضمّنة)، JSON-LD وOG وmeta description في كل صفحة، نموذج طلب مربوط بالمنصة · **المنصة:** مصادقة JWT في httpOnly cookies (`ap_at` على `/`، `ap_rt` على `/api/auth`)، CSRF بـSameSite=Strict + فحص Sec-Fetch-Site، bcrypt cost 12، throttle 5 محاولات/15 دقيقة → 429، مقارنة ثابتة الزمن ضد تعداد الحسابات، أخطاء RFC 9457، zod على كل مدخل؛ وحدات auth · projects · tickets (مرفقات بفحص magic bytes وتنظيف الاسم ضد path traversal) · requests (نموذج عام + إدارة) · users؛ 3 أدوار و11 كود صلاحية في طبقة domain؛ صندوق صادر outbox → تيليجرام عبر cron
- **Architecture notes:** ADR-P001: الموقع ثابت والمنصة صفحات client-side تنادي API منفصلاً على 127.0.0.1:3100 يوزّعه Caddy على `/api/*` · أربع طبقات لكل موديول domain → application → infrastructure → presentation (نمط motech-pos) · ترحيلات مُرقَّمة داخل `db.js` (001-init، 002-ticket-attachments) · نظام تصميم «مادي معتم»: النحاسي #C45C3E · الهيكل #211F24 · الأساس #D9D9D9؛ الضوء من أعلى-يسار فالظلال لا تُعكس في RTL؛ ظلال alpha ≥ .26 + حد 1px؛ خصائص منطقية حصراً؛ tracking عربي ≥ 0؛ احتياطي خارج `@layer` لـAndroid WebView < 99 (README الجذر «نظام التصميم»)
- **Status:** production-ready code (بُني ونُشر مؤقتاً على gensparkclaw في 2026-08)، لكن **بلا رابط حي الآن**: الدومين alabbasi.tech غير مسجَّل والروابط المؤقتة معطّلة وقت الفحص · السجل التجاري «قيد الإجراء» صراحة في الموقع (site/README)
- **Last commit:** 2026-08-07 (commit واحد)
- **Live URL:** none (انظر links.md)

## الأرقام ومصادرها / Numbers & sources
| Metric | Value | Source (file/line or command) |
|---|---|---|
| Site pages built | 19/19 | `npm run build` محلياً 2026-09-23 «Generating static pages (19/19)»؛ README الجذر «١٩ صفحة» |
| TypeScript errors | 0 | `npm run typecheck` محلياً 2026-09-23 (exit 0)؛ README «tsc --noEmit: صفر أخطاء» |
| Tests (site) | 11 passed (1 file) | `npx vitest run` محلياً 2026-09-23 — `site/src/lib/__tests__/site.test.ts` |
| Tests (portal) | none | `portal/package.json` scripts.test = placeholder؛ README المنصة: «16/16 ملف يمرّ node --check» |
| Pixel audit — pages × widths | 14 × 2 (390/768) = 28 عرضاً | `docs/pixel-audit-site.md` رأس التقرير (2026-08-06) |
| Horizontal overflow | 0 px في 28 عرضاً | `docs/pixel-audit-site.md` §2 «نتائج نظيفة» |
| Text overlap · broken images · touch < 24px | 0 · 0 · 0 | `docs/pixel-audit-site.md` §2 |
| Contrast defects | 151 مؤكَّداً وقت التدقيق → README يقول «0 (كانت 151)» بعد الإصلاح | `docs/pixel-audit-site.md` §1 · README الجذر «بوابات الجودة» (الإصلاح غير مُعاد قياسه في المستودع — يُستكمل) |
| Touch targets < 44px | 14 وقت التدقيق → 0 بعد الإصلاح | README الجذر «بوابات الجودة» |
| Portal audit worst contrast (pre-fix) | 1.22:1 على «← الموقع» | `docs/pixel-audit-portal.md` §1 · README «العطل ①» يوثّق الإصلاح `a:not([class]){color:inherit}` |
| Permission codes | 11 | `grep -oE "'[A-Z_]+'" portal/src/modules/auth/domain/permission.js \| sort -u \| wc -l` |
| Roles | 3 (client · staff · admin) | `portal/README.md` «الأدوار» |
| Portal modules | 5 (auth · projects · tickets · requests · users) | `ls portal/src/modules` |
| Portal API routes | 22 | `grep -rn "router\.\(get\|post\|patch\|delete\|put\)" portal/src \| wc -l` |
| DB migrations | 2 (001-init · 002-ticket-attachments) | `portal/src/infrastructure/db/db.js` سطر 16 و98 |
| Site source | 27 ملف ts/tsx · 3086 سطراً (src) · globals.css 894 سطراً | `git ls-files site/src` + `wc -l` |
| Portal source | 22 ملف js · 1607 سطراً (src) · portal.css 327 سطراً | `git ls-files portal/src` + `wc -l` |
| Repo files · commits | 85 · 1 | `git ls-files \| wc -l` · `git rev-list --count HEAD` |
| Audit tool | `docs/pixel-audit.js` 216 سطراً | `wc -l` |
| Users / clients | يُستكمل — لا عملاء موثّقون للمنصة | — |
| Numbers shown on /work/ (10 systems · 518 commits · 3884 files · 51 migrations · 128 tests · CTR 0.4→2.1% · 76→556 impressions · Lighthouse 100) | **أرقام عن مشاريع أخرى** لا عن هذا المستودع؛ README يعرض إثباتها بأوامر git على تلك المستودعات | README الجذر «قاعدة المحتوى» · `site/src/lib/site.ts` — لا تُستخدم على تصاميم هذا المشروع إلا منسوبة للموقع كمحتوى |

## ملاحظات التنظيف / Cleanup notes
- **لا رابط حي**: الدومين غير مسجَّل والنشر المؤقت معطّل — يُنشر بعد شراء alabbasi.tech وضبط `NEXT_PUBLIC_SITE_URL`.
- الموقع يحوي رقم هاتف واتساب (`site/src/lib/site.ts`، `Cta.tsx`، JSON-LD في `layout.tsx`) — طُمس في لقطات `/contact/`؛ لا يُنقل إلى أي تصميم.
- الموقع يذكر منافسَين بالاسم في صفحتَي البدائل (YemenSoft Onyx Pro · ZKTeco) — محتوى الموقع نفسه، يظهر في اللقطات الحقيقية؛ يُقرَّر مع معين هل تُستخدم هذه اللقطات في النشر.
- portal بلا اختبارات آلية؛ README يعتمد `node --check` فقط.
- commit واحد فقط بتاريخ 2026-08-07 — لا تاريخ تطوير مرئي في git.
- `docs/pixel-audit-portal.md` يذكر مساراً محلياً `/home/work/.openclaw/...` — يُنقّى قبل العرض العلني.
- README الجذر يقول «١٨ صفحة» في site/README و«١٩» في الجذر والبناء — المعتمد 19 (البناء الفعلي).
