#import cv2
#import time
#cap = cv2.VideoCapture(0)
#pTime = 0
#
#
#while True:
#    success, img = cap.read()
#    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
#    cTime = time.time()
#    fps = 1 / (cTime - pTime)
#    pTime = cTime
#    cv2.putText(img, f'FPS:{int(fps)}', (20, 70), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
#
#    cv2.imshow("Test", img)
#    cv2.waitKey(0)



import cv2
import mediapipe as mp
import time

cap = cv2.VideoCapture(0)

mpHands = mp.solutions.hands
hands = mpHands.Hands(static_image_mode=False,
                      max_num_hands=2,
                      min_detection_confidence=0.5,
                      min_tracking_confidence=0.5)
print(mp.solutions.hands)
mpDraw = mp.solutions.drawing_utils


pTime = 0
cTime = 0    



while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    
    #print(results.multi_hand_landmarks)
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            #print(handLM)
            for id, lm in enumerate(handLms.landmark):
                
                #print(id,lm)
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                #if id ==0:
                #cv2.circle(img, (cx,cy), 3, (255,0,255), cv2.FILLED)
                cv2.circle(img, (cx,cy), 3, (255,0,255))

            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)

    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime

    cv2.putText(img, str(int(fps)), (10,70), cv2.FONT_HERSHEY_PLAIN, 3, (255,0,255), 3)

    cv2.imshow("Image", img)
    if cv2.waitKey(1) & 0xFF ==  ord('q'):
        break


















