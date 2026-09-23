moain-promoter-ai | كاتب المحتوى | 2026-09-23 | project-pack v2

# Moain Promoter AI project pack v2 — مصادر كل نص ورقم وصورة

المشروع ليس في portfolio-hub؛ البند 0 أنتج `project/` (brief.ar/en.md · tech.md · links.md · screenshots/ + index.md) المرفق في هذه الحزمة وجاهز للإضافة إلى `01-projects/moain-promoter-ai/`. المصدر الأصلي: https://github.com/moain2028/moain-promoter-ai (main، commit 4d1a567، 2026-09-11) — README.md، docs/*.md، requirements.txt، dashboard/package.json، src/**، configs/*.yaml، prompts/**، tests/**، وتشغيل محلي 2026-09-23 بلا أي مفتاح.

## إفصاحات صدق (تسري على كل الحزمة)
- كل اللقطات من تشغيل محلي **بلا مفاتيح**: قائمة المستودعات في اللوحة تعرض **بيانات عرض** مضمّنة في `dashboard/components/repos/ReposPanel.tsx` (سقوط تلقائي عند غياب GITHUB_TOKEN) — وُسمت «بيانات عرض» في تذييل الشريحة 1/5 حيث ظهرت؛ المعرض والتقويم فارغان كما هما فعلياً؛ حقول المفاتيح فارغة ومخفية.
- لقطات المحادثة (desktop-01/02/03، mobile-01/02/03) **لم تُستخدم في أي تصميم** لأنها تحمل «7 Agents» و«171 مستودعاً» وشارة مزوّد داخل الواجهة (قرار مدير المنتج 2026-09-23). البطل = لوحة الإعدادات مقصوصة بلا رأس ولا شريط جانبي (desktop-10-settings-crop) + الإعدادات جوال (mobile-08).
- لا يُسمّى أي مزوّد نماذج بالاسم في النصوص؛ أسماء المزوّدين تظهر فقط داخل لقطة الواجهة نفسها (بطاقات الإعدادات) كما هي في المنتج.
- لا صورة ولا أيقونة مولّدة بالذكاء الاصطناعي في الحزمة؛ كل الصور لقطات حقيقية.
- «171+ مستودعاً» (README) رقم عن حساب المالك لا عن المشروع — لا يُعرض. «7 وكلاء» (README) مقابل 9 في الكود — اعتُمد الكود.
- الصياغة «مصمَّم لـ / يُدار من»؛ لا ادعاء أن منشوراً نُشر أو لقطة التُقطت آلياً.

## A. التصاميم (24 PNG)
| العنصر | AR | EN | المصدر |
|---|---|---|---|
| العنوان | Moain Promoter AI | Moain Promoter AI | README H1 |
| الثانوي | نظام تسويق متعدد الوكلاء | Multi-agent marketing system | README H1 «Multi-Agent Portfolio Marketing System» |
| السطر التعريفي | فريق من الوكلاء يسوّق محفظة GitHub — بلغتين وعلى ست منصات | A team of agents that markets a GitHub portfolio — in two languages, on six platforms | brief H1 (من README «المميزات»: ثنائي اللغة، 6 منصات) |
| الشارة | مفتوح المصدر · MIT | Open source · MIT | LICENSE (MIT)؛ GitHub API license.spdx_id |
| الميزات (X/Hero/Story) | 9 وكلاء تحت منسّق واحد… · منشورات عربية وإنجليزية لـ 6 منصات · 27 مزوّد نماذج… · وضع تجريبي افتراضي | (مقابلها) | src/agents (9) · src/publishers (6) · src/models/registry.py (27) · configs/agent_defaults.yaml `default_dry_run: true` |
| الأرقام الثلاثة | 9 وكلاء · 6 منصات نشر · 27 مزوّد نماذج | 9 agents · 6 publishing platforms · 27 model providers | tech.md |
| شارة الشريحة | شركات | Companies | تكليف مدير المنتج؛ #3B82F6 من 02-brand |
| التقنيات (فوتر) | Python · FastAPI · Playwright · Next.js 14 | | requirements.txt، dashboard/package.json (next 14.2.5) |
| الرابط | github.com/moain2028/moain-promoter-ai | | تكليف مدير المنتج؛ links.md |
| عنوان شريط المتصفح | فارغ عمداً | | لا موقع حي (links.md) |
| wordmark (logo فقط) | معين العباسي | Moain Al-Abbasi | معيار v2 |
| الخافت | #A3B1C0 | | معيار v2 |
| اللقطات | DESK = desktop-10-settings-crop · MOB = mobile-08-settings · FAN = mobile-08, mobile-09, mobile-07 | | project/screenshots/index.md |

