import tkinter as tk
import tkinter.messagebox as messagebox
import pickle
from PIL import Image,ImageTk
import BotSpeak
from s106111123.class_Foreign_exchange_OK import MyForeignExchange
from s106111123.class_invoice_OK import invoiceMyApp
from s106111123.class_weather_OK import Myweather
from s106111123.class_requests_OK import Myrequests
from s106111142.memo import Login
import date
import face_pyhon.face as face
########################################################################
class MyApp(object):
    """"""
    #----------------------------------------------------------------------
    def __init__(self):
        self.A=0#定義更改密碼的文字輸入盒的焦點
        """Constructor"""
        self.win = tk.Tk()
        self.win.geometry("600x800")
        self.win.title("Keeping_開始畫面")#定義標題名稱
        left=(self.win.winfo_screenwidth()-600)//2#指定視窗置中
        top=(self.win.winfo_screenheight()-800)//2
        self.win.geometry("{:}x{:}+{:}+{:}".format(600,800,left,top))
        #圖片呼叫
        self.photo_background=tk.PhotoImage(file=r"./image/首頁.png")
        self.photo_Login=tk.PhotoImage(file=r"./image/登入_加背.png")
        self.photo_備忘錄=tk.PhotoImage(file=r"./image/備忘錄.png")
        self.photo_行事曆=tk.PhotoImage(file=r"./image/行事曆.png")
        self.photo_生活小助手=tk.PhotoImage(file=r"./image/生活小助手.png")
        self.photo_日歷=tk.PhotoImage(file=r"./image/日歷_背.png")
        self.photo_使用說明=tk.PhotoImage(file=r"./image/使用說明.png")
        self.photo_管家=tk.PhotoImage(file=r"./image/管家_背.png")
        self.photo_筆記=tk.PhotoImage(file=r"./image/筆記_背.png")
        self.photo_weather=tk.PhotoImage(file=r"./image/天氣預報.png")
        self.photo_tick=tk.PhotoImage(file=r"./image/兌獎查詢.png")
        self.photo_money=tk.PhotoImage(file=r"./image/匯率換算.png")
        self.photo_start=tk.PhotoImage(file=r"./image/星座運勢.png")
        self.photo_使用說明=tk.PhotoImage(file=r"./image/使用說明_背.png")
        self.photo_喇叭=tk.PhotoImage(file=r"./image/喇叭.png")
        
        
        
        canvas_width = 1000#新增一個畫布
        canvas_height =1000
        canvas = tk.Canvas(self.win, 
        width=canvas_width, 
        height=canvas_height)
        canvas.pack()
        #背景
        canvas.create_image(300,400, image=self.photo_background)#將背景貼到畫布上
        
        #選擇使用說明
        but=tk.Button(self.win,image=self.photo_使用說明, command=self.openFrame) 
        but.place(x=410,y=10)
        
        #進入登入畫面
        but_Log=tk.Button(self.win,image=self.photo_Login, command=self.password) 
        but_Log.place(x=200,y=570)
        BotSpeak.speak("歡迎來到KEEPING個人資料管理系統  請點選下方按鍵登入")
        self.win.mainloop()
        BotSpeak.speak("掰掰") 
    #----------------------------------------------------------------------
    def chooseclear(self):
        self.win_ch = tk.Toplevel()
        #使用者關閉視窗觸發的事件（第一個刪除視窗，第二個為函式名，即過程）
        self.win_ch.protocol('WM_DELETE_WINDOW',lambda:self.closeWindow(self.win_ch))
        left=(self.win_ch.winfo_screenwidth()-500)//2
        top=(self.win_ch.winfo_screenheight()-250)//2
        self.win_ch.geometry("{:}x{:}+{:}+{:}".format(500,250,left,top))
        self.win_ch.bg06=tk.PhotoImage(file=r"./image/bg06.png")
        canvas_width = 500
        canvas_height =250
        canvas = tk.Canvas(self.win_ch, 
        width=canvas_width, 
        height=canvas_height)
        canvas.pack()   
        #背景
        canvas.create_image(130,10, image=self.win_ch.bg06)
        def print_selection():
            msg="你所選擇要進入的是{:}系統".format(var.get())
            BotSpeak.speak(msg)
            Ans=tk.messagebox.askyesno(title='小提醒', message='你是否選擇要進入' + var.get()+"的頁面？")
            if Ans:
                if var.get()=="備忘錄":
                    Login()
                    
                elif var.get()=="行事曆":
                    date()
