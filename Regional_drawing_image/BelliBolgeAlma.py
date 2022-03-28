import cv2
import numpy as np

image = cv2.imread("Bolgesel.jpg")

cv2.rectangle(image,(200,200),(300,100),[0,0,255],3,)
#1. parametre oynanaccak resim
#2. parametre çizilecek karenin sol alt köşesinin kordinatı ( x ,y) cinsinden
#3. parametre çizilecek karenin sağ üst köşesinin kordinatı ( x ,y) cinsinden
#4. parametre çizlecek karenin kenar rengi
#5. parametre çizilecek karenin kenar kalınlığı
cv2.imshow("Hababam",image)


cv2.waitKey(0)
cv2.destroyAllWindows()