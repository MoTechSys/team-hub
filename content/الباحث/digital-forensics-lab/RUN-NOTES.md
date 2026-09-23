digital-forensics-lab | الباحث | 2026-09-23 | ready

# RUN-NOTES — ماذا شُغّل فعليًا، وماذا لم يُشغَّل ولماذا

**المستودع المفحوص:** github.com/moain2028/digital-forensics-lab (عام) · الفرع main · 7 commits · آخر commit 2026-09-14 · 122 ملفًا · 23 MB · مستنسخ محليًا في `~/repos/digital-forensics-lab` يوم 2026-09-23.

## 1) ما شُغّل بنجاح هنا (Ubuntu، Python 3.12.3)

| الأمر | النتيجة | مطابقة README؟ |
|---|---|---|
| `python3 scripts/browser_history_parser.py -i evidence-info/History_EVIDENCE.db --csv out.csv --html out.html` | خرج بلا أخطاء؛ **19 سجل URL** مسترجعًا؛ CSV 19 صفًا + رأس؛ HTML مُولَّد | ✅ README §3 وMETHODOLOGY.md «19 URL records recovered» |
| بصمة `History_EVIDENCE.db` (md5sum / sha256sum) | MD5 `1fc18eb1…2fa14c` · SHA-256 `456a181c…9d2a800` · الحجم 163,840 بايت | ✅ مطابقة حرفيًا لـ README §3 «Evidence integrity» |
| فحص السلامة داخل المحلل | `Integrity re-check: PASSED — evidence unmodified` | ✅ مطابق لـ `reports/parser_console_output.txt` |
| فتح `windows-forensics/evidence/report/index.html` و`reports/browser_history_report.html` في Chromium headless | يُعرض التقرير العربي RTL بالكامل (معلومات الجهاز، أجهزة USB، Timeline مع وسوم MITRE) | — (تقرير ثابت مُولَّد سابقًا على ويندوز) |

> ملاحظة: مسار الدليل في `reports/parser_console_output.txt` الأصلي يُظهر `/home/work/forensics-repo/` — مسار جهاز المؤلف؛ إعادة التشغيل هنا أعطت نفس الأرقام والبصمات من مسارنا.

## 2) ما لم يُشغَّل هنا، ولماذا (موثّق بدقة)

| المكوّن | السبب | البديل المعتمَد للّقطات |
|---|---|---|
| `tools/install.sh` (Sleuth Kit + Autopsy + Java 17) | يحتاج `sudo apt` وتحميل Autopsy GUI؛ لا واجهة رسومية في هذه البيئة، وصورة القرص `nps-2009-canon2-gen6.E01` غير مضمّنة في المستودع (تُحمَّل من Digital Corpora) | لقطات Autopsy الفعلية من `screenshots/autopsy/` و`PRESENTATION_IMAGES/D01–D03` (1725×950). **D04 صورة رسمية من sleuthkit.org لا من تنفيذ المؤلف** — كما يُعلن INDEX.md صراحةً؛ لم تُستخدم في التصاميم |
| FTK Imager 4.7 | تطبيق ويندوز فقط | لقطات `PRESENTATION_IMAGES/B01–B13` — **من محاضرة الأستاذ لا من تنفيذ المؤلف** (INDEX.md المجموعة B). استُخدمت لقطة واحدة فقط (B11 نتيجة التحقق Match) بتسمية «توضيحية» |
| `Run-Windows-Forensics.ps1` / `Forensics-Helper.ps1` / `Invoke-DFIRTriage.ps1` | PowerShell + Registry + Event Log ويندوز فقط | لقطات المؤلف الحقيقية `PRESENTATION_IMAGES/A01–A09` (962 عرضًا، مقصوصة على نافذة PowerShell) |
| `advanced/Parse-AmCache.py` | يطلب حزمة `python-registry` غير المثبتة وملف AmCache.hve ويندوز | لا لقطة |
| BrowsingHistoryView (NirSoft) | تطبيق ويندوز | لقطات المؤلف `PRESENTATION_IMAGES/C01–C10` |

## 3) الطمس (privacy) المطبَّق على لقطات المستودع

- اسم الجهاز `ABDUL1` واسم المستخدم `abdul_alrahman` طُمسا (Gaussian blur) في: A01, A04, A05, A08 — تحديد المواقع بـ Tesseract OCR ثم طمس صناديق الكلمات.
- مسارات `C:/Users/PC/...` طُمست في C07 (BHV results). 
- عنوان تقرير HTML الويندوزي يحمل اسم الأستاذ («د. عمر») → طُمس داخل الصفحة قبل اللقطة (حقن CSS blur على النص فقط) وكذلك `ABDUL1` في جدول معلومات الجهاز.
- README يذكر «Dr. Omar» في السطر الأول → طُمس في لقطة GitHub.
- لم تُستخدم إطلاقًا: B06 (حقل Examiner)، B09/B13 (مسارات `C:\Users\Fxu`، `C:\Users\student`)، C09 (مسارات Desktop)، D04 (صورة رسمية).
- **تبقى في بيانات المستودع نفسه** (ليست في تصاميمنا): `R1_SystemInfo.json` وCSV الأحداث و`report/index.html` تحمل ABDUL1/abdul_alrahman، وملفان مرجعيان من الأستاذ (`reference_materials_from_professor/*.docx|pptx`) → بند «تحديثات المصدر» عند محمد.

## 4) اللقطات المُسلَّمة (34 ملفًا في `screenshots/`)

- `repo-01..14-*.png` — 14 لقطة من أدلة المستودع بعد الطمس (Registry ×3، Event Log ×4، Timeline، Chain of Custody، FTK Verify، Autopsy ×2، Chrome History، BHV).
- `desktop-*.png` (1440×900 @2x) و`mobile-*.png` (390×844 @2x) لـ 6 صفحات: تقرير ويندوز HTML، تقرير المتصفح HTML، تقرير التشغيل المحلي (2026-09-23)، صفحة GitHub، ملف المحلل، قاعدة Sigma — مع نسخ `-full` كاملة الطول للديسكتوب وصفحتين للجوال.

## 5) تحقّق الروابط (2026-09-23)
- `https://github.com/moain2028/digital-forensics-lab` → 200
- One-liner في README يشير إلى `raw.githubusercontent.com/Moain2026/...` (الحساب القديم) → 200 (لا يزال يعمل)، ونسخة moain2028 → 200 أيضًا. يُستحسن تحديث README إلى الحساب الجديد.
- `/blob/main/LICENSE` → 404: README يقول «License: MIT» لكن لا ملف ترخيص في المستودع.
