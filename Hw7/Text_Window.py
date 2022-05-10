'''文字區塊(Text)
• 輸入多行文字的文字區塊(類似一個簡單的文字編
輯器)
• 格式： Text(父物件, options, …)
    • 父物件：功能鍵所在的視窗
    • options
        • width與height：寬度與高度 (單位：字元)
        • bg與fg：背景與字型顏色
        • state：輸入狀態，NORMAL表示可輸入，DISABLE無法輸入
        • xcrollbarcommand：水平捲軸的連結
        • ycrollbarcommand：垂直捲軸的連結
        • warp：換行參數，預設為CHAR(換行)。
'''
# Text_Window
from tkinter import *

window = Tk()
window.title("MyText")
window.geometry("300x300")
text = Text(window,height=15,width=40)
text.insert(END,"title\nsubtitle\n\n")
str = """this is text."""
text.insert(END,str)
text.pack()

window.mainloop()
