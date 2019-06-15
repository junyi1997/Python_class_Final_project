# -*- coding: utf-8 -*-
import tkinter as tk
import datetime
import requests #產生HTTP的請求
from bs4 import BeautifulSoup

########################################################################
class invoiceMyApp(object):
    """"""
    #----------------------------------------------------------------------
    def __init__(self):
        self.month=""
        self.t="微軟正黑體"
        """Constructor"""        
        #取月份
        self.now_time = datetime.datetime.now()
        self.now_time =str(self.now_time).split("-")
#        print(self.now_time)
        self.yy=int(self.now_time[0])-1911
        self.mm=int(self.now_time[1])
        if self.mm % 2 == 0:
            self.mm = self.mm-3
        else:
            self.mm = self.mm-2
#        print("{:}{:02}".format(self.yy, self.mm))
        self.url="{:}{:02}".format(self.yy, self.mm)
        
        self.data_dict={
          "特別獎":"同期統一發票收執聯8位數號碼與特別獎號碼相同者獎金1,000萬元",
          "特獎":"同期統一發票收執聯8位數號碼與特獎號碼相同者獎金200萬元",
          "頭獎":"同期統一發票收執聯8位數號碼與頭獎號碼相同者獎金20萬元",
          "二獎":"同期統一發票收執聯末7 位數號碼與頭獎中獎號碼末7 位相同者各得獎金4萬元",
          "三獎":"同期統一發票收執聯末6 位數號碼與頭獎中獎號碼末6 位相同者各得獎金1萬元",
          "四獎":"同期統一發票收執聯末5 位數號碼與頭獎中獎號碼末5 位相同者各得獎金4千元",
          "五獎":"同期統一發票收執聯末4 位數號碼與頭獎中獎號碼末4 位相同者各得獎金1千元",
          "六獎":"同期統一發票收執聯末3 位數號碼與 頭獎中獎號碼末3 位相同者各得獎金2百元",
          "領獎注意事項":"1.領獎期間自108年4月6日起至108年7月5日止，中獎人請於領獎期間攜帶國民身分證(非本國國籍人士得以護照、居留證或內政部移民署核發入出境許可證等替代)及中獎統一發票，依代發獎金單位公告之兌獎營業時間臨櫃兌領，逾期不得領獎。\n2.統一發票未依規定載明金額者，不得領獎。 \n3.統一發票買受人為政府機關、公營事業、公立學校、部隊及營業人者，不得領獎。 \n4.中四獎(含)以上者，依規定應由發獎單位扣繳20﹪所得稅款。 \n5.中五獎(含)以上者，依規定應繳納0.4%印花稅款。 \n6.中獎之統一發票，每張按其最高中獎獎別限領1 個獎金。 \n7.詳細領獎規定，請查閱「統一發票給獎辦法」。若有疑義，請洽財金公司客服專線：4128282(手機請撥：02-4128282)，或至財金公司網站查詢。"
        }
        self.my_main()
        
        self.wnd=tk.Toplevel()
        self.centerwin(self.wnd,600,400)
#        self.wnd.geometry("600x400")
        self.wnd.title("發票兌獎")
        self.wnd.resizable(False,False)
        label_title=tk.Label(self.wnd, text="發票兌獎", width=8, height=1, fg="#5b00ae", font=(self.t,30))
        label_title.place(x=10,y=15)
        #-----------------------------------------------------
        self.label_month=tk.Label(self.wnd, text=self.mmonth, bg="#CCCCFF", font=(self.t, 14))
        self.label_month.place(x = 50, y = 90, width=500, height=50)#, 'bold'
        self.label_SpecialA=tk.Label(self.wnd, text=self.SpecialAA, bg="#CCCCFF", font=(self.t, 14))#, height=2, width=100
        self.label_SpecialA.place(x = 50, y = 150, width=500, height=50)#, 'bold'
        self.label_SpecialB=tk.Label(self.wnd, text=self.SpecialBB, bg="#CCCCFF", font=(self.t, 14))#, height=2, width=100
        self.label_SpecialB.place(x = 50, y = 210, width=500, height=50)#, 'bold'
        self.label_First=tk.Label(self.wnd, text=self.Firstt, bg="#CCCCFF", font=(self.t, 14))#, height=2, width=100
        self.label_First.place(x = 50, y = 270, width=500, height=50)#, 'bold'
        self.label_Add=tk.Label(self.wnd, text=self.aadd, bg="#CCCCFF", font=(self.t, 14))#, height=2, width=100
        self.label_Add.place(x = 50, y = 330, width=500, height=50)#, 'bold'

        self.wnd.mainloop()
    def my_main(self):
        self.r=requests.get('https://www.etax.nat.gov.tw/etw-main/web/ETW183W2_'+self.url+'/')
        self.invoice_Data()

    def invoice_Data(self):
        self.r.encoding='utf8'
        self.soup = BeautifulSoup(self.r.text,"html.parser")
        self.set_invoice = self.soup.select('tbody tr')
        self.my_content=[]
        self.invoice_dict={}
        self.my_title=['月份', '特別獎', '特獎', '頭獎', '二獎', '三獎', '四獎', '五獎', '六獎', '增開六獎', '領獎注意事項']
        
        self.j=0
        for self.i in self.set_invoice:
            self.j = self.j + 1
        #    my_title.append(i.text)
            self.data = str(self.i.text).strip('\n')
            self.data = self.data.split('\n')
            self.my_content.append(self.data)
        #print(my_content)
          
        self.total="月份：{:}\n\n特別獎：{:}\n　　　{:}\n\n特獎：{:}\n　　　{:}\n\n頭獎：{:}\n　　　{:}\n\n二獎：{:}\n\n三獎：{:}\n\n四獎：{:}\n\n五獎：{:}\n\n六獎：{:}\n\n增開六獎：{:}\n\n領獎注意事項：\n{:}".format(self.my_content[0][1],self.my_content[1][1],self.data_dict["特別獎"],self.my_content[3][1],self.data_dict["特獎"],self.my_content[5][1],self.data_dict["頭獎"],self.data_dict["二獎"],self.data_dict["三獎"],self.data_dict["四獎"],self.data_dict["五獎"],self.data_dict["六獎"],self.my_content[12][1],self.data_dict["領獎注意事項"])

        self.mmonth="月份：" + self.my_content[0][1]
        self.SpecialAA="特別獎：" + self.my_content[1][1]
        self.SpecialBB="特獎：" + self.my_content[3][1]
        self.Firstt="頭獎：" + self.my_content[5][1]
        self.aadd="增開六獎：" + self.my_content[12][1]
    
    #---------------------------------------------------------------------
    def centerwin(self,wnd, win_w, win_h):
        self.left = (self.wnd.winfo_screenwidth()-win_w)//2
        self.top = (self.wnd.winfo_screenheight()-win_h)//2
        self.wnd.geometry("{:}x{:}+{:}+{:}".format(win_w,win_h,self.left,self.top))

#----------------------------------------------------------------------
if __name__ == "__main__":
    app = invoiceMyApp() 
    