import math
import os.path
import random
import re
import time
from socket import *

from configobj import ConfigObj


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


def get_bcc(inputStr: str) -> str:
    bcc = 0
    for i in inputStr.split(' '):
        bcc = bcc ^ int(i, 16)

    return f'{bcc:x}'


def get_xor(data):
    result = re.sub(r"(?<=\w)(?=(?:\w\w)+$)", " ", data)
    return result


a = []


class login:
    def __init__(self):
        conf_ini = os.path.dirname(os.path.dirname(__file__)) + "\\conf\\config.ini"
        config = ConfigObj(conf_ini, encoding='UTF-8')
        self.wg = config['ces']['出租车_cswg']
        self.wg_port = config['ces']['出租车_cs808wg_port']
        self.wd = config['address']['茂名市WD']
        self.jd = config['address']['茂名市JD']
        self.baojing = config['808baojing']
        self.ztai = config['808ztai']
        self.sbei = config['sbei']['808sbei']
        self.socket = None
        self.is_connected = False

    def connect(self, ip, port):
        """建立socket连接"""
        try:
            if not self.is_connected:
                self.socket = socket(AF_INET, SOCK_STREAM)
                self.socket.settimeout(10)
                self.socket.connect((f'{ip}', int(port)))
                self.is_connected = True
                print("成功建立连接")
        except Exception as e:
            print(f"连接失败: {str(e)}")
            self.is_connected = False
            self.socket = None

    def reconnect_if_needed(self, ip, port):
        """检查连接状态并在需要时重连"""
        if not self.is_connected or self.socket is None:
            print("检测到连接断开，尝试重新连接...")
            self.connect(f'{ip}', int(port))

    def send_data(self, data, ip, port):
        """发送数据并处理可能的连接错误"""
        try:
            if not self.is_connected:
                self.connect(ip, port)

            self.socket.send(bytes().fromhex(data))
            send = self.socket.recv(1024).hex()
            print('服务器应答：' + send.upper())
            send1 = send.upper()[9:-4]
            a.append(send1)
            print(send1)
            return True
        except Exception as e:
            print(f"发送数据失败: {str(e)}")
            self.is_connected = False
            return False

    def close(self):
        """关闭连接"""
        if self.socket:
            try:
                self.socket.close()
            except:
                pass
        self.is_connected = False
        self.socket = None

    def get(self):  # 注册
        count = 0
        # 建立初始连接
        self.connect("221.3.192.207", 17202)

        for i in range(1):
            try:
                now_time = time.strftime('%Y%m%d%H%M%S', time.localtime())
                wd1 = '23.012173'
                wd2 = float(wd1) * 1000000
                print(int(wd2))
                wd3 = hex(int(wd2))
                jd1 = '114.340462'
                jd2 = float(jd1) * 1000000
                jd3 = hex(int(jd2))
                标识位 = '7E'
                消息ID = '0100'
                设备号 = "13526985577".zfill(12)
                print(f"设备号:{设备号}")
                流水号 = f'{i}'.zfill(4)
                省域ID = "0000"
                市县域ID = "0000"
                制造商ID = "0000000000"
                终端型号 = "0000000000".zfill(20)
                终端ID = "0000000000".zfill(14)
                车牌颜色 = "00"
                车辆标识 = "00003631353431393705D4C64C4441313838310000000000000000000000"
                baojlxs = ["00000010"]
                报警 = random.choice(baojlxs)
                状态 = self.ztai['ACC开定位开北斗GPS满载']
                纬度 = wd3[2:].zfill(8).upper()
                经度 = jd3[2:].zfill(8).upper()
                print(f'纬度:{纬度}' + ' ' + f'经度：{经度}')
                高程 = '0001'
                速度 = f'000A'
                方向 = '000C'
                时间 = now_time[2:]
                附加信息ID = 'EB29000C00B28986047701217055133200060089FFFFEFFF000600C5FFFFBFEF0004002D0F42000300A844'
                消息体属性 = f'{hex(int(len(报警 + 状态 + 纬度 + 经度 + 高程 + 速度 + 方向 + 时间 + 附加信息ID) / 2))[2:]}'.zfill(
                    4)
                注册消息体属性 = "0039"

                # w = 消息ID + 消息体属性 + 设备号 + 流水号 + 报警 + 状态 + 纬度 + 经度 + 高程 + 速度 + 方向 + 时间 + 附加信息ID  # + 附加里程 + 附加油量 + 附加信息ID
                w = 消息ID + 注册消息体属性 + 设备号 + 流水号 + 省域ID + 市县域ID + 制造商ID + 终端型号 + 终端ID + 车牌颜色 + 车辆标识  # + 附加里程 + 附加油量 + 附加信息ID
                a = get_xor(w)
                b = get_bcc(a)
                if b.upper() == "7E":
                    a.replace("00", "01")
                    b = get_bcc(a)
                E = w + b.upper().zfill(2)
                t = '7E' + E.replace("7E", "01") + '7E'
                D = get_xor(E)
                data = f'{标识位} ' + D + f' {标识位}'
                if data[:2] != "7E":
                    print(f"错误：{data}")
                    t = t[:81] + "00" + t[82:]
                    data = get_xor(t)
                    print("修改后data：{}".format(data))
                    print('\n' * 1)
                print(data)
                print(t)
                count += 1

                da = '01020006' + 设备号 + '0000313233343536'
                a1 = get_xor(da)
                b1 = get_bcc(a1)
                if b1.upper() == "7E":
                    a1.replace("00", "01")
                    b1 = get_bcc(a1)
                E1 = da + b1.upper().zfill(2)
                t1 = '7E' + E1.replace("7E", "01") + '7E'
                D1 = get_xor(E1)
                data1 = f'{标识位} ' + D1 + f' {标识位}'
                if data1[:2] != "7E":
                    print(f"错误：{data1}")
                    t1 = t1[:81] + "00" + t1[82:]
                    data1 = get_xor(t1)
                    print("修改后data：{}".format(data1))
                    print('\n' * 1)
                # print(data1)
                print(t1)

                # 发送数据前检查连接
                self.reconnect_if_needed("221.3.192.207", 17202)

                if self.send_data(t, "221.3.192.207", 17202):
                    self.send_data(t1, "221.3.192.207", 17202)
                    print('\n' * 1)
                    countdown(200)

            except Exception as e:
                print(f"发送过程中出现错误: {str(e)}")
                self.is_connected = False  # 标记连接状态为断开
                continue

    def __del__(self):
        """析构函数，确保连接被正确关闭"""
        self.close()


def countdown(t):
    for i in range(t):
        print("\r休眠倒计时:%d" % (t - i) + '秒', end='')
        time.sleep(1)


if __name__ == '__main__':
    ll = login()
    try:
        ll.get()
    finally:
        ll.close()
