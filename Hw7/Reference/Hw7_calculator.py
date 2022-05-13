# from Han.

from tkinter import *
def show(i):
    global message
    message += f'{i}'
    x.set(message)
def delete():
    global message
    if len(message) == 0:
        message = ""
        x.set(message)
    else:
        message = message[0:len(message)-1]
        x.set(message)
def clear():
    global message
    message = ""
    x.set(message)
def square():
    global message
    val = (eval(message))**2
    message = f'{val}'
    x.set(message)
def sq():
    global message
    val = round((eval(message))**0.5, 3)
    message = f'{val}'
    x.set(message)
def cal():
    global message
    val = eval(message)
    message = f'{val}'
    x.set(str(val))
window = Tk()
window.title("My Calculator")
window.geometry("200x210")
message = ""
x = StringVar()
label = Label(window, textvariable = x,
              bg = "lightyellow", #標籤背景色，也可加fg是文字顏色，foreground
              width = 15, #標籤寬度為15個字
              font = "Helvetica 16 bold italic",
              relief = RAISED) #邊框樣式
btn1 = Button(window, text = '1', command = lambda:show(1))
btn2 = Button(window, text = '2', command = lambda:show(2))
btn3 = Button(window, text = '3', command = lambda:show(3))
btn4 = Button(window, text = '4', command = lambda:show(4))
btn5 = Button(window, text = '5', command = lambda:show(5))
btn6 = Button(window, text = '6', command = lambda:show(6))
btn7 = Button(window, text = '7', command = lambda:show(7))
btn8 = Button(window, text = '8', command = lambda:show(8))
btn9 = Button(window, text = '9', command = lambda:show(9))
btn0 = Button(window, text = '0', command = lambda:show(0))
btna = Button(window, text = '+', command = lambda:show("+"))
btnm = Button(window, text = '-', command = lambda:show("-"))
btnp = Button(window, text = '*', command = lambda:show("*"))
btnd = Button(window, text = '/', command = lambda:show("/"))
btnsq = Button(window, text = 'sqrt(x)', command = sq)
btndelete = Button(window, text = '<-x', command = delete)
btncl = Button(window, text = 'C', command = clear)
btne = Button(window, text = '=', command = cal)
btndot = Button(window, text = '.', command = lambda:show("."))
btns = Button(window, text = 'x^2', command = square)
label.grid(row = 0, column = 0, columnspan = 4)
btndelete.grid(row = 1, column = 0)
btncl.grid(row = 1, column = 1)
btns.grid(row = 1, column = 2)
btna.grid(row = 1, column = 3)
btn7.grid(row = 2, column = 0)
btn8.grid(row = 2, column = 1)
btn9.grid(row = 2, column = 2)
btnm.grid(row = 2, column = 3)
btn4.grid(row = 3, column = 0)
btn5.grid(row = 3, column = 1)
btn6.grid(row = 3, column = 2)
btnp.grid(row = 3, column = 3)
btn1.grid(row = 4, column = 0)
btn2.grid(row = 4, column = 1)
btn3.grid(row = 4, column = 2)
btnd.grid(row = 4, column = 3)
btnsq.grid(row = 5, column = 0)
btn0.grid(row = 5, column = 1)
btndot.grid(row = 5, column = 2)
btne.grid(row = 5, column = 3)
window.mainloop()