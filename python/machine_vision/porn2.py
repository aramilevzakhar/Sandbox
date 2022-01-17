import numpy as np
import cv2
import time

#photo = np.zeros((300, 300, 3), dtype='uint8')
#cv2.imshow('wi1', photo)

def rotate(img_p, angle):
    height, widht = img_p.Shape[:2]
    point = (widht//2, height//2)

    mat = cv2.getRotationMatrix2D(point, angle, 1)
    return cv2.warpAffine(img_p, mat, (widht, height))

def transform(img, x, y):
    mat = np.float32([[1, 0, x], [0, 1, y]])
    return cv2.warpAffine(img, mat, (img.Shape[1], img.Shape[0]))


cap = cv2.VideoCapture(0)
acc = 0



while True:
    success, img = cap.read()

    blank = np.zeros((img.shape[0], img.shape[1], 3), dtype='uint8')
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #blank[:] = (0, 255, 0)
    #img = cv2.resize(img, (img.shape[1]//2, img.shape[0]//2))
    #img = cv2.GaussianBlur(img, (21, 21), 0)
    #img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = cv2.CascadeClassifier('faces1.xml')
    results = faces.detectMultiScale(gray, scaleFactor=2, minNeighbors=5)
    #img = cv2.Canny(img, 60, 60)
    print(results)
    #print('s', end=)
    for (x, y, w, h) in results:
        #img = cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), thickness=3)
        #time.sleep(1)
        blank = cv2.rectangle(blank, (x, y), (x+w, y+h), (0, 255, 0), thickness=3)
        #img = cv2.bitwise_and(img, blank)
        img = cv2.bitwise_or(img, blank)
        #print(x, y, w, h)
        img = cv2.putText(img, "Human", (x - 10, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.4, 255)
        #img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #img = cv2.Canny(img, 1, 1)
    #kernel = np.ones((5, 5), np.uint8)
    #cv2.imshow('blank', blank)
    cv2.imshow('face', img)


    #img = cv2.dilate(img, kernel, iterations=1)
    #img = cv2.erode(img, kernel, iterations=1)
    #img = cv2.flip(img, 1)
    #acc += 1
    #img = rotate(img, acc)
    

    #img = orm(img, acc, acc)
    #img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    #b, g, r = cv2.split(img)
    #img = cv2.merge([g, b, g])

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break









