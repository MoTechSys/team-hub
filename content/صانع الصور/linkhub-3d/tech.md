linkhub-3d | صانع الصور | 2026-09-23 | ready

# LinkHub 3D — Technical Sheet

- **Repo:** moain2028/linkhub-3d (public) · 1 commit فقط (2026-08-21)
- **Primary language / stack:** HTML5 + CSS3 + Vanilla JavaScript في ملف واحد لكل علامة (`keif/index.html` 419 سطراً، `asoul/index.html` 337) — **بلا إطار، بلا build، صفر طلبات خارجية** (الخطوط woff2 محلية، الأيقونات SVG inline، الصور `<picture>` AVIF/WebP/JPG محلية) · سكربتات قياس Python (contrast، gates، cdp) · QR ECC-H · docs/SPEC (المصدر: README، `git ls-files`، فحص الشبكة المحلي)
- **Problem:** صفحات link-in-bio التجارية (Linktree وأشباهها) قوائم مسطّحة موحّدة الشكل، تُحمّل سكربتات طرف ثالث، وتُعامل العربية كترجمة؛ العلامات الفاخرة تريد صفحة روابط بشعور «الدكة» — بطاقة مادية تنقلب في الفضاء وتُصبغ الصفحة بلون المنصة قبل الانتقال. (docs/00-INDEX «الطلب»، README)
- **Solution / core features:** شاشة واحدة بلا تمرير (844=844 مقيس) بـ 8 بطاقات (كيف) / 6 (أصول)، كل بطاقة `<a href>` حقيقي يعمل بلا JS. عند الضغط: انقلاب 3D حقيقي `rotateY(180deg)` بـ `perspective` + `preserve-3d` + `backface-visibility` (مقيس: `matrix3d(-1,0,0,0, 0,1,0,0, 0,0,-1,0, …)`)، حلقة تقدّم SVG `stroke-dashoffset` تكتمل في 900ms، تحوّل الصفحة كاملة إلى هوية المنصة (خلفية body من `rgb(10,8,7)` إلى `rgb(21,2,7)` لإنستقرام — مقيس)، ثم الانتقال؛ الإلغاء بضغطة ثانية أو Escape أو مغادرة المؤشر. الخامة: سُمك هندسي `translateZ(±3.5px)` (كيف) / لوح 10px بشرائح حرف (أصول)، لمعة specular تتبع المؤشر بلا rAF، حبيبات `feTurbulence`، بئر أيقونة محفور، ميل ±4°. (README «التفاعل»، «الخامة»، linkhub-audit.json)
- **Architecture notes:** كل صفحة ملف HTML واحد يحمل CSS وJS مضمّنَين؛ الثيمات كتل `[data-theme=<platform>]` على `<html>` (كيف) أو قاموس JS يضبط متغيّرات CSS (`--ink/--surface/--accent…`) على الجذر (أصول). المحتوى والروابط مصدرها `docs/data.json` ومضمّنة حرفياً في HTML ليعمل بلا JS؛ سكربت `verify_hrefs.py` يطابق 8/8 و6/6. `prefers-reduced-motion` يعطّل الانقلاب والميل واللمعة وينتقل فوراً. لونان صُحّحا لفشل التباين (`phone` كان 1.09:1، `snapchat` 1.27:1) وتوثيقهما في docs/02. JSON-LD LocalBusiness في كل صفحة. (index.html، docs/02-TECH-FACTS، README «المبادئ»)
- **Status:** production-ready كملفات ثابتة، لكن الرابطان الحيّان لا يستجيبان (2026-09-23) والنطاق موصوف في README نفسه بـ «مؤقت (VM)»؛ docs/03 يعلّق قرارات النطاق النهائي والحسابات الناقصة على المالك.
- **Last commit:** 2026-08-21 (`git log -1`) — المستودع commit واحد
- **Live URL:** none — README/docs يذكران `suppdizl.gensparkclaw.com/lnk/keif/` و`/lnk/asoul/` لكنهما **لا يستجيبان** (curl 2026-09-23؛ أكّده مدير المنتج في اليوم نفسه)

