# 引入日歷模組
import calendar
import tkinter as tk
from  tkinter import ttk
from tkinter.font import nametofont
datetime = calendar.datetime.datetime
timedelta = calendar.datetime.timedelta
class yearmonth:
    def __init__(self):
        
        日歷=''
        self.week1=[]#第一週
        self.week2=[]#第二週
        self.week3=[]#第三週
        self.week4=[]#第四週
        self.week5=[]#第五週
        self.title=''#年+月
#        self.yy =eval(input("請輸入年份："))
#        self.mm=eval(input("請輸入月份："))
        self.yy = datetime.now().year
        self.mm = datetime.now().month
        print(calendar.month(self.yy,self.mm))
        日歷=(calendar.month(self.yy,self.mm))
        
        Jan=日歷.split("\n")
        self.title=Jan[0]
        print(self.title)
        week=Jan[2]
        week=week.split(' ')
        c=len(week)
        for i in range(c):
            if week[i] != '':
                self.week1.append(week[i])
        week=Jan[3]
        week=week.split(' ')
        c=len(week)
        for i in range(c):
            if week[i] != '':
                self.week2.append(week[i])
        week=Jan[4]
        week=week.split(' ')
        c=len(week)
        for i in range(c):
            if week[i] != '':
                self.week3.append(week[i])
        week=Jan[5]
        week=week.split(' ')
        c=len(week)
        for i in range(c):
            if week[i] != '':
                self.week4.append(week[i])
        week=Jan[6]
        week=week.split(' ')
        c=len(week)
        for i in range(c):
            if week[i] != '':
                self.week5.append(week[i])
                
        for k in range(7-len(self.week1)):
            self.week1.insert( 0," ")    
        print("week1",self.week1)
        print("week2",self.week2)
        print("week3",self.week3)
        print("week4",self.week4)
        print("week5",self.week5)
        self.mainwin()
        # 顯示日歷
    def mainwin(self):
        self.win=tk.Toplevel()
#        nametofont("TkHeadingFont").configure(size=100)
        style = ttk.Style()
        style.configure("Treeview.Heading", font=(None, 30))
        style.configure("Treeview", font=(None, 30), rowheight=60)
        
        tree=ttk.Treeview(self.win,height=5, show="headings", columns=("Sun","Mon","Tue","Wed","Thu","Fri","Sat"))#表格
        tree.column("Sun",width=150, anchor='center')   #表示列,不顯示
        tree.column("Mon",width=150, anchor='center')
        tree.column("Tue",width=150, anchor='center')
        tree.column("Wed",width=150, anchor='center')
        tree.column("Thu",width=150, anchor='center')
        tree.column("Fri",width=150, anchor='center')
        tree.column("Sat",width=150, anchor='center')
        
        tree.heading("Sun",text="Sun")  #顯示表頭
        tree.heading("Mon",text="Mon")
        tree.heading("Tue",text="Tue")
        tree.heading("Wed",text="Wed")
        tree.heading("Thu",text="Thu")
        tree.heading("Fri",text="Fri")
        tree.heading("Sat",text="Sat")
         
        tree.insert("",0,text="week1" ,values=(self.week1)) #插入數據，
        tree.insert("",1,text="week2" ,values=(self.week2))
        tree.insert("",2,text="week3" ,values=(self.week3))
        tree.insert("",3,text="week4" ,values=(self.week4))
        tree.insert("",4,text="week5" ,values=(self.week5))
        tree.pack()
        self.win.mainloop()
if __name__=='__main__':
    yearmonth()
    