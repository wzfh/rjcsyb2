import binascii
import csv
import os
import time
import requests
import zipfile
import threading
import tkinter as tk
from tkinter import *
from tkinter.colorchooser import askcolor
from tkinter.ttk import *
import ttkbootstrap as ttk
import win32com.client  # TTS
from tkwebview2.tkwebview2 import WebView2
import webview
from tkinter import messagebox
import sys
import subprocess
import signal
from Crypto.Cipher import AES
from binascii import b2a_hex, a2b_hex
import base64
from concurrent.futures import ThreadPoolExecutor
from tkinter.messagebox import *
import fnmatch


def char_to_hex(char):
    return hex(ord(char))[2:]


def copy(editor, event=None):
    editor.event_generate("<<Copy>>")


def paste(editor, event=None):
    editor.event_generate('<<Paste>>')


def selectAll(editor, event=None):
    editor.tag_add('sel', '1.0', END)


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


# V3校验位
def crc1(data):
    crc = 0xFFFF
    data = binascii.unhexlify(data)

    for pos in data:
        crc ^= pos
        for i in range(8):
            lsb = crc & 0x0001
            crc >>= 1
            if lsb == 1:
                crc ^= 0x8408
    crc ^= 0xffff
    test = hex(crc).upper()
    return test


def get_xor(data):
    result = re.sub(r"(?<=\w)(?=(?:\w\w)+$)", " ", data)
    return result


def get_bcc(inputStr: str) -> str:
    bcc = 0
    for i in inputStr.split(' '):
        bcc = bcc ^ int(i, 16)

    return f'{bcc:x}'


def get_longitude(base_log=None, radius=None):
    radius_in_degrees = radius / 111300
    u = float(random.uniform(0.0, 1.0))
    v = float(random.uniform(0.0, 1.0))
    w = radius_in_degrees * math.sqrt(u)
    t = 2 * math.pi * v
    y = w * math.sin(t)
    longitude = y + base_log
    return str(longitude)[:10]


def get_latitude(base_lat=None, radius=None):
    radius_in_degrees = radius / 111300
    u = float(random.uniform(0.0, 1.0))
    v = float(random.uniform(0.0, 1.0))
    w = radius_in_degrees * math.sqrt(u)
    t = 2 * math.pi * v
    x = w * math.cos(t)
    latitude = x + base_lat
    return str(latitude)[:9]
