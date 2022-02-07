import numpy as np
import PIL.Image


message_to_hide = "This is my secret message!"
image = PIL.Image.open('image.png', 'r')
width, height = image.size
print(width, height)

if image.mode == "P":
    print('Not supported')
    exit()





img_arr = np.array(list(image.getdata()))
channels = 4 if image.mode == 'RGBA' else 3

pixels = img_arr.size // channels


stop_indicator = '$123123$'
stop_indicator_length = len(stop_indicator)


message_to_hide += stop_indicator



