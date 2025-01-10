import io
import os
import smtplib
import time
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from PIL import Image
import uiautomator2 as u2

# 发件人信息
sender_email = "1114377437@qq.com"
sender_password = "usnxlmvexcboiagh"

# 收件人信息
recipient_email = "1114377437@qq.com"
# 构造邮件对象
msg = MIMEMultipart()
msg['From'] = sender_email
msg['To'] = recipient_email


def countdown(t):
    for i in range(t):
        print("\r休眠倒计时：%02d" % (t - i) + '秒', end='')
        time.sleep(1)


def click_text(self, str, sq=0):  # 对于无法直接点击的控件写了个函数
    path = d(text=str)[sq]
    x, y = path.center()
    d.click(x, y)
    return str


def run():
    global d
    print("正在连接设备")
    device = os.popen("adb devices").readlines()
    device_id = device[1]
    print(device_id.split()[0])
    d = u2.connect_usb(f'{device_id.split()[0]}')
    if device_id.split()[1] != 'device':
        print('设备连接失败')
        os.system('adb  kill-server')
        os.system('adb  start-server')
        os.system('adb  devices')
        time.sleep(2)
        os.system(r'adb push C:\Users\rjcsyb2\Desktop\atx-agent_0.10.0_linux_armv7/atx-agent /data/local/tmp')
        time.sleep(2)
        os.system('adb shell chmod 755 /data/local/tmp/atx-agent')
        time.sleep(2)
        os.system('adb shell /data/local/tmp/atx-agent server -d')
        time.sleep(2)
        os.system('adb shell /data/local/tmp/atx-agent server -d --stop')
        time.sleep(2)
        job2()
    else:
        job2()


class MY():
    def __init__(self):
        self.file_path = r'C:\Users\rjcsyb2\Desktop\region.png'

    def 截图(self):
        from io import BytesIO
        imge = d.screenshot()
        # x1, y1, x2, y2 = 86, 646, 950, 1527
        # image = Image.open(io.BytesIO(imge))
        region_image = imge.crop((86, 646, 950, 1527))

        if os.path.exists(self.file_path):
            os.remove(self.file_path)
            print(f"\n文件 {self.file_path} 已被成功删除.")
        countdown(3)
        # imge.save('text.png')
        region_image.save(self.file_path)
        print('\n重新截取屏幕')

    def remove_whitespace(self,text):
        return text.replace('\n', '').strip()

    def 识别图片(self):
        # from PIL import Image
        import pytesseract

        pytesseract.pytesseract.tesseract_cmd = r'C:\Users\rjcsyb2\Desktop\Tesseract-OCR\tesseract.exe'

        file_path = self.file_path
        img = Image.open(file_path)
        config = r'-c tessedit_char_whitelist=0123456789 --psm 6'
        self.count1 = pytesseract.image_to_string(img, config=config)
        self.image_text = pytesseract.image_to_string(Image.open(file_path), lang='chi_sim')
        # 打印结果
        print([f'{self.image_text[0:9]}'])
        return [f'{self.image_text[0:9]}']

    def 识别图片1(self):
        # from PIL import Image
        import pytesseract

        pytesseract.pytesseract.tesseract_cmd = r'C:\Users\rjcsyb2\Desktop\Tesseract-OCR\tesseract.exe'

        file_path = r'C:\Users\rjcsyb2\Desktop\region.png'
        img = Image.open(file_path)
        config = r'-c tessedit_char_whitelist=0123456789 --psm 10'
        self.count1 = pytesseract.image_to_string(img, config=config)
        self.image_text = pytesseract.image_to_string(Image.open(file_path), lang='chi_sim')
        # 打印结果
        print([f'{self.image_text[16:20]}'])
        return [f'{self.image_text[16:20]}']

    def 识别图片2(self):
        # from PIL import Image
        import pytesseract

        pytesseract.pytesseract.tesseract_cmd = r'C:\Users\rjcsyb2\Desktop\Tesseract-OCR\tesseract.exe'

        file_path = self.file_path
        img = Image.open(file_path)
        config = r'-c tessedit_char_whitelist=0123456789 --psm 6'
        self.count1 = pytesseract.image_to_string(img, config=config)
        self.image_text = pytesseract.image_to_string(Image.open(file_path), lang='chi_sim')
        self.text_with = self.remove_whitespace(self.image_text)
        # 打印结果
        print(self.text_with)
        # print(self.image_text[:15])
        return self.text_with


