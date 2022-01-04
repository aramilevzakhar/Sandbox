import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np
import pickle

str1 = '10 14 21 23 27 32 39 45 55 61 62 68'
str2 = '3.8 4.8 5.9 6.1 6.2 6.3 6.6 7.4 8.5 9.7 10.5 12.4'
x = list(map(int, str1.split(' ')))
y = list(map(float, str2.split(' ')))
##print(x)
x = np.array(x).reshape((12, 1))
##print(x)
y = np.array(y)
##print(y)
model = LinearRegression()
model.fit(x, y)
print('r2: ', model.score(x, y))
print('b: ', model.intercept_)
print(f'a: {model.coef_}')
print(f'model.predict: {model.predict(x)}')
plt.plot(x, y, 'ro')
plt.plot(x, model.predict(x))
plt.grid()
plt.show()
#ysum = sum(y)
#xsum = sum(x)
#xx = sum([item**2 for item in x])
#xy = sum([xl*yl for xl, yl in zip(x, y)])



#print(f'ysum: {ysum}')
#print(f'xsum: {xsum}')
#print(f'xx: {xx}')
#print(f'xy: {xy}')
#b = (xy*xsum-ysum*xx)/(xsum**2-12*xx)
#a = (xy - b*xsum)/xx
#Show result
#print(f'my result\na:{a}\nb:{b}')
#plt.plot(x, list(map(lambda arg: a*arg + b, x)), 'g')
#print(list(map(lambda arg: a*arg + b, x)))
#print(x1)
#x.append(201)
#ax.plot([1, 20, 30, 60], [1, 3, 4 ,10])
#Добавляем подписи к осям:
#ax.set_xlabel('turnover')
#ax.set_ylabel('average output per worker')
#plt.plot(X, Y, 'ro')
#plt.axis([0, 6, 0, 20])

#plt.axis()
