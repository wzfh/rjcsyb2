import base64
import requests
import ast
import ddddocr
import random


def login():
    global sessionId
    url = "http://tx.dev.car900.com:9999/oauth/getCode"
    payload = ""
    headers = {"User-Agent": "Apipost/8 (https://www.apipost.cn)"}
    response = requests.request("GET", url, data=payload, headers=headers)
    user_dict = ast.literal_eval(response.text)
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
    # uuid = user_dict['obj']['uuid']
    # url = "http://tx.dev.car900.com:9999/oauth/v4/token"
    # payload = "-----011000010111000001101001\r\n" \
    #           "Content-Disposition: form-data; name=\"username\"\r\n\r\ntest-cs\r\n" \
    #           "-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"scope\"\r\n\r\n" \
    #           "carWeb4\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"tenantId\"\r\n\r\n1\r\n" \
    #           "-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"password\"\r\n\r\n" \
    #           "yxpgOP/E5xEbcPyvzEXbQw==\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; " \
    #           "name=\"code\"\r\n\r\n" \
    #           f"{result2}\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"uuid\"\r\n\r\n" \
    #           f"{uuid}\r\n-----011000010111000001101001--\r\n\r\n"
    # headers = {
    #     "Sessionid": "null",
    #     "User-Agent": "Apipost/8 (https://www.apipost.cn)",
    #     "content-type": "multipart/form-data; boundary=---011000010111000001101001"
    # }
    # response = requests.request("POST", url, data=payload, headers=headers)
    # print(response.text)
    # user_dict1 = ast.literal_eval(response.text)
    # sessionId = user_dict1['obj']['sessionId']
    # print('sessionId:\t' + sessionId)


def 部门(count):
    # login()
    for i in range(count):
        url = "http://tx.dev.car900.com:9999/car/v4/api/v4Department/addVehGroup.json"
        import random

        first_name = ["王", "李", "张", "刘", "赵", "蒋", "孟", "陈", "徐", "杨", "沈", "马", "高", "殷", "上官", "钟",
                      "常"]
        second_name = ["伟", "华", "建国", "洋", "刚", "万里", "爱民", "牧", "陆", "路", "昕", "鑫", "兵", "硕", "志宏",
                       "峰", "磊", "雷", "文", "明浩", "光", "超", "军", "达"]
        name = random.choice(first_name) + random.choice(second_name)
        payload = {
            "groupName": f"{name}",
            "parentId": 1131,
            "contactName": None,
            "phone": None,
            "remark": None,
            "provinceCode": None,
            "cityCode": None,
            "areaCode": None,
            "address": None
        }
        headers = {
            # "Sessionid": f"{sessionId}",
            "Sessionid": f"6820abbb4ce9499db4a491c56d5d47",
            "User-Agent": "Apipost/8 (https://www.apipost.cn)",
            "Content-Type": "application/json"
        }
        response = requests.request("POST", url, json=payload, headers=headers)
        print(response.text)


def 车辆(count):
    login()
    group_ids = [1221, 2121, 11121, 2122, 2123]
    selected_ids = []
    shu = int(count / len(group_ids))
    print(shu)
    for i in range(count):
        import requests

        url = "http://tx.dev.car900.com:9999/car/v4/api/assets/add.json"

        # 随机选择一个组ID
        selected_id = random.choice(group_ids)
        payload = {
            "assetsBaseVO": {
                "plate": "10" + "4450" + f"{i}".zfill(5),
                "groupId": f'{selected_id}',
                "iconType": 0,
                "terminalType": "GPRS-部标",
                "terminalNo": "10" + "4450" + f"{i}".zfill(5),
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
                "installDate": "2024-07-09 09:48:01"
            }
        }
        selected_ids.append(selected_id)
        headers = {
            "sessionid": f"{sessionId}",
            "Accept": "*/*",
            "Accept-Encoding": "gzip, deflate, br",
            "User-Agent": "PostmanRuntime-ApipostRuntime/1.1.0",
            "Connection": "keep-alive",
            "Content-Type": "application/json"
        }

        response = requests.request("POST", url, json=payload, headers=headers)
        print(response.text)
        if selected_ids.count(selected_id) == int(shu):
            group_ids.remove(selected_id)
        print("剩余的组ID：", group_ids)


def 学生(value):
    group_ids = [16202, 16203, 16204, 16205, 16206, 16207, 16208, 16209, 16210, 16211]
    selected_ids = []
    shu = int(value / len(group_ids))
    print(shu)
    for i in range(value):
        import requests
        selected_id = random.choice(group_ids)
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
            "classId": f'{selected_id}',
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
        selected_ids.append(selected_id)
        response = requests.request("POST", url, json=payload, headers=headers)
        if selected_ids.count(selected_id) == int(shu):
            group_ids.remove(selected_id)
        print(response.text)


if __name__ == '__main__':
    # 车辆(1000)
    # 部门(129)
    # login()
    学生(30000)
