keif-aldiafa-mobile-ui | متخصص SEO | 2026-09-23

# تشغيل محلي وقياس
1. `git clone --filter=blob:none --single-branch https://github.com/moain2028/keif-aldiafa-mobile-ui`
2. `python3 -m http.server 8777 --bind 127.0.0.1` من جذر المستودع (كما في README).
3. `python3 shoot.py` (Playwright/Chromium headless، 2x): 9 لقطات جوال 390×844 + 5 ديسكتوب 1440×900، ويكتب `measure.json`:
   - التباين: `getComputedStyle` لـ15 نصّاً + أقرب خلفية معتمة صاعداً في DOM + صيغة WCAG relative luminance؛ نص التدرّج (`background-clip:text`) يُستثنى صراحة.
   - الزر العائم: `getBoundingClientRect` للزر والشريط السفلي (تداخل 0 px)، وحالة `is-hidden` بعد التمرير (150 ms).
   - الأداء: سجل `response` (20 طلباً)، `PerformanceObserver` LCP، `navigation` timing — خادم محلي؛ أرقام نسبية لا إنتاجية.
   - reduced-motion: سياق `reduced_motion='reduce'` → لمعة `.btn-gold::after` تستمر (عيب موثّق).
4. Lighthouse غير متاح في البيئة (لا Chrome كامل) — استُبدل بالمقاييس أعلاه وذُكر ذلك في tech.md.
