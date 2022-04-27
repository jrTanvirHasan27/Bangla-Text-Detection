import numpy as np
import os
import cv2
import pytesseract
from PIL import Image, ImageDraw, ImageFont

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
img = cv2.imread('9.png')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

##  Detecting Characters
# print(pytesseract.image_to_boxes(img, lang='ben'))
# hImg,wImg,_  = img.shape
# boxes = pytesseract.image_to_boxes(img, lang='ben')
# for b in boxes.splitlines():
#    #print(b)
#    b = b.split(' ')
#    print(b)
#    x, y, w, h = int(b[1]), int(b[2]), int(b[3]), int(b[4])
#    cv2.rectangle(img, (x, hImg-y), (x+w, hImg-h), (0, 0, 255), 1)
#   cv2.putText(img, b[0], (x, hImg-y+30), cv2.FONT_HERSHEY_COMPLEX, 1, (50,50,255), 1)



hImg, wImg, _ = img.shape
boxes = pytesseract.image_to_data(img, lang='ben')
print(pytesseract.image_to_string(img, lang='ben'))

for x, b in enumerate(boxes.splitlines()):
    if x != 0:
        b = b.split()
        print(b)
        if len(b) == 12:
            x, y, w, h = int(b[6]), int(b[7]), int(b[8]), int(b[9])
            cv2.rectangle(img, (x, y), (x + w, h + y), (0, 0, 255), 1)
            # cv2.putText(img, b[11], (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.7, (50, 50, 255))

            fontpath = "C:\\Users\\jrtan\\Downloads\\kalpurush.ttf"
            font = ImageFont.truetype(fontpath, 14)
            img_pil = Image.fromarray(img)
            draw = ImageDraw.Draw(img_pil)
            draw.text((x, y + 40), b[11], font=font, fill=(0, 0, 255))
            img = np.array(img_pil)
            # cv2.putText(img, b[11], (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.7, (50, 50, 255))

test_img_path = "/Users/jrtan/PycharmProjects/Bangla Text Detection"
create_path = lambda f : os.path.join(test_img_path, f)

image_path = "9.png"
path = create_path(image_path)
file_save_path = "/Users/jrtan/PycharmProjects/Bangla Text Detection/Pdf"

pdf = pytesseract.image_to_pdf_or_hocr(path, extension='pdf')

file = open(os.path.join(file_save_path, "pdf-content.pdf"), 'w+b')
file.write(pdf)
file.close()


cv2.imshow('Result', img)
cv2.waitKey(0)