#                    pass
                elif var.get()=="生活小助手":
                    self.openFrame3() 
                    
                self.win_ch.destroy()#關閉畫面
                       
        def chpwd():
            self.usr_sign_up()#更改密碼
              
        var = tk.StringVar()
        l = tk.Label(self.win_ch, bg='yellow', text='選擇要進入之頁面',font= ('Noto Sans Mono CJK TC Regular',20))
        l.place(x=10, y=10)
        btn_chpw = tk.Button(self.win_ch, text='更改密碼', bg='orange',font= ('Noto Sans Mono CJK TC Regular',20),command=chpwd)
        btn_chpw.place(x=250, y=100)
        r1 = tk.Radiobutton(self.win_ch, text='備忘錄',
                            variable=var, value='備忘錄',font= ('Noto Sans Mono CJK TC Regular',16),
                            command=print_selection)
        r1.place(x=50, y=70)

        r2 = tk.Radiobutton(self.win_ch, text='行事曆',
                            variable=var, value='行事曆',font= ('Noto Sans Mono CJK TC Regular',16),
                            command=print_selection)
        r2.place(x=50, y=130)

        r3 = tk.Radiobutton(self.win_ch, text='生活小助手',
                            variable=var, value='生活小助手',font= ('Noto Sans Mono CJK TC Regular',16),
                            command=print_selection)
        r3.place(x=50, y=190)

    def usr_sign_up(self):
        self.A=0
        def sign_to_Mofan_Python():
            np = new_pwd.get()
            npf = new_pwd_confirm.get()
            nn = new_name.get()
            with open('usrs_info.pickle', 'rb') as usr_file:
                exist_usr_info = pickle.load(usr_file)
            if np != npf:
                tk.messagebox.showerror('Error', '兩個密碼不相同')
            #elif nn in exist_usr_info:
            #    tk.messagebox.showerror('Error', '此帳號已存在，請直接登入！')
            else:
                exist_usr_info[nn] = np
                with open('usrs_info.pickle', 'wb') as usr_file:
                    pickle.dump(exist_usr_info, usr_file)
