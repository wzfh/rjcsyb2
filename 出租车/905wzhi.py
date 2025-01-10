# coding=utf-8
import math
import os
import random
import re
import time
from socket import *
import itertools
from configobj import ConfigObj


def get_longitude(base_log=None, radius=None):
    radius_in_degrees = radius / 111300
    u = float(random.uniform(0.0, 1.0))
    v = float(random.uniform(0.0, 1.0))
    w = radius_in_degrees * math.sqrt(u)
    t = 2 * math.pi * v
    y = w * math.sin(t)
    longitude = y + base_log
    # print()
    return str(longitude)[:10]


def get_latitude(base_lat=None, radius=None):
    radius_in_degrees = radius / 111300
    u = float(random.uniform(0.0, 1.0))
    v = float(random.uniform(0.0, 1.0))
    w = radius_in_degrees * math.sqrt(u)
    t = 2 * math.pi * v
    x = w * math.cos(t)
    latitude = x + base_lat
    # print(str(latitude)[:9])
    return str(latitude)[:9]


def get_bcc(inputStr: str) -> str:
    bcc = 0
    for i in inputStr.split(' '):
        bcc = bcc ^ int(i, 16)

    return f'{bcc:x}'


def get_xor(data):
    result = re.sub(r"(?<=\w)(?=(?:\w\w)+$)", " ", data)
    return result


def countdown(t):
    for i in range(t):
        print("\r休眠倒计时：%d" % (t - i) + '秒', end='')
        time.sleep(1)


class login:

    def __init__(self):
        # conf_ini = os.path.dirname(os.path.dirname(__file__)) + "\\conf\\config.ini"
        # config = ConfigObj(conf_ini, encoding='UTF-8')
        self.wg = '120.241.74.130'
        self.wg_port = '17201'
        self.wd = '21.677431'
        self.jd = '110.919843'
        # self.baojing = config['905baojing']
        # self.ztai = config['905ztai']
        # self.sbei = config['sbei']['905sbei']

    def ww1(self):
        # path = os.path.dirname(__file__)
        # file_path = path + '/e-茂名-12.csv'
        # fCase = open(file_path, 'r', encoding='gbk')
        # datas = csv.reader(fCase)
        # data1 = []
        # o = 0
        # for line in datas:
        #     data1.append(line)
        # for nob1 in range(0, 205):
        #     t = data1[nob1]
        #     o += 1
        #     print('发送第%d条' % o)
        sbeis = ['015874584455']
        sudus = ['00', 'D2', '00', 'E3', '00', 'F4']
        cycle_sbeis = itertools.cycle(sbeis)
        cycle_sudus = itertools.cycle(sudus)
        while True:
            now_time = time.strftime('%Y%m%d%H%M%S', time.localtime())
            wd1 = get_latitude(base_lat=float(self.wd), radius=50)
            wd2 = float(wd1) * 60 / 0.0001
            # wd2 = float(self.wd) * 60 / 0.0001
            wd3 = hex(int(wd2))
            jd1 = get_longitude(base_log=float(self.jd), radius=50)
            jd2 = float(jd1) * 60 / 0.0001
            # jd2 = float(self.jd) * 60 / 0.0001
            jd3 = hex(int(jd2))
            标识位 = '7E'
            消息ID = '0200'
            消息体属性 = '0023'
            # ISU标识 = self.sbei  # 10位
            ISU标识 = next(cycle_sbeis)  # 10位
            流水号 = f'{1}'.zfill(4)
            报警 = '00000001'
            # ztai = [self.ztai['未卫星定位'],
            #         self.ztai['南纬'],
            #         self.ztai['西经'],
            #         self.ztai['停运状态'],
            #         self.ztai['预约任务车'],
            #         self.ztai['空转重'],
            #         self.ztai['重转空'],
            #         self.ztai['ACC开'],
            #         self.ztai['重车'],
            #         self.ztai['车辆油路断开'],
            #         self.ztai['车辆电路断开'],
            #         self.ztai['车门加锁'],
            #         self.ztai['车辆锁定'],
            #         self.ztai['已达到限制营运次数时间'],
            #         self.ztai['ACC开和载客']]
            状态 = '00000100'
            纬度 = wd3[2:].zfill(8).upper()
            经度 = jd3[2:].zfill(8).upper()
            速度 = f'00{next(cycle_sudus)}'
            方向 = '01'
            时间 = now_time[2:]
            附加里程 = f'0104000000{random.randint(10, 15)}'
            油量 = ['5208', '044C', '04B0']
            附加油量 = f'0202{random.choice(油量)}'
            w = 消息ID + 消息体属性 + ISU标识 + 流水号 + 报警 + 状态 + 纬度 + 经度 + 速度 + 方向 + 时间 + 附加里程 + 附加油量
            a = get_xor(w)
            b = get_bcc(a).zfill(2)
            E = w + b.upper()
            t = 标识位 + E.replace("7E", "00") + 标识位
            D = get_xor(E)
            data = '7E ' + D + ' 7E'
            if data[:2] != "7E":
                print(f"错误：{data}")
                print('\n' * 1)
                t = t[:81] + "00" + t[82:]
                data = get_xor(t)
                print("修改后data：{}".format(data))
                print('\n' * 1)
            print(t)
            print(data)
            s = socket(AF_INET, SOCK_STREAM)
            s.connect((self.wg, int(self.wg_port)))  # 测试
            s.send(bytes().fromhex(data))
            send = s.recv(1024).hex()
            print('服务器应答：' + send.upper())
            print('\n' * 1)
            countdown(3 * 50)


if __name__ == '__main__':
    ll = login()
    ll.ww1()
