soc-wazuh | الباحث | 2026-09-23 | v2

# soc-wazuh — بحث وتحليل (Research & Analysis)
تاريخ الوصول لكل الروابط أدناه: 2026-09-23 (تحقُّق HTTP 200 ما لم يُذكر غير ذلك). أرقام المشروع من tech.md/README فقط.

## 1. من يشتري هذا؟ (تحليل سوق مختصر)
- الشريحة المستهدفة في الـ brief: طلاب الأمن السيبراني ومشاريع التخرج، والفرق الصغيرة التي تريد SOC بلا ترخيص. (brief.ar.md)
- حجم الفئة الأم: سوق SIEM العالمي يقدَّر بـ 7.59 مليار دولار في 2025 مع توقع 13.67 مليار في 2031 (MarketsandMarkets — https://www.marketsandmarkets.com/Market-Reports/security-information-event-management-market-183343191.html). تقديرات أخرى تختلف (Mordor Intelligence: 10.67 مليار في 2025 — https://www.mordorintelligence.com/industry-reports/global-security-information-and-event-management؛ IMARC: 7.0 مليار — https://www.imarcgroup.com/security-information-event-management-market). الاختلاف كبير بين المصادر، فتُذكر كنطاق لا كرقم واحد.
- ما يهم قرارنا: المشروع لا يبيع منتجاً بل يبيع «قدرة» (تصميم/نشر/توثيق SOC مفتوح المصدر) — المشتري الفعلي هنا هو الجامعة/الطالب (مادة تعليمية ومشروع تخرج) والشركة الصغيرة (خدمة إعداد). حجم هاتين الفئتين لم يُعثر على رقم موثوق له في الوقت المتاح: يُستكمل.
- إشارة طلب حقيقية: مستودعات "SOC lab with Wazuh + Suricata" كثيرة على GitHub وأسئلة الطلاب على Reddit عن Wazuh لمشاريع التخرج (مثال: https://www.reddit.com/r/cybersecurity/comments/1n4ttha/is_it_still_best_practice_to_combine_wazuh_and/) — دليل على أن الفئة نشطة، لا قياس لحجمها.

## 2. المنافسون / البدائل (3 + بدائل مشابهة)
| البديل | ما هو | الرابط | ماذا يقول عن نفسه | أين يتفوّق مشروعنا (من tech.md فقط) |
|---|---|---|---|---|
| Security Onion | توزيعة Linux مجانية ومفتوحة لصيد التهديدات ومراقبة أمن الشبكة وإدارة السجلات؛ تضم Elastic Stack + Suricata + Zeek + Elastic Fleet. منذ 2.4 (2023) أُزيل Wazuh منها واستُبدل بـ Elastic Agent. | https://securityonionsolutions.com/ · https://github.com/Security-Onion-Solutions/securityonion · إعلان إزالة Wazuh: https://blog.securityonion.net/2023/03/ | «free and open platform for threat hunting, enterprise security monitoring, and log management» | مشروعنا يوثّق كل قاعدة/مستوى وحالة استخدام خطوة بخطوة مع أمر المحاكاة (docs/lab/UC-01..08) — أي مادة تعليمية قابلة للتكرار، بينما Security Onion منصة جاهزة «صندوق». ويضيف الاستجابة النشطة (VirusTotal + YARA حذف تلقائي) وهي ليست محور Security Onion. |
| Wazuh (المنصة نفسها) | منصة XDR/SIEM مجانية مفتوحة المصدر — هي الأساس الذي بُني عليه المشروع، وتوثيقها الرسمي يقدّم «Proof of Concept guide» بحالات مماثلة. | https://wazuh.com/ · https://github.com/wazuh/wazuh · https://documentation.wazuh.com/current/proof-of-concept-guide/index.html | «free and open source security platform that unifies XDR and SIEM protection» | البديل الحقيقي للطالب هو «أتّبع دليل Wazuh الرسمي». ما يضيفه مشروعنا: دمج Suricata + auditd/CDB + YARA + VirusTotal في معمل واحد بإعدادات منفصلة نظيفة (26 ملفاً)، وعقد قياس MTTD مع 145 اختباراً، وخطة اختبار إحصائية (30 محاولة/حالة، خط أساس 12 ساعة) — لا يوجد ذلك في دليل PoC. |
| AlienVault OSSIM (LevelBlue) | SIEM مفتوح المصدر قديم يجمع Snort/Nessus/Nmap/OpenNMS وغيرها في منتج واحد؛ آخر إصدار في README المستودع 5.1.1، والمستودع الرسمي يبدو غير نشط. | https://github.com/alienfault/ossim · صفحة المنتج: https://levelblue.com/products/ossim · تحميل: https://sourceforge.net/projects/os-sim/ | «Open Source SIEM… integrate, qualify and correlate both high level and low level security and network events» | مشروعنا على مكوّنات حديثة مدعومة (Wazuh 4.14.7، Suricata 8.0.6، YARA 4.5.5) وموثّق بالعربية؛ OSSIM مجاني لكن مجمّد نسبياً وبلا مسار تعليمي للطلاب. |
| Elastic Security (Free tier) | SIEM مجاني ضمن الرخصة الأساسية لـ Elastic Stack ذاتي الإدارة (كشف تهديدات جاهز، إدارة وكلاء). | https://www.elastic.co/blog/elastic-siem-free-open · https://www.elastic.co/pricing/self-managed | «Elastic SIEM: free and open for security analysts everywhere» | متطلبات موارد أعلى ومنحنى تعلم أكبر؛ مشروعنا يعمل على OVA واحدة + وكيلين وهو ما يناسب معمل جامعة. (مقارنة الموارد تقديرية — لا قياس في المستودع.) |
| مستودعات طلابية مشابهة | SOC-LAB (Wazuh + ELK + Zeek + pfSense)، Wazuh-SOC-Lab | https://github.com/Hatim-Bousseta/SOC-LAB · https://github.com/marxgoo/Wazuh-SOC-Lab | «fully functional, open-source-based SOC environment designed for learning» | الفرق الموثَّق: مشروعنا يحمل سجل مشكلات وقرارات وحالة مشروع، واختبارات وحدة (145)، وعقد قياس — وهو نادر في مستودعات المعامل الطلابية. (لم أُجرِ فحصاً كمياً لمستودعاتهم؛ الادعاء مقصور على ما في مستودعنا.) |

## 3. التموضع المقترح
«معمل SOC مفتوح المصدر موثّق قاعدةً بقاعدة، بإعدادات قابلة للنشر وعقد قياس — لا مجرد لقطات.»
- الرسالة للطلاب: كل تنبيه في اللوحة له صفحة تشرح لماذا ظهر وكيف تعيده.
- الرسالة للفرق الصغيرة: إعدادات Wazuh جاهزة للنسخ بلا ترخيص، مع سكربت تحقق.
- ما لا نقوله: «مُثبَت» أو «يكشف في X ثانية» — README يشترط إعادة تحقق حي، ولا نتائج MTTD بعد.

## 4. الكلمات المفتاحية
AR (10): مركز عمليات أمنية مفتوح المصدر · مشروع تخرج أمن سيبراني · Wazuh بالعربية · Wazuh Suricata معمل · كشف التسلل Suricata · قواعد Wazuh المخصصة · الاستجابة النشطة Wazuh · YARA فحص الملفات · مراقبة سلامة الملفات FIM · SIEM مجاني للشركات الصغيرة
EN (10): open source SOC lab · Wazuh SIEM graduation project · Wazuh Suricata integration · Wazuh active response VirusTotal · YARA Wazuh integration · auditd Wazuh CDB list · Shellshock detection Wazuh · file integrity monitoring Wazuh · MITRE ATT&CK Wazuh mapping · free SIEM for students
(المصدر: مصطلحات المشروع نفسها من README/tech.md + صياغة SEO؛ لم يُجرَ قياس حجم بحث — يُستكمل مع متخصص SEO.)

## 5. ثلاث زوايا محتوى
1. «من الحدث إلى التنبيه»: سلسلة منشورات، كل منشور حالة استخدام واحدة بلقطتها وقاعدتها ومستواها (8 حلقات جاهزة من docs/lab).
2. «لماذا 30 محاولة و12 ساعة؟»: شرح خطة القياس الإحصائية للطلاب — كيف تقيس زمن الكشف بصدق بدل رقم واحد لامع (tests/TEST_PLAN.md).
3. «SOC بدون ترخيص لفريق من 3»: دليل عملي للشركات الصغيرة من إعدادات wazuh/ مع تحذير صريح بما يُستكمل.

## 6. الفجوات (صريحة)
تقنياً:
- لا إعادة تحقق حي للحالات الثماني على المعمل الحالي؛ اللقطات تاريخية (أغسطس 2026) ولا تعتمد الكود الحالي (README).
- لا نتائج MTTD فعلية؛ الأداة موجودة والنتائج صفر (tests/README.md).
- استجابة YARA على Windows غير مؤكدة التنفيذ (ISSUE-006)؛ IP هدف Shellshock من شبكة مختلفة (ISSUE-004).
- CI غير مفعّل على GitHub (`workflows-pending`).
- الوكيل win1 كان «disconnected» وقت اللقطة (docs/02_ARCHITECTURE.md §2).
تسويقياً:
- اسم المستودع `my-bro` لا يدل على المحتوى (tech.md يقترح soc-wazuh-graduation).
- README موجّه لوكلاء الذكاء الاصطناعي أكثر من الطلاب؛ يحتاج مقدمة بشرية قصيرة (tech.md).
- اللقطات تحوي أسماء مستخدمين حقيقية (kaliabdualrahman، omar) وIPs — مقبولة للنشر التعليمي، لكن يُفضَّل لقطات جديدة بأسماء عامة.
- الملكية: README يقول «© فريق المشروع»، ودور معين (مشرف/مطوّر) غير موثّق — يجب حسمه قبل النشر باسمه.
- لا رابط حي ولا فيديو ديمو في المستودع الأصلي.

## 7. المصادر
- المستودع: https://github.com/moain2028/my-bro (عام، 200) — README.md · docs/00_PROJECT_STATE.md · docs/02_ARCHITECTURE.md · docs/lab/UC-06_shellshock.md · tests/README.md · wazuh/ · scripts/attack-emulation/
- portfolio-hub: 01-projects/soc-wazuh/{brief.ar.md, brief.en.md, tech.md, links.md}
- روابط المنافسين والسوق كما في الجداول أعلاه (كلها 200 عند الوصول 2026-09-23، عدا grandviewresearch.com 403 فاستُبعد).

## Summary (EN)
Buyers: cybersecurity students/capstone teams and small teams wanting a license-free SOC. The parent SIEM market is estimated at USD 7.6–10.7B in 2025 depending on the analyst. Alternatives: Security Onion (dropped Wazuh in 2.4, Elastic-based appliance), Wazuh's own PoC guide, AlienVault OSSIM (aging), Elastic Security free tier, and peer student labs. Our edge, strictly from tech.md: rule-by-rule documented use cases with emulation commands, 26 clean deployable configs, a 145-test MTTD measurement contract with a statistical test plan, and disciplined repo governance. Gaps: no live re-verification, no real MTTD results, Windows YARA AR unconfirmed, CI pending, unclear repo name and authorship.
