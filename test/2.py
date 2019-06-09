import tkinter as tk
import tkinter.messagebox as messagebox
import pickle
from PIL import Image,ImageTk

# filebase引用必要套件
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

########################################################################
class MyApp(object):
    """"""
    #----------------------------------------------------------------------
    def __init__(self, parent):
        self.A=0#定義更改密碼的文字輸入盒的焦點
        self.photo_background=tk.PhotoImage(file=r"./image/背景.png")
        """Constructor"""
        self.win = parent#將視窗繼承
        self.win.title("PDMS_開始畫面")#定義標題名稱
        self.frame = tk.Frame(parent)
        self.frame.pack()
        left=(self.win.winfo_screenwidth()-100)//2#指定視窗置中
        top=(self.win.winfo_screenheight()-100)//2
        self.win.geometry("{:}x{:}+{:}+{:}".format(100,100,left,top))
        #進入登入畫面
        but_Log=tk.Button(win, command=lambda:self.openFrame4()) 
        but_Log.place(x=0,y=0,width=40,height=40)
    #----------------------------------------------------------------------
    def hide(self):
        """"""
        self.win.withdraw()
    #----------------------------------------------------------------------   
    def closeWindow(self,myclosewindow):
        self.onCloseOtherFrame(myclosewindow)
    #----------------------------------------------------------------------
    def openFrame4(self):
        """"""
        #生活小助手      
        self.hide()
        self.win_main4 = tk.Toplevel()
        self.win_main4.option_add("*Font",'微軟正黑體 30')
        left=(self.win_main4.winfo_screenwidth()-600)//2
        top=(self.win_main4.winfo_screenheight()-700)//2
        self.win_main4.geometry("{:}x{:}+{:}+{:}".format(600,700,left,top))
        self.win_main4.title("記帳本")
        
        #使用者關閉視窗觸發的事件（第一個刪除視窗，第二個為函式名，即過程）
        self.win_main4.protocol('WM_DELETE_WINDOW',lambda:self.closeWindow(self.win_main4))
        
        canvas_width = 1000
        canvas_height =1000
        canvas = tk.Canvas(self.win_main4, 
        width=canvas_width, 
        height=canvas_height)
        canvas.pack()
        #背景
        canvas.create_image(300,400, image=self.photo_background)#將背景貼到畫布上

        but_1=tk.Button(self.win_main4,text="輸入",font= ('Noto Sans Mono CJK TC Regular',30))
        but_1.place(x=40,y=570)
        but_2=tk.Button(self.win_main4,text="查詢",font= ('Noto Sans Mono CJK TC Regular',30))
        but_2.place(x=170,y=570)
        but_3=tk.Button(self.win_main4)
        but_3.place(x=430,y=570)        
        
    #----------------------------------------------------------------------
    def onCloseOtherFrame(self, otherFrame):
        """"""
        self.a=0
        otherFrame.destroy()
        self.show()
    #----------------------------------------------------------------------
    def show(self):
        """"""
        self.win.update()
        self.win.deiconify()
#----------------------------------------------------------------------
if __name__ == "__main__":
    win = tk.Tk()
    win.geometry("100x100")
    app = MyApp(win) 
    win.mainloop()