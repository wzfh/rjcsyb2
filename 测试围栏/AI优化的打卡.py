import uiautomator2 as u2
import time
import os
import random
from io import BytesIO
from PIL import Image, ImageChops, ImageStat
import smtplib
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from datetime import datetime
import keyboard
import pytesseract
from pathlib import Path

package_name = "com.tencent.wework"


class AutoCheckIn:
    def __init__(self, sender_email, sender_password, recipient_email):
        self.sender_email = sender_email
        self.sender_password = sender_password
        self.recipient_email = recipient_email
        self.msg = MIMEMultipart()
        self.msg['From'] = sender_email
        self.msg['To'] = recipient_email

        # 设置正确的图片目录路径
        self.image_dir = Path("测试围栏/img")
        if not self.image_dir.exists():
            self.image_dir.mkdir(parents=True, exist_ok=True)
            print(f"创建图片目录: {self.image_dir}")

        self.load_images()

    def load_images(self):
        try:
            # 使用 Path 对象处理路径
            self.zhu_off_work_image = Image.open(self.image_dir / "zhu下班.jpg")
            self.zhu_on_work_image = Image.open(self.image_dir / "zhu上班.jpg")
            self.today_checked_image = Image.open(self.image_dir / "今日打卡已完成.jpg")
            self.on_work_normal_image = Image.open(self.image_dir / "上班·正常.jpg")
            self.auto_on_work_image = Image.open(self.image_dir / "上班自动打卡·正常.jpg")
            self.auto_off_work_image = Image.open(self.image_dir / "上班自动打卡·正常.jpg")
            self.off_work_normal_image = Image.open(self.image_dir / "下班·正常.jpg")
        except FileNotFoundError as e:
            print(f"错误：找不到图片文件: {e}")
            print(f"请确保以下图片文件存在于目录 {self.image_dir} 中：")
            print("- zhu下班.jpg")
            print("- zhu上班.jpg")
            print("- 今日打卡已完成.jpg")
            print("- 上班·正常.jpg")
            print("- 上班自动打卡·正常.jpg")
            print("- 下班·正常.jpg")
            raise

    def remove_whitespace(self, text):
        return text.replace('\n', '').replace(' ', '').strip()

    def recognize_image(self, file_path):
        pytesseract.pytesseract.tesseract_cmd = r'C:\Users\rjcsyb2\Desktop\Tesseract-OCR\tesseract.exe'
        image_text = pytesseract.image_to_string(Image.open(file_path), lang='chi_sim')
        return self.remove_whitespace(image_text)

    def open_app(self):
        try:
            # 获取设备列表
            devices = os.popen("adb devices").readlines()
            # 移除第一行（标题行）
            devices = [d.strip() for d in devices[1:] if d.strip()]

            if not devices:
                raise Exception("未检测到设备")

            # 使用第一个连接的设备
            device_id = devices[0].split()[0]
            device_status = devices[0].split()[1]

            if device_status != 'device':
                raise Exception(f'设备状态异常: {device_status}')

            # 初始化设备连接
            self.d = u2.connect_usb(device_id)
            print(f"成功连接设备: {device_id}")

            self.prepare_device()
            self.launch_wechat()
        except Exception as e:
            print(f"连接设备失败: {e}")
            self.handle_device_error()

    def prepare_device(self):
        os.system('adb shell input keyevent 224')
        os.system(r'adb push C:\Users\rjcsyb2\Desktop\atx-agent_0.10.0_linux_armv7\atx-agent /data/local/tmp')
        os.system('adb shell chmod 755 /data/local/tmp/atx-agent')
        os.system('adb shell /data/local/tmp/atx-agent server -d')
        os.system('adb shell /data/local/tmp/atx-agent server -d --stop')
        self.enable_bluetooth_and_location()

    def enable_bluetooth_and_location(self):
        os.system('adb shell svc bluetooth enable')
        os.system('adb shell settings put secure location_mode 1')
        print('打开蓝牙和定位')

    def launch_wechat(self):
        self.d.app_stop("com.tencent.wework")
        self.d.press('home')
        time.sleep(2)
        self.d.app_start("com.tencent.wework")
        print("启动企业微信成功")
        time.sleep(3)
        self.d(text="工作台").click()
        print("点击工作台")
        time.sleep(2)
        self.d.swipe(930, 1580, 980, 480)
        self.d(text="打卡").click()
        print("点击打卡")

    def handle_device_error(self):
        try:
            print("尝试重新连接设备...")
            # 重置 ADB 服务
            os.system('adb kill-server')
            time.sleep(2)
            os.system('adb start-server')
            time.sleep(2)

            # 重新初始化 uiautomator2
            os.system('python -m uiautomator2 init')
            time.sleep(3)

            # 重新连接设备
            devices = os.popen("adb devices").readlines()
            devices = [d.strip() for d in devices[1:] if d.strip()]

            if not devices:
                raise Exception("重新连接失败：未检测到设备")

            device_id = devices[0].split()[0]
            self.d = u2.connect_usb(device_id)
            print(f"重新连接成功: {device_id}")

            self.launch_wechat()
        except Exception as e:
            print(f"处理设备错误失败: {e}")
            print("请检查：")
            print("1. USB 连接是否正常")
            print("2. 手机是否已启用 USB 调试")
            print("3. 是否已授权 USB 调试")
            raise

    def is_similar(self, image1, image2):
        diff = ImageChops.difference(image1, image2)
        stat = ImageStat.Stat(diff)
        return all(mean < 10 for mean in stat.mean)

    def capture_screen(self):
        time.sleep(3)
        image = self.d.screenshot()
        image_path = self.image_dir / 'bei.jpg'
        if os.path.exists(image_path):
            os.remove(image_path)
        region_image = image.crop((86, 746, 940, 1527))
        region_image.save(image_path)
        print('截取屏幕并保存')
        return region_image

    def send_email(self, subject, image_path):
        try:
            self.d.app_stop(package_name)
            print('关闭蓝牙')
            os.system('adb shell svc bluetooth disable')
            print('关闭定位')
            os.system('adb shell settings put secure location_mode 0')
            os.system('adb shell input keyevent 26')
            print('息屏')

            # 确保 image_path 是 Path 对象，但不重复添加目录
            if isinstance(image_path, str):
                image_path = Path(image_path)

            self.msg['Subject'] = subject
            with open(image_path, "rb") as attachment:
                part = MIMEApplication(attachment.read(), _subtype='png')
                part.add_header('Content-Disposition', 'attachment',
                                filename=os.path.basename(str(image_path)))
                self.msg.attach(part)

            with smtplib.SMTP_SSL('smtp.qq.com', 465) as smtp:
                smtp.login(self.sender_email, self.sender_password)
                smtp.sendmail(self.sender_email, self.recipient_email, self.msg.as_string())

        except smtplib.SMTPResponseException as e:
            print("发生了SMTPResponseException异常")
            print('跳过异常')
        finally:
            self.msg.set_payload([])

    def check_in(self, is_on_work):
        print('开始打卡' + ('上班' if is_on_work else '下班'))
        self.open_app()
        while True:
            try:
                region_image = self.capture_screen()
                bei_path = self.image_dir / 'bei.jpg'
                if is_on_work:
                    if self.is_similar(self.zhu_on_work_image, region_image):
                        self.d.click(520, 1430)
                        print('上班打卡成功')
                        self.send_email('上班打卡成功', bei_path)
                        os._exit(0)
                    elif self.is_similar(self.on_work_normal_image, region_image):
                        print('上班正常成功')
                        self.send_email('上班正常成功', bei_path)
                        os._exit(0)
                    elif self.is_similar(self.auto_on_work_image, region_image):
                        print('自动上班打卡成功')
                        self.send_email('自动上班打卡成功', bei_path)
                        os._exit(0)
                    elif self.is_similar(self.zhu_off_work_image, region_image):
                        print('已打上班打卡')
                        self.send_email('已打上班打卡', bei_path)
                        os._exit(0)
                else:
                    if self.is_similar(self.off_work_normal_image, region_image):
                        print('下班正常成功')
                        self.send_email('下班正常成功', bei_path)
                        os._exit(0)
                    elif self.is_similar(self.zhu_off_work_image, region_image):
                        self.d.click(520, 1430)
                        print('下班打卡成功')
                        self.send_email('下班打卡成功', bei_path)
                        os._exit(0)
                    elif self.is_similar(self.today_checked_image, region_image):
                        print('今日已打卡')
                        self.send_email('今日已打卡', bei_path)
                        os._exit(0)
                    elif self.is_similar(self.auto_off_work_image, region_image):
                        print('自动下班打卡成功')
                        self.send_email('自动下班打卡成功', bei_path)
                        os._exit(0)
                time.sleep(5)
            except Exception as e:
                print(e)
                self.handle_device_error()

    def on_work(self):
        self.check_in(is_on_work=True)

    def off_work(self):
        self.check_in(is_on_work=False)

    def run(self):
        now = datetime.now()
        current_time = now.strftime("%H:%M")
        print(current_time)
        if current_time < "09:00":
            self.on_work()
        elif current_time > "17:29":
            self.off_work()


def main():
    sender_email = "1114377437@qq.com"
    sender_password = "usnxlmvexcboiagh"
    recipient_email = "1114377437@qq.com"
    auto_check_in = AutoCheckIn(sender_email, sender_password, recipient_email)

    from apscheduler.schedulers.blocking import BlockingScheduler
    sched = BlockingScheduler(timezone='Asia/Shanghai')
    print('等待打卡')

    def on_key_press(event):
        if event.name == 'home':
            auto_check_in.on_work()
        elif event.name == 'end':
            auto_check_in.off_work()

    keyboard.on_press(on_key_press)
    sched.add_job(auto_check_in.run, 'cron', day_of_week='mon-sat', hour='07', minute=f'0{random.randint(5, 9)}',
                  second='00', misfire_grace_time=3600)
    sched.add_job(auto_check_in.off_work, 'cron', day_of_week='sat', hour='12', minute='00', second='00',
                  misfire_grace_time=3600)
    sched.add_job(auto_check_in.run, 'cron', day_of_week='mon-fri', hour='17', minute='30', second='00',
                  misfire_grace_time=3600)
    sched.start()


if __name__ == "__main__":
    main()
