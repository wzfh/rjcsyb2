from tkinter import BooleanVar, messagebox
from socket import *
import time, re, requests, ast, base64, ddddocr, os, datetime, threading, math, keyboard, random, psutil, customtkinter, \
    sys, fnmatch, csv
from configobj import ConfigObj
from PIL import Image
from tkinter.colorchooser import askcolor
from tkinter import filedialog
import smtplib, imaplib, email
from email.mime.text import MIMEText
from email.header import decode_header
from datetime import datetime, timedelta

stop_threads = False
sender_email = '1114377437@qq.com'
receiver_email = '1114377437@qq.com'
password = 'usnxlmvexcboiagh'


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


class TipBox:
    def __init__(self, widget, text='默认信息', bg='#fafdc2'):
        self.widget = widget
        self.text = text
        self.bg = bg
        self.tipwindow = None
        self.x = self.y = 0

        # 绑定鼠标进入和离开事件
        self.widget.bind("<Enter>", self.enter)
        self.widget.bind("<Leave>", self.leave)
        self.widget.bind("<Motion>", self.update_position)

    def enter(self, e=None):
        # 创建提示窗口
        x = self.widget.winfo_rootx() + self.widget.winfo_width() // 2
        y = self.widget.winfo_rooty() + self.widget.winfo_height()
        self.tipwindow = customtkinter.CTkToplevel(self.widget)
        self.tipwindow.wm_overrideredirect(True)  # 去边框
        self.tipwindow.wm_attributes("-topmost", 1)  # 置顶
        self.tipwindow.wm_geometry("+%d+%d" % (x, y))

        label = customtkinter.CTkLabel(self.tipwindow, text=self.text, bg_color=self.bg)
        label.grid(ipadx=1)

    def leave(self, e=None):
        # 销毁提示窗口
        if self.tipwindow:
            self.tipwindow.destroy()

    def update_position(self, e=None):
        if self.tipwindow:
            # 更新提示窗口的位置，使其跟随鼠标
            x = e.x_root + 20
            y = e.y_root + 20
            # 更新窗口位置
            try:
                self.tipwindow.geometry("+%d+%d" % (x, y))
            except TclError as e:
                pass


