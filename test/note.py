# -*- coding: utf-8 -*-
"""
Created on Sat Jun  8 11:36:12 2019

@author: user1
"""


import tkinter.scrolledtext as tkst
import fileinput
import tkinter as tk
import os
import win32clipboard
from tkinter import font
from tkinter import messagebox
from tkinter import filedialog
from tkinter import colorchooser

t1 = []
root = None

def die(event = None):
  root.destroy()

def about():
  messagebox.showinfo(title = "當前版本為1.0,歡迎使用",message = "**作者:韓東\n**狀態:繼續努力ing")
#def newit(event):
  #editorit = editor()
  #editorit.neweditor()
class editor():
  def __init__(self,rt):
    if rt == None:
      self.t = tk.Tk()
    else:
      self.t = tk.Toplevel(rt)

    self.t.title("文本編輯器%d" % (len(t1)+1))
    
    

    self.frm_file = tk.Frame(rt)
    self.frm_file.grid(row =0,column =0,padx =0,sticky = tk.W)
    self.btn_open = tk.Button(self.frm_file,text = "打開",relief = tk.GROOVE,command = self.openfile)
    self.btn_open.pack(side = tk.LEFT,padx =5,fill = tk.BOTH,expand =1)
    self.btn_new = tk.Button(self.frm_file,text = "新建",relief = tk.GROOVE,command = self.neweditor)
    self.btn_new.pack(side =tk.LEFT,padx =5,fill = tk.BOTH)
    self.btn_save = tk.Button(self.frm_file,text = "保存",relief = tk.GROOVE,command = self.savefile)
    self.btn_save.pack(side = tk.LEFT,padx =5,fill = tk.BOTH)
    self.btn_saveas = tk.Button(self.frm_file,text = "另存為",relief = tk.GROOVE,command = self.saveasfile)
    self.btn_saveas.pack(side =tk.LEFT,padx =5,fill = tk.BOTH)
    self.btn_exit = tk.Button(self.frm_file,text = "退出",relief = tk.GROOVE,command = self.close)
    self.btn_exit.pack(side = tk.RIGHT,padx =5,fill = tk.BOTH)

    self.frm_edit = tk.Frame(rt)
    self.frm_edit.grid(row = 0 ,column =1,padx =1,sticky = tk.W)
    self.btn_copy = tk.Button(self.frm_edit,text = "復制")
    self.btn_copy.pack(side = tk.LEFT,padx =5,fill = tk.BOTH,expand =1)
    self.btn_cut = tk.Button(self.frm_edit,text = "剪切")
    self.btn_cut.pack(side = tk.LEFT,padx =5,fill = tk.BOTH,expand =1)
    self.btn_paste = tk.Button(self.frm_edit,text = "黏貼")
    self.btn_paste.pack(side = tk.LEFT,padx =5,fill = tk.BOTH,expand =1)
    self.btn_find = tk.Button(self.frm_edit,text = "查詢")
    self.btn_find.pack(side = tk.LEFT,padx =5,fill = tk.BOTH,expand =1)
    self.btn_allselect = tk.Button(self.frm_edit,text = "全選")
    self.btn_allselect.pack(side = tk.LEFT,padx =5,fill = tk.BOTH,expand =1)
    self.btn_font = tk.Button(self.frm_edit,text = "字體樣式")
    self.btn_font.pack(side = tk.LEFT,padx =5,fill = tk.BOTH,expand =1)
    self.btn_color = tk.Button(self.frm_edit,text = "字體顏色")
    self.btn_color.pack(side = tk.LEFT,padx =5,fill = tk.BOTH,expand =1)

 

    self.bar = tk.Menu(rt)
    self.filem = tk.Menu(self.bar)
    self.filem.add_separator()
    self.filem.add_command(label = "新建",command = self.neweditor,accelerator = "     Ctr +N")
    self.filem.bind_all("<Control-n>",self.neweditor)
    self.filem.add_separator()
    self.filem.add_command(label = "打開",command = self.openfile,accelerator = "     Ctr + O")
    self.filem.bind_all("<Control-o>",self.openfile)
    self.filem.add_separator()
    self.filem.add_command(label = "保存",command = self.savefile,accelerator = "     Ctr +S ")
    self.filem.bind_all("<Control-s>",self.savefile)
    self.filem.add_separator()
    self.filem.add_command(label = "另存為",command = self.saveasfile,accelerator = "     Ctr + D ")
    self.filem.bind_all("<Control-d>",self.saveasfile)

    self.filem.add_command(label = "關閉",command = self.close,accelerator = "     F4")
    self.filem.bind_all("<F4>",self.close)
    self.filem.add_separator()
    self.filem.add_command(label = "退出",command = die,accelerator = "     ESC")
    self.filem.bind_all("<Escape>",die)

    self.editm = tk.Menu(self.bar)
    self.editm.add_separator()
    self.editm.add_command(label = "復制",command = self.copy,accelerator = " "*10 + "Ctr + C")
    self.editm.bind_all("<Control-c>",self.copy)
    self.editm.add_separator()
    self.editm.add_command(label = "黏貼",command = self.paste,accelerator = " "*10 + "Ctr + V")
    self.editm.bind_all("<Control-v>",self.paste)
    self.editm.add_separator()
    self.editm.add_command(label = "剪切",command = self.cut,accelerator = " "*10 + "Ctr + X")
    self.editm.bind_all("<Control-x>",self.cut)
    self.editm.add_separator()
    self.editm.add_command(label = "刪除",command = self.delete_text,accelerator = " "*10 + "Delete")
    self.editm.bind_all("<Delete>",self.delete_text)
    self.editm.add_separator()
    self.editm.add_command(label = "查找",command = self.find_char,accelerator = " "*10 + "Ctr +F")
    self.editm.bind_all("<Control-f>",self.find_char)
    self.editm.add_separator()
    self.editm.add_command(label = "全選",command = self.select_char_all,accelerator = " "*10 + "Ctr + A")
    self.editm.bind_all("<Control-a>",self.select_char_all)

    self.formm = tk.Menu(self.bar)
    self.formm.add_command(label = "字體顏色",command = self.color_it,accelerator = " "*10 + "Alt + C")
    self.formm.bind_all("<Alt-f>",self.color_it)
    self.formm.add_separator()
    self.formm.add_command(label = "字體格式",command = self.font_it,accelerator = " "*10 + "Alt + F")
    self.formm.bind_all("<Alt-f>",self.font_it)


    self.helpm = tk.Menu(self.bar)
    self.helpm.add_command(label = "關於",command = about)

    self.bar.add_cascade(label = "文件",menu = self.filem)
    self.bar.add_cascade(label = "編輯",menu = self.editm)
    self.bar.add_cascade(label = "格式",menu = self.formm)
    self.bar.add_cascade(label = "幫助",menu = self.helpm)
    
    self.t.config(menu = self.bar)

    #self.f = Frame(self.t,width = 512)
    #self.f.pack(expand =1)

    self.st = tkst.ScrolledText(self.t)
    self.st.grid(row =1,column = 0,columnspan =3,pady =3)

  def close(self,event = None):
    self.t.destroy()
  def openfile(self,event =None):
    oname = filedialog.askopenfilename(filetypes = [("打開文件","*.txt")])
    if oname:
      for line in fileinput.input(oname):
        self.st.insert("1.0",line)
      self.t.title(oname)

  def savefile(self,event =None):
    if os.path.isfile(self.t.title()):
      opf = open(self.t.title(),"w")
      opf.write(self.st.get(1.0,tk.END))
      opf.flush()
      opf.close()
      
    else:
      sname = filedialog.asksaveasfilename(title = "保存好你的寶寶喲",filetypes = [("保存文件","*.txt")],defaultextension = ".txt")
      if sname:
        ofp = open(sname,"w")
        ofp.write(self.st.get(1.0,tk.END))
        ofp.flush()
        ofp.close()
      self.t.title(sname)
  def saveasfile(self,event = None):
    sname = filedialog.asksaveasfilename(title = "保存好你的寶寶喲",filetypes = [("保存文件","*.txt")],defaultextension = ".txt")
    if sname:
      ofp = open(sname,"w")
      ofp.write(self.st.get(1.0,tk.END))
      ofp.flush()
      ofp.close()
      self.t.title(sname)
    
  def neweditor(self,event = None):
    global root
    t1.append(editor(root))


  def copy(self,event = None):
    text = self.st.get(tk.SEL_FIRST,tk.SEL_LAST)
    self.st.clipboard_clear()
    self.st.clipboard_append(text)

  def paste(self,event= None):
    try:
      text = self.st.selection_get(selection = "CLIPBOARD")
      self.st.insert(tk.INSERT,text)
      self.st.clipboard_clear()
    except tk.TclError:
      pass
    
  def cut(self,event = None):
    text = self.st.get(tk.SEL_FIRST,tk.SEL_LAST)
    self.st.delete(tk.SEL_FIRST,tk.SEL_LAST)
    self.st.clipboard_clear()
    self.st.clipboard_append(text)
    
  def delete_text(self):
    self.st.delete(tk.SEL_FIRST,tk.SEL_LAST)

  def find_char(self,event = None):
    target = tk.simpledialog.askstring("簡易文本編輯器","尋找字符串")
    if target:
      end = self.st.index(tk.END)
      print(end)
      endindex = end.split(".")
      end_line = int(endindex[0])
      end_column = int(endindex[1])
      pos_line =1
      pos_column=0
      length =len(target)
      while pos_line <= end_line :
        if pos_line == end_line and pos_column +length > end_column:
          break
        elif pos_line < end_line and pos_column + length >500:
          pos_line = pos_line + 1
          pos_column = (pos_column + length) -500
          if pos_column > end_column:
            break
        else:
          pos = str(pos_line)+"."+str(pos_column)
          where = self.st.search(target,pos,tk.END)
          if where:
            print(where)
            where1 =where.split(".")
            sele_end_col = str(int(where1[1])+length)
            sele = where1[0] + "."+ sele_end_col
            self.st.tag_add(tk.SEL,where,sele)
            self.st.mark_set(tk.INSERT,sele)
            self.st.see(tk.INSERT)
            self.st.focus()
        
            again = messagebox.askokcancel(title = "繼續查詢麽")
            if again:
              pos_line = int(where1[0])
              pos_column = int(sele_end_col)
            else:
              aa=messagebox.showinfo(title = "你終於還是放棄了我",message = "你放棄了我--!")
              if aa:
                tk.sys.exit()
                
  def select_char_all(self,event= None):
    self.st.tag_add(tk.SEL,1.0,tk.END)
    self.st.see(tk.INSERT)
    self.st.focus()
  def color_it(self,event = None):
    color = colorchooser.askcolor()
    self.st["foreground"] = color[1]
  def font_it(self,event = None):
    self.t_font = tk.Toplevel()
    self.t_font.title("字體選擇面板")
    self.label_size = tk.Label(self.t_font,text = "字體大小")
    self.label_shape = tk.Label(self.t_font,text = "字體形狀")
    self.label_font = tk.Label(self.t_font,text = "字體類型")
    self.label_weight = tk.Label(self.t_font,text = "字體粗細")
    self.label_size.grid(row = 0 ,column =0,padx =30)
    self.label_shape.grid(row = 0,column =4,padx =30)
    self.label_font.grid(row = 0,column =2,padx =30)
    self.label_weight.grid(row =0,column = 6,padx =30)
    
    self.scroll_size = tk.Scrollbar(self.t_font)
    self.scroll_size.grid(row =1,column=1,stick = tk.NS)
    self.scroll_shape = tk.Scrollbar(self.t_font)
    self.scroll_shape.grid(row =1,column=3,stick = tk.NS)
    self.scroll_font = tk.Scrollbar(self.t_font)
    self.scroll_font.grid(row =1,column=5,stick = tk.NS)
    self.scroll_weight = tk.Scrollbar(self.t_font)
    self.scroll_weight.grid(row =1,column =7,stick = tk.NS)

    list_var_font = tk.StringVar()
    list_var_size = tk.StringVar()
    list_var_shape = tk.StringVar()
    list_var_weight = tk.StringVar()
    
    self.list_font = tk.Listbox(self.t_font,selectmode = tk.BROWSE,listvariable = list_var_font,exportselection =0)
    self.list_font.grid(row = 1,column =2,padx =4)
    list_font_item = ["\"Arial\"","\"Arial Baltic\"","\"Arial Black\"","\"Arial CE\"","\"Arial CYR\"","\"Arial Greek\"","\"Arial Narrow\"",
             "\"Arial TUR\"","\"Baiduan Number\"","\"Batang,BatangChe\""]
    for item in list_font_item:
      self.list_font.insert(0,item)
    self.list_font.bind("<ButtonRelease-1>",self.change_font)

    self.list_shape = tk.Listbox(self.t_font,selectmode = tk.BROWSE,listvariable =list_var_shape,exportselection =0 )
    self.list_shape.grid(row= 1,column =4,padx =4)
    list_shape_item = ["italic","roman"]
    for item in list_shape_item:
      self.list_shape.insert(0,item)
    self.list_shape.bind("<ButtonRelease-1>",self.change_shape)

    self.list_size = tk.Listbox(self.t_font,selectmode = tk.BROWSE,listvariable = list_var_size,exportselection =0)
    self.list_size.grid(row = 1,column = 0,padx =4)
    list_size_item = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]
    for item in list_size_item :
      self.list_size.insert(0,item)
    self.list_size.bind("<ButtonRelease-1>",self.change_size)
    
    self.list_weight = tk.Listbox(self.t_font,selectmode = tk.BROWSE,listvariable = list_var_weight,exportselection =0)
    self.list_weight.grid(row=1,column =6,padx =4)
    list_weight_item = ["bold","normal"]
    for item in list_weight_item:
      self.list_weight.insert(0,item)
    self.list_weight.bind("<ButtonRelease-1>",self.change_weight)
    
    self.labFra_display = tk.LabelFrame(self.t_font,text = "字體樣式演示區域")
    self.labFra_display.grid(row =2,column =0,pady =4)
    self.lab_display = tk.Label(self.labFra_display,text = "我在這裏")
    self.lab_display.pack()

    self.btn_ok = tk.Button(self.t_font,text = "確定",width = 10,height =2,command = self.change)
    self.btn_ok.grid(row = 2,column = 2,pady =4)
    self.btn_cancel = tk.Button(self.t_font,width =10,height =2,text = "取消",command = self.exit_subwindow)
    self.btn_cancel.grid(row =2,column =4,pady =4)
  def change_size(self,event):
    customFont = font.Font(family = "Helvetica",size = 12,weight = "normal",slant = "roman",underline =0)
    tk.size = customFont["size"]
    customFont.configure(size =self.list_size.get(self.list_size.curselection()))
    self.st.config(font = customFont)
    self.size_count = 1
    pass
    
    
  def change_font(self,event):
    customFont = font.Font(family = "Helvetica",size = 12,weight = "normal",slant = "roman",underline =0)
    tk.family = customFont["family"]
    customFont.configure(family =self.list_font.get(self.list_font.curselection()))
    self.st.config(font = customFont)
    self.font_count = 1
    pass

  def change_shape(self,event):
    customFont = font.Font(family = "Helvetica",size = 12,weight = "normal",slant = "roman",underline =0)
    tk.slant = customFont["slant"]
    customFont.configure(slant =self.list_shape.get(self.list_shape.curselection()))
    self.st.config(font = customFont)
    self.shape_count =1
    pass
  def change_weight(self,event):
    customFont = font.Font(family = "Helvetica",size = 12,weight = "normal",slant = "roman",underline =0)
    tk.weight = customFont["weight"]
    customFont.configure(weight =self.list_weight.get(self.list_weight.curselection()))
    self.st.config(font = customFont)
    self.shape_count =1
    
    
  def change(self,event):
    pass
    #self.st["font"] = (self.list_size.get(self.list_size.curselection()))
    #self.st["font"] = (self.list_font.get(self.list_font.curselection()))
    #self.st["font"] = (self.list_shape.get(self.list_shape.curselection()))
  
  def exit_subwindow(self):
    self.t_font.destroy()
    
    
if __name__ == "__main__":
  root = None
  t1.append(editor(root))
  root = t1[0].t
  root.mainloop()