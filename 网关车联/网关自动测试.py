import math
import os.path
import random
import re
import time
from socket import *
import base64
import requests
import ast
import ddddocr
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


import re


def is_valid_ip(ip):
    ipv4_pattern = re.compile(r'^(\d{1,3}\.){3}\d{1,3}$')
    if ipv4_pattern.match(ip):
        return all(0 <= int(num) < 256 for num in ip.split('.'))
    return False


def is_valid_domain(domain):
    domain_pattern = re.compile(
        r'^(?:[a-zA-Z0-9]'
        r'(?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?\.)+'
        r'[a-zA-Z]{2,6}$'
    )
    return domain_pattern.match(domain) is not None


def check_input(input_str):
    if is_valid_ip(input_str):
        return "IP Address"
    elif is_valid_domain(input_str):
        return "Domain Name"
    else:
        return "Invalid input"


import subprocess


def get_ip(domain):
    result = subprocess.run(['ping', '-c', '1', domain], stdout=subprocess.PIPE)
    output = result.stdout.decode('GBK')
    ip_address = output.split(' ')[7].strip('[]:')
    print(ip_address)
    return ip_address


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
        self.groupId = "550452"
        self.user = "YA123"
        self.password = "+B7I4Uv2HRZomxWqAbEMaw=="

    def login1(self):
        global sessionId
        url = "https://v4.car900.com:9998/oauth/getCode"
        payload = ""
        headers = {"User-Agent": "Apipost/8 (https://www.apipost.cn)"}
        response = requests.request("GET", url, data=payload, headers=headers)
        user_dict = ast.literal_eval(response.text)
        img_str = f"{user_dict['obj']['code'][22:]}"
        bytes_img = base64.b64decode(img_str)
        with open('../yzm.png', mode='wb') as f:
            f.write(bytes_img)
        ocr = ddddocr.DdddOcr(beta=True)
        with open('../yzm.png', mode='rb') as f:
            image = f.read()
        result2 = ocr.classification(image)
        uuid = user_dict['obj']['uuid']
        print('图形验证码:\t' + result2)  # 图形验证码
        print('uuid:\t\t' + user_dict['obj']['uuid'])
        url = "https://v4.car900.com:9998/oauth/v4/token"

        payload = "-----011000010111000001101001\r\n" \
                  "Content-Disposition: form-data; name=\"username\"\r\n\r\n" \
                  f"{self.user}\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"scope\"\r\n\r\n" \
                  "carWeb4\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"tenantId\"\r\n\r\n1\r\n" \
                  "-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"password\"\r\n\r\n" \
                  f"{self.password}\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"code\"\r\n\r\n" \
                  f"{result2}\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"uuid\"\r\n\r\n" \
                  f"{uuid}\r\n-----011000010111000001101001--\r\n\r\n"
        headers = {
            "Content-Type": "multipart/form-data; boundary=---011000010111000001101001",
            "sessionId": "13243",
            "Origin": "https://v4.car900.com",
            "Accept": "*/*",
            "Accept-Encoding": "gzip, deflate, br",
            "User-Agent": "PostmanRuntime-ApipostRuntime/1.1.0",
            "Connection": "keep-alive",
            "Cookie": "satoken=5e43775c-bfe6-455d-b257-a063d95ac8e9"
        }

        response = requests.request("POST", url, data=payload, headers=headers)
        user_dict1 = ast.literal_eval(response.text)
        sessionId = user_dict1['obj']['sessionId']
        print('sessionId:\t' + sessionId)
        return sessionId

    def baojpd(self, 报警):
        if 报警 == '00000080':
            bj = 'lowVoltage'  # 电源欠压
            return bj
        elif 报警 == '00000100':
            bj = 'powerDown'  # 电源掉电
            return bj
        elif 报警 == '':
            bj = 'isIllegalRemove'  # 非法拆除
            return bj
        elif 报警 == '00000002':
            bj = 'overSpeed'  # 超速报警
            return bj
        elif 报警 == '':
            bj = 'shockAlarm'  # 震动报警
            return bj
        elif 报警 == '02000000':
            bj = 'illegalMove'  # 位移报警
            return bj
        elif 报警 == '00000001':
            bj = 'emergencyAlarm'  # 紧急报警
            return bj
        elif 报警 == '20000000':
            bj = 'collideAlarm'  # 碰撞报警
            return bj
        elif 报警 == '':
            bj = 'lightAlarm'  # 光感报警
            return bj
        elif 报警 == '01000000':
            bj = 'illegalStart'  # 非法点火报警
            return bj
        elif 报警 == '40000000':
            bj = 'rolloverAlarm'  # 侧翻报警
            return bj
        elif 报警 == '00000040':
            bj = 'GPSAntennaState'  # GPS天线开路
            return bj
        elif 报警 == '':
            bj = 'accelerateAlarm'  # 急加速报警
            return bj
        elif 报警 == '':
            bj = 'slowDownAlarm'  # 急减速报警
            return bj
        elif 报警 == '':
            bj = 'swerveAlarm'  # 急转弯报警
            return bj
        elif 报警 == '':
            bj = 'pseudoLbs'  # 伪基站报警
            return bj
        elif 报警 == '':
            bj = 'audioAlarm'  # 声控报警
            return bj
        elif 报警 == '':
            bj = 'weakSignalAlarm'  # 信号弱报警
            return bj
        elif 报警 == '':
            bj = 'abnormalMoveRemove'  # 车辆异常轮动
            return bj
        elif 报警 == '':
            bj = 'pryingAlarm'  # 撬锁报警
            return bj
        elif 报警 == '':
            bj = 'scissorsAlarm'  # 剪锁报警
            return bj
        elif 报警 == '':
            bj = 'lowerPowerAlarm'  # 低压报警
            return bj
        elif 报警 == '':
            bj = 'cardRemovalAlarm'  # TF卡拔出报警
            return bj
        elif 报警 == '':
            bj = 'cardErrorAlarm'  # TF卡异常报警
            return bj
        else:
            return None

    def 车辆id(self):
        import requests

        url = "https://v4.car900.com:9998/car/v4/api/assets/list.json"

        querystring = {"keyword": f"{self.sbei}", "groupId": f"{self.groupId}", "state": "0", "childFlag": "1",
                       "pageNumber": "1",
                       "pageSize": "10"}
        payload = ""
        headers = {
            "sessionid": f"5e43775c-bfe6-455d-b257-a063d95ac8e9",
            "Accept": "*/*",
            "Accept-Encoding": "gzip, deflate, br",
            "User-Agent": "PostmanRuntime-ApipostRuntime/1.1.0",
            "Connection": "keep-alive",
            "Cookie": "satoken=5e43775c-bfe6-455d-b257-a063d95ac8e9"
        }

        response = requests.request("GET", url, data=payload, headers=headers, params=querystring)
        vehicleId = response.json()['obj']['data'][0]['vehicleId']
        print(f"\nvehicleId:{response.json()['obj']['data'][0]['vehicleId']}")
        return vehicleId

    def alam(self):
        import requests
        url = "https://v4.car900.com:9998/car/v1/accelerate/report/alarm/alarmAnalysis.json"
        querystring = {"chooseId": f"{self.车辆id()}", "groupId": f"{self.groupId}", "flag": "1",
                       "startTime": "2024-12-16 00:00:00", "endTime": "2024-12-16 23:59:59",
                       "longStay": "0", "alarmTypes": "emergencyAlarm", "pageNumber": "1", "pageSize": "10"}

        payload = ""
        headers = {
            "sessionid": "5e43775c-bfe6-455d-b257-a063d95ac8e9",
            "Accept": "*/*",
            "Accept-Encoding": "gzip, deflate, br",
            "User-Agent": "PostmanRuntime-ApipostRuntime/1.1.0",
            "Connection": "keep-alive",
            "Cookie": "satoken=5e43775c-bfe6-455d-b257-a063d95ac8e9"
        }

        response = requests.request("GET", url, data=payload, headers=headers, params=querystring)
        user_dict = ast.literal_eval(response.text)
        data = user_dict['obj']['data']

        def extract_values(string):
            enAlarmType = re.compile(r"'enAlarmType':\s*'([^']+)'")
            num = re.compile(r"'num':\s*(\d+)")
            startTime = re.compile(r"'startTime':\s*'([^']+)'")
            type = re.compile(r"'type':\s*'([^']+)'")
            match_enAlarmType = enAlarmType.search(string)
            match_num = num.search(string)
            match_startTime = startTime.search(string)
            match_type = type.search(string)
            if match_enAlarmType and match_num and match_startTime and match_type:
                return '报警字段：{}'.format(match_enAlarmType.group(1)), '报警次数：{}'.format(
                    match_num.group(1)), '报警时间：{}'.format(match_startTime.group(1)), '报警类型：{}'.format(
                    match_type.group(1)),
            return None

        results = []
        for item in data:
            result = extract_values(str(item))
            if result:
                results.append(result)
        for i in results:
            print(i)
        # if response.json()['msg'] == '成功':
        #     print(response.json()['obj']['data'][0])
        # else:
        #     print('321')

    def get(self):
        count = 0

        now_time = time.strftime('%Y%m%d%H%M%S', time.localtime())
        wd1 = '23.012173'
        wd2 = float(wd1) * 1000000
        wd3 = hex(int(wd2))
        jd1 = '114.340462'
        jd2 = float(jd1) * 1000000
        jd3 = hex(int(jd2))
        标识位 = '7E'
        消息ID = '0200'
        油耗消息体属性 = '002F'
        设备号 = "0" + f"{self.sbei}"
        print(f"设备号:{设备号}")

        流水号 = f'{1}'.zfill(4)
        baojlxs = [
            self.baojing['紧急报警'],
            # self.baojing['超速报警'], self.baojing['疲劳驾驶'],
            # self.baojing['LED顶灯故障'],
            # self.baojing['进出区域路线报警'],
            # self.baojing['路段行驶时间不足'], self.baojing['禁行路段行驶'],
            # self.baojing['车辆非法点火'],
            # self.baojing['车辆非法位移'],
            # self.baojing['所有清零报警'],
            # self.baojing['正常'],   self.baojing['危险预警'], self.baojing['模块故障'],
            # self.baojing['模块开路'],
            # self.baojing['侧翻报警'],
            # self.baojing['碰撞报警'],
            # self.baojing['终端欠压'], self.baojing['终端掉电'],
            # self.baojing['终端LCD故障'],
            # self.baojing['TTS故障'],
            # self.baojing['摄像头故障'], self.baojing['当天累计驾驶时长'],
            # self.baojing['超时停车']
        ]
        报警 = random.choice(baojlxs)
        状态 = self.ztai['ACC开定位开北斗GPS满载']
        纬度 = wd3[2:].zfill(8).upper()
        经度 = jd3[2:].zfill(8).upper()
        print(f'纬度:{纬度}' + ' ' + f'经度：{经度}')
        高程 = '0001'
        速度 = f'000A'
        方向 = '000C'
        时间 = now_time[2:]
        附加里程 = f'0104000000{random.randint(10, 25)}'
        油量 = ['5208', '044C', '04B0']
        附加油量 = f'0202{random.choice(油量)}'
        附加信息ID = '250400000000300103'
        w = 消息ID + 油耗消息体属性 + 设备号 + 流水号 + 报警 + 状态 + 纬度 + 经度 + 高程 + 速度 + 方向 + 时间 + 附加里程 + 附加油量 + 附加信息ID
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
        try:
            s = socket(AF_INET, SOCK_STREAM)
            ip = '47.107.222.141'
            if check_input(ip) == "Domain Name":
                s.connect((f'{get_ip(ip)}', int(7788)))  # 测试
            else:
                s.connect((ip, int(7788)))  # 测试
            s.send(bytes().fromhex(t))
            send = s.recv(1024).hex()
            print('服务器应答：' + send.upper())
            print('\n' * 1)
            countdown(3)
            if self.baojpd(报警) == None:
                print('\n平台没有对应的报警类型')
            else:
                self.alam(报警)
        except ConnectionRefusedError:
            print('提示连接被拒绝')
        except TimeoutError:
            print('提示连接超时')
        except Exception as e:
            print('提示' + e)


def countdown(t):
    for i in range(t):
        print("\r休眠倒计时：%d" % (t - i) + '秒', end='')
        time.sleep(1)


if __name__ == '__main__':
    ll = login()
    # ll.get()
    ll.alam()