class App(customtkinter.CTk):

    def login1(self):
        proxyMeta = f"{self.prox}"
        proxysdata = {
            'http': proxyMeta,
            'https': proxyMeta
        }
        url = "https://v4.car900.com:9998/oauth/getCode"
        payload = ""
        headers = {"User-Agent": "Apipost/8 (https://www.apipost.cn)"}
        response = requests.request("GET", url, data=payload, proxies=proxysdata, headers=headers)
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
                  f"{self.user账号()}\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"scope\"\r\n\r\n" \
                  "carWeb4\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"tenantId\"\r\n\r\n1\r\n" \
                  "-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"password\"\r\n\r\n" \
                  f"{self.pwd密码()}\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"code\"\r\n\r\n" \
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

        response = requests.request("POST", url, data=payload, proxies=proxysdata, headers=headers)
        user_dict1 = ast.literal_eval(response.text)
        sessionId = user_dict1['obj']['sessionId']
        print('sessionId:\t' + sessionId)
        return sessionId

    def baojpd(self, 报警):
        if 报警 == '00000080':
            bj = 'lowVoltage'  # 电源欠压  有了
            return bj
        elif 报警 == '00000100':
            bj = 'powerDown'  # 电源掉电  有了
            return bj
        elif 报警 == '5':
            bj = 'isIllegalRemove'  # 非法拆除报警
            return bj
        elif 报警 == '00000002':
            bj = 'overSpeed'  # 超速报警  有了
            return bj
        elif 报警 == '10000000':
            bj = 'illegalMove'  # 位移报警  有了
            return bj
        elif 报警 == '00000001':
            bj = 'emergencyAlarm'  # 紧急报警  有了
            return bj
        elif 报警 == '1':
            bj = 'collideAlarm,shockAlarm'  # 碰撞报警和震动报警
            return bj
        elif 报警 == "":
            bj = 'rolloverAlarm'  # 侧翻报警
            return bj
        elif 报警 == '':
            bj = 'lightAlarm'  # 光感报警
            return bj
        elif 报警 == '':
            bj = 'illegalStart'  # 非法点火报警
            return bj
        elif 报警 == '':
            bj = 'GPSAntennaState'  # GPS天线开路
            return bj
        elif 报警 == '4':
            bj = 'accelerateAlarm'  # 急加速报警
            return bj
        elif 报警 == '2':
            bj = 'slowDownAlarm'  # 急减速报警
            return bj
        elif 报警 == '3':
            bj = 'swerveAlarm'  # 急转弯报警
            return bj
        elif 报警 == '':
            bj = 'pseudoLbs'  # 伪基站报警
            return bj
        elif 报警 == '6':
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
        elif 报警 == '7':
            bj = 'cardRemovalAlarm'  # TF卡拔出报警
            return bj
        elif 报警 == '8':
            bj = 'cardErrorAlarm'  # TF卡异常报警
            return bj
        elif 报警 == '9':
            bj = 'lowVoltage,powerDown,overSpeed,illegalMove,emergencyAlarm,isIllegalRemove,collideAlarm,shockAlarm,accelerateAlarm,slowDownAlarm,swerveAlarm,audioAlarm,cardRemovalAlarm,cardErrorAlarm'  # TF卡异常报警
            return bj
        else:
            return None

    def 车辆id(self):
        import requests
        proxyMeta = f"{self.prox}"
        proxysdata = {
            'http': proxyMeta,
            'https': proxyMeta
        }
        url = "https://v4.car900.com:9998/car/v4/api/assets/list.json"

        querystring = {"keyword": f"{int(self.sb_hao())}", "groupId": f"{int(self.groupId组织())}", "state": "0",
                       "childFlag": "1",
                       "pageNumber": "1",
                       "pageSize": "10"}
        print(querystring)
        payload = ""
        headers = {
            "sessionid": f"{self.sessionId}",
            "Accept": "*/*",
            "origin": "https://v4.car900.com",
            "Accept-Encoding": "gzip, deflate, br",
            "User-Agent": "PostmanRuntime-ApipostRuntime/1.1.0",
            "Connection": "keep-alive",
            "Cookie": "satoken=5e43775c-bfe6-455d-b257-a063d95ac8e9"
        }

        response = requests.request("GET", url, data=payload, headers=headers, proxies=proxysdata, params=querystring)
        print(response.json())
        vehicleId = response.json()['obj']['data'][0]['vehicleId']
        print(f"\nvehicleId:{response.json()['obj']['data'][0]['vehicleId']}")
        return vehicleId

    def alam(self, 报警):
        # 统计
        # url = "https://v4.car900.com:9998/car/v1/accelerate/report/alarm/alarmAnalysis.json"
        # now_time1 = time.strftime('%Y-%m-%d', time.localtime())
        # alams = self.baojpd(报警)
        # print(alams)
        # querystring = {"chooseId": f"{self.车辆id()}", "groupId": f"{self.groupId}", "flag": "1",
        #                "startTime": f"{now_time1} 00:00:00", "endTime": f"{now_time1} 23:59:59",
        #                "longStay": "0", "alarmTypes": f"{alams}", "pageNumber": "1", "pageSize": "10"}
        #
        # payload = ""
        # headers = {
        #     "sessionid": f"{self.sessionId}",
        #     "Accept": "*/*",
        #     "Accept-Encoding": "gzip, deflate, br",
        #     "User-Agent": "PostmanRuntime-ApipostRuntime/1.1.0",
        #     "Connection": "keep-alive",
        #     "Cookie": "satoken=5e43775c-bfe6-455d-b257-a063d95ac8e9"
        # }
        #
        # response = requests.request("GET", url, data=payload, headers=headers, params=querystring)
        # 明细
        proxyMeta = f"{self.prox}"
        proxysdata = {
            'http': proxyMeta,
            'https': proxyMeta
        }
        url = "https://v4.car900.com:9998/car/v1/accelerate/report/alarm/alarmDetail.json"
        now_time1 = time.strftime('%Y-%m-%d', time.localtime())
        alams = self.baojpd(报警)
        print(alams)
        payload = "-----011000010111000001101001\r\n" \
                  "Content-Disposition: form-data; name=\"" \
                  f"vehicleId\"\r\n\r\n{self.车辆id()}\r\n" \
                  "-----011000010111000001101001\r\n" \
                  "Content-Disposition: form-data; name=\"" \
                  f"startTime\"\r\n\r\n{now_time1} 00:00:00\r\n" \
                  "-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"" \
                  f"endTime\"\r\n\r\n{now_time1} 23:59:59\r\n-----011000010111000001101001\r\n" \
                  "Content-Disposition: form-data; name=\"pageNumber\"\r\n\r\n1\r\n" \
                  "-----011000010111000001101001\r\n" \
                  f"Content-Disposition: form-data; name=\"enType\"\r\n\r\n{alams}\r\n" \
                  "-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"pageSize\"\r\n\r\n30\r\n" \
                  "-----011000010111000001101001--\r\n\r\n"
        headers = {
            "Content-Type": "multipart/form-data; boundary=---011000010111000001101001",
            "sessionId": f"{self.sessionId}",
            "Accept": "*/*",
            "Accept-Encoding": "gzip, deflate, br",
            "User-Agent": "PostmanRuntime-ApipostRuntime/1.1.0",
            "Connection": "keep-alive",
            "Cookie": "satoken=5e43775c-bfe6-455d-b257-a063d95ac8e9"
        }

        response = requests.request("GET", url, data=payload, proxies=proxysdata, headers=headers)
        user_dict = ast.literal_eval(response.text)
        data = user_dict['obj']['data']
        if data == []:
            self.textbox.insert(1.0,
                                '暂无查询到报警信息\n\n没触发的原因：\n1，触发设备当天之前已经触发但未结束报警\n2，没发送报警数据（没打开服务器按钮）\n\n解决方案：打开服务器按钮，点击报警发送正常数据，结束报警再去触发即可')
        print(data)
        res = []
        res.append(self.Trackjko())
        print(res[0][-1])

        def extract_values(string):
            startTime = re.compile("'timeBegin':\\s*'([^']+)'")
            type = re.compile("'type':\\s*'([^']+)'")
            speed = re.compile("'speedBegin':\\s*(\\d+)")
            match_startTime = startTime.search(string)
            match_type = type.search(string)
            match_speed = speed.search(string)
            if match_startTime:
                if match_type:
                    if match_speed:
                        return (
                            '报警时间：{}'.format(match_startTime.group(1)),
                            '报警类型：{}'.format(match_type.group(1)),
                        )

        results = []
        for item in data:
            result = extract_values(str(item))
            if result:
                results.append(result)
                for i in results:
                    print(i + res[0][-1])
                    self.textbox.insert("end", f"\n\n{i + res[0][-1]}")
        if 报警 == '9':
            possible_alarm_types = ["报警类型：碰撞报警", "报警类型：声控报警", "报警类型：防拆除报警",
                                    "报警类型：TF卡拔出报警", "报警类型：TF卡异常报警", "报警类型：紧急报警",
                                    "报警类型：急减速报警", "报警类型：震动报警", "报警类型：急转弯报警",
                                    "报警类型：急加速报警", "报警类型：终端主电源掉电", "报警类型：超速报警",
                                    "报警类型：终端主电源欠压", "报警类型：位移报警"]
            posss = []
            alarm_types = [result[1] for result in results]
            for alarm_type in alarm_types:
                posss.append(alarm_type)
            set1 = set(possible_alarm_types)
            set2 = set(posss)
            data = list(set1 - set2)
            print(data)
            if data:
                print(f"未触发的报警类型: {data}")
                messagebox.showinfo('提示', message=f"未触发的报警类型:\n {data}")
            else:
                print('所有报警已触发')
                messagebox.showinfo('提示', message='所有报警已触发')

    def Trackjko(self):
        proxyMeta = f"{self.prox}"
        proxysdata = {
            'http': proxyMeta,
            'https': proxyMeta
        }
        url = "https://v4.car900.com:9998/car/v1/accelerate/track/listVehTrackPoint.json"
        now_time1 = time.strftime('%Y-%m-%d', time.localtime())
        querystring = {"plate": f"{int(self.sb_hao())}", "vehicleId": f"{self.车辆id()}",
                       "beginTime": f"{now_time1} 00:00:00",
                       "endTime": f"{now_time1} 23:59:59", "filterTime": "0", "converge": "1", "isHeart": "1",
                       "locationType": "1%2C2%2C3%2C0%2C6"}
        payload = ""
        headers = {
            "Content-Type": "application/x-www-form-urlencoded",
            "sessionId": f"{self.sessionId}",
            "Accept": "*/*",
            "Accept-Encoding": "gzip, deflate, br",
            "User-Agent": "PostmanRuntime-ApipostRuntime/1.1.0",
            "Connection": "keep-alive",
            "Cookie": "satoken=5e43775c-bfe6-455d-b257-a063d95ac8e9"
        }
        response = requests.request("GET", url, data=payload, headers=headers, proxies=proxysdata, params=querystring)
        user_dict = ast.literal_eval(response.text)
        data = user_dict['obj']['data']['trackList']

        def extract_values(string):
            pattern_t = re.compile("'t':\\s*'(\\d{4}-\\d{2}-\\d{2} \\d{2}:\\d{2}:\\d{2})'")
            ACC状态 = re.compile("'e':\\s*(\\d+)")
            是否定位 = re.compile("'i':\\s*(\\d+)")
            speed = re.compile("'s':\\s*(\\d+)")
            mileage = re.compile("'g':\\s*(\\d+(?:\\.\\d+)?)")
            行停状态 = re.compile("'x':\\s*(\\d+)")
            match_t = pattern_t.search(string)
            match_e = ACC状态.search(string)
            match_i = 是否定位.search(string)
            match_s = speed.search(string)
            match_g = mileage.search(string)
            match_x = 行停状态.search(string)
            if match_e and match_i and match_s and match_g and match_x:
                if match_e.group(1) == '1':
                    acc = '关'
                else:
                    acc = '开'
                if match_i.group(1) == '1':
                    isStop = '北斗+GPS'
                else:
                    isStop = '卫星信号弱'
                if match_x.group(1) == '1':
                    x = '行驶'
                else:
                    if match_x.group(1) == '2':
                        x = '停止'
                    else:
                        if match_x.group(1) == '3':
                            x = '离线'
            return (
                'ACC：{}'.format(acc), '状态：{}'.format(isStop), '速度：{}'.format(match_s.group(1)),
                '里程：{}'.format(match_g.group(1)), '行停：{}'.format(x))

        results = []
        for item in data:
            result = extract_values(str(item))
            if result:
                results.append(result)
        # print(results)
        return results

    def Track(self):
        proxyMeta = f"{self.prox}"
        proxysdata = {
            'http': proxyMeta,
            'https': proxyMeta
        }
        url = "https://v4.car900.com:9998/car/v1/accelerate/track/listVehTrackPoint.json"
        now_time1 = time.strftime('%Y-%m-%d', time.localtime())
        querystring = {"plate": f"{int(self.sb_hao())}", "vehicleId": f"{self.车辆id()}",
                       "beginTime": f"{now_time1} 00:00:00",
                       "endTime": f"{now_time1} 23:59:59", "filterTime": "0", "converge": "1", "isHeart": "1",
                       "locationType": "1%2C2%2C3%2C0%2C6"}
        payload = ""
        headers = {
            "Content-Type": "application/x-www-form-urlencoded",
            "sessionId": f"{self.sessionId}",
            "Accept": "*/*",
            "Accept-Encoding": "gzip, deflate, br",
            "User-Agent": "PostmanRuntime-ApipostRuntime/1.1.0",
            "Connection": "keep-alive",
            "Cookie": "satoken=5e43775c-bfe6-455d-b257-a063d95ac8e9"
        }
        response = requests.request("GET", url, data=payload, headers=headers, proxies=proxysdata, params=querystring)
        user_dict = ast.literal_eval(response.text)
        data = user_dict['obj']['data']['trackList']
        data1 = user_dict['obj']['total']

        def extract_values(string):
            pattern_t = re.compile("'t':\\s*'(\\d{4}-\\d{2}-\\d{2} \\d{2}:\\d{2}:\\d{2})'")
            pattern_a = re.compile("'a':\\s*(\\d+\\.\\d+)")
            pattern_o = re.compile("'o':\\s*(\\d+\\.\\d+)")
            ACC状态 = re.compile("'e':\\s*(\\d+)")
            是否定位 = re.compile("'i':\\s*(\\d+)")
            speed = re.compile("'s':\\s*(\\d+)")
            mileage = re.compile("'g':\\s*(\\d+(?:\\.\\d+)?)")
            行停状态 = re.compile("'x':\\s*(\\d+)")
            match_t = pattern_t.search(string)
            match_a = pattern_a.search(string)
            match_o = pattern_o.search(string)
            match_e = ACC状态.search(string)
            match_i = 是否定位.search(string)
            match_s = speed.search(string)
            match_g = mileage.search(string)
            match_x = 行停状态.search(string)
            if match_t and match_a and match_o and match_e and match_i and match_s and match_g and match_x:
                if match_e.group(1) == '1':
                    acc = '关'
                else:
                    acc = '开'
                if match_i.group(1) == '1':
                    isStop = '北斗+GPS'
                else:
                    isStop = '卫星信号弱'
                if match_x.group(1) == '1':
                    x = '行驶'
                else:
                    if match_x.group(1) == '2':
                        x = '停止'
                    else:
                        if match_x.group(1) == '3':
                            x = '离线'
            return ('时间：{}'.format(match_t.group(1)),
                    '纬度：{}'.format(float(match_a.group(1))), '经度：{}'.format(float(match_o.group(1))),
                    'ACC：{}'.format(acc), '状态：{}'.format(isStop),
                    '速度：{}'.format(match_s.group(1)), '里程：{}'.format(match_g.group(1)), '行停：{}'.format(x))

        results = []
        for item in data:
            result = extract_values(str(item))
            if result:
                results.append(result)
        for i in results:
            print(i)
            self.Tracktextbox.insert(1.0, f'\n{i}\n')
        self.Tracktextbox.insert(1.0, '\n轨迹总条数：{}'.format(data1))
        print('轨迹总条数：{}'.format(data1))

    def 轨迹808(self):
        self.Tracktextbox.delete(1.0, "end")
        files = []
        exception_count = 0
        csv_pattern = '*.csv'
        for filename in os.listdir(os.getcwd()):
            if fnmatch.fnmatch(filename, csv_pattern):
                file_path = os.getcwd() + f'/{filename}'
                files.append(file_path)
                if self.Trackip_on():
                    result = messagebox.askyesno("提醒", f"是否使用   {files[0]}       跑轨迹文件？")
                    if result:
                        fCase = open(files[0], 'r', encoding='gbk')
                        datas = csv.reader(fCase)
                        data1 = []
                        o = 0
                        for line in datas:
                            data1.append(line)
                        for nob1 in range(0, int(self.TrackcountText())):
                            t = data1[nob1]
                            o += 1
                            now_time = time.strftime('%Y%m%d%H%M%S', time.localtime())
                            消息ID = '0200'
                            消息体属性 = '002F'
                            设备号 = f'{self.sb_hao()}'.zfill(12)
                            流水号 = f'{0}'.zfill(4)
                            报警 = '00000000'
                            状态 = '00000003'
                            wd2 = float(t[0]) * 1000000
                            wd3 = hex(int(wd2))
                            纬度 = wd3[2:].zfill(8).upper()
                            jd2 = float(t[1]) * 1000000
                            jd3 = hex(int(jd2))
                            经度 = jd3[2:].zfill(8).upper()
                            高程 = f'{nob1}'.zfill(4)
                            速度 = f'0{random.randint(20, 30)}0'
                            方向 = f'00{random.randint(10, 90)}'
                            时间 = now_time[2:]
                            附加里程 = '0104' + f'{nob1}0'.zfill(8)
                            附加信息ID = '0202044C250400000000300103'
                            w = 消息ID + 消息体属性 + 设备号 + 流水号 + 报警 + 状态 + 纬度 + 经度 + 高程 + 速度 + 方向 + 时间 + 附加里程 + 附加信息ID
                            a = get_xor(w)
                            b = get_bcc(a)
                            if b.upper() == "7E":
                                a.replace("00", "01")
                                b = get_bcc(a)
                            E = w + b.upper().zfill(2)
                            t = '7E' + E.replace("7E", "01") + '7E'
                            D = get_xor(E)
                            data = '7E ' + D + ' 7E'
                            if data[:2] != "7E":
                                print(f"错误：{data}")
                                t = t[:81] + "00" + t[82:]
                                data = get_xor(t)
                                print("修改后data：{}".format(data))
                                print('\n' * 1)
                            print(data)
                            s = socket(AF_INET, SOCK_STREAM)
                            try:
                                s.settimeout(10)
                                s.connect((f'{self.Trackip()}', int(self.Trackport())))
                                s.send(bytes().fromhex(t))
                                send = s.recv(1024).hex()
                                tip_content = '\n服务器应答：\n{}\n\n'.format(send.upper())
                                self.Tracktextbox.insert(1.0, tip_content)
                                time.sleep(3)
                            except ConnectionRefusedError:
                                messagebox.showinfo('提示', message="连接被拒绝")
                                self.Tracktextbox.delete(1.0, "end")
                                self.Tracktextbox.insert('end', '连接被拒绝')
                            except TimeoutError:
                                messagebox.showinfo('提示', message="连接超时")
                                self.Tracktextbox.delete(1.0, "end")
                                self.Tracktextbox.insert('end', '连接超时')
                            except Exception as e:
                                exception_count += 1
                                continue
                        self.Tracktextbox.insert(1.0, '数据发送完成\n')
                        if exception_count > 0:
                            messagebox.showinfo('提示', message=f"总共有 {exception_count} 条数据没有应答")
                            print(f"总共有 {exception_count} 条数据没有应答")
                        else:
                            pass
                    else:
                        file_path = filedialog.askopenfilename(initialdir=os.getcwd(), title="选择CSV文件",
                                                               filetypes=(("CSV files", "*.csv"), ("all files", "*.*")))
                        fCase = open(file_path, 'r', encoding='gbk')
                        datas = csv.reader(fCase)
                        data1 = []
                        o = 0
                        for line in datas:
                            data1.append(line)
                        for nob1 in range(0, int(self.TrackcountText())):
                            t = data1[nob1]
                            o += 1
                            now_time = time.strftime('%Y%m%d%H%M%S', time.localtime())
                            消息ID = '0200'
                            消息体属性 = '002F'
                            设备号 = f'{self.sb_hao()}'.zfill(12)
                            print(f'设备号:{设备号}')
                            流水号 = f'{0}'.zfill(4)
                            报警 = '00000000'
                            状态 = '00000003'
                            wd2 = float(t[0]) * 1000000
                            wd3 = hex(int(wd2))
                            纬度 = wd3[2:].zfill(8).upper()
                            jd2 = float(t[1]) * 1000000
                            jd3 = hex(int(jd2))
                            经度 = jd3[2:].zfill(8).upper()
                            高程 = f'{nob1}'.zfill(4)
                            速度 = f'0{random.randint(20, 30)}0'
                            方向 = f'00{random.randint(10, 90)}'
                            时间 = now_time[2:]
                            附加里程 = '0104' + f'{nob1}0'.zfill(8)
                            附加信息ID = '0202044C250400000000300103'
                            w = 消息ID + 消息体属性 + 设备号 + 流水号 + 报警 + 状态 + 纬度 + 经度 + 高程 + 速度 + 方向 + 时间 + 附加里程 + 附加信息ID
                            a = get_xor(w)
                            b = get_bcc(a)
                            if b.upper() == "7E":
                                a.replace("00", "01")
                                b = get_bcc(a)
                            E = w + b.upper().zfill(2)
                            t = '7E' + E.replace("7E", "01") + '7E'
                            D = get_xor(E)
                            data = '7E ' + D + ' 7E'
                            if data[:2] != "7E":
                                print(f"错误：{data}")
                                t = t[:81] + "00" + t[82:]
                                data = get_xor(t)
                                print("修改后data：{}".format(data))
                                print('\n' * 1)
                            print(data)
                            if self.Trackip_on():
                                s = socket(AF_INET, SOCK_STREAM)
                                try:
                                    s.settimeout(10)
                                    s.connect((f'{self.Trackip()}', int(self.Trackport())))
                                    s.send(bytes().fromhex(t))
                                    send = s.recv(1024).hex()
                                    tip_content = '\n服务器应答：\n{}\n\n'.format(send.upper())
                                    self.Tracktextbox.insert(1.0, tip_content)
                                    time.sleep(3)
                                except ConnectionRefusedError:
                                    messagebox.showinfo('提示', message="连接被拒绝")
                                    self.Tracktextbox.delete(1.0, "end")
                                    self.Tracktextbox.insert('end', '连接被拒绝')
                                except TimeoutError:
                                    messagebox.showinfo('提示', message="连接超时")
                                    self.Tracktextbox.delete(1.0, "end")
                                    self.Tracktextbox.insert('end', '连接超时')
                                except Exception as e:
                                    exception_count += 1
                                    continue
                        self.Tracktextbox.insert(1.0, '数据发送完成\n')
                        if exception_count > 0:
                            messagebox.showinfo('提示', message=f"总共有 {exception_count} 条数据没有应答")
                            print(f"总共有 {exception_count} 条数据没有应答")
                        else:
                            pass
                if self.Trackapi_on():
                    self.sessionId = self.login1()
                    self.groupId1 = self.groupId组织()
                    self.Trackcountdown(5)
                    self.Track()

                return ''

    def wzhi部标(self):
        global t
        exception_count = 0
        now_time = time.strftime('%Y%m%d%H%M%S', time.localtime())
        wd1 = float(self.wd部标())
        wd2 = float(wd1) * 1000000
        wd3 = hex(int(wd2))
        jd1 = float(self.jd部标())
        jd2 = float(jd1) * 1000000
        jd3 = hex(int(jd2))
        标识位 = '7E'
        消息ID = '0200'
        消息体属性 = '002F'
        流水号 = f'{random.randint(15, 20)}'.zfill(4)
        报警 = self.sb_bj()
        状态 = self.sb_ztai()
        纬度 = wd3[2:].zfill(8).upper()
        经度 = jd3[2:].zfill(8).upper()
        高程 = f'00{random.randint(15, 20)}'
        速度 = self.sdu()[2:].zfill(4).upper()
        print(速度)
        方向 = f'00{random.randint(15, 20)}'
        时间 = now_time[2:]
        设备号 = self.sb_hao().zfill(12)
        if 报警 == '1':
            报警1 = '00000000'
            消息体属性 = '006D'
            附加信息ID = f'EB4F000600A50000000F000600C5000000010004002D0DAC000300A80A002400A901CC000525541FAB262554202431255423322C255423332925541FC3270000000000000C00B289860432011891642044'
            w = 消息ID + 消息体属性 + 设备号 + 流水号 + 报警1 + 状态 + 纬度 + 经度 + 高程 + 速度 + 方向 + 时间 + 附加信息ID
        elif 报警 == "2":
            报警1 = '00000000'
            消息体属性 = '0040'
            附加信息ID = f'0104{self.lic().zfill(8)}EB1C000C00B28986047701207027150100060089FFFFFDFF000400B70D05'
            w = 消息ID + 消息体属性 + 设备号 + 流水号 + 报警1 + 状态 + 纬度 + 经度 + 高程 + 速度 + 方向 + 时间 + 附加信息ID
        elif 报警 == "3":
            报警1 = '00000000'
            消息体属性 = '0040'
            附加信息ID = f'0104{self.lic().zfill(8)}EB1C000C00B28986047701207027150100060089FDFFFFFF000400B71105'
            w = 消息ID + 消息体属性 + 设备号 + 流水号 + 报警1 + 状态 + 纬度 + 经度 + 高程 + 速度 + 方向 + 时间 + 附加信息ID
        elif 报警 == "4":
            报警1 = '00000000'
            消息体属性 = '0040'
            附加信息ID = f'0104{self.lic().zfill(8)}EB1C000C00B28986047701207027150100060089FFFFFEFF000400B70E05'
            w = 消息ID + 消息体属性 + 设备号 + 流水号 + 报警1 + 状态 + 纬度 + 经度 + 高程 + 速度 + 方向 + 时间 + 附加信息ID
        elif 报警 == "5":
            报警1 = '00000000'
            消息体属性 = '0053'
            附加信息ID = f'0104{self.lic().zfill(8)}30011F310110EB29000C00B28986047701217055133200060089FFFFEFFF000600C5FFFFBFEF0004002D0F42000300A844'
            w = 消息ID + 消息体属性 + 设备号 + 流水号 + 报警1 + 状态 + 纬度 + 经度 + 高程 + 速度 + 方向 + 时间 + 附加信息ID
        elif 报警 == "6":
            报警1 = '00000000'
            消息体属性 = '00A4'
            附加信息ID = f'0104{self.lic().zfill(8)}30011D310100642F0000000000210200000000000000000000000000000000221104203813002030303030303030221104203813000101EB49000C00B28986047701217055137000060089FFFFFFFF000600C5FFFFFFE70004002D1008000300A84B000B00D801CC002554016E6501001100D5383636383138303339393231343434'
            w = 消息ID + 消息体属性 + 设备号 + 流水号 + 报警1 + 状态 + 纬度 + 经度 + 高程 + 速度 + 方向 + 时间 + 附加信息ID
        elif 报警 == "7":
            报警1 = '00000000'
            消息体属性 = '008B'
            附加信息ID = f'0104{self.lic().zfill(8)}150400000000300118310100EB4C000C00B28986047701217055856000060089FFFFFFFF000600C5FFFFFFE7000B00D801CC0025540D89B1490004002D2EAA001100D5383633303731303639373236363734000600F880000000EF0D00000000000000000011120000'
            w = 消息ID + 消息体属性 + 设备号 + 流水号 + 报警1 + 状态 + 纬度 + 经度 + 高程 + 速度 + 方向 + 时间 + 附加信息ID
        elif 报警 == "8":
            报警1 = '00000000'
            消息体属性 = '008B'
            附加信息ID = f'0104{self.lic().zfill(8)}150400000000300118310100EB4C000C00B28986047701217055856000060089FFFFFFFF000600C5FFFFFFE7000B00D801CC0025540D89B1490004002D2EAA001100D5383633303731303639373236363734000600F880000000EF0D00000000000000000011150000'
            w = 消息ID + 消息体属性 + 设备号 + 流水号 + 报警1 + 状态 + 纬度 + 经度 + 高程 + 速度 + 方向 + 时间 + 附加信息ID
        elif 报警 == "9":
            报警1 = '00000000'
            alarms = ['00000001', '00000002', '00000080', '00000100', '10000000']
            消息体属性0 = '002F'
            附加信息ID0 = f'0104{self.lic().zfill(8)}0202044C250400000000300103'
            print('里程：' + self.lic().zfill(8))
            消息体属性_list = [
                '006D', '0040', '0040', '0040', '0053', '00A4', '008B', '008B',
            ]
            附加信息ID_list = [
                f'EB4F000600A50000000F000600C5000000010004002D0DAC000300A80A002400A901CC000525541FAB262554202431255423322C255423332925541FC3270000000000000C00B289860432011891642044',
                f'0104{self.lic().zfill(8)}EB1C000C00B28986047701207027150100060089FFFFFDFF000400B70D05',
                f'0104{self.lic().zfill(8)}EB1C000C00B28986047701207027150100060089FDFFFFFF000400B71105',
                f'0104{self.lic().zfill(8)}EB1C000C00B28986047701207027150100060089FFFFFEFF000400B70E05',
                f'0104{self.lic().zfill(8)}30011F310110EB29000C00B28986047701217055133200060089FFFFEFFF000600C5FFFFBFEF0004002D0F42000300A844',
                f'0104{self.lic().zfill(8)}30011D310100642F0000000000210200000000000000000000000000000000221104203813002030303030303030221104203813000101EB49000C00B28986047701217055137000060089FFFFFFFF000600C5FFFFFFE70004002D1008000300A84B000B00D801CC002554016E6501001100D5383636383138303339393231343434',
                f'0104{self.lic().zfill(8)}150400000000300118310100EB4C000C00B28986047701217055856000060089FFFFFFFF000600C5FFFFFFE7000B00D801CC0025540D89B1490004002D2EAA001100D5383633303731303639373236363734000600F880000000EF0D00000000000000000011120000',
                f'0104{self.lic().zfill(8)}150400000000300118310100EB4C000C00B28986047701217055856000060089FFFFFFFF000600C5FFFFFFE7000B00D801CC0025540D89B1490004002D2EAA001100D5383633303731303639373236363734000600F880000000EF0D00000000000000000011150000',
            ]
            for alarm in alarms:
                w = 消息ID + 消息体属性0 + 设备号 + 流水号 + alarm + 状态 + 纬度 + 经度 + 高程 + 速度 + 方向 + 时间 + 附加信息ID0
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
                    t = t[:81] + "00" + t[82:]
                print(t)
                if self.ip_on():
                    s = socket(AF_INET, SOCK_STREAM)
                    try:
                        s.settimeout(10)
                        s.connect((f'{self.ip()}', int(self.port())))
                        s.send(bytes().fromhex(t))
                        send = s.recv(1024).hex()
                        tip_content = '\n服务器应答：\n{}\n\n'.format(send.upper())
                        self.textbox.insert(1.0, tip_content)
                        time.sleep(1)
                    except ConnectionRefusedError:
                        messagebox.showinfo('提示', message="连接被拒绝")
                        self.textbox.delete(1.0, "end")
                        self.textbox.insert('end', '连接被拒绝')
                    except TimeoutError:
                        messagebox.showinfo('提示', message="连接超时")
                        self.textbox.delete(1.0, "end")
                        self.textbox.insert('end', '连接超时')
                    except Exception as e:
                        print(e)
                        exception_count += 1
                        continue
            for i in range(len(消息体属性_list) + 1):
                if i < len(附加信息ID_list):
                    w = 消息ID + 消息体属性_list[
                        i] + 设备号 + 流水号 + 报警1 + 状态 + 纬度 + 经度 + 高程 + 速度 + 方向 + 时间 + 附加信息ID_list[
                            i]
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
                        t = t[:81] + "00" + t[82:]
                    print(t)
                    if self.ip_on():
                        s = socket(AF_INET, SOCK_STREAM)
                        try:
                            s.settimeout(10)
                            s.connect((f'{self.ip()}', int(self.port())))
                            s.send(bytes().fromhex(t))
                            send = s.recv(1024).hex()
                            tip_content = '\n服务器应答：\n{}\n\n'.format(send.upper())
                            self.textbox.insert(1.0, tip_content)
                            time.sleep(1)
                        except ConnectionRefusedError:
                            messagebox.showinfo('提示', message="连接被拒绝")
                            self.textbox.delete(1.0, "end")
                            self.textbox.insert('end', '连接被拒绝')
                        except TimeoutError:
                            messagebox.showinfo('提示', message="连接超时")
                            self.textbox.delete(1.0, "end")
                            self.textbox.insert('end', '连接超时')
                        except Exception as e:
                            print(e)
                            exception_count += 1
                            continue
            # self.textbox.insert(1.0, '数据发送完成\n')
            if exception_count > 0:
                messagebox.showinfo('提示', message=f"总共有 {exception_count} 条数据没有应答")
                print(f"总共有 {exception_count} 条数据没有应答")
            else:
                pass
            if self.api_on():
                self.sessionId = self.login1()
                self.groupId1 = self.groupId组织()
                if self.baojpd(报警) is None:
                    self.textbox.insert(1.0, '\n平台没有对应的报警类型\n\n')
                else:
                    self.countdown(5)
                    self.alam(报警)
            return ''
        else:
            附加信息ID = f'0104{self.lic().zfill(8)}0202044C250400000000300103'
            w = 消息ID + 消息体属性 + 设备号 + 流水号 + 报警 + 状态 + 纬度 + 经度 + 高程 + 速度 + 方向 + 时间 + 附加信息ID
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
            t = t[:81] + "00" + t[82:]
            data = get_xor(t)
        print(data)
        print(t)

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
        print(data1)
        print(t1)
        tip_content = '\n位置数据：\n{}\n'.format(data)
        self.textbox.insert(1.0, tip_content)
        if self.ip_on():
            s = socket(AF_INET, SOCK_STREAM)
            try:
                s.settimeout(10)
                s.connect((f'{self.ip()}', int(self.port())))
                s.send(bytes().fromhex(t))
                send = s.recv(1024).hex()
                s.send(bytes().fromhex(t1))
                send1 = s.recv(1024).hex()
                tip_content = '服务器应答：\n{}\n\n'.format(send.upper())
                self.textbox.insert(1.0, tip_content)
            except ConnectionRefusedError:
                messagebox.showinfo('提示', message="连接被拒绝")
                self.textbox.delete(1.0, "end")
                self.textbox.insert('end', '连接被拒绝')
            except TimeoutError:
                messagebox.showinfo('提示', message="连接超时")
                self.textbox.delete(1.0, "end")
                self.textbox.insert('end', '连接超时')
            except Exception as e:
                print(e)
                exception_count += 1
                pass
        # self.textbox.insert(1.0, '数据发送完成\n')
        if exception_count > 0:
            messagebox.showinfo('提示', message=f"总共有 {exception_count} 条数据没有应答")
            print(f"总共有 {exception_count} 条数据没有应答")
        else:
            pass
        if self.api_on():
            self.sessionId = self.login1()
            self.groupId1 = self.groupId组织()
            if self.baojpd(报警) is None:
                self.textbox.insert(1.0, '\n平台没有对应的报警类型\n\n')
            else:
                self.countdown(5)
                self.alam(报警)
        else:
            pass
        return ''

    def qo_login部标(self):
        src = self.type_Text.get().strip()
        if src == '位置数据':
            sbb1 = self.sb_hao()
            if not sbb1:
                self.textbox.delete(1.0, "end")
                self.textbox.insert(1.0, "请输入设备号")
            else:
                self.textbox.delete(1.0, "end")
                self.textbox.insert(1.0, self.wzhi部标())

    def button_mode(self):
        global is_on
        wd1 = get_latitude(base_lat=float(self.wd()), radius=100)
        jd1 = get_longitude(base_log=float(self.jd()), radius=100)
        self.wd_Text.delete(0, "end")
        self.wd_Text.insert(0, wd1)
        self.jd_Text.delete(0, "end")
        self.jd_Text.insert(0, jd1)

    def thread_it(self, func, *args):
        self.myThread = threading.Thread(target=func, args=args)
        self.myThread.daemon = True
        self.myThread.start()

    def Trackcountdown(self, t):
        for i in range(t):
            countdown_message = "\r等待接口请求时长：%02d" % (t - i) + '秒'
            print(countdown_message, end='')
            # 清空文本框内容并插入新内容
            self.Tracktextbox.delete('1.0', 'end')
            self.Tracktextbox.insert('1.0', countdown_message)
            time.sleep(1)
        self.Tracktextbox.delete('1.0', 'end')

    def countdown(self, t):
        for i in range(t):
            countdown_message = "\r等待接口请求时长：%02d" % (t - i) + '秒'
            print(countdown_message, end='')
            # 清空文本框内容并插入新内容
            self.textbox.delete('1.0', 'end')
            self.textbox.insert('1.0', countdown_message)
            time.sleep(1)
        self.textbox.delete('1.0', 'end')

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)

    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def wd(self):
        wd = self.wd_Text.get().strip()
        return wd

    def jd(self):
        jd = self.jd_Text.get().strip()
        return jd

    def ip(self):
        ip = self.ip_Text.get().strip()
        return ip

    def port(self):
        port = self.port_Text.get().strip()
        return port

    def ip_on(self):
        ip_on = self.switch_var.get()
        print(ip_on)
        return ip_on

    def api_on(self):
        api_on = self.switch_var1.get()
        print(api_on)
        return api_on

    def Trackip_on(self):
        ip_on = self.Trackswitch_var.get()
        print(ip_on)
        return ip_on

    def Trackapi_on(self):
        api_on = self.Trackswitch_var1.get()
        print(api_on)
        return api_on

    def sb_hao(self):
        sb = self.sbei_Text.get().strip()
        return sb

    def wd部标(self):
        wd = self.wd_Text.get().strip()
        return wd

    def jd部标(self):
        jd = self.jd_Text.get().strip()
        return jd

    def groupId组织(self):
        group = self.group_Text1.get().strip()
        return group

    def user账号(self):
        user = self.user_Text1.get().strip()
        return user

    def pwd密码(self):
        pwd = self.pwd_Text1.get().strip()
        return pwd

    def sdu(self):
        sdu = self.sdu_Text.get().strip()
        sdu1 = hex(int(sdu) * 10)
        print(sdu1)
        return sdu1

    def lic(self):
        lic = self.lic_Text.get().strip()
        hex_num = hex(int(float(lic) * 10))
        return hex_num[2:].upper()

    def TrackcountText(self):
        TrackcountText = self.Trackcount_Text.get().strip()
        return int(TrackcountText)

    def Trackip(self):
        Trackip = self.Trackip_Text.get().strip()
        return Trackip

    def Trackport(self):
        Trackport = self.Trackport_Text.get().strip()
        return Trackport

    def sb_bj(self):
        sb = self.baoji_Text.get()
        if sb == "紧急报警":
            return '00000001'
        elif sb == "超速报警":
            return '00000002'
        elif sb == "模块开路":
            return '00000040'
        elif sb == "终端欠压":
            return '00000080'
        elif sb == "终端掉电":
            return '00000100'
        elif sb == "车辆非法点火":
            return '08000000'
        elif sb == "车辆非法位移":
            return '10000000'
        elif sb == "碰撞报警和震动报警":
            return "1"
        elif sb == "急减速":
            return "2"
        elif sb == "急转弯":
            return "3"
        elif sb == "急加速":
            return "4"
        elif sb == "非法拆除报警":
            return "5"
        elif sb == "声控报警":
            return "6"
        elif sb == "TF卡拔出报警":
            return "7"
        elif sb == "TF卡异常报警":
            return "8"
        elif sb == "自动化报警":
            return "9"
        elif sb == "正常":
            return '00000000'

    def sb_ztai(self):
        ztai = self.ztai_Text.get().strip()
        if ztai == "ACC开卫星信号弱":
            return "00000001"
        elif ztai == "ACC关卫星信号弱":
            return '00000000'
        elif ztai == "ACC关北斗+GPS":
            return '00000002'
        elif ztai == "南纬":
            return '00000004'
        elif ztai == "ACC开和北斗+GPS":
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

    def v4_button_event(self):
        self.select_frame_by_name("v4.car900.com")

    def home_button_event(self):
        self.select_frame_by_name("Track")

    def select_frame_by_name(self, name):
        # set button color for selected button
        self.sidebar_button_1.configure(fg_color=("gray75", "gray25") if name == "v4.car900.com" else "transparent")
        self.sidebar_button_2.configure(fg_color=("gray75", "gray25") if name == "Track" else "transparent")

        # show selected frame
        if name == "v4.car900.com":
            self.my_frame.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")
            self.result_frame.grid(row=1, column=1, padx=10, pady=1, sticky="nsew")
        else:
            self.my_frame.grid_forget()
            self.result_frame.grid_forget()
        if name == "Track":
            self.Track_frame.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")
            self.Trackresult_frame.grid(row=1, column=1, padx=10, pady=1, sticky="nsew")
        else:
            self.Track_frame.grid_forget()
            self.Trackresult_frame.grid_forget()

    def __init__(self):
        super().__init__()
        self.user = config['V4']['user']
        self.password = config['V4']['password']
        self.groupId = config['V4']['groupId']
        self.ip_st = config['V4']['ip']
        self.port_st = config['V4']['port']
        self.sbei = config['sbei']['808sbei']
        self.prox = config['V4']['bei_ip']

        #     self.title("启动等待")
        #     self.geometry("220x70")
        #     self.eval('tk::PlaceWindow . center')
        #     self.attributes("-topmost", True)
        #     # 创建一个标签用于显示加载信息
        #     self.label = customtkinter.CTkLabel(self, text="正在加载...", font=("Helvetica", 24))
        #     self.label.grid(padx=10,pady=5)
        #
        #     # 创建一个进度条
        #     self.progressbar = customtkinter.CTkProgressBar(self)
        #     self.progressbar.grid(padx=10,pady=5)
        #
        #     # 启动加载线程
        #     self.start_loading()
        #
        # def start_loading(self):
        #     # 创建并启动一个新线程来执行加载任务
        #     loading_thread = threading.Thread(target=self.load_task)
        #     loading_thread.start()
        #
        # def load_task(self):
        #     # 模拟加载任务
        #     for i in range(101):
        #         time.sleep(0.03)  # 模拟加载时间
        #         self.progressbar.set(i / 100)  # 更新进度条
        #         self.update_idletasks()  # 刷新界面
        #
        #     # 加载完成后显示主界面内容
        #     self.uimain()
        #
        # def uimain(self):#主页面

        self.geometry(f"{1120}x{560}+450+200")
        self.title("车联版本（锋） 作者 : 姚子奇")
        self.attributes("-topmost", False)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "test_images")
        self.ico_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "cache.ico")), size=(26, 26))
        self.v4_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "chat_dark.png")),
                                               dark_image=Image.open(os.path.join(image_path, "chat_light.png")),
                                               size=(20, 20))
        self.home_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "mt_dark.png")),
                                                 dark_image=Image.open(os.path.join(image_path, "mt_light.png")),
                                                 size=(20, 20))

        self.sidebar_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="  V4车联版本", image=self.ico_image,
                                                 compound="left", font=customtkinter.CTkFont(size=25, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=20)
        TipBox(self.logo_label, "可设置文件夹内config.ini配置设备号，组织ID，账号，密码")
        self.sidebar_button_1 = customtkinter.CTkButton(self.sidebar_frame, corner_radius=0, height=40,
                                                        border_spacing=10, text="v4.car900.com",
                                                        fg_color="transparent", text_color=("gray10", "gray90"),
                                                        hover_color=("gray70", "gray30"),
                                                        image=self.v4_image, anchor="w", command=self.v4_button_event)
        self.sidebar_button_1.grid(row=1, column=0, sticky="ew")
        self.sidebar_button_2 = customtkinter.CTkButton(self.sidebar_frame, corner_radius=0, height=40,
                                                        border_spacing=10, text="Track",
                                                        fg_color="transparent", text_color=("gray10", "gray90"),
                                                        hover_color=("gray70", "gray30"),
                                                        image=self.home_image, anchor="w",
                                                        command=self.home_button_event)
        self.sidebar_button_2.grid(row=2, column=0, sticky="ew")

        self.sbei_Text_label = customtkinter.CTkLabel(self.sidebar_frame, text="设备号",
                                                      font=customtkinter.CTkFont(size=13),
                                                      fg_color="transparent")
        self.sbei_Text_label.grid(row=3, column=0, padx=(15, 10), pady=(15, 0), sticky="nsew")
        self.sbei_Text = customtkinter.CTkEntry(self.sidebar_frame)
        self.sbei_Text.insert(0, f"{self.sbei}")
        self.sbei_Text.grid(row=4, column=0, padx=(15, 10), sticky="nsew")

        self.group_Text_label = customtkinter.CTkLabel(self.sidebar_frame, text="组织ID",
                                                       font=customtkinter.CTkFont(size=13), fg_color="transparent")
        self.group_Text_label.grid(row=5, column=0, padx=(15, 10), sticky="nsew")
        self.group_Text1 = customtkinter.CTkEntry(self.sidebar_frame)
        self.group_Text1.insert(0, f"{self.groupId}")
        self.group_Text1.grid(row=6, column=0, padx=(15, 10), sticky="nsew")

        self.user_Text_label = customtkinter.CTkLabel(self.sidebar_frame, text="登录账号",
                                                      font=customtkinter.CTkFont(size=13), fg_color="transparent")
        self.user_Text_label.grid(row=7, column=0, padx=(15, 10), sticky="nsew")
        self.user_Text1 = customtkinter.CTkEntry(self.sidebar_frame)
        self.user_Text1.insert(0, f"{self.user}")
        self.user_Text1.grid(row=8, column=0, padx=(15, 10), sticky="nsew")
        #
        self.pwd_Text_label = customtkinter.CTkLabel(self.sidebar_frame, text="加密密码",
                                                     font=customtkinter.CTkFont(size=13), fg_color="transparent")
        self.pwd_Text_label.grid(row=9, column=0, padx=(15, 10), sticky="nsew")
        self.pwd_Text1 = customtkinter.CTkEntry(self.sidebar_frame)
        self.pwd_Text1.insert(0, f"{self.password}")
        self.pwd_Text1.grid(row=10, column=0, padx=(15, 10), sticky="nsew")

        self.appearance_mode_label = customtkinter.CTkLabel(self.sidebar_frame, text="外观模式:",
                                                            font=customtkinter.CTkFont(size=17, weight="bold"),
                                                            anchor="w")
        self.appearance_mode_label.grid(row=11, column=0, padx=20, pady=5)
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame,
                                                                       font=customtkinter.CTkFont(size=15,
                                                                                                  weight="bold"),
                                                                       values=["Light", "Dark", "System"],
                                                                       command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=12, column=0, padx=20, pady=5)
        self.appearance_mode_optionemenu.set("System")
        self.scaling_label = customtkinter.CTkLabel(self.sidebar_frame, text="UI 界面设置:",
                                                    font=customtkinter.CTkFont(size=17, weight="bold"), anchor="w")
        self.scaling_label.grid(row=13, column=0, padx=20, pady=5)

        self.scaling_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame,
                                                               font=customtkinter.CTkFont(size=15, weight="bold"),
                                                               values=["80%", "90%", "100%", "110%", "120%", "150%"],
                                                               command=self.change_scaling_event)
        self.scaling_optionemenu.grid(row=14, column=0, padx=20, pady=(0, 20))
        self.scaling_optionemenu.set("100%")

        self.myframe2()
        self.myframe1()

    def myframe1(self):
        self.my_frame = customtkinter.CTkFrame(master=self)
        self.my_frame.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

        self.ip_Text_label = customtkinter.CTkLabel(self.my_frame, text="服务器ip", font=customtkinter.CTkFont(size=13),
                                                    fg_color="transparent")
        self.ip_Text_label.grid(row=0, column=0, padx=(15, 10), sticky="nsew")
        self.ip_Text = customtkinter.CTkOptionMenu(self.my_frame, values=["47.107.222.141", f"{self.ip_st}"],
                                                   font=customtkinter.CTkFont(size=15, weight="bold"))
        self.ip_Text.set("47.107.222.141")
        self.ip_Text.grid(row=1, column=0, padx=(15, 10), sticky="nsew")

        self.port_Text_label = customtkinter.CTkLabel(self.my_frame, text="服务器Port",
                                                      font=customtkinter.CTkFont(size=13), fg_color="transparent")
        self.port_Text_label.grid(row=0, column=1, padx=(15, 10), sticky="nsew")
        self.port_Text = customtkinter.CTkEntry(self.my_frame)
        self.port_Text.insert(0, f"{self.port_st}")
        self.port_Text.grid(row=1, column=1, padx=(15, 10), sticky="nsew")

        self.on_1 = customtkinter.CTkButton(self.my_frame, width=15, text="随机经纬度",
                                            font=customtkinter.CTkFont(size=13), command=self.button_mode,
                                            fg_color=("#DB3E39", "#821D1A"))
        self.on_1.grid(row=3, column=3, padx=(15, 10), sticky="nsew")

        self.switch_var = BooleanVar(value=False)
        self.switch = customtkinter.CTkSwitch(master=self.my_frame, text=f"服务器", font=customtkinter.CTkFont(size=13),
                                              variable=self.switch_var)
        self.switch.grid(row=3, column=2, padx=(15, 10), sticky="nsew")

        self.switch_var1 = BooleanVar(value=False)
        self.switch = customtkinter.CTkSwitch(master=self.my_frame, text=f"报警查询",
                                              font=customtkinter.CTkFont(size=13),
                                              variable=self.switch_var1)
        self.switch.grid(row=2, column=2, padx=(15, 10), sticky="nsew")

        self.wd_Text_label = customtkinter.CTkLabel(self.my_frame, text="纬度", font=customtkinter.CTkFont(size=13),
                                                    fg_color="transparent")
        self.wd_Text_label.grid(row=2, column=0, padx=(15, 10), sticky="nsew")
        self.wd_Text = customtkinter.CTkEntry(self.my_frame)
        self.wd_Text.insert(0, "23.012173")
        self.wd_Text.grid(row=3, column=0, padx=(15, 10), sticky="nsew")

        self.jd_Text_label = customtkinter.CTkLabel(self.my_frame, text="经度", font=customtkinter.CTkFont(size=13),
                                                    fg_color="transparent")
        self.jd_Text_label.grid(row=2, column=1, padx=(15, 10), sticky="nsew")
        self.jd_Text = customtkinter.CTkEntry(self.my_frame)
        self.jd_Text.insert(0, "114.340462")
        self.jd_Text.grid(row=3, column=1, padx=(15, 10), sticky="nsew")

        self.baoj_Text_label = customtkinter.CTkLabel(self.my_frame, text="报警", font=customtkinter.CTkFont(size=13),
                                                      fg_color="transparent")
        self.baoj_Text_label.grid(row=6, column=0, padx=(15, 10), sticky="nsew")
        self.baoji_Text = customtkinter.CTkOptionMenu(self.my_frame, font=customtkinter.CTkFont(size=15, weight="bold"),
                                                      values=["正常", "自动化报警", "紧急报警", "超速报警", "终端欠压",
                                                              "终端掉电",
                                                              # "车辆非法点火", "模块开路",
                                                              "车辆非法位移", "碰撞报警和震动报警", "急减速", "急加速",
                                                              "急转弯", "非法拆除报警", "声控报警"
                                                          , "TF卡拔出报警", "TF卡异常报警"])
        self.baoji_Text.set("紧急报警")
        self.baoji_Text.grid(row=7, column=0, padx=(15, 10), pady=(0, 15), sticky="nsew")

        self.sdu_Text_label = customtkinter.CTkLabel(self.my_frame, text="速度", font=customtkinter.CTkFont(size=13),
                                                     fg_color="transparent")
        self.sdu_Text_label.grid(row=4, column=0, padx=(15, 10), sticky="nsew")
        self.sdu_Text = customtkinter.CTkEntry(self.my_frame)
        self.sdu_Text.insert(0, '20')
        self.sdu_Text.grid(row=5, column=0, padx=(15, 10), sticky="nsew")

        self.lic_Text_label = customtkinter.CTkLabel(self.my_frame, text="里程", font=customtkinter.CTkFont(size=13),
                                                     fg_color="transparent")
        self.lic_Text_label.grid(row=4, column=1, padx=(15, 10), sticky="nsew")
        self.lic_Text = customtkinter.CTkEntry(self.my_frame)
        self.lic_Text.insert(0, '20')
        self.lic_Text.grid(row=5, column=1, padx=(15, 10), sticky="nsew")

        self.type_label = customtkinter.CTkLabel(self.my_frame, text="部标类型",
                                                 font=customtkinter.CTkFont(size=13), fg_color="transparent")
        # self.type_label.grid(row=6, column=2, padx=(15, 10), sticky="nsew")
        self.type_Text = customtkinter.CTkOptionMenu(self.my_frame, font=customtkinter.CTkFont(size=15, weight="bold"),
                                                     values=["位置数据"])
        self.type_Text.set('位置数据')
        # self.type_Text.grid(row=7, column=2, padx=(15, 10), pady=(0, 15), sticky="nsew")

        self.ztai_label = customtkinter.CTkLabel(self.my_frame, text="车辆状态", font=customtkinter.CTkFont(size=13),
                                                 fg_color="transparent")
        self.ztai_label.grid(row=6, column=1, padx=(15, 10), sticky="nsew")
        self.ztai_Text = customtkinter.CTkOptionMenu(self.my_frame, font=customtkinter.CTkFont(size=15, weight="bold"),
                                                     values=["ACC开卫星信号弱", "ACC开和北斗+GPS", "ACC关卫星信号弱",
                                                             "ACC关北斗+GPS", "停运状态",
                                                             "经纬度已经保密插件保密", "南纬", "西经",
                                                             "车辆油路断开", "车辆电路断开", "单北斗", "单GPS",
                                                             "北斗GPS双模", "ACC开定位开北斗GPS满载",
                                                             "ACC开定位开北斗GPS空车", "车门加锁"])
        self.ztai_Text.set('ACC开卫星信号弱')
        self.ztai_Text.grid(row=7, column=1, padx=(15, 10), pady=(0, 15), sticky="nsew")

        self.str_button = customtkinter.CTkButton(self.my_frame, text="专用808发送",
                                                  font=customtkinter.CTkFont(size=13), fg_color=("#DB3E39", "#821D1A"),
                                                  command=lambda: self.thread_it(self.qo_login部标))
        self.str_button.grid(row=1, column=3, padx=(15, 10), sticky="nsew")

        self.result_frame = customtkinter.CTkFrame(master=self)
        self.result_frame.grid(row=1, column=1, padx=10, pady=1, sticky="nsew")

        self.textbox = customtkinter.CTkTextbox(self.result_frame, width=850, height=260)
        self.textbox.grid(row=0, column=1, padx=(20, 0), pady=(20, 20), sticky="nsew")

    def myframe2(self):
        self.Track_frame = customtkinter.CTkFrame(master=self)
        self.Track_frame.grid(row=0, column=1, padx=10, pady=10, sticky='nsew')
        self.Trackip_Text_label = customtkinter.CTkLabel(self.Track_frame, text='服务器ip',
                                                         font=customtkinter.CTkFont(size=13),
                                                         fg_color='transparent')
        self.Trackip_Text_label.grid(row=0, column=0, padx=(15, 10), sticky='nsew')
        self.Trackip_Text = customtkinter.CTkOptionMenu(self.Track_frame,
                                                        values=['47.107.222.141', f"{self.ip_st}"],
                                                        font=customtkinter.CTkFont(size=15, weight='bold'))
        self.Trackip_Text.set('47.107.222.141')
        self.Trackip_Text.grid(row=1, column=0, padx=(15, 10), sticky='nsew')
        self.Trackport_Text_label = customtkinter.CTkLabel(self.Track_frame, text='服务器Port',
                                                           font=customtkinter.CTkFont(size=13),
                                                           fg_color='transparent')
        self.Trackport_Text_label.grid(row=0, column=1, padx=(15, 10), sticky='nsew')
        self.Trackport_Text = customtkinter.CTkEntry(self.Track_frame)
        self.Trackport_Text.insert(0, f"{self.port_st}")
        self.Trackport_Text.grid(row=1, column=1, padx=(15, 10), sticky='nsew')
        self.Tracktime_Text = customtkinter.CTkEntry(self.Track_frame, placeholder_text='轨迹时间(默认1s)')
        self.Tracktime_Text.grid(row=1, column=2, padx=(15, 10), sticky='nsew')
        self.Trackswitch_var = BooleanVar(value=True)
        self.Trackswitch = customtkinter.CTkSwitch(master=self.Track_frame, text='服务器',
                                                   font=customtkinter.CTkFont(size=13),
                                                   variable=self.Trackswitch_var)
        self.Trackswitch.grid(row=3, column=2, padx=(15, 10), sticky='nsew')
        self.Trackswitch_var1 = BooleanVar(value=False)
        self.Trackswitch = customtkinter.CTkSwitch(master=self.Track_frame, text='报警查询',
                                                   font=customtkinter.CTkFont(size=13),
                                                   variable=self.Trackswitch_var1)
        self.Trackswitch.grid(row=2, column=2, padx=(15, 10), sticky='nsew')
        self.Trackcount = customtkinter.CTkLabel(master=self.Track_frame, text='轨迹条数')
        self.Trackcount.grid(row=2, column=0, columnspan=2, padx=(15, 10), sticky='nsew')
        self.Trackcount_Text = customtkinter.CTkEntry(master=self.Track_frame)
        self.Trackcount_Text.insert(0, '2')
        self.Trackcount_Text.grid(row=3, column=0, columnspan=2, padx=(15, 10), sticky='nsew')
        self.Track_button = customtkinter.CTkButton(self.Track_frame, text='轨迹808发送',
                                                    font=customtkinter.CTkFont(size=13),
                                                    fg_color=('#DB3E39', '#821D1A'),
                                                    command=(lambda: self.thread_it(self.轨迹808)))
        self.Track_button.grid(row=4, column=0, columnspan=2, padx=(15, 10), pady=(20,
                                                                                   0), sticky='nsew')
        self.Trackresult_frame = customtkinter.CTkFrame(master=self)
        self.Trackresult_frame.grid(row=1, column=1, padx=10, pady=1, sticky='nsew')
        self.Tracktextbox = customtkinter.CTkTextbox(self.Trackresult_frame, width=850, height=280)
        self.Tracktextbox.grid(row=0, column=1, padx=(20, 0), pady=(30, 2), sticky='nsew')

