from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from io import BytesIO


def generate_pdf(mn, md, med, std, num):
    pdf = BytesIO()

    c = canvas.Canvas(pdf, pagesize=A4)

    c.setFont("Helvetica", 14)

    c.drawString(220 , 700 , "Mathematical Operations Results")
    c.drawString(110 , 660 , f"The Entered Numbers: {num}")
    c.drawString(110 , 640 , mn)
    c.drawString(110 , 620 , md)
    c.drawString(110 , 600 , med)
    c.drawString(110 , 580 , std)
    c.drawString(350 , 90 , "proprietor: CodeMaestro!")

    c.showPage()
    c.save()

    return pdf

#----------------------------------------------------------------------------------------#