def click(text1):
    # d.app_stop_all()
    d.app_stop("com.tencent.mm")
    print('关闭微信')
    d.app_stop("com.tencent.wework")
    print('关闭企业微信')
    d.click(139, 552)
    countdown(5)
    d.app_start("com.tencent.wework")  # 启动应用
    print("\n企业微信应用启动成功")
    countdown(5)
    d(text="工作台").click()
    print('\n找到工作台')
    countdown(2)
    d.swipe(930, 1480, 980, 480)
    click_text(d, '打卡')
    print('\n找到打卡页面')
    countdown(40)
    MY().截图()
    if MY().识别图片() == ['不在打卡范围内\n\n']:
        count = 0
        while True:
            print('\n' + str(count))
            d.press("back")
            print('\n返回')
            click_text(d, '打卡')
            print('点击打卡页面按钮')
            countdown(80)
            d(text=f"{text1}").click_exists(timeout=5.0)
            MY().截图()
            count += 1
            if MY().识别图片() != ['不在打卡范围内\n\n']:
                print("跳出循环")
                break
            continue
    if d(text="上班·正常").exists(timeout=2) or d(text="上班自动打卡·正常").exists(timeout=2):
        print('\n已打上班卡')
        countdown(5)
        MY().截图()
        body1 = MY().识别图片2()
        d.app_stop("com.tencent.mm")
        d.app_stop("com.tencent.wework")
        os.system('adb shell svc bluetooth disable')
        os.system('adb shell settings put secure location_mode 0')
        os.system('adb shell input keyevent 26')
        msg['Subject'] = f'{body1}'
        # msg.attach(MIMEText(body, 'plain'))
        with open(f"{MY().file_path}", "rb") as attachment:
            part = MIMEApplication(attachment.read(), _subtype='png')
            part.add_header('Content-Disposition', 'attachment', filename=MY().file_path)
            msg.attach(part)
        # 发送邮件
        with smtplib.SMTP_SSL('smtp.qq.com', 465) as smtp:
            smtp.login(sender_email, sender_password)
            smtp.sendmail(sender_email, recipient_email, msg.as_string())
        print('关闭蓝牙')
        os.system('adb shell svc bluetooth disable')
        print('关闭定位')
        os.system('adb shell settings put secure location_mode 0')
        # print('退出程序')
        # os._exit(0)
    elif d(text='今日打卡已完成，好好休息').exists(timeout=2):
        print('今日打卡已完成，好好休息')
        countdown(5)
        MY().截图()
        body1 = MY().识别图片2()
        d.app_stop("com.tencent.mm")
        d.app_stop("com.tencent.wework")
        os.system('adb shell svc bluetooth disable')
        os.system('adb shell settings put secure location_mode 0')
        os.system('adb shell input keyevent 26')
        msg['Subject'] = f'{body1}'
        # msg.attach(MIMEText(body, 'plain'))
        with open(f"{MY().file_path}", "rb") as attachment:
            part = MIMEApplication(attachment.read(), _subtype='png')
            part.add_header('Content-Disposition', 'attachment', filename=MY().file_path)
            msg.attach(part)
        # 发送邮件
        with smtplib.SMTP_SSL('smtp.qq.com', 465) as smtp:
            smtp.login(sender_email, sender_password)
            smtp.sendmail(sender_email, recipient_email, msg.as_string())
        print('关闭蓝牙')
        os.system('adb shell svc bluetooth disable')
        print('关闭定位')
        os.system('adb shell settings put secure location_mode 0')
        # print('退出程序')
        # os._exit(0)
    elif MY().识别图片() == ['你已在打卡范围 内']:
        countdown(5)
        if MY().识别图片1() == ['上班打卡']:
            countdown(5)
            d(text="上班打卡").click_exists(timeout=10.0)
            MY().截图()
            body1 = MY().识别图片2()
            d.app_stop("com.tencent.mm")
            d.app_stop("com.tencent.wework")
            os.system('adb shell svc bluetooth disable')
            os.system('adb shell settings put secure location_mode 0')
            os.system('adb shell input keyevent 26')
            msg['Subject'] = f'{body1}'
            with open(f"{MY().file_path}", "rb") as attachment:
                part = MIMEApplication(attachment.read(), _subtype='png')
                part.add_header('Content-Disposition', 'attachment', filename=MY().file_path)
                msg.attach(part)
            # 发送邮件
            with smtplib.SMTP_SSL('smtp.qq.com', 465) as smtp:
                smtp.login(sender_email, sender_password)
                smtp.sendmail(sender_email, recipient_email, msg.as_string())
            print('关闭蓝牙')
            os.system('adb shell svc bluetooth disable')
            print('关闭定位')
            os.system('adb shell settings put secure location_mode 0')
            # print('退出程序')
            # os._exit(0)
        elif MY().识别图片1() == ['下班打卡']:
            countdown(5)
            body1 = MY().识别图片2()
            d.app_stop("com.tencent.mm")
            d.app_stop("com.tencent.wework")
            os.system('adb shell svc bluetooth disable')
            os.system('adb shell settings put secure location_mode 0')
            os.system('adb shell input keyevent 26')
            msg['Subject'] = f'{body1}'
            with open(f"{MY().file_path}", "rb") as attachment:
                part = MIMEApplication(attachment.read(), _subtype='png')
                part.add_header('Content-Disposition', 'attachment', filename=MY().file_path)
                msg.attach(part)
            # 发送邮件
            with smtplib.SMTP_SSL('smtp.qq.com', 465) as smtp:
                smtp.login(sender_email, sender_password)
                smtp.sendmail(sender_email, recipient_email, msg.as_string())
            print('关闭蓝牙')
            os.system('adb shell svc bluetooth disable')
            print('关闭定位')
            os.system('adb shell settings put secure location_mode 0')
            # print('退出程序')
            # os._exit(0)
    else:
        pass
        # os._exit(0)

    # # 添加附件
    # with open(f"{MY().file_path}", "rb") as attachment:
    #     part = MIMEApplication(attachment.read(), _subtype='png')
    #     part.add_header('Content-Disposition', 'attachment', filename=MY().file_path)
    #     msg.attach(part)
    # # 发送邮件
    # with smtplib.SMTP_SSL('smtp.qq.com', 465) as smtp:
    #     smtp.login(sender_email, sender_password)
    #     smtp.sendmail(sender_email, recipient_email, msg.as_string())


