import cv2
import numpy as np
import time
import math
import Hand_Tracking_Module as htm



 
########################
wCam, hCam = (640, 480)
########################


cap = cv2.VideoCapture(0)

cap.set(3, wCam)
cap.set(4, hCam)
pTime = 0

detector = htm.handDetector(detectionCon=0.7)


while (True):
    success, img = cap.read()
    detector.findHands(img)
    lmList = detector.findPosition(img, draw=False) # get coords my hand
    if len(lmList[0]) != 0:

        #print(lmList[0][4], lmList[0][8])
        # get coords for thumb and forenger
        x1, y1 = lmList[0][4][1], lmList[0][4][2]
        x2, y2 = lmList[0][8][1], lmList[0][8][2]
        # get coords for center line 
        cx, cy = (x1+x2)//2, (y1+y2)//2

        length = math.hypot((x1-x2), (y1-y2))
        print(length)


        cv2.circle(img, (x1, y1), 20, (0, 255, 0), cv2.FILLED)
        cv2.circle(img, (x2, y2), 20, (0, 255, 0), cv2.FILLED)
        cv2.line(img, (x1, y1), (x2, y2), (0, 0, 0), 3)
        cv2.circle(img, (cx, cy), 20, (0, 255, 0), 2)

    cTime = time.time()
    fps = 1/(cTime - pTime)
    pTime = cTime
    img = cv2.putText(img, f'fps: {int(fps)}', (100, 100), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 2)
    cv2.imshow('img', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break