## B. تصاميم النشر (14 PNG)
- كاروسيل 5×AR + 5×EN: 1 المشكلة (brief «المشكلة»؛ لقطة desktop-12-repos-crop + mobile-04 — **تذييل «بيانات عرض»**) · 2 الحل (brief «الحل»؛ الإعدادات) · 3 كيف يعمل: اختيار المستودعات (api.py `/repos/list`، main.py CLI)، الوكلاء والشخصية و27 قالباً (prompts/)، حملة 30/60/90 (README «SchedulerAgent»، configs `campaign_default_days: 30`)، تبديل المزوّد واكتشاف النوع (docs/ROBUST_KEYS.md، src/models/detection/fingerprint.py)؛ لقطة mobile-07 · 4 الأرقام: 9 · 6 · 27 · 82 (tech.md) · 5 لمن (brief «لمن يفيد» + «للتواصل»؛ لقطة mobile-09).
- بطاقة «رقم واحد»: **82** — «اختباراً تمرّ — وCI فعلي على كل push» (pytest محلياً 2026-09-23: 82 passed؛ .github/workflows/ci.yml؛ 5 ملفات اختبار) — قيد مدير المنتج «أصدق ما في المشروع».
- بانر 1600×840 AR/EN: العنوان من زاوية «عمل فريق» (research §5)؛ الأرقام من tech.md؛ اللقطات desktop-10 + mobile-08.

## C. الريلان (1080×1920، 19.6 ث، بلا شعار)
- المشاهد: غلاف (brief H1) → الوكلاء (src/agents) → المنصات (src/publishers، prompts/templates 27، configs) → النماذج (registry 27، fingerprint، dry_run) → الأرقام (tech.md) → CTA (brief «للتواصل»). اللقطات: mobile-08, 07, 09, 06 فقط — لا لقطة محادثة.
- الموسيقى: 02-brand/scripts/reels/bgm-tech-minimal.mp3 (أصل الفريق). الغلاف = الإطار 00.

## D. الشرح (explainer AR/EN)
كل جملة من brief/tech/research؛ الأرقام من جدول tech.md؛ قسم «ما لم يُنجَز» من tech.md «ملاحظات التنظيف» + research §6.

## E. البحث (research.md)
Buffer https://buffer.com/pricing · Hootsuite https://www.hootsuite.com/plans · Typefully https://typefully.com/pricing (+ مراجعات efficient.app، kleo.so، voicemoat.com لأن الصفحة تُرسم بـ JS) · Postiz https://postiz.com/pricing + GitHub API gitroomhq/postiz-app (36,216★، AGPL-3.0) — كلها بتاريخ 2026-09-23.

## F. نصوص النشر (copy AR/EN + نص الريل)
من brief + tech + research؛ الأطوال داخل الحدود (LinkedIn ≤120 · X ≤280 · IG ≤150). draft للمحرر. لا اسم مزوّد نماذج.

## project/ (البند 0)
brief.ar/en.md · tech.md (20 صفاً، كل رقم بأمر/ملف) · links.md · screenshots/ (17 لقطة أصلية + 5 مقصوصة + index.md + سكربتا الالتقاط).

## tools/
packgen.py · reelgen.py · project.py · _portfolio-shoot.mjs · _crop-shoot.mjs — لإعادة التوليد.
