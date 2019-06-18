import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry
import time as times
import pymysql
#引入函式庫

root = tk.Tk()
root.geometry("400x500")
root.title("Date")
# change ttk theme to 'clam' to fix issue with downarrow button
style = ttk.Style(root)
style.theme_use('clam')
db = pymysql.connect(host="localhost",
    user="root", passwd="",
    db="test0530", charset="utf8")
cursor = db.cursor()
def Getall():
    global user
    user=userWindow.get()
    global time
    time=timeWindow.get()
    global event
    event=eventWindow.get(1.0,tk.END)
def IDget():
    global ID
    ID=IDWindow.get()
def Userget():
    global user
    user=userWindow.get()
def Timeget():
    global time
    time=timeWindow.get()
def Eventget():
    global event
    event=eventWindow.get(1.0,tk.END)
def Insert():
        global userWindow
        global eventWindow
        global timeWindow
        Window=tk.Tk()
        Window.geometry("400x400")
        Lab1=tk.Label(Window,text="用戶名")
        Lab1.pack()
        Lab1.place(x=40,y=10)
        Lab2=tk.Label(Window,text="時間")
        Lab2.pack()
        Lab2.place(x=45,y=47)
        Lab3=tk.Label(Window,text="事件")
        Lab3.pack()
        Lab3.place(x=45,y=87)
        userWindow=tk.Entry(Window,width=25)
        userWindow.pack(pady=10)
        userWindow.insert(10,"你的名字")
        timeWindow=tk.Entry(Window,width=25)
        timeWindow.pack(pady=10)
        timeWindow.insert(10,"(yyyy-mm-dd \n00:00:00)")
        eventWindow=tk.Text(Window,width=35,height=15)
        eventWindow.pack(pady=10)
        eventWindow.place(x=90,y=95)
        eventWindow.insert(tk.END,"提醒事項")
        CreateBotton = tk.Button(Window,
                               text="確認",
                               command = Getall,
                               width=10, height=2)
        CreateBotton.pack(side="bottom",pady=10)
        Window.mainloop()
        # 插入資料
        cursor.execute('INSERT INTO member (user,time,event) '
        'VALUES ("{:}","{:}","{:}");'.format(user,time,event))
        db.commit()
        #關閉連線
        db.close()
        
"""
def Update():
    #修改--把名稱是name 的改成c
    cursor.execute('UPDATE member SET "{:}" = "{:}" WHERE "{:}" = "{:}";')
    db.commit()
    
    db.close()
"""
def Delete():
    global IDWindow
    Window=tk.Tk()
    Window.geometry("200x100")
    IDWindow=tk.Entry(Window,width=20)
    IDWindow.pack()
    IDWindow.place(x=45,y=20)
    lab4=tk.Label(Window,text="ID")
    lab4.pack()
    lab4.place(x=10,y=17)
    CreateBotton = tk.Button(Window,
                           text="確認",
                           command = IDget,
                           width=10, height=2)
    CreateBotton.pack(side="bottom",pady=5)    
    IDWindow.mainloop()
    #刪除資料欄位  把名稱是B的刪除
    cursor.execute('DELETE FROM member WHERE ID = "{:}";'.format(ID))
    #cursor.execute('DELETE FROM member WHERE ID = "1";')
    db.commit()   
    db.close()
def Search():
    
    # 執行 MySQL 查詢指令
    cursor.execute("SELECT * FROM member")
    #cursor.execute('SELECT * FROM member WHERE time = "{:}";'.format(de.get()))
    # 取回所有查詢結果
    results = cursor.fetchall()
    # 輸出結果
    #print(de.get())
    for record in results:
        
     col1 = record[0]
     col2 = record[1]
     col3 = record[2]
     col4 = record[3]     
     w.insert (tk.END,"%s, %s, %s, %s,%s" % (col1, col2, col3, col4,"\n"))
     #t=(str(col1),str(col2),str(col3),str(col4))
     #print(t)
     #allt=t+"\n"+t
     #print(allt)
     #w.config(text="{:}".format(allt))
    # 關閉連線
    db.close()
class MyDateEntry(DateEntry):
    def __init__(self, master=None, **kw):
                DateEntry.__init__(self, master=None, **kw)
                
                today='{:}-{:}-{:}'.format(times.strftime('%Y'), times.strftime('%m'),times.strftime('%d'))
                self._top_cal.configure(bg='black', bd=2)
                #在日曆添加黑色外邊框
                tk.Label(self._top_cal, bg='gray90', anchor='w',
                #
                         text='今天日期為:{:}'.format(today)).pack(fill='x')
                #在日曆添加今天日期
    
    def CreateBotton():
        CreateBotton = tk.Button(root,
                           text="新增",
                           command = Insert,
                           width=10, height=2)
        CreateBotton.pack(side="right")
        CreateBotton.place(x=70, y=400)
    def DeleteBotton():
        DeleteBotton = tk.Button(root,
                           text="刪除",
                           command=Delete,
                           width=10, height=2)
        DeleteBotton.pack(side='left')
        DeleteBotton.place(x=250, y=400)       

    def SearchBotton():
        SearchBotton = tk.Button(root,
                           text="查詢",
                           command=Search,
                           width=10, height=2)
        SearchBotton.pack(side="right")
        SearchBotton.place(x=160, y=330)
"""
    def InsertBotton():
        InsertBotton = tk.Button(root,
                           text="修改",
                           command=Update,
                           width=10, height=2)
        InsertBotton.pack(side='left')
        InsertBotton.place(x=250, y=400)
""" 
        

# create the entry and configure the calendar colors
de = MyDateEntry(root, year=2019, month=5, day=30,
                 selectbackground='gray80',
                 selectforeground='black',
                 normalbackground='white',
                 normalforeground='black',
                 background='gray90',
                 foreground='black',
                 bordercolor='gray90',
                 othermonthforeground='gray50',
                 othermonthbackground='white',
                 othermonthweforeground='gray50',
                 othermonthwebackground='white',
                 weekendbackground='white',
                 weekendforeground='black',
                 headersbackground='white',
                 headersforeground='gray70')

de.pack(pady=30)
MyDateEntry.CreateBotton()
MyDateEntry.DeleteBotton()
#MyDateEntry.InsertBotton()
MyDateEntry.SearchBotton()
w = tk.Text(root,bg="white",width=52, height=16)
w.pack()
w.place(x=20,y=60)
root.mainloop()