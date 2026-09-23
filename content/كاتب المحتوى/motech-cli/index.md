motech-cli | كاتب المحتوى | 2026-09-23 | ready

# motech-cli — فهرس اللقطات (20 لقطة حقيقية، 2x)

المشروع أداة سطر أوامر بلا واجهة رسومية. اللقطات = **نصوص طرفية حقيقية** من تشغيل محلي للمستودع moain2028/motech-cli (commit 1b1d51b، main، Go 1.23.4، linux/amd64) مُدرجة في بطاقة طرفية داكنة بألوان الهوية ومصوَّرة بـ Playwright/Chromium بـ deviceScaleFactor=2 (ديسكتوب 1440 عرض → 2880 بكسل؛ جوال 390 → 780). النصوص في `_txt/*.txt` هي المخرجات الأصلية حرفياً (اسم المستخدم استُبدل بـ motech في `ls -la` فقط؛ لا مسارات شخصية). لم يُنفَّذ setup/register على خادم حقيقي: `setup` و`register` شُغّلا بلا root وبلا توكن لإظهار بوابة الصلاحيات الفعلية. أمر التصوير: `_term-shoot.mjs`.

| الملف | المحتوى | استخدام مقترح |
|---|---|---|
| desktop/mobile-00-install | أوامر التثبيت بسطر واحد من README (Linux/macOS تفاعلي وصامت + Windows)؛ التوكن مُخفى •••• | الكاروسيل «كيف يعمل» |
| desktop/mobile-01-test | `go vet ./... && go test -v ./...` — 6 اختبارات PASS في 3 حزم | **اللقطة الرئيسية** / بطاقة الرقم |
| desktop/mobile-02-build | البناء المتقاطع للأهداف الستة (linux/darwin/windows × amd64/arm64) + `ls -la dist/` | الكاروسيل «الحل» |
| desktop/mobile-03-sums | `sha256sum motech_* > SHA256SUMS` — 6 بصمات | زاوية التوقيع/السلامة |
| desktop/mobile-04-help | `motech --help` (الأوامر الستة بالعربية) + `motech version` → v0.1.0 | الكاروسيل «المشكلة/الحل» |
| desktop/mobile-05-status | `motech status` (Registered false · Elevated false · NetBird IP not connected) + `motech setup` بلا root → رسالة الصلاحيات | |
| desktop/mobile-06-register | `motech register` بلا توكن وبلا root → نفس البوابة | |
| desktop/mobile-07-release-yml | `.github/workflows/release.yml` (permissions · cosign-installer · build 6 targets) | زاوية cosign |
| desktop/mobile-08-security | أول 30 سطراً من SECURITY.md | |
| desktop/mobile-09-tree | شجرة المستودع (27 ملفاً) + سطر الأرقام | |

لا صورة مولّدة بالذكاء الاصطناعي؛ إطار البطاقة رسم CSS.
