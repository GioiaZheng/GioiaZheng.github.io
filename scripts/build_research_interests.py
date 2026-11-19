from pathlib import Path
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import pypdfium2 as pdfium
ROOT=Path(__file__).resolve().parents[1]
for name,file in [('Body','calibri.ttf'),('Bold','calibrib.ttf')]:
    pdfmetrics.registerFont(TTFont(name,'C:/Windows/Fonts/'+file))
pdfmetrics.registerFontFamily('Body',normal='Body',bold='Bold',italic='Body',boldItalic='Bold')
styles={
'name':ParagraphStyle('name',fontName='Bold',fontSize=25,leading=29,spaceAfter=7,textColor=colors.HexColor('#202B36')),
'heading':ParagraphStyle('heading',fontName='Bold',fontSize=11,leading=14,spaceBefore=15,spaceAfter=6,textColor=colors.HexColor('#254C61')),
'body':ParagraphStyle('body',fontName='Body',fontSize=11,leading=15,spaceAfter=8,textColor=colors.HexColor('#202B36')),
'meta':ParagraphStyle('meta',fontName='Body',fontSize=10,leading=14,spaceAfter=5,textColor=colors.HexColor('#52606B'))}
story=[]
def p(text,style='body'):story.append(Paragraph(text,styles[style]))
p('Gioia Zheng','name')
p('M.Sc. Computer Science, TU Darmstadt','meta')
p('<link href="https://gioiazheng.github.io">gioiazheng.github.io</link> | <link href="https://github.com/GioiaZheng">GitHub</link> | gioia.zheng@stud.tu-darmstadt.de','meta')
p('RESEARCH INTERESTS','heading')
p('I study how retrieval and learning systems fail under controlled or exact evaluation, and how reproducible artifacts can make those failures inspectable.')
p('RESEARCH FOCUS','heading')
p('<b>Evaluation beyond one aggregate score.</b> I am interested in paired comparisons, uncertainty estimates, controlled ablations, and per-query analysis. The aim is to distinguish a robust improvement from a result that depends on one metric, threshold, or sample.')
p('<b>Retrieval and evidence diagnostics.</b> I separate retrieval miss, ranking error, context pollution, evidence omission, unsupported generation, and citation failure. This requires intermediate evidence rather than only a final score or answer.')
p('<b>Agent evaluation.</b> I am interested in exact policy evaluation, controlled interventions, adversarial objectives, and representation choices that reveal failures hidden by sampled rollouts. I am developing robot-learning foundations through an ongoing IAS Robot Learning IP; it is not presented as a completed robotics result.')
p('<b>Reproducible ML systems.</b> I treat schemas, experiment manifests, configuration checks, tests, and explicit limitations as part of the research result. A claim should remain traceable to the code, data, configuration, and evaluator that produced it.')
p('SELECTED EVIDENCE','heading')
p('<b>MS MARCO Generative QA.</b> A 6,980-query paired comparison with explicit first-stage boundaries, paired-bootstrap intervals, versioned manifests, and external retrieval checks. The qrels-anchored 50,000-passage arm is not a like-for-like full-corpus comparison.')
p('<b>Q-Learning Exploitability.</b> Exact best-response evaluation found force-loss exploits in 6/6 baseline checkpoint-seat policies; controlled adversarial backup plus D4 evidence pooling reduced this to 0/6 in an exhaustively searchable testbed. This does not establish general robotics or deep-RL performance.')
p('<b>PAIEC 2026.</b> <link href="https://openreview.net/forum?id=unVHJGkE8n">Accepted technical report</link> on fixed shrinkage for evaluation with few labels, selected for poster presentation. This is not an award, ranking, proceedings-publication or completed-presentation claim.')
p('METHODS AND RESEARCH FIT','heading')
p('Fixed query sets and invariant configuration checks; paired and exact evaluation; bootstrap intervals; stage-local signals; versioned schemas and manifests; automated tests and documented scope limits.')
p('I seek HiWi, research assistant, research engineering and collaborative research opportunities in information retrieval, NLP, agent evaluation, robot learning and reproducible ML systems.')
p('Updated 19 November 2026. Current CV and project evidence: gioiazheng.github.io/materials/','meta')
out=ROOT/'public/research/Gioia_Zheng_research_interests.pdf'
SimpleDocTemplate(str(out),pagesize=A4,leftMargin=43,rightMargin=43,topMargin=32,bottomMargin=32,title='Gioia Zheng - Research Interests',author='Gioia Zheng').build(story)
doc=pdfium.PdfDocument(str(out));assert len(doc)==1
preview=ROOT/'tmp/pdfs/research-interests-1.png';preview.parent.mkdir(parents=True,exist_ok=True);doc[0].render(scale=1.5).to_pil().save(str(preview))
print('Research interests: one page')
