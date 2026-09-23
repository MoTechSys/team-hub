linkhub-3d | صانع الصور | 2026-09-23 | ready

# كيف أُنجز هذا المجلد (لمن يكمل بعدي)

1. الاستنساخ: `git clone --filter=blob:none --single-branch https://github.com/moain2028/linkhub-3d` (عام، 76 ملفاً، commit واحد).
2. التشغيل: لا build — `python3 -m http.server 8792` من جذر المستودع؛ `/keif/` و`/asoul/` 200.
3. إعادة قياس README: `wc -c` وgzip -9 للصفحتَين؛ `grep` للطلبات الخارجية وrAF وpreserve-3d؛ تشغيل `keif/contrast-v2.py` و`asoul/contrast.py` من المستودع نفسه (ALL PASS).
4. الفحص الحي (`scripts/shoot.py <out> audit`): Playwright يسجّل كل طلب شبكة (0 خارجي)، يعدّ البطاقات وhref، يقيس scrollHeight/viewport، أصغر لمس وخط، طبقات backgroundImage/boxShadow على `.face`، ثم ينقر بطاقة إنستقرام مع تعطيل مؤقّت الانتقال (`setTimeout` ≥ 1000ms → لا يُطلق) ويقرأ `transform` (matrix3d عند 180°) وخلفية body قبل/بعد وسمة الثيم وحلقة `stroke-dashoffset`، ثم Escape ويتحقق من الاستعادة. النتائج في `screenshots/linkhub-audit.json`.
5. اللقطات (`desktop` / `mobile` / `flip`): طمس أرقام الهاتف في كل عقدة نصية وaria-label قبل الالتقاط؛ في وضع flip تُطال مدد الانتقال ×1 ث بـ `<style>` مُحقَن لالتقاط منتصف الانقلاب، ويُحجب أي طلب خارج الأصل المحلي (`route.abort`).
6. الفيديو (`video`): سياق Playwright بتسجيل 390×844، نقر بالماوس على 3 بطاقات لكل علامة مع Escape بينها؛ ثم `ffmpeg -ss 1.6` لقصّ الثانية الأولى (قبل تطبيق الطمس) وتحويل إلى mp4. هذه المقاطع تُركَّب داخل إطار الهاتف في الريل.
7. الكتابة: tech.md من README + docs/02 + index.html + القياسات + audit.json؛ brief من tech.md فقط.

ما بقي: النطاق النهائي والحسابات الناقصة — قرارات معلّقة في docs/03 على المالك.
