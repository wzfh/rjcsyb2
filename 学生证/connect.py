import socket
from connect001 import *
from Crypto.Cipher import AES
import base64
import configparser
import os
import time
from binascii import b2a_hex, a2b_hex
import random


#
# key = "97 26 4F E3 C3 77 C0 8A D2 58 CB D0 01 63 A9 5A"
# iv = "14 DB AF 0B CA F4 43 5E 1D C5 92 FF 92 41 42 2A"
#
#
# def AES_CBC_decrypt(text, key, iv):
#     bs = 16
#     key = bytes.fromhex(key)
#     iv = bytes.fromhex(iv)
#     text = base64.b64decode(text)
#     mode = AES.MODE_CBC
#
#     cryptos = AES.new(key, mode, iv)
#     plain_text = cryptos.decrypt(text)
#     str_data = plain_text.decode('utf-8')
#     str_data = str_data.replace('\r', '')
#
#     return str_data
#
#
# def AES_CBC_encrypt(text, key, iv):
#     bs = 16
#     PADDING = lambda s: s + (bs - len(s) % bs) * chr(bs - len(s) % bs)
#     mode = AES.MODE_CBC
#     key = bytes.fromhex(key)
#     iv = bytes.fromhex(iv)
#     cryptos = AES.new(key, mode, iv)
#     crypt = cryptos.encrypt(PADDING(text).encode('utf-8'))
#     print('请求的数据：' + text)
#     crypted_str = base64.b64encode(crypt)
#     return crypted_str


def 定位数据():
    WD = '21.677431'
    JD = '110.919843'
    now_time = time.strftime('%Y%m%d%H%M%S', time.localtime())
    # 消息头
    消息头起始符 = '['
    设备号 = '867082058798585'.zfill(15)
    分隔符 = ','
    ICCID = '89860000192027575850'.zfill(20)
    交易流水号 = f'{now_time}0000'
    接口标识 = 'REPORT_LOCATION_INFO'
    报文类型 = '3'  # 平台下发请求标示 1，则终 端响应标示为 2，终端上报接口标 示为 3，平台响应标示为 4
    时间 = f'{now_time}'
    报文长度 = '79'
    报文体 = f'0E{JD}N{WD}T{now_time}@0!0!0!0!0'
    结束标识符 = ']'
    data = 消息头起始符 + 设备号 + 分隔符 + ICCID + 分隔符 + 交易流水号 + 分隔符 + 接口标识 + 分隔符 + 报文类型 + 分隔符 + 时间 + 分隔符 + 报文长度 + 分隔符 + 报文体 + 结束标识符
    print(data)
    return data


