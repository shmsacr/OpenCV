import cv2
import numpy as np

image = cv2.imread("deb.jpg")

aynalananResim = cv2.copyMakeBorder(image,100,100,200,400,cv2.BORDER_REFLECT)
#resmi aynalamak için kullanılan fonksiyonlar ve metotlar
uzatilanResim = cv2.copyMakeBorder(image,120,120,120,120,cv2.BORDER_REPLICATE)
tekrarEdilen = cv2.copyMakeBorder(image,100,100,100,100,cv2.BORDER_WRAP)
sarilanResim = cv2.copyMakeBorder(image,50,50,50,50,cv2.BORDER_CONSTANT,value=(0,50,150) ) # value değeri çerçeceye renk verir


cv2.imshow("De Bruyne",aynalananResim)
cv2.imshow("De Bruyne uzatılan",uzatilanResim)
cv2.imshow("De Bruyne Tekrar",tekrarEdilen)
cv2.imshow("De Bruyne Cerceve",sarilanResim)
cv2.waitKey(0)
cv2.destroyAllWindows()