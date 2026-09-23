soc-wazuh | الباحث | 2026-09-23 | v2

# soc-wazuh project pack v2 — مصدر كل نص ورقم وصورة

المصدر الحي: https://github.com/moain2028/portfolio-hub → 01-projects/soc-wazuh/ (سحب 2026-09-23) + المستودع الأصلي https://github.com/moain2028/my-bro (آخر commit 2026-09-09، 60 commit).

## النصوص والأرقام على التصاميم (A + B + C)
| العنصر | النص/الرقم | المصدر |
|---|---|---|
| العنوان AR | مركز عمليات أمنية مفتوح المصدر — مشروع تخرج بـ Wazuh وSuricata وYARA | brief.ar.md — سطر العنوان |
| Title EN | Open-Source SOC — a graduation project on Wazuh, Suricata, and YARA | brief.en.md — title |
| السطر التعريفي AR | كل حالة استخدام موثّقة خطوة بخطوة مع قاعدة التنبيه ومستواه، وإعدادات Wazuh نظيفة قابلة للنشر مع سكربت تحقق. | brief.ar.md — «الحل»، الجملة الأخيرة |
| Tagline EN | Every use case is documented with its alert rule and level, plus deployable configs and a validation script. | brief.en.md — "Solution", last sentence |
| 8 حالات استخدام | 8 | README جدول الحالات · tech.md (UC-01..08) · brief «النتيجة» |
| 26 ملف إعداد Wazuh | 26 | tech.md ← شجرة `wazuh/` (تحقّقت: `find wazuh -type f` = 26 بتاريخ 2026-09-23) |
| 145 اختباراً محلياً | 145 | tech.md ← tests/README.md «145 اختباراً محلياً: 123 قياس + 22 أمان» |
| 5 سكربتات محاكاة هجوم | 5 | tech.md ← scripts/attack-emulation/ (eicar, malware_downloader, netcat, nmap, shellshock — تحقّقت) |
| تاجات التقنيات | Wazuh 4.14.7 · Suricata 8.0.6 · YARA · VirusTotal · auditd · Kali Linux | README · tech.md «stack» · docs/02_ARCHITECTURE.md §3 |
| الشريحة | طلاب / Students (#8B5CF6) | مهمة التوزيع (مدير المنتج 2026-09-23) · 02-brand/README.md |
| التذييل | github.com/moain2028/my-bro | النسخة العامة المحددة في المهمة؛ HTTP 200 بتاريخ 2026-09-23 |
| نسخة logo | Moain Al-Abbasi / معين العباسي (نص فقط) | project-pack-standard-v2.md §A |
| النص الخافت | #A3B1C0 | تحديث v2 المعتمد 2026-09-23 |
| كاروسيل 1 (المشكلة) | نص brief «المشكلة» حرفياً | brief.ar/en |
| كاروسيل 2 (الحل) | نص brief «الحل» (الجملة الأولى) | brief.ar/en |
| كاروسيل 3 (كيف يعمل) | Shellshock → access.log → القاعدة 31168 مستوى 15 → MITRE T1068/T1190 | docs/lab/UC-06_shellshock.md · docs/02_ARCHITECTURE.md §4–5 · اللقطة report-06 تُظهر الصف نفسه |
| كاروسيل 4 (الأرقام) | 8 · 26 · 145 · 5 + «إعادة التحقق الحي: يُستكمل» | tech.md · README «تحتاج إعادة تحقق حي» · brief «النتيجة» |
| كاروسيل 5 (لمن) | نص brief «لمن يفيد» + «تواصل» | brief.ar/en |
| بطاقة الرقم | 8 حالات استخدام + أسماؤها | README جدول الحالات |
| الريل (6 مشاهد) | كما في copy.*.md «نص الريل» | brief + UC-06 + tech.md؛ ≤6 كلمات/مشهد حسب editorial-style-guide §3 |

## الصور
| الملف المستخدم | ماذا يعرض | الأصل | معالجة |
|---|---|---|---|
| crops/report-06-events.png | لوحة Wazuh — MITRE ATT&CK، وكيل kali1، صف «Shellshock attack detected» مستوى 15، القاعدة 31168 | 01-projects/soc-wazuh/screenshots/report-06-img19.png (من تقرير المعمل، أغسطس 2026) | قصّ الشريط العلوي (72px: شعار Wazuh/اسم المستخدم) فقط؛ لا تعديل آخر |
| crops/report-03-events.png | لوحة Wazuh — Threat Hunting، أحداث auditd «Highly Suspicious Command» (القاعدة 100210) | screenshots/report-03-img11.png | نفس القصّ |
| crops/report-02-events.png | لوحة Wazuh — Threat Hunting، وكيل kailatak، أحداث SCA/agent | screenshots/report-02-img05.png | نفس القصّ |
| report-08-img27.png | nano: /var/ossec/etc/rules/local_rules.xml (القواعد 100300/100301/108000/108001/100050) | screenshots/ كما هو | بلا تعديل |
| report-07-img24.png | nano: /var/ossec/active-response/bin/yara.sh | screenshots/ كما هو | بلا تعديل |
| تسميات شريط المتصفح | «wazuh-dashboard · MITRE ATT&CK · kali1» وغيرها | تسمية وصفية للصفحة، لا URL (لا رابط حي — links.md) | — |

ملاحظات: اللقطات تاريخية من تقرير المعمل (README يحذّر أنها لا تعتمد الكود الحالي) — مُعلَن هنا. تحوي أسماء مستخدمين (kaliabdualrahman/omar) وIPs معملية؛ لا أسماء عملاء. لا لقطة مولَّدة. الأرقام داخل اللقطات (hits، timestamps) لم تُقتبس في أي نص.

## الملفات النصية
- soc-wazuh-explainer.ar/en.md — كل فقرة تحمل مصدرها بين قوسين (brief/tech/README/docs).
- soc-wazuh-research.md — كل منافس/رقم سوق برابط وتاريخ وصول 2026-09-23.
- soc-wazuh-copy.ar/en.md — من brief المختوم + tech.md؛ حالة draft حتى ختم المحرر.

## التحقق
- 24 تصميماً + 10 كاروسيل + 2 بطاقة رقم + 2 بانر + 2 غلاف ريل = 40 PNG مطابقة للمقاسات بالبكسل (assert في make_pack.py / فحص نهائي).
- ريلان 1080×1920، 30fps، 25.5 ث، بلا شعار، لا مشهد خطأ/404، بلا موسيقى (لا يوجد مصدر موسيقى بلا حقوق متاح داخل بيئة العمل — يُستكمل عند النشر أو يضيفها صانع الفيديو).
- التباين: Sand/Amber/Mist على Navy > 7:1؛ الخافت #A3B1C0 على Navy ≈ 8:1.
- أدوات التوليد مرفقة: make_pack.py · make_carousel.py · make_reel.py · spec.json (تعتمد 02-brand/scripts/brand.py).