#                tk.messagebox.showinfo('Welcome', '恭喜你已成功更改密碼！')
                BotSpeak.speak("恭喜你已成功更改密碼！")
                win_pw_sign_up.destroy()
        win_pw_sign_up = tk.Toplevel()
        win_pw_sign_up.geometry("500x200+130+130")
        win_pw_sign_up.title('更改密碼')

        new_name = tk.StringVar()
        new_name.set('105103308')
        tk.Label(win_pw_sign_up, text='使用者帳號: ').place(x=10, y= 10)
        entry_new_name = tk.Entry(win_pw_sign_up, textvariable=new_name)
        entry_new_name.place(x=150, y=10)

        new_pwd = tk.StringVar()
        tk.Label(win_pw_sign_up, text='使用者密碼: ').place(x=10, y=50)
        entry_usr_pwd = tk.Entry(win_pw_sign_up, textvariable=new_pwd, show='*')
        entry_usr_pwd.place(x=150, y=50)

        new_pwd_confirm = tk.StringVar()
        tk.Label(win_pw_sign_up, text='重複輸入密碼: ').place(x=10, y= 90)
        entry_usr_pwd_confirm = tk.Entry(win_pw_sign_up, textvariable=new_pwd_confirm, show='*')
        entry_usr_pwd_confirm.place(x=150, y=90)

        btn_comfirm_sign_up = tk.Button(win_pw_sign_up, text='建立', command=sign_to_Mofan_Python)
        btn_comfirm_sign_up.place(x=150, y=130)

        def usr_clear():
            new_name.set('105103308')
            new_pwd_confirm.set('')
            new_pwd.set('')
        # login and sign up button
        btn_login = tk.Button(win_pw_sign_up, text='C',font= ('Noto Sans Mono CJK TC Regular',18), command=usr_clear)
        btn_login.place(x=420, y=130,width=40,height=40)
        self.A=0
        #輸入方塊 A=0-->上面，A=1-->下面
        def btn0():
                
            if self.A==0:
                self.A=1
                buttontext.set('↑')   
                BotSpeak.speak("輸入方塊的焦點在重複輸入密碼")
            elif self.A==1:
                self.A=0 
                BotSpeak.speak("輸入方塊的焦點在輸入密碼")  
                buttontext.set('↓')   
        def btn01():
              
            if self.A==0:
                entry_usr_pwd.insert(tk.END, '1')
            else:
                entry_usr_pwd_confirm.insert(tk.END, '1')

        def btn02():
              
            if self.A==0:
                entry_usr_pwd.insert(tk.END, '2')
            else:
                entry_usr_pwd_confirm.insert(tk.END, '2')
        def btn03():
              
            if self.A==0:
                entry_usr_pwd.insert(tk.END, '3')
            else:
                entry_usr_pwd_confirm.insert(tk.END, '3')
        def btn04():
              
            if self.A==0:
                entry_usr_pwd.insert(tk.END, '4')
            else:
                entry_usr_pwd_confirm.insert(tk.END, '4')
        def btn05():
              
            if self.A==0:
                entry_usr_pwd.insert(tk.END, '5')
            else:
                entry_usr_pwd_confirm.insert(tk.END, '5')
        def btn06():
              
            if self.A==0:
                entry_usr_pwd.insert(tk.END, '6')
            else:
                entry_usr_pwd_confirm.insert(tk.END, '6')
        def btn07():
              
            if self.A==0:
                entry_usr_pwd.insert(tk.END, '7')
            else:
                entry_usr_pwd_confirm.insert(tk.END, '7')
        def btn08():
              
            if self.A==0:
                entry_usr_pwd.insert(tk.END, '8')
            else:
                entry_usr_pwd_confirm.insert(tk.END, '8')
        def btn09():
             
            if self.A==0:
                entry_usr_pwd.insert(tk.END, '9')
            else:
                entry_usr_pwd_confirm.insert(tk.END, '9')
        def btn00():
              
            if self.A==0:
                entry_usr_pwd.insert(tk.END, '0')
            else:
                entry_usr_pwd_confirm.insert(tk.END, '0')
        buttontext = tk.StringVar()
        buttontext.set('↓')   
        btn_login = tk.Button(win_pw_sign_up, textvariable = buttontext,font= ('Noto Sans Mono CJK TC Regular',20), command=btn0)
        btn_login.place(x=340, y=130,width=40,height=40)
        btn_login = tk.Button(win_pw_sign_up, text='0',font= ('Noto Sans Mono CJK TC Regular',20), command=btn00)
        btn_login.place(x=380, y=130,width=40,height=40)
        btn_login = tk.Button(win_pw_sign_up, text='1',font= ('Noto Sans Mono CJK TC Regular',20), command=btn01)
        btn_login.place(x=340, y=90,width=40,height=40)
        btn_login = tk.Button(win_pw_sign_up, text='2',font= ('Noto Sans Mono CJK TC Regular',20), command=btn02)
        btn_login.place(x=380, y=90,width=40,height=40)
        btn_login = tk.Button(win_pw_sign_up, text='3',font= ('Noto Sans Mono CJK TC Regular',20), command=btn03)
        btn_login.place(x=420, y=90,width=40,height=40)
        btn_login = tk.Button(win_pw_sign_up, text='4',font= ('Noto Sans Mono CJK TC Regular',20), command=btn04)
        btn_login.place(x=340, y=50,width=40,height=40)
        btn_login = tk.Button(win_pw_sign_up, text='5',font= ('Noto Sans Mono CJK TC Regular',20), command=btn05)
        btn_login.place(x=380, y=50,width=40,height=40)
        btn_login = tk.Button(win_pw_sign_up, text='6',font= ('Noto Sans Mono CJK TC Regular',20), command=btn06)
        btn_login.place(x=420, y=50,width=40,height=40)
        btn_login = tk.Button(win_pw_sign_up, text='7',font= ('Noto Sans Mono CJK TC Regular',20), command=btn07)
        btn_login.place(x=340, y=10,width=40,height=40)
        btn_login = tk.Button(win_pw_sign_up, text='8',font= ('Noto Sans Mono CJK TC Regular',20), command=btn08)
        btn_login.place(x=380, y=10,width=40,height=40)
        btn_login = tk.Button(win_pw_sign_up, text='9',font= ('Noto Sans Mono CJK TC Regular',20), command=btn09)
        btn_login.place(x=420, y=10,width=40,height=40)
    #---------------------------------------------------------------------- 
    def face_ID(self):
