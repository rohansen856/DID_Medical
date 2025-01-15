import base64
import os
from io import BytesIO

import pytesseract
from PIL import Image, ImageOps


def do_ocr(b64image):
    image = Image.open(BytesIO(base64.b64decode(b64image)))

    
    gray_image = ImageOps.grayscale(image)

    scale_factor = 2
    resized_image = gray_image.resize(
        (gray_image.width * scale_factor, gray_image.height * scale_factor),
        resample=Image.LANCZOS
    )

    improved_text = pytesseract.image_to_string(resized_image)

    print(improved_text)

    return improved_text
    # resized_image.save('preprocessed_image.jpg')