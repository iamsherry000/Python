# test: 做出10個按照長度大小區分的長條圖
import matplotlib.pyplot as plt
import numpy as np

'''
x = np.random.randn(1000)    
plt.hist(x,bins=20,color='b')
    

plt.title("example")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()


'''

num1 = 10
num2 = 9
num3 = 8
num4 = 7
num5 = 6
num6 = 5
num7 = 4
num8 = 3
num9 = 2
num10 = 1

likes = [num1,num2,num3,num4,num5,num6,num7,num8,num9,num10]  # 將喜愛數加入likes的陣列

for i in range(1,11):  # 將喜愛度從1-10排序
    numbers = i
    

# x = np.arange(len(numbers))  # 10
x = np.arange(10)  
plt.bar(numbers, likes, 
        color=['LightBlue',
               'PowderBlue', 
               'LightSkyBlue', 
               'DodgerBlue', 
               'CornflowerBlue', 
               'RoyalBlue', 
               'Blue', 
               'MediumBlue',
               'DarkBlue',
               'MidnightBlue'
               ])
# plt.xticks(numbers, likes)
plt.xlabel('Numbers')
plt.ylabel('Likes')
plt.title('Dcard-Meme-Collection')
plt.show()