#        print("準備臉部辨識中...")
        BotSpeak.speak("準備臉部辨識中") 
        self.Account=face.my_main()
        print("Account",self.Account)
        with open('usrs_info.pickle', 'rb') as usr_file:
            usrs_info = pickle.load(usr_file)
        if self.Account in usrs_info:
#            tk.messagebox.showinfo(title='歡迎', message='歡迎來到PDMS！ ' + self.Account)
            msg="歡迎來到KEEPING{:}".format(self.Account)
            BotSpeak.speak(msg) 
            self.win_pw.destroy()              
            self.chooseclear()
        
    #----------------------------------------------------------------------
    def password(self):
        BotSpeak.speak("請輸入密碼或者點選#鍵進行臉部辨識") 
        self.hide()
        self.win_pw = tk.Toplevel()
        self.win_pw.title('root')
        left=(self.win_pw.winfo_screenwidth()-500)//2
        top=(self.win_pw.winfo_screenheight()-200)//2
        self.win_pw.geometry("{:}x{:}+{:}+{:}".format(500,200,left,top))
        self.win_pw.bg05=tk.PhotoImage(file=r"./image/bg05.png")
        #使用者關閉視窗觸發的事件（第一個刪除視窗，第二個為函式名，即過程）
        self.win_pw.protocol('WM_DELETE_WINDOW',lambda:self.closeWindow(self.win_pw))
        canvas_width = 500
        canvas_height =200
        canvas = tk.Canvas(self.win_pw, 
        width=canvas_width, 
        height=canvas_height)
        canvas.pack()   
        #背景
        canvas.create_image(130,10, image=self.win_pw.bg05)
        
        # user information
        tk.Label(self.win_pw, text='使用者名稱: ').place(x=50, y= 50)
        tk.Label(self.win_pw, text='使用者密碼: ').place(x=50, y=90)

        var_usr_name = tk.StringVar()
        var_usr_name.set('105103308')
        entry_usr_name = tk.Entry(self.win_pw, textvariable=var_usr_name)
        entry_usr_name.place(x=160, y=50)
        var_usr_pwd = tk.StringVar()
        entry_usr_pwd = tk.Entry(self.win_pw, textvariable=var_usr_pwd, show='*')
        entry_usr_pwd.place(x=160, y=90)

        def usr_login():
            usr_name = var_usr_name.get()
            usr_pwd = var_usr_pwd.get()
            try:
                with open('usrs_info.pickle', 'rb') as usr_file:
                    usrs_info = pickle.load(usr_file)
            except EOFError:
                with open('usrs_info.pickle', 'wb') as usr_file:
                    usrs_info = {'admin': 'admin'}
                    pickle.dump(usrs_info, usr_file)
            if usr_name in usrs_info:
                if usr_pwd == usrs_info[usr_name]:
                    self.Account=usr_name
#                    tk.messagebox.showinfo(title='歡迎', message='歡迎來到PDMS！ ' + usr_name)
                    msg="歡迎來到KEEPING{:}".format(str(usr_name))
                    BotSpeak.speak(msg)
                    #cleardata = tk.messagebox.askyesno('Welcome',
                    #                '是否要清空資料庫？')

                    #if cleardata:  
                    self.win_pw.destroy()              
                    self.chooseclear()
                             
                else:
#                    tk.messagebox.showerror(message='密碼輸入錯誤')
                    BotSpeak.speak("密碼輸入錯誤") 

            else:
