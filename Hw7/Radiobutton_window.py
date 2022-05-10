""" 選項鈕(Radiobutton)
• 提供由滑鼠點選的方式決定動作
• 每次只有一個選項能被選取
• 格式： Radiobutton(父物件, options, …)
    • 父物件：功能鍵所在的視窗
    • options
        • text：選項鈕旁的文字
        • font：字型
        • width與height：寬度與高度 (單位：字元)
        • padx：決定選項鈕與文字的距離
        • pady：決定選項鈕的上下間距
        • value：選項鈕的值
        • indicatoron：建立盒形選項鈕
        • command：當改變選項時，自動執行此方法
        • Variable：設定或取得目前選取的選項按鈕，值通常為IntVar或
        StringVar
"""
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
                variable=var,
                value=val,
                command=PrintSelection).pack()

window.mainloop()

'''
問題: 選項長度不同，會影響排版
'''