## الأرقام ومصادرها / Numbers & sources
(قياس 2026-09-23 على نسخة مستنسخة مخدومة محلياً بـ `python3 -m http.server`، Chromium headless عبر Playwright — `scripts/shoot.py audit` → `screenshots/linkhub-audit.json`)
| Metric | كيف | أصول | Source |
|---|---|---|---|
| `index.html` خام | 29,613 B (29.6 KB) | 26,428 B (26.4 KB) | `wc -c` — يطابق README (29.6/26.4) |
| gzip -9 | **8,448 B (8.4 KB)** | **7,961 B (8.0 KB)** | `gzip -9 -c \| wc -c` — يطابق README |
| طلبات خارجية | **0** | **0** | Playwright: كل الطلبات (6 / 7) من الأصل المحلي؛ `schema.org` في JSON-LD نص لا طلب |
| إجمالي الطلبات عند التحميل | 6 | 7 | Playwright request log |
| أخطاء الكونسول | 0 | 0 | Playwright console/pageerror |
| بطاقات (`a.card`) / منها بـ href حقيقي | 8 / 8 | 6 / 6 | DOM count — يطابق README «يعمل بلا JS» |
| شاشة واحدة (390×844) | scrollHeight 844 = viewport 844 | نفسها | DOM measure — يطابق README |
| أصغر مساحة لمس | 68 px | 78 px | `getBoundingClientRect` — يطابق README |
| أصغر خط | 14 px | 14 px | computed fontSize — يطابق README |
| طبقات `backgroundImage` على `.face` | **15** | 17 | computed style split — README يذكر 15 لكيف فقط |
| طبقات `boxShadow` على `.face` | 5 | 5 | computed style — يطابق README |
| `backdrop-filter` | 0 | 0 | computed style scan — يطابق README |
| حلقة rAF دائمة | 0 | 1 مرة تنتهي (لا حلقة) | `grep requestAnimationFrame` — يطابق docs/02 |
| الانقلاب 3D عند 180° | `matrix3d(-1,0,0,0, 0,1,0,0, 0,0,-1,0, 0,0,0,1)` | نفسه | computed transform بعد النقر — يطابق docs/02 |
| `transform-style: preserve-3d` | 2 في الكود · 1 عنصر مفعّل في البطاقة | 4 · 1 | `grep` + computed |
| تحوّل الثيم (إنستقرام) | `<html data-theme="instagram">` · body bg `rgb(10,8,7)` → `rgb(21,2,7)` | `body.themed` · `rgb(4,16,14)` → `rgb(21,2,7)` | computed style قبل/بعد النقر |
| الحلقة أثناء الشحن | `stroke-dashoffset` 100.5px (من 339.3 → 0 خلال 900ms) | 119.38px | computed style لحظة الالتقاط |
| الاستعادة بعد Escape | `data-theme` = null · class "" | class "" | computed بعد Escape |
| فحوص التباين WCAG | ALL PASS (أدناه 4.64:1) — 8 ثيمات × 5 أزواج | ALL PASS — 7 ثيمات | `python3 keif/contrast-v2.py` · `asoul/contrast.py` (تشغيل محلي) |
| ثيمات المنصات في data.json | 11 | — | docs/data.json platforms |
| صور | 20 ملف · 1,552 KB (AVIF/WebP/JPG بـ 3 مقاسات × ديسكتوب/جوال + macro + og) | 10 · 872 KB | `ls`, `du -sk` |
| خطوط محلية | 3 woff2 · 52 KB (Amiri 700 عربي · Kufi 400/700) | نفسها | `<brand>/font`, 3 `@font-face` |
| ملفات المستودع | 76 | | `git ls-files` |
| الالتزامات | **1** (2026-08-21) | | `git log` |
| صفوف/منصات | واتساب · اتصال · إنستقرام · تيك توك · X · تيليجرام · فيسبوك · خريطة | واتساب · اتصال · إنستقرام · تيك توك · سناب · خريطة | index.html |
| Lighthouse | يُستكمل — غير متاح في البيئة؛ استُبدل بفحص Playwright الموثّق أعلاه | | linkhub-audit.json |

## ملاحظات التنظيف / Cleanup notes
- الرابطان الحيّان ميتان، وcanonical/og:url/JSON-LD في الصفحتَين تشير إليهما — تُحدَّث عند النقل إلى النطاق النهائي (docs/03 يطرح السؤال على المالك).
- رقمَا الواتساب/الهاتف للعلامتَين مكتوبان صريحاً في HTML (ظاهران في البطاقات وaria-label وJSON-LD `telephone`) وفي docs/data.json — طُمسا في كل لقطة وفيديو هنا، ولا يظهران في أي تصميم أو نص.
- حسابات السوشيال (handles) ظاهرة في البطاقات — بقيت في اللقطات لأنها هويات علنية للعلامتَين، لكن لا تُذكر في نصوص الحزمة (المشروع يُقدَّم كنمط تقني).
- README يقول «15 طبقة backgroundImage» — صحيح لكيف؛ أصول 17 طبقة (لم يُذكر).
- README يقول شاشة واحدة عند 932 و900 أيضاً — قِست 844 فقط.
- commit واحد فقط — لا تاريخ تطوير؛ التقارير REPORT-V1/V2 داخل المستودع تحمل الطابع الزمني بديلاً.
- docs/03-NEXT-TASK يذكر توكن GitHub «كُشف في الشات سابقاً» وأسماء مستودعات خاصة أخرى — لا يُنقل شيء منه؛ يُنبَّه المالك إلى تنظيف الوثيقة.
- الشعارات داخل الصفحتَين (شعار كيف/أصول) من أصول العلامتَين (`logo-512.webp`، SVG data-URI) — ليست مولّدة هنا؛ صور الهيرو من `assetsFrom` بطاقات VIP السابقة، أصلها غير موثّق في المستودع → يُفصَح بأنها «من أصول العلامة، مصدرها غير موثّق».
- docs/00-INDEX يذكر `src/` غير موجود في المستودع (المصدر داخل keif/ وasoul/ مباشرة).

## اللقطات والفيديو
`screenshots/` — 18 لقطة حقيقية 2x من التشغيل المحلي: لكل علامة قاعدة ديسكتوب 1440×900 + ميل hover + قاعدة جوال 390×844 (الصفحة شاشة واحدة فلقطة full-page تطابق القاعدة وحُذفت من الحزمة لتوفير الحجم)، و3 منصات × (منتصف الانقلاب + منقلبة بثيم كامل) على الجوال + الاستعادة بعد Escape. `linkhub-audit.json` يوثّق القياسات. `video/interaction-{keif,asoul}-390x844.mp4` (≈13.8 ث لكل منهما) تسجيل Playwright فعلي: نقر → انقلاب 3D + حلقة + تحوّل الثيم → Escape → استعادة، لثلاث منصات. الانتقال الخارجي محجوب أثناء التسجيل (route abort) وأرقام الهاتف مطموسة قبل الالتقاط.
