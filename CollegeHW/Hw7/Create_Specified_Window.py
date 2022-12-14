# create a specified window
from tkinter import *

window = Tk()
window.title("myWindow") # 視窗標題
window.geometry("400x300") # 視窗大小
window.config(bg = "light yellow") # window bg color

window.mainloop() #show window