def 报警数据(value):
    now_time = time.strftime('%Y%m%d%H%M%S', time.localtime())
    消息头起始符 = '['
    设备号 = '867082058798585'.zfill(15)
    分隔符 = ','
    ICCID = '89860000192027575850'.zfill(20)
    交易流水号 = f'{now_time}0000'
    报文类型 = '3'
    时间 = f'{now_time}'
    结束标识符 = ']'
    if value == "sos报警":
        data = 消息头起始符 + 设备号 + 分隔符 + ICCID + 分隔符 + 交易流水号 + 分隔符 + 'REPORT_SOS' + 分隔符 + 报文类型 + 分隔符 + 时间 + 分隔符 + '1' + 分隔符 + '1' + 结束标识符
    elif value == "关机报警":
        data = 消息头起始符 + 设备号 + 分隔符 + ICCID + 分隔符 + 交易流水号 + 分隔符 + 'ALARM_POWER' + 分隔符 + 报文类型 + 分隔符 + 时间 + 分隔符 + '5' + 分隔符 + '2@' + 结束标识符
    elif value == "缺电报警":
        data = 消息头起始符 + 设备号 + 分隔符 + ICCID + 分隔符 + 交易流水号 + 分隔符 + 'ALARM_POWER' + 分隔符 + 报文类型 + 分隔符 + 时间 + 分隔符 + '5' + 分隔符 + '1@10%' + 结束标识符
    elif value == "自动关机报警":
        data = 消息头起始符 + 设备号 + 分隔符 + ICCID + 分隔符 + 交易流水号 + 分隔符 + 'ALARM_POWER' + 分隔符 + 报文类型 + 分隔符 + 时间 + 分隔符 + '5' + 分隔符 + '3@5%' + 结束标识符
    elif value == "开机报警":
        data = 消息头起始符 + 设备号 + 分隔符 + ICCID + 分隔符 + 交易流水号 + 分隔符 + 'ALARM_POWER' + 分隔符 + 报文类型 + 分隔符 + 时间 + 分隔符 + '5' + 分隔符 + '4@90%' + 结束标识符
    elif value == "设备充电":
        data = 消息头起始符 + 设备号 + 分隔符 + ICCID + 分隔符 + 交易流水号 + 分隔符 + 'ALARM_POWER' + 分隔符 + 报文类型 + 分隔符 + 时间 + 分隔符 + '5' + 分隔符 + '5@' + 结束标识符
    elif value == "电源已断开":
        data = 消息头起始符 + 设备号 + 分隔符 + ICCID + 分隔符 + 交易流水号 + 分隔符 + 'ALARM_POWER' + 分隔符 + 报文类型 + 分隔符 + 时间 + 分隔符 + '5' + 分隔符 + '6@' + 结束标识符
    elif value == "设备电量已充满":
        data = 消息头起始符 + 设备号 + 分隔符 + ICCID + 分隔符 + 交易流水号 + 分隔符 + 'ALARM_POWER' + 分隔符 + 报文类型 + 分隔符 + 时间 + 分隔符 + '5' + 分隔符 + '7@100%' + 结束标识符
    print(data)
    return data


def 终端上报(value):
    WD = '21.677431'
    JD = '110.919843'
    now_time = time.strftime('%Y%m%d%H%M%S', time.localtime())
    消息头起始符 = '['
    设备号 = '867082058798585'.zfill(15)
    分隔符 = ','
    ICCID = '89860000192027575850'.zfill(20)
    交易流水号 = f'{now_time}0000'
    报文类型 = '3'
    时间 = f'{now_time}'
    结束标识符 = ']'
    手机号 = '13829622823'
    开始时间 = now_time[:12] + '00'
    结束时间 = now_time
    时长 = int(结束时间) - int(开始时间)
    血氧 = f''
    心率 = f''
    温度 = f'{float()}'
    佩戴状态 = f''
    上报状态 = f''
    if value == "设备模式上报":  # 平衡模式
        data = 消息头起始符 + 设备号 + 分隔符 + ICCID + 分隔符 + 交易流水号 + 分隔符 + 'DEVICE_STATUS' + 分隔符 + 报文类型 + 分隔符 + 时间 + 分隔符 + '20' + 分隔符 + f'{random.randint(1, 3)}@{random.randint(1, 3)}@{int(time.time() * 1000)}@20' + 结束标识符
    elif value == "设备登录":
        data = 消息头起始符 + 设备号 + 分隔符 + ICCID + 分隔符 + 交易流水号 + 分隔符 + 'DEVICE_LOGIN' + 分隔符 + 报文类型 + 分隔符 + 时间 + 分隔符 + '22' + 分隔符 + f'5@1@111@1@1@100@0' + 结束标识符
    elif value == "健康参数上报":
        data = 消息头起始符 + 设备号 + 分隔符 + ICCID + 分隔符 + 交易流水号 + 分隔符 + 'REPORT_HEALTH' + 分隔符 + 报文类型 + 分隔符 + 时间 + 分隔符 + '36' + 分隔符 + f'0000-0000@000!000!000!000!@{random.randint(35, 38)}@0000' + 结束标识符
    elif value == "通话记录上报":
        data = 消息头起始符 + 设备号 + 分隔符 + ICCID + 分隔符 + 交易流水号 + 分隔符 + 'REPORT_CALL_LOG' + 分隔符 + 报文类型 + 分隔符 + 时间 + 分隔符 + '26' + 分隔符 + f'{手机号}@{开始时间}!{结束时间}@{时长}@{random.randint(0, 1)}' + 结束标识符
    elif value == "获取天气信息":
        data = 消息头起始符 + 设备号 + 分隔符 + ICCID + 分隔符 + 交易流水号 + 分隔符 + 'GET_WEATHER_INFO' + 分隔符 + 报文类型 + 分隔符 + 时间 + 分隔符 + '106' + 分隔符 + f'0E{JD}N{WD}T{now_time}@460!0!9231!2351@0!0!0!0!0!0!0!0!0!0!0!0!0!' + 结束标识符
    elif value == "健康心率血氧参数上报":
        if 佩戴状态 == "未佩戴":
            pdai = 0
        elif 佩戴状态 == "已佩戴":
            pdai = 1
        if 上报状态 == "定时上报":
            sb = 0
        elif 上报状态 == "主动上报":
            sb = 1
        data = 消息头起始符 + 设备号 + 分隔符 + ICCID + 分隔符 + 交易流水号 + 分隔符 + 'REPORT_HEART_HEALTH' + 分隔符 + 报文类型 + 分隔符 + 时间 + 分隔符 + '36' + 分隔符 + f'{血氧}@{心率}@{温度}@{pdai}@{sb}' + 结束标识符

    print(data)
    return data


