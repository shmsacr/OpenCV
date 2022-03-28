import cv2

image = cv2.imread("image.jpg",0)
#değer seçme zorunluluğunu ortadan kaldırır otomatik belirler

#simple thresholding
ret1,thresh1 = cv2.threshold(image,125,255,cv2.THRESH_BINARY)

#otsu thresholding

ret2,thresh2 = cv2.threshold(image,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
#2 parametre min deperi , 3. parametre max değer belirlenir
#kendisi oto değer alır


cv2.imshow("Orjinal",image)
cv2.imshow("Simple Thresh",thresh1)
cv2.imshow("Otsu Thresh",thresh2)


cv2.waitKey(0)
cv2.destroyAllWindows()