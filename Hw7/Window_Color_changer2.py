# window color change_button (lambda)
from tkinter import *

def BG_Color(bgColor):
    window.config(bg=bgColor) # window background color

window = Tk()
window.title("myButton")
window.geometry("300x200")

# build three buttons 
ExitBtn = Button(window,text="Exit",command=window.destroy)
BlueBtn = Button(window,text="Blue",command = lambda:BG_Color("blue"))
YellowBtn = Button(window,text="Yellow",command = lambda:BG_Color("yellow"))

# set buttons positions
ExitBtn.pack(anchor=S,side="right",padx=5,pady=5)
BlueBtn.pack(anchor=S,side="right",padx=5,pady=5)
YellowBtn.pack(anchor=S,side="right",padx=5,pady=5)

window.mainloop()