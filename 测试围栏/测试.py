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
今日打卡已完成_image = Image.open("img/今日打卡已完成.jpg")
上班正常_image = Image.open("img/上班·正常.jpg")


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
    print('保存文件 bei.jpg成功')


def email():
    d.app_stop(package_name)
    print('关闭蓝牙')
    os.system('adb shell svc bluetooth disable')
    print('关闭定位')
    os.system('adb shell settings put secure location_mode 0')
    os.system('adb shell input keyevent 26')
    print('息屏')
    msg['Subject'] = f"{识别图片2('img/bei.jpg')}"
    # with open('img/bei.jpg', "rb") as attachment:
    #     part = MIMEApplication(attachment.read(), _subtype='png')
    #     part.add_header('Content-Disposition', 'attachment', filename='img/bei.jpg')
    #     msg.attach(part)
    # with smtplib.SMTP_SSL('smtp.qq.com', 465) as smtp:
    #     smtp.login(sender_email, sender_password)
    #     smtp.sendmail(sender_email, recipient_email, msg.as_string())


def 下班():
    打开应用()
    # 自动打卡_image= Image.open("img/自动打卡.jpg")
    while True:
        截图()
        if is_similar(zhu下班_image, region_image):
            d.click(520, 1430)
            print('下班打卡成功')
            email()
            break
        if is_similar(今日打卡已完成_image, region_image):
            print('今日打卡已完成')
            email()
            break
        time.sleep(5)


def 上班():
    打开应用()
    # zhu上班_image = Image.open("img/zhu上班.jpg")
    # 自动打卡_image= Image.open("img/自动打卡.jpg")
    while True:
        截图()
        # if is_similar(zhu上班_image, region_image):
        #     d.click(520, 1430)
        #     print('上班打卡成功')
        #     break
        # if is_similar(上班正常_image, region_image):
        #     print('上班正常成功')
        #     d.app_stop(package_name)
        #     break
        if is_similar(zhu下班_image, region_image):
            print('已打上班卡成功')
            email()
            break
        # if is_similar(自动打卡_image, region_image):
        #     print('自动上班打卡成功')
        #     break
        time.sleep(5)


import sys

log1 = os.getcwd() + "\\log.out"
print(log1)
f = open(log1, 'w')
sys.stdout = f
sys.stderr = f

if __name__ == "__main__":
    print(f'{datetime.now().hour}:{datetime.now().minute}')
    if datetime.now().hour < 9:
        上班()
    if f'{datetime.now().hour}:{datetime.now().minute}' >= '17:30':
        下班()

# imge = d.screenshot()
# region_image = imge.crop((86, 646, 940, 1427))
# if os.path.exists('img/ces1.jpg'):
#     os.remove('img/ces1.jpg')
#     print("\n文件 ces1.jpg 已被成功删除.")
# time.sleep(3)
# region_image.save('img/ces1.jpg')
# print('\n重新截取屏幕')
