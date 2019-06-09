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
class weatherMyApp(object):
    """"""
    #----------------------------------------------------------------------
    def __init__(self):
        self.month=""
        self.t="微軟正黑體"
        """Constructor"""
        self.win = tk.Tk()
        self.win.geometry("100x100")
        self.win.title("Main frame")
        #圖片呼叫
        self.win.title("PDMS_開始畫面")
        self.data_str=[]#欄位值溫度、舒適度、降雨機率
        self.data_int=[]#溫度、舒適度、降雨機率的數值
#        self.url="新北市"
        self.Combobox_V="新北市"#預設值新北市
        #天氣預報文字敘述網址
        self.data_w={
        '臺北市': 'https://www.cwb.gov.tw/V7/forecast/taiwan/Data/W50_63.txt?', 
        '桃園市': 'https://www.cwb.gov.tw/V7/forecast/taiwan/Data/W50_68.txt?', 
        '臺中市': 'https://www.cwb.gov.tw/V7/forecast/taiwan/Data/W50_66.txt?', 
        '臺南市': 'https://www.cwb.gov.tw/V7/forecast/taiwan/Data/W50_67.txt?', 
        '高雄市': 'https://www.cwb.gov.tw/V7/forecast/taiwan/Data/W50_64.txt?', 
        '基隆市': 'https://www.cwb.gov.tw/V7/forecast/taiwan/Data/W50_10017.txt?', 
        '新竹市': 'https://www.cwb.gov.tw/V7/forecast/taiwan/Data/W50_10018.txt?', 
        '新竹縣': 'https://www.cwb.gov.tw/V7/forecast/taiwan/Data/W50_10004.txt?', 
        '苗栗縣': 'https://www.cwb.gov.tw/V7/forecast/taiwan/Data/W50_10005.txt?', 
        '彰化縣': 'https://www.cwb.gov.tw/V7/forecast/taiwan/Data/W50_10007.txt?', 
        '南投縣': 'https://www.cwb.gov.tw/V7/forecast/taiwan/Data/W50_10008.txt?', 
        '雲林縣': 'https://www.cwb.gov.tw/V7/forecast/taiwan/Data/W50_10009.txt?', 
        '嘉義市': 'https://www.cwb.gov.tw/V7/forecast/taiwan/Data/W50_10020.txt?', 
        '嘉義縣': 'https://www.cwb.gov.tw/V7/forecast/taiwan/Data/W50_10010.txt?', 
        '屏東縣': 'https://www.cwb.gov.tw/V7/forecast/taiwan/Data/W50_10013.txt?', 
        '宜蘭縣': 'https://www.cwb.gov.tw/V7/forecast/taiwan/Data/W50_10002.txt?', 
        '花蓮縣': 'https://www.cwb.gov.tw/V7/forecast/taiwan/Data/W50_10015.txt?', 
        '臺東縣': 'https://www.cwb.gov.tw/V7/forecast/taiwan/Data/W50_10014.txt?', 
        '澎湖縣': 'https://www.cwb.gov.tw/V7/forecast/taiwan/Data/W50_10016.txt?', 
        '金門縣': 'https://www.cwb.gov.tw/V7/forecast/taiwan/Data/W50_09020.txt?', 
        '連江縣': 'https://www.cwb.gov.tw/V7/forecast/taiwan/Data/W50_09007.txt?', 
        '新北市': 'https://www.cwb.gov.tw/V7/forecast/taiwan/Data/W50_65.txt?'
        }
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
        self.openFrame()
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
        #self.url=input("請輸入縣市名稱：")
        #self.r2存天氣預報文字敘述網址，用字典方式拿網址
        self.r2=requests.get(self.data_w[self.url])
        self.r2.encoding='utf8'
        self.soup_2 = BeautifulSoup(self.r2.text,"html.parser")#為解析 HTML 文件的模組
        #print(self.soup_2.text,"\n\n")
        self.r=requests.get("https://www.cwb.gov.tw/V7/forecast/taiwan/"+self.mydict[self.url])
        self.r.encoding='utf8'
        self.soup = BeautifulSoup(self.r.text,"html.parser")
        self.set_Ex = self.soup.select('tbody th')
        self.set_E = self.soup.select('tbody td')
        
        for i in self.set_Ex:
            self.data_str.append(i.text)

        for i in self.set_E:
            self.data_d = str(i.text).strip("\n")
        #    print(data_d+"+"+str(j))
            self.data_int.append(self.data_d)
        #    print(i.text)
        #print(soup.text)
        #print(self.data_str,self.data_int)
        #print("[{:<40s}][{:^10}][{:^18}][{:^12}]".format("新北市","溫度(℃)","舒適度","降雨機率 (%)"))
        #print("[{:<40s}][{:^10}][{:^18}][{:^12}]".format(data_str[0],data_int[0],data_int[2],data_int[3]))
        #print("[{:<40s}][{:^10}][{:^18}][{:^12}]".format(data_str[1],data_int[4],data_int[6],data_int[7]))
        #print("[{:<40s}][{:^10}][{:^18}][{:^12}]".format(data_str[2],data_int[8],data_int[10],data_int[11]))
        
        self.text="{:}\n\n{:}\n{:}{:}\n{:}{:}\n{:}{:}\n\n{:}\n{:}{:}\n{:}{:}\n{:}{:}\n\n{:}\n{:}{:}\n{:}{:}\n{:}{:}".format(self.url,
        self.data_str[0],"溫度(℃)：",self.data_int[0], "舒適度：",self.data_int[2],"降雨機率 (%)：",self.data_int[3],self.data_str[1],
        "溫度(℃)：",self.data_int[4], "舒適度：",self.data_int[6],"降雨機率 (%)：",self.data_int[7],self.data_str[2],"溫度(℃)：",self.data_int[8], 
        "舒適度：",self.data_int[10],"降雨機率 (%)：",self.data_int[11])

        self.texe_c="{:<40}{:<20}{:<20}{:<20}\n\n{:<40}{:<20}{:<20}{:<20}\n\n{:<40}{:<20}{:<20}{:<20}\n\n".format(self.data_str[0],self.data_int[0],self.data_int[2],self.data_int[3],
                                                                                                                  self.data_str[1],self.data_int[4],self.data_int[6],self.data_int[7],
                                                                                                                  self.data_str[2],self.data_int[8],self.data_int[10],self.data_int[11])
        self.texe_t="{:^60}{:^20}{:^20}{:^20}".format(self.url,"溫度(℃)","舒適度","降雨機率 (%)")
        
        #print(self.texe_c)
        label_I=tk.Label(self.wnd, text=self.texe_t, width=70, height=1, font=(self.t,12),anchor = 'w')
        label_I.place(x=10,y=160)
        label_I=tk.Label(self.wnd, text=self.texe_c, width=70, height=9, font=(self.t,12),anchor = 'w')
        label_I.place(x=10,y=180)
