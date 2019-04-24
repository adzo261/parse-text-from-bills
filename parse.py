from PIL import Image
import re
from pytesseract import image_to_string


def parse_bill(image):
    data = image_to_string(Image.open(image)).split()
    i1, i2 = -1, -1
    for i in range(len(data)):
        if data[i] == "PBoy:":
            i1 = i-1
        if data[i] == "GST":
            i2 = i-1
            break
    print(f'Total amount is Rs: {data[i2]} for Bill No:{data[i1]}')


parse_bill('billd1.png')
parse_bill('billd2.png')
parse_bill('billnod.png')
