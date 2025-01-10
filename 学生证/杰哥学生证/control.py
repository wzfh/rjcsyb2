from ui import WinGUI
import socks
import socket
from tkinter import messagebox
import threading
import time
from until import *
import re
import random


# 示例下载 https://www.pytk.net/blog/1702564569.html
class Controller:
    # 导入UI类后，替换以下的 object 类型，将获得 IDE 属性提示功能
    ui: WinGUI

    def __init__(self):
        pass

    def init(self, ui):
        """
        得到UI实例，对组件进行初始化配置
        """
        self.ui = ui

    def connect(self, evt):
        ip = self.ui.tk_input_lxv77ls0.get().strip()
        port = self.ui.tk_input_lxv78ycf.get().strip()
        print("ip:%s" % str(ip))
        self.tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_addr = (ip, int(port))
        try:
            self.tcp_socket.connect(server_addr)
            messagebox.showinfo('提示', message="连接成功")
            # self.ui.tk_button_lxv773zl.config(text="已连接", state="disabled")
            self.ui.tk_button_lxv773zl.config(text="已连接")
            self.ui.tk_button_lxv773zl.config(state="disabled")
            self.ui.tk_button_lxv7avzl.config(state="normal")
            threading.Thread(target=self.rece_msg, args=(self.tcp_socket,)).start()
            print("开启监听线程")
            # threading.Thread(target=self.send_msg, args=(self.tcp_socket,)).start()
            # print("开启发送线程")
            return True, self.tcp_socket
        except ConnectionRefusedError:
            messagebox.showinfo('提示', message="连接被拒绝")
            return False, "连接被拒绝"
        except TimeoutError:
            messagebox.showinfo('提示', message="连接超时")
            return False, "连接超时"
        except Exception as e:
            print(str(e))
            messagebox.showinfo('提示', message=str(e))
            return False, str(e)

    def disconnect(self, evt):
        try:
            self.tcp_socket.close()
            self.ui.tk_button_lxv773zl.config(text="连接", state="normal")
            self.ui.tk_button_lxv7avzl.config(state="disabled")
            messagebox.showinfo('提示', message="连接断开")
        except:
            messagebox.showinfo('提示', message="请先连接")
        # print("连接断开")

    # def change_page(self, evt):
    #     value = self.ui.tk_select_box_lxv7ckxd.get().strip()
    #     print(value)
    #     if value == "报警数据":
    #         # self.__tk_frame_lxygtwgi(self.tk_label_frame_lxv73o6w).place(x=0, y=4, width=600, height=496)
    #         self.ui.tk_frame_lxygtwgi.place(x=0, y=40, width=199, height=191)
    #     elif value == "自定义文本":
    #         self.ui.tk_frame_lxygtwgi1.place(x=0, y=40, width=199, height=191)
    #         print(2)
    #     elif value == "其他":
    #         self.ui.tk_frame_lxygtwgi2.place(x=0, y=40, width=199, height=191)
    #         print(3)

    def change_page(self, evt):
        self.frames = {}
        self.frames["定位数据"] = self.ui.tk_frame_lxygtwgi
        self.frames["报警数据"] = self.ui.tk_frame_lxygtwgi1
        self.frames["自定义文本"] = self.ui.tk_frame_lxygtwgi2
        self.frames["其他"] = self.ui.tk_frame_lxygtwgi3
        value = self.ui.tk_select_box_lxv7ckxd.get().strip()
        print(value)
        for frame in self.frames.values():
            frame.place_forget()  # 隐藏所有Frame
        if value in self.frames:
            self.frames[value].place(x=0, y=73, width=192, height=158)  # 显示选中的Frame

    def change_page1(self, evt):
        self.frames = {}
        self.frames["设备模式上报"] = self.ui.tk_label_frame_ly8bjuf5
        self.frames["通用"] = self.ui.tk_label_frame_ly8bjuf51
        self.frames["健康参数上报"] = self.ui.tk_label_frame_ly8bjuf52
        self.frames["通话记录上报"] = self.ui.tk_label_frame_ly8bjuf53
        self.frames["到家提醒"] = self.ui.tk_label_frame_ly8bjuf54
        self.frames["上报答题结果"] = self.ui.tk_label_frame_ly8bjuf55
        self.frames["跳绳数据上报"] = self.ui.tk_label_frame_ly8bjuf56
        self.frames["蓝牙信标上传"] = self.ui.tk_label_frame_ly8bjuf56
        value = self.ui.tk_select_box_ly8bh0v7.get().strip()
        print(value)
        for frame in self.frames.values():
            frame.place_forget()  # 隐藏所有Frame
        if value in self.frames:
            self.frames[value].place(x=0, y=30, width=188, height=123)  # 显示选中的Frame
        else:
            self.frames["通用"].place(x=0, y=30, width=188, height=123)  # 显示选中的Frame

    def random_gps(self, evt):
        p = random.uniform(114.106906, 114.117906)
        p1 = round(p, 6)
        p2 = random.uniform(22.468459, 22.479459)
        p3 = round(p2, 6)
        self.ui.tk_input_lxygxlii.delete(0, "end")
        self.ui.tk_input_lxygxzvc.delete(0, "end")
        self.ui.tk_input_lxygxlii.insert(0, p1)
        self.ui.tk_input_lxygxzvc.insert(0, p3)

    def wifi_data(self, evt):
        imei = self.ui.tk_input_lxygvyfs.get().strip()
        mm = "[%s,89860120801790891086,202109271427200000,REPORT_LOCATION_INFO,3,20210927142720,341,2E0.000000N0.000000T00000000000000@460!1!9671!73129860!-56@wifi1!5C:E8:83:9D:F8:C1!-45#wifi2!5C:E8:83:9D:F8:C0!-45#wifi3!5C:E8:83:9E:01:61!-47#wifi4!E8:68:19:62:1B:E1!-57#wifi5!5C:E8:83:9E:01:60!-57#wifi6!5C:E8:83:9E:69:A0!-60#wifi7!E8:68:19:62:1B:E0!-60#wifi8!3C:CD:5D:27:E4:C4!-63#wifi9!E8:68:19:62:1B:E2!-69#wifi10!40:F4:20:8F:F9:1A!-71]" % imei
        try:
            self.send_msg1(self.tcp_socket, mm)
        # self.ui.tk_text_lxy5p1aw.insert('insert', time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))+"  发送数据："+"%s\n"%mm)
        except:
            messagebox.showinfo('提示', message="请先连接服务器")

    def send(self, evt):
        name = self.ui.tk_select_box_lxv7ckxd.get().strip()
        print(name)
        imei = self.ui.tk_input_lxygvyfs.get().strip()
        is_11_digit_number(imei)
        if is_11_digit_number(imei) == True:
            if name == "定位数据":
                gps1 = self.ui.tk_input_lxygxlii.get().strip()
                gps2 = self.ui.tk_input_lxygxzvc.get().strip()
                mm = "[%s,89860484012080099999,202109271427200000,REPORT_LOCATION_INFO,3,20210927142720,79,0E%sN%sT20210927142720@0!0!0!0!0]" % (
                    imei, gps1, gps2)
                # try:
                print(mm)
                self.send_msg1(self.tcp_socket, mm)
                # self.ui.tk_text_lxy5p1aw.insert('insert', time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))+"  发送数据："+"%s\n"%mm)
                # except:
                #     messagebox.showinfo('提示', message="请先连接服务器")

            elif name == "报警数据":
                alarm_value = self.ui.tk_select_box_ly703s7u.get().strip()
                print(alarm_value)
                if alarm_value == "sos报警":
                    mm = "[%s,89860484012080099999,202109271427200000,REPORT_SOS,3,20210927142720,1,1]" % imei
                    try:
                        self.send_msg1(self.tcp_socket, mm)
                        # self.ui.tk_text_lxy5p1aw.insert('insert', time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))+"  发送数据："+"%s\n"%mm)
                    except:
                        messagebox.showinfo('提示', message="请先连接服务器")
                elif alarm_value == "开机":
                    mm = "[{},89860484012080099999,202109271427200000,ALARM_POWER,3,20210927142720,2,4@11%]".format(
                        imei)
                    try:
                        self.send_msg1(self.tcp_socket, mm)
                        # self.ui.tk_text_lxy5p1aw.insert('insert', time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))+"  发送数据："+"%s\n"%mm)
                    except:
                        messagebox.showinfo('提示', message="请先连接服务器")
                elif alarm_value == "关机":
                    mm = "[{},89860484012080099999,202109271427200000,ALARM_POWER,3,20210927142720,2,2@8%]".format(imei)
                    try:
                        self.send_msg1(self.tcp_socket, mm)
                        # self.ui.tk_text_lxy5p1aw.insert('insert', time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))+"  发送数据："+"%s\n"%mm)
                    except:
                        messagebox.showinfo('提示', message="请先连接服务器")
                elif alarm_value == "缺电":
                    mm = "[{},89860484012080099999,202109271427200000,ALARM_POWER,3,20210927142720,5,1@12%]".format(
                        imei)
                    try:
                        self.send_msg1(self.tcp_socket, mm)
                        # self.ui.tk_text_lxy5p1aw.insert('insert', time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))+"  发送数据："+"%s\n"%mm)
                    except:
                        messagebox.showinfo('提示', message="请先连接服务器")
                elif alarm_value == "自动关机":
                    mm = "[{},89860484012080099999,202109271427200000,ALARM_POWER,3,20210927142720,4,3@2%]".format(imei)
                    try:
                        self.send_msg1(self.tcp_socket, mm)
                        # self.ui.tk_text_lxy5p1aw.insert('insert', time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))+"  发送数据："+"%s\n"%mm)
                    except:
                        messagebox.showinfo('提示', message="请先连接服务器")
                elif alarm_value == "心跳":
                    mm = "[{},89860484012080099999,202109271427200000,REPORT_HEARTBEAT,3,20210927142720,6,90%@6000]".format(
                        imei)
                    try:
                        self.send_msg1(self.tcp_socket, mm)
                        # self.ui.tk_text_lxy5p1aw.insert('insert', time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))+"  发送数据："+"%s\n"%mm)
                    except:
                        messagebox.showinfo('提示', message="请先连接服务器")

            elif name == "自定义文本":
                test = self.ui.tk_text_lxy5okbn.get("1.0", "end").strip()
                if test != "":
                    print(test)
                    self.ui.tk_text_lxy5okbn.delete("1.0", "end")
                    try:
                        self.send_msg1(self.tcp_socket, test)
                        # self.ui.tk_text_lxy5p1aw.insert('insert', time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))+"  发送数据："+"%s\n"%mm)
                    except:
                        messagebox.showinfo('提示', message="请先连接服务器1")
                else:
                    messagebox.showinfo('提示', message="输入不能为空")

            elif name == "其他":
                name1 = self.ui.tk_select_box_ly8bh0v7.get().strip()
                if name1 == "设备模式上报":
                    timestamp = int(time.time() * 1000)
                    stat = self.ui.tk_list_box_ly8dvqzm.get().strip()
                    str1 = "[{},89860000192198904130,202109271427200013,DEVICE_STATUS,3,20210927142720,20,0@{}@{}@20]".format(
                        imei, stat, timestamp)
                    try:
                        self.send_msg1(self.tcp_socket, str1)
                        # self.ui.tk_text_lxy5p1aw.insert('insert', time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))+"  发送数据："+"%s\n"%mm)
                    except:
                        messagebox.showinfo('提示', message="请先连接服务器")
                elif name1 == "设备登录":
                    pass
                elif name1 == "健康参数上报":
                    pass
                elif name1 == "通话记录上报":
                    pass
                elif name1 == "到家提醒":
                    pass
                elif name1 == "亲情号码报警":
                    pass
                elif name1 == "上报答题结果":
                    pass
                elif name1 == "跳绳数据上报":
                    pass
                elif name1 == "获取跳绳蓝牙mac地址":
                    pass
                elif name1 == "蓝牙信标上传":
                    pass
                pass
            # print(self.connect(evt))
            # print("发送数据")
        else:
            messagebox.showinfo('提示', message="imei错误")

    def rece_msg(self, tcp_socket):
        # global true
        while True:
            try:
                recv_msg = tcp_socket.recv(1024).decode("utf8")
            except:
                messagebox.showinfo('提示', message="连接超时，请重新连接")
                self.ui.tk_button_lxv773zl.config(text="连接", state="normal")
                self.ui.tk_button_lxv7avzl.config(state="disabled")
            if recv_msg == "exit":
                true = False
            print("接收到的信息为:%s" % str(recv_msg))
            aa = str_split(recv_msg, 0)
            key = "96 B6 71 5E F5 0F A4 55 7F 6C F9 77 17 8E 86 C9"
            iv = "11 C5 00 74 0B E4 4D 4E E5 BD AE D0 3C E7 6F FF"
            bb = AES_CBC_decrypt(aa, key, iv)
            # print("解密后的消息:%s" % str(str(bb, 'utf8').encode('utf-8')))
            match = re.search(r'\[(.*?)\]', bb.decode('utf-8'))
            if match:
                # 提取匹配到的内容（不包括中括号）
                content_inside_brackets = match.group(1)
                print("[%s]" % content_inside_brackets)
                self.ui.tk_text_lxy5p1aw.insert('insert', time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(
                    time.time())) + "  收到数据：" + "[%s]\n" % content_inside_brackets)
            else:
                print("No match found.")

            # a = str_split2(str(bb), ",")
            # try:
            #     name2 = a[3]
            # except:
            #     name2 = ""
            # if name2 != "":
            #     if a[3] == "SET_LOCATION_MODE":
            #         jj = "[123456789012347,89860484012080099999,202109282146240006,SET_LOCATION_MODE,2,20210928214624,1,0]"
            #         kk = jj.replace("202109282146240006", a[2])
            #         time1 = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
            #         ll = kk.replace("20210928214624", time1)
            #         mm = ll.replace("123456789012347", str(a[0])[3:])
            #         print("回复的消息:%s" % str(mm))
            #         self.send_msg1(tcp_socket, mm)
            #     elif a[3] == "SET_REDAY_MODE":
            #         jj = "[123456789012347,89860484012080099999,202109282146240006,SET_REDAY_MODE,2,20210928214624,1,0]"
            #         kk = jj.replace("202109282146240006", a[2])
            #         time1 = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
            #         ll = kk.replace("20210928214624", time1)
            #         mm = ll.replace("123456789012347", str(a[0])[3:])
            #         print("回复的消息:%s" % str(mm))
            #         self.send_msg1(tcp_socket, mm)
            #     elif a[3] == "SET_CLASS_MODEL":
            #         jj = "[123456789012347,89860484012080099999,202109282146240006,SET_CLASS_MODEL,2,20210928214624,1,0]"
            #         kk = jj.replace("202109282146240006", a[2])
            #         time1 = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
            #         ll = kk.replace("20210928214624", time1)
            #         mm = ll.replace("123456789012347", str(a[0])[3:])
            #         print("回复的消息:%s" % str(mm))
            #         self.send_msg1(tcp_socket, mm)
            #     elif a[3] == "SET_DEVICE_RFID":
            #         jj = "[123456789012347,89860484012080099999,202109282146240006,SET_DEVICE_RFID,2,20210928214624,1,1]"
            #         kk = jj.replace("202109282146240006", a[2])
            #         time1 = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
            #         ll = kk.replace("20210928214624", time1)
            #         mm = ll.replace("123456789012347", str(a[0])[3:])
            #         print("回复的消息:%s" % str(mm))
            #         self.send_msg1(tcp_socket, mm)
            #     elif a[3] == "LOCATION_INFO_GET":
            #         jj = "[123456789012347,89860802012080190052,202109282146240006,LOCATION_INFO_GET,2,20210928214624,339,2E0.000000N0.000000T00000000000000@460!0!955  6!24012039!-50@wifi1!5C:E8:83:9E:01:61!-32#wifi2!5C:E8:83:9E:01:60!-32#wifi3!E8:68:19:62:2A:C1!-55#wifi4!5C:E8:83:9D:F8:C0!-59#wifi5!E8:68:19:62:2A:C0!-59#wifi6!E8:68:19:62:2A:C2!-63#wifi7!5C:E8:83:9D:F8:C1!-64#wifi8!3C:CD:5D:27:E4:C5!-65#wifi9!E8:68:19:62:27:60!-71#wifi10!5C:E8:83:9E:69:A0!-73]"
            #         # jj = "[123456789012347,89860802012080190052,202109282146240006,REPORT_LOCATION_INFO,3,20210928214624,79,0E114.107596N22.652717T00000000000000@0!0!0!0!0]"
            #         kk = jj.replace("202109282146240006", a[2])
            #         time1 = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
            #         ll = kk.replace("20210928214624", time1)
            #         mm = ll.replace("123456789012347", str(a[0])[3:])
            #         print("回复的消息:%s" % str(mm))
            #         self.send_msg1(tcp_socket, mm)
            #     elif a[3] == "GET_HEALTH_INFO":
            #         pass
            #         # aa = input("请输入验证码")
            #         # TRIP(tcp_socket,aa)
            #     elif a[3] == "DEVICE_LOGIN":
            #         # logger.info("开始获取健康码")
            #         #       # aa = "[866136055799444,89860477012170573202,202203181413300009,GET_HEALTH_INFO,3,20220318141330,1,0]"
            #         #       # send_msg1(tcp_socket, aa, "健康码")
            #         pass
            #     # if a[3] == "SET_NORMAL_BUTTON":
            #     #     jj = "[123456789012347,89860320757558907795,202109282146240006,SET_NORMAL_BUTTON,2,20210928214624,1,0]"
            #     #     kk = jj.replace("202109282146240006", a[2])
            #     #     time1 = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
            #     #     ll = kk.replace("20210928214624", time1)
            #     #     mm = ll.replace("123456789012347", str(a[0])[3:])
            #     #     logger.info("回复的消息:%s" % str(mm))
            #     #     send_msg1(tcp_socket, mm)
            #     elif a[3] == "SET_HEALTH_NUM":
            #         jj = "[123456789012347,89860484012080099944,202109282146241000,SET_HEALTH_NUM,2,20210928214624,1,0]"
            #         kk = jj.replace("202109282146241000", a[2])
            #         time1 = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
            #         ll = kk.replace("20210928214624", time1)
            #         mm = ll.replace("123456789012347", str(a[0])[3:])
            #         print("回复的消息:%s" % str(mm))
            #         self.send_msg1(tcp_socket, mm)
            #     elif a[3] == "SET_NORMAL_BUTTON":
            #         jj = "[123456789012347,898608051921C0078553,202109282146241000,SET_NORMAL_BUTTON,2,20210928214624,1,0]"
            #         kk = jj.replace("202109282146241000", a[2])
            #         time1 = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
            #         ll = kk.replace("20210928214624", time1)
            #         mm = ll.replace("123456789012347", str(a[0])[3:])
            #         print("回复的消息:%s" % str(mm))
            #         self.send_msg1(tcp_socket, mm)
            #     elif a[3] == "SET_ANSWER_MODE":
            #         jj = "[123456789012347,898608051921C0078553,202110181648490143,SET_ANSWER_MODE,2,20211018164849,1,0]"
            #         kk = jj.replace("202110181648490143", a[2])
            #         time1 = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
            #         ll = kk.replace("20211018164849", time1)
            #         mm = ll.replace("123456789012347", str(a[0])[3:])
            #         logger.info("回复的消息:%s" % str(mm))
            #         self.send_msg1(tcp_socket, mm)
            #     elif a[3] == "SEND_SMS":
            #         jj = "[123456789012347,89860484012080099999,202110181648490143,SEND_SMS,2,20211018164849,1,0]"
            #         kk = jj.replace("202110181648490143", a[2])
            #         time1 = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
            #         ll = kk.replace("20211018164849", time1)
            #         mm = ll.replace("123456789012347", str(a[0])[3:])
            #         print("回复的消息:%s" % str(mm))
            #         self.send_msg1(tcp_socket, mm)
            #     elif a[3] == "REMOTE_OPERATE_TERMINAL":
            #         jj = "[123456789012347,89860484012080099999,202110181648490143,REMOTE_OPERATE_TERMINAL,2,20211018164849,1,0]"
            #         kk = jj.replace("202110181648490143", a[2])
            #         time1 = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
            #         ll = kk.replace("20211018164849", time1)
            #         mm = ll.replace("123456789012347", str(a[0])[3:])
            #         print("回复的消息:%s" % str(mm))
            #         self.send_msg1(tcp_socket, mm)
            #     elif a[3] == "SET_STUDENT_INFO":
            #         jj = "[123456789012347,89860484012080099999,202110181648490143,SET_STUDENT_INFO,2,20211018164849,1,0]"
            #         kk = jj.replace("202110181648490143", a[2])
            #         time1 = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
            #         ll = kk.replace("20211018164849", time1)
            #         mm = ll.replace("123456789012347", str(a[0])[3:])
            #         print("回复的消息:%s" % str(mm))
            #         self.send_msg1(tcp_socket, mm)
            #     elif a[3] == "SET_SKIP_MAC":
            #         jj = "[123456789012347,89860484012080099999,202110181648490143,SET_SKIP_MAC,2,20211018164849,1,0]"
            #         kk = jj.replace("202110181648490143", a[2])
            #         time1 = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
            #         ll = kk.replace("20211018164849", time1)
            #         mm = ll.replace("123456789012347", str(a[0])[3:])
            #         print("回复的消息:%s" % str(mm))
            #         self.send_msg1(tcp_socket, mm)
            #     elif a[3] == "SET_FIND_DEVICES":
            #         jj = "[123456789012347,89860484012080099999,202110181648490143,SET_FIND_DEVICES,2,20211018164849,1,0]"
            #         kk = jj.replace("202110181648490143", a[2])
            #         time1 = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
            #         ll = kk.replace("20211018164849", time1)
            #         mm = ll.replace("123456789012347", str(a[0])[3:])
            #         print("回复的消息:%s" % str(mm))
            #         self.send_msg1(tcp_socket, mm)
            #     else:
            #         pass
            # else:
            #     pass

    def send_msg(self, tcp_socket):
        global true
        while true:
            text = input('请输入要发送的内容\n')
            a = str_split2(str(text), ",")
            time1 = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
            str2 = text.replace(str(a[5]), str(time1))
            key = get_config("key", "key1")
            iv = get_config("key", "iv1")
            res = AES_CBC_encrypt(str2, key, iv)
            res1 = str(res, 'utf-8') + "" + "#kdsjafjalsdjg#170"
            tcp_socket.send(res1.encode())
            print("消息发送成功:%s" % str(str2))
            if self.send_msg == "exit":
                true = False

    def send_msg1(self, tcp_socket, text):
        key = "96 B6 71 5E F5 0F A4 55 7F 6C F9 77 17 8E 86 C9"
        iv = "11 C5 00 74 0B E4 4D 4E E5 BD AE D0 3C E7 6F FF"
        time1 = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
        str2 = text.replace("20210927142720", str(time1))
        res = AES_CBC_encrypt(str2, key, iv)
        res1 = str(res, 'utf-8') + "" + "#kdsjafjalsdjg#170"
        print(res1.encode('raw_unicode_escape'))
        tcp_socket.send(res1.encode('raw_unicode_escape'))
        self.ui.tk_text_lxy5p1aw.insert('insert', time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(
            time.time())) + "  发送数据：" + "%s\n" % str(str2))
        logger.info("消息发送成功:%s" % (str(res1)))
        if self.send_msg == "exit":
            true = False


if __name__ == '__main__':
    pass
