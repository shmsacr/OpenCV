import cv2 
import numpy as np

img = cv2.imread("image.jpg")
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) # resmi grileştirme
blur = cv2.GaussianBlur(gray,(3,3),0)


def autoCanny(blur,sigma = 0.33):
    median= np.median(blur)
    lower = int(max(0,(1.0-sigma)*median))
    upper = int(min(255,(1.0+sigma)*median))
    
    canny = cv2.Canny(blur,lower,upper)
    
    
    return canny
    
wide = cv2.Canny(blur,10,220) # geniş eşik değerli
tight = cv2.Canny(blur,200,300) # dar eşik değerli


auto = autoCanny(blur)



cv2.imshow("Orjinal",img)
cv2.imshow("Blurred İmage",blur)

cv2.imshow("Kenarlar",np.hstack([wide,tight,auto]))


cv2.waitKey(0)
cv2.destroyAllWindows()
