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
num7 = 8
num8 = 7
num9 = 6
num6 = 5


for i in range(1,11):  # 將喜愛度從1-10排序
    numbers = i

likes = [1th,2th,3th,4th,5th,6th,7th,8th,9th,10th]  # 將喜愛數加入likes的陣列



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