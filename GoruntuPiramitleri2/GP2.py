import cv2 as cv
import numpy as np


image = np.zeros((300,300,3),dtype="uint8")

print(image)
#görüntü için boş bir alan oluşturdu

cv.waitKey(0)
cv.destroyAllWindows()