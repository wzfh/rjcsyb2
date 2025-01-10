# import re
# import requests
# from lxml import etree
# import time
# from os import remove
# import aiofiles
# from aiohttp import ClientSession, ClientTimeout
# import asyncio
# from colorama import init
#
#
# def len_str(string):
#     count = 0
#     for ch in string:
#         if ch >= '\u007f':
#             count += 1
#     return count
#
#
# def width(string, length):
#     if length < len_str(string):
#         return 0
#     else:
#         return length - len_str(string)
#
#
# # 获取小说书名、目录、章节链接
# def get_book_info(url):
#     try:
#         response1 = requests.get(url, cookies=cookies, headers=headers)
#         html1 = etree.HTML(response1.text, parser=etree.HTMLParser(encoding='utf-8'))
#         chapter_name1 = html1.xpath('/html/body/div[5]/dl/dd/a/text()')
#         chapter_name2 = html1.xpath('/html/body/div[5]/dl/span/dd/a/text()')
#         chapter_url1 = html1.xpath('/html/body/div[5]/dl/dd/a/@href')
#         chapter_url2 = html1.xpath('/html/body/div[5]/dl/span/dd/a/@href')
#         chapter_names = chapter_name1[0:10] + chapter_name2 + chapter_name1[-10:]
#         chapter_urls = chapter_url1[0:10] + chapter_url2 + chapter_url1[-10:]  # 拼接完整章节目录和链接
#         novel_name = html1.xpath('/html/body/div[4]/div[2]/h1/text()')  # 获取小说书名
#         return chapter_names, chapter_urls, novel_name
#     except Exception as e:
#         print(f'\033[31m获取小说书名出错，出错原因\033[0m：{e}')
#         return [], [], ['error']
#
#
# # 单章小说内容下载
# async def singe_chapter_download(url1, name1, sem):
#     chapter_url = f"https://www.biqg.cc/{url1}"  # 拼接章节网址
#     i = 0
#     async with sem:
#         while i < 5:
#             i += 1
#             try:
#                 timeout = ClientTimeout(total=20)
#                 async with ClientSession(headers=headers, cookies=cookies, timeout=timeout) as session:
#                     async with session.get(chapter_url) as resp1:
#                         html2 = etree.HTML(await resp1.text(), parser=etree.HTMLParser(encoding='utf-8'))
#                         singe_content = html2.xpath('//*[@id="chaptercontent"]/text()')  # 获取小说章节内容
#                         result = re.findall(r'第(.*?)章', singe_content[0])
#                         if len(result):
#                             del singe_content[0]  # 去除可能出现的重复标题
#                         content = singe_content[0:-2]  # 去除网站附带的广告链接
#                         name2 = strinfo.sub('_', name1)  # 去除小说章节书名中的特殊字符，避免生成章节文件时出错
#                         async with aiofiles.open(f"./小说/{name2}.txt", "w", encoding="utf-8") as f:  # 在小说目录下创建临时的单章txt
#                             await f.write(name2 + '\r\r\r')
#                             for lists in content:
#                                 await f.write(lists + '\r\r')
#                         name2_width = 60 - len_str(name2)
#                         print(f'{name2:<{name2_width}}finish')
#                         break
#             except Exception as e:
#                 print(f'{name1}                               false        {i}/5')
#                 print(e)
#
#
# # 创建异步任务
# async def create_tasks(name_chapter, url_chapter, lens):
#     tasks = []
#     if lens > 1000:
#         sema = 1000
#     else:
#         sema = lens
#     sem = asyncio.Semaphore(sema)  # 设置同时进行的异步数量，可以根据上面自行设定，数量越大，下载越快
#     for url4, name3 in zip(url_chapter, name_chapter):
#         tasks.append(asyncio.create_task(singe_chapter_download(url4, name3, sem)))  # 创建任务
#     await asyncio.gather(*tasks)
#
#
# def start_download(url):
#     chapter_name, chapter_url, novel_name = get_book_info(f'https://www.biqg.cc/{url}')  # 获取小说目录，对应的网页链接，书名
#     length = len(chapter_name)
#     if length:
#         print(f"\033[31m《{novel_name[0]}》共{length}章, 开始下载！！\033[0m\n\n")
#         time1 = time.time()
#         loop.run_until_complete(create_tasks(chapter_name, chapter_url, length))  # 提交任务
#         time2 = time.time()
#         with open(f'./小说/{novel_name[0]}.txt', 'w', encoding='utf-8') as f1:  # 将分散的小说章节写入一个{书名}.txt中
#             for chapter_names in chapter_name:
#                 chapter_name2 = strinfo.sub("_", chapter_names)
#                 try:
#                     with open(f'./小说/{chapter_name2}.txt', 'r', encoding='utf-8') as f2:
#                         text1 = f2.read()
#                         f1.write(text1)
#                     remove(f"./小说/{chapter_name2}.txt")  # 移除已写入{书名}.txt的临时章节
#                 except Exception as e:
#                     print(f'{chapter_names}  false 错误原因:{e}')
#             print('==============================下载完成==============================\n')
#         print(f'共耗时：\033[33m{time2 - time1:.2f}s\033[0m\n\n')
#         print(f'\033[32m《{novel_name[0]}》已下载！！！！\033[0m\n\n\n')
#     else:
#         print('error')
#
#
# if __name__ == '__main__':
#     cookies = {
#     }
#
#     headers = {
#         'authority': 'www.biqg.cc',
#         'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
#         'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6', 'cache-control': 'no-cache',
#         'pragma': 'no-cache',
#         'referer': 'https://www.biqg.cc/',
#         'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Microsoft Edge";v="120"', 'sec-ch-ua-mobile': '?0',
#         'sec-ch-ua-platform': '"Windows"', 'sec-fetch-dest': 'document', 'sec-fetch-mode': 'navigate',
#         'sec-fetch-site': 'same-origin',
#         'sec-fetch-user': '?1', 'upgrade-insecure-requests': '1',
#         'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0',
#     }
#     # get_title('https://www.bige3.cc/book/66/') 7293788896888884263
#     init(autoreset=True)
#     loop = asyncio.new_event_loop()
#     asyncio.set_event_loop(loop)
#     strinfo = re.compile('[/:*?"<>|\\\\]')  # 匹配字符串中特殊的字符
#     print('小说保存在exe同目录下的小说文件夹下')
#     a = input('笔趣阁本地搜索：    1\n笔趣阁书籍id下载：    2\n请选择：')
#     if a == '1':
#         with open('./小说/all_books.txt', 'r', encoding='utf-8') as f:
#             books = f.read()
#         books = eval(books)
#         while True:
#             k, target = 1, []
#             a = input('本地搜索已启动:')
#             for dic in books:
#                 result = re.findall(f'{a}', dic[0] + dic[1])
#                 if len(result):
#                     target.append(dic)
#                     print(f'{k:<4}{dic[0]:^{width(dic[0], 60)}}{dic[1]:<{width(dic[1], 40)}}')
#                     k = k + 1
#                     if k > 100:
#                         break
#             if len(target) == 0:
#                 print('小说不存在，请重新输入')
#                 continue
#             choose = input('请输入序号(批量下载请使用空格分隔序号, 重新搜索请输入0, 全部下载请输入101)：')
#             if choose == '0':
#                 continue
#             elif choose == '101':
#                 for book in target:
#                     start_download(book[2])
#                     time.sleep(0.5)
#             else:
#                 choose_list = choose.split(' ')
#                 for ids in choose_list:
#                     if ids.isdigit():
#                         if int(ids) <= len(target):
#                             if int(ids):
#                                 start_download(target[int(ids) - 1][2])
#                                 time.sleep(0.5)
#                             else:
#                                 continue
#                         else:
#                             print('\033[31m序号超出范围，请重新搜索！！\033[0m')
#                     else:
#                         print('\033[31m请输入正确格式的书籍序号！！！！\033[0m')
#     elif a == '2':
#         print('\n请到 \033[32mhttps://www.biqg.cc/\033[0m 网站搜索你想下的小说，并获取相应的的书籍id\n')
#         while True:
#             book_id = input('请输入书籍id(即小说链接数字部分):')
#             start_download(f"/book/{book_id}/")

