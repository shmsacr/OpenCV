import cv2
import numpy as np

img1 = cv2.imread("1.png")
img2 = cv2.imread("2.png")


#beyaz rengi 1 siyah rengi 0 
bitwaise_and = cv2.bitwise_and(img1,img2)
bitwaise_or = cv2.bitwise_or(img1,img2)
bitwaise_xor = cv2.bitwise_xor(img1,img2)
bitwaise_not = cv2.bitwise_not(img1)
bitwaise_not2 = cv2.bitwise_not(img2)


cv2.imshow("image1",img1)
cv2.imshow("image2",img2)
cv2.imshow("Bitwaise AND", bitwaise_and)
cv2.imshow("Bitwaise OR", bitwaise_or)
cv2.imshow("Bitwaise XOR", bitwaise_xor)
cv2.imshow("Bitwaise NOT",bitwaise_not)
cv2.imshow("Bitwaise NOT",bitwaise_not2)


cv2.waitKey(0)
cv2.destroyAllWindows()