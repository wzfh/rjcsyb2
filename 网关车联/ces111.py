import customtkinter as ctk
import time, re, ast
import threading
import requests


def Track(self):
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
    response = requests.request("GET", url, data=payload, headers=headers, params=querystring)
    user_dict = ast.literal_eval(response.text)
    data = user_dict['obj']['data']['trackList']
    data1 = user_dict['obj']['total']

    def extract_values(string):
        pattern_t = re.compile(r"'t':\s*'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})'")
        pattern_a = re.compile(r"'a':\s*(\d+\.\d+)")
        pattern_o = re.compile(r"'o':\s*(\d+\.\d+)")
        match_t = pattern_t.search(string)
        match_a = pattern_a.search(string)
        match_o = pattern_o.search(string)
        if match_t and match_a and match_o:
            return match_t.group(1), float(match_a.group(1)), float(match_o.group(1))
        return None

    results = []
    for item in data:
        result = extract_values(str(item))
        if result:
            results.append(result)
    for i in results:
        print(i)
        self.Tracktextbox.insert(1.0, f'\n{i}')
    self.Tracktextbox.insert(1.0, f'\n{data1}')
    print('轨迹总条数：{}'.format(data1))
