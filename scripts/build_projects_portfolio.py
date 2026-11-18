from pathlib import Path
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, KeepTogether
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
import pypdfium2 as pdfium
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'public/research/Gioia_Zheng_projects_portfolio.pdf'
INK=colors.HexColor('#202B36'); TEAL=colors.HexColor('#008B94'); LINE=colors.HexColor('#B8CDD5'); PALE=colors.HexColor('#EDF5F6')
W=A4[0]-84
styles={
 'title':ParagraphStyle('title',fontName='Helvetica-Bold',fontSize=20,leading=24,textColor=INK,spaceAfter=4),
 'subtitle':ParagraphStyle('subtitle',fontName='Helvetica',fontSize=9,leading=12,textColor=colors.HexColor('#52606B'),spaceAfter=7),
 'heading':ParagraphStyle('heading',fontName='Helvetica-Bold',fontSize=12,leading=15,textColor=INK,spaceBefore=12,spaceAfter=7),
 'body':ParagraphStyle('body',fontName='Helvetica',fontSize=9.5,leading=13,textColor=INK,spaceAfter=7),
 'small':ParagraphStyle('small',fontName='Helvetica',fontSize=8.5,leading=11.5,textColor=INK,spaceAfter=4),
 'label':ParagraphStyle('label',fontName='Helvetica-Bold',fontSize=9,leading=12,textColor=TEAL,spaceAfter=5),
 'bullet':ParagraphStyle('bullet',fontName='Helvetica',fontSize=9.5,leading=13,textColor=INK,leftIndent=10,bulletIndent=0,spaceAfter=5)}
story=[]
def P(t,style='body'):return Paragraph(t,styles[style])
def p(t,style='body'):story.append(P(t,style))
def bullet(t):story.append(Paragraph(t,styles['bullet'],bulletText='-'))
def link(url,label):return '<link href="'+url+'" color="#21566B">'+label+'</link>'
def head(sub):
 p('Gioia Zheng','title');p(sub,'subtitle')
 p('PROJECTS PORTFOLIO | Updated 18 November 2026','label')
 p(link('https://gioiazheng.github.io','gioiazheng.github.io')+' | '+link('https://github.com/GioiaZheng','GitHub')+' | gioia.zheng@stud.tu-darmstadt.de','small')
def boxes(items):
 cells=[P('<b>'+title+'</b><br/>'+text,'small') for title,text in items]
 t=Table([cells],colWidths=[W/len(cells)]*len(cells));t.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,-1),PALE),('BOX',(0,0),(-1,-1),0.5,LINE),('INNERGRID',(0,0),(-1,-1),0.5,LINE),('VALIGN',(0,0),(-1,-1),'TOP'),('LEFTPADDING',(0,0),(-1,-1),8),('RIGHTPADDING',(0,0),(-1,-1),8),('TOPPADDING',(0,0),(-1,-1),8),('BOTTOMPADDING',(0,0),(-1,-1),7)]));story.append(t);story.append(Spacer(1,7))
def footer(c,d):
 c.setStrokeColor(LINE);c.line(42,31,A4[0]-42,31);c.setFont('Helvetica',8);c.setFillColor(INK);c.drawString(42,20,'Gioia Zheng');c.drawRightString(A4[0]-42,20,'Page '+str(d.page))

