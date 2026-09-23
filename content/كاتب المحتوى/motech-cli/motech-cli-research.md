motech-cli | كاتب المحتوى | 2026-09-23 | v1

# Motech CLI — بحث وتحليل (Research & positioning)

تاريخ البحث: 2026-09-23 (فتح صفحات الأسعار + GitHub API). كل ادعاء عن مشروعنا من tech.md؛ كل ادعاء عن بديل من رابطه بتاريخ الوصول. لا «ALL GREEN» ولا ادعاء CI غير متحقَّق منه، ولا عملاء، ولا كلمة «مفتوح المصدر» لمشروعنا (LICENSE ملكية خاصة).

## 1. من يشتري هذا؟
- المستخدم: فريق دعم فني أو مزوّد خدمات مدارة (MSP) يربط أجهزة عملاء كثيرة (Windows/Linux/macOS) بمنصة وصول آمن عن بُعد، ويريد أمراً واحداً بلا مثبّت رسومي ولا نسخ مفاتيح يدوي (README «Cross-platform, single-command secure-access agent»؛ PROGRESS «lightweight alternative to the full GUI installer»).
- المشتري في المحفظة: الشريحة «شركات» — الأداة جزء من منصة Motech (الباك-إند motech-platform، #4 على المنصة)، لا منتج مستقل يُشترى وحده.
- حجم الفئة: لا رقم موثّق لدينا. مؤشر غير مباشر: NetBird (الشبكة التي يبني عليها المشروع) عند 29,444 نجمة على GitHub وآخر push 2026-09-23؛ Tailscale 36,777 نجمة — فئة الوصول الشبكي الصفري-الثقة نشطة وكبيرة.

## 2. البدائل الحقيقية (وصول 2026-09-23)
| # | البديل | ماذا هو | السعر المعلن | الرابط | ملاحظة |
|---|---|---|---|---|---|
| 1 | Tailscale | شبكة WireGuard مدارة بعميل لكل نظام + Tailscale SSH | Personal $0 حتى 6 مستخدمين · Standard $8 · Premium $18 للمستخدم/شهر · Enterprise بالتواصل؛ أجهزة غير محدودة | https://tailscale.com/pricing | 36,777★ · BSD-3-Clause (العميل) · آخر push 2026-09-23 |
| 2 | Teleport | منصة هوية للبنية التحتية (SSH/K8s/DB/Desktop) بتدقيق وجلسات مسجَّلة | تسعير بالاستخدام: Monthly Active User + Protected Resource — لا أسعار منشورة بالدولار؛ Enterprise Edition تجارية، سحابية أو ذاتية الاستضافة | https://goteleport.com/pricing/ · https://goteleport.com/pricing/guide/ | 20,935★ · AGPL-3.0 (المستودع) · آخر push 2026-09-17 |
| 3 | NetBird | شبكة WireGuard نظير-لنظير مفتوحة المصدر بلوحة تحكم وSSH مدمج — **الطبقة التي يبني عليها Motech CLI** | Free $0 حتى 5 مستخدمين و100 جهاز · Team $6 · Business $12 للمستخدم/شهر · Enterprise بالتواصل؛ استضافة ذاتية داخل بنيتك | https://netbird.io/pricing · https://github.com/netbirdio/netbird | 29,444★ · آخر push 2026-09-23 |

ملاحظات: Teleport لا ينشر أسعاراً بالدولار على صفحته (النموذج MAU + TPR فقط) فلم يُذكر رقم؛ الأسعار تتغيّر — كلها بتاريخ 2026-09-23.

## 3. التموضع
ماذا يقول المنافسون: شبكات وصول ناضجة، مدارة، بعملاء رسميين لكل نظام ولوحات تحكم وسياسات وصول وتدقيق؛ تُشترى بالمستخدم أو بالمورد. الجهاز يُضاف بتثبيت العميل ثم تسجيل الدخول بحساب.

أين يتميّز Motech CLI (من tech.md فقط):
- **أمر واحد يربط جهاز عميل لا موظفاً**: `motech setup` يبادل رمز تفعيل لمرة واحدة مع خادم Motech وينهي التسجيل والانضمام للشبكة وتثبيت المفتاح وتسجيل الخدمة — بلا حساب مستخدم على الجهاز ولا مثبّت رسومي.
- **لا مفتاح خاص على العميل**: الخادم يملك زوج المفاتيح ويرسل العام فقط؛ الرمز لا يُمرَّر كوسيط قط؛ TLS 1.2+ صارم؛ ملف الحالة 0600.
- **يبني على NetBird لا يستبدله**: الانضمام بـ SSH المدمج (`--allow-server-ssh`) بلا تعديل sshd — فيرث نضج الشبكة ويضيف طبقة التسجيل والتحكم من خادم Motech (rotate / disable / install_pubkey من heartbeat).
- **ثنائي واحد بلا اعتماديات**: Go، اعتماد مباشر واحد، ≈5.5 MB لكل هدف، 6 أهداف، إصدار موقَّع cosign مع SHA256 قبل التثبيت.

أين يتأخر (صريح): ليس منتجاً مستقلاً — يحتاج خادم Motech وشبكة NetBird؛ لا لوحة تحكم ولا سياسات وصول ولا تسجيل جلسات (كل ذلك عند Tailscale/Teleport)؛ الكود عام للاطلاع لكن الرخصة ملكية خاصة (ليس مفتوح المصدر)؛ 3 commits في يوم واحد؛ لا عملاء أو نشر موثَّق؛ الإصدار الموقَّع على حساب moain2026 لا على moain2028 الذي يحمل التذييل؛ CI معلن في PROGRESS ولم يُتحقق من سجل Actions؛ Authenticode وnotarization قادمان لا منجزان.

## 4. الكلمات المفتاحية
AR (10): وكيل وصول آمن عن بُعد · أمر واحد لربط جهاز العميل · NetBird SSH مدمج · مفتاح SSH عام من الخادم · خدمة خلفية systemd launchd · تدوير مفاتيح من الخادم · إصدار موقَّع cosign · تحقق SHA256 قبل التثبيت · أداة Go متعددة المنصات · مزوّدو الخدمات المدارة MSP
EN (10): single-command secure-access agent · cross-platform Go CLI Windows Linux macOS · NetBird mesh SSH onboarding · server-owned SSH key rotation · zero private keys on client · cosign keyless signed release · SHA256 verified installer · systemd launchd scheduled task service · MSP device onboarding tool · heartbeat remote disable agent

## 5. ثلاث زوايا محتوى
1. «مثبّت رسومي لكل نظام؟ أمر واحد يكفي» — زاوية المنتج: من الرمز إلى الخدمة في أمر واحد على ثلاث منصات.
2. «0 مفتاح خاص على جهاز العميل» — زاوية الأمان للمهندسين: الخادم يملك الزوج، الرمز لا يُمرَّر كوسيط، TLS صارم، 0600، SHA256 وcosign.
3. «6 اختبارات وصفر vet قبل أول إصدار» — زاوية الصدق: ما بُني واختُبر فعلاً (6/6، 6 أهداف، إصدار موقَّع بـ 11 ملفاً) وما لم يُنجَز (لوحة، عملاء، Authenticode).

## 6. الفجوات (بلا تجميل)
تقنياً: LICENSE «All rights reserved» رغم أن المستودع عام — يُوضَّح المقصود · README/PROGRESS يشيران إلى moain2026 والإصدار هناك فعلاً؛ moain2028 tag بلا release · مضيف سكربت تثبيت مؤقت في PROGRESS لم يستجب · لا CHANGELOG · CI «ALL GREEN» ادعاء PROGRESS غير متحقَّق منه · توصيات SECURITY المفتوحة (Authenticode، notarization، branch protection) لم تُنفَّذ · 3 commits في يوم واحد · setup/register لم يُجرَّبا على خادم حقيقي في هذه الحزمة (بوابة الصلاحيات فقط).
تسويقياً: لا عملاء ولا نشر موثَّق · لا فيديو ولا دراسة حالة · يعتمد على منصة Motech فلا يُسوَّق وحده · اسم الأمر `motech` عام قد يتعارض مع منتجات أخرى.

## 7. المصادر
- المشروع: https://github.com/moain2028/motech-cli (200، HEAD 1b1d51b) · https://github.com/moain2026/motech-cli/releases/tag/v0.1.0 (11 ملفاً، 2026-06-15) · README.md · SECURITY.md · PROGRESS.md · LICENSE · go.mod · cmd/motech/main.go · internal/** · .github/workflows/ci.yml · release.yml · تشغيل محلي 2026-09-23 (go vet 0 · go test 6/6 · 6 أهداف).
- البدائل: الروابط أعلاه (كلها 200 بتاريخ 2026-09-23) + GitHub API لـ tailscale/tailscale، gravitational/teleport، netbirdio/netbird.

## EN summary
Motech CLI targets IT support teams and MSPs that onboard many client devices to the Motech secure-access platform. Real alternatives (accessed 2026-09-23): Tailscale (free up to 6 users, $8 / $18 per user per month), Teleport (usage-based on active users + protected resources, no published dollar prices, AGPL-3 repo), and NetBird (free up to 5 users / 100 machines, $6 / $12 per user per month, self-hostable) — the mesh Motech CLI builds on. Its edge: one command joins a device (not a person) — activation code exchange, NetBird join with built-in SSH, server-owned public key install, background service with heartbeats and server-driven rotation — with zero private keys on the client, one Go binary, six targets, and a cosign-signed release with SHA256 verified before install. Gaps: not standalone (needs the Motech server and NetBird), no dashboard or session recording, proprietary license despite a public repo, three commits in one day, no documented customers, signed release on moain2026 not moain2028, CI claimed but unverified, Authenticode/notarization pending.
