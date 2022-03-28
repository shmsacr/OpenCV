import cv2
import numpy as np

degea = cv2.imread("degea.jpg")
don = cv2.imread("don.jpg")


cv2.imshow("Degea",degea)
cv2.imshow("Don",don)

toplam = cv2.add(degea,don)
agirlikliToplama = cv2.addWeighted(degea,0.4,don,0.6,0)
#Agırlıklar toplanarak yeni resim oluşturuldu
#♠son parametreye 0 verilir


cv2.imshow("Toplanmis Resimler",toplam)
cv2.imshow("Agirlikli Toplama",agirlikliToplama)
cv2.waitKey(0)
cv2.destroyAllWindows()