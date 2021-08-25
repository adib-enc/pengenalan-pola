# Operasi image pada Python 
# Instalasi paket open cv
# pip install opencv-contrib-python 

# pilihan load image (contoh logo ipb)
import matplotlib.pyplot as plt
import cv2
import numpy as np
import time

def readAndShowImg(fname):
    img = cv2.imread(fname)
    cv2.imshow("img", img)
    return img


print("read images using opencv")
five = cv2.imread("p-5.png")
print(five.shape)
print(five.size)

# cv2.imshow("ims", five)
plt.imshow(five)
cv2.waitKey(0)

img = cv2.imread("ipb.png")
# cv2.imshow("img", img)
plt.imshow(img)

img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# cv2.imshow("img", img)
plt.imshow(img)

# mengambil nilai matriksnya
# acces pixel of images per postion 
pixels = five[100,100]
print(pixels)