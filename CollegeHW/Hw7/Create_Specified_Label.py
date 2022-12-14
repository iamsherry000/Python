# create a specified label
from tkinter import *

window = Tk()
window.title("myWindow") # 視窗標題
window.geometry("400x300") # 視窗大小
label = Label(window,text = "MCU_CCE",
            bg = "lightyellow",
            width = 15,
            font = "Helvetica 16 bold italic",
            #relief = RAISED,
            relief = "raised"
            )
label.pack()

window.mainloop()