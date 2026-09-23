motech-cli | كاتب المحتوى | 2026-09-23 | project-pack v2

# Motech CLI project pack v2 — مصادر كل نص ورقم وصورة

المشروع ليس في portfolio-hub؛ البند 0 أنتج `project/` (brief.ar/en.md · tech.md · links.md · screenshots/ + index.md) المرفق في هذه الحزمة وجاهز للإضافة إلى `01-projects/motech-cli/`. المصدر الأصلي: https://github.com/moain2028/motech-cli (main، commit 1b1d51b، 2026-06-15) — README.md، SECURITY.md، PROGRESS.md، LICENSE، go.mod، cmd/motech/main.go، internal/**، scripts/**, .github/workflows/ci.yml + release.yml — وبناء وتشغيل محلي 2026-09-23 (Go 1.23.4، linux/amd64). الإصدار الموقَّع: https://github.com/moain2026/motech-cli/releases/tag/v0.1.0 (GitHub API 2026-09-23: منشور 2026-06-15، 11 ملفاً؛ نفس HEAD).

## إفصاحات صدق (تسري على كل الحزمة)
- المشروع أداة سطر أوامر بلا واجهة رسومية: كل «اللقطات» بطاقات طرفية داكنة تحمل **نصوصاً حقيقية حرفياً** من التشغيل المحلي (`project/screenshots/_txt/*.txt`) مصوَّرة بـ Playwright 2x؛ إطار البطاقة CSS. لا صورة ولا أيقونة مولّدة بالذكاء الاصطناعي.
- **لم يُنفَّذ setup/register على خادم حقيقي**: شُغّلا بلا root وبلا توكن فظهرت بوابة الصلاحيات الفعلية (desktop/mobile-05، 06). التوكن في أوامر التثبيت مُخفى ••••. اسم المستخدم في `ls -la` استُبدل بـ motech؛ لا مسارات شخصية.
- **الإصدار الموقَّع منجَز** (قرار مدير المنتج 2026-09-23): موجود فعلاً على moain2026 بـ 11 ملفاً (6 ثنائيات + SHA256SUMS + .sig + .pem + مثبّتان) — يُحال إليه في links.md وهنا؛ التذييل على كل التصاميم والريل github.com/moain2028/motech-cli (tag v0.1.0 بلا release) — فرق الحسابَين مُعلَن في الفجوات وبنود محمد.
- الأرقام المسموحة على التصاميم: **6 أوامر · 6 أهداف · 1 اعتماد · 6 اختبارات · 11 ملفاً موقَّعاً** — لا غير. لا «ALL GREEN» ولا ادعاء CI (PROGRESS يعلنه ولم يُتحقق من سجل Actions)؛ لا عملاء ولا نشر فعلي؛ Authenticode/notarization «قادم» فقط.
- LICENSE ملكية خاصة «All rights reserved»: الصياغة «الكود عام للاطلاع، ليس مفتوح المصدر» — لا كلمة open source في أي نص من هذه الحزمة.
- الدعوة في nologo «راسلني / DM me» بلا اسم؛ الاسم النصّي «معين العباسي / Moain Al-Abbasi» في نسخة logo فقط.

## A. التصاميم (24 PNG)
| العنصر | AR | EN | المصدر |
|---|---|---|---|
| العنوان | Motech CLI | Motech CLI | README H1 |
| الثانوي | وكيل وصول آمن بأمر واحد | Single-command secure-access agent | README «Cross-platform, single-command secure-access agent» |
| السطر التعريفي | أمر واحد يربط جهاز العميل بشبكة آمنة — بلا مفتاح خاص على العميل | One command joins a client device to a secure mesh — with no private key on the client | brief H1؛ README «Security» + internal/proto/client.go (المفتاح العام فقط) |
| الشارة | Windows · Linux · macOS | | internal/platform/platform_{linux,darwin,windows}.go؛ ci.yml |
| الميزات (X/Hero/Story) | 6 أوامر… · المفتاح الخاص يبقى على الخادم… · خدمة خلفية heartbeat وتدوير… · SHA256 + cosign | (مقابلها) | cmd/motech/main.go · README «Security» · internal/agent/loop.go · scripts/install.sh · release.yml |
| الأرقام الثلاثة | 6 أوامر · 6 أهداف بناء · 1 اعتماد خارجي | 6 commands · 6 build targets · 1 direct dependency | tech.md (main.go switch؛ ci.yml cross-build + بناء محلي؛ go.mod) |
| شارة الشريحة | شركات | Companies | تكليف مدير المنتج؛ #3B82F6 من 02-brand |
| التقنيات (فوتر) | Go 1.23 · NetBird · cosign · GitHub Actions | | go.mod · README · release.yml · ci.yml |
| الرابط | github.com/moain2028/motech-cli | | تكليف مدير المنتج؛ links.md |
| wordmark (logo فقط) | معين العباسي | Moain Al-Abbasi | معيار v2 |
| الخافت | #A3B1C0 | | معيار v2 |
| اللقطات | DESK = desktop-04-help (`motech --help` + `version`) · MOB = mobile-01-test (`go vet && go test` 6/6) · FAN = mobile-01, 04, 02 | | project/screenshots/index.md؛ البطل معتمد من مدير المنتج 2026-09-23 |

