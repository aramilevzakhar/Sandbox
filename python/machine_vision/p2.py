#import numpy as np
#arr = np.array([[3, 2, 4], [5, 0, 1]])
#print(np.sort(arr))
#arr = np.array([1, 2, 3, 4], ndmin=5)
#print(arr)
#print('shape of array :', arr.shape)
#arr = np.array([1, 2, 3, 4, 5, 6, 7])
#print(arr[1:5])
#arr = np.array([1, 2, 3, 4, 5, 6, 7])
#print(arr[4:])
#arr = np.array([1, 2, 3, 4, 5, 6, 7])
#print(arr[::2])
#np.concatenate()
import cv2
import numpy as np
from matplotlib import pyplot as plt
  
#Let's load a color image first: 
img = cv2.imread('mult.jpg')

print(img.shape)
print(img.size)
rows, cols, ch = img.shape
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('win', img)

#flags = [i for i in dir(cv2) if i.startswith('COLOR_')]
#print(len(flags))




  
#pts1 = np.float32([[50, 50],
#                   [200, 50], 
#                   [50, 200]])
#  
#pts2 = np.float32([[10, 100],
#                   [200, 50], 
#                   [100, 250]])
#  
#M = cv2.getAffineTransform(pts1, pts2)
#dst = cv2.warpAffine(img, M, (cols, rows))
#  
#plt.subplot(121)
#plt.imshow(img)
#plt.title('Input')
#  
#plt.subplot(122)
#plt.imshow(dst)
#plt.title('Ouput')
#  
#plt.show()
#  
## Displaying the image
#while(1):
#      
#    cv2.imshow('image', img)
#    if cv2.waitKey(20) & 0xFF == 27:
#        break
#          
cv2.waitKey(0)
#cv2.destroyAllWindows()
