
import tkinter as tk
import datetime
from PIL import Image,ImageTk
import requests #產生HTTP的請求
from bs4 import BeautifulSoup


########################################################################
class Myrequests(object):
    """"""
    #----------------------------------------------------------------------
    def __init__(self):
        self.total=""
        self.t="微軟正黑體"
        """Constructor"""

#        but_Log=tk.Button(self.win, command=lambda:self.openFrame()) 
#        but_Log.place(x=0,y=0,width=40,height=40)
        self.url=""
        self.now_time = datetime.datetime.now()#系統日期
        self.now_time=str(self.now_time).split(" ")#print(time_dict["now_time"])
        self.my_URL={
                '金牛座': ['http://astro.click108.com.tw/daily_1.php?iAcDay=','&iAstro=1'],
                '雙子座': ['http://astro.click108.com.tw/daily_2.php?iAcDay=','&iAstro=2'], 
                '巨蠍座': ['http://astro.click108.com.tw/daily_3.php?iAcDay=','&iAstro=3'], 
                '獅子座': ['http://astro.click108.com.tw/daily_4.php?iAcDay=','&iAstro=4'], 
                '處女座': ['http://astro.click108.com.tw/daily_5.php?iAcDay=','&iAstro=5'], 
                '天秤座': ['http://astro.click108.com.tw/daily_6.php?iAcDay=','&iAstro=6'], 
                '天蠍座': ['http://astro.click108.com.tw/daily_7.php?iAcDay=','&iAstro=7'], 
                '射手座': ['http://astro.click108.com.tw/daily_8.php?iAcDay=','&iAstro=8'], 
                '摩羯座': ['http://astro.click108.com.tw/daily_9.php?iAcDay=','&iAstro=9'], 
                '水瓶座': ['http://astro.click108.com.tw/daily_10.php?iAcDay=','&iAstro=10'], 
                '雙魚座': ['http://astro.click108.com.tw/daily_11.php?iAcDay=','&iAstro=11'],
                '牡羊座': ['http://astro.click108.com.tw/daily_0.php?iAcDay=','&iAstro=0']
                }
        self.wnd=tk.Toplevel()
        self.centerwin(self.wnd,1020,400)
