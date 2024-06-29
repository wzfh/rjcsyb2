import uiautomator2 as u2
import time
import os, random
from io import BytesIO
from PIL import Image, ImageChops, ImageStat
import smtplib
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from datetime import datetime

try:
    device = os.popen("adb devices").readlines()
    device_id = device[1]
    d = u2.connect_usb(f'{device_id.split()[0]}')
    print(device_id.split())
    if device_id.split()[1] != 'device':
        print('设备连接失败')
        os.system('adb  kill-server')
        os.system('adb  devices')
except AttributeError:
    os.system('adb  kill-server')
    os.system('adb  devices')
package_name = "com.tencent.wework"
activity_name = "com.tencent.wework.launch.LaunchSplashActivity"
sender_email = "1114377437@qq.com"
sender_password = "usnxlmvexcboiagh"
recipient_email = "1114377437@qq.com"
msg = MIMEMultipart()
msg['From'] = sender_email
msg['To'] = recipient_email
zhu下班_image = Image.open("img/zhu下班.jpg")
zhu上班_image = Image.open("img/zhu上班.jpg")
今日打卡已完成_image = Image.open("img/今日打卡已完成.jpg")
上班正常_image = Image.open("img/上班·正常.jpg")
上班自动打卡_image = Image.open("img/上班自动打卡·正常.jpg")
下班自动打卡_image = Image.open("img/上班自动打卡·正常.jpg")
下班正常_image = Image.open("img/下班·正常.jpg")


def remove_whitespace(text):
    return text.replace('\n', '').replace(' ', '').strip()


def 识别图片2(file_path):
    import pytesseract
    pytesseract.pytesseract.tesseract_cmd = r'C:\Users\rjcsyb2\Desktop\Tesseract-OCR\tesseract.exe'
    image_text = pytesseract.image_to_string(Image.open(file_path), lang='chi_sim')
    text_with = remove_whitespace(image_text)
    print(text_with)
    return text_with


def 打开应用():
    global d
    try:
        os.system('adb shell input keyevent 224')
        os.system(r'adb push C:\Users\rjcsyb2\Desktop\atx-agent_0.10.0_linux_armv7\atx-agent /data/local/tmp')
        os.system('adb shell chmod 755 /data/local/tmp/atx-agent')
        os.system('adb shell /data/local/tmp/atx-agent server -d')
        os.system('adb shell /data/local/tmp/atx-agent server -d --stop')
        print('打开蓝牙')
        os.system('adb shell svc bluetooth enable')
        os.system('adb shell settings put secure location_mode 1')
        print('打开定位')
        d.app_stop(package_name)
        d.press('home')
        time.sleep(2)
        d.app_start(package_name)
        print("启动企业微信成功")
        time.sleep(3)
        d(text="工作台").click()
        print("点击工作台")
        time.sleep(2)
        d.swipe(930, 1480, 980, 480)
        d(text="打卡").click()
        print("点击打卡")
    except:
        os.system('python -m uiautomator2 init')
        d.app_start(package_name)
        print("启动企业微信成功")
        d(text="工作台").click()
        print("点击工作台")
        time.sleep(2)
        d.swipe(930, 1480, 980, 480)
        d(text="打卡").click()
        print("点击打卡")


def is_similar(image1, image2):
    diff = ImageChops.difference(image1, image2)
    stat = ImageStat.Stat(diff)
    return stat.mean[0] < 10 and stat.mean[1] < 10 and stat.mean[2] < 10


def 截图():
    global region_image
    time.sleep(3)
    imge = d.screenshot()
    region_image = imge.crop((86, 646, 940, 1427))
    if os.path.exists('img/bei.jpg'):
        os.remove('img/bei.jpg')
        print("文件 bei.jpg 已被成功删除.")
    time.sleep(3)
    print('重新截取屏幕')
    region_image.save('img/bei.jpg')
    识别图片2('img/bei.jpg')


def email():
    d.app_stop(package_name)
    print('关闭蓝牙')
    os.system('adb shell svc bluetooth disable')
    print('关闭定位')
    os.system('adb shell settings put secure location_mode 0')
    os.system('adb shell input keyevent 26')
    print('息屏')
    msg['Subject'] = f"{识别图片2('img/bei.jpg')}"
    with open('img/bei.jpg', "rb") as attachment:
        part = MIMEApplication(attachment.read(), _subtype='png')
        part.add_header('Content-Disposition', 'attachment', filename='img/bei.jpg')
        msg.attach(part)
    with smtplib.SMTP_SSL('smtp.qq.com', 465) as smtp:
        smtp.login(sender_email, sender_password)
        smtp.sendmail(sender_email, recipient_email, msg.as_string())


def 上班():
    print('上班')
    打开应用()
    while True:
        截图()
        if is_similar(zhu上班_image, region_image):
            d.click(520, 1430)
            print('上班打卡成功')
            time.sleep(3)
            截图()
            d.app_stop(package_name)
            email()
            break
        if is_similar(上班正常_image, region_image):
            print('上班正常成功')
            截图()
            d.app_stop(package_name)
            email()
            break
        if is_similar(zhu下班_image, region_image):
            print('已打上班卡成功')
            d.app_stop(package_name)
            email()
            break
        if is_similar(上班自动打卡_image, region_image):
            print('自动上班打卡成功')
            d.app_stop(package_name)
            email()
            break
        time.sleep(5)


def 下班():
    print('下班')
    打开应用()
    while True:
        try:
            截图()
            if is_similar(下班正常_image, region_image):
                print('下班正常成功')
                d.app_stop(package_name)
                email()
                break
            if is_similar(zhu下班_image, region_image):
                d.click(520, 1430)
                print('下班打卡成功')
                time.sleep(3)
                截图()
                d.app_stop(package_name)
                email()
                break
            if is_similar(今日打卡已完成_image, region_image):
                print('今日打卡已完成')
                d.app_stop(package_name)
                email()
                break
            if is_similar(下班自动打卡_image, region_image):
                print('下班自动上班打卡成功')
                d.app_stop(package_name)
                email()
                break
            time.sleep(5)
        except:
            os.system('adb  kill-server')
            os.system('adb  devices')


now = datetime.now()
current_time = now.strftime("%H:%M")
print(current_time)


# import sys
#
# log1 = os.getcwd() + "\\log.out"
# print(log1)
# f = open(log1, 'w')
# sys.stdout = f
# sys.stderr = f
def run():
    now = datetime.now()
    current_time = now.strftime("%H:%M")
    print(current_time)
    if current_time < "09:00":
        上班()
    if current_time > "17:30":
        下班()


if __name__ == "__main__":
    if "06：20" < current_time < "09:00":
        run()
    elif "17：40" < current_time:
        run()
    else:
        from apscheduler.schedulers.blocking import BlockingScheduler

        sched = BlockingScheduler(timezone='Asia/Shanghai')
        print('等待打卡计划时间')
        sched.add_job(run, 'cron', day_of_week='mon-sat', hour='06', minute='00', second='00')
        sched.add_job(下班, 'cron', day_of_week='sat', hour='12', minute='00', second='01')
        sched.add_job(run, 'cron', day_of_week='mon-fri', hour='17', minute='30', second='01')
        # 每天的20:30:00执行一次
        sched.start()

    # imge = d.screenshot()
    # region_image = imge.crop((86, 646, 940, 1427))
    # if os.path.exists('img/ces1.jpg'):
    #     os.remove('img/ces1.jpg')
    #     print("\n文件 ces1.jpg 已被成功删除.")
    # time.sleep(3)
    # region_image.save('img/ces1.jpg')
    # print('\n重新截取屏幕')
