"""
圖形(PhotoImage)
• 可以使用於如標籤、功能鈕、文字區塊等元件上。
• 格式： PhotoImage(file=“xxx.gif”)
• 支援gif、png格式圖檔
"""
# PhotoImage_button_window
from tkinter import *


def msgShow():
    label["text"] = "MCU_CCE"
    label["bg"] = "lightyellow"
    label["fg"] = "blue"


window = Tk()
window.title("MyButton")
# window.geometry("300x200")

label = Label(window)
cce_gif = PhotoImage(file="CCE_logo.gif")
btn = Button(window, image=cce_gif,
             command=msgShow, text="click", compound=TOP)  # compound=TOP 由上往下疊

label.pack()
btn.pack()  # 包裝位置

window.mainloop()

''' 測 Path 用
import os
print(os.getcwd())
'''
