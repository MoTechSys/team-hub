alabbasi-tech-platform | متخصص SEO | 2026-09-23 | v2

# SOURCES — مصدر كل نص ورقم وصورة في alabbasi-tech-platform-project-pack-v2

المرجع: https://github.com/moain2028/alabbasi-tech-platform (commit واحد 2026-08-07) — README الجذر · site/README.md · portal/README.md · portal/CHANGELOG.md · site/DEPLOYMENT.md · docs/pixel-audit-site.md · docs/pixel-audit-portal.md — و`0-project/tech.md` (تحقق محلي 2026-09-23) و`02-brand/README.md` في portfolio-hub.

## الصور (كلها حقيقية من تشغيل محلي للمستودع — لا شيء مولّد)
| الاستخدام | الملف في `0-project/screenshots/` | ملاحظة |
|---|---|---|
| البطل (A كلها، B بانر، C مشهد 1) | `desktop-01-home.png` 2880×1800 + `mobile-01-home.png` 780×1688 | الصفحة الرئيسية `/` من `site/out` بعد `npm run build` |
| B كاروسيل 2 / C مشهد 3 | `desktop-02-work.png` | صفحة `/work/` |
| B كاروسيل 1 (خافتة) / C مشهد 2 | `desktop-03-systems.png` | صفحة `/systems/` |
| B كاروسيل 3 / C مشهد 6 | `desktop-14-portal-tickets.png` | لوحة المنصة، تبويب التذاكر، حساب تجريبي |
| B كاروسيل 5 / C مشهد 4 | `mobile-08-portal-projects.png` · `mobile-02-work.png` | لوحة المنصة على الجوال + أعمالنا |
| بيانات المنصة | — | حساب تجريبي واحد (demo@example.test، «مدير تجريبي») أُنشئ بـ`scripts/seed-admin.js`؛ لا مشاريع/تذاكر/طلبات (عدّادات 0)؛ لا بيانات حقيقية |
| طمس | `desktop-10-contact.png` · `mobile-05-contact.png` | زر واتساب برقم الهاتف مطموس؛ هذه اللقطات ليست في التصاميم |
| غير مستخدمة في التصاميم | `desktop-05/06-alternatives*`، `desktop-11-zero-trust` وغيرها | موجودة في 0-project للأرشيف؛ صفحات البدائل تسمّي منافسَين بالاسم — بانتظار قرار |
| الأداة | `tools/shoot.py` · `tools/shoot_portal.py` · `tools/combo.py` | Playwright/Chromium 2x؛ خادم محلي يقدّم الموقع والمنصة معاً ويمرّر /api |

