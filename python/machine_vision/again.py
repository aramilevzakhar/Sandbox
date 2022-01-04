
import cv2
import numpy as np


#import ls

img = cv2.imread('mult.jpg')
#img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)



arr = np.array([13, 2, 43, 4, 95, 6, 74, 8, 9, 10, 11])
print(np.where(arr > 2))

cv2.imshow('speriance', img)
cv2.waitKey(0)



def draw_circles(img, circles):
    # img = cv2.imread(img,0)
    cimg = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)
    for i in circles[0,:]:
    # draw the outer circle
        cv2.circle(cimg,(i[0],i[1]),i[2],(0,255,0),2)
        # draw the center of the circle
        cv2.circle(cimg,(i[0],i[1]),2,(0,0,255),3)
        cv2.putText(cimg,str(i[0])+str(',')+str(i[1]), (i[0],i[1]), cv2.FONT_HERSHEY_SIMPLEX, 0.4, 255)
    return cimg

def detect_circles(image_path):
    gray = cv2.imread(image_path, cv2.CV_LOAD_IMAGE_GRAYSCALE)
    gray_blur = cv2.medianBlur(gray, 13)  # Remove noise before laplacian
    gray_lap = cv2.Laplacian(gray_blur, cv2.CV_8UC1, ksize=5)
    dilate_lap = cv2.dilate(gray_lap, (3, 3))  # Fill in gaps from blurring. This helps to detect circles with broken edges.
    # Furture remove noise introduced by laplacian. This removes false pos in space between the two groups of circles.
    lap_blur = cv2.bilateralFilter(dilate_lap, 5, 9, 9)
    # Fix the resolution to 16. This helps it find more circles. Also, set distance between circles to 55 by measuring dist in image.
    # Minimum radius and max radius are also set by examining the image.
    circles = cv2.HoughCircles(lap_blur, cv2.cv.CV_HOUGH_GRADIENT, 16, 55, param2=450, minRadius=20, maxRadius=40)
    cimg = draw_circles(gray, circles)
    print("{} circles detected.".format(circles[0].shape[0]))
    # There are some false positives left in the regions containing the numbers.
    # They can be filtered out based on their y-coordinates if your images are aligned to a canonical axis.
    # I'll leave that to you.
    return cimg
