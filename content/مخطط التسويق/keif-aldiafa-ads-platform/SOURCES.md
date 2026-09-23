keif-aldiafa-ads-platform | مخطط التسويق | 2026-09-23 | v2

# SOURCES.md — مصدر كل نص ورقم وصورة في keif-aldiafa-ads-platform-project-pack-v2

المشروع لم يكن في portfolio-hub؛ البند 0 أنتج `project/` (brief.ar/en.md · tech.md · links.md · screenshots/ 16 لقطة) — المصدر الأساسي لكل ما يلي، مع الكود والوثائق في https://github.com/moain2028/keif-aldiafa-ads-platform (commit e21bd98، 2026-08-31) وبناء محلي بتاريخ 2026-09-23.

## A. النصوص والأرقام على التصاميم
| العنصر | المصدر |
|---|---|
| الاسم «منصة كيف الإعلانية / Keif Ads Platform» | README «منصة كيف الضيافة (Keif Aldiafa Ads Platform)» — مختصر ليتّسع؛ الاسم الكامل في brief/explainer |
| slug keif-aldiafa-ads-platform | اسم المستودع |
| العنوان «اتصال دائم بـ Google Ads يجيب: من غيّر إيش ومتى؟» | README «الهدف: منصة تتصل… اتصالاً دائماً… تكشف من غيّر إيش ومتى» |
| السطر الوصفي (Hono + D1، تجديد توكن تلقائي، GAQL حر، فحص صحة رباعي، لوحة RTL، دليل GAQL) | README «المميزات المكتملة» + `src/google.ts` + docs/07 |
| 13 نقطة API | `grep -o "app\.(get\|post)(" src/index.tsx` = 11 + 2 |
| 19 وصفة GAQL | `docs/07-GAQL-COOKBOOK.md` عناوين `###` تحت «مُختبرة وتعمل» (19) |
| 5 استعلامات فاشلة موثَّقة | نفس الملف، جدول «تفشل» (5 صفوف) |
| 4 فحوص صحة | `src/google.ts healthCheck()` (الأسرار، التوكن، Ads، GSC) |
| 10 وثائق | `ls docs` = 10 (README يقول 11 بعدّ نفسه) |
| 3 جداول D1 | `migrations/0001_init.sql` |
| 5 دقائق (تحديث اللوحة) | `src/ui.tsx setInterval(loadHealth, 300000)` |
| «Auto-Apply يحذف كلمات» / «تعديلات مجهولة» / «رموز تنتهي كل ساعة» (نوعياً) | README «المشاكل التي تحلّها» + docs/02 («access_token عمره ساعة») — بلا أي رقم حقيقي |
| تاجات: TypeScript · Hono · Cloudflare D1 · Google Ads API | `package.json` + `wrangler.jsonc` + `src/google.ts` |
| شارة الشريحة: شركات / Companies | تكليف مدير المنتج msg 4616212 + 02-brand SEGMENTS |
| الفوتر github.com/moain2028/keif-aldiafa-ads-platform | تكليف مدير المنتج |
| wordmark «معين العباسي / Moain Al-Abbasi» (نسخ logo فقط) | project-pack-standard-v2 §A |
| بطاقة الرقم «19 وصفة GAQL مُختبرة» + قائمة الموضوعات | docs/07 عناوين الأقسام (الحساب، الميزانيات، الصلاحيات، تدقيق التاج، تغييرات الميزانية/الحالة، Auto-Apply، عبارات البحث) |
| البانر «من غيّر ميزانية حملتك؟ قراءة change_event…» | عنوان مقال مقترح (زاوية 1 في research) من docs/04 |
| «المرحلة 0 مكتملة / المرحلة 1 لم تُبنَ» (brief/explainer/copy) | docs/00-HANDOVER + docs/08-ROADMAP |
| 758 سطر TS · 14.5 KB gzip (brief/explainer فقط) | `wc -l src/*` · `npm run build` 2026-09-23 |

