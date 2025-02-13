import uiautomator2 as u2
import time
import os, random
from io import BytesIO
from PIL import Image, ImageChops, ImageStat
import smtplib
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from datetime import datetime
import keyboard

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

now = datetime.now()
current_time = now.strftime("%H:%M")
current_directory = os.getcwd()


def remove_whitespace(text):
    return text.replace('\n', '').replace(' ', '').strip()


def on_key_press(event):
    if event.name == 'home':
        上班()
    elif event.name == 'end':
        下班()


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
        device = os.popen("adb devices").readlines()
        device_id = device[1]
        d = u2.connect_usb(f'{device_id.split()[0]}')
        print(device_id.split())
        if device_id.split()[1] != 'device':
            print('设备连接失败')
            os.system('adb  kill-server')
            os.system('adb  devices')
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
        d.swipe(930, 1580, 980, 480)
        d(text="打卡").click()
        print("点击打卡")
    except:
        os.system('adb  kill-server')
        os.system('adb  devices')
        os.system('python -m uiautomator2 init')
        d.app_start(package_name)
        print("启动企业微信成功")
        d(text="工作台").click()
        print("点击工作台")
        time.sleep(2)
        d.swipe(930, 1580, 980, 480)
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
    if os.path.exists('img/bei.jpg'):
        os.remove('img/bei.jpg')
        print("文件 bei.jpg 已被成功删除.")
    region_image = imge.crop((86, 746, 940, 1527))
    print('重新截取屏幕')
    region_image.save('img/bei.jpg')
    识别图片2('img/bei.jpg')
    time.sleep(5)


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
    from smtplib import SMTPResponseException
    try:
        with smtplib.SMTP_SSL('smtp.qq.com', 465) as smtp:
            smtp.login(sender_email, sender_password)
            smtp.sendmail(sender_email, recipient_email, msg.as_string())
    except SMTPResponseException as e:
        print("发生了SMTPResponseException异常")
        print('跳过异常')
        pass
    del msg['Subject']
    msg.set_payload([])


def 上班():
    print('上班')
    打开应用()
    while True:
        try:
            截图()
            if is_similar(zhu上班_image, region_image):
                print('点击上班打卡')
                d.click(520, 1430)
                print('上班打卡成功')
                time.sleep(3)
                截图()
                email()
                break
            # if is_similar(zhu下班_image, region_image):
            #     print('已打上班卡成功')
            #     email()
            #     break
            if is_similar(上班正常_image, region_image):
                print('上班正常成功')
                截图()
                email()
                break
            if is_similar(上班自动打卡_image, region_image):
                print('自动上班打卡成功')
                email()
                break
            if current_time == "07:10":
                d.press("back")
                print('\n返回')
                d(text="打卡").click()
                print("点击打卡")
                continue
            time.sleep(5)
        except:
            # os.system('adb  kill-server')
            # os.system('adb  devices')
            pass


def 下班():
    print('下班')
    打开应用()
    while True:
        try:
            截图()
            if is_similar(下班正常_image, region_image):
                print('下班正常成功')
                email()
                break
            if is_similar(zhu下班_image, region_image):
                print('点击下班打卡')
                d.click(520, 1430)
                print('下班打卡成功')
                time.sleep(3)
                截图()
                email()
                break
            if is_similar(今日打卡已完成_image, region_image):
                print('今日打卡已完成')
                email()
                break
            if is_similar(下班自动打卡_image, region_image):
                print('下班自动上班打卡成功')
                email()
                break
            if current_time == "18:10":
                d.press("back")
                print('\n返回')
                d(text="打卡").click()
                print("点击打卡")
                continue
            time.sleep(5)
        except:
            os.system('adb  kill-server')
            os.system('adb  devices')


def run():
    now = datetime.now()
    current_time = now.strftime("%H:%M")
    print(current_time)
    os.system('adb shell input keyevent 26')
    if current_time < "09:00":
        上班()
    if current_time > "17:29":
        下班()


def 截图测试():
    global d
    device = os.popen("adb devices").readlines()
    device_id = device[1]
    d = u2.connect_usb(f'{device_id.split()[0]}')
    time.sleep(5)
    imge = d.screenshot()
    if os.path.exists('img/bei.jpg'):
        os.remove('img/bei.jpg')
        print("文件 bei.jpg 已被成功删除.")
    region_image = imge.crop((86, 746, 940, 1527))
    print('重新截取屏幕')
    region_image.save('img/bei.jpg')
    识别图片2('img/bei.jpg')



if __name__ == "__main__":
    from apscheduler.schedulers.blocking import BlockingScheduler

    #
    sched = BlockingScheduler(timezone='Asia/Shanghai')
    print('等待打卡')
    keyboard.on_press(on_key_press)
    sched.add_job(run, 'cron', day_of_week='mon-sat', hour='07', minute=f'0{random.randint(5, 9)}', second='00',
                  misfire_grace_time=3600)
    sched.add_job(下班, 'cron', day_of_week='sat', hour='12', minute=f'00', second='00', misfire_grace_time=3600)
    sched.add_job(run, 'cron', day_of_week='mon-fri', hour='17', minute=f'30', second='00', misfire_grace_time=3600)
    sched.start()
    # 截图测试()
    # 识别图片2('img/上班自动打卡·正常.jpg')
