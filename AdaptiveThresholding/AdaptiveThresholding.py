import cv2



img = cv2.imread("image.jpg",0)

#Simple Threshholding
ret,thresh1 = cv2.threshold(img,160,255,cv2.THRESH_BINARY)

#Adaptive ThreshHolding bölgesellendirme eşik değeri 
thresh2 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,\
                                cv2.THRESH_BINARY,11,2)

thresh3 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
                                cv2.THRESH_BINARY,11,2)                               

cv2.imshow("Orjinal", img)
cv2.imshow("Thresh1",thresh1)
cv2.imshow("THRESH2 MEAN", thresh2)
cv2.imshow("THRESH3 Gauss",thresh3)


cv2.waitKey(0)
cv2.destroyAllWindows()