# import binascii
# import csv
# import os
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
# import webview
# from tkinter import messagebox
# import sys
# import requests
#
# from tkinter.messagebox import *
# import fnmatch
#
# LOG_LINE_NUM = 0
# init_window = ttk.Window()
#
# s = ttk.Style()
# s.theme_use("superhero")
#
# now_time = time.strftime('%Y%m%d%H%M%S', time.localtime())
# now_time1 = time.strftime('%H%M%S', time.localtime())
#
#
# def char_to_hex(char):
#     return hex(ord(char))[2:]
#
#
# def copy(editor, event=None):
#     editor.event_generate("<<Copy>>")
#
#
# def paste(editor, event=None):
#     editor.event_generate('<<Paste>>')
#
#
# def selectAll(editor, event=None):
#     editor.tag_add('sel', '1.0', END)
#
#
# current_directory = os.getcwd()
#
# mp3_pattern = '*.mp3'
# ico_pattern = '*.ico'
# gif_pattern = '*.gif'
#
#
# class MY_GUI(tk.Tk):
#     def __init__(self, init_window_name):
#         self.init_window_name = init_window_name
#         conf_ini = current_directory + "\\conf\\config.ini"
#         config = ConfigObj(conf_ini, encoding='UTF-8')
#         self.conf_wg = config['ces']['出租车_cswg']
#         self.conf_905wg_port = config['ces']['出租车_cs905wg_port']
#         self.conf_808wg_port = config['ces']['出租车_cs808wg_port']
#         self.conf_wd = config['address']['茂名市WD']
#         self.conf_jd = config['address']['茂名市JD']
#         self.conf_wd1 = config['address']['规划WD']
#         self.conf_jd1 = config['address']['规划JD']
#         self.sbei905 = config['sbei']['905sbei']
#         self.sbei808 = config['sbei']['808sbei']
#         self.baojing = config['905baojing']
#         self.baojing808 = config['808baojing']
#         self.jiexurl = config['URL']['jiexurl']
#         self.Zombie = config['Zombie']['range']
#         self.jinyong = config['Zombie']['jinyong']
#
#     # 部标位置
#
#     def thread_it(self, func, *args):
#         """ 将函数打包进线程 """
#         self.myThread = threading.Thread(target=func, args=args)
#         self.myThread.daemon = True
#         self.myThread.start()
#
#     def show_menu(self, event):
#         self.init_window_name.menu.post(event.x_root, event.y_root)
#
#     def topmost_on(self):
#         if self.init_window_name.attributes('-topmost'):
#             self.init_window_name.attributes('-topmost', False)
#             self.init_window_name.menu.entryconfig(1, label='窗口置顶')
#         else:
#             self.init_window_name.attributes('-topmost', True)
#             self.init_window_name.menu.entryconfig(1, label='取消置顶')
#
#     def choose_color(self):
#         color = askcolor()[1]
#         if color:
#             self.init_window_name.config(bg=color)
#             self.init_window_name.set_value_to_registry('background_color', color)
#
#     def zhuti(self):
#         theme_names = s.theme_names()
#         print(theme_names)
#         theme_selection = Toplevel(self.init_window_name)
#         theme_selection.title("选择主题")
#         theme_selection.geometry('450x70+750+400')
#         label = Label(theme_selection, text="主题选择")
#         label.grid(row=0, column=0)
#         theme_cbo = ttk.Combobox(
#             master=theme_selection,
#             text=s.theme.name,
#             values=theme_names,
#             width=60, height=20,
#         )
#         theme_cbo.grid(row=1, column=0)
#
#         def change_theme(event):
#             theme_cbo_value = theme_cbo.get()
#             s.theme_use(theme_cbo_value)
#             theme_cbo.selection_clear()
#
#         theme_cbo.bind('<<ComboboxSelected>>', change_theme)
#
#     def tm(self):
#         def confirm():
#             value = input_entry.get().strip()
#             if value:
#                 value = int(value) * float("0.1")
#                 self.init_window_name.attributes('-alpha', value)
#
#         input_dialog = Toplevel(self.init_window_name)
#         input_dialog.title("窗口透明度设置")
#         input_dialog.geometry('380x77+750+400')
#         input_label = Label(input_dialog, text="透明度值：(%)")
#         input_label.grid(row=0, column=0)
#         items = ("1", "2", "3", "4", "5", "6", "7", "8", "9")
#         input_entry = Combobox(input_dialog, width=50, values=items)
#         input_entry.grid(row=1, column=0)
#         input_entry.current(5)
#         confirm_button = tk.Button(input_dialog, text="确认", command=confirm)
#         confirm_button.grid(row=2, column=0)
#
#     def get_current_time5(self):
#         current_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
#         return current_time
#
#     def payload(self):
#         import json
#         payload = self.payload_Text.get(1.0, END)
#         data = json.loads(payload)
#         print(data)  # 输出解析后的数据
#         return data
#
#     def 车辆(self):
#         for i in range(1):
#             url = "http://tx.dev.car900.com:9999/car/v4/api/assets/add.json"
#             headers = {
#                 "Sessionid": f"e0bbd098955a4dc0852b96f054ed1c2f",
#                 "User-Agent": "Apipost/8 (https://www.apipost.cn)",
#                 "Content-Type": "application/json"
#             }
#             response = requests.request("POST", url, json=self.payload(), headers=headers)
#             print(response.text)
#
#     # 设置窗口
#     def set_init_window(self):
#         self.init_window_name.title("配置版本  作者 : 姚子奇")
#         self.init_window_name.geometry('1100x602+450+200')
#         note = Notebook(self.init_window_name)
#         pane2 = Frame()
#         self.init_window_name.menu = Menu(pane2, tearoff=0)
#         self.init_window_name.menu.add_command(label="退出应用", command=self.init_window_name.quit)
#         self.init_window_name.menu.add_command(label="窗口置顶", command=self.topmost_on)
#         self.init_window_name.menu.add_command(label="修改颜色", command=self.choose_color)
#         self.init_window_name.menu.add_command(label="窗口透明度设置", command=self.tm)
#         self.init_window_name.menu.add_command(label="主题切换", command=self.zhuti)
#         self.init_window_name.bind("<Button-3>", self.show_menu)
#
#         self.fw_Text_label2 = Label(pane2, text="环境url")
#         self.fw_Text_label2.grid(row=0, columnspan=2, sticky=N)
#
#         items = ("")
#         self.fw_Text2 = Combobox(pane2, width=50, height=2, values=items)
#         self.fw_Text2.grid(row=1, column=0, sticky=W)
#         #
#         self.payload_Text_label2 = Label(pane2, text="参数")
#         self.payload_Text_label2.grid(row=2, columnspan=2, sticky=N)
#         self.payload_Text = Text(pane2, width=50, height=20)
#         self.payload_Text.grid(row=3, column=0, sticky=W)
#
#         self.button = Button(pane2, text="发送", width=10,
#                              command=self.车辆)
#         self.button.grid(row=4, column=0)
#
#         note.add(pane2, text='部标808TCP发送')
#         note.grid()
#
#
# def countdown(t):
#     for i in range(t):
#         print("\r休眠倒计时：%02d" % (t - i) + '秒', end='')
#         time.sleep(1)
#
#
# def gui4_start():
#     ZMJ_PORTAL = MY_GUI(init_window)
#     ZMJ_PORTAL.set_init_window()
#     init_window.deiconify()
#     for filename in os.listdir(current_directory):
#         if fnmatch.fnmatch(filename, ico_pattern):
#             init_window.iconbitmap(f"{filename}")
#     init_window.mainloop()
#
#
# # ZMJ_PORTAL = MY_GUI(init_window)
# # ZMJ_PORTAL.车辆(1)
# gui4_start()
# # if __name__ == '__main__':
# 导入gooey
import cv2
import ddddocr
import os
import cchardet
import datetime
import fake_useragent
import httpx
import threading
from tkinter import *
from PIL import ImageTk, Image
from curl2py import curlParseTool
from tkinter import filedialog
from tkinter import ttk, scrolledtext, simpledialog
from parsel import Selector