head('Information retrieval, RAG evaluation and reproducible ML systems')
p('FLAGSHIP RESEARCH ENGINEERING PROJECT','label');p('RAG Observatory','heading')
p('A trace-based toolkit for turning RAG runs into inspectable evidence: stage-aware reports, configuration comparisons, failure labels and explicit observability gaps.')
p(link('https://github.com/GioiaZheng/rag-observatory','Repository')+' | '+link('https://huggingface.co/spaces/GioiaZheng/rag-observatory','Hugging Face demo')+' | '+link('https://gioiazheng.github.io/projects/rag-observatory/','Project overview'))
p('What the system records','heading')
p('Query > Retrieval > Reranking > Context > Prompt > Generation > Evaluation > Diagnostics','small')
boxes([('OBSERVABILITY CONTRACT','Maps public traces into ordered stage spans. Accepts offline OTLP/HTTP JSON exports containing OpenInference retriever, reranker and LLM spans. Large payloads remain outside low-cardinality attributes.'),('DIAGNOSTIC BOUNDARY','Missing stages stay explicit. If an imported trace does not prove which chunks entered the prompt, the adapter records the gap rather than inventing selected context.')])
p('Controlled SciFact retrieval-depth run','heading')
p('Twenty fixed BEIR SciFact test queries were run with deterministic BM25 at retrieval_top_k=1 and 5. The query set, top-1 context policy, extractive generator and qrels evaluator remained fixed.')
rows=[['Configuration','Retrieval hit','Failure-labelled','Retrieval failures','Context failures'],['top_k=1','13/20 (0.650)','7/20','7/20 (35%)','7/20 (35%)'],['top_k=5','14/20 (0.700)','20/20','20/20 (100%)','7/20 (35%)']]
t=Table([[P(x,'small') for x in row] for row in rows],colWidths=[W*x for x in [.19,.20,.19,.22,.20]]);t.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),PALE),('GRID',(0,0),(-1,-1),0.5,LINE),('VALIGN',(0,0),(-1,-1),'TOP'),('TOPPADDING',(0,0),(-1,-1),7),('BOTTOMPADDING',(0,0),(-1,-1),6)]));story.append(t)
p('What this exposed','heading')
bullet('Retrieval hit improved by one query, but the noise heuristic labelled every top_k=5 trace because any irrelevant retrieved document triggers the signal.')
bullet('The largest observed change localized to retrieval: 35% to 100%. Context and generation failure rates both remained 35%.')
bullet('The comparison reveals a retrieval-depth trade-off and a diagnostic-heuristic limitation; it does not turn a smoke experiment into a benchmark claim.')
p('<b>Scope.</b> This is a retrieval-stage run over 40 public traces, not a full generative RAG benchmark. Twenty sorted queries support an inspectable engineering comparison, not a population-level or causal claim.','small')
p('Implementation evidence and limits','heading')
boxes([('DOCUMENTED SNAPSHOT','40 public traces; 20 fixed queries; 107 automated tests; 8 explicit RAG stages. Counts describe the documented study snapshot.'),('IMPLEMENTED','Public trace conversion, OTLP/OpenInference JSON import, stage-aware Markdown reports, configuration reports and per-query failure changes.')])
p('The documented artifact does not establish a production tracing backend, network receiver, dataset-wide generative result or causal conclusion beyond the controlled exported runs.','small')

story.append(PageBreak());head('Accepted report and released retrieval-audit resource')
p('ACCEPTED TECHNICAL REPORT','label');p('Fixed Shrinkage for Predictive AI Evaluation with Few Observed Labels','heading')
p('<b>Gioia Zheng</b> | PAIEC 2026 | Accepted November 2026')
p('Predicting model correctness with few observed labels. The submitted method uses fixed Beta(1,1) shrinkage, <b>(successes + 1) / (labels + 2)</b>, with random label acquisition.')
boxes([('METHOD AND EVALUATION','Local experiments examine small-budget gains and low-success bias. Weaker shrinkage, transferred priors and lexical weighting did not meet the criteria for replacing the submitted method.'),('REPRODUCTION','Frozen report code revision, evaluation protocol, result summaries and reproducible checks. The documented synthetic-input checks require no dataset, GPU or API.')])
p(link('https://openreview.net/forum?id=unVHJGkE8n','Accepted report - OpenReview paper 29')+'<br/>'+link('https://github.com/GioiaZheng/paiec-2026','Code and reproduction')+' | '+link('https://github.com/GioiaZheng/paiec-2026/blob/main/RESULTS.md','Results')+' | '+link('https://github.com/GioiaZheng/paiec-2026/blob/main/docs/evaluation_protocol.md','Evaluation protocol'))
p('The acceptance concerns the technical report. Competition rank, awards and individual presentation selection are not established by that decision.','small')
story.append(Spacer(1,12));p('RELEASED RESEARCH RESOURCE','label');p('Stage-Aware Retrieval Audit','heading')
p('<b>Release v0.2.2</b> | Candidate availability in two-stage retrieval')
p('Checks where the first judged-relevant document appears in a frozen BM25 run and whether it is available to a reranker restricted to the top 100 candidates. The four operational outcomes are rank 1-10, rank 11-100, rank 101-1000, and no judged-relevant hit by rank 1000.')
boxes([('EVIDENCE COVERAGE','BEIR NFCorpus and SciFact test sets: 623 audited queries. TREC Deep Learning 2019/2020: 97 judged topics. Positive BEIR judgments use relevance >= 1; TREC-DL uses >= 2.'),('INDEPENDENT CHECKS','Author-produced, code-path-independent metric and category recomputation; pinned ranked-run bundle; SHA-256 verification; machine-readable JSON/CSV outputs and provenance documentation.')])
p(link('https://github.com/GioiaZheng/stage-aware-retrieval-audit-release','Repository and quick start')+' | '+link('https://github.com/GioiaZheng/stage-aware-retrieval-audit-release/releases/tag/v0.2.2','Versioned release')+'<br/>'+link('https://github.com/GioiaZheng/stage-aware-retrieval-audit-release/blob/main/docs/PROVENANCE.md','Artifact provenance')+' | '+link('https://gioiazheng.github.io/projects/stage-aware-retrieval-audit/','Project overview'))
p('<b>Scope.</b> The categories describe candidate-set availability under frozen ranked runs and relevance judgments. They do not establish semantic explanations of query difficulty or causal explanations of generated-answer failure. Resource release is separate from any paper-acceptance decision.','small')

