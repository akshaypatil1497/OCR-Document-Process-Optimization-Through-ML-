import easygui
from pdf2image import convert_from_path

pdfs = easygui.fileopenbox()
pages = convert_from_path(pdfs, dpi=300, poppler_path='C:\\Program Files (x86)\\poppler-0.68.0\\bin')

i = 1
for page in pages:
    image_name = "Page_" + str(i) + ".jpg"
    page.save(image_name, "JPEG")
    i = i + 1
