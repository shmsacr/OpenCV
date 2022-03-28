import cv2
import numpy as np

resim = np.zeros((300,300,3),dtype = "uint8")
img = np.zeros((1920,1920,3),dtype ="uint8")
cv2.line(resim,(0,0),(100,10),(0,0,255),2)
#1. parametre çizgi çekilecek resim
#2. parametre çizginin başlangıç konumu
#3. parametre çizginin bitiş konumu
#4. parametre çizginin rengi
#5. parametre çizginin kalınlığı

cv2.circle(resim,(250,250),25,(0,255,0),3)
#daire oluşturmma
for i in range(0,1000):
    i +=10
    for j in range(100,1000):
        cv2.rectangle(img,(i,0),(j,10),(0,0,255),3)
        j +=10

cv2.putText(resim,"Sehmus ACAR",(15,50),cv2.FONT_HERSHEY_COMPLEX,1,(255,0,0),1)
cv2.imshow("Deneme", resim)
cv2.imshow("Tam boyut",img)


cv2.waitKey(0)
cv2.destroyAllWindows()