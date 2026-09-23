almutahassil-site | متخصص SEO | 2026-09-23 | v2

# SOURCES — مصدر كل نص ورقم وصورة في almutahassil-site-project-pack-v2

المرجع: https://github.com/moain2028/almutahassil-site (commitان 2026-08-11) — README.md · brand/BRAND.md · docs/00-INDEX.md · ملفات HTML/CSS/JS — و`0-project/tech.md` (تحقق محلي 2026-09-23) و`02-brand/README.md` في portfolio-hub (هوية معين العباسي للتصاميم).

## الصور (كلها لقطات حقيقية من تشغيل محلي للمستودع — أُخذت بـPlaywright/Chromium 2x)
| الاستخدام | الملف في `0-project/screenshots/` | ملاحظة |
|---|---|---|
| البطل (A كلها، B بانر، C مشهد 1) | `desktop-01-home.png` 2880×1800 + `mobile-01-home.png` 780×1688 | `index.html` عبر `python3 -m http.server` |
| B كاروسيل 3 / C مشهد 6 | `desktop-08-demo-kpis.png` | `demo.html` بعد التمرير إلى بطاقات KPI والرسم — بيانات عرض مُعلَنة في الصفحة |
| B كاروسيل 1 (خافتة) / C مشهد 2 | `desktop-05-about.png` | صفحة «عن النظام» |
| C مشهد 3 | `desktop-03-features.png` | صفحة الوحدات |
| B كاروسيل 5 / C مشهد 4 | `mobile-06-demo-kpis.png` · `mobile-07-home-modules.png` | لوحة الـdemo وشبكة الوحدات على الجوال |
| أرشيف (غير مستخدمة في التصاميم) | `desktop-02/04/06/07/09/10/11-*.png` · `mobile-02..05-*.png` | demo أعلى الصفحة، FAQ، contact، changelog، شبكة الوحدات، آلية العمل، سؤال مفتوح |
| **الأيقونات داخل اللقطات** | — | الأيقونات العشر في الموقع **مولّدة بالذكاء الاصطناعي** بإقرار README («مسار جودة الأيقونات»)؛ تظهر في اللقطات بوصفها جزءاً من الموقع الحقيقي، ولا تُقدَّم كتصوير. سطر إفصاح صغير على شرائح الكاروسيل التي تحمل لقطات (2، 3، 5) فقط — لا على البطل (قرار مدير المنتج 2026-09-23) |
| طمس | كل اللقطات | اسم الجهة الشخصي (شريط التنقل، مجسّم الهاتف، التذييل، الخط الزمني، جدول الإنتاجية) والهاتف/البريد النموذجيان في `contact.html` — blur 6px عبر `tools/shoot.py` |
| الأداة | `tools/shoot.py` · `tools/make_pack_mut.py` · `tools/make_extras.py` · `tools/make_reel.py` | التصوير والتوليد؛ تبني على `02-brand/scripts/brand.py` |

