import cv2
import numpy as np


img = cv2.imread("image.jpg",0)

ret,thresh1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
ret,thresh2 = cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)
ret,thresh3= cv2.threshold(img,127,255,cv2.THRESH_TRUNC)
ret,thresh4 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO)
ret,thresh5 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO_INV)

#2. parametre belirlenen pixel değerinin altındakiler 0 a yuvarlandı
#3. parametre belirlenen pixel değerinin üstünde olanlar ise 255 e yuvarlanır





cv2.imshow("Orjinal", img)
cv2.imshow("Thresh", thresh1)
cv2.imshow("Thresh2", thresh2)
cv2.imshow("Thresh3",thresh3)
cv2.imshow("Thresh4",thresh4)
cv2.imshow("Thresh5",thresh5)


cv2.waitKey(0)
cv2.destroyAllWindows()
