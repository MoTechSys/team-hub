motech-cli | كاتب المحتوى | 2026-09-23 | ready

# motech-cli — Technical Sheet (Motech CLI)

- **Repo:** moain2028/motech-cli (public، أُنشئ على هذا الحساب 2026-09-23) — نفس HEAD `1b1d51b` لمستودع moain2026/motech-cli (public، يحمل الإصدار v0.1.0 المنشور 2026-06-15 بـ 11 ملفاً: 6 ثنائيات + SHA256SUMS + .sig + .pem + install.sh + install.ps1). الرخصة: ملكية خاصة «All rights reserved» (LICENSE) — ليس مفتوح المصدر رغم أن الكود عام.
- **Primary language / stack:** Go 1.23 · اعتماد خارجي واحد مباشر (`golang.org/x/term`) + `x/sys` غير مباشر · `CGO_ENABLED=0 -trimpath -ldflags "-s -w"` · GitHub Actions (CI مصفوفة ubuntu/windows/macos + cross-compile؛ Release بـ cosign keyless) · سكربتا تثبيت sh/PowerShell — المصدر: go.mod، .github/workflows/*.yml، scripts/.
- **Problem:** ربط جهاز عميل بمنصة Motech (الوصول الآمن عن بُعد) كان يحتاج مثبّتاً رسومياً كاملاً؛ المطلوب أمر واحد متعدد المنصات يربط الجهاز بشبكة NetBird ويثبّت مفتاح SSH العام من الخادم ويعمل كخدمة خلفية (README «Cross-platform, single-command secure-access agent»؛ PROGRESS «lightweight alternative to the full GUI installer»).
- **Solution / core features:** 6 أوامر (setup · register · run · status · uninstall · version). التسجيل يبادل توكن إعداد لمرة واحدة مع الخادم (`POST /api/agent/register`) ويستلم توكن وكيل ومفتاح إعداد NetBird والمفتاح **العام** فقط — الخادم يملك الزوج ولا يحمل العميل مفتاحاً خاصاً أبداً. الانضمام إلى NetBird بـ SSH المدمج (`--allow-server-ssh`) بلا تعديل sshd. كتابة المفتاح في authorized_keys بوسم لتدوير سطرنا فقط (0600). خدمة خلفية: systemd / launchd / Scheduled Task. heartbeat يعالج أوامر الخادم (rotate / disable / install_pubkey / apply_ssh) ويصلح الانضمام ذاتياً. التوكن لا يُقبل كوسيط أبداً (prompt بلا صدى أو متغير بيئة يُمسح بـ Unsetenv). TLS صارم 1.2+ وإعادة محاولة 5 مرات بتراجع أسّي 2/4/8/16 ث. المثبّت يتحقق من SHA256 قبل التثبيت؛ الإصدار موقَّع cosign keyless بهوية الـ workflow (README، SECURITY.md، internal/proto/client.go، cmd/motech/main.go).
- **Architecture notes:** `cmd/motech/main.go` (الأوامر، الطباعة عربية/إنجليزية) · `internal/proto` (العقد السلكي RegisterRequest/Response + Heartbeat، عميل HTTP، `proto_contract_test.go` يحرس الانجراف عن الباك-إند motech-platform) · `internal/agent` (التسجيل، الحلقة، الحالة `/etc/motech/agent.json` 0600) · `internal/platform` (واجهة `Platform` بتنفيذات linux/darwin/windows + تنزيل NetBird) · `scripts/install.sh|.ps1` · `.github/workflows/ci.yml|release.yml` · SECURITY.md · PROGRESS.md.
- **Status:** v0.1.0 (2026-06-15) — بُني واختُبر محلياً 2026-09-23: `go vet` صفر، 6/6 اختبارات PASS، 6 أهداف تُبنى؛ CI معلن «ALL GREEN» في PROGRESS (لم أتحقق من سجل Actions). الإصدار الموقَّع موجود فعلاً على moain2026 (11 ملفاً) لا على moain2028 (tag فقط، بلا release) — روابط README تشير إلى moain2026. قرار مفتوح في PROGRESS: كان المستودع خاصاً فالسطر الواحد كان يعيد 404؛ الآن المستودع عام على الحسابَين. مضيف سكربت التثبيت المذكور في PROGRESS لم يستجب (2026-09-23).
- **Last commit:** 2026-06-15 — 3 commits (كلها 2026-06-15).
- **Live URL:** none (أداة CLI؛ صفحة الإصدار: github.com/moain2026/motech-cli/releases/tag/v0.1.0).

## الأرقام ومصادرها / Numbers & sources
| Metric | Value | Source |
|---|---|---|
| Commands | 6 | `cmd/motech/main.go` switch (setup, register, run, status, uninstall, version)؛ `./motech --help` محلياً |
| Targets (OS × arch) | 6 (linux/darwin/windows × amd64/arm64) | `.github/workflows/ci.yml` cross-build؛ بُنيت محلياً 2026-09-23 |
| Release assets v0.1.0 | 11 (6 binaries + SHA256SUMS + .sig + .pem + 2 installers) | api.github.com/repos/moain2026/motech-cli/releases (2026-09-23) |
| Binary size | ≈5.4–5.8 MB لكل هدف | `ls -la dist/` محلياً (linux/amd64 5,587,096 B) |
| Internal packages | 3 (agent, platform, proto) | `ls internal` |
| Go files / LOC | 16 / 1,486 | `find . -name '*.go' \| xargs cat \| wc -l` |
| Tests | 6 test functions in 3 files — all PASS | `go test -v ./...` محلياً 2026-09-23 |
| go vet | 0 issues | `go vet ./...` exit 0 |
| Direct dependencies | 1 (`golang.org/x/term`) | go.mod |
| CI jobs / steps | 2 jobs (test matrix ×3 OS, cross-build) · 9 steps | `.github/workflows/ci.yml` |
| Release workflow steps | 8 (build 6 targets, SHA256SUMS, cosign sign-blob, publish) | `.github/workflows/release.yml` |
| Retry policy | 5 attempts, backoff 2/4/8/16 s | `internal/proto/client.go` |
| TLS minimum | 1.2, no InsecureSkipVerify | `internal/proto/client.go` |
| State file perms | 0600 (`/etc/motech/agent.json`) | README «Security»؛ platform_linux.go |
| Tracked files | 27 | `git ls-files \| wc -l` |
| Commits | 3 (2026-06-15) | `git log --oneline \| wc -l` |
| Docs | README 87 · SECURITY 49 · PROGRESS 56 lines | `wc -l` |
| GitHub stars | 0 (كلا الحسابَين) | GitHub API 2026-09-23 |
| Clients / deployments | غير موثَّق — لا يُعرض | PROGRESS يذكر E2E واحداً بلا أرقام عملاء |

## ملاحظات التنظيف / Cleanup notes
- README/PROGRESS يشيران إلى moain2026 (الإصدار هناك فعلاً) — يُقرَّر المستودع الكانوني ويُنشر الإصدار على moain2028 أو تُوحَّد الروابط.
- LICENSE ملكية خاصة بينما المستودع عام — يُوضَّح المقصود (عام للتوزيع، لا للتعديل).
- PROGRESS يحوي مضيف سكربت تثبيت مؤقت لم يستجب — يُحذف أو يُحدَّث.
- لا CHANGELOG؛ الإصدار في الثنائي يُضبط بـ ldflags فقط.
- توصيات SECURITY المفتوحة (Authenticode، notarization، branch protection) تُذكر كـ«قادم» لا كمنجز.
