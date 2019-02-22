#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# @Author  : lusheng


# from tkinter import Label, Tk, Entry, Button
from tkinter import *
import requests
import re
from tkinter import messagebox
from PIL import ImageTk
import os




# def callback():
#     print("你好")

def design():
    startUrl = 'http://www.uustv.com/'
    # 获取用户输入的姓名
    name = entry.get()
    # 去空格
    name = name.strip()
    if name == '':
        messagebox.showinfo('提示：', '请输入姓名')
    if len(name) > 5:
        messagebox.showinfo('提示：', '姓名过长，请输入较短的姓名')
    else:
        data = {
            'word': name,
            'sizes': '60',
            'fonts': 'jfcs.ttf',
            'fontcolor': '#000000'
        }
        result = requests.post(startUrl, data=data)
        result.encoding = 'utf-8'
        # 获取网站的源代码
        html = result.text
        reg = '<div class="tu">.<img src="(.*?)"/></div>'
        # 正则表达  （.*?）全部都需要匹配
        imagePath = re.findall(reg, html)
        # 获取图片的完整路径
        imgUrl = startUrl + imagePath[0]
        # print(imgUrl)
        # 获取图片内容
        response = requests.get(imgUrl).content
        f = open('签名.gif', 'wb')
        f.write(response)

        # 图片显示到窗口上
        bm = ImageTk.PhotoImage(file='签名.gif')
        f.close()
        os.remove('签名.gif')
        label2 = Label(root, image=bm)
        label2.bm = bm
        label2.grid(row=2, columnspan=2)

def blank():
    startUrl = 'http://www.uustv.com/'
    data = {
        'word': ' ',
        'sizes': '60',
        'fonts': 'jfcs.ttf',
        'fontcolor': '#000000'
    }
    result = requests.post(startUrl, data=data)
    result.encoding = 'utf-8'
    # 获取网站的源代码
    html = result.text
    reg = '<div class="tu">.<img src="(.*?)"/></div>'
    # 正则表达  （.*?）全部都需要匹配
    imagePath = re.findall(reg, html)
    # 获取图片的完整路径
    imgUrl = startUrl + imagePath[0]
    # print(imgUrl)
    # 获取图片内容
    response = requests.get(imgUrl).content
    f = open('空白签名.gif', 'wb')
    f.write(response)

    # 图片显示到窗口上
    bm = ImageTk.PhotoImage(file='空白签名.gif')
    f.close()
    os.remove('空白签名.gif')
    label2 = Label(root, image=bm)
    label2.bm = bm
    label2.grid(row=2, columnspan=2)


class section:
    def onPaste(self):
        try:
            self.text = root.clipboard_get()
        except TclError:
            pass
        show.set(str(self.text))

    def onCopy(self):
        root.clipboard_clear()
        self.text = entry.get()
        root.clipboard_append(self.text)

    def onCut(self):
        self.onCopy()
        try:
            entry.delete('sel.first', 'sel.last')
        except TclError:
            pass

def popupmenu(event):
    menu.post(event.x_root, event.y_root)



root = Tk()
show = StringVar()
root.title('签名设计')
root.geometry('550x300')
root.geometry('+400+200')
label = Label(root, text='签名',font=('楷体', 20),fg='blue')
label.grid()
entry = Entry(root, textvariable=show, font=('微软雅黑', 20))
entry.grid(row=0, column=1)
button = Button(root,text='签名设计',font=('微软雅黑',18),fg='red',command=design)
button.grid(row=1, column=0)
blank()
section = section()
menu = Menu(root, tearoff=0)
menu.add_command(label="复制", command=section.onCopy)
menu.add_separator()
menu.add_command(label="粘贴", command=section.onPaste)
menu.add_separator()
menu.add_command(label="剪切", command=section.onCut)

menubar = Menu(root)
filemenu = Menu(menubar, tearoff=False)
filemenu.add_command(label='打开', command=callback)
filemenu.add_command(label='保存', command=callback)
filemenu.add_separator()  # 添加分割线
filemenu.add_command(label='退出', command=root.quit)
menubar.add_cascade(label='文件', menu=filemenu)  # 创建级联菜单，menu选项指定下一级的菜单是什么
root.config(menu=menubar)

editmenu = Menu(menubar, tearoff=False)
editmenu.add_command(label='剪切', command=callback)
editmenu.add_command(label='拷贝', command=callback)
editmenu.add_separator()  # 添加分割线
editmenu.add_command(label='粘贴', command=callback)
menubar.add_cascade(label='编辑', menu=editmenu)
entry.bind("<Button-3>", popupmenu)


root.mainloop()
# 在IDLE中点退出没反应是因为IDLE也是Tkinter实现的，他们两个共用了一个mainloop()，退出代码重复了，产生了冲突

