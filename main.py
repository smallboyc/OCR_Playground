from pprint import pprint
import schedule
import time
from app.utils import *
from app.data_manager import *
from app.ocr import process_image_with_ocr
from PIL import Image, ImageEnhance, ImageOps

if __name__ == "__main__":
    data = get_data()
    # pprint(data)
    file = "img/img_00.jpg"
    # Opening Image
    im = Image.open(file)

    # Appliquer la correction d'orientation basée sur EXIF
    im = ImageOps.exif_transpose(im)

    # Conversion en niveaux de gris
    greyscale = im.convert("L")
    greyscale.show()

    # Ajustement de la luminosité et du contraste
    im3 = ImageEnhance.Brightness(greyscale)
    im3 = im3.enhance(1.5)
    im4 = ImageEnhance.Contrast(im3)
    im4 = im4.enhance(3.0)
    im5 = ImageEnhance.Brightness(im4)
    im5 = im5.enhance(1.0)

    # OCR sur l'image originale
    print("Classic OCR")
    process_image_with_ocr(im)

    # OCR sur l'image modifiée
    print("OCR with edition")
    process_image_with_ocr(im5)

# try to update ecobalyse data -> every day
# schedule.every().week.at("00:00").do(update_data)

# while True:
#     schedule.run_pending()
#     time.sleep(1)
