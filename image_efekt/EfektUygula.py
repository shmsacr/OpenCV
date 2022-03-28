import cv2
import numpy as np

cr = cv2.imread("cr.jpg")


cr[20:100,100:200,0] = 255



cv2.imshow("CRİSTİONA RONALDO",cr)



cv2.waitKey(0) # sabit pencere
cv2.destroyAllWindows() # arkada çalışan projeyi kapatır