#        self.wnd.geometry("1020x400")
        self.wnd.title("星座占卜")
        self.wnd.resizable(False,False)
        label_title=tk.Label(self.wnd, text="星座占卜", width=8, height=1, fg="#8A2BE2", font=(self.t,30))
        label_title.place(x=10,y=15)
        #摩羯座----------------------------------------------------------------------------------------------
        self.摩羯座_img = Image.open(r".\s106111123\12requests\摩羯座.png")
        self.摩羯座_img = self.摩羯座_img.resize((80,80), Image.ANTIALIAS)#符合Button大小的圖示
        self.摩羯座_photoImg = ImageTk.PhotoImage(self.摩羯座_img)
        摩羯座_Bt=tk.Button(self.wnd , text = "摩羯座",image=self.摩羯座_photoImg, width=80, height=80,command=lambda:self.my_main("摩羯座"))
        摩羯座_Bt.place(x=20,y=90)
        #---------------------------------------------------------------------------------------------------
        #水瓶座----------------------------------------------------------------------------------------------
        self.水瓶座_img = Image.open(r".\s106111123\12requests\水瓶座.png")
        self.水瓶座_img = self.水瓶座_img.resize((80,80), Image.ANTIALIAS)
        self.水瓶座_photoImg = ImageTk.PhotoImage(self.水瓶座_img)
        水瓶座_Bt=tk.Button(self.wnd , text = "水瓶座", image=self.水瓶座_photoImg, width=80, height=80,command=lambda:self.my_main("水瓶座"))
        水瓶座_Bt.place(x=110,y=90)
        #---------------------------------------------------------------------------------------------------
        #雙魚座----------------------------------------------------------------------------------------------
        self.雙魚座_img = Image.open(r".\s106111123\12requests\雙魚座.png")
        self.雙魚座_img = self.雙魚座_img.resize((80,80), Image.ANTIALIAS)
        self.雙魚座_photoImg = ImageTk.PhotoImage(self.雙魚座_img)
        雙魚座_Bt=tk.Button(self.wnd , text = "雙魚座", image=self.雙魚座_photoImg, width=80, height=80,command=lambda:self.my_main("雙魚座"))
        雙魚座_Bt.place(x=200,y=90)
        #---------------------------------------------------------------------------------------------------
        #牡羊座----------------------------------------------------------------------------------------------
        self.牡羊座_img = Image.open(r".\s106111123\12requests\牡羊座.png")
        self.牡羊座_img =self.牡羊座_img.resize((80,80), Image.ANTIALIAS)
        self.牡羊座_photoImg = ImageTk.PhotoImage(self.牡羊座_img)
        牡羊座_Bt=tk.Button(self.wnd , text = "牡羊座", image=self.牡羊座_photoImg, width=80, height=80,command=lambda:self.my_main("牡羊座"))
        牡羊座_Bt.place(x=290,y=90)
        #---------------------------------------------------------------------------------------------------
        #金牛座----------------------------------------------------------------------------------------------
        self.金牛座_img = Image.open(r".\s106111123\12requests\金牛座.png")
        self.金牛座_img = self.金牛座_img.resize((80,80), Image.ANTIALIAS)
        self.金牛座_photoImg = ImageTk.PhotoImage(self.金牛座_img)
        金牛座_Bt=tk.Button(self.wnd , text = "金牛座", image=self.金牛座_photoImg, width=80, height=80,command=lambda:self.my_main("金牛座"))
        金牛座_Bt.place(x=20,y=180)
        #---------------------------------------------------------------------------------------------------
        #雙子座----------------------------------------------------------------------------------------------
        self.雙子座_img = Image.open(r".\s106111123\12requests\雙子座.png")
        self.雙子座_img = self.雙子座_img.resize((80,80), Image.ANTIALIAS)
        self.雙子座_photoImg = ImageTk.PhotoImage(self.雙子座_img)
        雙子座_Bt=tk.Button(self.wnd , text = "雙子座", image=self.雙子座_photoImg, width=80, height=80,command=lambda:self.my_main("雙子座"))
        雙子座_Bt.place(x=110,y=180)
        #---------------------------------------------------------------------------------------------------
        #巨蠍座----------------------------------------------------------------------------------------------
        self.巨蠍座_img = Image.open(r".\s106111123\12requests\巨蠍座.png")
        self.巨蠍座_img =self.巨蠍座_img.resize((80,80), Image.ANTIALIAS)
        self.巨蠍座_photoImg = ImageTk.PhotoImage(self.巨蠍座_img)
        巨蠍座_Bt=tk.Button(self.wnd , text = "巨蠍座", image=self.巨蠍座_photoImg, width=80, height=80,command=lambda:self.my_main("巨蠍座"))
        巨蠍座_Bt.place(x=200,y=180)
        #---------------------------------------------------------------------------------------------------
        #獅子座----------------------------------------------------------------------------------------------
        self.獅子座_img = Image.open(r".\s106111123\12requests\獅子座.png")
        self.獅子座_img =self.獅子座_img.resize((80,80), Image.ANTIALIAS)
        self.獅子座_photoImg =  ImageTk.PhotoImage(self.獅子座_img)
        獅子座_Bt=tk.Button(self.wnd , text = "獅子座", image=self.獅子座_photoImg, width=80, height=80,command=lambda:self.my_main("獅子座"))
        獅子座_Bt.place(x=290,y=180)
        #---------------------------------------------------------------------------------------------------
        #處女座----------------------------------------------------------------------------------------------
        self.處女座_img = Image.open(r".\s106111123\12requests\處女座.png")
        self.處女座_img =self.處女座_img.resize((80,80), Image.ANTIALIAS)
        self.處女座_photoImg = ImageTk.PhotoImage(self.處女座_img)
        處女座_Bt=tk.Button(self.wnd , text = "處女座", image=self.處女座_photoImg, width=80, height=80,command=lambda:self.my_main("處女座"))
        處女座_Bt.place(x=20,y=270)
        #---------------------------------------------------------------------------------------------------
        #天秤座----------------------------------------------------------------------------------------------
        self.天秤座_img = Image.open(r".\s106111123\12requests\天秤座.png")
        self.天秤座_img =self.天秤座_img.resize((80,80), Image.ANTIALIAS)
        self.天秤座_photoImg = ImageTk.PhotoImage(self.天秤座_img)
        天秤座_Bt=tk.Button(self.wnd , text = "天秤座", image=self.天秤座_photoImg, width=80, height=80,command=lambda:self.my_main("天秤座"))
        天秤座_Bt.place(x=110,y=270)
        #---------------------------------------------------------------------------------------------------
        #天蠍座----------------------------------------------------------------------------------------------
        self.天蠍座_img = Image.open(r".\s106111123\12requests\天蠍座.png")
        self.天蠍座_img =self.天蠍座_img.resize((80,80), Image.ANTIALIAS)
        self.天蠍座_photoImg = ImageTk.PhotoImage(self.天蠍座_img)
        天蠍座_Bt=tk.Button(self.wnd , text = "天蠍座", image=self.天蠍座_photoImg, width=80, height=80,command=lambda:self.my_main("天蠍座"))
        天蠍座_Bt.place(x=200,y=270)
        #---------------------------------------------------------------------------------------------------
        #射手座----------------------------------------------------------------------------------------------
        self.射手座_img = Image.open(r".\s106111123\12requests\射手座.png")
        self.射手座_img =self.射手座_img.resize((80,80), Image.ANTIALIAS)
        self.射手座_photoImg = ImageTk.PhotoImage(self.射手座_img)
        射手座_Bt=tk.Button(self.wnd , text = "射手座", image=self.射手座_photoImg, width=80, height=80,command=lambda:self.my_main("射手座"))
        射手座_Bt.place(x=290,y=270)
        #--------------------------------------------------------------------------------------------------
        #圖片路徑
        self.my_picture={
                '金牛座': tk.PhotoImage(file=r".\s106111123\12requests\金牛座.png"),
                '雙子座': tk.PhotoImage(file=r".\s106111123\12requests\雙子座.png"),
                '巨蠍座': tk.PhotoImage(file=r".\s106111123\12requests\巨蠍座.png"),
                '獅子座': tk.PhotoImage(file=r".\s106111123\12requests\獅子座.png"),
                '處女座': tk.PhotoImage(file=r".\s106111123\12requests\處女座.png"),
                '天秤座': tk.PhotoImage(file=r".\s106111123\12requests\天秤座.png"),
                '天蠍座': tk.PhotoImage(file=r".\s106111123\12requests\天蠍座.png"),
                '射手座': tk.PhotoImage(file=r".\s106111123\12requests\射手座.png"),
                '摩羯座': tk.PhotoImage(file=r".\s106111123\12requests\摩羯座.png"),
                '水瓶座': tk.PhotoImage(file=r".\s106111123\12requests\水瓶座.png"),
                '雙魚座': tk.PhotoImage(file=r".\s106111123\12requests\雙魚座.png"),
                '牡羊座': tk.PhotoImage(file=r".\s106111123\12requests\牡羊座.png")
                }
        #Text
        self.T = tk.Text(self.wnd, height=2, width=30, font=(self.t, 14))#, 'bold'
        self.T.place(x = 400, y = 55, width=600,height=300)
        
        #滾輪
        self.scrollb = tk.Scrollbar(self.wnd, orient="vertical")
        self.scrollb.place(x=1000, y=55, height=300)#,anchor=tk.NE
        self.scrollb.config(command=self.T.yview)
        self.T.config(yscrollcommand = self.scrollb.set)
        #---------------------------------------------------------------------------------------------------
        self.wnd.mainloop()
        
    def my_main(self,vvv):
        self.T.config(state='normal')#智能打開
        self.T.delete(1.0,tk.END)#清空text
        self.T.image_create(tk.END, image=self.my_picture[vvv])#圖片
