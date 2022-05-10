# window color change_button
from tkinter import *

def yellow():  # 設定視窗背景是黃色
    window.config(bg="yellow")
def blue():  # 設定視窗背景是藍色
    window.config(bg="blue")

window = Tk()
window.title("myButton")
window.geometry("300x200")

# build three buttons 
ExitBtn = Button(window,text="Exit",command=window.destroy)
BlueBtn = Button(window,text="Blue",command = blue)
YellowBtn = Button(window,text="Yellow",command=yellow)

# set buttons positions
ExitBtn.pack(anchor=S,side="right",padx=5,pady=5)
BlueBtn.pack(anchor=S,side="right",padx=5,pady=5)
YellowBtn.pack(anchor=S,side="right",padx=5,pady=5)

window.mainloop()