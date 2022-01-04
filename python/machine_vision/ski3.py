from skimage.future import graph
from skimage import data, segmentation, color, filters, io
from matplotlib import pyplot as plt
import cv2

#img = data.coffee()
img = cv2.imread('mult.jpg')

gimg = color.rgb2gray(img)
#cv2.imshow('win1', gimg)







labels = segmentation.slic(img, compactness=30, n_segments=100, start_label=1)
print(labels)
edges = filters.sobel(gimg)
edges_rgb = color.gray2rgb(edges)

g = graph.rag_boundary(labels, edges)
lc = graph.show_rag(labels, g, edges_rgb, img_cmap=None, edge_cmap='viridis',
                    edge_width=0.2)

plt.colorbar(lc, fraction=0.03)
io.show()