#                tk.messagebox.showerror(message='查無此人')
                BotSpeak.speak("查無此人") 
                '''
                is_sign_up = tk.messagebox.askyesno('Welcome',
                                    '無使用者資料，是否創建一個？')
                if is_sign_up:
                    self.usr_sign_up()
                '''
        def usr_clear():
            var_usr_name.set('105103308')
            var_usr_pwd.set('')
        # login and sign up button
        btn_login = tk.Button(self.win_pw, text='登入',font= ('Noto Sans Mono CJK TC Regular',18), command=usr_login)
        btn_login.place(x=150, y=130)
        btn_login = tk.Button(self.win_pw, text='C',font= ('Noto Sans Mono CJK TC Regular',18), command=usr_clear)
        btn_login.place(x=420, y=130,width=40,height=40)

        def btn01():
            entry_usr_pwd.insert(tk.END, '1')
        def btn02():
            entry_usr_pwd.insert(tk.END, '2')
        def btn03():
            entry_usr_pwd.insert(tk.END, '3')
        def btn04():
            entry_usr_pwd.insert(tk.END, '4')
        def btn05():
            entry_usr_pwd.insert(tk.END, '5')
        def btn06():
            entry_usr_pwd.insert(tk.END, '6')
        def btn07():
            entry_usr_pwd.insert(tk.END, '7')
        def btn08():
            entry_usr_pwd.insert(tk.END, '8')
        def btn09():
            entry_usr_pwd.insert(tk.END, '9')
        def btn00():
            entry_usr_pwd.insert(tk.END, '0')
            
        btn_login = tk.Button(self.win_pw, text='#',font= ('Noto Sans Mono CJK TC Regular',20),command=lambda:self.face_ID())
        btn_login.place(x=340, y=130,width=40,height=40)
        btn_login = tk.Button(self.win_pw, text='0',font= ('Noto Sans Mono CJK TC Regular',20), command=btn00)
        btn_login.place(x=380, y=130,width=40,height=40)
        btn_login = tk.Button(self.win_pw, text='1',font= ('Noto Sans Mono CJK TC Regular',20), command=btn01)
        btn_login.place(x=340, y=90,width=40,height=40)
        btn_login = tk.Button(self.win_pw, text='2',font= ('Noto Sans Mono CJK TC Regular',20), command=btn02)
        btn_login.place(x=380, y=90,width=40,height=40)
        btn_login = tk.Button(self.win_pw, text='3',font= ('Noto Sans Mono CJK TC Regular',20), command=btn03)
        btn_login.place(x=420, y=90,width=40,height=40)
        btn_login = tk.Button(self.win_pw, text='4',font= ('Noto Sans Mono CJK TC Regular',20), command=btn04)
        btn_login.place(x=340, y=50,width=40,height=40)
        btn_login = tk.Button(self.win_pw, text='5',font= ('Noto Sans Mono CJK TC Regular',20), command=btn05)
        btn_login.place(x=380, y=50,width=40,height=40)
        btn_login = tk.Button(self.win_pw, text='6',font= ('Noto Sans Mono CJK TC Regular',20), command=btn06)
        btn_login.place(x=420, y=50,width=40,height=40)
        btn_login = tk.Button(self.win_pw, text='7',font= ('Noto Sans Mono CJK TC Regular',20), command=btn07)
        btn_login.place(x=340, y=10,width=40,height=40)
        btn_login = tk.Button(self.win_pw, text='8',font= ('Noto Sans Mono CJK TC Regular',20), command=btn08)
        btn_login.place(x=380, y=10,width=40,height=40)
        btn_login = tk.Button(self.win_pw, text='9',font= ('Noto Sans Mono CJK TC Regular',20), command=btn09)
        btn_login.place(x=420, y=10,width=40,height=40)

    #----------------------------------------------------------------------
    def hide(self):
        """"""
        self.win.withdraw()
    
    def closeWindow(self,myclosewindow):
        self.onCloseOtherFrame(myclosewindow)
        
    def close使用說明(self,win):
        win.destroy()
        self.openFrame()
        
    def spaekHowToUse(self,tit):
        a="{:}_使用說明書.txt".format(tit)
        with open (a,"r",encoding="UTF-8") as fd:
            data=fd.read()
            BotSpeak.speak(data)
    #----------------------------------------------------------------------
    def openFrame01(self):

        """"""
        self.hide()
        self.win_HOW01 = tk.Toplevel()
        #使用者關閉視窗觸發的事件（第一個刪除視窗，第二個為函式名，即過程）
        self.win_HOW01.protocol('WM_DELETE_WINDOW',lambda:self.close使用說明(self.win_HOW01))
        #self.win_HOW01.attributes("-fullscreen", True)
        left=(self.win_HOW01.winfo_screenwidth()-600)//2
        top=(self.win_HOW01.winfo_screenheight()-700)//2
        self.win_HOW01.geometry("{:}x{:}+{:}+{:}".format(600,700,left,top))
        self.win_HOW01.title("備忘錄")
        self.win_HOW01.photo_background=tk.PhotoImage(file=r"./image/memo使用說明.png")
        canvas_width = 600
        canvas_height =700
        canvas = tk.Canvas(self.win_HOW01, 
        width=canvas_width, 
        height=canvas_height)
        canvas.pack()
        #背景
        canvas.create_image(300,350, image=self.win_HOW01.photo_background)
        
        btn= tk.Button(self.win_HOW01,image=self.photo_喇叭,command=lambda:self.spaekHowToUse("備忘錄"))
        btn.place(x=505,y=630)
     #----------------------------------------------------------------------
    def openFrame02(self):

        """"""
        self.hide()
        self.win_HOW02 = tk.Toplevel()
        #使用者關閉視窗觸發的事件（第一個刪除視窗，第二個為函式名，即過程）
        self.win_HOW02.protocol('WM_DELETE_WINDOW',lambda:self.close使用說明(self.win_HOW02))
        #self.win_HOW02.attributes("-fullscreen", True)
        left=(self.win_HOW02.winfo_screenwidth()-600)//2
        top=(self.win_HOW02.winfo_screenheight()-700)//2
        self.win_HOW02.geometry("{:}x{:}+{:}+{:}".format(600,700,left,top))
        self.win_HOW02.title("生活小助手")
        self.win_HOW02.photo_background=tk.PhotoImage(file=r"./image/生活小助手使用說明.png")
        canvas_width = 600
        canvas_height =700
        canvas = tk.Canvas(self.win_HOW02, 
        width=canvas_width, 
        height=canvas_height)
        canvas.pack()
        #背景
        canvas.create_image(300,350, image=self.win_HOW02.photo_background)
        btn= tk.Button(self.win_HOW02,image=self.photo_喇叭,command=lambda:self.spaekHowToUse("生活小幫手"))
        btn.place(x=505,y=630)
     #----------------------------------------------------------------------
    def openFrame03(self):

        """"""
        self.hide()
        self.win_HOW03 = tk.Toplevel()
        #使用者關閉視窗觸發的事件（第一個刪除視窗，第二個為函式名，即過程）
        self.win_HOW03.protocol('WM_DELETE_WINDOW',lambda:self.close使用說明(self.win_HOW03))
        #self.win_HOW03.attributes("-fullscreen", True)
        left=(self.win_HOW03.winfo_screenwidth()-600)//2
        top=(self.win_HOW03.winfo_screenheight()-700)//2
        self.win_HOW03.geometry("{:}x{:}+{:}+{:}".format(600,700,left,top))
        self.win_HOW03.title("使用說明")
        self.win_HOW03.photo_background=tk.PhotoImage(file=r"./image/行事曆使用說明.png")
        canvas_width = 600
        canvas_height =700
        canvas = tk.Canvas(self.win_HOW03, 
        width=canvas_width, 
        height=canvas_height)
        canvas.pack()
        #背景
        canvas.create_image(300,350, image=self.win_HOW03.photo_background)
        
        btn= tk.Button(self.win_HOW03,image=self.photo_喇叭,command=lambda:self.spaekHowToUse("行事曆"))
        btn.place(x=505,y=630)    
    #----------------------------------------------------------------------
    def openFrame(self):

        """"""
        self.hide()
        self.win_HOW = tk.Toplevel()
        #使用者關閉視窗觸發的事件（第一個刪除視窗，第二個為函式名，即過程）
        self.win_HOW.protocol('WM_DELETE_WINDOW',lambda:self.closeWindow(self.win_HOW))
        #win_HOW.attributes("-fullscreen", True)
        left=(self.win_HOW.winfo_screenwidth()-600)//2
        top=(self.win_HOW.winfo_screenheight()-700)//2
        self.win_HOW.geometry("{:}x{:}+{:}+{:}".format(600,700,left,top))
        self.win_HOW.title("行事曆")
        self.win_HOW.photo_background=tk.PhotoImage(file=r"./image/背景.png")
        canvas_width = 600
        canvas_height =700
        canvas = tk.Canvas(self.win_HOW, 
        width=canvas_width, 
        height=canvas_height)
        canvas.pack()
        #背景
        canvas.create_image(300,350, image=self.win_HOW.photo_background)
        
        def 備忘錄():
            self.win_HOW.destroy()
            self.openFrame01()
        def 生活小助手():
            self.win_HOW.destroy()
            self.openFrame02()
        def 記事本():
            self.win_HOW.destroy()
            self.openFrame03()
        
        btn01= tk.Button(self.win_HOW, text="備忘錄",font= ('Noto Sans Mono CJK TC Regular',30),fg='white',bg='Maroon',command=備忘錄)
        btn01.place(x=220,y=100)
        btn02= tk.Button(self.win_HOW, text="生活小助手",font= ('Noto Sans Mono CJK TC Regular',30),fg='white',bg='#0000FF',command=生活小助手)
        btn02.place(x=180,y=250)
        btn03= tk.Button(self.win_HOW, text="行事曆",font= ('Noto Sans Mono CJK TC Regular',30),fg='white',bg='#FF44AA',command=記事本)
        btn03.place(x=220,y=400)
        
