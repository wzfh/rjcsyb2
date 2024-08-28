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
    elif value == "获取学生信息(FA67专用)":
        data = 消息头起始符 + 设备号 + 分隔符 + ICCID + 分隔符 + 交易流水号 + 分隔符 + 'GET_STUDENT_STATUS' + 分隔符 + 报文类型 + 分隔符 + 时间 + 分隔符 + '1' + 分隔符 + f'1' + 结束标识符

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
first_name = ['张', '王', '李', '赵', '刘', '陈', '杨', '黄', '周', '吴', '徐', '孙', '胡', '朱', '高', '林',
              '何', '郭', '马', '罗',
              '梁', '宋', '郑', '谢', '韩', '唐', '冯', '于', '董', '萧', '程', '曹', '袁', '邓', '许', '傅',
              '沈', '曾', '彭', '吕',
              '苏', '卢', '蔡', '余', '丁', '蒋', '魏', '薛', '叶', '阎', '余', '潘', '杜', '戴', '夏', '钟',
              '汪', '田', '任', '姜',
              '范', '方', '石', '姚', '谭', '廖', '邹', '熊', '金', '陆', '郝', '孔', '白', '崔', '康', '毛',
              '邱', '秦', '江', '史',
              '顾', '侯', '龚', '邵', '孟', '龙', '段', '雷', '钱', '汤', '尹', '黎', '易', '常', '武', '乔',
              '贺', '赖', '庞', '樊']
second_name = ["伟第一中学", "华第一中学", "建国第一中学", "洋第一中学", "刚第一中学", "万里第一中学",
               "爱民第一中学", "牧第一中学", "陆第一中学",
               "路第一中学", "昕第一中学", "鑫第一中学", "兵第一中学", "硕第一中学", "志宏第一中学",
               "峰第一中学", "磊第一中学", "雷第一中学", "文第一中学", "明浩第一中学", "光第一中学",
               "超第一中学", "军第一中学", "达第一中学"]
name = random.choice(first_name) + random.choice(second_name)


def 组织(value):
    import requests
    for i in range(value):
        url = "https://www.tfzhijiao.com:6443/v1/api/org/addMore"
        payload = {
            "isLockSim": 0,
            "orgId": None,
            "orgName": f"{name}",
            "orgPid": 402,
            "province": "110000",
            "city": "110100",
            "district": "110116",
            "sortNum": None,
            "remark": "",
            "roleType": 1,
            "roleId": 1,
            "loginName": f"{name}",
            "isCreateSchool": 0,
            "school": {
                "num": 10,
                "schoolName": "",
                "schoolType": 1,
                "educationStage": 1,
                "roleId": 3
            }
        }
        headers = {
            "sessionId": "40340264171842ca8a92f336f853f3fa",
            "Content-Type": "application/json",
            "from": "PC",
            "Accept": "*/*",
            "Accept-Encoding": "gzip, deflate, br",
            "User-Agent": "PostmanRuntime-ApipostRuntime/1.1.0",
            "Connection": "keep-alive"
        }

        response = requests.request("POST", url, json=payload, headers=headers)

        print(response.text)


def 学校(value):
    for i in range(value):
        import requests
        url = "https://www.tfzhijiao.com:6443/v1/api/school/addMore"
        payload = {
            "num": 10,
            "schoolName": f"{name}",
            "schoolType": 1,
            "headName": None,
            "orgId": 402,
            "headPhone": None,
            "provinces": "110000",
            "schoolAddress": f"{name}",
            "city": "110100",
            "county": "110116",
            "educationStage": 3,
            "remark": "",
            "roleId": 3,
            "loginName": f"{name}",
            "extendId": "",
            "lngLat": []
        }
        headers = {
            "sessionId": "40340264171842ca8a92f336f853f3fa",
            "Content-Type": "application/json",
            "from": "PC",
            "Accept": "*/*",
            "Accept-Encoding": "gzip, deflate, br",
            "User-Agent": "PostmanRuntime-ApipostRuntime/1.1.0",
            "Connection": "keep-alive"
        }

        response = requests.request("POST", url, json=payload, headers=headers)

        print(response.text)


