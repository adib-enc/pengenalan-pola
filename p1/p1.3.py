# Operasi image pada Python 
# Instalasi paket open cv
# pip install opencv-contrib-python 

# pilihan load image (contoh logo ipb)
import matplotlib.pyplot as plt
import cv2
import numpy as np

print("read images using opencv")
five = cv2.imread("p-5.png")
print(five.shape)
print(five.size)
plt.imshow(five)
cv2.waitKey(0)

im = cv2.imread("ipb.png")
plt.imshow(im)

im = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
plt.imshow(im)

# mengambil nilai matriksnya
# acces pixel of images per postion 
pixels = five[100,100]
print(pixels)