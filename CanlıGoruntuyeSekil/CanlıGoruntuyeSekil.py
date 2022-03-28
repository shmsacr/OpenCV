import cv2
import numpy as np

kamera = cv2.VideoCapture(0)

while True:
    ret,goruntu = kamera.read()
    
    cv2.rectangle(goruntu,(250,250),(300,400),(0,0,255),2)
    cv2.line(goruntu,(0,0),(100,100),(255,0,0),5)
    cv2.imshow("Kamera Goruntu",goruntu)
    
    if cv2.waitKey(25) & 0xFF == ord("q"):
        break
        
kamera.release()

cv2.destroyAllWindows()