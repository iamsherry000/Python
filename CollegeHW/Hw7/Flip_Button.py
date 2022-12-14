'''
變數類別(variable classes)
• 若程式在執行時，要動態更改視窗元件的內容，可以透過tlinter模組內定義的變數類別。
    • 標籤的本文
    • 執行方法
• 變數類別
    • IntVar()：整數變數，預設為0
    • DoubleVar()：浮點數變數，預設為0.0
    • StringVar()：字串變數，預設為””
    • BooleanVar()：布林值變數，預設為True (1)
• 方法
    • get()：取得變數內容
    • set()：設定變數內容
'''
# Flip Button
from tkinter import *


def btn_Flip():  # button func
    global msg_on
    if msg_on == False: 
        msg_on = True
        x.set("MCU_CCE")  # show sentence
    else:
        msg_on = False
        x.set("")  # show no sentense


window = Tk()
window.title("myButton")

msg_on = False  # global variable default FALSE
x = StringVar()  # Label info

label = Label(window, textvariable=x,
              fg="blue", bg="lightyellow",
              font="Verdana 16 bold",
              width=25, height=2).pack()

btn = Button(window, text="Hit", command=btn_Flip).pack()

window.mainloop()