## B. تصاميم النشر (14 PNG)
- كاروسيل 5×AR + 5×EN: 1 المشكلة (brief «المشكلة»؛ README/PROGRESS «GUI installer»؛ لقطة 00-install) · 2 الحل (brief «الحل»؛ لقطة 04-help) · 3 كيف يعمل — ثم التوقيع: الرمز لا يُمرَّر كوسيط (main.go prompt/Unsetenv)، المفتاح العام فقط (proto/client.go)، الخدمة بـ heartbeat وتدوير (agent/loop.go، platform_*)، SHA256 قبل التثبيت + cosign بـ 11 ملفاً (install.sh، release.yml، GitHub API)؛ لقطة 03-sums = زاوية التوقيع (قرار مدير المنتج) · 4 الأرقام: 6 · 6 · 6 · 11 (tech.md) · 5 لمن (brief «لمن يفيد» + «للتواصل»؛ لقطة 09-tree).
- بطاقة «رقم واحد»: **0** — «مفتاح خاص على جهاز العميل» (README «Security: the client never holds a private key»؛ internal/proto RegisterResponse يحمل `public_key` فقط؛ TLS 1.2+ client.go؛ الرمز لا يُمرَّر كوسيط main.go) — معتمدة من مدير المنتج.
- بانر 1600×840 AR/EN: العنوان من زاوية «مثبّت رسومي لكل نظام؟ أمر واحد يكفي» (research §5)؛ الأرقام من tech.md؛ اللقطات desktop-02-build + mobile-02-build.

## C. الريلان (1080×1920، 19.6 ث، بلا شعار)
- المشاهد: غلاف (brief H1) → أمر واحد (README Quick start؛ لقطات 04-help + 00-install) → الأمان (README Security، SECURITY.md؛ لقطة 03-sums) → الخدمة (agent/loop.go، platform_*؛ لقطات 05-status + 02-build) → الأرقام (tech.md) → CTA «راسلني / DM me» (brief «للتواصل»؛ لقطة 09-tree). المدد: 3.2 + 3.6×3 + 3.8 + 3.8 − انتقالات 0.4×5 = 19.6 ث.
- بطاقات طرفية بلا إطار هاتف (KIND=cli). الموسيقى: 02-brand/scripts/reels/bgm-tech-minimal.mp3 (أصل الفريق). الغلاف = الإطار 00.

## D. الشرح (explainer AR/EN)
كل جملة من brief/tech/research؛ الأرقام من جدول tech.md (20 صفاً)؛ قسم «ما لم يُنجَز» من tech.md «ملاحظات التنظيف» + research §6. الرخصة بصيغة «عام للاطلاع، ليس مفتوح المصدر».

## E. البحث (research.md)
Tailscale https://tailscale.com/pricing ($0 حتى 6 · $8 · $18) · Teleport https://goteleport.com/pricing/ + /pricing/guide/ (MAU + TPR، بلا أسعار منشورة) · NetBird https://netbird.io/pricing ($0 حتى 5/100 · $6 · $12) + GitHub API لـ tailscale/tailscale (36,777★)، gravitational/teleport (20,935★ AGPL-3.0)، netbirdio/netbird (29,444★) — كلها بتاريخ 2026-09-23.

## F. نصوص النشر (copy AR/EN + نص الريل)
من brief + tech + research؛ الأطوال داخل الحدود (LinkedIn ≤120 · X ≤280 · IG ≤150). draft للمحرر.

## project/ (البند 0)
brief.ar/en.md · tech.md (20 صفاً، كل رقم بأمر/ملف) · links.md · screenshots/ (20 بطاقة 2x + index.md + _txt/ + _term-shoot.mjs).

## tools/
packgen.py · reelgen.py · project.py · _term-shoot.mjs — لإعادة التوليد.
