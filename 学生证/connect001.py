# -*- coding=utf-8-*-
from Crypto.Cipher import AES
from binascii import b2a_hex, a2b_hex
import hashlib
from crcmod import *
from binascii import *
import binascii
import base64
import xlrd
import configparser
import logging
import os
import time
from xlutils.copy import copy
import openpyxl
import xlwt
import pymysql
import socket
from socket import *


def AES_CBC_encrypt(text, key, iv):
    bs = 16
    PADDING = lambda s: s + (bs - len(s) % bs) * chr(bs - len(s) % bs)
    mode = AES.MODE_CBC
    key = bytes.fromhex(key)
    iv = bytes.fromhex(iv)
    cryptos = AES.new(key, mode, iv)

    crypt = cryptos.encrypt(PADDING(text).encode('utf-8'))

    crypted_str = base64.b64encode(crypt)

    return crypted_str


# AES-CBC解密
def AES_CBC_decrypt(text, key, iv):
    key = bytes.fromhex(key)
    iv = bytes.fromhex(iv)
    text = base64.b64decode(text)
    mode = AES.MODE_CBC
    cryptos = AES.new(key, mode, iv)
    plain_text = cryptos.decrypt(text)
    return plain_text


def str_split(str, key):
    aa = str.split("#")
    return aa[key]


import connect

if __name__ == '__main__':
    from tkinter import messagebox

    # ip = "81.71.67.36"
    ip = "119.91.139.137"  # 老人
    # ip = "47.113.121.87"
    # ip = "159.75.222.93"
    port = 7999
    key = "96 B6 71 5E F5 0F A4 55 7F 6C F9 77 17 8E 86 C9"
    iv = "11 C5 00 74 0B E4 4D 4E E5 BD AE D0 3C E7 6F FF"
    res = AES_CBC_encrypt(
        f"{connect.终端上报('睡眠数据上报')}",
        key, iv)
    res0 = str(res, 'utf-8') + "" + "#kdsjafjalsdjg#170"
    res1 = res0.encode('raw_unicode_escape')
    s = socket(AF_INET, SOCK_STREAM)

    print("res加密:%s" % res0.encode('raw_unicode_escape'))
    s.connect((ip, int(port)))
    s.send(res1)
    print(("消息发送成功:%s" % (str(res1))))
    recv_msg = s.recv(1024).decode("utf8")
    print("接收到的信息为:%s" % str(recv_msg))
    aa = str_split(recv_msg, 0)
    res2 = AES_CBC_decrypt(f"{aa}", key, iv)
    import re

    match = re.search(r'\[(.*?)\]', res2.decode('utf-8'))
    if match:
        # 提取匹配到的内容（不包括中括号）
        content_inside_brackets = match.group(1)
        print("解密res1:[%s]" % content_inside_brackets)
    else:
        print("No match found.")
