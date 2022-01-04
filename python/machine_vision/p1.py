import numpy as np
import cv2
import skimage
# Importing Necessary Libraries
#from skimage import data
#from skimage.color import rgb2gray
#import matplotlib.pyplot as plt
#img = cv2.imread("mult.jpg", 1)  # image reading
img = cv2.imread('mult.jpg')  # image reading
# converting it into Hue, saturation, value (HSV)
print("hello wo")
# Convert BGR to HSV
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)  
t1 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
t2 = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
#cv2.imshow('hsv', hsv)
#cv2.imshow('window1', t1)
#cv2.imshow('window2', t2)
# the : in an array in python means that we're going to slice that part of the array
print(hsv)
# hue
h = hsv[:, :, 0]
# saturation
s = hsv[:, :, 1]
# value
v = hsv[:, :, 2]
#for it in range(len(h)):
#    print(f'{it}: {h[it]}')
#print(f'len: {len(h)}')
#print(h,s,v,sep='\n')
a = np.array([[1, 2], [3, 4]])
a2 = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6]])
print(np.concatenate((a, a2), axis=1))
#hsv_split = np.concatenate((h, s, v), axis=1)
#print(hsv_split)
#cv2.imshow("Split hsv", hsv_split) 
#  some of the values require multiple variables, hence why ret is shown multiple times
#ret, min_sat = cv2.threshold(s, 40, 255, cv2.THRESH_BINARY)
#  showing an image is very simple, first argument is the name, second is the image we wish to show
#cv2.imshow("Sat filter", min_sat) 
#ret, max_hue = cv2.threshold(h, 15, 255, cv2.THRESH_BINARY_INV)  # will do the inverse of the normal threshold
#cv2.imshow("Hue filter", max_hue)
# the final image is the min saturation and the max hue put together
#final = cv2.bitwise_and(min_sat, max_hue)
#cv2.imshow("Final", final)
#cv2.imshow("Original image", img)
#  the windows will display until a key is pressed, this is using key characters, in this case we're using escape, which is 27 but 0 also works
#  destroy all windows will prevent you from having to mass spam the kill keys
#arr = np.array([1, 2, 3, 4, 5, 6, 7, 3 ,22, 342, 3])
#print(arr[:4:])
start_point = (5, 5)
end_point = (220, 220)
color = (255, 0, 0)
thinkness = 2
image = cv2.rectangle(img, start_point, end_point, color, thinkness)
# Here we drawn circle and rectangle
#cv2.imshow('rectangle', image)
center_point = (120, 50)
radius = 30
color = (10, 230, 10)
thinkness = -1
image = cv2.circle(img, center_point, radius, color, thinkness)
#cv2.imshow('circle', image)
cv2.waitKey(0)
#cv2.destoryAllWindows()
