royal-coffee-hospitality | مخطط التسويق | 2026-09-23 | v2

# SOURCES.md — مصدر كل نص ورقم وصورة في royal-coffee-hospitality-project-pack-v2

المشروع لم يكن في portfolio-hub؛ البند 0 أنتج `project/` (brief.ar/en.md · tech.md · links.md · screenshots/ 32 لقطة) — وهي المصدر الأساسي لكل ما يلي، مع README الكود في https://github.com/moain2028/royal-coffee-hospitality (commit 7a60aa4، 2026-08-21) وأمر `npm run build` بتاريخ 2026-09-23.

## A. النصوص والأرقام على التصاميم
| العنصر | المصدر |
|---|---|
| الاسم «القهوة الملكية / Royal Coffee» | README السطر 1 و4 |
| slug royal-coffee-hospitality | اسم المستودع |
| العنوان «موقع ضيافة سعودي فاخر يُصيَّر على الحافة بلا إطار عمل» | brief H1 ← README «الهدف» + «النشر: التقنيات… بلا React، بلا Tailwind» |
| السطر الوصفي (Hono وTypeScript على Cloudflare Workers — 73 صفحة من طبقة بيانات واحدة، Onyx + Gold، RTL أصيل) | README «معمارية البيانات» + sitemap (73) + «الهدف» |
| 52.6 KB Worker مضغوط | `npm run build` 2026-09-23: 179.65 kB / gzip 52.59 kB (README الجولة 5: 52.59) |
| 73 صفحة | `curl /sitemap.xml` من التشغيل المحلي: 73 `<loc>`؛ README الجولة 4 «كل الـ73 رابطاً» |
| 49 أيقونة SVG يدوية | `src/icons.tsx` عدّ `: S(` = 49 (README يقول 40+) |
| 0 مكتبة وقت التشغيل | `package.json` (dependency واحدة: hono، تُدمج في البناء) + README «مكتبات خارجية: صفر» |
| 17.7 KB CSS · 4.8 KB JS مضغوط | `gzip -c public/static/style.css` = 17,770 B · `app.js` = 4,780 B (مطابق README الجولة 5 §6) |
| 23 KB هيرو الجوال | README الجولة 5 §2 و§6 |
| 71 صنفاً · 8 تصنيفات · 10 مدن · 8 خدمات · 6 مناسبات | `src/data.ts` MENU/SERVICES/OCCASIONS · `src/cities.ts` CITIES (عدّ برمجي) |
| 13 بانياً JSON-LD | `src/ld.ts` (13 export) — README يقول 11 في جولة سابقة |
| 15 صفحة (الموقع الأصلي) | README «الأصل» |
| 95% جوال | DIAFA_ANALYSIS.md §8 «حرج — 95% موبايل» (تقدير المحلل في وثيقة المستودع؛ يُعرض كنسبة من الوثيقة لا كإحصاء سوقي) |
| تاجات: Hono · TypeScript · Cloudflare Workers · Vite 8 · CSS · JSON-LD | README «النشر: التقنيات» + package.json |
| شارة الشريحة: مشاريع صغيرة / Small business (#F4A62A) | تكليف مدير المنتج msg 4611462 + 02-brand |
| الفوتر github.com/moain2028/royal-coffee-hospitality | تكليف مدير المنتج (نسخة عامة) |
| wordmark «معين العباسي / Moain Al-Abbasi» (نسخ logo فقط) | project-pack-standard-v2 §A |
| نصوص الكاروسيل 1–5 والريل | brief + tech.md + README؛ copy.ar/en.md |
| بطاقة الرقم «0 مكتبة وقت التشغيل» | README «الأداء والكود النظيف: لا React، لا Tailwind وقت التشغيل، لا jQuery، لا خطوط أيقونات، لا إيموجي» |
| البانر «كيف تبني موقعاً فاخراً بـ 52 كيلوبايت» | عنوان مقال مقترح (زاوية 1 في research) من الأرقام أعلاه |

## B. الصور (كلها لقطات حقيقية من تشغيل محلي 2026-09-23، Playwright Chromium، DPR 2، reduced-motion)
| الاستخدام | الملف | ملاحظة |
|---|---|---|
| القطع الست، الكاروسيل 1، غلاف الريل، الريل 2 | desktop-01-home / mobile-01-home | الرئيسية |
| كاروسيل 2 | desktop-02-services | الخدمات |
| كاروسيل 3، الريل 3 | desktop-14-locations / mobile-14-locations | المدن |
| كاروسيل 4، الريل 4 | desktop-04-menu / mobile-04-menu | القائمة |
| كاروسيل 5، الريل 5 | mobile-07-contact | تواصل |
| البانر | desktop-01-home | |
| **بيانات داخل اللقطات** | `+966 50 000 0000` و`hello@example.com` تظهر في تواصل/الأزرار | placeholders معلنة في README ⚠️ — ليست بيانات حقيقية، فلم تُطمس؛ لم تُكرَّر كنص على أي تصميم |
| صور الموقع نفسه (دلال، بوفيه…) | داخل اللقطات | مولّدة أصلاً حسب README — تظهر فقط كجزء من اللقطة الحقيقية للموقع |
| أرقام الهيرو داخل الموقع (+6500 · +60 · 10 · 24/7) | داخل لقطة الرئيسية | محتوى الموقع؛ لم تُستخدم كنص على أي تصميم |
| الخلفيات/الشبكة/التوهج | مولّدة برمجياً (02-brand/scripts/brand.py) | لا صور مخزون، لا لقطة مولّدة بالذكاء الاصطناعي |

## C. الصوت
- الريلان: موسيقى آلية مولّدة (CassetteAI/music-generator، 24 ث، 2026-09-23) — نفس مقطع s-acm وhafawa لتوحيد صوت المحفظة؛ بلا حقوق طرف ثالث.

## D. ملفات البحث والنص
- `research.md`: كل ادعاء خارجي برابط وتاريخ وصول 2026-09-23؛ يتضمن تصحيح تموضع DIAFA_ANALYSIS (keif/osoul مشاريع معين).
- `explainer.ar/en.md`، `copy.ar/en.md`: كل جملة من brief/tech/README؛ draft حتى ختم المحرر.

## E. ما لم يُستخدم عمداً
- أرقام الهيرو والمراجعات (REVIEWS) — محتوى عرض.
- «أكثر من 70 صنفاً بصور حقيقية» و«صور حقيقية من مناسباتنا» (عناوين داخل الموقع) — الصور مولّدة حسب README؛ استُخدم «71 صنفاً» كعدد كيانات فقط.
- أرقام QA من README غير القابلة لإعادة التشغيل (73/73 SEO، 68/68 مسار، 0 مقصوص) — ذُكرت في brief/tech منسوبة لـ README، ولم توضع على أي تصميم.
- أي رقم هاتف أو بريد أو اسم شخص.
- keifaldiafa/asoulaldiafa كمنافسين.

## F. التباين
كما في hafawa (نفس الشريحة): Sand على Navy 13.4:1 · Mist 11.3:1 · Amber 7.2:1 · #A3B1C0 6.7:1 · Ink على شارة #F4A62A 8.9:1.

## G. التوليد
`make/packlib.py` + `make/build.py` (Pillow + raqm، خطوط 02-brand/fonts) · لقطات `make/shoot.py` (Playwright) · ريل ffmpeg.
