import time

#time.datefmt('')

named_tuple = time.localtime() # get struct_time
#time_string = time.strftime("%m/%d/%Y, %H:%M:%S", named_tuple)
time_string = time.strftime("%m/%d/%Y, %H:%M:%S", named_tuple)

print(time_string)
print('time min: ', time.gmtime(5).tm_min)
print('time hour: ', time.gmtime(5).tm_hour)
print('time sec: ', time.gmtime(5).tm_sec)

print('time min: ', time.asctime())
print('time hour: ', time.asctime())
print('time sec: ', time.asctime())








