from matplotlib import colors
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# x = [1, 2, 3, 4]
# y = [10, 8, 6, 9]

# #print(plt.style.available)

# plt.style.use('dark_background')
# plt.plot(x, y, color="red")
# plt.show() 

'''
Pyplot API và Object-Oriented API là hai cách để vẽ đồ thị
- Ptplot API : Vẽ nhanh chóng (plt.plot())
- Ô API : vẽ những đồ thì phức tạp
'''

# Pyplot API:

# x = np.linspace(0, 10, 1000)
# plt.plot(x, np.sin(x), color="blue", label = "sin(x)")
# plt.plot(x, np.cos(x), color="red", label = 'cos(x)')
# plt.xlabel('Bien X')
# plt.ylabel('Sin(x)')
# # plt.xlim([0,4])
# # plt.ylim([0,10])
# plt.legend()
# plt.show()

# OO API :

# x = [1,2,3,4]
# y= [11,22,33,44]

# # Setup plot
# fig, ax = plt.subplots(figsize = (5,5)) # Figure size = width & height
# ax.plot(x, y);
# ax.set(title='A simpke plot', xlabel ='x-axis', ylabel='y-axis')
# plt.show()

'''
Most common types of Matplotlib plots:
- Line
- Scatter
- bar
- hist
- subplots()
'''

'''
Line:
'''
# x = np.linspace(0, 10, 100)
# x[:5]
# fig, ax = plt.subplots()
# ax.plot(x, x**2)
# plt.show()

'''
Scatter
'''
# plt.scatter(x, np.exp(x))
# plt.show()

# OO API

# rng = np.random.RandomState(0)

# x = rng.randn(100)
# y = rng.randn(100)

# color = rng.rand(100)
# fid, ax = plt.subplots()
# img = ax.scatter(x, y, c=color, cmap='viridis')

# fid.colorbar(img)
# plt.show()

'''
Bar: Vertical, Horizontal
'''
# soft_drink = {'coke': 10, 'Pessi': 12, "sting": 8}

# # Biểu đồ dọc : Vertical
# fig, ax = plt.subplots()
# ax.bar(soft_drink.keys(), soft_drink.values())
# ax.set(title = 'bach hoa', ylabel= 'Gia $' )
# plt.show()

# Biểu đồ ngang : Horizontal
# fig, ax = plt.subplots()
# ax.barh(list(soft_drink.keys()), list(soft_drink.values()))
# plt.show() 

'''
Histogram
'''
# student_height = np.random.normal(170, 10, 250)
# plt.hist(student_height, bins=30)
# plt.show()

'''
Subplots: Multiple plot on one figure
'''
# x = np.random.randn(100)
# fig, ((ax1, ax2), (ax3,ax4)) = plt.subplots(nrows=2, ncols=2, figsize = (10,5)) # Số hàng, só cột, size 
# ax1.plot(x,x/2)
# ax2.scatter(x,x**2)
# ax3.bar(x, x*2)
# ax4.hist(x)
# plt.show()