def job2():
    time.sleep(2)
    os.system(r'adb push C:\Users\rjcsyb2\Desktop\atx-agent_0.10.0_linux_armv7\atx-agent /data/local/tmp')
    time.sleep(2)
    os.system('adb shell chmod 755 /data/local/tmp/atx-agent')
    time.sleep(2)
    os.system('adb shell /data/local/tmp/atx-agent server -d')
    time.sleep(2)
    os.system('adb shell /data/local/tmp/atx-agent server -d --stop')
    time.sleep(2)
    print('打开蓝牙')
    os.system('adb shell svc bluetooth enable')
    os.system('adb shell settings put secure location_mode 1')
    print('打开定位')
    time.sleep(2)
    for i in range(1):
        print(f'循环次数：{i + 1}')
        click("上班打卡")
        countdown(5)
    d.app_stop("com.tencent.mm")
    print('\n关闭微信')
    d.app_stop("com.tencent.wework")
    print('关闭企业微信')
    print('关闭蓝牙')
    os.system('adb shell svc bluetooth disable')
    print('关闭定位')
    os.system('adb shell settings put secure location_mode 0')
    print('结束程序')
    os.system('adb shell input keyevent 26')


if __name__ == "__main__":
    from apscheduler.schedulers.blocking import BlockingScheduler

    sched = BlockingScheduler(timezone='Asia/Shanghai')
    print('等待早上打卡计划时间')
    sched.add_job(run, 'cron', hour='06', minute='00', second='00')
    # 每天的20:30:00执行一次
    sched.start()
    # run()
    # run()
    # print("正在连接设备")
    # device = os.popen("adb devices").readlines()
    # device_id = device[1]
    # print(device_id.split()[0])
    # d = u2.connect_usb(f'{device_id.split()[0]}')
    # if device_id.split()[1] != 'device':
    #     print('设备连接失败')
    #     os.system('adb  kill-server')
    #     os.system('adb  start-server')
    #     os.system('adb  devices')
    #     time.sleep(2)
    #     os.system(r'adb push C:\Users\rjcsyb2\Desktop\atx-agent_0.10.0_linux_armv7/atx-agent /data/local/tmp')
    #     time.sleep(2)
    #     os.system('adb shell chmod 755 /data/local/tmp/atx-agent')
    #     time.sleep(2)
    #     os.system('adb shell /data/local/tmp/atx-agent server -d')
    #     time.sleep(2)
    #     os.system('adb shell /data/local/tmp/atx-agent server -d --stop')
    #     time.sleep(2)
    #     job2()
    # else:
    #     job2()
    # MY().识别图片2()
