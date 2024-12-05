import pytesseract
from PIL import Image, ImageEnhance
# import cv2


# OCR
def process_image_with_ocr(image: any) -> None:
    # image = cv2.imread(image_path)
    extracted_text = pytesseract.image_to_string(image)
    print(f"Extract text : {extracted_text}")
