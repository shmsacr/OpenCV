import cv2


image = cv2.imread("filtreleme.jpg")

meanFilter = cv2.blur(image,(5,5))
meanFilter2 = cv2.blur(image,(10,10))
#filtrelemek istenen fotoğrafı belirlediğimiz matris boyutunda seçer ve ortalamasını alır
#doğrusal filtreleme çeşididir

mediamFilter = cv2.medianBlur(image,3)
mediamFilter2 = cv2.medianBlur(image,5)
#mediam filtre matrisi küçükten büyüğe sıralar ortaki değeri ortalama olarak alır

gauss = cv2.GaussianBlur(image,(3,3),0)
#gürültüyü azaltır

cv2.imshow("orjinal resim", image)

cv2.imshow("meanFilter",meanFilter)
cv2.imshow("meanFilter 10*10",meanFilter2)

cv2.imshow("Median Filter,", mediamFilter)
cv2.imshow("Median Filter5*5,", mediamFilter2)

cv2.imshow("Gauss Filtreleme", gauss)



cv2.waitKey(0)
cv2.destroyAllWindows()