def 心跳数据():
    now_time = time.strftime('%Y%m%d%H%M%S', time.localtime())
    消息头起始符 = '['
    设备号 = f'{self.imei_Text11.get()}'.zfill(15)
    分隔符 = ','
    ICCID = f'{self.iccid_Text11.get()}'.zfill(20)
    交易流水号 = f'{now_time}0000'
    报文类型 = '3'
    时间 = f'{now_time}'
    结束标识符 = ']'
    开始时间 = now_time[:12] + '00'
    结束时间 = now_time
    data = 消息头起始符 + 设备号 + 分隔符 + ICCID + 分隔符 + 交易流水号 + 分隔符 + 'REPORT_HEARTBEAT' + 分隔符 + 报文类型 + 分隔符 + 时间 + 分隔符 + '5' + 分隔符 + f'{random.randint(80, 100)}%@{random.randint(100, 2000)}' + 结束标识符
    print(data)


# str1 = f"{data}"
# str1 = "[867082058798193,89860000192027575560,202408221639450000,REPORT_HEARTBEAT3,20240822163945,5,97%@0]"
# 设备模式自动回复
# str1 = "[000001111122222,89860484012080099999,202110186666666666,DEVICE_STATUS,2,20211025100120,1,0]"

# 设备模式上报
# str1 = "[147258369147257,89860484012080099999,202110186666666666,DEVICE_STATUS,3,20211025100120,1,1@3@1634125515502@25]"
# 0 = 待机模式 1 = 省电模式 2 = 平衡模式 3 = 实时模式

# # 上传步数心跳请求
# str1 = "[489494984163156,89860484012080099999,202110186666666666,REPORT_HEARTBEAT,3,20211025100120,3,100%@7080]"


# centerLat=39.97664735218192, centerLon=116.39291340297486,
# 体温
# str1 = "[123165497898755,89860484012080099999,202110186666666666,REPORT_HEALTH,3,20211025100120,36,0900-1000@000!000!000!000!@38.5@0000]"
# 上线
# str1 = "[867413828698541,89860484012080099999,202110186666666666,REPORT_LOCATION_INFO,3,20220628120320,106,0E121.411783N31.178125T20080121165030@460!0!9231!2351@wifi!AC:BC:32:78:A2:5F!-97#wifi1!AC:BC:32:78:A2:5F!-97#wifi1!AC:BC:32:78:A2:5F!-97#wifi1!AC:BC:32:78:A2:5F!-97#wifi1!AC:BC:32:78:A2:5F!-97#wifi1!AC:BC:32:78:A2:5F!-97#wifi1!AC:BC:32:78:A2:5F!-97#wifi1!AC:BC:32:78: A2:5F!-97#wifi1!AC:BC:32:78:A2:5F!-97#wifi1!AC:BC:32:78:A2:5F!-97#wifi1!AC:BC:32:78:A2:5F!-97#wifi1!AC:BC:32:78:A2:5F!-97]"
# sos报警
# str1 = "[489494984163156,89860484012080099999,202110186666666666,REPORT_SOS,3,20211025100120,1,1]"
# 出入围栏
# str1 = "[231521512516521,89860484012080099999,202110186666666666,REPORT_LOCATION_INFO,3,20211025100120,79,0E116.39291340297486N39.97664735218192T20211025100120@0@0]"
# str1 = "[789789789456456,89860484012080099999,202110186666666666,REPORT_LOCATION_INFO,3,20211025100120,79,0E110.48500728459983N37.99338605032084T20211025100120@0@0]"
# 缺电
# str1 = "[123165497898755,89860484012080099999,202110186666666666,ALARM_POWER,3,20211025100120,5,1@19%]"
# #关机
# str1 = "[489494984163156,89860484012080099999,202110186666666666,ALARM_POWER,3,20211025100120,2,2@8%]"