story.append(PageBreak());head('Engineering delivery, merged open-source work and methods')
p('Reliable mobile system - CiboCompass','heading')
p('A full-stack food-exploration application for international students in Italy, built with a React Native/Expo client, Go REST API and SQLite persistence.')
bullet('Implemented local caching, a durable pending-feedback queue, and retry on startup, foregrounding or later submissions.')
bullet('Reused idempotency keys across retries and collapsed queued updates to the newest rating per dish and nationality.')
boxes([('OFFLINE DELIVERY','Ratings remain in a durable local queue when the network is unavailable. Retries run on startup, foregrounding and later submissions.'),('WRITE SAFETY','Retries preserve the same idempotency key. Offline delivery does not imply complete multi-device synchronization, actor identity or cross-device conflict resolution.')])
p(link('https://github.com/GioiaZheng/CiboCompass','CiboCompass repository'))
p('Merged open-source work','heading')
boxes([('MTEB ECOSYSTEM','Documented the model-evaluation request workflow: '+link('https://github.com/embeddings-benchmark/mteb/pull/4861','MTEB #4861')+'.<br/><br/>Added model language-scope metadata, tests and accessibility coverage in leaderboard cards: '+link('https://github.com/embeddings-benchmark/leaderboard-frontend/pull/31','Leaderboard #31')+'.')])
p('Client systems delivery - Idearia','heading')
p('<b>Web Development Collaborator</b>')
boxes([('DATA TOOL','Built a client-facing web tool for inspecting and analysing uploaded Excel data.'),('OPERATIONS TOOL','Built a second client system for managing employee leave requests and administrative records.'),('WEB AND AUTOMATION','Maintained WordPress/PHP sites, created minisites with domain and email setup, delivered two n8n workflows and managed Xibo media content.')])
p('Methods and application context','heading')
boxes([('IR AND NLP','BM25, FAISS, cross-encoder reranking, T5, retrieval diagnostics and RAG evaluation.'),('EVALUATION','Paired bootstrap, confidence intervals, controlled comparisons, failure taxonomies and qrels-based checks.'),('SYSTEMS','Python, Go, SQL, REST APIs, SQLite, Docker, GitHub Actions, offline queues and idempotent writes.')])
p('<b>Education.</b> M.Sc. Computer Science, TU Darmstadt (Winter 2026). B.Sc. Applied Computer Science and Artificial Intelligence, Sapienza University of Rome (Winter 2022).','small')
p('<b>Research fit.</b> HiWi, research assistant and research engineering opportunities in information retrieval, NLP, reliable RAG and reproducible ML systems.','small')
p('Current CV, research interests and project evidence: '+link('https://gioiazheng.github.io/materials/','gioiazheng.github.io/materials/'),'small')
SimpleDocTemplate(str(OUT),pagesize=A4,leftMargin=42,rightMargin=42,topMargin=35,bottomMargin=43,title='Gioia Zheng - Projects Portfolio',author='Gioia Zheng').build(story,onFirstPage=footer,onLaterPages=footer)
doc=pdfium.PdfDocument(str(OUT));assert len(doc)==3, len(doc)
qa=ROOT.parents[1]/'output/pdf/portfolio';qa.mkdir(parents=True,exist_ok=True)
for i,page in enumerate(doc):page.render(scale=1.5).to_pil().save(str(qa/f'portfolio-{i+1}.png'))
print('Portfolio generated: 3 pages')
