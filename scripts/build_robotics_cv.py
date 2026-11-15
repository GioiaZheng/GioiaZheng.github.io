from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import Flowable, HRFlowable, Paragraph, SimpleDocTemplate, Spacer


OUT = Path(__file__).resolve().parents[1] / "public" / "cv" / "robotics"
OUT.mkdir(exist_ok=True)
PDF = OUT / "Gioia_Zheng_CV.pdf"

BLUE_HEX = "17365D"
BLUE = colors.HexColor("#17365D")
GRAY = colors.HexColor("#555555")
RULE = colors.HexColor("#D9D9D9")


SECTIONS = [
    (
        "RESEARCH AND ENGINEERING EXPERIENCE",
        [
            {
                "title": "Undergraduate Thesis Research — RAG Pipeline Evaluation",
                "meta": "Sapienza University of Rome · Aug 2026–Present",
                "detail": "Supervisor: Prof. Marco Raoul Marini · Co-tutor: Valerio Venanzi",
                "bullets": [
                    "Evaluated retrieve-rerank-generate pipelines across MS MARCO, TREC-DL, SciFact, and NFCorpus.",
                    "Found 72/323 NFCorpus queries with no relevant document in the top 100, including 48 still unresolved at depth 1,000; distinguished depth-recoverable misses from persistent retrieval failures.",
                    "Compared ranking improvements with fixed candidate recall to identify when reranking cannot recover missing evidence.",
                ],
            },
            {
                "title": "NLP Algorithm Engineer Intern",
                "meta": "Microsoft · Remote · Feb–May 2026",
                "detail": None,
                "bullets": [
                    "Implemented BM25 retrieval and cross-encoder reranking for an MS MARCO question-answering pipeline in Python.",
                    "Extended evaluation to TREC-DL 2019/2020 and built reproducible experiment, metric-validation, and query-level analysis workflows.",
                ],
            },
        ],
    ),
    (
        "SELECTED MACHINE LEARNING PROJECTS",
        [
            {
                "title": "Q-learning Exploitability",
                "meta": "Python · Reinforcement Learning · Self-Play",
                "url": "https://github.com/GioiaZheng/q-learning-exploitability",
                "detail": None,
                "bullets": [
                    "Implemented tabular self-play Q-learning and evaluated policies against exact best responses to expose failures hidden by sampled win rates.",
                    "Compared opponent mixtures, adversarial Bellman backups and symmetry-aware state representations under matched training budgets.",
                ],
            },
            {
                "title": "Handwritten OCR System",
                "meta": "PyTorch · OpenCV · CNN–RNN–CTC",
                "url": "https://github.com/GioiaZheng/handwritten-ocr-system",
                "detail": None,
                "bullets": [
                    "Developed an experimental handwriting-recognition pipeline with image preprocessing, convolutional features, bidirectional LSTMs and CTC decoding.",
                    "Implemented image augmentation and CER/WER evaluation; documented dataset configuration and reproducibility checks.",
                ],
            },
        ],
    ),
    (
        "ADDITIONAL EXPERIENCE",
        [
            {
                "title": "DARE Robotics - Student Member",
                "meta": "TU Darmstadt · Nov 2026–Present",
                "detail": None,
                "bullets": [],
            },
            {
                "title": "NoDiscorSi",
                "meta": "Social Media Support",
                "detail": None,
                "bullets": ["Helped manage Instagram and Facebook accounts."],
            },
        ],
    ),
]

OPEN_SOURCE = [
    "Merged MTEB contributions: symmetric STS pair counting (#4958), GermanGovService v2 (#5323), and evaluation-request workflow documentation (#4861).",
    "Merged fixes for cached M-BEIR instruction lookup in Pyserini (#2655) and model language-scope display in the MTEB leaderboard frontend (#31).",
]

SKILLS = [
    ("Programming", "Python, SQL, Bash, Git; working knowledge of Go, JavaScript, and Java"),
    ("ML and Vision", "PyTorch, OpenCV, CNNs, LSTMs, CTC, tabular Q-learning, Transformers, scikit-learn"),
    ("Evaluation", "Policy robustness, CER/WER, MRR, nDCG, paired bootstrap, ablations and failure analysis"),
    ("Engineering", "Linux, Docker, GitHub Actions, pytest, SQLite, REST APIs, reproducible configurations and CI"),
    ("Languages", "Chinese (native), Italian (bilingual), English (professional), German (beginner)"),
]













