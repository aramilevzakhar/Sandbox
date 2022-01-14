import numpy as np
import cv2
#import easyocr

#import easyocr as es
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

#cap = cv2.VideoCapture('input.mp4')
#cap = cv2.VideoCapture(0)
img = cv2.imread('image.jpg')
#acc = 0
#success, img = cap.read()
#img = cv2.resize(img, (img.shape[1]//2, img.shape[0]//2))
#img = cv2.GaussianBlur(img, (9, 9), 0)
g1 = cv2.medianBlur(img, 7)
#cv2.imshow('medianBlur', g1)




gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#cv2.imshow('BGR2GRAY', gray)
#ret, thresh = cv2.threshold(gray, 125, 255, cv2.THRESH_BINARY)
#cv2.imshow('threshold', thresh)
w, h = img.shape[:2]
blank = np.zeros((w, h, 3), dtype='uint8')

circle = cv2.circle(blank.copy(), (200, 200), 43, 200, -1)
cv2.imshow('circle', circle)
#cv2.imshow('bitwise_and', btw)
faces = cv2.CascadeClassifier('faces1.xml')
results = faces.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=3)

acc = 0
for (x, y, w, h) in results:
    print(x, y, w, h)
    #circle = cv2.circle(blank.copy(), (x, y), w, (0, 255, 9), -1)
    #img = cv2.bitwise_and(img, circle)    
    #cv2.bitwise_and()
    blank = cv2.rectangle(blank, (x, y), (x+w, y+h), (0, 255, 0), thickness=-1)
    blank = cv2.bitwise_and(img, blank)
    acc +=1
print(acc)

cv2.imshow('blanc', blank)
#cv2.imshow('face', img)
cv2.waitKey(0)

#img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#img = cv2.Canny(img, 1, 1)
#kernel = np.ones((5, 5), np.uint8)
#img = cv2.dilate(img, kernel, iterations=1)
#img = cv2.erode(img, kernel, iterations=1)
#img = cv2.flip(img, 1)
#acc += 1
#img = rotate(img, acc)
#img = transform(img, acc, acc)
#img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
#b, g, r = cv2.split(img)
#img = cv2.merge([g, b, g])

#if cv2.waitKey(1) & 0xFF == ord('q'):
#    break









