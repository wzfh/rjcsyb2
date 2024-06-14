import os
import math
import threading
import random
import tkinter as tk
from tkinter import *
from tkinter.ttk import *
import ttkbootstrap as ttk
from socket import *
from configobj import ConfigObj
import time
is_on = True
LOG_LINE_NUM = 0
init_window = ttk.Window()

s = ttk.Style()
s.theme_use("superhero")


def get_xor(data):
    result = re.sub(r"(?<=\w)(?=(?:\w\w)+$)", " ", data)
    return result


def get_bcc(inputStr: str) -> str:
    bcc = 0
    for i in inputStr.split(' '):
        bcc = bcc ^ int(i, 16)

    return f'{bcc:x}'


def get_longitude(base_log=None, radius=None):
    radius_in_degrees = radius / 111300
    u = float(random.uniform(0.0, 1.0))
    v = float(random.uniform(0.0, 1.0))
    w = radius_in_degrees * math.sqrt(u)
    t = 2 * math.pi * v
    y = w * math.sin(t)
    longitude = y + base_log
    return str(longitude)[:10]


def get_latitude(base_lat=None, radius=None):
    radius_in_degrees = radius / 111300
    u = float(random.uniform(0.0, 1.0))
    v = float(random.uniform(0.0, 1.0))
    w = radius_in_degrees * math.sqrt(u)
    t = 2 * math.pi * v
    x = w * math.cos(t)
    latitude = x + base_lat
    return str(latitude)[:9]


current_directory = os.getcwd()


