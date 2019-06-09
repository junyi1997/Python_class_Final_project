
import tkinter as tk
from tkinter import messagebox
window=tk.Tk()
#window.geometry("380x420+500+240")

def closeWindow():
    messagebox.showinfo(title="警告",message="好好回答，不許關閉")

#使用者關閉視窗觸發的事件（第一個刪除視窗，第二個為函式名，即過程）
window.protocol('WM_DELETE_WINDOW',closeWindow)

#顯示視窗(訊息迴圈)
window.mainloop()