def 设备(value):
    for i in range(value):
        import requests

        url = "https://www.tfzhijiao.com:6443/v1/api/card/add"
        '000089799874470'
        payload = {
            "imei": f"8979987447" + f"{i}".zfill(5),
            "finger": "",
            "rfid": "",
            "deviceType": "SC01",
            "orgId": 402,
            "cardId": None,
            "bindingPhone": None
        }
        headers = {
            "sessionId": "40340264171842ca8a92f336f853f3fa",
            "Content-Type": "application/json",
            "from": "PC",
            "Accept": "*/*",
            "Accept-Encoding": "gzip, deflate, br",
            "User-Agent": "PostmanRuntime-ApipostRuntime/1.1.0",
            "Connection": "keep-alive"
        }

        response = requests.request("POST", url, json=payload, headers=headers)

        print(response.text)


def 学生(value):
    for i in range(value):
        import requests

        url = "https://www.tfzhijiao.com:6443/v1/api/student/add"
        first_name = ['张', '王', '李', '赵', '刘', '陈', '杨', '黄', '周', '吴', '徐', '孙', '胡', '朱', '高', '林',
                      '何', '郭', '马', '罗',
                      '梁', '宋', '郑', '谢', '韩', '唐', '冯', '于', '董', '萧', '程', '曹', '袁', '邓', '许', '傅',
                      '沈', '曾', '彭', '吕',
                      '苏', '卢', '蔡', '余', '丁', '蒋', '魏', '薛', '叶', '阎', '余', '潘', '杜', '戴', '夏', '钟',
                      '汪', '田', '任', '姜',
                      '范', '方', '石', '姚', '谭', '廖', '邹', '熊', '金', '陆', '郝', '孔', '白', '崔', '康', '毛',
                      '邱', '秦', '江', '史',
                      '顾', '侯', '龚', '邵', '孟', '龙', '段', '雷', '钱', '汤', '尹', '黎', '易', '常', '武', '乔',
                      '贺', '赖', '庞', '樊']
        second_name = ["伟", "华", "建国", "洋", "刚", "万里", "爱民", "牧", "陆", "路", "昕", "鑫", "兵", "硕", "志宏",
                       "峰", "磊", "雷", "文", "明浩", "光", "超", "军", "达"]
        name = random.choice(first_name) + random.choice(second_name)
        payload = {
            "studentName": f"{name}",
            "finger": "",
            "sex": 1,
            "schoolId": 1402,
            "gradeId": 10,
            "classId": 16202,
            "deviceType": 1,
            "imei": "",
            "rfid": None,
            "studentNo": None,
            "phone": None,
            "devSn": "",
            "idCard": ""
        }
        headers = {
            "sessionId": "40340264171842ca8a92f336f853f3fa",
            "Content-Type": "application/json",
            "from": "PC",
            "Accept": "*/*",
            "Accept-Encoding": "gzip, deflate, br",
            "User-Agent": "PostmanRuntime-ApipostRuntime/1.1.0",
            "Connection": "keep-alive"
        }

        response = requests.request("POST", url, json=payload, headers=headers)

        print(response.text)


if __name__ == '__main__':
    # 组织数量200个，学校数量500个，班级数量1000个，学生证数量30000个，学生30000个；
    # 组织(2)
    # 学校(1)
    import os


    def get_filenames_without_extension(directory):
        # 获取目录下的所有文件和文件夹
        items = os.listdir(directory)
        # 存储不带扩展名的文件名
        filenames_without_extension = []

        for item in items:
            # 分离文件名和扩展名
            file_name, file_extension = os.path.splitext(item)
            # 将不带扩展名的文件名添加到列表中
            filenames_without_extension.append(file_name)

        return filenames_without_extension


    # 调用函数，传入目录路径
    directory = r"C:\Users\rjcsyb2\Desktop\开发库迁移\开发库迁移"
    result = get_filenames_without_extension(directory)
    print(result)
