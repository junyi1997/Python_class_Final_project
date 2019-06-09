# -*- coding: utf-8 -*- 
import calendar
import tkinter as tk
import tkinter.font as tkFont
from tkinter import ttk
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

datetime = calendar.datetime.datetime
timedelta = calendar.datetime.timedelta
saveK1=[]
saveK2=[]
saveK3={}
save4=[]
sumi_1=0
class Calendar:

    def __init__(self, point = None, position = None):
# point 提供一個基點，來確定窗口位置
# position 窗口在點的位置 'ur'-右上, 'ul'-左上, 'll'-左下, 'lr'-右下
#s.master = tk.Tk()
        s=self
        s.master = tk.Toplevel()
        s.master.withdraw()
        fwday = calendar.SUNDAY

        year = datetime.now().year
        month = datetime.now().month
        locale = None
        sel_bg = '#ecffc4'
        sel_fg = '#05640e'

        s._date = datetime(year, month, 1)
        s._selection = None # 設置為未選中日期

        s.G_Frame = ttk.Frame(s.master)

        s._cal = s.__get_calendar(locale, fwday)

        s.__setup_styles()       # 創建自定義樣式
        s.__place_widgets() # pack/grid 小部件
        s.__config_calendar() # 調整日曆列和安裝標記
        # 配置畫布和正確的綁定，以選擇日期。
        s.__setup_selection(sel_bg, sel_fg)
        # 存儲項ID，用於稍後插入。
        s._items = [s._calendar.insert('', 'end', values='') for _ in range(6)]

        # 在當前空日曆中插入日期
        s._update()

        s.G_Frame.pack(expand = 1, fill = 'both')
        s.master.overrideredirect(1)
        s.master.update_idletasks()
        width, height = s.master.winfo_reqwidth(), s.master.winfo_reqheight()
        if point and position:
            if   position == 'ur': x, y = point[0], point[1] - height
            elif position == 'lr': x, y = point[0], point[1]
            elif position == 'ul': x, y = point[0] - width, point[1] - height
            elif position == 'll': x, y = point[0] - width, point[1]
        else: x, y = (s.master.winfo_screenwidth() - width)/2, (s.master.winfo_screenheight() - height)/2
        s.master.geometry('%dx%d+%d+%d' % (width, height, x, y)) #窗口位置居中
        s.master.after(300, s._main_judge)
        s.master.deiconify()
        s.master.focus_set()
        s.master.wait_window()#這裡應該使用wait_window掛起窗口，如果使用mainloop,可能會導致主程序很多錯誤

    def __get_calendar(self, locale, fwday):
        s=self
        # 實例化適當的日曆類
        if locale is None:
            return calendar.TextCalendar(fwday)
        else:
            return calendar.LocaleTextCalendar(fwday, locale)

    def __setitem__(self, item, value):
        s=self
        if item in ('year', 'month'):
            raise AttributeError("attribute '%s' is not writeable" % item)
        elif item == 'selectbackground':
            s._canvas['background'] = value
        elif item == 'selectforeground':
            s._canvas.itemconfigure(s._canvas.text, item=value)
        else:
            s.G_Frame.__setitem__(s, item, value)

    def __getitem__(self, item):
        s=self
        if item in ('year', 'month'):
            return getattr(s._date, item)
        elif item == 'selectbackground':
            return s._canvas['background']
        elif item == 'selectforeground':
            return s._canvas.itemcget(s._canvas.text, 'fill')
        else:
            r = ttk.tclobjs_to_py({item: ttk.Frame.__getitem__(s, item)})
            return r[item]

    def __setup_styles(self):
        s=self
        # 自定義TTK風格
        style = ttk.Style(s.master)
        arrow_layout = lambda dir: (
            [('Button.focus', {'children': [('Button.%sarrow' % dir, None)]})]
        )
        style.layout('L.TButton', arrow_layout('left'))
        style.layout('R.TButton', arrow_layout('right'))

    def __place_widgets(self):
        s=self
        # 標頭框架及其小部件
        Input_judgment_num = s.master.register(s.Input_judgment) # 需要將函數包裝一下，必要的
        hframe = ttk.Frame(s.G_Frame)
        gframe = ttk.Frame(s.G_Frame)
        bframe = ttk.Frame(s.G_Frame)
        hframe.pack(in_=s.G_Frame, side='top', pady=5, anchor='center')
        gframe.pack(in_=s.G_Frame, fill=tk.X, pady=5)
        bframe.pack(in_=s.G_Frame, side='bottom', pady=5)

        lbtn = ttk.Button(hframe, style='L.TButton', command=s._prev_month)
        lbtn.grid(in_=hframe, column=0, row=0, padx=12)
        rbtn = ttk.Button(hframe, style='R.TButton', command=s._next_month)
        rbtn.grid(in_=hframe, column=5, row=0, padx=12)
        
        s.CB_year = ttk.Combobox(hframe, width = 5, values = [str(year) for year in range(datetime.now().year, datetime.now().year-11,-1)], validate = 'key', validatecommand = (Input_judgment_num, '%P'))
        s.CB_year.current(0)
        s.CB_year.grid(in_=hframe, column=1, row=0)
        s.CB_year.bind('<KeyPress>', lambda event:s._update(event, True))
        s.CB_year.bind("<<ComboboxSelected>>", s._update)
        tk.Label(hframe, text = '年', justify = 'left').grid(in_=hframe, column=2, row=0, padx=(0,5))

        s.CB_month = ttk.Combobox(hframe, width = 3, values = ['%02d' % month for month in range(1,13)], state = 'readonly')
        s.CB_month.current(datetime.now().month - 1)
        s.CB_month.grid(in_=hframe, column=3, row=0)
        s.CB_month.bind("<<ComboboxSelected>>", s._update)
        tk.Label(hframe, text = '月', justify = 'left').grid(in_=hframe, column=4, row=0)

        # 日历部件
        s._calendar = ttk.Treeview(gframe, show='', selectmode='none', height=7)
        s._calendar.pack(expand=1, fill='both', side='bottom', padx=5)

        ttk.Button(bframe, text = "確 定", width = 6, command = lambda: s._exit(True)).grid(row = 0, column = 0, sticky = 'ns', padx = 20)
        ttk.Button(bframe, text = "取 消", width = 6, command = s._exit).grid(row = 0, column = 1, sticky = 'ne', padx = 20)
        
        
        tk.Frame(s.G_Frame, bg = '#565656').place(x = 0, y = 0, relx = 0, rely = 0, relwidth = 1, relheigh = 2/200)
        tk.Frame(s.G_Frame, bg = '#565656').place(x = 0, y = 0, relx = 0, rely = 198/200, relwidth = 1, relheigh = 2/200)
        tk.Frame(s.G_Frame, bg = '#565656').place(x = 0, y = 0, relx = 0, rely = 0, relwidth = 2/200, relheigh = 1)
        tk.Frame(s.G_Frame, bg = '#565656').place(x = 0, y = 0, relx = 198/200, rely = 0, relwidth = 2/200, relheigh = 1)

    def __config_calendar(self):
        s=self
        # cols = s._cal.formatweekheader(3).split()
        cols = ['日','一','二','三','四','五','六']
        s._calendar['columns'] = cols
        s._calendar.tag_configure('header', background='grey90')
        s._calendar.insert('', 'end', values=cols, tag='header')
        # 調整其列寬
        font = tkFont.Font()
        maxwidth = max(font.measure(col) for col in cols)
        for col in cols:
            s._calendar.column(col, width=maxwidth, minwidth=maxwidth,
                anchor='center')

    def __setup_selection(self, sel_bg, sel_fg):
        s=self
        def __canvas_forget(evt):
            canvas.place_forget()
            s._selection = None

        s._font = tkFont.Font()
        s._canvas = canvas = tk.Canvas(s._calendar, background=sel_bg, borderwidth=0, highlightthickness=0)
        canvas.text = canvas.create_text(0, 0, fill=sel_fg, anchor='w')

        canvas.bind('<Button-1>', __canvas_forget)
        s._calendar.bind('<Configure>', __canvas_forget)
        s._calendar.bind('<Button-1>', s._pressed)

    def _build_calendar(self):
        s=self
        year, month = s._date.year, s._date.month

        # update header text (Month, YEAR)
        header = s._cal.formatmonthname(year, month, 0)

        # 更新日曆顯示的日期
        cal = s._cal.monthdayscalendar(year, month)
        for indx, item in enumerate(s._items):
            week = cal[indx] if indx < len(cal) else []
            fmt_week = [('%02d' % day) if day else '' for day in week]
            s._calendar.item(item, values=fmt_week)

    def _show_select(self, text, bbox):
        s=self
        """为新的选择配置画布。"""
        x, y, width, height = bbox

        textw = s._font.measure(text)

        canvas = s._canvas
        canvas.configure(width = width, height = height)
        canvas.coords(canvas.text, (width - textw)/2, height / 2 - 1)
        canvas.itemconfigure(canvas.text, text=text)
        canvas.place(in_=s._calendar, x=x, y=y)

    def _pressed(self, evt = None, item = None, column = None, widget = None):
        s=self
        """在日历的某个地方点击。"""
        if not item:
            x, y, widget = evt.x, evt.y, evt.widget
            item = widget.identify_row(y)
            column = widget.identify_column(x)

        if not column or not item in s._items:
            # 在工作日行中單擊或僅在列外單擊。
            return

        item_values = widget.item(item)['values']
        if not len(item_values): # 這個月的行是空的。
            return

        text = item_values[int(column[1]) - 1]
        if not text: # 日期為空
            return

        bbox = widget.bbox(item, column)
        if not bbox: # 日曆尚不可見
            s.master.after(20, lambda : s._pressed(item = item, column = column, widget = widget))
            return

        # 更新，然後顯示選擇
        text = '%02d' % text
        s._selection = (text, item, column)
        s._show_select(text, bbox)

    def _prev_month(self):
        s=self
        """更新日曆以顯示前一個月。"""
        s._canvas.place_forget()
        s._selection = None

        s._date = s._date - timedelta(days=1)
        s._date = datetime(s._date.year, s._date.month, 1)
        s.CB_year.set(s._date.year)
        s.CB_month.set(s._date.month)
        s._update()

    def _next_month(self):
        s=self
        """更新日曆以顯示下一個月。"""
        s._canvas.place_forget()
        s._selection = None

        year, month = s._date.year, s._date.month
        s._date = s._date + timedelta(
            days=calendar.monthrange(year, month)[1] + 1)
        s._date = datetime(s._date.year, s._date.month, 1)
        s.CB_year.set(s._date.year)
        s.CB_month.set(s._date.month)
        s._update()

    def _update(self, event = None, key = None):
        s=self
        """刷新界面"""
        if key and event.keysym != 'Return': return
        year = int(s.CB_year.get())
        month = int(s.CB_month.get())
        if year == 0 or year > 9999: return
        s._canvas.place_forget()
        s._date = datetime(year, month, 1)
        s._build_calendar() # 重建日歷

        if year == datetime.now().year and month == datetime.now().month:
            day = datetime.now().day
            for _item, day_list in enumerate(s._cal.monthdayscalendar(year, month)):
                if day in day_list:
                    item = 'I00' + str(_item + 2)
                    column = '#' + str(day_list.index(day)+1)
                    s.master.after(100, lambda :s._pressed(item = item, column = column, widget = s._calendar))

    def _exit(self, confirm = False):
        s=self
        """退出窗口"""
        if not confirm: s._selection = None
        s.master.destroy()

    def _main_judge(self):
        s=self
        """判斷窗口是否在最頂層"""
        try:
            #s.master 為 TK 窗口
            #if not s.master.focus_displayof(): s._exit()
            #else: s.master.after(10, s._main_judge)

            #s.master 為 toplevel 窗口
            if s.master.focus_displayof() == None or 'toplevel' not in str(s.master.focus_displayof()): s._exit()
            else: s.master.after(10, s._main_judge)
        except:
            s.master.after(10, s._main_judge)
            #s.master.tk_focusFollowsMo​​use() # 焦點跟隨鼠標

    def selection(self):
        s=self
        """返回表示當前選定日期的日期時間。"""
        if not s._selection: return None

        year, month = s._date.year, s._date.month
        return str(datetime(year, month, int(s._selection[0])))[:10]

    def Input_judgment(self, content):
        s=self
        """輸入判斷"""
        # 如果不加上==""的話，就會發現刪不完。總會剩下一個數字
        if content.isdigit() or content == "":
            return True
        else:
            return False
