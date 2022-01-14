

import numpy as np
import cv2
import time
import webbrowser
import speech_recognition as sr
import os
import sys

print("hello")
print("")
img = cv2.imread('car2.jpg')
blank = np.zeros((img.shape[0], img.shape[1], 3), dtype='uint8')

(h, w, d) = img.shape  # returns weight, height, and channels
img = cv2.resize(img, (w // 2, h // 2))
M = cv2.getRotationMatrix2D((w // 2, h // 2), 90, 2)

print(M)
print("")

rotate_img = cv2.warpAffine(img, M, (w, h))
cv2.imshow('gray img', rotate_img)

gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('gray img', gray_img)

ret, threshold_img = cv2.threshold(gray_img, 120, 130, 0)
cv2.imshow('threshold img', threshold_img)


# blank[:] = (0, 255, 0)
# img = cv2.resize(img, (img.shape[1]//2, img.shape[0]//2))
# img = cv2.GaussianBlur(img, (21, 21), 0)
# body = cv2.CascadeClassifier('cars.xml')
# results = body.detectMultiScale(gray_img, scaleFactor=1.1, minNeighbors=4)


# img = cv2.Canny(img, 60, 60)
# print('s', end=)
# for (x, y, w, h) in results:
# img = cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), thickness=3)
# time.sleep(1)
# img = cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), thickness=3)
# img = cv2.bitwise_and(img, blank)
# img = cv2.bitwise_or(img, blank)
# print(x, y, w, h)
# img = cv2.putText(img, "Human", (x - 10, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.4, 255)
# img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# cv2.imshow('find body', img)
# cv2.imshow('face', img[200:400, 200:400])
# cv2.imshow('bgr2gray', img)

# img = cv2.dilate(img, kernel, iterations=1)
# img = cv2.erode(img, kernel, iterations=1)
# img = cv2.flip(img, 1)
# acc += 1
# img = rotate(img, acc)


# img = orm(img, acc, acc)
# img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
# b, g, r = cv2.split(img)
# img = cv2.merge([g, b, g])


cv2.waitKey(0)
