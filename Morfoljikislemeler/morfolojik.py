import cv2
import numpy as np

image = cv2.imread("adsiz.png")

kernel = np.ones((5,5),np.uint8)

dilation = cv2.dilate(image,kernel,iterations = 1)
#gürültüyü genişletir
erosion = cv2.erode(image,kernel,iterations = 1)
#aşındırma işlemi
dilation_erosion = cv2.dilate(erosion,kernel,iterations = 2)
#iterations artıkça işlem artar

opening = cv2.morphologyEx(image,cv2.MORPH_OPEN,kernel)
#opening morgphology dilation + erosion yapar
closing = cv2.morphologyEx(image,cv2.MORPH_CLOSE,kernel)

cv2.imshow("orjinal",image)
cv2.imshow("Dilation", dilation)
cv2.imshow("erosion", erosion)
cv2.imshow("Dilation_erosion", dilation_erosion)
cv2.imshow("opening", opening)
cv2.imshow("Closing", )

cv2.waitKey(0)
cv2.destroyAllWindows