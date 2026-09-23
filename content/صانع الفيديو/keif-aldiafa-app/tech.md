keif-aldiafa-app | صانع الفيديو | 2026-09-23 | draft

# keif-aldiafa-app — Technical Sheet

- **Repo:** moain2028/keif-aldiafa-app (public) · الفرع main · 3 commits (2026-08-01 → 2026-08-03) · المستودع على GitHub أُنشئ 2026-09-22
- **Primary language / stack:** TypeScript · React Native 0.86.2 · Expo SDK 57 (expo-router · expo-sqlite · expo-print · expo-auth-session) · TanStack Query 5 · Zustand 5 · react-hook-form + zod · خطوط Amiri + Tajawal
- **Problem:** مؤسسة كيف الضيافة (ضيافة قهوة سعودية للشركات والفعاليات) تدير العمليات على دفتر ورقي؛ 4 فجوات موثّقة من كلام العميل: تعارض حجز المضيف، نقص المخزون عند تزامن الفعاليات، ضياع مستحقات المضيفين، تأخر تحصيل الشركات (README «ما يحلّه النظام»).
- **Solution / core features:** تطبيق جوال مستخدم واحد، محلي بالكامل بلا إنترنت؛ 6 تبويبات (اللوحة · الفعاليات · المالية · العملاء والمضيفون · المخزون · الإعدادات) + شاشات إنشاء/تفاصيل؛ دورة عمل: عميل → فعالية → حجز مضيفين → عرض سعر → موافقة → فاتورة → عربون → ورقة تجهيز → تسليم → تنفيذ → إرجاع وتدقيق → صرف المستحقات → إغلاق؛ تصدير PDF عربي (عرض سعر/فاتورة/كشف حساب)؛ نسخة احتياطية إلى Google Drive (appDataFolder، نطاق drive.appdata فقط) + تصدير ومشاركة ملف النسخة.
- **Architecture notes:** القيود تُفرض في SQLite بـ TRIGGER + RAISE(ABORT) لا في الواجهة (HOST_DOUBLE_BOOKED على إدراج/تحديث host_assignments، INVENTORY_SHORTAGE على stock_moves من نوع ISSUE)؛ المخزون «محجوز زمنياً»: المتاح = المملوك − التالف/المفقود − المسلَّم لفعاليات متداخلة؛ ترقيم المستندات ذرّي بـ `UPDATE counters ... RETURNING`؛ الضريبة تُحسب لكل بند ثم تُجمع مع تقريب لهللتين؛ `PRAGMA wal_checkpoint(TRUNCATE)` قبل أي نسخ/رفع؛ RTL إجباري؛ نظام تصميم «فخامة خليجية» (ذهبي #C5A059 · كحلي #1A254C · لؤلؤي #F5EFE0).
- **Status:** prototype/beta — الكود كامل الدورة ويعمل، لكن لا اختبارات ولا APK منشور (انظر التنظيف)
- **Last commit:** 2026-08-03
- **Live URL:** none (تطبيق جوال؛ لا نسخة ويب منشورة)

## الأرقام ومصادرها / Numbers & sources
| Metric | Value | Source (file/line or command) |
|---|---|---|
| الفجوات التي يحلّها | 4 | README §«ما يحلّه النظام» (جدول 4 صفوف) · 02-analysis/00-master-analysis.md §1 |
| التبويبات الرئيسية | 6 | app/app/(tabs)/_layout.tsx (6 × Tabs.Screen) · README §الشاشات |
| الشاشات (مسارات expo-router) | 14 | `git ls-files 'app/app/*.tsx' \| grep -v _layout \| wc -l` = 14 (6 تبويبات + event/new + event/[id] + quote/new + quote/[id] + invoice/[id] + client/new + host/new + item/new) |
| جداول قاعدة البيانات | 18 | `grep -c 'CREATE TABLE' app/src/db/schema.sql` = 18 |
| القيود المُنفَّذة بـ TRIGGER | 3 | schema.sql: trg_assign_overlap_ins (س104) · trg_assign_overlap_upd (س121) · trg_block_overissue (س292) |
| الفهارس | 14 | `grep -c 'CREATE INDEX' schema.sql` |
| دوال طبقة البيانات (repo) | 37 | `grep -c '^export async function' app/src/db/repo.ts` |
| أسطر TypeScript/TSX في app/ | 5,392 | `git ls-files 'app/*.ts' 'app/*.tsx' \| xargs cat \| wc -l` |
| حالات الفعالية | 5 | README: DRAFT → QUOTED → CONFIRMED → IN_PROGRESS → COMPLETED |
| حالات الفاتورة | 5 | schema.sql س197–198 (DRAFT/ISSUED/PARTIAL/PAID/CANCELLED) |
| مشروبات مهيّأة مسبقاً | 15 (10 ساخنة + 5 عصائر) | app/src/db/seed.ts (HOT = 10 · JUICES = 5) · README |
| أصناف مخزون مهيّأة | 11 | seed.ts (ITEMS = 11) · README |
| نسبة الاقتراح الافتراضية | مضيف لكل 25 ضيفاً | seed.ts `guestsPerHost=25` · docs/USER-GUIDE.md |
| نسبة العربون الافتراضية | 50% | seed.ts `depositPercent=50` |
| البنود الجاهزة لعرض السعر | 6 | docs/USER-GUIDE.md §4 (جدول 6 صفوف) |
| قرارات معمارية موثّقة (ADR) | 10 | 03-architecture/00-decisions.md (10 صفوف) |
| أبحاث معمّقة | 6 ملفات · ~295 KB | `wc -c 05-research/*` = 294,685 بايت (README يقول ~250 KB) |
| ملفات المستودع | 99 | `git ls-files \| wc -l` |
| الالتزامات (commits) | 3 | `git log --oneline \| wc -l` |
| حجم المستودع | 8.8 MB (منها 7.1 MB حزمة dist-android مسبقة) | `du -sh` بلا .git/node_modules |
| الاختبارات | 0 (سكربت `vitest run` موجود لكن لا ملفات اختبار) | app/package.json س58 · `grep -rn 'describe(' app/src app/app` = 0 |
| Users / clients | يُستكمل (مؤسسة واحدة مذكورة؛ لا عدد مستخدمين موثّق) | README §الترخيص |

## ملاحظات التنظيف / Cleanup notes
- **لا APK منشور:** لا Releases على GitHub، وآخر تشغيل لـ workflow «بناء APK محسَّن» (2026-09-22) انتهى بـ failure. README يشرح eas build كبديل.
- **لا اختبارات آلية** رغم وجود سكربت test.
- **الأرقام المتضاربة (لا تُعرض):** حجم الأبحاث «~250 KB» في README مقابل ~295 KB فعلياً؛ «٦ تبويبات» صحيحة.
- **بيانات حساسة في الكود:** seed.ts يحوي رقم هاتف وبريد وحساب بنكي وIBAN للمؤسسة كإعدادات افتراضية — **لا تُعرض على أي تصميم أو لقطة** (أُخفيت في لقطة الإعدادات).
- **أسماء أشخاص في README:** جدول «التحقق» يذكر اسمي عميلين وأرقام نماذج — لا يُستخدم في المواد الترويجية.
- **تحقّق README المُعلن (5,530 ر.س / 700 ر.س)** لم أُعد إنتاجه لأنه يتطلب أسماء أشخاص؛ منطق الحساب موجود في repo.ts computeTotals.
- **RBAC والإشعارات في الأبحاث (05-research) ليست في الكود:** التطبيق مستخدم واحد بلا أدوار ولا إشعارات (`grep casl/notifications` في src = 0). @casl موجود في package.json فقط.
- **ADR #3 يذكر PostgreSQL EXCLUDE** بينما التنفيذ SQLite triggers (README يوضح السبب).
- **تشغيل الويب (للتصوير فقط):** يلزم تعديلان محليان غير مُلتزَمين: (1) metro.config.js — إضافة `wasm` إلى assetExts + رؤوس COOP/COEP لـ expo-sqlite web؛ (2) src/db/index.ts — `withExclusiveTransactionAsync` غير مدعومة على الويب فاستُبدلت محلياً بـ `withTransactionAsync`. شاشتا «تعذّر تجهيز قاعدة البيانات» و«حجز مضيف متداخل» لم تُصوَّرا.

## اللقطات (screenshots/) — 38 لقطة حقيقية 2x من التشغيل المحلي (Expo web، Chromium، 2026-09-23)
جوال 390×844 وديسكتوب 1440×900، 19 لكل منهما: dashboard · events · money · money-quotes · people · people-hosts · people-dues · stock · stock-shortages · settings · event-detail(+2) · event-completed(+2) · quote-detail · quote-new · invoice-detail · event-new · item-new.
بيانات العرض تجريبية أُدخلت عبر دوال التطبيق نفسها: عملاء بأسماء شركات وهمية، مضيفون بأرقام («مضيف ١»…)، هواتف 05XXXXXXXX؛ لا اسم شخص حقيقي ولا رقم حقيقي.
