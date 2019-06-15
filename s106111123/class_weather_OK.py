# -*- coding: utf-8 -*-
#剩下對齊
import tkinter as tk
from tkinter import ttk
import requests #產生HTTP的請求
from bs4 import BeautifulSoup

########################################################################
class Myweather(object):
    """"""
    #----------------------------------------------------------------------
    def __init__(self):
        self.month=""
        self.t="微軟正黑體"
        """Constructor"""
        
        self.data_str=[]#欄位值溫度、舒適度、降雨機率
        self.data_int=[]#溫度、舒適度、降雨機率的數值
        #self.url="新北市"
        self.Combobox_V="新北市"#預設值新北市

        #天氣資訊網址
        self.mydict={
        '臺北市': 'Taipei_City.htm', 
        '桃園市': 'Taoyuan_City.htm', 
        '臺中市': 'Taichung_City.htm', 
        '臺南市': 'Tainan_City.htm', 
        '高雄市': 'Kaohsiung_City.htm', 
        '基隆市': 'Keelung_City.htm', 
        '新竹市': 'Hsinchu_City.htm', 
        '新竹縣': 'Hsinchu_County.htm', 
        '苗栗縣': 'Miaoli_County.htm', 
        '彰化縣': 'Changhua_County.htm', 
        '南投縣': 'Nantou_County.htm', 
        '雲林縣': 'Yunlin_County.htm', 
        '嘉義市': 'Chiayi_City.htm', 
        '嘉義縣': 'Chiayi_County.htm', 
        '屏東縣': 'Pingtung_County.htm', 
        '宜蘭縣': 'Yilan_County.htm', 
        '花蓮縣': 'Hualien_County.htm', 
        '臺東縣': 'Taitung_County.htm', 
        '澎湖縣': 'Penghu_County.htm', 
        '金門縣': 'Kinmen_County.htm', 
        '連江縣': 'Lienchiang_County.htm', 
        '新北市': 'New_Taipei_City.htm'
        }
        self.win=tk.Toplevel()
        self.centerwin(self.win,725,400)
        #self.win.geometry("800x400")
        self.win.title("天氣資訊")
        self.win.resizable(False,False)
        label_title=tk.Label(self.win, text="天氣資訊", width=8, height=1, fg="#0080ff", font=(self.t,30))
        label_title.place(x=10,y=15)
        #-----------------------------------------------------
        label_c=tk.Label(self.win, text="選擇其他縣市：", width=12, height=1, font=(self.t,14))
        label_c.place(x=10,y=80)
        #下拉式選單
        self.Combobox_n = ttk.Combobox(self.win,values=['臺北市','新北市','桃園市','臺中市','臺南市',
                                                        '高雄市','基隆市','新竹市','新竹縣','苗栗縣',
                                                        '彰化縣','南投縣','雲林縣','嘉義市','嘉義縣',
                                                        '屏東縣','宜蘭縣','花蓮縣','臺東縣','澎湖縣',
                                                        '金門縣','連江縣']
                                                        , width=15, height=3, font=(self.t,14))
        self.Combobox_n.place(x=10, y=110)
        self.Combobox_n.current(1)
        self.Combobox_n.bind("<<ComboboxSelected>>",self.callbackFunc)
        
        self.push_d()
        self.win.mainloop()
    def my_main(self):
        self.push_d()
  
    def push_d(self):
        #初始化----------
        self.data_str=[]
        self.data_int=[]
        
        #爬蟲------------
        #self.url存使用者點選的縣市
        self.url=self.Combobox_V
 
        self.r=requests.get("https://www.cwb.gov.tw/V7/forecast/taiwan/"+self.mydict[self.url])
        self.r.encoding='utf8'
        self.soup = BeautifulSoup(self.r.text,"html.parser")
        self.set_Ex = self.soup.select('tbody th')
        self.set_E = self.soup.select('tbody td')
        
        for i in self.set_Ex:
            self.data_str.append(i.text)

        for i in self.set_E:
            self.data_d = str(i.text).strip("\n")
            self.data_int.append(self.data_d)

        #-------------
        tree=ttk.Treeview(self.win,show="headings")#表格
        style = ttk.Style()
        style.configure("Treeview.Heading", font=("微軟正黑體", 14))
        style.configure("Treeview", font=("微軟正黑體", 14))
        self.name=self.url
        tree["columns"]=(self.name,"溫度(℃)","舒適度","降雨機率 (%)")
        tree.column(self.name,width=350 )
        tree.column("溫度(℃)",width=100,anchor='center' )   #表示列,不顯示
        tree.column("舒適度",width=100,anchor='center')
        tree.column("降雨機率 (%)",width=150,anchor='center')
        tree.heading(self.name,text=self.name)  #顯示表頭
        tree.heading("溫度(℃)",text="溫度(℃)")  
        tree.heading("舒適度",text="舒適度")
        tree.heading("降雨機率 (%)",text="降雨機率 (%)")
         
        tree.insert("",0,text="line1" ,values=(self.data_str[0],self.data_int[0],self.data_int[2],self.data_int[3])) #插入数据，
        tree.insert("",1,text="line1" ,values=(self.data_str[1],self.data_int[4],self.data_int[6],self.data_int[7]))
        tree.insert("",2,text="line1" ,values=(self.data_str[2],self.data_int[8],self.data_int[10],self.data_int[11]))
        tree.place(x=10, y=150)
    #---------------------------------------------------------------------
    def centerwin(self,win, win_w, win_h):
        self.left = (self.win.winfo_screenwidth()-win_w)//2
        self.top = (self.win.winfo_screenheight()-win_h)//2
        self.win.geometry("{:}x{:}+{:}+{:}".format(win_w,win_h,self.left,self.top))

    def callbackFunc(self,even):
        self.Combobox_V = self.Combobox_n.get()
        print(self.Combobox_V)
        self.push_d()

#----------------------------------------------------------------------
if __name__ == "__main__":
    app = Myweather() 