tabControl = ttk.Notebook(self.app)  # Create Tab Control
http_chkout = ttk.Frame(tabControl)  # http 窗口
tabControl.add(http_chkout, text='HTTP')
Curl = ttk.Frame(tabControl)
tabControl.add(Curl, text='CURL')
Yzm = ttk.Frame(tabControl)
tabControl.add(Yzm, text='验证码')


def http_check(self, http_chkout):
    # ----------------- http 测试界面 ------------------ #
    chec = ttk.Frame(http_chkout)
    chec.grid(column=0, row=0)
    # 请求方式列表
    self.method = ttk.Combobox(chec, width=8)
    self.method['values'] = ('GET', 'POST', 'PUT')
    self.method.grid(column=0, row=1)
    self.method.current(0)  # 设置初始显示值，值为元组['values']的下标
    self.method.config(state='readonly')  # 设为只读模式
    # URL
    self.url = ttk.Entry(chec, width=88)
    self.url.grid(column=1, row=1, sticky='W')
    search = ttk.Button(chec, text="测试", width=10, command=self.search)  # 搜索
    search.grid(column=2, row=1)
    # 状态    states
    states = ttk.Frame(http_chkout)
    states.grid(column=0, row=1, ipadx=1, sticky=W)
    state1 = ttk.Frame(states)
    state1.grid(column=0, row=0, pady=10, padx=20, sticky=W)
    state2 = ttk.Frame(states)
    state2.grid(column=1, row=0, pady=10, padx=20, sticky=W)
    state3 = ttk.Frame(states)
    state3.grid(column=2, row=0, pady=10, padx=20, sticky=W)
    # 上面 三个  框架
    Label(state1, text="请求头").grid(column=0, row=0)
    add = ttk.Button(state1, text="➕", width=5, command=self.add)
    add.grid(column=1, row=0)
    del_e = ttk.Button(state1, text="➖", width=5, command=self.dele)
    del_e.grid(column=2, row=0)
    curl = ttk.Button(state1, text="curl", width=5, command=self.Curl)
    curl.grid(column=3, row=0)
    self.table_header = ttk.Treeview(state1, show="headings", height=13, columns=("name", "value"))
    self.table_header.column("name", width=65, anchor='center')
    self.table_header.column("value", width=130, anchor="w")
    self.table_header.heading("name", text="name")
    self.table_header.heading("value", text="value")
    self.table_header.grid(column=0, row=1, columnspan=4, pady=5)  # column 列

    Label(state2, text="DATA ( param )").grid(column=0, row=0)
    self.Data = scrolledtext.ScrolledText(state2, width=33, height=10, wrap=WORD)
    self.Data.grid(column=0, row=2)
    Label(state2, text="JSON").grid(column=0, row=3)
    self.Data = scrolledtext.ScrolledText(state2, width=33, height=10, wrap=WORD)
    self.Data.grid(column=0, row=4)

    Label(state3, text="特殊选择").grid(column=0, row=0, columnspan=3)
    self.http2 = BooleanVar()  # HTTP 版本选择
    Checkbutton(state3, text="Http2.0 (默认1.0)", variable=self.http2).grid(column=0, row=1, sticky=W, columnspan=3)
    self.ua = BooleanVar()  # 随机 UA
    ua = Checkbutton(state3, text="随机UA", variable=self.ua)
    ua.select()
    ua.grid(column=0, row=2, sticky=W, columnspan=3)
    self.Ajax = BooleanVar()
    Checkbutton(state3, text="Ajax XMLHttp", variable=self.Ajax).grid(column=0, row=3, sticky=W, columnspan=3)
    self.verify = BooleanVar()
    verify = Checkbutton(state3, text="忽略证书验证", variable=self.verify)
    verify.select()
    verify.grid(column=0, row=4, sticky=W, columnspan=3)
    self.Xpath = BooleanVar()
    Checkbutton(state3, text="XPATH :", variable=self.Xpath, command=self.small_xpath).grid(column=0, row=5,
                                                                                            sticky=W)
    self.xpath = ttk.Entry(state3, width=20)
    self.xpath.insert(0, "如： //div[@id='xxxx']")
    self.xpath.configure(state='readonly')
    self.xpath.grid(column=1, row=5, sticky=W, columnspan=2)

    Label(state3, text="TimeOut: ").grid(column=0, row=6, sticky=W)
    self.TimeOut = Spinbox(state3, from_=3, to=30, width=5)
    self.TimeOut.grid(column=1, row=6, sticky=W)
    txt_xpath = ttk.Button(state3, text="Xpath", width=10)
    txt_xpath.grid(column=2, row=6, sticky=E)
    self.Proxies = BooleanVar()  # 代理
    proxies = Checkbutton(state3, text="代理 :", variable=self.Proxies, command=self.proxie)
    proxies.grid(column=0, row=7, sticky=W)
    self.proxies = ttk.Entry(state3, width=20)
    self.proxies.insert(0, "如：000.000.000.000:80")
    self.proxies.configure(state='readonly')
    self.proxies.grid(column=1, row=7, sticky=W, columnspan=2)
    self.Auth = BooleanVar()  # 账号密码
    auth = Checkbutton(state3, text="Auth :", variable=self.Auth, command=self.author)
    auth.grid(column=0, row=8, sticky=W)
    self.auth = ttk.Entry(state3, width=20)  # setPlaceholderText
    self.auth.insert(0, "如：username;password")
    self.auth.configure(state='readonly')
    self.auth.grid(column=1, row=8, sticky=W, columnspan=2)

    self.Redirect = BooleanVar()
    redirect = Checkbutton(state3, text="是否允许  重定向", variable=self.Redirect)  # 重定向
    redirect.select()
    redirect.grid(column=0, row=9, sticky=W, columnspan=3)

    result_data = ttk.LabelFrame(state3, text="展示结果类型")
    result_data.grid(column=0, row=10, columnspan=3)
    self.result = IntVar()
    self.result.set(99)

    Radiobutton(result_data, text="Json", variable=self.result, value=1).grid(column=0, row=9, sticky=W)
    Radiobutton(result_data, text="Text", variable=self.result, value=2).grid(column=1, row=9, sticky=W)
    r = Radiobutton(result_data, text="None", variable=self.result, value=3)
    r.select()
    r.grid(column=2, row=9, sticky=W)

    # 展示结果
    # show = ttk.Frame(http_chkout)
    # show.grid(column=0, row=2, pady=10, padx=20, sticky=W, columnspan=3)
    self.Show = scrolledtext.ScrolledText(states, width=10, height=20, wrap=WORD)
    self.Show.grid(column=0, row=1, sticky='WE', columnspan=3, padx=10)


