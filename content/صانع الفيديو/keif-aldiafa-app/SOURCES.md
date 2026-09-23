keif-aldiafa-app | صانع الفيديو | 2026-09-23 | v2

# SOURCES — كل نص ورقم وصورة في الحزمة

## المستودع (قراءة 2026-09-23، commit 7138e65 بتاريخ 2026-08-03)
- github.com/moain2028/keif-aldiafa-app (عام) — README.md · app/ · docs/USER-GUIDE.md · 01-inputs · 02-analysis · 03-architecture · 05-research

## الأرقام
| الرقم | أين يظهر | المصدر |
|---|---|---|
| 4 فجوات | brief، explainer، الكاروسيل 1، البحث | README §«ما يحلّه النظام» (جدول 4 صفوف) |
| 6 تبويبات | كل التصاميم، الريل، النصوص | app/app/(tabs)/_layout.tsx (6 × Tabs.Screen) |
| 14 شاشة | كل التصاميم، الريل، النصوص | `git ls-files 'app/app/*.tsx' \| grep -v _layout \| wc -l` = 14 |
| 18 جدولاً | التصاميم، الكاروسيل 4، بطاقة الرقم، النصوص | `grep -c 'CREATE TABLE' app/src/db/schema.sql` = 18 |
| 3 قيود TRIGGER | التصاميم، الكاروسيل 3–4، بطاقة الرقم «3»، الريل | schema.sql س104 trg_assign_overlap_ins · س121 trg_assign_overlap_upd · س292 trg_block_overissue |
| 14 فهرساً | explainer | `grep -c 'CREATE INDEX' schema.sql` |
| 0 إنترنت | الكاروسيل 4، الريل | README «يعمل محلياً بالكامل بلا إنترنت» |
| 5 حالات فعالية | explainer | README §دورة العمل |
| 15 مشروباً / 11 صنفاً / 6 بنود جاهزة | explainer، البحث | app/src/db/seed.ts (HOT=10، JUICES=5، ITEMS=11) · docs/USER-GUIDE.md §4 |
| 10 قرارات ADR / 6 أبحاث | explainer | 03-architecture/00-decisions.md · `ls 05-research` |
| React Native 0.86 · Expo 57 · SQLite · TanStack Query | التذييل وشرائح التقنيات | app/package.json |
| 0 اختبارات · 0 إصدارات · فشل CI 2026-09-22 | tech.md، البحث، explainer | app/package.json س58 · GitHub API /releases (0) · /actions/runs (failure) |
| Rentman €39/شهر + €14/مستخدم + €9 | research | https://rentman.io/pricing (2026-09-23) |
| دفترة 1,440 ر.س/سنة (قبل الخصم) · قيود 2,070 ر.س/سنة | research | mazaya.monshaat.gov.sa/mazaya/13871 · /12984 (2026-09-23) |
| قيود «+25 ألف عميل، 14 يوم تجربة» | research | https://www.qoyod.com/ (2026-09-23) |

## النصوص
- brief.ar/en، explainer، copy: كل جملة من README.md، docs/USER-GUIDE.md، 02-analysis/00-master-analysis.md، 03-architecture/00-decisions.md، وtech.md. عبارة «إخفاء زر ليس حماية» من README §القرارات الجوهرية ١ وADR #2. لا اسم عميل أو شخص أو هاتف.
- research: كل ادعاء عن منافس برابطه وتاريخ الوصول في الملف.

## الصور (38 لقطة حقيقية في screenshots/)
- المصدر: تشغيل محلي للمستودع عبر `npx expo start --web` (Expo web، Chromium/Playwright، deviceScaleFactor 2) بتاريخ 2026-09-23. جوال 390×844 وديسكتوب 1440×900.
- تعديلان محليان للتشغيل على الويب فقط (غير مُلتزَمين، لا يغيّران الوظائف): metro.config.js (wasm + رؤوس COOP/COEP) وsrc/db/index.ts (بديل withTransactionAsync لأن المعاملات الحصرية غير مدعومة على الويب).
- بيانات العرض تجريبية أُدخلت عبر دوال التطبيق نفسها (repo.ts): 3 عملاء بأسماء شركات وهمية، 4 مضيفين بأرقام («مضيف ١»…)، 4 فعاليات، 3 عروض أسعار، 2 فاتورتان، حركات تسليم/إرجاع؛ الهواتف 05XXXXXXXX؛ بيانات الاتصال والحساب البنكي للمؤسسة أُخفيت في لقطة الإعدادات (DOM mask).
- لا لقطة خطأ/404 ولا لقطة فارغة ولا اسم شخص.
- التصاميم A وB وأغلفة الريل تستخدم: mobile-dashboard · mobile-stock-shortages · mobile-invoice-detail · mobile-events · mobile-event-detail · mobile-event-completed-2 · mobile-people-dues · mobile-quote-detail · desktop-event-completed.

## الهوية
- 02-brand/README.md (portfolio-hub): Navy/Ink/Amber/Sand/Mist + لون شريحة «مشاريع صغيرة»؛ الخافت #A3B1C0 (تحديث 2026-09-23)؛ IBM Plex Arabic / Inter / JetBrains Mono. الأساس بلا شعار؛ «بشعار» = wordmark نصّي «معين العباسي / Moain Al-Abbasi».
- الموسيقى: 02-brand/scripts/reels/bgm-tech-minimal.mp3 (أصل الفريق، بلا حقوق).
