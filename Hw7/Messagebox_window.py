"""
對話方塊(messagebox)
• 提供8種使用於不同場合的對話方塊
• showinfo(title, message, options)：一般提示訊息
• showwarning(title, message, options)：警告訊息
• showerror(title, message, options)：錯誤訊息
• askquestion(title, message, options)：詢問訊息
• askokcancel(title, message, options)：確定或取消訊息
• askyesno(title, message, options)：是或否訊息
• askyesnocancel(title, message, options)：是或否或取消訊息
• askretrycancel(title, message, options)：重試或取消訊息
"""
# Message box window
from tkinter import *
from tkinter import messagebox

def myMsg():
    messagebox.showinfo("My messsage box","早安")

window = Tk()
window.title("MyMessage")
window.geometry("300x200")

Button(window,text="Good Morning",command=myMsg).pack()

window.mainloop()