motech-platform | مهندس | 2026-09-23 | research v2 — بحث ويب مؤرَّخ (تاريخ الوصول لكل رابط: 2026-09-23)

# منصة Motech — بحث وتحليل السوق (E)

**Executive summary (EN):** Motech Platform sits in the "secure remote access to managed Windows fleets" niche. The three closest alternatives an IT team would actually weigh are Tailscale (mesh VPN + Tailscale SSH), Teleport (certificate-based access platform) and MeshCentral (open-source remote management). All three are broader and more mature; Motech's distinct angle — from tech.md only — is backend-owned per-client ed25519 keys (private key never leaves the server), a NetBird-native mesh with a signed Windows agent, a one-link install, an RTL Arabic dashboard, and a single Go binary per component. Gaps are explicit below: no deployment figures, no live demo, no releases verified, no tests beyond 7 Go files, and no activity since June.

## 1) من يشتري هذا؟ (السوق)
- المشتري: فرق تقنية المعلومات ومورّدو البرمجيات الذين يدعمون أجهزة Windows عن بُعد (brief.ar.md — لمن يفيد؛ tech.md — الشريحة: شركات).
- حالة الاستخدام: دعم أجهزة العملاء والفروع (Windows غالباً) عن بُعد، بديلاً عن كلمات المرور المشتركة ومفاتيح SSH المتناثرة بلا تدوير ولا سجل (tech.md — المشكلة).
- حجم الفئة: **يُستكمل** — لا رقم سوقي موثّق في مصادر المشروع، ولم أضع تقديراً مخترعاً.

## 2) ثلاث بدائل فعلية (روابط حقيقية، وصول 2026-09-23)

### أ) Tailscale (+ Tailscale SSH)
- الرابط: https://tailscale.com/pricing · https://tailscale.com/kb/1193/tailscale-ssh
- ماذا يقول: شبكة mesh قائمة على WireGuard؛ «Tailscale SSH is available for all plans»؛ الأسعار: Personal «$0 for up to 6 users»، Standard «$8 per user, per month»، Premium «$18 per user, per month»، Enterprise حسب الطلب.
- قيد مهم: «Tailscale SSH's server component is only available on: Linux, macOS (open source tailscale + tailscaled CLI)» — أي أن جهاز Windows لا يعمل خادم Tailscale SSH؛ يُتصل *منه* لا *إليه*.
- أين يتفوّق Motech (من tech.md فقط): يستهدف أجهزة Windows كطرف مُدار بوكيل .exe موقّع Authenticode يعمل كخدمة، والوصول عبر SSH المدمج في NetBird؛ المفاتيح تُولَّد وتُدوَّر من الخادم مع سجل نشاط.

### ب) Teleport (Community / Enterprise)
- الرابط: https://goteleport.com/pricing/ · https://goteleport.com/docs/faq/ · https://goteleport.com/docs/feature-matrix/
- ماذا يقول: «Teleport is a certificate authority» — وصول SSH بشهادات قصيرة العمر؛ «Teleport provides two editions: Teleport Enterprise, Teleport Community Edition»؛ التسعير «Pay only for what you use: active users and protected resources» (بلا أرقام معلنة على الصفحة؛ Vendr يذكر «$12–$18 per resource per month» كتقدير سوقي غير رسمي). في Community Edition الـ SSO محدود بـ GitHub وفق مصفوفة الميزات.
- أين يتفوّق Motech (من tech.md فقط): بساطة النشر — ملف Go واحد للخادم وواحد للوكيل، PostgreSQL قياسي بمتغيّر `DATABASE_URL` واحد، JWT ذاتي بلا SDK خارجي؛ لوحة عربية RTL؛ التبديل بين NetBird Cloud وSelf-hosted بمتغيّر واحد. Teleport أشمل بكثير (Kubernetes، قواعد بيانات، تسجيل الجلسات) لكنه أثقل تشغيلاً.

### ج) MeshCentral (مفتوح المصدر)
- الرابط: https://github.com/Ylianst/MeshCentral · https://docs.meshcentral.com/
- ماذا يقول: «you can run your own web server to remotely manage and control computers on a local network or anywhere on the internet»؛ «full web-based remote desktop, terminal and file management capability»؛ الترخيص «Apache 2.0»؛ وكلاء لـ Windows وLinux وmacOS وAndroid.
- أين يتفوّق Motech (من tech.md فقط): نموذج «المفاتيح مملوكة للخادم» — زوج ed25519 لكل عميل، الخاص مشفّر AES-256-GCM لا يلمس جهاز العميل؛ وصول SSH عبر شبكة NetBird mesh بدل خادم ويب مكشوف؛ تدوير مفاتيح بدورة confirm/ack. MeshCentral أغنى وظيفياً (سطح مكتب بعيد وملفات) ومجاني بالكامل.

