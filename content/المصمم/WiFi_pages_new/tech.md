WiFi_pages_new | المصمم | 2026-09-23 | draft

# WiFi_pages_new — Technical Sheet

- **Repo:** moain2028/WiFi_pages_new (public — استُنسخ بلا مصادقة 2026-09-23). الشقيق: moain2028/WiFi_pages_old (لم يُفحص).
- **ما هو فعلاً:** **قوالب بوابة هوت سبوت MikroTik RouterOS** (`/ip hotspot html/`) — ليست موقع ويب. 8 ملفات HTML تحوي متغيرات القالب `$(…)` وشروط `$(if …)` التي يملؤها الراوتر عند التقديم. README §«طريقة التركيب» يؤكد ذلك.
- **Primary language / stack:** HTML + CSS3 خام (Glassmorphism، animated gradient، `backdrop-filter`) + JavaScript قديم للـ CHAP-MD5 (`md5.js`) وكوكيز حفظ اسم المستخدم/السرعة. صفر مكتبات خارجية (README، `grep` لا يجد أي `src="http`/`href="http` لمكتبات).
- **Problem:** مزوّد إنترنت لاسلكي محلي يريد صفحة دخول للكروت تبدو حديثة على هواتف المستخدمين دون كسر منطق MikroTik (أسماء الحقول، form action، CHAP، الكوكيز).
- **Solution / core features:** إعادة تصميم كاملة لطبقة CSS (4.7 KB → 19.9 KB) مع الحفاظ على HTML/JS وظيفياً: صفحة دخول (اختيار سرعة + رقم كرت + زر تجربة مجانية شرطي)، حالة الجلسة (وقت متبقٍ/بايتات)، نجاح الدخول، الخروج، خطأ، حظر مؤقت، إعلان، إعادة توجيه WISP. أيقونات SVG مضمّنة (6)، 9 حركات CSS، 7 media queries، نسخة `original/` احتياطية.
- **Architecture notes:** كل صفحة تربط `style/style.css` واحداً؛ لا build ولا index (حُذف index.html في commit 2 حسب CLEANUP_LOG). الفوتر يحوي رقم هاتف المزوّد، وجدول أسعار كروت، وروابط داخلية لشبكة LAN (10.10.10.10) وبث خارجي.
- **Status:** v2.0 (README) — قوالب جاهزة للرفع؛ لا يمكن التحقق من عملها على راوتر هنا.
- **Last commit:** 2026-02-13 (`git log -1`) · 2 commits.
- **Live URL:** none — بوابات الهوت سبوت تُخدَم من الراوتر على الشبكة المحلية فقط.

## الأرقام ومصادرها / Numbers & sources
| Metric | Value | Source |
|---|---|---|
| HTML templates | **8** (login, status, alogin, logout, error, hacker, radvert, rlogin) | `ls *.html \| wc -l` |
| MikroTik template variables | **27** فريدة (`$(link-login-only)`, `$(chap-id)`, `$(bytes-in)`…) | `grep -oh '\$([a-z-]*)' *.html errors.txt \| sort -u \| wc -l` |
| Template conditions | 9 أشكال `$(if …)` + 1 `$(elif …)` | grep |
| style.css | **19,894 B** (853 سطراً) مقابل الأصل 4,753 B | `wc -c style/style.css original/style.css` (README يقول ~19 KB — مطابق) |
| CSS animations | **9** `@keyframes` (gradientShift, floatOrb, twinkle, shimmer, btnShine, alertPulse, fadeIn, textGlow) | grep |
| `backdrop-filter` uses | 16 | grep |
| Media queries | 7 (575px, 380px, 768px, 600px, print) | grep `@media` |
| Inline SVG icons | 6 | grep `<svg` |
| External libraries | **0** | grep لمكتبات؛ README |
| Deploy payload (html+css+js+png+errors.txt) | 136,193 B ≈ 133 KB (الشعار 68 KB منها) | `du -cb` |
| Background gradient colors | 8 (README) — الكود: `linear-gradient(-45deg, #0f0c29, …)` | style.css:24 |
| Login form inputs | 11 عنصر `<input>`؛ أسماء الحقول username/password/speed/popup/domain/dst محفوظة | grep |
| md5.js | 217 سطراً (CHAP) | wc -l |
| Emoji in UI | 21 | regex |
| Commits | 2 · 2026-02-13 | git log |
| Tests | none | لا ملفات |
| Users / hotspots | يُستكمل | غير موثّق |

## ملاحظات التنظيف / Cleanup notes
- **عطل CSS حقيقي:** القاعدة `.wrap h1:first-of-type` (style.css:682–688) تطبّق `-webkit-text-fill-color: transparent` + `background-clip: text` لتأثير النيون على اسم الشبكة، لكن في `status.html` أول `<h1>` يحوي **الأزرار الثلاثة** («انقر هنا لفتح الاستراحة…») فيصير نصّها شفافاً → أزرار بلا نص (لُوحظ في اللقطة وتحقّقت منه بـ getComputedStyle: `webkitTextFillColor: rgba(0,0,0,0)`). الحل: تقييد القاعدة بـ `.brand-glow` أو استثناء `h1 button`.
- **رقم هاتف المزوّد** (tel:) في login/status + روابط LAN 10.10.10.10 ورابط بث خارجي (نطاق طرف ثالث) — طُمست/عُطّلت في المعاينة؛ لا تظهر على أي تصميم.
- **جدول أسعار الكروت** (100–300 ريال) — بيانات عرض للعميل؛ طُمس في اللقطات ولا يُعرض.
- **اسم العميل «كلاسيكو نت»** داخل الصفحات فقط؛ لا يظهر على التصاميم.
- **الشعار 1.png** (768×545) — أصله غير موثّق؛ يظهر داخل اللقطات كجزء من الواجهة فقط.
- **UUID سرعة افتراضي** مضمّن في JS (`55987b0d-…`) — خاص بتهيئة الراوتر؛ لا يُعرض.
- README يذكر `index.html` في هيكل الملفات رغم حذفه (CLEANUP_LOG) — تحديث README.
- `alogin.html`/`radvert.html` تعيد التوجيه فوراً (`meta refresh`) — عُطّلت في المعاينة فقط (render.py).
- خط الواجهة `Segoe UI/Tahoma` نظامي — لا خط عربي مخصص.
- لا اختبارات؛ لا يمكن التحقق من CHAP إلا على راوتر.
