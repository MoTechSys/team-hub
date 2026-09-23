keif-aldiafa-angular | صانع العروض | 2026-09-23 | project-pack-v2

# مصادر كل نص ورقم وصورة — keif-aldiafa-angular project-pack-v2 (البند 0 + A–G)

المصدر: https://github.com/moain2028/keif-aldiafa-angular (عام) — README.md · CONTRACT.md · AUDIT-GAPS.md · docs/ARCHITECTURE.md · docs/DECISIONS.md · package.json · src/ · git log، وتشغيل محلي 2026-09-23. الهوية 02-brand/README.md (portfolio-hub) · المعيار project-pack-standard-v2.md.
التذييل على كل تصميم: github.com/moain2028/keif-aldiafa-angular (مستودع عام). لا اسم شخص، لا رقم هاتف، لا سجل تجاري.

## 0. ملفات portfolio-hub الجديدة (portfolio/)
brief.ar.md · brief.en.md · tech.md (جدول الأرقام ومصادرها) · links.md · screenshots/ (32 لقطة 2x: 16 صفحة × ديسكتوب 1440×900 + جوال 390×844) — بقالب 01-projects/_template. تُضاف إلى portfolio-hub/01-projects/keif-aldiafa-angular/.

## A. التصاميم (24 PNG) + B. النشر (14 PNG)
| العنصر | AR | EN | المصدر |
|---|---|---|---|
| العنوان H1 | بديل رقمي للدفتر الورقي في إدارة الضيافة | A digital replacement for the hospitality paper ledger | brief H1 ← README «نظام يستبدل الدفتر الورقي» |
| السطر فوق العنوان | نظام إدارة كيف الضيافة | Keif Al-Diafa Management System | README H1 |
| اسم المستودع (Mono/Amber) | keif-aldiafa-angular | same | اسم المستودع |
| السطر التعريفي | يعمل بلا خادم وبلا إنترنت — على جوالك | No server, works offline — on your phone | README «المعمارية» + «PWA» |
| الوصف | حجوزات بمعالج 4 خطوات، منع تعارض المضيف بالدقيقة، كشف عجز المخزون، عروض وفواتير آلية، دفتر ذمم وأعمار ديون، ومطابقة تسليم وإرجاع العُهد | 4-step booking wizard, minute-level host conflict prevention… | brief «الحل» ← README «المشاكل السبع» + AUDIT-GAPS (معالج 4 خطوات) |
| تاجات | Angular 22 · Signals · IndexedDB · PWA · TypeScript strict · Vitest | same | README badges + package.json |
| 232 | اختباراً خضراء | green tests | `npx ng test --watch=false` 2026-09-23 |
| 60 | إذناً ذرياً | atomic permissions | permission.model.ts (10 × 6) + README |
| 12 | وحدة ميزات | feature modules | `ls src/app/features/` |
| 12 | قراراً معمارياً | architecture decisions | docs/DECISIONS.md ADR-001…012 |
| 13 (بطاقة رقم واحد) | اختبار تعارض | conflict tests | conflict.service.spec.ts + README |
| السطر السفلي | دراسة حالة · مؤسسة حقيقية في جدة — بيانات اللقطات تجريبية ومطموسة | Case study · a real company in Jeddah — screenshot data is seed & masked | README «ما هذا؟» + قاعدة v2 (إعلان seed) |
| CTA | أُحوّل دفترك الورقي إلى نظام يعمل على جوالك — راسلني | Let's turn your paper ledger into an app on your phone — DM or email | brief «للتواصل» (شريحة مشاريع صغيرة) |
| شارة الشريحة | مشاريع صغيرة | Small business | brief · لون #F4A62A من 02-brand (نص Ink عليه ≈ 8:1) |
| wordmark (logo) | معين العباسي | Moain Al-Abbasi | project-pack-standard-v2 §A |
| كاروسيل 1–5 | المشكلة / الحل / كيف يعمل / الأرقام / الدعوة | same | README «المشاكل السبع» · «المعمارية» · «PWA» · docs/ARCHITECTURE.md §4 · tech.md · brief |
| بانر المقال | العنوان + السطر التعريفي + التاجات | same | كما أعلاه |

