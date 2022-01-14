
import cv2 as cv

file = 'mult.jpg'
img = cv.imread(file)
#b, g, r = cv.split(img)


img[:,:,0] = 0
img[3:33,:,0] = 0
img[3:33,:,1] = 0
img[3:33,:,2] = 0




#print(len(b), b)
#b1 = img[:,:,0]
#for it in b:
#    print(it)



print("")
    


#print(len(b1), b1)
#cout(b, g, r)
#img = cv.merge((0, g, 0))
#cv.imshow()
cv.imshow('window', img)
#text = f'file name: {file}\n\
#        width: {img.shape[1]}\n\
#        height: {img.shape[0]}\n\
#        channels: {img.shape[2]}'
#
#cv.displayOverlay('window', text)

cv.waitKey(0)
cv.destroyAllWindows()
