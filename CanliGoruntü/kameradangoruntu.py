import cv2 
import numpy as np


kamera = cv2.VideoCapture(0)#0 dendiğinde pc de ki kamera
#1 olduğunda usb e takılı olan kamera
#2 olunca harici bir video çeker

while True:
    ret,goruntu = kamera.read()
    #ret kameranın açık olup olmadığını kontrol eder
    cv2.imshow("Kamera",goruntu)
    
    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

kamera.release() #kamerayı serbest bıraktı
cv2.destroyAllWindows()    