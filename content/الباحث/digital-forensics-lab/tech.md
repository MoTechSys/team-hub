digital-forensics-lab | الباحث | 2026-09-23 | ready

# digital-forensics-lab — Technical Sheet (مختبر تحليل جنائي رقمي عملي — مشروع تعليمي)

- **Repo:** moain2028/digital-forensics-lab (public) — النسخة الأصلية كانت على حساب Moain2026 (روابط README ما زالت تشير إليه)
- **Primary language / stack:** PowerShell 5 (Windows side: Registry / Event Log / triage) · Python 3 stdlib فقط (`browser_history_parser.py`، `Parse-AmCache.py`) · Bash (`install.sh`) · Sigma YAML · HTML/CSS (تقارير RTL) · أدوات: Autopsy 4.21.0 · The Sleuth Kit 4.12.1 · FTK Imager 4.7 · BrowsingHistoryView (NirSoft) · Chrome/Chromium · GitHub Languages: PowerShell 59.4% · Python 23.4% · HTML 13.7% · Shell 3.5%
- **Problem:** مقرر تحليل جنائي رقمي يطلب تغطية خمسة مواضيع (Windows Registry، Event Log، Autopsy، FTK Imager، Browser Forensics) بتطبيق عملي موثّق بلقطات وأدلة حقيقية، لا بالشرائح فقط.
- **Solution / core features:** (1) محلل سجل متصفح Chromium/Firefox يعمل على نسخة عمل ويعيد التحقق من البصمة (MD5+SHA-256) قبل/بعد، ويصدر CSV/HTML؛ (2) مُشغّل PowerShell بأمر واحد يستخرج Registry (SystemInfo/USBSTOR/BAM) وEvent Log (4624/4625/1102/6005/6006) ويبني Timeline موحّدًا وChain of Custody بـ SHA-256 ويلتقط لقطات آليًا ويولّد تقرير HTML عربي RTL بوسوم MITRE؛ (3) 3 قواعد Sigma أصلية؛ (4) أدوات متقدمة (DFIR triage مع VSS، AmCache parser، USB→Process→PrivEsc correlation، ISO/IEC 27037 integrity check)؛ (5) توثيق منهجي (METHODOLOGY.md، research.md، محتوى 25 شريحة، فهرس صور العرض).
- **Architecture notes:** جذر المستودع = الجانب Linux (Autopsy + Browser Forensics + المحلل)؛ `windows-forensics/` = الجانب Windows (Registry/Event Log/FTK) مع `evidence/` (data CSV/JSON، screenshots، PRESENTATION_IMAGES مقصوصة ومفهرسة، report HTML)؛ لا خدمة تعمل — كل المخرجات ملفات ثابتة قابلة لإعادة التوليد بالأوامر الموثقة.
- **Status:** prototype / coursework — مكتمل كمشروع تعليمي؛ تنفيذ Autopsy توقّف قبل مرحلة التحليل (الصورة الرابعة D04 رسمية من sleuthkit.org — مُعلَن).
- **Last commit:** 2026-09-14 (7 commits: 1 بتاريخ 2026-09-13 من Moain2026 + 6 بتاريخ 2026-09-14 من «حارس (DFIR Agent)»)
- **Live URL:** none (مستودع + تقارير HTML ثابتة)

