keif-aldiafa-mobile-ui | متخصص SEO | 2026-09-23 | v2

# SOURCES — مصدر كل نص ورقم وصورة في keif-aldiafa-mobile-ui-project-pack-v2

المرجع: https://github.com/moain2028/keif-aldiafa-mobile-ui (commitان 2026-08-08) — README.md · index.html · styles.css · app.js — و`0-project/tech.md` + `0-project/tools/measure.json` (قياسي المستقل 2026-09-23) و`02-brand/README.md` في portfolio-hub (هوية معين العباسي للتصاميم).

## الصور (كلها لقطات حقيقية من تشغيل محلي للمستودع — لا لقطة مولّدة)
> إفصاح إلزامي: **الصور السبع داخل الواجهة مولّدة بالذكاء الاصطناعي** (README «7 صور مولّدة أصلياً (nano-banana-pro)»؛ commit b039e58 «الأصول المستخدمة كلها مولّدة»): `assets/opt/hero.jpg` · `cat-coffee/sweets/service/events.jpg` · `dallah-solo.jpg` · `texture-pattern.jpg`. تظهر في اللقطات بوصفها جزءاً من الواجهة الحقيقية. سطر إفصاح على كل شريحة كاروسيل ومشهد ريل يحمل لقطة (كاروسيل 2، 3، 5 · ريل 1، 3، 4، 6)، وفي الشرح؛ لا على البطل (A).

| الاستخدام | الملف في `0-project/screenshots/` | ملاحظة |
|---|---|---|
| البطل (A لاندسكيب: هاتفان) | `mobile-01-hero.png` 780×1688 + `mobile-04-services.png` | جوال 390×844 @2x |
| البطل (A عمودي: متصفح + هاتف) · B بانر · C مشهد 6 | `desktop-01-frame-hero.png` 2880×1800 + `mobile-01-hero.png` | ديسكتوب 1440×900: إطار الجهاز كما يعرضه الموقع > 520px |
| B كاروسيل 2 / C مشهد 1 | `mobile-01-hero.png` · `mobile-02-tiles.png` | |
| B كاروسيل 3 / C مشهد 3 | `mobile-04-services.png` · `mobile-07-drawer.png` | القائمة الجانبية مفتوحة (جوال — تعمل صحيحاً) |
| B كاروسيل 1 (خافتة) / C مشهد 2 | `desktop-02-frame-tiles.png` | |
| C مشهد 4 | `desktop-03-frame-services.png` | |
| أرشيف (غير مستخدمة) | `mobile-03/05/06/08/09-*.png` · `desktop-04/05-*.png` | `desktop-05-frame-drawer` يُظهر عيب القائمة خارج الإطار — أرشيف فقط |
| طمس | — | لا شيء يحتاج طمساً على الشاشة: زر واتساب رقم نائب في `href` فقط (لا يظهر نصاً)؛ لا اسم شخص |
| الأداة | `tools/shoot.py` · `tools/measure.json` · `tools/make_pack_kam.py` · `tools/make_extras.py` · `tools/make_reel.py` | Playwright/Chromium 2x + القياسات؛ التوليد يبني على `02-brand/scripts/brand.py` |

