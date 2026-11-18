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
p('I study how retrieval-augmented systems fail, how those failures change across configurations and data boundaries, and how evaluation artifacts can make the evidence inspectable and reproducible.')
p('RESEARCH FOCUS','heading')
p('<b>Evaluation beyond one aggregate score.</b> I am interested in paired comparisons, uncertainty estimates, controlled ablations, and per-query analysis. The aim is to distinguish a robust improvement from a result that depends on one metric, threshold, or sample.')
p('<b>Retrieval and evidence diagnostics.</b> I want to separate retrieval miss, ranking error, context pollution, evidence omission, unsupported generation, and citation failure. This requires traces that preserve intermediate states rather than only the final answer.')
p('<b>Reproducible ML systems.</b> I treat schemas, experiment manifests, configuration checks, tests, and explicit limitations as part of the research result. A claim should remain traceable to the code, data, configuration, and evaluator that produced it.')
p('SELECTED EVIDENCE','heading')
p('<b>RAG Observatory.</b> Trace schema, OpenTelemetry/OpenInference JSON ingestion, stage-aware reports, configuration comparison, and 40 public SciFact retrieval traces over 20 fixed queries. The small retrieval-stage study is not a full generative benchmark.')
p('<b>Stage-Aware Retrieval Audit.</b> Released v0.2.2 resource for inspecting candidate-set availability in frozen BM25 runs, with separate metric recomputation and provenance checks. Candidate availability does not establish semantic or causal failure attribution.')
p('<b>PAIEC 2026.</b> Accepted technical report: <link href="https://openreview.net/forum?id=unVHJGkE8n">Fixed Shrinkage for Predictive AI Evaluation with Few Observed Labels</link>. Acceptance is not an award or ranking claim.')
p('METHODS AND RESEARCH FIT','heading')
p('Fixed query sets and invariant configuration checks; paired evaluation and bootstrap intervals; stage-local signals; versioned schemas and manifests; automated tests and documented scope limits.')
p('I seek HiWi, research assistant, research engineering and collaborative research opportunities in information retrieval, NLP, reliable RAG and reproducible ML systems. I am also developing robot-learning foundations through the ongoing IAS Robot Learning IP at TU Darmstadt.')
p('Updated 18 November 2026. Current CV and project evidence: gioiazheng.github.io/materials/','meta')
out=ROOT/'public/research/Gioia_Zheng_research_interests.pdf'
SimpleDocTemplate(str(out),pagesize=A4,leftMargin=43,rightMargin=43,topMargin=32,bottomMargin=32,title='Gioia Zheng - Research Interests',author='Gioia Zheng').build(story)
doc=pdfium.PdfDocument(str(out));assert len(doc)==1
preview=ROOT/'research-interests-preview.png';doc[0].render(scale=1.5).to_pil().save(str(preview))
print('Research interests: one page')