def count_runs():
    global file_path
    current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    try:
        path = r"C:\Users"
        if not os.path.exists(path):
            os.makedirs(path)
        file_path = os.path.join(path, "count.txt")
        with open(file_path, "r") as file:
            runs = int(file.readline().strip()) + 1
        with open(file_path, "w") as file:
            file.write(f"{runs}\n")
        print(f"第 {runs} 次运行于 {current_time}")
        return runs
    except FileNotFoundError:
        with open(file_path, "w") as file:
            file.write("0\n")


def check_double_press(key, interval=0.5):
    if keyboard.is_pressed(key):
        print('点击一次')
        time.sleep(interval)
        if keyboard.is_pressed(key):
            print('点击二次')
            return True
    return False


def create_shortcut():
    import sys
    current_file = os.path.abspath(sys.argv[0])
    desktop_path = os.path.join(os.path.expanduser('~'), 'Desktop')
    shortcut_name = os.path.basename(current_file[:-4]) + '.lnk'
    shortcut_path = os.path.join(desktop_path, shortcut_name)
    if not os.path.exists(shortcut_path):
        result1 = messagebox.askokcancel('创建快捷方式', '是否要创建快捷方式')
        if result1:
            command = f'powershell "$ws = New-Object -ComObject WScript.Shell; $s = $ws.CreateShortcut(\'{shortcut_path}\'); $s.TargetPath = \'{current_file}\'; $s.WorkingDirectory = \'{os.path.dirname(current_file)}\'; $s.Save()"'
            os.system(command)
            messagebox.showwarning('提示', '快捷方式已创建桌面。')
            os._exit(2)
        else:
            os._exit(2)
    else:
        os._exit(2)


