# Scrollbar_Window
from tkinter import *

window = Tk()
window.title("MyText")
window.geometry("300x100")

scrollbar = Scrollbar(window)  # 卷軸物件
text = Text(window,height=2,width=30)  # 文字區域物件
scrollbar.pack(side=RIGHT,fill=Y)  # 靠右安置與父物件高度相同
text.pack(side=LEFT,fill=Y)  # 靠左安置與父物件高度相同
scrollbar.config(command=text.yview)
text.config(yscrollcommand=scrollbar.set)
text.insert(END,"title\nsubtitle\n\n")
str = """000000000,111111111111111,2222222222222222222222222222222222222222\
    3333,444444444444,55555555555555555\
    6666666666\
    ,7777777777777777777777777777777,
    8888888888888888888888888888888888\
    9"""
text.insert(END,str)

window.mainloop()