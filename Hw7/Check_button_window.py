"""
核取方塊(Checkbutton)
• 功能與選項鈕相同，但可以複選
• 格式： Checkbutton(父物件, options, …)
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
        • Variable：設定或取得目前選取的選項按鈕，值通常為IntVar
        或StringVar
"""
# Checkbuttom window
from tkinter import *

def PrintInfo():  # 列出所選城市
    selection = ''
    for i in checkboxes:  # 檢查此字典
        if checkboxes[i].get() == True:  # 被選取則執行
            selection = selection + sports[i]+"\t"  # \t = tab
    print(selection)

window = Tk()
window.title("MySport")
window.geometry("300x200")

Label(window, text="favorite?",
      fg='blue', bg='lightyellow', width=40).grid(row=0)

sports = {0: "football", 1: "baseball",
          2: "basketball", 3: "tennis", 4: "table-tennis"}
checkboxes = {}  # 字典存放被選取項目
for i in range(len(sports)):  # 將運動字典轉成核取方塊
    checkboxes[i] = BooleanVar()  # 布林選取物件
    Checkbutton(window, text=sports[i],
                variable=checkboxes[i]).grid(row=i+1, sticky=W)

Button(window, text='submit', width=10, command=PrintInfo).grid(row=i+2)

window.mainloop()
