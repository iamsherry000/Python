# Calculator func: Add
from tkinter import *

def Add():
    n3.set(n1.get()+n2.get())

def Clear():
    s1.delete(0,END)
    s2.delete(0,END)
    s3.delete(0,END)

window = Tk()
window.title("ADD")

n1 = IntVar()
n2 = IntVar()
n3 = IntVar()

s1 = Entry(window,width=8,textvariable=n1)  # 文字方塊1
lab1 = Label(window,width=3,text='+')  # 加號
s2 = Entry(window,width=8,textvariable=n2)  # 文字方塊2
btn1 = Button(window,width=5,text='=',command=Add)  # =按鈕
s3 = Entry(window,width=8,textvariable=n3)  # 儲存結果文字方塊
btn2 = Button(window,text="Clear",command=Clear)
btn3 = Button(window,text="Quit",command=window.destroy)

s1.grid(row=0,column=0)  # 定位文字方塊1
lab1.grid(row=0,column=1,padx=5)  # 定位加號
s2.grid(row=0,column=2)  # 定位文字方塊2
btn1.grid(row=0,column=3,pady=5)  # 定位"=按鈕"
s3.grid(row=0,column=4)  # 定位儲存結果
btn2.grid(row=2,column=0)
btn3.grid(row=2,column=0)

window.mainloop()