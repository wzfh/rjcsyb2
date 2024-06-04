# import binascii
# import csv
import os
# import threading
# import tkinter as tk
# from tkinter import *
# from tkinter.colorchooser import askcolor
# from tkinter.ttk import *
# import ttkbootstrap as ttk
# import win32com.client  # TTS
# from tkwebview2.tkwebview2 import WebView2
# from V3ku import *
# from 出租车.V905ku import 报警标志, 车辆状态, 经纬度, 速度, 签退方式, 报警标志1, 车辆状态1, 经纬度1, 速度1, 评价选项, \
#     电召订单ID, 交易类型
# from 报警 import *
#
# init_window = ttk.Window()
# class MY_GUI(tk.Tk):
#     def __init__(self, init_window_name):
#         self.init_window_name = init_window_name
#
#     def set_init_window(self):
#         self.init_window_name.title("配置版本  作者 : 姚子奇")
#         self.init_window_name.geometry('1100x618+450+200')
#
#         note = Notebook(self.init_window_name)
#         pane1 = Frame()
#
#
#         def search():
#             txt = 'http://www.baidu.com'
#             frame.load_url(txt)
#
#         entry = Entry(pane1, width=50)
#         entry.pack(side="top", padx=5, pady=2)
#         button3 = Button(pane1, text="访问http", command=search)
#         button3.pack(side="top", padx=10, pady=2)
#         frame = WebView2(pane1, 1000, 550)
#         frame.pack(side='left', padx=10)
#         note.add(pane1,text='123')
#         note.pack()
#
#
#
# ZMJ_PORTAL = MY_GUI(init_window)
# ZMJ_PORTAL.set_init_window()
# init_window.mainloop()

import subprocess
import re

# 启动exe程序
def start_exe(exe_path):
    subprocess.Popen(exe_path)

def find_numbers_in_strings(strings):
    pattern = re.compile(r'\d+')
    return [pattern.findall(s) for s in strings if s.strip()]
def stop_exe(exe_name):
    import os
    import signal

    # 获取所有运行中的exe进程
    for i in range(2):
        processes = os.popen('tasklist').read()
        print(processes)
        if exe_name in processes:
            # 找到进程ID
            pid = [i for i in processes.split('\n') if exe_name in i][0].split(' ')
            print(find_numbers_in_strings(pid)[1][0])
            print(exe_name)
            try:
                os.kill(int(find_numbers_in_strings(pid)[1][0]), signal.SIGTERM)
            except OSError:
                print(f'无法关闭 {exe_name}')


# 使用方法
# start_exe(os.getcwd() + "\\conf\\Zombie.exe")  # 替换为你的exe路径和文件名
stop_exe('Zombie.exe')  # 替换为你的exe文件名
