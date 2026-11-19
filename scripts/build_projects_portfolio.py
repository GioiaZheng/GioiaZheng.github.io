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
 p('PROJECTS PORTFOLIO | Updated 19 November 2026','label')
 p(link('https://gioiazheng.github.io','gioiazheng.github.io')+' | '+link('https://github.com/GioiaZheng','GitHub')+' | gioia.zheng@stud.tu-darmstadt.de','small')
def boxes(items):
 cells=[P('<b>'+title+'</b><br/>'+text,'small') for title,text in items]
 t=Table([cells],colWidths=[W/len(cells)]*len(cells));t.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,-1),PALE),('BOX',(0,0),(-1,-1),0.5,LINE),('INNERGRID',(0,0),(-1,-1),0.5,LINE),('VALIGN',(0,0),(-1,-1),'TOP'),('LEFTPADDING',(0,0),(-1,-1),8),('RIGHTPADDING',(0,0),(-1,-1),8),('TOPPADDING',(0,0),(-1,-1),8),('BOTTOMPADDING',(0,0),(-1,-1),7)]));story.append(t);story.append(Spacer(1,7))
def footer(c,d):
 c.setStrokeColor(LINE);c.line(42,31,A4[0]-42,31);c.setFont('Helvetica',8);c.setFillColor(INK);c.drawString(42,20,'Gioia Zheng');c.drawRightString(A4[0]-42,20,'Page '+str(d.page))

head('Exact agent evaluation and controlled failure analysis')
p('FEATURED AGENT-EVALUATION STUDY','label');p('Q-Learning Exploitability','heading')
p('Can apparently competent self-play policies remain systematically exploitable? This study evaluates frozen policies against exact best responses, then tests controlled interventions under matched Q-update budgets.')
p(link('https://github.com/GioiaZheng/q-learning-exploitability','Repository and reproducibility guide')+' | '+link('https://gioiazheng.github.io/projects/q-learning-exploitability/','Project overview')+' | '+link('https://gioiazheng.github.io/writing/when-self-play-q-learning-remains-exploitable/','Technical note'))
boxes([('QUESTION','Sampled matches can hide a systematic counter-policy. Exact evaluation checks whether an opponent can force a loss from every reachable state.'),('CONTRIBUTION','A reproducible failure-analysis chain separating opponent diversity, adversarial Bellman objectives and symmetry-aware evidence pooling.')])
p('Controlled experiment chain','heading')
rows=[['Method','Force-loss exploitable policies','Strategic tests'],['Sampled self-play','6/6','16/21'],['+ Opponent mixture','6/6','20/21'],['+ Adversarial backup','4/6','20/21'],['+ Adversarial backup + D4','0/6','21/21']]
t=Table([[P(x,'small') for x in row] for row in rows],colWidths=[W*.42,W*.34,W*.24]);t.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),PALE),('GRID',(0,0),(-1,-1),0.5,LINE),('VALIGN',(0,0),(-1,-1),'TOP'),('TOPPADDING',(0,0),(-1,-1),7),('BOTTOMPADDING',(0,0),(-1,-1),6)]));story.append(t)
p('What the exact evaluation exposed','heading')
bullet('Opponent mixture improved sampled behavior but left all six frozen checkpoint-seat policies force-loss exploitable.')
bullet('Adversarial backup reduced exploitability to 4/6; D4 canonicalization pooled equivalent evidence across rotations and reflections and reduced it to 0/6.')
bullet('Final policies selected exact-optimal greedy actions in 99.93-99.96% of reachable states.')
p('Mechanism and reproducibility','heading')
boxes([('REPRESENTATION','Reachable states: 4,520 to 627. Reachable state-actions: 16,167 to 2,270.'),('SPARSE EVIDENCE','A historical sparse state increased from 29 raw-orientation visits to 169 pooled visits.'),('ARTIFACTS','12 frozen checkpoints, machine-readable metrics, exact exploit trajectories and 24 automated tests.')])
p('<b>Scope.</b> Tic-Tac-Toe is an exhaustively searchable testbed. This is not a new general reinforcement-learning algorithm and does not establish results for DQN, PPO, robots, stochastic environments or larger games.','small')

