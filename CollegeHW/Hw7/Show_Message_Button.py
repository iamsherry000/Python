'''
Button:
    父物件:功能鍵所在的視窗
    options:
        text
        width、height
        bg、fg: bg背景顏色, fg字形顏色
        image
        command: 按下功能鍵後，所要執行的方法

'''
# show message button
from tkinter import *

def msgShow():
    label["text"] = "MCU_CCE"
    label["bg"] = "lightyellow"
    label["fg"] = "blue"

window = Tk()
window.title("button_test_Window")
label = Label(window)
btn1 = Button(window,text="Message",width=15,command=msgShow)
btn2 = Button(window,text="Exit",width=15,command=window.destroy)
label.pack()
btn1.pack(side=LEFT)
btn2.pack(side=RIGHT)

window.mainloop()