def infinite_loop():
    global stop_threads
    while not stop_threads:
        mailcountdown(50)
        reply = check_reply()
        time.sleep(5)
        if reply is not None:
            break
        break


def mailcountdown(t):
    for i in range(t):
        countdown_message = '\r等待时长：%02d' % (t - i) + '秒'
        print(countdown_message, end='')
        time.sleep(1)


def check_ipv5():
    result = os.popen('ipconfig').read()
    pattern = r'\d+\.\d+\.\d+\.\d+'
    ipv4_list = re.findall(pattern, result)
    # print(ipv4_list[0])
    return ipv4_list[0]


def send_request():
    current_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
    subject = f"{check_ipv5()}请求使用 {current_time}"
    body = ''
    msg = MIMEText(body, 'plain', 'utf-8')
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject
    try:
        server = smtplib.SMTP_SSL('smtp.qq.com', 465)
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
        server.quit()
        print('请求邮件已发送')
    except Exception as e:
        try:
            print(f"发送邮件失败: {e}")
        finally:
            e = None
            del e


def check_reply():
    try:
        mail = imaplib.IMAP4_SSL('imap.qq.com')
        mail.login(sender_email, password)
        mail.select('inbox')

        status, messages = mail.search(None, 'UNSEEN')
        if status == "OK":
            latest_email_id = messages[0].split()[-1]  # 获取最新的一封邮件的ID
            status, data = mail.fetch(latest_email_id, '(RFC822)')
            if status == "OK":
                for response_part in data:
                    if isinstance(response_part, tuple):
                        msg = email.message_from_bytes(response_part[1])
                        subject = decode_header(msg["subject"])[0][0]
                        if isinstance(subject, bytes):
                            subject = subject.decode()
                        if f"Re:{check_ipv5()}请求使用" in subject:
                            for part in msg.walk():
                                if part.get_content_type() == "text/plain":
                                    body = part.get_payload(decode=True).decode()
                                    print(body)
                                    if "可以" in body:
                                        print("程序已启动")
                                        return True
                                    elif "不" in body:
                                        print("程序无法启动")
                                        messagebox.showinfo(title='远程被控', message='\n软件程序已远程关闭\n')
                                        os._exit(2)
                                        return False
            mail.logout()
    except Exception as e:
        print(f"检查邮件失败: {e}")
    return None