story.append(PageBreak());head('Retrieval, generation and candidate-availability evidence')
p('FEATURED RETRIEVAL STUDY','label');p('MS MARCO Generative QA','heading')
p('When do retrieval and reranking changes transfer into better generated answers, and when are they bounded by missing first-stage candidates?')
p(link('https://github.com/GioiaZheng/msmarco-genqa','Repository')+' | '+link('https://github.com/GioiaZheng/msmarco-genqa/blob/main/RESULTS.md','Results')+' | '+link('https://huggingface.co/datasets/GioiaZheng/msmarco-genqa-benchmark-runs','Public benchmark runs')+' | '+link('https://gioiazheng.github.io/projects/msmarco-genqa/','Project overview'))
boxes([('EVALUATED COMPARISON','6,980 paired MS MARCO dev/small queries with fixed T5-small. BM25 uses the full 8.8M-passage corpus; the reranked-dense arm uses a 50,000-passage qrels-anchored pool.'),('HEADLINE RESULT','Token-F1: 0.1966 to 0.3677; paired difference +0.1711, 95% bootstrap CI [+0.1632, +0.1789]. The comparison changes the first-stage condition and does not isolate reranking.')])
p('Generation metrics under the documented comparison','heading')
rows=[['Metric','BM25 arm','Reranked-dense arm','Paired difference'],['Token-F1','0.1966','0.3677','+0.1711'],['ROUGE-L','0.1836','0.3579','+0.1743'],['Sentence BLEU','0.0785','0.2118','+0.1333'],['Exact Match','0.0304','0.0777','+0.0473']]
t=Table([[P(x,'small') for x in row] for row in rows],colWidths=[W*.25,W*.22,W*.28,W*.25]);t.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),PALE),('GRID',(0,0),(-1,-1),0.5,LINE),('VALIGN',(0,0),(-1,-1),'TOP'),('TOPPADDING',(0,0),(-1,-1),6),('BOTTOMPADDING',(0,0),(-1,-1),5)]));story.append(t)
p('External retrieval evidence and limits','heading')
bullet('TREC-DL 2019/2020 provides full-corpus BM25 plus cross-encoder retrieval evidence over 43 and 54 judged topics; it is not generation evidence.')
bullet('On NFCorpus and SciFact, reranking improves early ranking within the fixed BM25 top-100 candidate set while Recall@100 remains unchanged.')
bullet('The current artifacts do not establish full-corpus dense retrieval superiority or generalization beyond the documented datasets.')
p('RELEASED RESEARCH RESOURCE','label');p('Stage-Aware Retrieval Audit','heading')
p('Release v0.2.2 audits where the first judged-relevant item appears in frozen BM25 runs and whether it is available to a top-100 reranker. Coverage: 623 BEIR queries plus 97 TREC-DL topics; independent metric recomputation, pinned runs, SHA-256 checks and machine-readable outputs.')
p(link('https://github.com/GioiaZheng/stage-aware-retrieval-audit-release','Repository and quick start')+' | '+link('https://github.com/GioiaZheng/stage-aware-retrieval-audit-release/releases/tag/v0.2.2','Versioned release')+' | '+link('https://gioiazheng.github.io/projects/stage-aware-retrieval-audit/','Project overview'))
p('<b>Scope.</b> Candidate availability does not establish a semantic or causal explanation of query difficulty or generated-answer failure.','small')

