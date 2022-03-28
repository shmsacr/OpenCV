import cv2
import numpy as np

image = cv2.imread("BB.png")

cv2.imshow("BB",image)
print(image[(230,80)])#sol köşesi referans alınarak yazlıan konumadaki piksel çağırılır


print("resmin boyutu:"+ str(image.size))
print("Resmin Özelliği:"+ str(image.shape))
print("Resmin Veri tip:"+ str(image.dtype))

cv2.waitKey(0)
cv2.destroyAllWindows()