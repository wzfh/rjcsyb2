import binascii
import csv
import os
import threading
import tkinter as tk
from tkinter import *
from tkinter.colorchooser import askcolor
from tkinter.ttk import *
import ttkbootstrap as ttk
import win32com.client  # TTS
from tkwebview2.tkwebview2 import WebView2
from V3ku import *
from 出租车.V905ku import 报警标志, 车辆状态, 经纬度, 速度, 签退方式, 报警标志1, 车辆状态1, 经纬度1, 速度1, 评价选项, \
    电召订单ID, 交易类型
from 报警 import *

init_window = ttk.Window()
class MY_GUI(tk.Tk):
    def __init__(self, init_window_name):
        self.init_window_name = init_window_name

    def set_init_window(self):
        self.init_window_name.title("配置版本  作者 : 姚子奇")
        self.init_window_name.geometry('1100x618+450+200')

        note = Notebook(self.init_window_name)
        pane1 = Frame()


        def search():
            txt = 'http://www.baidu.com'
            frame.load_url(txt)

        entry = Entry(pane1, width=50)
        entry.pack(side="top", padx=5, pady=2)
        button3 = Button(pane1, text="访问http", command=search)
        button3.pack(side="top", padx=10, pady=2)
        frame = WebView2(pane1, 1000, 550)
        frame.pack(side='left', padx=10)
        note.add(pane1,text='123')
        note.pack()



ZMJ_PORTAL = MY_GUI(init_window)
ZMJ_PORTAL.set_init_window()
init_window.mainloop()