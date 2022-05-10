# Radiobutton window
from tkinter import *

def PrintSelection():  # 列出所選城市
    print(cities[var.get()])

window = Tk()
window.title("MyCity")
# window.geometry("300x100")
cities = {0: "Taipei", 1: "Tokio", 2: "Paris", 3: "London", 4: "HongKong"}

var = IntVar()
var.set(0)  # 預設選項
label = Label(window, text="favorite city:",
              fg="blue", bg="lightyellow", width=30).pack()

for val, city in cities.items():  # 建立選項紐
    Radiobutton(window,
                text=city,
                indicatoron=0,  # 用盒子取代選項紐
                width=30,
                variable=var,
                value=val,
                command=PrintSelection).pack()

window.mainloop()
