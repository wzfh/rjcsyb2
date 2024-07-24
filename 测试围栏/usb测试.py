# import threading
# import random
#
#
# def print_numbers(start, end):
#     group_ids = [1221, 2121, 11121, 2122, 2123]
#     selected_ids = []
#     shu = int(10000 / len(group_ids))
#     print(shu)
#     for i in range(start, end):
#         import requests
#
#         url = "http://tx.dev.car900.com:9999/car/v4/api/assets/add.json"
#
#         # 随机选择一个组ID
#         selected_id = random.choice(group_ids)
#         payload = {
#             "assetsBaseVO": {
#                 "plate": "10" + "4650" + f"{i}".zfill(5),
#                 "groupId": f'{selected_id}',
#                 "iconType": 0,
#                 "terminalType": "GPRS-部标",
#                 "terminalNo": "10" + "4650" + f"{i}".zfill(5),
#                 "terminalStatus": 0,
#                 "displayYear": None,
#                 "activationTmeStr": None,
#                 "serviceCode": None,
#                 "remark": None
#             },
#             "cardInfoVO": {
#                 "sim": None,
#                 "iccid": None,
#                 "totalFlow": 0,
#                 "flowType": 2
#             },
#             "customerInfoVO": {
#                 "vehicleType": None,
#                 "engineNo": None,
#                 "frameNo": None,
#                 "owner": None,
#                 "license": None,
#                 "phone": None,
#                 "address": None
#             },
#             "iInstallInfoVO": {
#                 "installPlace": None,
#                 "installPerson": None,
#                 "installRemark": None,
#                 "installDate": "2024-07-09 09:48:01"
#             }
#         }
#         selected_ids.append(selected_id)
#         headers = {
#             "sessionid": f"a13ec2d06b4d4807a21ce3c8946d07d5",
#             "Accept": "*/*",
#             "Accept-Encoding": "gzip, deflate, br",
#             "User-Agent": "PostmanRuntime-ApipostRuntime/1.1.0",
#             "Connection": "keep-alive",
#             "Content-Type": "application/json"
#         }
#
#         response = requests.request("POST", url, json=payload, headers=headers)
#         print(response.text)
#         if selected_ids.count(selected_id) == int(shu):
#             group_ids.remove(selected_id)
#         print("剩余的组ID：", group_ids)
#
#
# # 创建两个线程
# from concurrent.futures import ThreadPoolExecutor
#
# # 创建一个线程池，包含两个线程
# with ThreadPoolExecutor(max_workers=5) as executor:
#     # 将任务提交给线程池
#     executor.submit(print_numbers, 0, 2000)
#     executor.submit(print_numbers, 2000, 4000)
#     executor.submit(print_numbers, 4000, 6000)
#     executor.submit(print_numbers, 6000, 8000)
#     executor.submit(print_numbers, 8000, 10000)
