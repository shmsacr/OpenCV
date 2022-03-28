import cv2
import numpy as np

image1 = cv2.imread("salah.jpg")
image2 = cv2.imread("alex.jpg")


print(image1[200,300])
print(image2[150,250])

cv2.imshow("SALAH", image1)
cv2.imshow("ALEX DE SOUZA", image2)

print(image1[200,300] + image2[150,250])

#toplanan bgr değerleri 255 değerini aşarsa devir atlar

cv2.waitKey(0)
cv2.destroyAllWindows()