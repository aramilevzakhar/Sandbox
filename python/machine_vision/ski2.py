#from skimage import data
#import os
#camera = data.camera()
#print(camera)
#camera.shape()


from skimage import data
from skimage.color import rgb2gray
import matplotlib.pyplot as plt
from skimage import io as io 
# Setting the plot size to 15,15
plt.figure(figsize=(15, 15))
 
# Sample Image of scikit-image package
coffee = data.coffee()
plt.subplot(1, 2, 1)
 
# Displaying the sample image
plt.imshow(coffee)
 
# Converting RGB image to Monochrome
gray_coffee = rgb2gray(coffee)
#io.imshow(gray_coffee)
#io.show(gray_coffee)

plt.subplot(1, 2, 2)
 
# Displaying the sample image - Monochrome
# Format
plt.imshow(gray_coffee, cmap="gray")

