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
from dcard_picture_v3 import dcard

window=Tk()
window.title("Dcard梗圖收集器")
window.geometry("2000x1000")
window.config(bg="white")

pics=[]

def show(buttonString):  #顯示字在label
    content = equ.get()
    equ.set(buttonString)#content + tag累加

def backspace(): #倒退
    equ.set(str(equ.get()[:-20]))

def getdcard():
    dcard()
    for i in tag:
        image = Image.open(f'C:/Users/weili/OneDrive/桌面/py/image/{i}') #讀入圖片
        globals()[f'{i}'] = image.resize((500,300),Image.ANTIALIAS)
        globals()[f'{i}'] = ImageTk.PhotoImage(globals()[f'{i}'])#把圖片轉成tkinter的格式
        globals()[f'p{i}'] = Label(window,image=globals()[f'{i}'])
        print(i)
        
    p1.place(x=0,y=250)
    p2.place(x=500,y=250)

    for i in range(3,11):
           if i < 7:
               globals()[f'p{i}'].place(x=1000,y=250*(i-3)) 
           else:
               globals()[f'p{i}'].place(x=1500,y=250*(i-7))
    
def comparision():#比對
    global equ
    if equ in topics:
        tag=topics[equ]
        
    elif equ=="搜尋":
        tag=[str(i)+".jpg" for i in range(1,11)]
        
    

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
btn6 = Button(window,text="#閒聊",bg="white",command=lambda:show("閒聊"))
a2= Label(window,text="!!梗圖排名!!",bg="#508cf0",font=("標楷體", 20),fg="#FFFFFF",relief=RAISED)


'''
image=Image.open("D:/github/Python/FinalProject/aqua.png")#讀入圖片

img = image.resize((200,200),Image.ANTIALIAS) 

img = ImageTk.PhotoImage(img)#把圖片轉成tkinter的格式

a3 = Label(window,image=img)#將圖片標籤化
a3.config(width=200, height=200)
'''
'''
for i in range(1,11):
    image = Image.open(f'C:/Users/weili/OneDrive/桌面/py/image/{i}.jpg') #讀入圖片
    globals()[f'img{i}'] = image.resize((500,300),Image.ANTIALIAS)
    globals()[f'img{i}'] = ImageTk.PhotoImage(globals()[f'img{i}'])#把圖片轉成tkinter的格式
    globals()[f'p{i}'] = Label(window,image=globals()[f'img{i}'])

'''
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
'''
p1.place(x=0,y=250)
p2.place(x=500,y=250)

for i in range(3,11):
    if i < 7:
        globals()[f'p{i}'].place(x=1000,y=250*(i-3))
        
    else:
        globals()[f'p{i}'].place(x=1500,y=250*(i-7))
'''
window.mainloop()