#        handler = lambda: self.onCloseOtherFrame(self.win_HOW)
#        btn = tk.Button(self.win_HOW, text="continue",command=handler,font= ('Noto Sans Mono CJK TC Regular',20),fg='white',bg='Maroon',width=8)
#        btn.place(x=330,y=380)
  
    #----------------------------------------------------------------------
    def openFrame3(self):
        """"""
        #生活小助手      
        self.hide()
        self.win_main3 = tk.Toplevel()
        left=(self.win_main3.winfo_screenwidth()-600)//2
        top=(self.win_main3.winfo_screenheight()-700)//2
        self.win_main3.geometry("{:}x{:}+{:}+{:}".format(600,700,left,top))
        a="{:}生活小助手"
        a=a.format(self.Account)
        self.win_main3.title(a)
        
        #使用者關閉視窗觸發的事件（第一個刪除視窗，第二個為函式名，即過程）
        self.win_main3.protocol('WM_DELETE_WINDOW',lambda:self.CloseWin(self.win_main3))
        
        canvas_width = 1000
        canvas_height =1000
        canvas = tk.Canvas(self.win_main3, 
        width=canvas_width, 
        height=canvas_height)
        canvas.pack()
        #背景
        canvas.create_image(300,350, image=self.photo_生活小助手)
        def weather():
            BotSpeak.speak("現在進入的是天氣預報介面") 
            Myweather()
        def invoice():
            BotSpeak.speak("現在進入的是兌獎查詢介面") 
            invoiceMyApp()
        def Foreign():
            BotSpeak.speak("現在進入的是匯率轉換介面")
            MyForeignExchange()
        def requests():
            BotSpeak.speak("現在進入的是星座運勢介面")
            Myrequests()
        but_weather=tk.Button(self.win_main3,image=self.photo_weather,command=weather)
        but_weather.place(x=44,y=5)
        but_tick=tk.Button(self.win_main3,image=self.photo_tick,command=invoice)
        but_tick.place(x=310,y=295)
        but_money=tk.Button(self.win_main3,image=self.photo_money,command=Foreign)
        but_money.place(x=44,y=295)
        but_start=tk.Button(self.win_main3,image=self.photo_start,command=requests)
        but_start.place(x=310,y=2)
        BotSpeak.speak("現在進入的是生活小助手介面 請點選個別按鈕進入相對應的介面")     
    #----------------------------------------------------------------------
    def onCloseOtherFrame(self, otherFrame):
        """"""
        self.a=0
        otherFrame.destroy()
        self.show()
    #----------------------------------------------------------------------
    def CloseWin(self, otherFrame):
        """"""
        otherFrame.destroy()
        self.chooseclear()    
    #----------------------------------------------------------------------
    def show(self):
        """"""
        self.win.update()
        self.win.deiconify()
#----------------------------------------------------------------------
if __name__ == "__main__":
    app = MyApp() 