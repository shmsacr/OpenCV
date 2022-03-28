import cv2
import numpy as np

image = cv2.imread("neymar.jpg")
grilesmisResim = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

yukseklik,genislik,kanalSayisi = image.shape
print("Orjinal",yukseklik,genislik,kanalSayisi)
#resim grilesince kanal sayisi 1 e düser

yukseklik1,genislik1 = grilesmisResim.shape
print("Grilestirmis Resim", yukseklik1,genislik1)


cv2.imshow("Neymar",image)
cv2.imshow("Grilesmis",grilesmisResim)

cv2.waitKey(0)
cv2.destroyAllWindows()
