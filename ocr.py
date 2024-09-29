import cv2
import pytesseract
from PIL import Image
from transformers import TrOCRProcessor, VisionEncoderDecoderModel
from langdetect import detect
from langdetect.lang_detect_exception import LangDetectException
import pytesseract

# If Tesseract is not in your system PATH, specify its location
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\Atharv\AppData\Local\Programs\Tesseract-OCRtesseract.exe'  # Adjust the path if necessary


# Load Pretrained Model for OCR from Huggingface
processor = TrOCRProcessor.from_pretrained("microsoft/trocr-base-handwritten")
model = VisionEncoderDecoderModel.from_pretrained("microsoft/trocr-base-handwritten")

# Preprocess the image before OCR for better accuracy
def preprocess_image(image_path):
    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Adaptive thresholding for handwritten text
    thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
    return thresh

# OCR function using pytesseract for Hindi and English text extraction
def perform_ocr(image):
    custom_config = r'--oem 1 --psm 3'
    image = Image.open(image)
    text = pytesseract.image_to_string(image, lang='eng+hin', config=custom_config)
    return text

# Function to detect the language of extracted text
def detect_language(text):
    try:
        lang = detect(text)
        if lang == 'hi':
            return "Hindi"
        elif lang == 'en':
            return "English"
        else:
            return "Unknown"
    except LangDetectException:
        return "Unable to detect language"