# 自动关机
# str1 = "[231521512516521,89860484012080099999,202110186666666666,ALARM_POWER,3,20211025100120,4,3@15%]"
# 开机
# str1 = "[867413828698541,89860484012080099999,202110186666666666,ALARM_POWER,3,20211025100120,2,4@32%]"
# 电量已充满
# str1 = "[123789123789123,89860484012080099999,202110186666666666,ALARM_POWER,3,20211025100120,6,7@100%]"


# time1 = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
# str2 = str1.replace('20220628120320', str(time1))
# print(str2)
# str1 = "[123456789012345,89860484012080099999,202408231238520000,REPORT_LOCATION_INFO,3,20240823123852,79,0E114.106906N22.468459T20240823123852@0!0!0!0!0]"
# tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# server_addr = ('81.71.67.36', int(7999))
# try:
#     tcp_socket.connect(server_addr)
#     print('成功')
#
#     res = AES_CBC_encrypt(str1, key, iv)
#     print("加密数据:%s" % res)
#     res1 = str(res, 'utf-8') + "#kdsjafjalsdjg#170"
#     tcp_socket.send(res1.encode())
#     print("发送消息:%s" % str(res1))
#     try:
#         recv_msg = tcp_socket.recv(1024).decode("utf8")
#     except:
#         print("连接超时，请重新连接")
#     print("接收到的信息为:%s" % str(recv_msg))
# except:
#     print('失败')
血氧 = f'{self.xue_data_Text11.get()}'
心率 = f'{self.xinlv_data_Text11.get()}'
温度1 = f'{float(self.wendu1_data_Text11.get())}'
佩戴状态 = f'{self.pdai_data_Text11.get()}'
上报状态 = f'{self.sb_data_Text11.get()}'

self.xue_data_label11 = Label(pane11, text="血氧")
items = ("98", "80")
self.xue_data_Text11 = Combobox(pane11, width=22, height=20, values=items)
self.xue_data_Text11.current(0)

self.xinlv_data_label11 = Label(pane11, text="心率")
items = ("120", "130")
self.xinlv_data_Text11 = Combobox(pane11, width=22, height=2, values=items)
self.xinlv_data_Text11.current(0)

self.wendu1_data_label11 = Label(pane11, text="温度")
items = ("36.2", "37", "38", "39.4")
self.wendu1_data_Text11 = Combobox(pane11, width=50, height=12, values=items)
self.wendu1_data_Text11.current(0)

self.pdai_data_label11 = Label(pane11, text="佩戴状态")
items = ("未佩戴", "已佩戴")
self.pdai_data_Text11 = Combobox(pane11, width=22, height=20, values=items)
self.pdai_data_Text11.current(0)

self.sb_data_label11 = Label(pane11, text="上报状态")
items = ("定时上报", "主动上报")
self.sb_data_Text11 = Combobox(pane11, width=22, height=2, values=items)
self.sb_data_Text11.current(0)

self.xue_data_label11.grid_remove()
self.xue_data_Text11.grid_remove()
self.xinlv_data_label11.grid_remove()
self.xinlv_data_Text11.grid_remove()
self.wendu1_data_label11.grid_remove()
self.wendu1_data_Text11.grid_remove()
self.pdai_data_label11.grid_remove()
self.pdai_data_Text11.grid_remove()
self.sb_data_label11.grid_remove()
self.sb_data_Text11.grid_remove()
