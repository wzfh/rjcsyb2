import http.client

import requests
import json

proxyMeta = "192.168.10.59:808"
proxysdata = {
    'http': proxyMeta,
    'https': proxyMeta
}
url = "https://taxitest.car900.com:7101/test/doAuth"

response = requests.request("GET", url, proxies=proxysdata)
data = json.loads(response.text)
print(data['data']['test']['appId'])
print(data['data']['test']['requestId'])
print(data['data']['test']['timestamp'])
print(data['data']['test']['token'])

import requests

url = "https://taxitest.car900.com:7101/partialdata/operate"

payload = {"operateList": [
    {
        "id": 1,
        "companyId": "1200DDCX3307",
        "orderId": "17801823561662",
        "onArea": "440902",
        "driverName": "柯木娣",
        "licenseId": "440902197012143224",
        "fareType": "0",
        "vehicleNo": "粤KUM986",
        "bookDepTime": 20240331161633,
        "waitTime": None,
        "depLongitude": "110942540",
        "depLatitude": "21649440",
        "depArea": "新福路.|茂名市.愉园中学-南门",
        "depTime": 20240331162409,
        "destLongitude": "110932691",
        "destLatitude": "21666552",
        "destArea": "文明路.|福华花园",
        "destTime": 20240331163220,
        "bookModel": "40600",
        "model": "40600",
        "driveMile": "3.03",
        "driveTime": "480",
        "waitMile": None,
        "factPrice": "8.99",
        "price": "8.99",
        "cashPrice": None,
        "lineName": "",
        "linePrice": None,
        "posName": "",
        "posPrice": None,
        "benfitPrice": "0.0",
        "bookTip": None,
        "passengerTip": None,
        "peakUpPrice": None,
        "nightUpPrice": None,
        "farUpPrice": "0.0",
        "otherUpPrice": "0.0",
        "payState": 1,
        "payTime": 20240331163259,
        "orderMatchTime": 20240331163259,
        "invoiceStatus": 2
    }
]}
headers = {
    "appId": f"{data['data']['test']['appId']}",
    "requestId": f"{data['data']['test']['requestId']}",
    "timestamp": f"{data['data']['test']['timestamp']}",
    "token": f"{data['data']['test']['token']}",
    "content-type": "application/json"
}

response = requests.request("POST", url, json=payload, headers=headers, proxies=proxysdata)

print(response.text)