#        print(self.text)
        
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
        self.centerwin(self.wnd,800,400)
#        self.wnd.geometry("800x400")
        self.wnd.title("天氣資訊")
        self.wnd.resizable(False,False)
        label_title=tk.Label(self.wnd, text="天氣資訊", width=8, height=1, fg="#5b00ae", font=(self.t,30))
        label_title.place(x=10,y=15)
        #-----------------------------------------------------
        label_c=tk.Label(self.wnd, text="選擇其他縣市：", width=12, height=1, font=(self.t,12))
        label_c.place(x=10,y=80)
        #下拉是選單
        self.Combobox_n = ttk.Combobox(self.wnd,values=['臺北市','新北市','桃園市','臺中市','臺南市',
                                                        '高雄市','基隆市','新竹市','新竹縣','苗栗縣',
                                                        '彰化縣','南投縣','雲林縣','嘉義市','嘉義縣',
                                                        '屏東縣','宜蘭縣','花蓮縣','臺東縣','澎湖縣',
                                                        '金門縣','連江縣']
                                                        , width=15, height=3)
        self.Combobox_n.place(x=10, y=110)
        self.Combobox_n.current(1)
        self.Combobox_n.bind("<<ComboboxSelected>>",self.callbackFunc)
        
        self.push_d()
        
    def callbackFunc(self,even):
        self.Combobox_V = self.Combobox_n.get()
        print(self.Combobox_V)
        self.push_d()
        #---------------------------------------------------------------
        
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
    app = weatherMyApp() 
    
