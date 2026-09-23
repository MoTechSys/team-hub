alabbasi-tech-platform | متخصص SEO | 2026-09-23 | v2 · بحث وتحليل (بحث ويب مؤرَّخ: 2026-09-23)

# alabbasi-tech-platform — بحث وتحليل السوق والتموضع
English summary at the end.

## 1. من يشتري هذا؟
هذا المشروع ذو وجهَين، ولكل وجه مشترٍ:
- **الموقع نفسه كواجهة لبيت البرمجيات:** جمهوره شركات في اليمن والمنطقة تبحث عن بديل لنظام مغلق (ERP/POS، حضور، رسائل، وصول بعيد) — الموقع يخاطبهم بصفحات «بدائل» وأرقام مُتحقَّقة (site/README «الصفحات»، README الجذر «قاعدة المحتوى»).
- **النمط نفسه كخدمة قابلة للبيع:** أي شركة تريد موقعاً رسمياً سريعاً على شبكة ضعيفة + بوابة عملاء (مشاريع/تذاكر/طلبات) تملك شفرتها وبياناتها بلا اشتراك شهري (brief «لمن يفيد»، portal/README «لا DevOps ولا تكلفة شهرية»).
- حجم الفئة: لا رقم مؤرّخ موثوق لعدد الشركات اليمنية الباحثة عن بوابة عملاء — **يُستكمل**. مؤشر نوعي: البحث عن «شركة برمجيات اليمن» يُظهر عدة منافسين محليين بمواقع تسويقية نشطة (§2).