## الأرقام ومصادرها / Numbers & sources
| Metric | Value | Source (file/line or command) |
|---|---|---|
| المواضيع المغطاة | 5 (Registry, Event Log, Autopsy, FTK Imager, Browser Forensics) | README.md سطر 3–4 |
| سجلات سجل المتصفح المسترجعة | 19 | تشغيل محلي 2026-09-23 `[+] Records recovered: 19` + `reports/parser_console_output.txt` + `docs/METHODOLOGY.md` |
| حجم دليل المتصفح | 163,840 بايت | `stat -c %s evidence-info/History_EVIDENCE.db` + README §3 |
| بصمة MD5 للدليل | `1fc18eb16b982a25b681e2c6522fa14c` | `md5sum` محليًا = README §3 |
| بصمة SHA-256 للدليل | `456a181c02b62bab4096bd52d88c2906545e8543d3acf93ccde9c8b799d2a800` | `sha256sum` محليًا = README §3 |
| فحص السلامة بعد التحليل | PASSED | تشغيل محلي + `reports/parser_console_output.txt` |
| قواعد Sigma | 3 | `ls windows-forensics/sigma_rules/*.yml` |
| تقنيات MITRE ATT&CK المذكورة في الكود/القواعد | 16 معرّفًا فريدًا (T1021.001, T1052.001, T1053, T1059, T1059.001, T1070, T1070.001, T1070.004, T1070.006, T1078, T1091, T1105, T1110, T1204, T1489, T1548) | `grep -o "T1[0-9]{3,4}(\.[0-9]{3})?" --include=*.ps1 --include=*.yml --include=*.py \| sort -u` |
| معرّفات Event Log المستخرجة | 6 (4624, 4625, 1102, 6005, 6006 + تصنيف Boot/Shutdown) | `windows-forensics/README.md` §Event Log؛ `Run-Windows-Forensics.ps1` |
| محاولات دخول فاشلة (4625) في الدليل | 15 | `windows-forensics/evidence/data/E2_Failed_Logons.csv` (15 سجلًا) + لقطة A05 |
| أجهزة USB في USBSTOR | 7 | `R2_USB_Devices.csv` (7 صفوف) + لقطة A02 |
| سجلات BAM | 211 | `R3_BAM.csv` |
| أحداث Timeline الموحّد | 37 | `T1_Timeline.csv` |
| ملفات أدلة مبصومة (Chain of Custody) | 7 | `windows-forensics/evidence/report/chain_of_custody.csv` |
| صور العرض المقصوصة والمفهرسة | 40 (A9 + B13 + C10 + D4 + E4) | `ls PRESENTATION_IMAGES` (بدون INDEX.md) |
| لقطات المؤلف الحقيقية (Registry/EventLog/Timeline/CoC) | 9 | `windows-forensics/evidence/screenshots/` وPRESENTATION_IMAGES/A* |
| سكربتات قابلة للتشغيل | 9 (6 PowerShell: Run-Windows-Forensics, Install, Forensics-Helper, Invoke-DFIRTriage, Detect-USBBrutforce-Chain, Verify-Evidence-Integrity · 2 Python: browser_history_parser, Parse-AmCache · 1 Bash: install.sh) | `find -name "*.ps1" -o -name "*.py" -o -name "*.sh"` |
| أسطر الكود (سكربتات) | 1,640 (6 ps1: 1,081 · 2 py: 578 · install.sh: 81) | `wc -l` |
| شرائح العرض المكتوبة | 25 | `windows-forensics/SLIDE_CONTENT_FULL.md` (`grep -c "^## سلايد"`) — README يقول 21 (قديم) |
| صورة القرص (Autopsy) | `nps-2009-canon2-gen6.E01` · 31,129,600 بايت · MD5 `750b509d…cdc61` · FAT12 · ملف محذوف `_MG_0025.JPG` | README §4 + METHODOLOGY.md — **غير مُضمَّنة في المستودع، لم تُعاد هنا** |
| Commits | 7 | `git log --oneline \| wc -l` |
| ملفات | 122 | `find -type f` (بدون .git) |
| حجم المستودع | 23 MB | `du -sh` |
| Stars / Forks | 0 / 0 | صفحة GitHub 2026-09-23 |
| مراجع أكاديمية 2024–2026 | 9 مرجعًا | `windows-forensics/README.md` §المراجع |

**لا يُعرض تسويقيًا:** «~5 دقائق» و«10 دقائق» (تقديرات README غير مقاسة)، «الأول على الدفعة»، أي وقت تنفيذ.

## ملاحظات التنظيف / Cleanup notes
- **لا ملف LICENSE** رغم أن README يقول MIT (`/blob/main/LICENSE` → 404).
- **بيانات شخصية في الأدلة:** اسم الجهاز `ABDUL1` واسم المستخدم `abdul_alrahman` في `R1_SystemInfo.json`، `E1/E2/T1 *.csv`، `report/index.html`، ولقطات A01/A04/A05/A08 وأسماء ملفاتها. يُقترح إعادة التسمية أو التعمية قبل أي نشر.
- **اسم الأستاذ** («Dr. Omar» / «د. عمر») في README (سطر 3)، `windows-forensics/README.md`، `report/index.html` (عنوان)، `INDEX.md`، `DESIGNER_BRIEF.md`، `SLIDE_CONTENT_FULL.md`، واسم ملف `USB_Image_Acquisition_by_Dr_Omar.pptx` — وأيضًا مجلد `reference_materials_from_professor/` بملفَي docx/pptx من الأستاذ (حقوق نشر محتملة).
- روابط README (one-liner + clone) تشير إلى الحساب القديم `Moain2026` — تعمل الآن لكن يُفضَّل التحديث إلى `moain2028`.
- `author:` في قواعد Sigma الثلاث = «أصول الضيافة (DFIR-Toolkit)» — اسم مشروع آخر من المحفظة؛ يُوحَّد.
- README يذكر «21 سلايد» بينما SLIDE_CONTENT_FULL يحوي 25؛ ويذكر «لقطات F1..F14» و«R1..R4» غير موجودة بهذه الأسماء.
- مسارات `C:/Users/PC`، `C:\Users\Fxu`، `C:\Users\student`، `Desktop\...` ظاهرة في لقطات B09/B13/C07/C09/C10.
- **نسب المشروع الأكاديمي** (فريق/فرد/مشرف) — بند قرار قائم عند محمد كما kitabi/crypto-lab/soc-wazuh؛ الصياغة المعتمدة الآن: «مشروع تعليمي / مختبر عملي».