## اللقطات (حقيقية من التشغيل المحلي — لا لقطة مولّدة)
- البطلة في A والبانر: `desktop-04-event-detail.png` (صفحة الفعالية بأزرار دورة الحياة) + `mobile-10-ledger.png`؛ Story تضيف `mobile-12-aging.png`.
- كاروسيل: `desktop-03-events.png` (1) · `mobile-10-ledger.png` (2) · `desktop-10-ledger.png` (3) · `desktop-12-aging.png` (5).
- الريل: desktop-04-event-detail · mobile-10-ledger · desktop-12-aging · desktop-10-ledger.
- البيانات: بذر seed-data.ts (عملاء ومضيفون تجريبيون) + عرض سعر وفاتورة منقولان من مستندَي العميل الحقيقيَين (ADR-008). **الطمس** قبل التصوير: السجل التجاري → •••، أرقام الجوال → 3 أرقام + •••، البريد → •••@•••، IBAN → SA•• ••••، اسم العميلة الحقيقية → «أ. العـ••••». شعار المؤسسة الرسمي يبقى داخل اللقطة (جزء من الواجهة، ADR-010) ولا يُنسخ خارجها.
- اللقطات في المستودع (docs/proof، 26 ملفاً 390px) لم تُستخدم لأنها بلا طمس وبدقة 1x.

## C. الريل
- `keif-aldiafa-angular-reel-1080x1920-{ar,en}-nologo.mp4`: 21 ث · 1080×1920 · 30fps · H.264/AAC · 6 مشاهد × 4 ث، تلاشٍ 0.6 ث، زوم بطيء · بلا شعار · لا مشاهد خطأ. غلافان = المشهد 1.
- الموسيقى: `reel/music.mp3` مولَّدة بالذكاء الاصطناعي (CassetteAI عبر أدوات Genspark، 30 ث، instrumental) — بلا حقوق طرف ثالث.

## D. الشروحات — explainer.{ar,en}.md ~490/480 كلمة + خلاصة 5 نقاط، كل جملة مذيَّلة بمصدرها.
## E. البحث — research.md: Odoo · Ubeya · Zoho Bookings (+ مرجع eventstaffapp) بروابط مؤرَّخة 2026-09-23؛ التموضع من README/ADR فقط.
## F. النصوص — copy.{ar,en}.md: LinkedIn ≤120 · X ≤280 · IG ≤150 · نص الريل — draft للمحرر.

## تناقضات لم تُعرض (قاعدة v2)
- عدد النماذج: README 14 · ARCHITECTURE 18 · الشجرة 17 → لم يُعرض.
- عدد المكوّنات المشتركة: README 18 · الشجرة 24 → لم يُعرض.
- «500 حركة دفتر بصفر انحراف» (README) — لم أجد الاختبار المطابق بالاسم؛ لم يُعرض.
- «1000 هيكلية» صلاحيات (اقتباس العميل) — ليس رقماً مقيساً؛ لم يُعرض.

## ملاحظات التشغيل (البند 0)
- `npm ci` → `tsc --noEmit` 0 أخطاء → `ng build` ناجح → `ng test` 232/232. الخادم الثابت يحتاج history fallback للمسارات الداخلية. `vitest run` المباشر يُسقط 68 اختباراً لغياب بيئة Angular — ليس عيباً في الكود.
- التعديل على المستودع: صفر (قراءة وتشغيل فقط).

## الهوية والتباين
Navy #0E2A47 · Ink #08172B · Amber #F4A62A (شريحة مشاريع صغيرة) · Sand #F7F5F0 · Mist #DCE3EA · خافت #A3B1C0. Sand على Navy ≈ 13:1 · Amber على Navy ≈ 7.5:1 · Ink على Amber ≈ 8:1 · #A3B1C0 على Navy ≈ 7:1.

## إعادة التوليد
`shoot.py` (Playwright، يحتاج الخادم `spa.py` على dist) → `build.py all` · `build.py b` · `build.py reel` + `make_reel.sh ar|en`.
