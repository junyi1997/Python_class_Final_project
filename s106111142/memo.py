# -*- coding: utf-8 -*-

#pip install PyMySQL
#from tkinter import *

from tkinter import messagebox,END,ttk  #呼叫套件
import tkinter.scrolledtext as ScrolledText  #呼叫滾動元件ScrolledText
from datetime import date #引入日期
import pymysql
import tkinter as TK  #呼叫模組別名是TK

class Login(): #登入畫面
     def __init__(self):
         
         self.Login = TK.Tk()
         self.Login.title('my memo')
         self.Login.geometry('300x200+0+0') #視窗大小
         self.userLabel = ttk.Label(self.Login, text='使用者:', font=('Arial', 15),  width=15) #使用者標籤
         self.Loginname = ttk.Entry(self.Login, width=20)  #使用者文字方塊

         #元件擺放位置
         self.userLabel.place(x=0, y=50, anchor='nw')
         self.Loginname.place(x=90, y=50, anchor='nw')
                  
         self.loadbtn = ttk.Button(self.Login, text='登入', width=15, command=lambda: self.login(self.Loginname.get()))#登入按鈕
         self.loadbtn.place(x=50, y=100, anchor='nw')

     def login(self,name):
         if (name ==""):#沒輸入姓名
             messagebox.showinfo("提示訊息", "請輸入姓名")
         else: #有輸入姓名，呼叫該使用者memo內容視窗
             Main(name)
        
         self.Login.mainloop()


