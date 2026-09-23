keif-blins-invoices | متخصص SEO | 2026-09-23 | v2 · بحث وتحليل (بحث ويب مؤرَّخ: 2026-09-23)

# keif-blins-invoices — بحث وتحليل السوق والتموضع
English summary at the end.

## 1. من يشتري هذا؟ (تحليل مختصر)
- المشتري النموذجي: مؤسسة فردية أو صغيرة في الضيافة/المناسبات (تجهيز قاعات، بوفيهات، قهوة عربية) تُصدر بضع فواتير وعروض أسعار في الأسبوع، وتحتاج مستنداً رسمياً عربياً بختم المؤسسة يُرسل عبر واتساب في اللحظة نفسها. (المصدر: brief.ar.md «لمن يفيد»، tech.md «Problem»)
- ما يريده: مستند واحد يبدو رسمياً، تفقيط عربي، بلا اشتراك شهري ولا حساب سحابي ولا إنترنت إجباري — الفئة التي تُخاطبها إعلانات «فواتير بدون اشتراك» على Google Play (المصدر: نتائج بحث «تطبيق فواتير بدون اشتراك» 2026-09-23، مثل isalapp.vercel.app وبوكيبي).
- حجم الفئة: لم أجد رقماً موثوقاً لعدد مؤسسات الضيافة الفردية في السعودية في نتائج البحث المؤرّخة، فلا أضع رقماً — **يُستكمل** إن أراد محمد مصدراً رسمياً (الهيئة العامة للإحصاء / منشآت).

## 2. ثلاثة منافسين/بدائل حقيقية (تاريخ الوصول 2026-09-23)
| البديل | ماذا يقول عن نفسه | السعر المعلن | الرابط |
|---|---|---|---|
| **Zoho Invoice** (تطبيق جوال + سحابة) | «تطبيق فوترة مجاني بالكامل» للأعمال الصغيرة؛ فواتير وعروض أسعار وتتبع وقت ومصاريف؛ يدعم العربية | مجاني، بسقف: حتى 500 فاتورة/سنة، 2 مستخدمين، 3 مشاريع (بحسب صفحة الأسعار والمراجعات) | https://www.zoho.com/us/invoice/pricing/ · https://www.zoho.com/us/invoice/mobile-apps/ |
| **Invoice Simple** (تطبيق جوال عالمي) | «أسهل تطبيق فوترة للجوال»؛ 60+ قالباً، دفع إلكتروني | Essentials 6.99$/شهر (حتى 3 فواتير/شهر) · Plus 14.99$ (10 فواتير) · Premium 21.99$ (بلا حد) | https://www.invoicesimple.com/pricing-packages/ |
| **وافِق Wafeq** (محاسبة وفوترة إلكترونية سعودية) | برنامج محاسبي سحابي متوافق مع هيئة الزكاة، فواتير وعروض أسعار وأوامر شراء، 40+ تقريراً، تطبيق جوال | Starter 119 ر.س/شهر (99 ر.س سنوياً) · Plus 149 ر.س/شهر · Premium 199 ر.س/شهر سنوياً — بحسب مركز المساعدة | https://help.wafeq.com/hc/en-sa/articles/22187364508700-What-are-your-pricing-plans-and-available-packages · https://www.wafeq.com/ar |

بدائل أخرى ظهرت في البحث (للإحاطة): قيود Qoyod (محاسبة سحابية سعودية، اشتراك) https://www.qoyod.com/ · دفترة Daftra (تجربة 14 يوماً ثم اشتراك) https://www.daftra.com/ · Invoice/Estimate Maker من Bookipi (Play: «لا يدعم العربية» بحسب مراجعة مستخدم) https://play.google.com/store/apps/details?id=bookipi.invoice.maker.estimate.billing&hl=ar

## 3. التموضع: ماذا يقول المنافس، وأين يتفوّق مشروعنا (من tech.md/README فقط)
| ما يقوله المنافس | ما عندنا (المصدر) |
|---|---|
| Zoho: «مجاني» لكن سحابي بحساب، وسقف 500 فاتورة/سنة | يعمل محلياً بلا خادم ولا حساب، بلا سقف فواتير، والبيانات على الهاتف مع نسخة احتياطية JSON (tech.md «Solution»، README «قرارات ثابتة: خارج النطاق Firebase/حسابات سحابية») |
| Invoice Simple: اشتراك شهري بالدولار يتدرّج بعدد الفواتير | لا اشتراك: APK منشور مجاناً على صفحة الإصدارات (brief «تواصل»، links.md) |
| وافِق/قيود: منظومة محاسبية كاملة (تقارير، رواتب، زاتكا) بـ 99–199 ر.س/شهر | نطاق مركّز: 4 أنواع مستندات (فاتورة/عرض سعر، كشف مختصر، كشف تفصيلي، سند قبض A5) بثيم رسمي معتمد من المؤسسة (tech.md «Document types») |
| القوالب العالمية إنجليزية أو مُعرَّبة يدوياً | عربي RTL أصلي: جداول RTL، تفقيط عربي، مكتبة pdf معدّلة داخلياً لإصلاح مسافات RTL (tech.md stack: `third_party/pdf/` RTL-patched) |
| — | جودة مُثبتة: 32 اختباراً ناجحاً، 0 تحذيرات analyzer، اختبار ضغط كشف بـ 60 دفعة (README، tech.md) |