## B. الصور (كلها لقطات حقيقية من تشغيل محلي 2026-09-23، Playwright Chromium، DPR 2)
| الاستخدام | الملف | ملاحظة |
|---|---|---|
| القطع الست، كاروسيل 2، البانر، غلاف الريل، الريل 2 | desktop-01-dashboard / mobile-01-dashboard | اللوحة |
| كاروسيل 1 | mobile-01-dashboard | |
| كاروسيل 3، الريل 3 | desktop-02-api-health / mobile-02-api-health | استجابة `/api/health` الحقيقية من التشغيل المحلي، مقدَّمة كبطاقة طرفية (نفس البايتات، تنسيق فقط) |
| كاروسيل 4، الريل 4 | desktop-03-api-performance / mobile-03-api-performance | استجابة `/api/ads/performance?days=30` |
| كاروسيل 5، الريل 5 | mobile-01c-dashboard-gsc | جدول كلمات البحث في اللوحة |
| **بيانات داخل اللقطات** | كل الأرقام (80,060 ظهور، 3,244 نقرة، 10,490.75 SAR، 71 تحويل)، الحملات الثلاث «(عرض)»، الكلمات الست، «حساب تجريبي (بيانات عرض)»، `0000000000`، `example.com`، `MOCK-ACCESS-TOKEN` | **وهمية** من `make/mock/mock-worker.js` — لم يُتصل بأي حساب حقيقي؛ لا يُقتبس منها رقم نصاً |
| «كيف الضيافة — لوحة الاتصال الدائم» و«keif-diafa-api» في رأس اللوحة | من `src/ui.tsx` الأصلي | اسم جهة معروفة على المنصة — مسموح؛ لا أشخاص |
| الخلفيات/الشبكة/التوهج وإطار الطرفية | مولّدة برمجياً (02-brand/scripts/brand.py + shoot.py) | لا صور مخزون، لا لقطة مولّدة بالذكاء الاصطناعي |

## C. الصوت
- الريلان: نفس المقطع الموسيقي الآلي المولّد (CassetteAI/music-generator، 24 ث، 2026-09-23) المستخدم في حزمي السابقة لتوحيد صوت المحفظة؛ بلا حقوق طرف ثالث.

## D. ملفات البحث والنص
- `research.md`: كل ادعاء خارجي برابط وتاريخ وصول 2026-09-23 (Optmyzr، Adalysis، Google Ads Scripts، change-event، Auto-apply).
- `explainer.ar/en.md`، `copy.ar/en.md`: كل جملة من brief/tech/README/docs؛ draft حتى ختم المحرر.

## E. طريقة التشغيل (make/)
- `mock/mock-worker.js` + `mock/wrangler.jsonc`: غلاف يستورد `dist/_worker.js` المبني من المستودع ويعترض `fetch` إلى Google بردود وهمية؛ D1 محلي عبر `wrangler dev --local` + migration المستودع. **خارج المستودع؛ الكود الأصلي لم يُغيَّر.**
- `shoot.py`: التصوير (اللوحة + بطاقات API). `build.py` + `packlib.py`: التصاميم. `make_reel.sh`: الريل.

## F. ما لم يُستخدم عمداً
- لقطة `/api/catalog` (حُذفت): الاستجابة تحمل بريد المالك المكتوب في `src/index.tsx:219`.
- معرّف حساب Google Ads الحقيقي، رابط الموقع، معرّفات الحملات الحقيقية، وأرقام الأداء الحقيقية (55 كلمة، 8 تغييرات، ROAS 0.00) الموجودة في README وdocs/03–06 — وُصفت المشاكل نوعياً فقط.
- «محرك تحليل جنائي» و«حرس حساب» كمنجَزات — المرحلة 1 غير مبنية (docs/08)؛ استُخدم «منهجية جنائية موثَّقة».
- «11 وثيقة» من README — الفعلي 10 في docs.
- أي رقم من بيانات اللقطات الوهمية؛ أي اسم شخص أو هاتف أو بريد.

## G. التباين
- النصوص على الخلفية الداكنة: White/#F2F2F2 و#A3B1C0 (الخافت المعتمد) على Navy — AA فأعلى؛ الشارة الصفراء الوسطى للشريحة بنص Navy؛ لا نص مقطوع (فحص بصري لـ LinkedIn AR/EN، كاروسيل 3 EN، مقاسات كل الـ40 آلياً).