def my_main():
    root = tk.Tk()
    root.geometry("600x700")
    width=600
    height=700
    #width, height = root.winfo_reqwidth() + 50, 50 #窗口大小
    x, y = (root.winfo_screenwidth()  - width )/2, (root.winfo_screenheight() - height)/2
    root.geometry('%dx%d+%d+%d' % (width, height, x, y )) #窗口位置居中

##########################################################################################
    
    
    date_str = tk.StringVar()                                                            #
    date = ttk.Entry(root, textvariable = date_str,font= ('Noto Sans Mono CJK TC Regular',20))                                      
    date.place(x = 150, y = 20,width=150,height=70)#, relx = 5/20, rely = 1/6, relwidth = 14/20, relheigh = 2/3)  
    year = datetime.now().year
    month = datetime.now().month
    day = datetime.now().day
    a=str(datetime(year, month, day))[:10]
    date_str.set(a)
##########################################################################################
    T = tk.Text(root, height=2, width=30)
    T.place(x = 50, y = 120, width=500,height=530)
    S = tk.Scrollbar(root)
    S.pack(side=tk.RIGHT, fill=tk.Y)
    S.config(command=T.yview)
    T.config(yscrollcommand=S.set)

    date_str_gain = lambda: [
        date_str.set(date)
        for date in [Calendar((100,300), 'ur').selection()]
        if date]
    tk.Button(root, text = '日期:', command = date_str_gain,font= ('Noto Sans Mono CJK TC Regular',20)).place(x = 50, y = 20)#, relx = 1/20, rely = 1/6, relwidth = 4/20, relheigh = 2/3)
    
    def date_input():
        global sumi_1 ,save4,saveK1
        save4.clear()
        saveK1.clear()
        sumi_1=0
        #Get Collection
        doc_ref = db.collection("行事曆")
        docs = doc_ref.get()
        #print("docs=",docs)
        for doc in docs:
            sumi_1+=1
            save4.append(doc.to_dict())
        #print("save4=",save4)   
        #print("sumi_1=",sumi_1)
        for i in range(0,sumi_1):
            saveK1.append(save4[i]['Date']) 
        #print("saveK1=",saveK1)    
        T1=T.get(0.0,tk.END)
        Time=date.get()
        doc = {
            'Date': Time,
            'content': T1
            }    
        # 建立文件 必須給定 集合名稱 文件id
        # 即使 集合一開始不存在 都可以直接使用

        # 語法
        # doc_ref = db.collection("集合名稱").document("文件id")
        if Time in saveK1:
            T.insert('end',"\n原來的資料\n")
            print("已經有該時間的資料了")
            T.insert('end',saveK3[Time])
        else: 
            A="第{:}筆".format(sumi_1+1)   
            doc_ref = db.collection("行事曆").document(A)
            doc_ref.set(doc)
            sumi_1=sumi_1+1
            T.delete(1.0,tk.END)    
    def Delete_input():
        global sumi_1
        cleardata = tk.messagebox.askyesno('Welcome','是否要清空資料庫？')
        if cleardata: 
            for i in range(sumi_1+1):
                A="第{:}筆".format(i)
                doc_ref = db.collection("行事曆").document(A)
                doc_ref.delete()
                print(A,"DONE")    
        T.delete(1.0,tk.END)
    def serach_input():
        global sumi_1 ,save4,saveK1,saveK2,saveK3
        save4.clear()
        saveK1.clear()
        sumi_1=0
        Time=date.get()
        
        #Get Collection
        doc_ref = db.collection("行事曆")
        docs = doc_ref.get()
        #print("docs=",docs)
        for doc in docs:
            sumi_1+=1
            save4.append(doc.to_dict())
        print("save4=",save4)   
        print("sumi_1=",sumi_1)
        for i in range(0,sumi_1):
            saveK1.append(save4[i]['Date']) 
            saveK2.append(save4[i]['content']) 
            saveK3[saveK1[i]]=saveK2[i]
        print("saveK1=",saveK1) 
        print("saveK2=",saveK2) 
        print("saveK3=",saveK3) 
        T.delete(1.0,tk.END)
        if Time in saveK1:
            T.insert('end',saveK3[Time])
        else: 
            T.insert('end',"無資料可查詢")      

    tk.Button(root, text = '儲存', command =date_input,font= ('Noto Sans Mono CJK TC Regular',20)).place(x = 475, y = 20)
    tk.Button(root, text = '清空', command =Delete_input,font= ('Noto Sans Mono CJK TC Regular',20)).place(x = 395, y = 20)
    tk.Button(root, text = '查詢', command =serach_input,font= ('Noto Sans Mono CJK TC Regular',20)).place(x = 310, y = 20)
    root.mainloop()
if __name__ == '__main__':
    saveK1=[]
    saveK2=[]
    saveK3={}
    save4=[]
    sumi_1=0
    # 引用私密金鑰
    # path/to/serviceAccount.json 請用自己存放的路徑
    cred = credentials.Certificate(r'./serviceAccount.json')

    # 初始化firebase，注意不能重複初始化
    firebase_admin.initialize_app(cred)

    # 初始化firestore
    db = firestore.client()

    save4.clear()
    saveK1.clear()
    sumi_1=0
    #Get Collection
    doc_ref = db.collection("行事曆")
    docs = doc_ref.get()
    #print("docs=",docs)
    for doc in docs:
        sumi_1+=1
        save4.append(doc.to_dict())
    for i in range(0,sumi_1):
        saveK1.append(save4[i]['Date']) 
        saveK2.append(save4[i]['content']) 
        saveK3[saveK1[i]]=saveK2[i]
    my_main()