def build_pdf():
    pdfmetrics.registerFont(TTFont("ArialEmbedded", r"C:\Windows\Fonts\arial.ttf"))
    pdfmetrics.registerFont(TTFont("ArialEmbedded-Bold", r"C:\Windows\Fonts\arialbd.ttf"))
    pdfmetrics.registerFont(TTFont("ArialEmbedded-Italic", r"C:\Windows\Fonts\ariali.ttf"))
    page_width, page_height = A4
    doc = SimpleDocTemplate(
        str(PDF), pagesize=A4, leftMargin=13.5 * mm, rightMargin=13.5 * mm,
        topMargin=10 * mm, bottomMargin=10 * mm,
        title="Gioia Zheng CV", author="Gioia Zheng",
    )
    usable = page_width - 27 * mm
    styles = getSampleStyleSheet()
    title = ParagraphStyle("cvTitle", parent=styles["Normal"], fontName="ArialEmbedded-Bold", fontSize=19.5, leading=21, alignment=TA_CENTER, spaceAfter=2)
    position = ParagraphStyle("position", parent=styles["Normal"], fontName="ArialEmbedded", fontSize=10.4, leading=12, alignment=TA_CENTER, spaceAfter=2)
    contact = ParagraphStyle("contact", parent=styles["Normal"], fontName="ArialEmbedded", fontSize=9.2, leading=11, alignment=TA_CENTER, spaceAfter=6)
    body = ParagraphStyle("body", parent=styles["Normal"], fontName="ArialEmbedded", fontSize=9.9, leading=12.1, alignment=TA_LEFT, spaceAfter=2)
    heading = ParagraphStyle("heading", parent=styles["Normal"], fontName="ArialEmbedded-Bold", fontSize=11, leading=13, textColor=BLUE, spaceBefore=4, spaceAfter=2)
    role = ParagraphStyle("role", parent=styles["Normal"], fontName="ArialEmbedded-Bold", fontSize=10.1, leading=12, spaceBefore=3, spaceAfter=0.5)
    detail = ParagraphStyle("detail", parent=styles["Normal"], fontName="ArialEmbedded", fontSize=9.4, leading=11.2, textColor=GRAY, spaceAfter=1)
    bullet = ParagraphStyle("bullet", parent=styles["Normal"], fontName="ArialEmbedded", fontSize=9.65, leading=11.7, leftIndent=9, firstLineIndent=-5.5, bulletIndent=0, spaceAfter=1)
    skill = ParagraphStyle("skill", parent=styles["Normal"], fontName="ArialEmbedded", fontSize=9.6, leading=11.6, spaceAfter=1.3)

    story = [
        Paragraph("GIOIA ZHENG", title),
        Paragraph("M.Sc. Computer Science · Reinforcement Learning · Computer Vision · Reproducible ML", position),
        Paragraph("Darmstadt, Germany · <link href='mailto:gioia.zheng@stud.tu-darmstadt.de' color='black'>gioia.zheng@stud.tu-darmstadt.de</link> · +49 163 7322499 · <link href='https://github.com/GioiaZheng' color='black'>github.com/GioiaZheng</link> · <link href='https://gioiazheng.github.io/' color='black'>gioiazheng.github.io</link>", contact),
        Paragraph("Computer science master's student with hands-on projects in reinforcement learning, handwriting recognition and NLP evaluation. Currently starting an IAS robot-learning project, with experience in Python, PyTorch, testing and reproducible experiments.", body),
    ]

    def add_heading(text):
        story.append(Paragraph(text, heading))
        story.append(HRFlowable(width="100%", thickness=0.45, color=RULE, spaceBefore=0, spaceAfter=1.4))

    def add_role(item, separate_meta=False):
        title_markup = item['title']
        if item.get('url'):
            title_markup = f"<link href='{item['url']}' color='black'>{item['title']}</link>"
        if separate_meta:
            story.append(Paragraph(title_markup, role))
            story.append(Paragraph(item['meta'], detail))
        else:
            story.append(Paragraph(f"{title_markup} &nbsp;&nbsp;<font name='ArialEmbedded' color='#000000'>{item['meta']}</font>", role))
        if item["detail"]:
            story.append(Paragraph(item["detail"], detail))
        for text in item["bullets"]:
            story.append(Paragraph(f"•&nbsp;&nbsp;{text}", bullet))

    add_heading("EDUCATION")
    story.append(Paragraph("<b>TU Darmstadt</b>", role))
    story.append(Paragraph("M.Sc. Computer Science · Enrolled, Winter Semester 2026/27", detail))
    story.append(Paragraph("<b>Selected for Robot Learning: Integrated Project - Part 1</b> (20-00-0753-pj), WiSe 2026/27", detail))
    story.append(Paragraph("Project (ongoing): <i>Learning Amphibious Legged Locomotion</i>", detail))
    story.append(Paragraph("Intelligent Autonomous Systems (IAS) Lab · Course instructor: Prof. Jan Peters", detail))
    story.append(Paragraph("Project supervisors: Henrik Metternich, Davide Molinaroli, Sucheth Shenoy", detail))
    story.append(Paragraph("<b>Sapienza University of Rome</b>", role))
    story.append(Paragraph("B.Sc. Applied Computer Science and Artificial Intelligence · Expected Dec 2026", detail))
    for section_name, items in SECTIONS:
        add_heading(section_name)
        for item in items:
            add_role(item, separate_meta=(section_name == "RESEARCH AND ENGINEERING EXPERIENCE"))
    add_heading("OPEN SOURCE CONTRIBUTIONS")
    for text in OPEN_SOURCE:
        story.append(Paragraph(f"•&nbsp;&nbsp;{text}", bullet))
    add_heading("TECHNICAL SKILLS")
    for label, value in SKILLS:
        story.append(Paragraph(f"<b>{label}:</b> {value}", skill))
    doc.build(story)


if __name__ == "__main__":
    build_pdf()
    print(PDF)