**نقطة صدق:** المنافسون يتفوّقون في التكامل الضريبي (فوترة إلكترونية زاتكا المرحلة الثانية)، والتقارير المالية، وتعدد المستخدمين/الأجهزة، وiOS. مشروعنا لا يقدّم أي منها بتصميم (README «خارج النطاق»).

## 4. الكلمات المفتاحية
**عربي (10):** تطبيق فواتير للجوال · برنامج فواتير بدون اشتراك · فاتورة PDF عربي · عرض سعر PDF من الجوال · سند قبض إلكتروني · كشف حساب عميل · تطبيق فواتير بدون إنترنت · فواتير مؤسسة ضيافة · تفقيط المبلغ بالعربي · تطبيق فواتير أندرويد مجاني
**English (10):** offline invoice app android · invoice app no subscription · Arabic invoice PDF generator · quotation maker app · receipt voucher app · client account statement app · Flutter invoice app open source · local-only invoicing app · hospitality invoicing app · amount in words Arabic invoice
(ملاحظة: بلا أحجام بحث لأن لا أداة بيانات كلمات مفتاحية متاحة هنا؛ الاختيار مبني على صياغات ظهرت فعلاً في نتائج البحث المؤرّخة أعلاه وعلى وظائف المنتج الموثّقة.)

## 5. ثلاث زوايا محتوى مقترحة
1. **«فاتورة رسمية من الهاتف بلا اشتراك»** — مقارنة صريحة: ماذا تخسر مع سقف Zoho أو اشتراك Invoice Simple، وماذا تحصل عليه محلياً (للشريحة أفراد/مشاريع صغيرة).
2. **«كيف صنعنا PDF عربياً صحيحاً في Flutter»** — قصة تقنية: مكتبة pdf المعدّلة لمسافات RTL، المال بالهللات كـ int، الضريبة بالـ basis points (للمجتمع التقني؛ من README/tech.md).
3. **«موقع + تطبيق فوترة لعميل واحد»** — دراسة حالة مشتركة مع keif-aldiafa-web: نفس المؤسسة، موقع يجلب رسائل واتساب وتطبيق يُصدر مستنداتها (links.md «Case study: see keif-aldiafa-web»).

## 6. الفجوات (صريحة)
- **تقنية:** أندرويد فقط، لا iOS ولا ويب كمنتج (README «خارج النطاق») · لا فوترة إلكترونية زاتكا (QR/UBL) — عائق للمنشآت المسجّلة ضريبياً · لا مزامنة بين أجهزة · لا لقطات لواجهة التطبيق في المستودع (tech.md «يُستكمل») · التطبيق مُخصَّص لمؤسسة واحدة (الاسم والثيم والمجلد باسمها) — ليس منتجاً عاماً بعد · عملاء موثّقون: مؤسسة واحدة (tech.md).
- **تسويقية:** اسم المستودع `keif_blins` غير معبّر (tech.md يقترح إعادة التسمية) · لا صفحة هبوط ولا قائمة على Google Play؛ التوزيع APK مباشر يعني ثقة أقل عند غير التقنيين · لا فيديو تشغيل حقيقي للتطبيق (links.md «Demo video: يُستكمل») · README يخاطب «الوكيل» وليس المستخدم النهائي.

## 7. المصادر
- brief.ar.md / brief.en.md / tech.md / links.md / tech-designer.md — portfolio-hub `01-projects/keif-blins-invoices/`
- README المستودع: https://github.com/moain2028/keif_blins (نسخة عامة) · الأصل https://github.com/MoTechSys/keif_blins · الإصدار https://github.com/MoTechSys/keif_blins/releases/tag/v2.2.0
- Zoho Invoice pricing/mobile: الروابط في الجدول أعلاه (تاريخ الوصول 2026-09-23)
- Invoice Simple pricing: https://www.invoicesimple.com/pricing-packages/ (2026-09-23)
- Wafeq pricing help center: https://help.wafeq.com/hc/en-sa/articles/22187364508700-What-are-your-pricing-plans-and-available-packages (2026-09-23)
- Qoyod: https://www.qoyod.com/ · Daftra: https://www.daftra.com/ · Bookipi (Play): الرابط في §2 (2026-09-23)

---
## English summary
Buyer: sole/small hospitality and events businesses in Saudi Arabia that issue a few Arabic invoices, quotes, and receipts a week and want an official-looking PDF sent over WhatsApp immediately, without a subscription or cloud account. Market size: no reliable dated figure found — left as "to be completed".
Three alternatives (accessed 2026-09-23): Zoho Invoice (free, cloud, capped at 500 invoices/year, 2 users), Invoice Simple ($6.99–$21.99/month by invoice volume), Wafeq (Saudi cloud accounting + ZATCA e-invoicing, SAR 119–199/month). Also seen: Qoyod, Daftra, Bookipi.
Positioning (from tech.md/README only): local-only with no server or account and no invoice cap; free APK; native Arabic RTL with an in-house patched pdf library and Arabic amount-in-words; four official document types in the company's approved theme; 32 passing tests and zero analyzer issues. Honest gaps: Android only, no ZATCA e-invoicing, no multi-device sync, no app-UI screenshots, single documented client, repo name and distribution (direct APK, no Play listing) hurt trust.
Keywords (10+10) and three content angles are listed above.
