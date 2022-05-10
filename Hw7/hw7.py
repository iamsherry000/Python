# Calculator
from tkinter import *

window = Tk()
window.title("Calculator")
window.geometry("300x600")


def Clicked(x):
    number = X


# def Clear():

msg_on = False  # global variable default FALSE
x = StringVar()  # Label info

for m in range(0,6):
    Label()['lab%s' % m] = Label(window)

for n in range(0, 10):
    # globals()['btn%s' % n] = '%d' % n
    Button()['btn%s' % n] = Button(window, text='%d' % n,
              width=25, height=2)

btn0.pack(anchor=S,side="right",padx=5,pady=5)
lab0.pack()


window.mainloop()
