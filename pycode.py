import cv2 # importing cv2 library
import pytesseract as tess
tess.pytesseract.tesseract_cmd = r'C:\Users\Dell\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'
from PIL import Image
from gtts import gTTS
import os	
from pytesseract.pytesseract import Output
import numpy as np
url= 'http://192.168.0.101:8080/video'
cam = cv2.VideoCapture(url)
count = 0
while True:
    ret, img = cam.read()

    cv2.imshow("Test", img)
    if not ret:
        break
    k=cv2.waitKey(1)
    if k%256==27:
        #For Esc key
        print("Close")
        break
    elif k%256==32:
        #For Space key
        print("Image "+str(count)+"saved")
        file='C:/Users/Dell/Desktop/blind reader/img'+str(count)+'.jpg'
        cv2.imwrite(file, img)
        count +=1
cam.release
cv2.destroyAllWindows
img = Image.open('img0.jpg')
text = tess.image_to_string(img)
print(text)
outfile = open("test.txt",'w')
outfile.write(text)
outfile.close()
fh = open("test.txt",'r')
mytext=fh.read().replace("\n"," ")
language='en'
output=gTTS(text=mytext, lang=language, slow=False)
output.save("out.mp3")
fh.close()
os.system("start out.mp3")
