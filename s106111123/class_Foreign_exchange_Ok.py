# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
#剩下對齊
import tkinter as tk
from tkinter import ttk
import datetime
from PIL import Image,ImageTk
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import requests #產生HTTP的請求
from bs4 import BeautifulSoup


########################################################################
class ForeignMyApp(object):
    """"""
    #----------------------------------------------------------------------
    def __init__(self):
        self.t="微軟正黑體"
        """Constructor"""
        self.win = tk.Tk()
        self.win.geometry("100x100")
        self.win.title("Main frame")
        #圖片呼叫
        self.win.title("PDMS_開始畫面")
        self.cou="TWD"
        self.data=[]#原始匯率(未經整理)
        self.country=[]#國家名TWD, USD, CNY, JPY...
        self.country_data=[]#匯率
        self.num=0
        self.money=1.0
        self.ans_val=""
        self.r=requests.get('https://www.findrate.tw/converter.php#.XOosO4gzZPY')
        self.r.encoding='utf8'
        self.soup = BeautifulSoup(self.r.text,"html.parser")
        self.set_ExchangeRate = self.soup.select('table tr')
        for i in self.set_ExchangeRate:
            self.num+=1
            self.temp=i.text
            self.temp=self.temp.strip("\n")
            self.data.append(self.temp)
            #self.num >= 3 要切掉不要的資料
            if self.num >= 3:
                self.country_data.append(self.temp.split("\n"))
        #print(self.country_data)
        #print(self.data)
        self.country=self.data[1].split("\n")
        #print(self.country)
        self.coin={
            "新台幣":"TWD",
            "美元":"USD",
            "人民幣":"CNY",
            "日圓":"JPY" ,
            "澳幣":"AUD" ,
            "歐元":"EUR" ,
            "港幣":"HKD" ,
            "英鎊":"GBP" ,
            "加幣":"CAD" ,
            "泰銖":"THB" ,
            "南韓圜":"KRW" ,
            }
        self.country_name=["新台幣","美元","人民幣","日圓","澳幣","歐元","港幣","英鎊","加幣","泰銖","南韓圜"]
        self.openFrame()
        self.win.mainloop()
    def Change(self):
        #self.cou=input("請輸入國家:")
        #self.change=input("轉換為:")
        #self.money=input("請輸入金額：")
        self.cou=self.coin[self.Combobox_country.get()]
        self.change=self.coin[self.Combobox_country_turn.get()]
        self.money=self.txtEntry_monty.get()
        #print(self.cou,self.change,self.money)
        if self.cou== "":
            self.cou="TWD"

        if self.money.isdigit()==True and float(self.money)>=0.0:
            self.money=float(self.money)
        else:
            self.money=1.0

            
        self.exchange_money={
            "TWD":self.country_data[0][1],
            "USD":self.country_data[0][2],
            "CNY":self.country_data[0][3],
            "JPY":self.country_data[0][4],
            "AUD":self.country_data[0][5],
            "EUR":self.country_data[0][6],
            "HKD":self.country_data[0][7],
            "GBP":self.country_data[0][8],
            "CAD":self.country_data[0][9],
            "THB":self.country_data[0][10],
            "KRW":self.country_data[0][11],
                            }
         #print(self.exchange_money[self.cou],self.exchange_money[self.change])
         #計算外匯
        if self.cou == self.change == "TWD":
            self.ans=self.money * float(self.exchange_money[self.cou])
        else:
            self.ans=self.money / float(self.exchange_money[self.cou]) * float(self.exchange_money[self.change])
        self.ans_val="計算結果為：{:.2f}".format(self.ans)
        #print("{:.2f}".format(self.ans))
        #print(self.ans_val)
        
        self.Label_result=tk.Label(self.wnd, text=self.ans_val, width=20 ,height=1, font=(self.t,14), fg="#FF0000",anchor = 'w')
        self.Label_result.place(x=100, y=200)


    def onEntryFocusIn(self,ev,objec):
       #print("on fount...") 
        objec.set("")
     
    def my_main(self):
        #self.wnd.option_add("*Font","微軟正黑體 16 normal")
        self.Change()
    
    #---------------------------------------------------------------------
    def centerwin(self,wnd, win_w, win_h):
        self.left = (self.wnd.winfo_screenwidth()-win_w)//2
        self.top = (self.wnd.winfo_screenheight()-win_h)//2
        self.wnd.geometry("{:}x{:}+{:}+{:}".format(win_w,win_h,self.left,self.top))
    
    #----------------------------------------------------------------------
    def hide(self):
        """"""
        self.win.withdraw()
    #---------------------------------------------------------------------- 
    def openFrame(self):
        
        """"""
        self.hide()
        self.wnd=tk.Toplevel()
        self.centerwin(self.wnd,500,400)
        #self.wnd.geometry("500x400")
        self.wnd.title("外幣匯率轉換")
        self.wnd.resizable(False,False)
        self.label_title=tk.Label(self.wnd, text="外幣匯率轉換", width=10, height=1, fg="#5151a2", font=(self.t,30))
        self.label_title.place(x=10,y=15)
        
        self.Label_exchange=tk.Label(self.wnd, text="兌換成", width=7,height=1, font=(self.t,12))
        self.Label_exchange.place(x=210, y=100)
        
        self.Label_money=tk.Label(self.wnd, text="兌換金額", width=7,height=1, font=(self.t,12))
        self.Label_money.place(x=80, y=150)
        
        self.strEntry_monty=tk.StringVar()
        self.strEntry_monty.set("請輸入兌換金額...")
        self.txtEntry_monty=tk.Entry(self.wnd,textvariable=self.strEntry_monty, width=18, font=(self.t,12))
        self.txtEntry_monty.bind("<FocusIn>",lambda x:self.onEntryFocusIn(x,self.strEntry_monty))
        self.txtEntry_monty.place(x=170, y=150)
        
        self.Button_change_val=tk.Button(self.wnd, text="轉換", width=7, height=1, command=self.Change)#lambda :self.change()
        self.Button_change_val.place(x=350, y=150)
        
        #下拉式選單(原始)
        self.Combobox_country = ttk.Combobox(self.wnd,values=self.country_name, font=(self.t,12), width=18)
        self.Combobox_country.bind("<<ComboboxSelected>>", self.Combobox_country.get())
        self.Combobox_country.place(x=20, y=100)
        self.Combobox_country.current(0)
        
        #下拉式選單(被轉)
        self.Combobox_country_turn = ttk.Combobox(self.wnd,values=self.country_name, font=(self.t,12), width=18)
        self.Combobox_country_turn.bind("<<ComboboxSelected>>", self.Combobox_country_turn.get())
        self.Combobox_country_turn.place(x=300, y=100)
        self.Combobox_country_turn.current(0)
             
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
    
    app = ForeignMyApp() 