## النصوص والأرقام — كلها من قياسي 2026-09-23 (لا من README إلا حيث يُذكر للمطابقة)
| العنصر | AR / EN | المصدر |
|---|---|---|
| H1 | «واجهة جوال فاخرة بلا إطار — تباين مقيس لا تقديري» / “A premium mobile UI with no framework — contrast measured, not eyeballed” | brief.ar/en.md ← README العنوان + «تباين مقيس (WCAG AA)» |
| اسم المشروع | واجهة كيف الضيافة / Keif Al-Diafa UI · keif-aldiafa-mobile-ui | README؛ يُقدَّم كنمط تقني (تكليف مدير المنتج msg 4615580) |
| السطر التعريفي | «صفحة واحدة HTML/CSS/JS خام، RTL كامل، لوحة ألوان بـ21 متغيّراً، وزر واتساب عائم يختفي أثناء التمرير — كل نص فُحص تباينه بـgetComputedStyle.» / EN | brief «الحل» ← README «المواصفات» · `styles.css :root` (21 متغيّراً) · `app.js` |
| 31.2 KB — كود كامل · 9.7 KB مضغوطاً | `wc -c index.html styles.css app.js` = 11,820+17,479+1,913 = 31,212 B · `gzip -c \| wc -c` = 3,398+5,514+820 = 9,732 B (README 11.8/17.5/1.9 KB — مطابق) |
| 15/15 — نصّاً فوق 4.5:1 | `measure.json` contrast_mobile: 15 عنصراً مقيساً بـgetComputedStyle + صيغة WCAG relative luminance؛ الأدنى foot_tag 5.00 · الأعلى 15.89 (README: 11 عنصراً — الثمانية المُسمّاة مطابقة؛ tab_txt 7.45 لا 5.00) |
| 0 px — تداخل الزر العائم مع الشريط | `measure.json` fab_mobile / fab_desktop / fab_mobile_scrolled: `getBoundingClientRect` overlap = 0 (فجوة 6–7 px) |
| 232 ms — LCP محلي | `measure.json` perf_mobile.lcp_ms — **ليس على أي تصميم** (قرار مدير المنتج msg 4616156: رقم أداء محلي يُقرأ كادعاء عام)؛ يبقى في tech.md وresearch بشروطه |
| 20 — طلباً في التحميل الأول (A البطاقة 4، B، C) | `measure.json` requests.total = 20 (9 محلية + 11 Google Fonts) |
| 7 — صور · 590 KB (B، C) | `ls assets/opt \| wc -l` = 7 · `du -b assets/opt/*` = 603,565 B |
| 21 — متغيّر CSS · 5 نقاط ذهب (B، C) | `grep -oE '^\s*--[a-z0-9-]+:' styles.css \| sort -u \| wc -l` = 21 · `--g1..--g5` |
| 3 ملفات · 7 صور · 590 KB (D) | `git ls-files` · `du -b assets/opt/*` = 603,565 B |
| الشريحة «مشاريع صغيرة» | تكليف مدير المنتج؛ لون الشريحة #F4A62A من `02-brand/README.md` |
| الدعوة | «أُصمّم واجهة جوالك الفاخرة بتباين مقيس — راسلني.» / “I design premium mobile UIs with measured contrast — DM me.” | brief «للتواصل» — صيغة «راسلني/DM me» للأساس بلا شعار |
| التذييل | github.com/moain2028/keif-aldiafa-mobile-ui | تكليف مدير المنتج؛ الرابط يعمل (200) 2026-09-23 |
| النص الخافت | #A3B1C0 | معيار v2 |
| Wordmark (نسخة logo فقط) | «معين العباسي» / “Moain Al-Abbasi” | قاعدة الشعار 2026-09-23: نص فقط بلا علامة |

## ما لم يُستخدم عمداً
- أرقام شريط الثقة في الواجهة (+٥٠٠ مناسبة · ٤.٩ · ٣ مدن) — نص ثابت بلا مصدر؛ تظهر داخل اللقطات فقط.
- رقم واتساب `wa.me/966500000000` — نائب في href؛ لا يُكتب.
- أرقام README غير المُعاد قياسها (600KB أصول، «13.99MB → 589KB وفر 95.9%») — لم أقس الأصل قبل التحسين فلم أستخدم نسبة الوفر.
- Lighthouse — غير متاح في البيئة؛ لم يُذكر رقم.
- لقطات المؤلف `shots/v8-*.png` — لا تُستخدم.
- أي مقارنة بمشاريع «كيف الضيافة» الأخرى على المنصة — مستبعدة بتكليف مدير المنتج.

## الخطوط والموسيقى
- IBM Plex Sans Arabic (AR) · Inter (EN) · JetBrains Mono (الروابط/الوسوم) — من `02-brand/scripts/brand.py`. (خطوط الواجهة نفسها Almarai + Amiri تظهر داخل اللقطات.)
- الريل: `02-brand/scripts/reels/bgm-tech-minimal.mp3` (داخلية)؛ لا تعليق صوتي.

## البحث (E)
روابط مؤرَّخة 2026-09-23 في `keif-aldiafa-mobile-ui-research.md` §7: framer.com/pricing + goodspeed.studio (2026-05-28)، tailwindcss.com/plus + toolradar.com، figma.com/community + elements.envato.com، animaapp.com/pricing.