class MY_GUI(tk.Tk):
    def __init__(self, init_window_name):
        self.init_window_name = init_window_name
        conf_ini = current_directory + "\\conf\\config.ini"
        config = ConfigObj(conf_ini, encoding='UTF-8')
        self.conf_wg = config['ces']['出租车_cswg']
        self.conf_808wg_port = config['ces']['出租车_cs808wg_port']
        self.conf_wd1 = config['address']['规划WD']
        self.conf_jd1 = config['address']['规划JD']
        self.sbei808 = config['sbei']['808sbei']

    def wzhi部标(self):
        global data
        count = 0
        # try:
        now_time = time.strftime('%Y%m%d%H%M%S', time.localtime())
        wd1 = float(self.wd部标())
        wd2 = wd1 * 1000000
        wd3 = hex(int(wd2))
        jd1 = float(self.jd部标())
        jd2 = jd1 * 1000000
        jd3 = hex(int(jd2))
        标识位 = '7E'
        消息ID = '0200'
        消息体属性 = '002F'
        流水号 = f'{random.randint(12, 20)}'.zfill(4)
        报警 = self.sb_bj2()
        状态 = self.sb_ztai2()
        纬度 = wd3[2:].zfill(8).upper()
        经度 = jd3[2:].zfill(8).upper()
        高程 = f'00{random.randint(12, 20)}'
        速度 = self.sdu2()[2:].zfill(4).upper()
        方向 = f'00{random.randint(12, 20)}'
        时间 = now_time[2:]
        附加信息ID = f'0104000000{self.lic().zfill(2)}0202044C250400000000300103'
        设备号 = self.sb_hao2().zfill(12)
        w = 消息ID + 消息体属性 + 设备号 + 流水号 + 报警 + 状态 + 纬度 + 经度 + 高程 + 速度 + 方向 + 时间 + 附加信息ID
        a = get_xor(w)
        b = get_bcc(a)
        if b.upper() == "7E":
            a.replace("00", "01")
            b = get_bcc(a)
        E = w + b.upper().zfill(2)
        t = 标识位 + E.replace("7E", "01") + 标识位
        D = get_xor(E)
        data = '7E ' + D + ' 7E'
        if data[:2] != "7E":
            t = t[:81] + "00" + t[82:]
            data = get_xor(t)
        count += 1
        tip_content = '\n位置数据：\n{}\n源数据：\n{}\n'.format(data, t)
        self.result_data_Text2.insert(1.0, tip_content)
        if self.ip_on2() == '是':
            s = socket(AF_INET, SOCK_STREAM)
            s.connect((f'{self.ip2()}', int(self.port2())))
            s.settimeout(5)
            try:
                s.send(bytes().fromhex(data))
                send = s.recv(1024).hex()
                tip_content = '服务器应答：\n{}\n\n'.format(send.upper())
                self.result_data_Text2.insert(1.0, tip_content)
            except:
                self.result_data_Text2.delete(1.0, END)
                self.result_data_Text2.insert(1.0, "连接超时，未收到服务器响应")
        # except:
        #     return "数据解析有误，查看是否数据填写错误，修改无误后，请重新点击生成数据"
        self.result_data_Text2.insert(1.0, "生成位置数据条数:{}\n".format(str(count)))
        return ""

    def thread_it(self, func, *args):
        self.myThread = threading.Thread(target=func, args=args)
        self.myThread.daemon = True
        self.myThread.start()

    def sb_on2(self):
        sb_on2 = self.sb_on_Text2.get().strip()
        return sb_on2

    def sb_hao2(self):
        sb = self.sbei_Text2.get().strip()
        return sb

    def sb_ztai2(self):
        ztai = self.ztai_Text2.get().strip()
        if ztai == "ACC开":
            return "00000001"
        elif ztai == "不定位":
            return '00000000'
        elif ztai == "定位":
            return '00000002'
        elif ztai == "南纬":
            return '00000004'
        elif ztai == "ACC开和定位":
            return '00000003'
        elif ztai == "西经":
            return '00000008'
        elif ztai == "停运状态":
            return '00000010'
        elif ztai == "经纬度已经保密插件保密":
            return '00000020'
        elif ztai == "单北斗":
            return '00000040'
        elif ztai == "单GPS":
            return '00000080'
        elif ztai == "北斗GPS双模":
            return '000000C0'
        elif ztai == "ACC开定位开北斗GPS空车":
            return '000000C3'
        elif ztai == "ACC开定位开北斗GPS满载":
            return '000003C3'
        elif ztai == "车辆油路断开":
            return '00000403'
        elif ztai == "车辆电路断开":
            return '00000803'
        elif ztai == "车门加锁":
            return '00001003'

    def sb_bj2(self):
        sb = self.baoji_Text2.get()
        if sb == "紧急报警":
            return '00000001'
        elif sb == "超速报警":
            return '00000002'
        elif sb == "疲劳驾驶":
            return '00000004'
        elif sb == "危险预警":
            return '00000008'
        elif sb == "模块故障":
            return '00000010'
        elif sb == "模块开路":
            return '00000040'
        elif sb == "终端欠压":
            return '00000080'
        elif sb == "终端掉电":
            return '00000100'
        elif sb == "终端LCD故障":
            return '00000200'
        elif sb == "TTS故障":
            return '00000400'
        elif sb == "摄像头故障":
            return '00000800'
        elif sb == "道路运输证IC卡模块故障":
            return '00001000'
        elif sb == "超速预警":
            return '00002000'
        elif sb == "疲劳驾驶预警":
            return '00004000'
        elif sb == "当天累计驾驶时长":
            return '00040000'
        elif sb == "超时停车":
            return '00080000'
        elif sb == "进出区域":
            return '00100000'
        elif sb == "进出路线":
            return '00200000'
        elif sb == "路段行驶时间不足":
            return '00400000'
        elif sb == "路线偏离报警":
            return '00800000'
        elif sb == "车辆VSS故障":
            return '01000000'
        elif sb == "车辆油量异常":
            return '02000000'
        elif sb == "车辆被盗":
            return '04000000'
        elif sb == "车辆非法点火":
            return '08000000'
        elif sb == "车辆非法位移":
            return '10000000'
        elif sb == "碰撞预警":
            return '20000000'
        elif sb == "侧翻预警":
            return '40000000'
        elif sb == "非法开门报警":
            return '80000000'
        elif sb == "所有实时报警":
            return 'FFFCFFFF'
        elif sb == "正常":
            return '00000000'

    def wd部标(self):
        wd = self.wd_Text2.get().strip()
        return wd

    def jd部标(self):
        jd = self.jd_Text2.get().strip()
        return jd

    def su2(self):
        su = self.su_Text2.get().strip()
        return su

    def plsu2(self):
        plsu2 = self.plsu2_Text2.get().strip()
        return plsu2

    def ip2(self):
        ip = self.ip_Text2.get().strip()
        return ip

    def port2(self):
        port = self.port_Text2.get().strip()
        return port

    def sdu2(self):
        sdu = self.sdu_Text2.get().strip()
        sdu1 = hex(int(sdu) * 10)
        return sdu1

    def lic(self):
        lic = self.lic_Text.get().strip()
        hex_num = hex(int(float(lic) * 10))
        return hex_num[2:].upper()

    def ip_on2(self):
        ip_on = self.ip_on_Text2.get().strip()
        return ip_on

    def button_mode2(self):
        global is_on
        wd1 = get_latitude(base_lat=float(self.wd部标()), radius=100)
        jd1 = get_longitude(base_log=float(self.jd部标()), radius=100)
        self.wd_Text2.delete(0, END)
        self.wd_Text2.insert(0, wd1)
        self.jd_Text2.delete(0, END)
        self.jd_Text2.insert(0, jd1)

    def show_menu(self, event):
        self.init_window_name.menu.post(event.x_root, event.y_root)

    def zhuti(self):
        theme_names = s.theme_names()
        print(theme_names)
        theme_selection = Toplevel(self.init_window_name)
        theme_selection.title("选择主题")
        theme_selection.geometry('450x70+750+400')
        label = Label(theme_selection, text="主题选择")
        label.grid(row=0, column=0)
        theme_cbo = ttk.Combobox(
            master=theme_selection,
            text=s.theme.name,
            values=theme_names,
            width=60, height=20,
        )
        theme_cbo.grid(row=1, column=0)

        def change_theme(event):
            theme_cbo_value = theme_cbo.get()
            s.theme_use(theme_cbo_value)
            theme_cbo.selection_clear()

        theme_cbo.bind('<<ComboboxSelected>>', change_theme)

    def qo_login部标(self):
        src = self.init_data_Text2.get().strip()
        if src == '1':
            sbb1 = self.sb_hao2()
            if not sbb1:
                self.result_data_Text2.delete(1.0, END)
                self.result_data_Text2.insert(1.0, "请输入设备号")
            else:
                self.result_data_Text2.delete(1.0, END)
                self.result_data_Text2.insert(1.0, self.wzhi部标())

    def qo_send2(self):
        src = self.data_Text2.get()
        d = src[:-6]
        s = d.replace("7E ", "")
        b = get_bcc(s).zfill(2)
        E = " " + s + ' ' + b.upper() + " "
        t = "7E" + E.replace("7E", "00") + "7E"
        if not src:
            self.result_data_Text2.delete(1.0, END)
            self.result_data_Text2.insert(1.0, "请输入自定义数据")
        else:
            s = socket(AF_INET, SOCK_STREAM)
            s.connect((f'{self.ip2()}', int(self.port2())))
            s.send(bytes().fromhex(t))
            send = s.recv(1024).hex()
            self.result_data_Text2.delete(1.0, END)
            self.result_data_Text2.insert(1.0, f"{t}\n\n")
            self.result_data_Text2.insert(END, f"服务器应答：{send.upper()}\n\n")


    def set_init_window(self):
        self.init_window_name.geometry('1080x542+450+200')
        self.init_window_name.menu = Menu(self.init_window_name, tearoff=0)
        self.init_window_name.menu.add_command(label="主题切换", command=self.zhuti)
        self.init_window_name.bind("<Button-3>", self.show_menu)
        self.ip_Text_label2 = Label(self.init_window_name, text="服务器ip")
        self.ip_Text_label2.grid(row=0, columnspan=2, sticky=N)
        items = (f"{self.conf_wg}", "47.119.168.112", "120.79.176.183")
        self.ip_Text2 = Combobox(self.init_window_name, width=50, height=2, values=items)
        self.ip_Text2.current(0)
        self.ip_Text2.grid(row=1, column=0, sticky=W)
        self.port_Text_label2 = Label(self.init_window_name, text="服务器Port")
        self.port_Text_label2.grid(row=2, columnspan=2, sticky=N)
        items = (f"{self.conf_808wg_port}", "17700", "17800", "7788")
        self.port_Text2 = Combobox(self.init_window_name, width=50, height=2, values=items)
        self.port_Text2.current(0)
        self.port_Text2.grid(row=3, column=0, sticky=W)
        self.su_Text_label2 = Label(self.init_window_name, text="循环发送次数(禁用)")
        self.su_Text_label2.grid(row=4, columnspan=2, sticky=W)
        items = ("0", "10")
        self.su_Text2 = Combobox(self.init_window_name, width=22, height=2, values=items, state='disabled')
        self.su_Text2.current(0)
        self.su_Text2.grid(row=5, column=0, sticky=W)
        self.plsu2_Text_label2 = Label(self.init_window_name, text="批量上线设备次数(禁用)")
        self.plsu2_Text_label2.grid(row=4, columnspan=2, sticky=E)
        items = ("1", "10")
        self.plsu2_Text2 = Combobox(self.init_window_name, width=22, height=2, values=items, state='disabled')
        self.plsu2_Text2.current(0)
        self.plsu2_Text2.grid(row=5, column=0, sticky=E)
        self.sbei_Text_label2 = Label(self.init_window_name, text="808部标设备号")
        self.sbei_Text_label2.grid(row=6, column=0, columnspan=1, sticky=N)
        items = (f"{self.sbei808}", "10356000000", "10351000000")
        self.sbei_Text2 = Combobox(self.init_window_name, width=50, height=2, values=items)
        self.sbei_Text2.current(0)
        self.sbei_Text2.grid(row=7, column=0, sticky=N, columnspan=1)
        self.on_ = Button(self.init_window_name, text="随机经纬度", width=10, command=self.button_mode2)
        self.on_.grid(row=9, column=10)
        self.wd_Text_label2 = Label(self.init_window_name, text="纬度")
        self.wd_Text_label2.grid(row=8, column=0, columnspan=1, sticky=N)
        items = (f"{self.conf_wd1}", "23.012173", "32.330217")
        self.wd_Text2 = Combobox(self.init_window_name, width=50, height=2, values=items)
        self.wd_Text2.current(0)
        self.wd_Text2.grid(row=9, column=0, sticky=N, columnspan=1)
        self.jd_Text_label2 = Label(self.init_window_name, text="经度")
        self.jd_Text_label2.grid(row=10, column=0, columnspan=1, sticky=N)
        items = (f"{self.conf_jd1}", "114.340462", "104.903551")
        self.jd_Text2 = Combobox(self.init_window_name, width=50, height=2, values=items)
        self.jd_Text2.current(0)
        self.jd_Text2.grid(row=11, column=0, sticky=N, columnspan=1)
        self.ip_on_Label2 = Label(self.init_window_name, text="发服务器")
        self.ip_on_Label2.grid(row=11, column=10, sticky=N)
        items = ("否", "是")
        self.ip_on_Text2 = Combobox(self.init_window_name, width=2, height=3, values=items)
        self.ip_on_Text2.current(0)
        self.ip_on_Text2.grid(row=12, column=10, columnspan=1, sticky=N)
        self.baoj_Text_label2 = Label(self.init_window_name, text="报警")
        self.baoj_Text_label2.grid(row=12, column=0, columnspan=1, sticky=N)
        items = ("正常", "紧急报警", "超速报警", "疲劳驾驶", "危险预警", "模块故障", "模块开路", "终端欠压", "终端掉电",
                 "终端LCD故障", "TTS故障",
                 "摄像头故障", "道路运输证IC卡模块故障", "超速预警", "疲劳驾驶预警", "当天累计驾驶时长", "超时停车",
                 "进出区域", "进出路线",
                 "路段行驶时间不足", "路线偏离报警", "车辆VSS故障", "车辆油量异常", "车辆被盗", "车辆非法点火",
                 "车辆非法位移", "碰撞预警", "侧翻预警",
                 "非法开门报警", "所有实时报警",)
        self.baoji_Text2 = Combobox(self.init_window_name, width=50, height=12, values=items)
        self.baoji_Text2.current(0)
        self.baoji_Text2.grid(row=13, column=0, sticky=N, columnspan=1)
        self.sdu_Text_label2 = Label(self.init_window_name, text="速度")
        self.sdu_Text_label2.grid(row=14, columnspan=2, sticky=W)
        items = ("10", "20", "30", "40")
        self.sdu_Text2 = Combobox(self.init_window_name, width=22, height=20, values=items)
        self.sdu_Text2.current(1)
        self.sdu_Text2.grid(row=15, column=0, sticky=W)
        self.lic_Text_label = Label(self.init_window_name, text="里程")
        self.lic_Text_label.grid(row=14, columnspan=2, sticky=E)
        items = ("12", "23")
        self.lic_Text = Combobox(self.init_window_name, width=22, height=2, values=items)
        self.lic_Text.current(0)
        self.lic_Text.grid(row=15, column=0, sticky=E)
        self.times_Text_label2 = Label(self.init_window_name, text="发送停顿时间(禁用)")
        self.times_Text_label2.grid(row=14, column=11)
        items = ("1", "0.5", "1.5", "2")
        self.times_Text2 = Combobox(self.init_window_name, width=60, height=20, values=items, state='disabled')
        self.times_Text2.current(0)
        self.times_Text2.grid(row=15, column=11, sticky=N)
        self.init_data_label2 = Label(self.init_window_name, text="位置数据包请按1")
        self.init_data_label2.grid(row=16, column=0, sticky=N)
        items = ("1",)
        self.init_data_Text2 = Combobox(self.init_window_name, width=50, height=12, values=items, state='disabled')
        self.init_data_Text2.current(0)
        self.init_data_Text2.grid(row=17, column=0, columnspan=1, sticky=N)
        self.ztai_Text_label2 = Label(self.init_window_name, text="车辆状态")
        self.ztai_Text_label2.grid(row=16, column=11)
        items = (
            "ACC开", "ACC开和定位", "不定位", "定位", "停运状态", "经纬度已经保密插件保密", "南纬", "西经",
            "车辆油路断开", "车辆电路断开", "单北斗", "单GPS", "北斗GPS双模", "ACC开定位开北斗GPS满载",
            "ACC开定位开北斗GPS空车",)
        self.ztai_Text2 = Combobox(self.init_window_name, width=60, height=20, values=items)
        self.ztai_Text2.grid(row=17, column=11)
        self.ztai_Text2.current(1)
        self.data_label2 = Label(self.init_window_name, text="自定义发送(选择服务器ip和port端口)")
        self.data_label2.grid(row=18, column=0, sticky=N)
        items = ()
        self.data_Text2 = Combobox(self.init_window_name, width=50, height=2, values=items)
        self.data_Text2.grid(row=19, column=0, sticky=N)
        self.result_Text2 = Button(self.init_window_name, text="发送", command=lambda: self.thread_it(self.qo_send2))
        self.result_Text2.grid(row=19, column=10, )
        self.result_data_label2 = Label(self.init_window_name, text="输出结果：有返回，即发送成功")
        self.result_data_label2.grid(row=0, column=11)
        self.result_data_Text2 = Text(self.init_window_name, width=85, height=20, relief='solid')
        self.result_data_Text2.grid(row=1, column=11, rowspan=13, columnspan=15)
        self.str_trans_to_md5_button2 = Button(self.init_window_name, text="专用808生成", width=10,
                                               command=lambda: self.thread_it(self.qo_login部标))
        self.str_trans_to_md5_button2.grid(row=5, column=10)





def gui4_start():
    ZMJ_PORTAL = MY_GUI(init_window)
    ZMJ_PORTAL.set_init_window()
    init_window.deiconify()
    init_window.mainloop()


gui4_start()
