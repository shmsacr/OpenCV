import cv2
import numpy as np

camera = cv2.VideoCapture(0)

width = int(camera.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(camera.get(cv2.CAP_PROP_FRAME_HEIGHT))
#kamerada ki görüntünün yüksekliğini ve genişliğini tutmak

print(width,height)

#format belirledik
fourcc =cv2.VideoWriter_fourcc(*'MP4V')

writer = cv2.VideoWriter("kayit.mp4",fourcc,20,(width,height))
#3. parametre video hızını belirler

while True:
    ret,frame = camera.read()
    writer.write(frame)
    cv2.imshow("Video",frame)
    
    if cv2.waitKey(25) & 0xFF == ord("q"):
        break
    
camera.release()
writer.release()
cv2.destroyAllWindows()    