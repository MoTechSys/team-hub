asoul-aldiafa-ops | متخصص SEO | 2026-09-23

# RUN-NOTES — كيف شُغّل وصُوِّر
- `git clone --filter=blob:none --single-branch https://github.com/moain2028/asoul-aldiafa-ops` → 53 ملفاً، 868 KB، 4 commits (2026-09-18).
- المستودع وثائق + بيانات + سكربتات؛ لا خادم ولا واجهة. السكربتات تحتاج ملفات وسيطة غير مرفوعة (`parsed.json`, `pages/`) فلم تُعاد تشغيلها؛ بدلاً من ذلك `verify.py` أعاد حساب كل رقم من المخرجات المرفوعة (`crawl-report.csv`, `similarity-matrix.csv`, `probe-results.tsv`, `imgsizes.tsv`, `sitemap*.xml`, `mobile-audit.md`) — كل رقم في README تطابق.
- اللقطات (`shoot.py`, Playwright Chromium headless, 2x): 18 ديسكتوب 1440×900 + 7 جوال 390×844 = 25. كل لقطة عرض حقيقي لملف من المستودع: Markdown مُصيَّر (python-markdown: tables + fenced_code) بنمط قراءة داكن بخط IBM Plex Sans Arabic/JetBrains Mono من 02-brand/fonts؛ CSV كجدول؛ مصفوفة التشابه كخريطة حرارية مرسومة من `similarity-matrix.csv` (كل خلية = قيمة CSV)؛ ومخرجات طرفية حقيقية (`verify.py`, `git log`, `ls`, `sed` على `similarity.py`).
- الطمس: اسم النشاط، الدومين، رقمان هاتفيان، بريد، حسابات التواصل → `filter: blur(6px)` على العقد النصية عبر تعبير `RX` في `shoot.py`. لم تُصوَّر `POLICY-FINDINGS.md` (حالة التعليق ورمز التوجيه) ولا `title-meta-optimization.md` (أرقام Search Console حقيقية).
- لا صورة/أيقونة مولّدة بالذكاء الاصطناعي في اللقطات؛ الخريطة الحرارية والأنماط مرسومة برمجياً من البيانات.
