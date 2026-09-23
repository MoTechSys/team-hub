keif-aldiafa-angular | صانع العروض | 2026-09-23 | complete

# keif-aldiafa-angular — Technical Sheet
نظام إدارة مؤسسة كيف الضيافة — PWA عربي بالكامل لإدارة فعاليات الضيافة

- **Repo:** moain2028/keif-aldiafa-angular (public) · اسم الحزمة `keif-app`
- **Primary language / stack:** TypeScript strict · Angular 22.1.0 (standalone · signals · zoneless) · IndexedDB عبر `idb` 8 · Service Worker (`@angular/service-worker`) · jsPDF + html2canvas للمستندات · Vitest 4 + jsdom + fake-indexeddb للاختبارات (package.json · node_modules/@angular/core/package.json)
- **الشريحة:** مشاريع صغيرة
- **Problem:** مؤسسة ضيافة في جدة تدير الحجوزات والمضيفين والعُهد والذمم في دفتر ورقي؛ تعارض حجز المضيف، نقص الأغراض عند تزامن الفعاليات، عروض وفواتير يدوية، ديون متراكمة بلا مركزية. (README «المشاكل السبع»)
- **Solution / core features:** حجوزات رقمية بمعالج 4 خطوات · منع تعارض المضيف **بالدقيقة** · كشف عجز المخزون عبر الفعاليات المتداخلة · توليد عرض السعر والفاتورة آلياً من بيانات الفعالية (PDF) · دفتر ذمم append-only لكل مضيف وعميل («له/عليه») · كشوف حساب + أعمار ديون + تذكير سداد (إشعار داخلي/واتساب) · مطابقة تسليم ↔ إرجاع العُهد مع التوالف والمفقود · صلاحيات ذرية 60 إذناً وأدوار مخصّصة · نسخ احتياطي JSON + Google Drive اختياري · قابل للتثبيت ويعمل أوفلاين. (README · docs/ARCHITECTURE.md)
- **Architecture notes:** بلا خادم — كل البيانات في IndexedDB على الجهاز (ADR-002)؛ المال بالهللات الصحيحة `toCents` (ADR-004)؛ 12 ADR موثّقة في docs/DECISIONS.md؛ عقد ملزم CONTRACT.md (ملف ≤400 سطر، صفر `any`، اختبار لكل خدمة منطق).
- **Status:** قيد التطوير (شارة README) — تدقيق AUDIT-GAPS.md يرصد فجوات وظيفية (إشعار المضيف عند الحجز غير موصول؛ التذكير واتساب/داخلي لا SMS).
- **Last commit:** 2026-08-05 (أول commit 2026-08-01) — git log
- **Live URL:** none (نشر داخلي rsync إلى /var/www/keif-app حسب README)

## الأرقام ومصادرها / Numbers & sources
| Metric | Value | Source |
|---|---|---|
| Angular | 22.1.0 | node_modules/@angular/core/package.json بعد `npm ci` 2026-09-23 |
| اختبارات | 232 اختباراً في 24 ملف spec — كلها خضراء | `npx ng test --watch=false` 2026-09-23: «Test Files 24 passed · Tests 232 passed» |
| اختبارات التعارض | 13 | `grep -c "it(" src/app/core/services/conflict.service.spec.ts` (يوافق README «13 اختباراً») |
| أذونات ذرية | 60 = 10 موارد × 6 أفعال | src/app/core/models/permission.model.ts سطر 8–23 (RESOURCES ×  ACTIONS) — يوافق README |
| نماذج البيانات | 17 ملف `*.model.ts` | `ls src/app/core/models/` (README يقول 14 وARCHITECTURE يقول 18 — تعارض؛ الرقم المعتمد هنا من الشجرة) |
| خدمات المنطق | 33 خدمة | `ls src/app/core/services/*.ts` بلا spec/index |
| مكوّنات UI مشتركة | 24 | `ls -d src/app/shared/components/*/` (README يقول 18 — تعارض؛ المعتمد من الشجرة) |
| Pipes | 4 (sar · arDate · eventStatus · relativeTime) | src/app/shared/pipes + README |
| وحدات الميزات | 12 (auth · dashboard · events · clients · hosts · inventory · quotes · invoices · ledger · reports · notifications · settings) | `ls src/app/features/` |
| ADRs | 12 | docs/DECISIONS.md (ADR-001…012) |
| أسطر TypeScript (بلا اختبارات) | 21,551 | `find src -name '*.ts' ! -name '*.spec.ts' \| xargs cat \| wc -l` |
| أسطر HTML | 4,575 | `find src -name '*.html' \| xargs cat \| wc -l` |
| commits · ملفات · مدة | 40 commit · 412 ملفاً · 2026-08-01 → 2026-08-05 (5 أيام) | git log / git ls-files |
| صور إثبات في docs/proof | 26 لقطة 390px | `ls docs/proof` |
| حجم المستودع | 16 MB بلا node_modules | `du -sh` |
| البناء | `npx tsc --noEmit` صفر خطأ · `npx ng build` ناجح (تحذيران CommonJS من jspdf/canvg) | تشغيل 2026-09-23 |
| المستخدمون/الفعاليات في الإنتاج | يُستكمل | غير موثّق |

## التشغيل والتصوير (2026-09-23 — صانع العروض)
- `npm ci` (Node 22.23) → `npx tsc --noEmit` (0 أخطاء) → `npx ng build` → خدمة `dist/keif-app/browser` بخادم ثابت مع history fallback (الخادم البسيط بلا fallback يعطي 404 على المسارات الداخلية — كما يحذّر README «الفخ 6»).
- ملاحظة: `npx vitest run` مباشرةً يُسقط 68 اختباراً (TestBed/jsdom غير مهيّأ) — الطريقة الصحيحة `npx ng test --watch=false` وتنجح كاملة.
- الدخول ببيانات المدير المبذورة (seed.service.ts) ثم 16 صفحة × (ديسكتوب 1440×900 + جوال 390×844) بدقة 2x = 32 لقطة في screenshots/.
- **الطمس:** رقم السجل التجاري وأرقام الجوال والبريد وIBAN واسم العميلة الحقيقية (من عرض السعر/الفاتورة المنقولَين حرفياً — ADR-008) طُمست في اللقطات عبر استبدال نصّي في DOM قبل التصوير. بقية الأسماء في seed-data تجريبية.
- الشعار الرسمي للمؤسسة يظهر في اللقطات لأنه جزء من الواجهة (ADR-010) — لا يُنسخ خارج اللقطة على التصاميم.

## ملاحظات التنظيف / Cleanup notes
- README يضمّ رقم السجل التجاري وconstants.ts يضمّ IBAN ورقم حساب بنكي وجوال المؤسسة — بيانات حقيقية في مستودع عام؛ يُستحسن نقلها إلى إعدادات تُدخل عند التشغيل.
- كلمة مرور المدير المبدئية «123» مكتوبة في seed.service.ts (تُجزَّأ عند البذر، لكن القيمة نصّ في المستودع).
- تعارض أعداد النماذج (14/17/18) والمكوّنات (18/24) بين README وARCHITECTURE والشجرة.
- AUDIT-GAPS.md يرصد: إشعار المضيف عند الحجز غير موصول؛ ربط العُهدة بالمضيف عند التسليم غير إلزامي.
- لا رابط حي؛ النشر rsync يدوي.

## مصادر
README.md · CONTRACT.md · AUDIT-GAPS.md · docs/ARCHITECTURE.md · docs/DECISIONS.md · package.json · src/app/core/models/permission.model.ts · seed.service.ts · git log · تشغيل محلي 2026-09-23.