## النصوص والأرقام
| العنصر | AR / EN | المصدر |
|---|---|---|
| H1 | «موقع تعريفي ولوحة تجريبية لنظام تحصيل وسداد ذكي» / “Marketing site and demo dashboard for a smart collection system” | brief.ar/en.md ← README عنوان المستودع «موقع نظام التحصيل والسداد الذكي» + «Landing + لوحة تجريبية» |
| اسم المشروع | المتحصل / Al-Mutahassil · almutahassil-site | README · BRAND.md (اللاتينية “Al-Mutahassil” للمواد الإنجليزية فقط؛ BRAND.md يمنعها في الواجهات العربية) |
| السطر التعريفي | «8 صفحات HTML/CSS/JS خام بلا build ولا تبعيات — عربي RTL كامل بأرقام هندية، 10 أيقونات 3D بأسلوب واحد، ولوحة إدارة تجريبية ببطاقات KPI وجداول قابلة للفرز.» / EN | brief «الحل» ← README «المواصفات» (بلا إطار/بلا build/بلا CDN JS، RTL، أرقام هندية، 10 أيقونات) · `demo.js` (KPI، فرز) |
| 8 — صفحات HTML | `ls *.html \| grep -v nav-snippet \| wc -l` (tech.md) |
| 0 — تبعيات · بلا build | README «المواصفات»؛ لا package.json؛ `grep -h '<script[^>]*src' *.html` → app.js، demo.js فقط |
| 10 → 20 — أيقونات 3D → WebP | `ls icons/*.png \| wc -l` = 10 · `ls icons/opt/*.webp \| wc -l` = 20 |
| 180 — سمة aria | `grep -ohE 'aria-[a-z]+=' *.html \| wc -l` |
| 9 — وحدات (B، C) | `grep -c '<article class="mod' features.html` = 9 · `app.js` FEATURES = 9 (index يقول «عشر» — المعتمد الكود) |
| 12 — سؤالاً شائعاً (B، C) | `grep -oE 'class="faq-item' faq.html \| wc -l` |
| 22.8 KB · 14 متغيّراً (B، C) | `wc -c style.css` = 22,783 · `grep -oE '^\s*--[a-z0-9-]+:' style.css \| sort -u \| wc -l` = 14 |
| 5 — إصدارات (D) | `grep -c '<article class="rel' changelog.html` |
| 7 أقسام · 4 خطوات · 6 حقول · 4 محطات (D) | README «البنية» · `index.html` `#how` · `contact.html` name= · `about.html` tl-item |
| الشريحة «شركات» | مهمة مدير المنتج (msg 4613772) · لون الشريحة #3B82F6 من `02-brand/README.md` |
| الدعوة | «أُصمّم موقعك التعريفي ولوحته التجريبية بهوية كاملة — راسلني.» / “I build marketing sites with a demo dashboard and full brand system — DM or email.” | brief «للتواصل» — صيغة شريحة الشركات في دليل التحرير |
| التذييل | github.com/moain2028/almutahassil-site | مهمة مدير المنتج؛ الرابط يعمل (200) 2026-09-23 |
| النص الخافت | #A3B1C0 | معيار v2 (تحديث الهوية) |
| Wordmark (نسخة logo فقط) | «معين العباسي» / “Moain Al-Abbasi” | قاعدة الشعار 2026-09-23: نص فقط بلا علامة |

## ما لم يُستخدم عمداً
- عدّادات الرئيسية (99.9% · 4ث · 100%) وأرقام لوحة الـdemo (4,820,500 ر.ي · 148 سند …) وادعاءات changelog (4.2→1.1 ث · 68% · 72 ساعة) — بيانات عرض/تسويق غير قابلة للتحقق من الكود؛ تظهر داخل اللقطات فقط بوصفها محتوى الموقع.
- اسم الشخص الكامل كاسم الجهة — مطموس ولا يُكتب؛ الوصف المعتمد «صندوق تحصيل متعدد الفروع».
- الهاتف والبريد والعنوان في `contact.html` — مطموسة.
- الرابط «المباشر» في README — معطّل؛ لا يُكتب.
- شعار «المتحصل» (`brand/logo.svg`) — يظهر داخل اللقطات كجزء من الموقع؛ لا يُستخدم كعلامة على التصاميم (الأساس بلا شعار).

## الخطوط والموسيقى
- IBM Plex Sans Arabic (AR) · Inter (EN) · JetBrains Mono (الروابط/الوسوم) — من `02-brand/scripts/brand.py`.
- الريل: `02-brand/scripts/reels/bgm-tech-minimal.mp3` (داخلية)؛ لا تعليق صوتي.

## البحث (E)
روابط مؤرَّخة 2026-09-23 في `almutahassil-site-research.md` §7: cobrapp.co (صفحتا المنتج والأسعار)، aksat-ms.com، sanadims.site، credgenics.com، ecolor.com.sa، dhman.io.
