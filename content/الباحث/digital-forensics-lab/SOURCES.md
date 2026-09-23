digital-forensics-lab | الباحث | 2026-09-23 | v2 — G (مصادر كل نص ورقم وصورة)

# SOURCES — digital-forensics-lab project pack v2

المستودع: https://github.com/moain2028/digital-forensics-lab (فُحص 2026-09-23، HTTP 200) · commit الأحدث 2026-09-14 · مستنسخ محليًا 2026-09-23.
ملفات المرجع: `01-projects/digital-forensics-lab/{tech.md, brief.ar.md, brief.en.md, links.md, RUN-NOTES.md}` (مضمّنة في `project/`).

## 1) الأرقام
| الرقم كما يظهر | المصدر | طريقة التحقق |
|---|---|---|
| 5 مواضيع | README.md سطر 3–4 | قراءة |
| 19 سجل تصفح | تشغيل محلي 2026-09-23 لـ `scripts/browser_history_parser.py` → `[+] Records recovered: 19`؛ يطابق `reports/parser_console_output.txt` و`docs/METHODOLOGY.md` | أمر |
| MD5 `1fc18eb1…` / SHA-256 `456a181c…` مطابقتان | `md5sum`/`sha256sum evidence-info/History_EVIDENCE.db` = README §3 | أمر |
| Integrity re-check: PASSED | مخرجات التشغيل المحلي + `reports/parser_console_output.txt` | أمر |
| 15 محاولة دخول فاشلة (Event 4625) | `windows-forensics/evidence/data/E2_Failed_Logons.csv` (15 سجلًا بعد الرأس) + لقطة A05 | `python csv` عدّ |
| 127.0.0.1 · 8 أيام (5/9 → 13/9) | E2_Failed_Logons.csv الأعمدة TimeCreated/Message؛ لقطة A05 | قراءة |
| 7 أجهزة USB | `R2_USB_Devices.csv` (7 صفوف) + لقطة A02 | عدّ |
| 7 ملفات مبصومة (Chain of Custody) | `windows-forensics/evidence/report/chain_of_custody.csv` | عدّ |
| 3 قواعد Sigma | `ls windows-forensics/sigma_rules/*.yml` | أمر |
| 16 تقنية MITRE ATT&CK | `grep -o "T1[0-9]{3,4}(\.[0-9]{3})?"` على *.ps1/*.yml/*.py → 16 معرّفًا فريدًا | أمر |
| T1110 (Brute Force) | `windows-forensics/advanced/Detect-USBBrutforce-Chain.ps1` و`Run-Windows-Forensics.ps1` | grep |
| T1078 / T1091 على صفوف Timeline | `Run-Windows-Forensics.ps1` سطر 202/205 | قراءة |
| 4624 / 4625 / 1102 / 6005 / 6006 | `windows-forensics/README.md` §Event Log؛ `Run-Windows-Forensics.ps1` | قراءة |
| Autopsy 4.21.0 · Sleuth Kit 4.12.1 · FTK Imager 4.7 · PowerShell 5 · Python 3 | README.md سطر 7–8؛ `windows-forensics/README.md`؛ لقطات A* تُظهر «Windows PowerShell (x86)» | قراءة |
| `nps-2009-canon2-gen6.E01` · 31,129,600 بايت · MD5 `750b509d…` · FAT12 · `_MG_0025.JPG` محذوف | README §4 + METHODOLOGY.md (غير مُعاد هنا — الصورة غير مضمّنة) | قراءة |
| 25 شريحة · 9 سكربتات · 1,640 سطر · 122 ملف · 7 commits · 23 MB | tech.md (أوامر grep/wc/find/git log/du) | أمر |

**مستبعَد عمدًا:** «~5 دقائق»، «10 دقائق»، «الأول على الدفعة»، أي وقت تنفيذ، أي نسب أكاديمي أو اسم شخص/مؤسسة.

## 2) النصوص
- العناوين والتاغلاين في A/B/C: مشتقة من brief.ar/en.md وtech.md (المشكلة/الحل/الأرقام).
- كاروسيل 1/5 «المشكلة»: brief §المشكلة. 2/5 «الحل»: brief §الحل + README §2/§6. 3/5 «كيف يعمل»: E2_Failed_Logons.csv + Run-Windows-Forensics.ps1 (Timeline/CoC). 4/5 «الأرقام»: tech.md. 5/5 «لمن»: brief §لمن يفيد.
- Explainer (D): README §3–§6، `docs/METHODOLOGY.md`، `windows-forensics/README.md`، `sigma_rules/*.yml` (العناوين الثلاثة)، التشغيل المحلي.
- Research (E): روابط في `digital-forensics-lab-research.md`، فُحصت 2026-09-23 (HTTP 200)؛ الاقتباسات حرفية من الصفحات؛ سعر CyberDefenders Pro من مصدر ثالث (dfirdiva.com، 2025-03-10) — مُعلَن كذلك.
- Copy (F): كل رقم من الجدول أعلاه؛ X ≤ 280 حرفًا (229 AR / 244 EN).

## 3) الصور
| الاستخدام | الملف الأصلي في المستودع | المعالجة |
|---|---|---|
| البطل/LinkedIn/X/IG/Story/Hero — لقطة رئيسية | `windows-forensics/evidence/report/index.html` (رُندر بـ Playwright 1440×900 @2x، قصّ بطاقة Timeline) | طمس اسم الأستاذ في العنوان واسم الجهاز (JS قبل اللقطة) |
| ثانوية — Event 4625 | `PRESENTATION_IMAGES/A05_…_EventLog_4625_BruteForce.png` | OCR (tesseract) + Gaussian blur لعمود User (30 صندوقًا)؛ قصّ رأس PowerShell المشوّه (ترميز) في قصاصة التصميم فقط |
| ثالثة — Chain of Custody | `report/index.html` بطاقة CoC (رندر Playwright) | — |
| Story/كاروسيل 5 — USBSTOR | `PRESENTATION_IMAGES/A02_…_Registry_USBSTOR_USB_Devices_Serials.png` | قصّ الرأس المشوّه؛ لا بيانات شخصية |
| كاروسيل 1 / ريل 2 — Chrome History | `PRESENTATION_IMAGES/E01_Chrome_History_FullList_Dates.png` | بلا تعديل (ملف مختبر نظيف، README §7) |
| number-card | لا صورة | — |
| article-banner | لقطة Timeline | — |
| screenshots/ (34) | 14 من PRESENTATION_IMAGES بعد الطمس + 20 Playwright (تقريران HTML، تشغيل محلي، GitHub ×3) | الطمس موثّق في RUN-NOTES §3 |

**لم تُستخدم:** D04 (صورة رسمية من sleuthkit.org لا من تنفيذ المؤلف)، B06 (حقل Examiner)، B09/B13/C09/C10 (مسارات `C:\Users\…`/Desktop)، `reference_materials_from_professor/*`.

**لا صور ولا أيقونات مولّدة بالذكاء الاصطناعي** في هذه الحزمة — كل الصور لقطات حقيقية من المستودع أو رندر لملفاته.

## 4) الهوية والمعيار
- `02-brand/scripts/brand.py` (الألوان/الخطوط IBM Plex Sans Arabic · Inter · JetBrains Mono)؛ النص الخافت #A3B1C0 (معيار v2)؛ شريحة «طلاب» بنفسجي.
- معيار الحزمة: `project-pack-standard-v2.md` (مرفق مهمة #33).
- أدوات الإنتاج: `tools/` في الحزمة (make_pack.py، make_carousel.py، make_reel.py، redact.py، shots_web.py، spec.json).

## 5) الريل
- 6 مشاهد × (4/5/5/5/5/4 ث) − 5 × 0.5 ث تداخل = 25.5 ث؛ 1080×1920؛ 30fps؛ H.264؛ بلا موسيقى (تُضاف عند النشر — لا مصدر خالٍ من الحقوق محليًا)؛ بلا إطار هاتف (المشروع بلا واجهة جوال)؛ لا مشاهد خطأ.
