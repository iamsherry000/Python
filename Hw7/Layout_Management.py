'''
將視窗元件包裝與定位的三種配置方法:
pack()、grid()、place()
* pack():
    1. 排列方向:side
    2. 水平間距:padx(單位像素)
    3. 垂直間距:pady(單位像素)
'''
'''
# Layout management
from tkinter import *

window = Tk()
window.title("myDepartment") # 視窗標題
window.geometry("300x150") # 視窗大小
label1 = Label(window,text = "MCU",
            bg = "lightyellow",
            width = 10)
label2 = Label(window,text = "TECH",
            bg = "lightgreen",
            width = 10)
label3 = Label(window,text = "CCE",
            bg = "lightblue",
            width = 10)
label1.pack(side = TOP,pady = 5)
label2.pack(side = "top",pady = 5)
label3.pack(side = TOP,pady = 5)

window.mainloop()

'''
# Layout management_1
from tkinter import *

window = Tk()
window.title("myDepartment") # 視窗標題
window.geometry("300x150") # 視窗大小
lab1 = Label(window,
            text = "MCU",
            bg = "lightyellow",
            width = 10)
lab2 = Label(window,
            text = "TECH",
            bg = "lightgreen",
            width = 10)
lab3 = Label(window,
            text = "資傳系",
            bg = "lightblue",
            width = 10)
lab4 = Label(window,
            text = "資工系",
            bg = "orange",
            width = 10)
lab5 = Label(window,
            text = "資管系",
            bg = "cyan",
            width = 10)
# method 1:
'''
lab1.pack(side = TOP,pady = 5)
lab2.pack()
lab3.pack(side = LEFT,padx = 10)
lab4.pack(side = "left",padx = 15)
lab5.pack(side = LEFT)
'''
# method 2:
lab1.place(x=100,y=0)
lab2.place(x=100,y=50)
lab3.place(x=0,y=100)
lab4.place(x=100,y=100)
lab5.place(x=200,y=100)

window.mainloop()
