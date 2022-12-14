from tkinter import *
import os
from PIL import Image, ImageTk
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure
import requests,os,glob
import json
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from dcard_picture_def import dcard
import pandas as pd
import matplotlib.pyplot as plt


window=Tk()
window.title("Dcard梗圖收集器")
window.geometry("2000x1000")
window.config(bg="white")


def a():
    # Reference: https://www.796t.com/article.php?id=71353
    global likeCount
    pics = ["pic_1","pic_2","pic_3","pic_4","pic_5",
           "pic_6","pic_7","pic_8","pic_9","pic_10"]
    # commentCount: [36, 27, 32, 7, 58, 31, 33, 34, 4, 26]

    #likes = [10,9,8,7,6,5,4,3,2,1]  # 將喜愛數加入likes的陣列


    dict = {
        "pics": pics,
        "likes": likeCount
    }
    #print(likeCount)
    select_df = pd.DataFrame(dict)

    # 圖片大小
    #plt.figure(figsize=(10, 5)) 
    barplot = Figure(figsize=(8,4.3))
    b = barplot.add_subplot(111)
    #圖片像素
    plt.rcParams['savefig.dpi'] = 1000 
    #分辨
    #plt.rcParams['figure.dpi'] = 1000

    # 抓取select_df的sports、nums欄位，並以pics當x軸，畫出一個bar，顏色為#5887ff
    # ax = plot(data = select_df[['pics', 'likes']],x='pics', kind='bar', color='#5887ff')
    b.bar(x=select_df['pics'],height=select_df['likes'], color='#5887ff')
    # 把資料放進來並指定對應的X軸、Y軸的資料，用方形做標記(s-)，並指定線條顏色為紅色，使用label標記線條含意
    # plt.plot(pics,commentCount,'s-',color = 'r', label="commentCount")

    #用來顯示正常的中文標籤
    plt.rcParams['font.sans-serif']=['Microsoft JhengHei'] 
    #標題
    b.set_title('Dcard-Meme-Collection', fontsize="18") 
    #X軸的名稱、字體大小
    b.set_xlabel("Pictures", fontsize="14") 
    #Y軸名稱、字體大小、轉方向、靠旁邊
    b.set_ylabel("Likes", fontsize="14", rotation=360, horizontalalignment='right', verticalalignment='top')
    #刻度
    #X軸刻度大小、轉方向
    #b.set_xticks(fontsize=10, rotation=360)
    #Y軸刻度大小
    #b.set_yticks(fontsize=14)
    #Y軸座標範圍
    b.set_ylim([0, 3000])

    #顯示該直條圖的數字
    x = select_df['pics'].tolist()
    y = select_df['likes'].tolist()
    #l是要放入X軸的index
    l=[i for i in range(len(select_df))]
    for i,(_x,_y) in enumerate(zip(l, y)): 
               b.text(_x, _y, str(y[i])[0:4], ha='center', va= 'bottom', color='black', fontsize=12)
    
    #把圖顯示出來
    #plt.show()
    canvas = FigureCanvasTkAgg(barplot, master=window)
    canvas.draw()
    canvas.get_tk_widget().place(x=100, y=550)


def show(buttonString):  #顯示字在label
    content = equ.get()
    equ.set(buttonString)#content + tag累加
    
    
def backspace(): #倒退
    equ.set(str(equ.get()[:-20]))
    

def getdcard():
    a()
    tag=[]
    tag=comparision(topics)
    tag.insert(0,tag[-1])
    tag.pop(-1)
    for index,i in enumerate(tag):#index計數，i=1.jpg....
        print("我是",i,index)
        image = Image.open(f'D:/github/Python/FinalProject/images/{i}') #讀入圖片        
        globals()[f'{i}'] = image.resize((500,300),Image.ANTIALIAS)
        globals()[f'{i}'] = ImageTk.PhotoImage(globals()[f'{i}'])#把圖片轉成tkinter的格式
        globals()[f'p{index+1}'] = Label(window,image=globals()[f'{i}'])
        print("我是",i)
        pos=index+2
        
    p1.place(x=0,y=250)
    p2.place(x=500,y=250)

    for i in range(3,pos):
           if i < 7:
               globals()[f'p{i}'].place(x=1000,y=250*(i-3)) 
           else:
               globals()[f'p{i}'].place(x=1500,y=250*(i-7))
            
    
def comparision(topics):#比對
    global equ
    global tag

    a=equ.get()
    print(a)
    tag=[]
    
    if a in topics:
        tag=topics[a]
        
    elif a=="":
        tag=[str(i)+".jpg" for i in range(1,11)]
    
    print(tag)
    return tag

def reduce_button():
    for i in range(1,11):
        globals()[f'p{i}'].destroy()        
    

likeCount,commentCount,topics=dcard()
print("1")
equ = StringVar()#變數
equ.set("")
a1= Label(window,text="Dcard梗圖收集器",bg="#3264a0",font=("標楷體", 50),fg="#FFFFFF",relief=RAISED)
b1 = Entry(window,selectbackground="#1e46b4",font=("標楷體", 30),textvariable=equ)
btn = Button(window,text="刪除",bg="white",height=4,command=backspace)
btn1 = Button(window,text="搜尋",bg="white",height=2,width=5,command=getdcard)
btn2 = Button(window,text="#梗圖",bg="white",command=lambda:show("梗圖"))
btn3 = Button(window,text="#迷因",bg="white",command=lambda:show("迷因"))
btn4 = Button(window,text="#搞笑",bg="white",command=lambda:show("搞笑"))
btn5 = Button(window,text="#有趣",bg="white",command=lambda:show("有趣"))
btn6 = Button(window,text="#隱藏",bg="white",command=reduce_button)
a2= Label(window,text="!!梗圖排名!!",bg="#508cf0",font=("標楷體", 20),fg="#FFFFFF",relief=RAISED)

'''''''''''''''''''''''''位置'''''''''''''''''''''''''''

a1.place(x = 0, y =0,width=1000,height=100)
b1.place(x = 0, y =100,width=600,height=50)
btn.place(x = 600, y =100,width=200,height=50)
btn1.place(x = 800, y =100,width=200,height=50)

btn2.place(x = 0, y =150,width=200,height=50)
btn3.place(x = 200, y =150,width=200,height=50)
btn4.place(x = 400, y =150,width=200,height=50)
btn5.place(x = 600, y =150,width=200,height=50)
btn6.place(x = 800, y =150,width=200,height=50)

a2.place(x=0, y =200,width=1000,height=50)

window.mainloop()