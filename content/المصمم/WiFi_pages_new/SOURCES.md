WiFi_pages_new | المصمم | 2026-09-23 | draft

# SOURCES — WiFi_pages_new project pack v2

المستودع: https://github.com/moain2028/WiFi_pages_new · commit 14a68ad (2026-02-13) · استُنسخ 2026-09-23. كل الأرقام أُعيد قياسها بأوامر مذكورة في tech.md.

## الأرقام
| الرقم | أين يظهر | المصدر |
|---|---|---|
| 8 قوالب | كل التصاميم، الريل، الشرح، النصوص | `ls *.html \| wc -l` = 8 |
| 27 متغير MikroTik | التصاميم، بطاقة الرقم، الريل، الشرح، النصوص | `grep -oh '\$([a-z-]*)' *.html errors.txt \| sort -u \| wc -l` = 27 |
| 0 مكتبة خارجية | التصاميم، الريل، الشرح، النصوص | grep على `src="http`/`href="http` لا يجد مكتبات؛ README «صفر مكتبات خارجية» |
| 9 حركات CSS | كاروسيل 4، الريل، الشرح، النصوص | `grep -c '@keyframes' style/style.css` = 9 |
| 19.9 KB CSS (19,894 B) · 4.7 KB الأصل | كاروسيل 5، الشرح، النصوص | `wc -c style/style.css original/style.css` |
| 16 استخدام backdrop-filter | الشرح | grep |
| 7 media queries · 380px | كاروسيل 5، الشرح | grep `@media` |
| 6 أيقونات SVG | كاروسيل 5، الشرح | grep `<svg` |
| 133 KB حمولة (68 KB شعار) | الشرح، البحث | `du -cb *.html errors.txt md5.js 1.png style/style.css` |
| 6 أسماء حقول (username/password/speed/popup/domain/dst) | كاروسيل 3، الريل | grep `name="` في login.html؛ README §سلامة البيانات |
| 2 commits · 2026-02-13 | الشرح، البحث | git log |
| 41★ Responsive-Mikrotik-Template | البحث | curl على GitHub 2026-09-23 ~06:09 UTC |
| **غير معروض عمداً:** أسعار الكروت (100–300 ريال)، رقم الهاتف، عدد المستخدمين/الهوت سبوتات | — | بيانات عميل/غير موثّقة |

## النصوص
- «form action محفوظ»، «input names لم تتغير»، «MD5 CHAP يعمل بدون تعديل»، «متغيرات MikroTik محفوظة»: README §سلامة البيانات — وتحقّقتُ منها بـ grep.
- «طريقة التركيب على MikroTik» (`/ip hotspot html/`): README.
- أسماء الحركات (gradientShift, floatOrb, twinkle, shimmer, btnShine, alertPulse, fadeIn, textGlow): style.css.
- **عطل `.wrap h1:first-of-type`** (style.css:682–688): تشخيص بـ Playwright `getComputedStyle` → `webkitTextFillColor: rgba(0,0,0,0)` على أزرار status.html — موثّق في tech.md وresearch §6 والشرح.
- الدعوة «راسلني / DM me» في nologo — draft للمحرر.
- «الراوتر لم يلاحظ شيئاً» صياغة تسويقية للحقيقة الموثّقة (لا تغيير في HTML/JS)؛ لم يُختبر على راوتر فعلي — مذكور في الفجوات.

## الصور
- **18 لقطة + 1 تمرير** في screenshots/: Playwright Chromium على قوالب مصيَّرة محلياً (`render.py` → preview/ → `http.server :8767`)، جوال 390×844 @2x وديسكتوب 1440×900 @2x، الحركات مجمَّدة عند الالتقاط (`shoot.py`).
- **RUN-NOTES — التصيير المحلي:** لا راوتر MikroTik هنا؛ `render.py` يحلّ `$(var)` بقيم وهمية (username=demo-user، ip 10.5.50.21، uptime 1h32m10s، بايتات مختلقة) ويُقيّم `$(if …)/$(elif …)/$(endif)` لسيناريوهات: دخول عادي، دخول بخطأ («invalid username or password»)، حالة مستخدم، حالة تجربة، نجاح، خروج، خطأ، حظر، إعلان. يعطّل `meta refresh` و`location.href` للالتقاط فقط.
- **الطمس:** رقم هاتف المزوّد → `77• ••• •••`؛ جدول الأسعار → `•• ريال / • ساعات / • أيام / ••• ميجا`؛ روابط LAN (10.10.10.10) والبث الخارجي → `#`.
- **اسم العميل «كلاسيكو نت»** يظهر داخل اللقطات فقط كجزء من الواجهة؛ لا على أي تصميم خارجها ولا في العناوين.
- **الشعار 1.png** (768×545) أصله غير موثّق في المستودع؛ يظهر كجزء من الواجهة فقط ولا يُستخدم عنصراً مستقلاً.
- `shot-desktop-login-crop.png`: قصّ 62% من وسط لقطة الديسكتوب (البطاقة متمركزة). `shot-mobile-quad*.png`, `reel-mobile-stack.png`: تركيب 3–4 لقطات جوال حقيقية على خلفية #0f0c29 (لون الموقع) — بلا تعديل على المحتوى.
- لا صورة مولّدة بالذكاء الاصطناعي أضفتها أنا؛ الخلفيات في الموقع CSS خالص (README «لا فيديو أو صور ثقيلة»).
- الموسيقى: `reel/music.mp3` مولّدة بـ CassetteAI/music-generator 2026-09-23 (30 ث) — بلا حقوق طرف ثالث.

## الهوية
- 02-brand/README.md (portfolio-hub): Navy/Ink/Amber/Sand/Mist + شريحة «مشاريع صغيرة» #F4A62A؛ النص الخافت #A3B1C0؛ IBM Plex Sans Arabic / Inter / JetBrains Mono. الأساس بلا شعار؛ نسخة logo = wordmark نصّي «معين العباسي / Moain Al-Abbasi».
- التذييل: github.com/moain2028/WiFi_pages_new. لا رابط حي (links.md).
