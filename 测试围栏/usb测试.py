import time
from io import BytesIO
from PIL import Image, ImageChops, ImageStat
import smtplib
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
import email
from email.message import EmailMessage

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


def email(img):
    msg['Subject'] = f"{识别图片2(f'{img}')}"
    with open(f'{img}', "rb") as attachment:
        part = MIMEApplication(attachment.read(), _subtype='png')
        part.add_header('Content-Disposition', 'attachment', filename=f'{img}')
        msg.attach(part)
    with smtplib.SMTP_SSL('smtp.qq.com', 465) as smtp:
        smtp.login(sender_email, sender_password)
        smtp.sendmail(sender_email, recipient_email, msg.as_string())
        smtp.quit()
    del msg['Subject']
    msg.set_payload([])

    # time.sleep(60)
    # os.remove(f'{img}')


import os

email('img/bei.jpg')
email('img/bei1.jpg')
