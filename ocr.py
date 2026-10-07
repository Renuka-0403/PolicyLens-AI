import pytesseract
import fitz
from PIL import Image, ImageEnhance, ImageFilter
import io
pytesseract.pytesseract.tesseract_cmd = (
    r"C:\Program Files\Tesseract-OCR\tesseract.exe"
)
def preprocess_image(image):
    image = image.convert("L")
    image = ImageEnhance.Contrast(image).enhance(1.5)
    image = image.filter(ImageFilter.SHARPEN)
    return image
def extract_text_from_image(file):
    image = Image.open(file)
    image = preprocess_image(image)
    text = pytesseract.image_to_string(
        image,
        config="--psm 6"
    )
    return text
def extract_text_from_pdf(file):
    pdf_bytes = file.read()
    document = fitz.open(
        stream=pdf_bytes,
        filetype="pdf"
    )
    text = ""
    for page in document:
        pix = page.get_pixmap(
            matrix=fitz.Matrix(2, 2)
        )
        image = Image.open(
            io.BytesIO(
                pix.tobytes("png")
            )
        )
        image = preprocess_image(image)
        page_text = pytesseract.image_to_string(
            image,
            config="--psm 6"
        )
        text += page_text
        text += "\n\n"
    document.close()
    return text
def extract_text(file):
    file_name = file.name.lower()
    if file_name.endswith(".pdf"):
        return extract_text_from_pdf(file)
    if file_name.endswith(
        (".png", ".jpg", ".jpeg")
    ):
        return extract_text_from_image(file)
    return ""