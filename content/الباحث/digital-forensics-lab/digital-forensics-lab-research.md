digital-forensics-lab | الباحث | 2026-09-23 | v2 — E (بدائل حقيقية، تموضع، كلمات، زوايا، فجوات)

# E — البدائل والتموضع

> القاعدة: نقارن بمنصات مختبرات DFIR ومقررات مؤسسية، لا بمشاريع طلاب أفراد. كل رابط فُحص بتاريخ 2026-09-23 (HTTP 200). الأسعار كما تظهر على صفحات المزوّد يوم الفحص وقد تتغيّر.

## 1) ثلاثة بدائل حقيقية

| البديل | ما هو | ما يقدّمه | التسعير (كما في المصدر) | الرابط (فُحص 2026-09-23) |
|---|---|---|---|---|
| **Blue Team Labs Online (BTLO)** — Security Blue Team | منصة تدريب دفاعي «designed for defenders that already have experience with security tools and investigations» | تحديات مجانية قابلة للتنزيل (memory dumps، phishing emails، packet captures، logs) + «273 unique investigation labs» للمشتركين | مجاني للتحديات؛ الاشتراك £15/شهر، £40.5/3 أشهر، £76.5/6 أشهر، £144/سنة | https://blueteamlabs.online/ · https://support.blueteamlabs.online/hc/en-gb/articles/27488518976412-Getting-Started-with-BTLO |
| **CyberDefenders** | منصة «vendor-neutral, hands-on cyber defense training» + شهادة CCD | مختبرات Blue Team في DFIR وThreat Hunting وThreat Intelligence وMalware Analysis، «new additions published every week»، تعمل من المتصفح بلا إعداد | حساب مجاني مع «5 hours across their accounts lifetime» على Trial Labs؛ Pro بحسب مصدر ثالث (DFIR Diva، 2025-03-10): $20/شهر – $200/سنة | https://cyberdefenders.org/ · https://cyberdefenders.org/blue-team-labs/ · https://help.cyberdefenders.org/en/articles/9544344-cyberrange-free-trial-labs |
| **SANS FOR500: Windows Forensic Analysis** (GIAC GCFE) | مقرر مؤسسي «focuses on building in-depth digital forensics knowledge of Microsoft Windows operating systems» | 6 أقسام، «22 hands-on labs and a capstone Windows Forensic Challenge»؛ يغطي Registry (Hives/MRU/Deleted Keys)، Event Log (EVTX)، Web Browser Forensics (Chrome/Edge/IE/Firefox)، USB Forensics (Serial، Last Drive Letter) | «Course price $8,780 USD» (بدون الضرائب) | https://www.sans.org/cyber-security-courses/windows-forensic-analysis/ |

بديل رابع مرجعي (مصدر بيانات لا منافس): **Digital Corpora** — «digital corpora for use in computer forensics education research»، صور أقراص ولقطات ذاكرة وشبكة «freely available and may be used without prior authorization» — وهو نفسه مصدر صورة القرص المستخدمة في هذا المشروع. https://digitalcorpora.org/

## 2) التموضع

المشروع ليس منصة تدريب ولا مقررًا؛ هو **مختبر مفتوح المصدر قابل لإعادة التنفيذ** يُظهر كيف تُبنى منهجية جنائية كاملة (اقتنِ → ابصم → حلّل → وثّق → أعد البصمة) على المواضيع الخمسة الأساسية، بأدوات مجانية وأدلة حقيقية، وبكود يمكن قراءته وتعديله — لا بمختبرات مغلقة تُحلّ داخل متصفح ولا بمقرر بآلاف الدولارات.

- مقابل BTLO/CyberDefenders: هم يقدّمون **حجمًا** (مئات المختبرات) و**سيناريوهات جاهزة**؛ المشروع يقدّم **الشفافية**: الكود الذي يستخرج الأثر مفتوح، وسلسلة الحيازة ملف CSV يمكن التحقق منه، والتقرير يُولَّد لا يُملأ.
- مقابل SANS FOR500: يغطي نفس عائلة الآثار (Registry، Event Log، Browser، USB) لكن كنقطة انطلاق **مجانية وعربية** للطالب قبل أو بدون مقرر بـ $8,780.
- الجملة الواحدة: «مختبر DFIR مفتوح المصدر: خمسة مواضيع، منهجية واحدة، وكل رقم ببصمة».

## 3) الكلمات المفتاحية (10 + 10)

**عربي:** التحليل الجنائي الرقمي · مختبر DFIR · Windows Registry · سجل الأحداث Event Log · سلسلة الحيازة · بصمة SHA-256 · قواعد Sigma · MITRE ATT&CK · تحليل سجل المتصفح · صورة القرص الجنائية

**English:** digital forensics lab · DFIR hands-on · Windows Registry forensics · Event Log 4625 brute force · chain of custody · SHA-256 evidence integrity · Sigma rules · MITRE ATT&CK mapping · browser history forensics · Autopsy Sleuth Kit

## 4) ثلاث زوايا للمحتوى

1. **«الدليل الذي لا يتغيّر»** — قصة البصمة قبل وبعد: لماذا ينسخ المحلل ملف SQLite قبل فتحه (journal/WAL)، وكيف تُقرأ «Integrity re-check: PASSED». زاوية تعليمية للطلاب.
2. **«من 4625 إلى T1110»** — كيف تتحوّل 15 محاولة دخول فاشلة إلى نمط Brute Force مصنَّف بـ MITRE في خط زمني موحّد، ثم إلى قاعدة Sigma. زاوية «الكشف كقاعدة» لمهتمي SOC.
3. **«أمر واحد، تقرير كامل»** — أتمتة الاستخراج (Registry + Event Log + Timeline + Chain of Custody + HTML) بسطر PowerShell واحد. زاوية DFIR-as-Code للمهندسين.

## 5) الفجوات الصريحة (لا تُخفى)

- تنفيذ Autopsy توقّف قبل مرحلة التحليل؛ الصورة الرابعة (D04) رسمية من sleuthkit.org — مُعلَن في INDEX.md ولم تُستخدم في التصاميم.
- لقطات FTK Imager (B01–B13) من محاضرة الأستاذ لا من تنفيذ المؤلف — استُخدمت واحدة فقط (نتيجة Match) بوصف «توضيحية».
- صورة القرص غير مضمّنة في المستودع (تُحمَّل من Digital Corpora)؛ خطوات Autopsy/TSK لم تُعاد في بيئتنا.
- `Parse-AmCache.py` يحتاج حزمة `python-registry` غير المثبتة وملف hive من ويندوز — لم يُختبر.
- الدليل الويندوزي من جهاز طالب واحد (اسمه ومستخدمه طُمسا في تصاميمنا وما زالا في ملفات المستودع).
- «~5 دقائق» و«10 دقائق» في README تقديرات غير مقاسة — لا تُستخدم تسويقيًا.
- لا ملف LICENSE رغم إعلان MIT.
