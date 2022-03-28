import cv2
import numpy as np

image = cv2.imread("cr.jpg")
ikikatB = cv2.pyrUp(image)
ikikatK = cv2.pyrDown(image)

cv2.imshow("Orjinal CR", image)
cv2.imshow("İkikat",ikikatB)
cv2.imshow("iki kat kücük",ikikatK)

cv2.waitKey(0)
cv2.destroyAllWindows()