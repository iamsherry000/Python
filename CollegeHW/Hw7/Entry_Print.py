'''文字方塊(Entry)
• 輸入一行文字的文字方塊
• 格式： Entry(父物件, options, …)
    • 父物件：功能鍵所在的視窗
    • options
        • width與height：寬度與高度 (單位：字元)
        • bg與fg：背景與字型顏色
        • state：輸入狀態，NORMAL表示可輸入，DISABLE無法輸入
        • textvariable：文字變數
        • show：顯示輸入文字
'''
# Entry_print
from tkinter import *

def PrintInfo():
    print("Account: %s\nPassword: %s" %(win1.get(),win2.get()))

window = Tk()
window.title("MyWindow")
window.geometry("250x100")
lab1 = Label(window,text="Account ").grid(row=0)
lab2 = Label(window,text="Account ").grid(row=1)

win1 = Entry(window)
win1.grid(row=0,column=1)
win2 = Entry(window,show='*')
win2.grid(row=1,column=1)

btn1 = Button(window,text="Print",command=PrintInfo)
btn1.grid(row=2,column=0)
btn2 = Button(window,text="Quit",command=window.destroy)
btn2.grid(row=2,column=1)

window.mainloop()