current_directory = os.getcwd()
conf_ini = current_directory + '\\config.ini'
config = ConfigObj(conf_ini, encoding='UTF-8')


def main():
    global stop_threads
    # send_request()
    # send_request()
    app = App()
    count_runs()
    with open('C:\\Users\\count.txt', 'r') as (file):
        runs = int(file.readline().strip()) + 1
        print(runs)
    if runs == 1:
        now = datetime.datetime.now()
        expiration_date = now + datetime.timedelta(days=(int('184')))
        with open('C:\\Users\\expiration_date.txt', 'w') as (f):
            f.write(expiration_date.strftime('%Y-%m-%d %H:%M:%S'))
    else:
        with open('C:\\Users\\expiration_date.txt', 'r') as (f):
            now = datetime.now()
            expiration_date_str = f.read()
            expiration_date = datetime.strptime(expiration_date_str, '%Y-%m-%d %H:%M:%S')
            print(expiration_date)
        if now > expiration_date:
            app.withdraw()
            app.attributes('-topmost', True)
            messagebox.showwarning(title='软件过期提醒', message='\n软件程序已过期，无法启动\n')
            while check_double_press('end'):
                try:
                    os.remove('C:\\Users\\expiration_date.txt')
                    os.remove('C:\\Users\\count.txt')
                except:
                    pass
                else:
                    app.attributes('-topmost', True)
                    messagebox.showwarning(title='欢迎超级管理员', message='\n已额外授权使用\n')
                    break

            os._exit(2)
        else:
            app.protocol('WM_DELETE_WINDOW', create_shortcut)
        app.mainloop()
        stop_threads = True


if __name__ == '__main__':
    thread1 = threading.Thread(target=infinite_loop)
    thread2 = threading.Thread(target=main)
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()
    # send_request()