## النصوص والأرقام
| العنصر | AR / EN | المصدر |
|---|---|---|
| H1 | «موقع رسمي ثابت ومنصة عملاء لبيت هندسة برمجيات» / “Static official site and client portal for a software house” | brief.ar/en.md (هذا التسليم) ← README الجذر عنوان المستودع «الموقع الرسمي ومنصة العملاء» + «بيت هندسة برمجيات · صنعاء» |
| اسم المشروع | العباسي تِك / Alabbasi Tech · alabbasi-tech-platform | README الجذر · site/README |
| السطر التعريفي | «موقع Next.js 15 بتصدير ثابت كامل — 19 صفحة عربية RTL بلا صورة واحدة — ومنصة عملاء Express + SQLite: مشاريع، تذاكر، طلبات واردة، و11 كود صلاحية.» / EN | brief «الحل» ← site/README «التقنية» (static export، صفر صور) · portal/README «الوحدات» · README «11 كود صلاحية» |
| 19/19 — صفحة تُبنى ثابتة | `npm run build` محلياً 2026-09-23 «Generating static pages (19/19)»؛ README الجذر «١٩ صفحة» |
| 0 — أخطاء TypeScript | `npm run typecheck` محلياً (exit 0)؛ README «tsc --noEmit: صفر أخطاء» |
| 11 — اختباراً ناجحاً | `npx vitest run` محلياً: 11 passed (site/src/lib/__tests__/site.test.ts) |
| 0 px — تمرير أفقي في 28 عرضاً | docs/pixel-audit-site.md §2 «تمرير أفقي: ٠px في كل ٢٨ عرضاً» (14 صفحة × 390/768) |
| 11 — كود صلاحية · 3 أدوار (B، C) | `grep` على portal/src/modules/auth/domain/permission.js = 11؛ portal/README «الأدوار» |
| 22 — مسار API في المنصة (B، C) | `grep -rn "router\.\(get\|post\|patch\|delete\|put\)" portal/src \| wc -l` = 22 |
| 14 صفحة × عرضَين · 0 تداخل · 0 صور مكسورة (بطاقة الرقم الواحد) | docs/pixel-audit-site.md رأس التقرير و§2 |
| تاجات التقنيات | Next.js 15 · React 19 · TypeScript · Express 5 · SQLite | site/package.json (next 15.5.4، react 19.1.0) · portal/package.json (express ^5.2.1، better-sqlite3) |
| الدعوة للتواصل | «أُقدّم موقعاً وبوابة عملاء تملكهما بالكامل — راسلني.» / “Let's scope a site and portal you own — DM or email.” | brief «للتواصل» ← README «التموضع: … الشفرة والبيانات للعميل» + دليل التحرير (شركات: “Let's scope …”) |
| الكاروسيل — شريحة المشكلة (3 بطاقات) | «صفحات ثقيلة على شبكة ضعيفة · أرقام تسويقية بلا إثبات · طلبات العملاء في رسائل متفرقة» | إعادة صياغة مباشرة لـ: portal/README ADR-P001 «حرج لليمن»، README «قاعدة المحتوى: حقائق مُتحقَّقة فقط»، portal/README «استقبال الطلبات» — لا معلومة جديدة |
| الكاروسيل — الحل | «كل بايت قابل للتخزين على الحافة، عربي RTL من الأساس، أيقونات SVG مضمّنة، JSON-LD وOG في كل صفحة» | portal/README ADR-P001 · site/README «نظام التصميم» · docs/pixel-audit-site.md §2 «البنية والوصولية» |
| الكاروسيل — كيف يعمل | أربع طبقات، JWT httpOnly، CSRF | README الجذر «معمارية المنصة» و«الأمن» |
| الرابط | github.com/moain2028/alabbasi-tech-platform | مهمة #25؛ HTTP 200 في 2026-09-23. لا رابط حي (links.md) |
| شارة الشريحة | شركات / Companies · #3B82F6 | مهمة #25 · 02-brand/README.md |
| الشعار النصّي (نسخة logo في A فقط) | «معين العباسي» / “Moain Al-Abbasi” نصاً بلا أيقونة | project-pack-standard-v2 §A |
| الشرح D · البحث E · النصوص F | داخل كل ملف تعليق مصادر | README/tech.md/docs؛ روابط البحث مؤرّخة 2026-09-23 |

## ما لم يُستخدم عن قصد
- **رقم الهاتف** (site/src/lib/site.ts، Cta.tsx، JSON-LD) — لا يظهر في أي تصميم أو نص؛ مطموس في لقطات /contact/ الأرشيفية.
- **اسم شخص** — لا يوجد على أي تصميم (الحساب التجريبي «مدير تجريبي» فقط).
- **أرقام صفحة /work/** (10 أنظمة، 518 commit، 3884 ملف، 51 ترحيل، 128 اختبار، CTR 0.4→2.1٪، 76→556 ظهور، Lighthouse 100) — تخص مشاريع أخرى لا هذا المستودع؛ لم تُعرض كأرقام لهذا المشروع.
- **أسماء المنافسين** في صفحات البدائل (YemenSoft Onyx Pro، ZKTeco) — لا تظهر على أي تصميم؛ لقطات تلك الصفحات في الأرشيف فقط.
- **151 عيب تباين / 14 هدف لمس** — أرقام «قبل الإصلاح» من التدقيق؛ README يقول 0 بعد الإصلاح بلا إعادة قياس مرفقة، فلم يُعرض أي منهما على التصاميم (فقط في explainer/research بصفتها الحقيقية).
- **الروابط الحية المؤقتة** (gensparkclaw) — معطّلة؛ لا تُنشر.

## الهوية
02-brand/README.md؛ الشريحة شركات #3B82F6؛ النص الخافت #A3B1C0 (v2). التباين: Sand على Navy ≈ 13:1 · Amber ≈ 7.5:1 · Mist ≈ 10:1 · #A3B1C0 ≈ 6.9:1 — فوق AA. nologo: مساحة أمان 12% خالية أعلى-يمين (AR) / أعلى-يسار (EN). الموسيقى: bgm-tech-minimal داخلية بلا حقوق طرف ثالث.

## الأداة (tools/)
`shoot.py` + `shoot_portal.py` + `combo.py` (البند 0) · `make_pack_at.py` (A) · `make_extras.py` (B) · `make_reel.py` (C) — Python 3 + Pillow/raqm + Playwright + ffmpeg؛ مبنية على `02-brand/scripts/brand.py`.
