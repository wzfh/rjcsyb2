import base64
import requests
import ast
import ddddocr


def login():
    global sessionId
    url = "http://tx.dev.car900.com:9999/oauth/getCode"
    payload = ""
    headers = {"User-Agent": "Apipost/8 (https://www.apipost.cn)"}
    response = requests.request("GET", url, data=payload, headers=headers)
    user_dict = ast.literal_eval(response.text)
    print(user_dict)
    img_str = f"{user_dict['obj']['code'][22:]}"
    bytes_img = base64.b64decode(img_str)
    with open('yzm.png', mode='wb') as f:
        f.write(bytes_img)
    ocr = ddddocr.DdddOcr(beta=True)
    with open('yzm.png', mode='rb') as f:
        image = f.read()
    result2 = ocr.classification(image)
    print('图形验证码:\t' + result2)  # 图形验证码
    print('uuid:\t\t' + user_dict['obj']['uuid'])
    uuid = user_dict['obj']['uuid']
    url = "http://tx.dev.car900.com:9999/oauth/v4/token"
    payload = "-----011000010111000001101001\r\n" \
              "Content-Disposition: form-data; name=\"username\"\r\n\r\nyaoziqi1\r\n" \
              "-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"scope\"\r\n\r\n" \
              "carWeb4\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"tenantId\"\r\n\r\n1\r\n" \
              "-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"password\"\r\n\r\n" \
              "gVsweVZH75MvWpn3hkPe+A==\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"code\"\r\n\r\n" \
              f"{result2}\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"uuid\"\r\n\r\n" \
              f"{uuid}\r\n-----011000010111000001101001--\r\n\r\n"
    headers = {
        "Sessionid": "null",
        "User-Agent": "Apipost/8 (https://www.apipost.cn)",
        "content-type": "multipart/form-data; boundary=---011000010111000001101001"
    }
    response = requests.request("POST", url, data=payload, headers=headers)
    user_dict1 = ast.literal_eval(response.text)
    sessionId = user_dict1['obj']['sessionId']
    print('sessionId:\t' + sessionId)


def 部门(count):
    login()
    for i in range(count):
        url = "http://tx.dev.car900.com:9999/car/v4/api/v4Department/addVehGroup.json"
        payload = {
            "groupName": f"测试{i}",
            "parentId": 1024,
            "contactName": None,
            "phone": None,
            "remark": None,
            "provinceCode": None,
            "cityCode": None,
            "areaCode": None,
            "address": None
        }
        headers = {
            "Sessionid": f"{sessionId}",
            "User-Agent": "Apipost/8 (https://www.apipost.cn)",
            "Content-Type": "application/json"
        }
        response = requests.request("POST", url, json=payload, headers=headers)
        print(response.text)


def 车辆(count):
    login()
    for i in range(count):
        url = "http://tx.dev.car900.com:9999/car/v4/api/assets/add.json"
        payload = {
            "assetsBaseVO": {
                "plate": f"1356854775{i}",
                "groupId": 1024,
                "iconType": 0,
                "terminalType": "GPRS-部标",
                "terminalNo": f"1356854775{i}",
                "terminalStatus": 0,
                "displayYear": None,
                "activationTmeStr": None,
                "serviceCode": None,
                "remark": None
            },
            "cardInfoVO": {
                "sim": None,
                "iccid": None,
                "totalFlow": 0,
                "flowType": 2
            },
            "customerInfoVO": {
                "vehicleType": None,
                "engineNo": None,
                "frameNo": None,
                "owner": None,
                "license": None,
                "phone": None,
                "address": None
            },
            "iInstallInfoVO": {
                "installPlace": None,
                "installPerson": None,
                "installRemark": None,
                "installDate": "2024-06-24 12:50:41"
            }
        }
        headers = {
            "Sessionid": f"{sessionId}",
            "User-Agent": "Apipost/8 (https://www.apipost.cn)",
            "Content-Type": "application/json"
        }
        response = requests.request("POST", url, json=payload, headers=headers)
        print(response.text)


if __name__ == '__main__':
    车辆(10)
    部门(10)
