import cv2 
import numpy as np

image = cv2.imread("resim.png") # kullanacağımız resimi çekme, 2. parametre renk tonu

cv2.imshow("DERS1",image)#çektiğimiz resmi gösterme
cv2.imwrite("newimage.png",image)

print(image.size) # resimin matris boyutu
print(image.dtype)#resim veri tipi
print(image.shape)#resim şekli
cv2.waitKey(0)
cv2.destroyAllWindows() # resimle alakalı tum verileri kapatır