story.append(PageBreak());head('Accepted work, open-source contributions and delivery')
p('ACCEPTED TECHNICAL REPORT','label');p('Fixed Shrinkage for Predictive AI Evaluation with Few Observed Labels','heading')
p('<b>Gioia Zheng</b> | PAIEC at NeurIPS 2026 | Accepted and selected for poster presentation, November 2026')
p('The submitted method predicts model correctness from few observed labels using fixed Beta(1,1) shrinkage, <b>(successes + 1) / (labels + 2)</b>, with random label acquisition.')
boxes([('METHOD AND EVALUATION','Local experiments examine small-budget gains and low-success bias. Weaker shrinkage, transferred priors and lexical weighting did not meet the criteria for replacing the submitted method.'),('REPRODUCTION','Frozen report code revision, evaluation protocol, result summaries and synthetic-input checks that require no dataset, GPU or API.')])
p(link('https://openreview.net/forum?id=unVHJGkE8n','Accepted report - OpenReview paper 29')+' | '+link('https://github.com/GioiaZheng/paiec-2026','Code and reproduction'))
p('Poster selection does not imply an award, competition ranking, proceedings publication or completed presentation.','small')
p('Merged open-source work','heading')
boxes([('EVALUATION CORRECTNESS',link('https://github.com/vectara/open-rag-eval/pull/162','Open RAG Eval #162')+': preserved input order and added a regression test.<br/><br/>'+link('https://github.com/embeddings-benchmark/mteb/pull/4958','MTEB #4958')+': fixed duplicate counting for symmetric STS pairs.<br/><br/>'+link('https://github.com/embeddings-benchmark/mteb/pull/5323','MTEB #5323')+': updated GermanGovService retrieval to v2.'),('REPRODUCIBILITY AND DELIVERY',link('https://github.com/embeddings-benchmark/results/pull/676','MTEB Results #676')+': required run settings for new results.<br/><br/>'+link('https://github.com/embeddings-benchmark/leaderboard-frontend/pull/31','Leaderboard #31')+': added language-scope metadata and accessibility coverage.<br/><br/>'+link('https://github.com/castorini/pyserini/pull/2655','Pyserini #2655')+': fixed M-BEIR instruction lookup from cache-home paths.')])
p('Selected engineering delivery','heading')
boxes([('CIBOCOMPASS','React Native/Expo, Go and SQLite. Implemented durable offline feedback, retry and idempotency-key reuse. This does not imply full multi-device synchronization or actor identity.'),('IDEARIA','Built client-facing data and leave-management tools; maintained WordPress/PHP sites; delivered web, domain/email and n8n workflow support.')])
p('Methods and current direction','heading')
boxes([('RETRIEVAL AND NLP','BM25, FAISS, cross-encoder reranking, T5, retrieval diagnostics and RAG evaluation.'),('AGENT EVALUATION','Exact best response, controlled self-play comparisons, adversarial objectives and symmetry-aware representations.'),('REPRODUCIBLE SYSTEMS','Python, PyTorch, Go, SQL, versioned manifests, tests, Docker and GitHub Actions.')])
p('<b>Education.</b> M.Sc. Computer Science, TU Darmstadt. B.Sc. Applied Computer Science and Artificial Intelligence, Sapienza University of Rome.','small')
p('<b>Research fit.</b> Information retrieval, RAG/LLM evaluation, agent evaluation and reproducible ML. Developing robot-learning foundations through the ongoing IAS Robot Learning IP at TU Darmstadt; no completed robotics result is claimed here.','small')
p('Current CV, research interests and project evidence: '+link('https://gioiazheng.github.io/materials/','gioiazheng.github.io/materials/'),'small')
SimpleDocTemplate(str(OUT),pagesize=A4,leftMargin=42,rightMargin=42,topMargin=35,bottomMargin=43,title='Gioia Zheng - Projects Portfolio',author='Gioia Zheng').build(story,onFirstPage=footer,onLaterPages=footer)
doc=pdfium.PdfDocument(str(OUT));assert len(doc)==3, len(doc)
qa=ROOT/'tmp/pdfs/portfolio';qa.mkdir(parents=True,exist_ok=True)
for i,page in enumerate(doc):page.render(scale=1.5).to_pil().save(str(qa/f'portfolio-{i+1}.png'))
print('Portfolio generated: 3 pages')
