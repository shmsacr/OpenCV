import cv2
import numpy as np

image = cv2.imread("BB.png")

image[100,200] = [255,255,255] #girdiğimiz değeri başka bir bgr değeriyle değişti



for i in range(500): #Resime 100 piksel boyutunda çizgi çekme
    image[70,i] = [255,255,255]

cv2.imshow("BB",image)


cv2.waitKey(0)
cv2.destroyAllWindows()