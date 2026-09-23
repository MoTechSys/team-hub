dallat-alkaif-static | المحرر | 2026-09-23 | final

# SOURCES — dallat-alkaif-static project pack v2

## النصوص
| النص | المصدر |
|---|---|
| «نفس الهوية بلا أي إطار» / "The same brand with no framework at all" | brief.ar/en.md (المحرر) ← README §ملاحظة (التوأم) + §لماذا بلا إطار |
| 13 صفحة · HTML/CSS/JS خام · بلا build · 0 تبعية · أي استضافة | README §نظرة عامة + §لماذا بلا إطار؛ تحقّق: `ls *.html \| wc -l`، لا package.json |
| حجز → واتساب · Open Graph في كل صفحة · بلا قفل تكبير | booking.html (script: location.href='https://wa.me/…?text=') · grep og: (7×13) · grep maximum-scale = 0 |
| تنسيق الرئيسية مضمَّن / sv.css للبقية | README §البنية + index.html `<style>` · 12 صفحة تربط sv.css |
| 82 سطر JavaScript في صفحتين | `sed -n '/<script>/,/<\/script>/p' index.html booking.html \| wc -l` = 38 + 44 |
| الثمن: تكرار يدوي، لا مكوّنات، لا فحص أنواع، تخطيط 480px | README §لماذا بلا إطار (جدول المقابل) + §الاستجابة |
| «الخلاصة الصادقة: لـ 13 صفحة ثابتة سليم؛ عند الديناميكي Next.js» | README §لماذا بلا إطار (اقتباس شبه حرفي) |
| قواعد المحتوى (لا مدن خارج النطاق، لا إحصائيات، لا أسعار، لا شعارات) | README §قواعد المحتوى |
| «الصور مولَّدة بالذكاء الاصطناعي» | README §ما زال مطلوباً |
| لا رابط حي | og:url في الصفحات → toalgzwc.gensparkclaw.com/keif/ ؛ curl 2026-09-23 = 000 |
| الدعوة «موقعك 13 صفحة ويحمل إطاراً كاملاً؟ راسلني» | brief (المحرر) — شريحة مشاريع صغيرة |
| البحث E — اقتباسات البدائل | عناوين/أوصاف wix.com · astro.build · gohugo.io · pages.github.com · netlify.com (curl 2026-09-23)؛ النجوم من api.github.com |

## الأرقام (كلها على التصاميم أو في النصوص)
| الرقم | المصدر وشروط القياس |
|---|---|
| 13 صفحة | `ls *.html \| wc -l`؛ شارة README |
| 0 تبعية | لا package.json/node_modules؛ شارة README |
| 8 طلبات · 558 KB (الرئيسية static) / 47 · 1.5 MB (next) | work/dallat/measure3.js: puppeteer-core + chrome 154، خادم python http.server محلي لكل نسخة، `setCacheEnabled(false)`، viewport 390×844 @2x، `networkidle0`، Google Fonts محجوبة للثابت؛ next مبني بـ `next build` (16.3.0) ويُخدَم تحت /dallat؛ 2026-09-23، جهاز واحد، قياس واحد لكل صفحة. أرقام القهوة (3/70 مقابل 30/907) والحجز (4/87 مقابل 27/799) من نفس التشغيل. |
| 0 KB مقابل ≈494 KB JavaScript إطار | نفس التشغيل (فئة js)؛ على القرص `du -cb out/_next/static/chunks/*.js` = 636 KB (يشمل chunks لا تُحمَّل في الرئيسية) |
| 82 سطر JS | كما أعلاه |
| 941 KB صور مستخدَمة / 1.22 MB غير مستخدمة | `du -cb` على 12 صورة مُشار إليها = 963,862 B؛ hero.jpg + s1.jpg = 1,277,187 B بلا مرجع في أي html |
| 280 مجلداً في node_modules (next) | `ls node_modules \| wc -l` بعد npm install |
| 16 HTML (next out/) | `find out -name "*.html" \| wc -l` |
| 20 لقطة بلا خطأ كونسول / 0 تمرير أفقي | work/dallat/shoot.js (page.on console/requestfailed + scrollWidth) |
| 40 موضع رقم هاتف مطموس | prep.sh (grep -c بعد الاستبدال) |
| إيداع واحد 2026-08-07 | `git log` |
تحفّظات مذكورة في tech.md/الشرح: prefetch في Next (RSC 524 KB) يسرّع التنقّل اللاحق؛ خطوط Next المحلية 404 على الخادم البسيط (basePath) فلم تُحسب بايتاتها.

## الصور واللقطات
| الملف | المصدر |
|---|---|
| mobile-01-home · mobile-03-packages · mobile-06-coffee (البطل في A/B/C) وبقية الـ20 | puppeteer-core على http://127.0.0.1:8080 (نسخة عمل مطمّسة)، 1440×900 و390×844 @2x، 2026-09-23 (work/dallat/shoot.js) |
| **الصور داخل اللقطات** | أصول المستودع assets/*.jpg — **مولَّدة بالذكاء الاصطناعي** بتصريح README؛ سطر إفصاح خافت (#A3B1C0) في أسفل كل تصميم يعرض لقطة (A كلها، كاروسيل 2/3/4، البانر، إطارات الريل 2/3/4) + هنا + الشرح |
| التطميس | رقم واتساب/الجوال (wa.me · tel: · النص) → 9665XXXXXXXX / +966 5X XXX XXXX في 13 صفحة؛ لا أسماء أشخاص في الموقع؛ لا JSON-LD (work/dallat/prep.sh) |
| الهوية وإطار الهاتف | 02-brand/README.md + scripts/brand.py (phone_frame)؛ لون الشريحة #F4A62A؛ الخافت #A3B1C0 |
| الريلان (21 ث، بلا موسيقى) | إطارات dallat.py + ffmpeg (work/dallat/reel.sh)؛ موسيقى بلا حقوق تُضاف عند النشر |

## القواعد المطبَّقة
الأساس بلا شعار؛ نسخة logo = اسم نصّي فقط؛ التذييل github.com/moain2028/dallat-alkaif-static؛ لا اسم شخص ولا رقم حقيقي على أي تصميم؛ لقطات مختلفة عن #24 (التخطيط الجوالي الثابت)؛ المنافسون خارجيون فقط؛ لا رابط حي؛ النصوص مختومة مباشرة بحكم الدور.
