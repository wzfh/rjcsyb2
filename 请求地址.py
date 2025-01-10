# import requests
# from urllib.parse import urlsplit
#
# # 读取包含多个地址的文件
# with open(r'C:\Users\Administrator\Desktop\新建文本文档.txt', 'r',encoding='utf-8', errors='ignore') as file:
#     urls = file.readlines()
#     # print(urls[1].replace('\n', '').strip())
#
#
# # # 遍历每个URL
# for url in urls:
#     # 去除URL两端的空白字符
#     url = url.replace('\n', '').strip()
#     print(url)
# #
# #     # 检查URL是否有效
# #     if not urlsplit(url).scheme:
# #         print(f"无效的URL: {url}")
# #         continue
# # url="http://10.181.7.68:7405/dc/openapi/getPersonnelIntegrityFileInformation?CXZGZH=440902199409203714&XM=朱康林"
# #     # 发送HTTP请求
#     try:
#         response = requests.get(url, timeout=5)
#         #
#         #     # 检查HTTP响应状态码
#         print(response.text)
#     except:
#         print(f"请求超时：{url}")
#         continue
#
from email.mime.text import MIMEText


def 天气预报():
    import json
    import smtplib

    import requests

    url = "http://api.tanshuapi.com/api/weather/v1/index?key=5bcc683feede6ef8c1ad6026b483a5d7&city=惠州"

    payload = {}
    headers = {
        'User-Agent': 'Apifox/1.0)'
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    data = response.text
    data_dict = json.loads(data)
    # 访问data键并切片
    data1 = data_dict['data']['future'][0]['weather']
    print(data1)

    from email.mime.application import MIMEApplication
    from email.mime.multipart import MIMEMultipart
    # 发件人信息
    sender_email = "1114377437@qq.com"
    sender_password = "usnxlmvexcboiagh"

    # 收件人信息
    recipient_email = "1114377437@qq.com"
    # 构造邮件对象
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = f'{data1}'
    msg.attach(MIMEText(data, 'plain'))

    # 发送邮件
    with smtplib.SMTP_SSL('smtp.qq.com', 465) as smtp:
        smtp.login(sender_email, sender_password)
        smtp.sendmail(sender_email, recipient_email, msg.as_string())


天气预报()
# from apscheduler.schedulers.blocking import BlockingScheduler
#
# sched = BlockingScheduler(timezone='Asia/Shanghai')
# print('等待天气预报计划时间')
# sched.add_job(天气预报, 'cron', hour='06', minute='00', second='00')
# # 每天的20:30:00执行一次
# sched.start()