#        print("vvv",vvv)
        #vvv星座名稱
        self.url=vvv
#        print(self.my_URL[self.url][0]+self.now_time[0]+self.my_URL[self.url][1])
        self.new_url=self.my_URL[self.url][0]+self.now_time[0]+self.my_URL[self.url][1]
        self.set_requests()
   
    def set_requests(self): 
    
        r=requests.get(self.new_url)
        r.encoding='utf8'
        #今日星座解析
        soup = BeautifulSoup(r.text,"html.parser")
        set_constellation = soup.select('div.TODAY_CONTENT h3')#print(type(set_constellation))
        set_constellation = str(set_constellation).strip("[<h3></h3>]")#print("結果：",set_constellation,"\n")
        set_overall_content = soup.select('div.TODAY_CONTENT p')
        set_overal2_content = soup.select('div.TODAY_CONTENT h3')
        set_Today_Word = soup.select('div.TODAY_WORD')
        
        for i in set_overal2_content:
            title_temp=i.text
        #print(title_temp)
        for temp in set_Today_Word:
            Today_Word = temp.text
            Today_Word=Today_Word.strip("\n")
        #print(Today_Word)
            
        Today_Lucky =[]
        set_Today_Lucky = soup.select('div.TODAY_LUCKY h4')
        for temp in set_Today_Lucky:
            Today_Lucky.append(temp.text)
         #print(Today_Lucky)#數字、顏色、方位、時間、星座
         #print("整體運勢：",set_overall_content[0].text,'\n',set_overall_content[1].text)
         #print("愛情運勢：",set_overall_content[2].text,'\n',set_overall_content[3].text)
         #print("事業運勢：",set_overall_content[4].text,'\n',set_overall_content[5].text)
         #print("財運運勢：",set_overall_content[6].text,'\n',set_overall_content[7].text,'\n\n')
         #print("{:}　　　　　　　　　　　　{:}　　　　　　　　　　　　幸運數字：{:}\n\n　　　　　　　　　　　　幸運顏色：{:}\n\n　　　　　　　　　　　　開運方位：{:}\n\n　　　　　　　　　　　　今日吉時：{:}\n\n　　　　　　　　　　　　幸運星座：{:}\n\n整體運勢：{:}\n\n愛情運勢：{:}\n\n事業運勢：{:}\n\n財運運勢：{:}".format(123,Today_Word,Today_Lucky[0],Today_Lucky[1],Today_Lucky[2],Today_Lucky[3],Today_Lucky[4],set_overall_content[0].text+'\n\n　　'+set_overall_content[1].text,set_overall_content[2].text+'\n\n　　'+set_overall_content[3].text,set_overall_content[4].text+'\n\n　　'+set_overall_content[5].text,set_overall_content[6].text+'\n\n　　'+set_overall_content[7].text))
        
        self.total="{:}\n\n今日短評：{:}\n\n幸運數字：{:}\n\n幸運顏色：{:}\n\n開運方位：{:}\n\n今日吉時：{:}\n\n幸運星座：{:}\n\n整體運勢：{:}\n\n愛情運勢：{:}\n\n事業運勢：{:}\n\n財運運勢：{:}\n".format(title_temp,Today_Word,Today_Lucky[0],Today_Lucky[1],Today_Lucky[2],Today_Lucky[3],Today_Lucky[4],set_overall_content[0].text+'\n\n　　'+set_overall_content[1].text,set_overall_content[2].text+'\n\n　　'+set_overall_content[3].text,set_overall_content[4].text+'\n\n　　'+set_overall_content[5].text,set_overall_content[6].text+'\n\n　　'+set_overall_content[7].text)
        self.T.insert(tk.END,self.total)
        self.T.config(state=tk.DISABLED)
        
    #---------------------------------------------------------------------
    def centerwin(self,wnd, win_w, win_h):#畫面置中
        self.left = (self.wnd.winfo_screenwidth()-win_w)//2
        self.top = (self.wnd.winfo_screenheight()-win_h)//2
        self.wnd.geometry("{:}x{:}+{:}+{:}".format(win_w,win_h,self.left,self.top))

#----------------------------------------------------------------------
if __name__ == "__main__":
    app = Myrequests() 