## 2. المنافسون/البدائل الحقيقية (تاريخ الوصول 2026-09-23)
### أ) بدائل «الأداة» — بناء الموقع والبوابة بمنصات مغلقة
| البديل | ماذا يقول عن نفسه | السعر المعلن | الرابط |
|---|---|---|---|
| **Webflow** (بناء مواقع + CMS) | منصة تصميم ونشر مواقع | Site plans 15–25$/شهر سنوياً (25–39$ شهرياً)؛ CMS نحو 23–29$/شهر بحسب صفحات المقارنة؛ تحديث مايو 2026 يخفّض خطة إلى 25$/شهر سنوياً | https://webflow.com/pricing · https://help.webflow.com/hc/en-us/articles/51059955082387 |
| **Zoho Desk** (تذاكر دعم + بوابة عملاء) | مكتب مساعدة سحابي | مجاني حتى 3 وكلاء؛ 7 / 14 / 23 / 40 $ لكل وكيل/شهر سنوياً (Express/Standard/Professional/Enterprise) | https://www.zoho.com/desk/pricing.html |
| **SuiteDash** (بوابة عملاء + CRM + مشاريع) | «Client Portal Software» بمستخدمين غير محدودين | من 19$/شهر (Start) حتى 99$/شهر؛ خيار مدى الحياة | https://suitedash.com/pricing/ |
### ب) بدائل «المنافس» — بيوت برمجيات يمنية لها مواقع تسويقية
| الشركة | ماذا تقول | الرابط |
|---|---|---|
| ORTECH Solutions | «أفضل شركة برمجة في اليمن» — ERP، AI، مواقع، تطبيقات، IoT | https://ortech.tech/ar |
| Avero Digital (صنعاء) | مواقع، اختبار اختراق، ERP، نقاط بيع، ربط محافظ | https://averodigital.vercel.app/ |
| مدارات تك | تطوير مواقع ومتاجر وERP وتطبيقات لليمن والخليج | https://madarat-tech.com/ |
(أيضاً: اكواد فلو https://acouad.com/ · إبداع سوفت https://ebda3soft.com/)

## 3. التموضع: ماذا يقول البديل، وأين يتفوّق مشروعنا (من README/tech.md فقط)
| ما يقوله البديل | ما عندنا (المصدر) |
|---|---|
| Webflow/SuiteDash/Zoho: اشتراك شهري بالدولار، بياناتك على سحابتهم | الشفرة والبيانات للعميل؛ موقع ثابت يُستضاف على أي CDN ومنصة Express + SQLite بلا تكلفة شهرية (README «التموضع»، portal/README «SQLite… لا DevOps ولا تكلفة شهرية») |
| مواقع المنافسين المحليين: صور ثقيلة وادعاءات «الأفضل» | صفر صور (أيقونات SVG مضمّنة)، تصدير ثابت كامل، وقاعدة «حقائق مُتحقَّقة فقط» بأوامر git، مع استبعاد صريح لمشروع مضخَّم (README «قاعدة المحتوى») |
| قوالب عالمية LTR مُعرَّبة | عربي RTL من الأساس: خصائص منطقية حصراً، ظلال لا تُعكس، tracking ≥ 0، `dir="ltr"` لكل رمز لاتيني (README «نظام التصميم») |
| بوابات عملاء عامة | أمن موثّق: JWT في httpOnly cookies، CSRF بـSameSite=Strict + Sec-Fetch-Site، bcrypt 12، throttle 5/15د، مقارنة ثابتة الزمن، RFC 9457، فحص magic bytes للمرفقات (README «الأمن») |
| — | جودة مقاسة: تدقيق بكسلي 14 صفحة × عرضَين — 0px تمرير أفقي، 0 تداخل، 0 صور مكسورة؛ 19/19 صفحة، 0 أخطاء TS، 11 اختباراً (tech.md) |

**نقطة صدق:** البدائل السحابية تتفوّق في السرعة للتشغيل (دقائق لا أيام)، والدعم، والتكاملات (دفع، بريد، أتمتة)، وiOS/Android جاهزة. مشروعنا **بلا رابط حي الآن** (الدومين غير مسجَّل والنشر المؤقت معطّل)، والمنصة بلا اختبارات آلية، وبعض عيوب التباين وثّقها التدقيق قبل الإصلاح ولم يُعَد قياسها في المستودع، والسجل التجاري «قيد الإجراء» (tech.md «Cleanup notes»).

## 4. الكلمات المفتاحية
**عربي (10):** شركة برمجيات في اليمن · تطوير مواقع صنعاء · موقع شركة سريع على شبكة ضعيفة · بوابة عملاء للشركات · نظام تذاكر دعم عربي · بديل الأنظمة المغلقة · برمجيات تملكها الشركة · موقع Next.js عربي RTL · تصميم موقع بلا صور · تدقيق وصولية موقع عربي
**English (10):** software company Yemen · Next.js static export Arabic RTL · client portal Express SQLite · self-hosted client portal · owned software vs closed systems · zero-image website performance · RTL design system logical properties · pixel audit WCAG contrast touch targets · JSON-LD Arabic company site · low-bandwidth website design
(بلا أحجام بحث — لا أداة بيانات هنا؛ الاختيار من صياغات ظهرت في نتائج البحث المؤرّخة ومن محتوى الموقع الفعلي.)

## 5. ثلاث زوايا محتوى مقترحة
1. **«موقع بلا صورة واحدة»** — لماذا صمّمنا موقع شركة برمجيات بصفر صور وكيف يخدم ذلك أندرويد الرخيص والشبكة الضعيفة في اليمن (README «نظام التصميم»، «مادي معتم»).
2. **«الظلال لا تُعكس في RTL»** — 6 قواعد غير قابلة للتفاوض لتصميم عربي صحيح + 5 أعطال حُلَّت (a{color:inherit} خارج @layer، الإزاحة السالبة تمدّد الصفحة…) — للمجتمع التقني (README «أعطال حُلَّت»).
3. **«مقاسة لا مُدَّعاة»** — كيف يقيس تدقيق بكسلي كل عنصر من البكسلات المرسومة، ولماذا كانت 39 من 194 عيباً كاذبة (docs/pixel-audit-site.md §1).

## 6. الفجوات (صريحة)
- **تقنية:** لا رابط حي (دومين غير مسجَّل، نشر مؤقت معطّل) · المنصة بلا اختبارات آلية (placeholder) · إصلاحات التباين مذكورة في README بلا إعادة قياس مرفقة · commit واحد فقط بلا تاريخ تطوير · `docs/pixel-audit-portal.md` يحوي مساراً محلياً · تعارض «18 صفحة» (site/README) مع «19» (الجذر والبناء).
- **تسويقية:** الموقع يحمل رقم هاتف مباشراً (لا يُنقل للتصاميم) · لا عملاء موثّقون للمنصة · السجل التجاري قيد الإجراء · صفحات البدائل تسمّي منافسَين بالاسم (Onyx Pro، ZKTeco) — يحتاج قرار معين للنشر · لا نسخة إنجليزية من الموقع (عربي فقط) رغم أن الشريحة «شركات» تُفضَّل لها EN أولاً في دليل التحرير.

## 7. المصادر
- README الجذر · site/README.md · portal/README.md · portal/CHANGELOG.md · site/DEPLOYMENT.md · docs/pixel-audit-site.md · docs/pixel-audit-portal.md — https://github.com/moain2028/alabbasi-tech-platform
- tech.md الخاص بهذا التسليم (أوامر التحقق المحلي 2026-09-23)
- Webflow: https://webflow.com/pricing · https://help.webflow.com/hc/en-us/articles/51059955082387 · مقارنات flowout.com / landerlab.io (2026-09-23)
- Zoho Desk: https://www.zoho.com/desk/pricing.html · desk365.io / getmacha.com (2026-09-23)
- SuiteDash: https://suitedash.com/pricing/ (2026-09-23)
- منافسون محليون: ortech.tech · averodigital.vercel.app · madarat-tech.com · acouad.com · ebda3soft.com (2026-09-23)

---
## English summary
Two audiences: companies in Yemen/the region looking to replace closed systems (the site's own "alternatives" pages), and any company wanting a fast site plus an owned client portal with no monthly fee. Market size: no dated figure — "to be completed".
Alternatives (accessed 2026-09-23): tools — Webflow ($15–39/site/month), Zoho Desk (free for 3 agents; $7–40/agent/month), SuiteDash ($19–99/month); local competitors — ORTECH, Avero Digital, Madarat Tech (plus ACOUAD, Ebda3Soft).
Positioning (from README/tech.md only): client owns code and data; fully static export with zero images for weak networks; native RTL design rules; documented security (httpOnly JWT, CSRF guard, bcrypt 12, throttle, RFC 9457, magic-byte checks); measured quality (pixel audit 14 pages × 2 widths, 0 px overflow; 19/19 pages, 0 TS errors, 11 tests). Honest gaps: no live URL today, no portal tests, contrast fixes not re-measured in repo, single commit, phone number on site, no documented portal clients, competitors named on site, Arabic-only site.
