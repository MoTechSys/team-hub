almutahassil-site | متخصص SEO | 2026-09-23

# تشغيل محلي وتصوير
1. `git clone --filter=blob:none --single-branch https://github.com/moain2028/almutahassil-site`
2. موقع ثابت: `python3 -m http.server 3300 --bind 127.0.0.1` من جذر المستودع (لا build، لا تبعيات).
3. `python3 shoot.py` (Playwright/Chromium headless، device_scale_factor=2): 7 صفحات ديسكتوب 1440×900 + 4 لقطات مواضع (KPI الـdemo، شبكة الوحدات، آلية العمل، سؤال مفتوح) + 5 صفحات جوال 390×844 + 2 مواضع = 18 PNG.
   - يمرّ السكربت على الصفحة كاملة قبل اللقطة لتشغيل reveal والعدّادات ثم يعود للأعلى.
   - طمس (blur 6px) لأي نص يحوي اسم الجهة الشخصي أو الهاتف/البريد النموذجيَّين.
4. تحقق: كل الصفحات 200؛ لا أخطاء console مؤثّرة؛ الخط يُحمَّل من Google Fonts (يلزم إنترنت للتصوير).
