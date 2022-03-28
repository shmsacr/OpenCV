import cv2
import numpy as np

image = cv2.imread("LM.jpg")

kesit = image[50:200,200:400] #istenen kesit bölgesini başka bir değişkene atıldı
print(image.shape)

image[0:150,0:200] = kesit #kesilen bölgeyi ana resimdeki yere yapıştırıldı

image[100:200,100:300] = (25,125,225)#resmin bir alanını boyama

cv2.imshow("LEO MESSI",image)

cv2.waitKey(0)
cv2.destroyAllWindows()