def curl_(self, Curl):
    # ----------------- curl 测试界面 ------------------ #
    curl = ttk.Frame(Curl)
    curl.grid(column=0, row=0, pady=10, padx=20, sticky=W)
    Label(curl, text="CURL 命令").grid(column=0, row=0)
    self.curl_u = scrolledtext.ScrolledText(curl, width=105, height=20, wrap=WORD)
    self.curl_u.grid(column=0, row=1)
    Label(curl, text="CURL 转换结果").grid(column=0, row=2)
    self.curl_result = scrolledtext.ScrolledText(curl, width=105, height=20, wrap=WORD)
    self.curl_result.grid(column=0, row=3)

    self.curl_u.bind("<Key>", self.curl_stran)
    self.curl_u.bind("<Control-Key-v>", self.curl_stran)


def YZM(self, Yzm):
    org_init = """请选择图片放入"""
    pic = ttk.Frame(Yzm)
    pic.grid(column=0, row=0, pady=10, padx=20, sticky=W)
    self.pic_yzm1 = Label(pic, relief="sunken", text=org_init)
    self.pic_yzm1.bind("<Button-1>", self.open_file)
    self.pic_yzm1.grid(column=0, row=0)
    self.pic_yzm2 = Label(pic, relief="sunken", text=org_init)
    self.pic_yzm2.bind("<Button-1>", self.open_file2)
    self.pic_yzm2.grid(column=1, row=0)
    txt = "========================================================================================"
    Label(pic, width=107, height=1, text=txt).grid(column=0, row=1, columnspan=2)
    push_button = ttk.Frame(Yzm)
    push_button.grid(column=0, row=1, pady=10, padx=20, sticky=W)

    # 请求方式列表
    self.code_type = ttk.Combobox(push_button, width=10)
    self.code_type['values'] = ('字符验证码', '滑块验证码', '汉字验证码', '点选验证码')
    self.code_type.grid(column=0, row=0)
    self.code_type.current(0)  # 设置初始显示值，值为元组['values']的下标
    self.code_type.config(state='readonly')  # 设为只读模式
    Label(push_button, padx=10, text="验证码结果：").grid(column=2, row=0)
    Label(push_button, padx=10, text="").grid(column=5, row=0)
    ttk.Button(push_button, text="处理验证码", width=10, command=self.ORC).grid(column=6, row=0)

    self.old_ddddorc = IntVar()
    dc = Checkbutton(push_button, text="老版本模型", variable=self.old_ddddorc)
    dc.deselect()
    dc.grid(column=7, row=0, sticky=W)

    self.code_result = ttk.Entry(push_button, x=10, width=50)
    self.code_result.grid(column=4, row=0, sticky='W')

    self.Identify_code = scrolledtext.ScrolledText(Yzm, width=105, height=15, wrap=WORD)
    self.Identify_code.grid(column=0, row=2)


http_check()