class Main(): #memo內容
    def __init__(self,username): #初始化
        self.user = username
     
        window = TK.Tk()
        window.title('my memo')
        window.geometry('600x450+500+50') #視窗大小
        #window.iconbitmap("memoicon.ico")
        window.resizable(False, False) #鎖住視窗寬高
        db = pymysql.connect("localhost","root","root","programs" ) #資料庫

        tableexist = "SHOW TABLES LIKE '"+self.user+"'"; #判斷使用者table是否存在，如果不存在，新增資料表
        
        cursor = db.cursor()
        cursor.execute(tableexist)
        result = cursor.fetchone() #查詢有無資料表
        
        if result == None: #沒有資料表，新增資料表
            sql = "CREATE TABLE `"+self.user+"` ( `ID` INT NOT NULL AUTO_INCREMENT , `Subject` VARCHAR(20) NOT NULL , `text` TEXT NOT NULL , PRIMARY KEY (`ID`))"
            cursor.execute(sql)

        self.itemvalue=[]  #裝下拉式標題的list
        
        #查詢使用者memo資料id+標題加到標題list
        sql = "SELECT * FROM `"+self.user+"`"
        print(sql)
        try:
           cursor.execute(sql)
           results = cursor.fetchall()
           for row in results:
              self.itemvalue.append(str(row[0])+":"+str(row[1]))
              
        except: 
           print ("Error: unable to fetch data")
           
        if (len(self.itemvalue)) ==0: #沒有memo項目
            self.itemvalue=["無項目"] #丟無項目的值
            
            self.loadbtn = ttk.Button(
            window, text='載入', width=15, command=lambda: self.Load())
            self.loadbtn["state"] = "disabled"
        else: #有項目
            self.loadbtn = ttk.Button(
            window, text='載入', width=15, command=lambda: self.Load())
        
        db.close() #關閉連線
        self.timeLabel = ttk.Label(window, text='標題:', font=('Arial', 15),  width=15)
        self.savelabel = ttk.Label(window, text='已儲存memo:', font=('Arial', 15),  width=15)

        today = date.today() #現在時間
        self.time = ttk.Entry(window, width=40) #時間文字方塊
        self.time.insert(0, today) #加在time文字方塊內

        self.sText = ScrolledText.ScrolledText(window, width=60) #內容文字方塊
        self.comboExample = ttk.Combobox( window,  values=self.itemvalue)
        self.comboExample.current(0) #選第0個項目

       
        self.savebtn = ttk.Button(
            window, text='儲存', width=15, command=lambda: self.Save())
        self.delbtn = ttk.Button(
            window, text='刪除', width=15,command=lambda: self.Delete())
        self.newbtn = ttk.Button(
            window, text='新增', width=15, command=lambda: self.New())
        self.delbtn["state"] = "disabled"
        self.savebtn["state"] = "disabled"
        
        #元件座標定位
        self.timeLabel.place(x=0, y=10, anchor='nw')
        self.time.place(x=70, y=10, anchor='nw')
        self.comboExample.place(x=130, y=50, anchor='nw')

        self.savelabel.place(x=0, y=50, anchor='nw')
        self.loadbtn.place(x=300, y=50, anchor='nw')
        self.savebtn.place(x=450, y=10, anchor='nw')
        self.delbtn.place(x=450, y=50, anchor='nw')
        self.newbtn.place(x=450, y=90, anchor='nw')

        self.sText.place(x=0, y=90, anchor='nw')
        
        
        window.mainloop()


    def Load(self):  #載入
        self.savebtn['state'] = 'normal' #儲存刪除按鈕可以點
        self.delbtn['state'] = 'normal'

        id = self.comboExample.get().split(":")[0] #抓ID
        db = pymysql.connect("localhost","root","root","programs") #連線資料庫
        cursor = db.cursor()

        self.itemvalue=[] #裝下拉式標題的list

        #把內容清除
        self.time.delete(0, 'end')
        self.sText.delete('1.0', END)
        
        #抓使用者選擇的memo id的內容
        sql = "SELECT * FROM `"+self.user+"` where id ="+id
        print(sql)
        try:
           cursor.execute(sql)
           results = cursor.fetchall()
           for row in results:
                self.time.insert(0, row[1]) #設定標題文字方塊
                self.sText.insert(1.0, row[2]) #設定內容文字方塊
                #print(str(row[1])+":"+str(row[2]))
        except:
           print ("Error: unable to fetch data")
           
         
        db.close() #關閉連線
        
        messagebox.showinfo("提示訊息", "載入完畢")
        #print(self.sText.get(1.0, END))
        
   
    def Save(self):  #儲存檔案
        id = self.comboExample.get().split(":")[0] #抓ID
        db = pymysql.connect("localhost","root","root","programs")
        cursor = db.cursor()
        sql = "update `"+self.user+"` set Subject = '"+self.time.get()+"', text = '"+self.sText.get(1.0, END)+"' where id = "+id
        print(sql)
        try:
           cursor.execute(sql)
           db.commit()
        except:
           db.rollback()
        db.close()
        self.time.delete(0, 'end')
        self.sText.delete('1.0', END)
        messagebox.showinfo("提示訊息", "儲存完畢")
        db = pymysql.connect("localhost","root","root","programs")
        self.itemvalue=[] #重新取得標題
        
        cursor = db.cursor()
        sql = "SELECT * FROM `"+self.user+"`"
        try:
            cursor.execute(sql)
            results = cursor.fetchall()
            for row in results:
                self.itemvalue.append(str(row[0])+":"+str(row[1]))
        except :
            print ("Error: unable to fetch data")
            
        if (len(self.itemvalue)) ==0:
            self.itemvalue=["無項目"]
        self.comboExample['values'] = self.itemvalue #更新後的標題丟到下拉式選單
        
        #self.comboExample.current(0) #預設選的項目
        
    def Delete(self):  #刪除檔案
        MsgBox = messagebox.askyesno("提示訊息","您確定要刪除嗎?") #刪除確認方塊
        if (MsgBox == True):
            id = self.comboExample.get().split(":")[0] #抓ID
            db = pymysql.connect("localhost","root","root","programs")
            cursor = db.cursor()
            sql = "delete from `"+self.user+"` where id = "+id
            #print(sql)
            try:
                cursor.execute(sql)
                db.commit()
                db.rollback()
                db.close()
                self.time.delete(0, 'end')
                self.sText.delete('1.0', END)
                messagebox.showinfo("提示訊息", "刪除完畢")
            except:
                print("error")

            db = pymysql.connect("localhost","root","root","programs")
            self.itemvalue=[] #重新取得標題
            cursor = db.cursor()
            sql = "SELECT * FROM `"+self.user+"`"

            try:
                cursor.execute(sql)
                results = cursor.fetchall()
                for row in results:
                    self.itemvalue.append(str(row[0])+":"+str(row[1]))
            except:
                print ("Error: unable to fetch data") #無memo按載入顯示找無資料
                
            if (len(self.itemvalue)) ==0:
                self.itemvalue=["無項目"]
                self.loadbtn['state'] ="disabled"
            self.savebtn['state'] ="disabled"
            self.delbtn['state'] ="disabled"

            self.comboExample['values'] = self.itemvalue
            self.comboExample.current(0) #選第0個項目
            
        else:
            pass
        
    def New(self): #取得標題、文字的值新增到資料庫
        
        if (self.time.get()==""): #標題要打東西
             messagebox.showinfo("提示訊息", "標題不能為空")
             return
        #print(self.time.get())
        self.loadbtn['state'] = 'normal' #讓使用者可以按載入按鈕
        #print(self.sText.get(1.0, END))
        
        db = pymysql.connect("localhost","root","root","programs")
        cursor = db.cursor()
        sql = "INSERT INTO `"+self.user+"` VALUES (null, '"+self.time.get()+"','"+self.sText.get(1.0, END)+"')"
        #print(sql)
        try:
           cursor.execute(sql)
           db.commit()
        except:
           db.rollback()
        db.close()
        
        messagebox.showinfo("提示訊息", "新增完畢")
        
        self.time.delete(0, 'end') #新增後把標題文字方塊內容清除
        self.sText.delete('1.0', END) #新增後把內容文字方塊內容清除
        

        db = pymysql.connect("localhost","root","root","programs")
        self.itemvalue=[] #重新取得標題
        cursor = db.cursor()
        sql = "SELECT * FROM `"+self.user+"`"
        print(sql)
        try:
            cursor.execute(sql)
            results = cursor.fetchall()
            for row in results:
                self.itemvalue.append(str(row[0])+":"+str(row[1]))
        except:
            print ("Error: unable to fetch data") #無memo按載入顯示找無資料


        self.comboExample['values'] = self.itemvalue
        self.comboExample.current(0) #選第0個項目
        
     
if __name__ == "__main__":
    Login()
