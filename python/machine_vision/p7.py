import cv2
import numpy as np

img_rgb = cv2.imread('123.png')
template = cv2.imread('1.png')
w, h = template.shape[:-1]


arr = np.array([1, 2, 3, 4, 5])
#print(arr[:-1])
print(np.where(arr < 2))


res = cv2.matchTemplate(img_rgb, template, cv2.TM_CCOEFF_NORMED)
threshold = .28
print(res)
loc = np.where(res >= threshold)
print(len(loc
          ))
#print(loc)
for pt in zip(*loc[::-1]):  # Switch collumns and rows
    cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (255, 0, 0), 1)

cv2.imwrite('result.png', img_rgb)
cv2.imshow('helll', img_rgb)
cv2.waitKey(0)




















