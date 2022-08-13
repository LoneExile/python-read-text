import fitz
from pdf_annotate import Appearance, Location, PdfAnnotator

a = PdfAnnotator("test.pdf")
a.add_annotation(
    "square",
    Location(x1=50, y1=50, x2=100, y2=100, page=0),
    Appearance(stroke_color=(1, 0, 0), stroke_width=1),
)
a.write("output.pdf")

doc = fitz.open("output.pdf")
page = doc[0]

rect = page.first_annot.rect

print(page.get_textbox(rect))

# not work
# import fitz

# doc = fitz.open("./test.pdf")
# for page in doc:
#     page.draw_rect([1, 1, 100, 100], color=(0, 1, 0), width=2)
# doc.save("./output.pdf")