### مرجع رابع (منصة الشبكة التي يبني عليها Motech، ليس منافساً)
- NetBird: https://netbird.io/pricing — Free «up to 5 users · 100 machines»، Team «€6 user / month»، Business «€12 user / month»، Enterprise حسب الطلب، مع خيار self-hosted. مهم لتسعير الحل الكامل: Motech يضيف طبقة إدارة المفاتيح والوكيل فوق NetBird، فتكلفة NetBird (أو استضافته ذاتياً) جزء من التكلفة الإجمالية للعميل.

## 3) التموضع
- جملة التموضع (من brief/tech): «وصول آمن عن بُعد لأجهزة العملاء، والمفاتيح بيد الخادم» — منصة مركزية تولّد وتدوّر مفاتيح SSH لكل عميل، مع وكيل Windows موقّع على شبكة NetBird ولوحة عربية.
- المنافس يقول «شبكة» (Tailscale) أو «هوية وشهادات» (Teleport) أو «تحكّم كامل بالجهاز» (MeshCentral). Motech يقول «إدارة مفاتيح الوصول لأسطول Windows، بأبسط نشر ممكن وبالعربية».
- لا نُقارن بالأرقام التشغيلية (لا أرقام نشر فعلية — brief: «يُستكمل»).

## 4) الكلمات المفتاحية
AR (10): إدارة الوصول عن بُعد · مفاتيح SSH للشركات · تدوير مفاتيح SSH · الوصول الآمن لأجهزة العملاء · بديل كلمات المرور المشتركة · شبكة NetBird · وكيل Windows موقّع · لوحة تحكم عربية للدعم التقني · سجل نشاط الوصول · دعم فني عن بُعد للفروع
EN (10): remote access management · SSH key management · SSH key rotation · backend-owned SSH keys · NetBird mesh access · Windows fleet remote support · signed Windows agent · zero shared passwords · access audit log · Go PostgreSQL remote access platform

## 5) ثلاث زوايا محتوى
1. **«لماذا لا يجب أن يلمس المفتاح الخاص جهاز العميل»** — شرح نموذج ed25519 + AES-256-GCM من tech.md (مقال تقني + كاروسيل «كيف يعمل»).
2. **«من 3 أجهزة إلى 1000+: تصميم للتوسّع قبل الحاجة»** — المبادئ المعمارية (ملف Go واحد، PostgreSQL قياسي، NetBird cloud/self-hosted) مع التصريح أنه هدف تصميمي.
3. **«أمر واحد على ثلاث منصات»** — Motech CLI: 6 أوامر، cosign keyless، SHA256SUMS، ورمز التفعيل لا يُقبل كوسيط (فيديو/تيرمينال قصير).

## 6) الفجوات (صريحة)
- تقنياً: لا أرقام نشر فعلية (brief: يُستكمل)؛ لا رابط حي (الرابط في docs/SETUP.md لا يستجيب — tech.md)؛ رابط releases للـ CLI غير متحقَّق؛ الاختبارات 4 ملفات في platform + 3 في CLI فقط؛ لا نشاط في المستودع الأصلي منذ 2026-06-16 (النسخة الأحدث motech_V2 آخر commit 2026-06-24)؛ ترخيص Proprietary يحدّ من الاعتماد المجتمعي مقارنةً بـ MeshCentral/Teleport Community.
- تسويقياً: لا دراسة حالة ولا عميل مُعلن؛ لا فيديو تعريفي منشور (links.md: يُستكمل)؛ لا صفحة منتج عامة؛ اللوحة عربية لكن brief يصنّف المشروع «EN أولاً» — يلزم قرار لغة الجمهور.
- تعارض يجب حسمه قبل النشر الخارجي: المستودع الكانوني (moain2026/motech-platform ↔ MoTechSys/motech-platform ↔ moain2028/motech_V2) — tech.md: «يُحدَّد الكانوني».

## 7) المصادر
- portfolio-hub/01-projects/motech-platform: brief.ar.md · brief.en.md · tech.md · links.md · screenshots/README.md
- README github.com/moain2028/motech_V2 (HTTP 200، 2026-09-23) · README github.com/moain2028/motech-cli (HTTP 200)
- https://tailscale.com/pricing · https://tailscale.com/kb/1193/tailscale-ssh (2026-09-23)
- https://goteleport.com/pricing/ · https://goteleport.com/docs/faq/ · https://goteleport.com/docs/feature-matrix/ · https://goteleport.com/how-it-works/ (2026-09-23)
- https://www.vendr.com/marketplace/teleport (تقدير سوقي غير رسمي، 2026-09-23)
- https://github.com/Ylianst/MeshCentral · https://docs.meshcentral.com/ (2026-09-23)
- https://netbird.io/pricing (2026-09-23)
