# _*_ coding:utf-8 _*_

import re
import time


def get_bcc(inputStr: str) -> str:
    bcc = 0
    for i in inputStr.split(' '):
        bcc = bcc ^ int(i, 16)

    return f'{bcc:x}'


def get_xor(data):
    result = re.sub(r"(?<=\w)(?=(?:\w\w)+$)", " ", data)
    return result


"""
7E                   协议头
6021                 消息ID
L1 L2                 消息属性
013000008888         手机号
0005                 流水号
200608202135         时间2020年6月8号20点21分35秒
0003                 BMS协议版本指令
L3 L4                 L3 L4为BMS数据长度
02                   有2个TLV包
2802015E             TLV包，寄存器地址为0x28，数据长度为2，数据内容为350
29027530             TLV包，寄存器地址为0x29，数据长度为2，数据内容为7530
OR                   异或校验
7E                    协议尾
"""


def time16():
    ti = time.strftime("%Y%m%d%H%M%S")
    ti2 = str(ti)
    ti3 = 2 * '' + ti2[2:]
    ti4 = (hex(int(ti3[0:2]))[2:4]).zfill(2)
    ti5 = (hex(int(ti3[2:4]))[2:4]).zfill(2)
    ti6 = (hex(int(ti3[4:6]))[2:4]).zfill(2)
    ti7 = (hex(int(ti3[6:8]))[2:4]).zfill(2)
    ti8 = (hex(int(ti3[8:10]))[2:4]).zfill(2)
    ti9 = (hex(int(ti3[10:12]))[2:4]).zfill(2)
    ti10 = ti4 + ti5 + ti6 + ti7 + ti8 + ti9
    return ti10


# def bms():
协议头 = '7E'
消息ID = '6821'
手机号 = '13000008888'.zfill(12)
流水号 = '0001'
时间 = f"{time.strftime('%Y%m%d%H%M%S', time.localtime())[2:]}"
BMS协议版本指令 = '0004'
TLV包数 = '5A'
TLV包1 = '1A020DDE'
TLV包2 = '2102003C'
TLV包3 = '2802015E'
TLV包4 = '29027530'
TLV包5 = '2A020320'
TLV包6 = '2B020001'
TLV包7 = '2C020001'
TLV包8 = '2D02003C'
TLV包9 = '2E020028'
TLV包10 = '2F020001'
TLV包11 = '30020001'
TLV包12 = '31020003'
TLV包13 = '32020003'
TLV包14 = '33020004'
TLV包15 = '34020001'
TLV包16 = '35020001'
TLV包17 = '36020001'
TLV包18 = '37020001'
TLV包19 = '38020001'
TLV包20 = '39020001'
TLV包21 = '3A022233'
TLV包22 = '3B023303'
TLV包23 = '3C020F84'
TLV包24 = '3D028507'
TLV包25 = '3E020001'
TLV包26 = '3F020001'

TLV包27 = '40027530'
TLV包28 = '4102001E'
TLV包29 = '4202003C'
TLV包30 = '48020E42'
TLV包31 = '63020000'
TLV包32 = '64020001'

TLV包33 = F'6506{time16()}'
TLV包34 = F'6806{time16()}'

TLV包35 = F'80020001'
TLV包36 = F'81020001'
TLV包37 = F'82020001'
TLV包38 = F'83020001'
TLV包39 = F'84020001'
TLV包40 = F'85020001'
TLV包41 = F'86020001'
TLV包42 = F'87020001'
TLV包43 = F'88020001'
TLV包44 = F'89020000'

TLV包45 = F'8A020009'
TLV包46 = F'8B02015E'
TLV包47 = F'8C02015E'
TLV包48 = F'8D02015E'
TLV包49 = F'8E02015E'
TLV包50 = F'8F02015E'

TLV包51 = F'9002015E'
TLV包52 = F'9102015E'
TLV包53 = F'9202015E'
TLV包54 = F'93027530'
TLV包55 = F'94027530'
TLV包56 = F'95027530'
TLV包57 = F'96027530'
TLV包58 = F'9702003C'
TLV包59 = F'9802003C'
TLV包60 = F'9902003C'

TLV包61 = F'9A02003C'
TLV包62 = F'9B02003C'
TLV包63 = F'9C02003C'
TLV包64 = F'9D02003C'
TLV包65 = F'9E02003C'
TLV包66 = F'9F020001'

TLV包67 = F'A0020001'
TLV包68 = F'A102003C'
TLV包69 = F'A202003C'
TLV包70 = F'A3020001'
TLV包71 = F'A4020001'
TLV包72 = F'A5020001'
TLV包73 = F'A6020001'
TLV包74 = F'A7020001'
TLV包75 = F'A802003C'
TLV包76 = F'A9025431'

TLV包77 = F'CC04{time16()[:-6]}00'
TLV包78 = F'CF020001'
TLV包79 = F'D0020001'
TLV包80 = F'D1020001'
TLV包81 = F'D2020000'
TLV包82 = F'D406{time16()}'
TLV包83 = F'D702000A'
TLV包84 = F'D8020001'
TLV包85 = F'D9020001'

TLV包86 = F'DA02015E'
TLV包87 = F'DB02015E'
TLV包88 = F'DC02015E'
TLV包89 = F'DD020001'
TLV包90 = F'DE02015E'
tlv_packages = [
    '1A020DDE', '2102003C', '2802015E', '29027530', '2A020320', '2B020001', '2C020001', '2D02003C', '2E020028',
    '2F020001',
    '30020001', '31020003', '32020003', '33020004', '34020001', '35020001', '36020001', '37020001', '38020001',
    '39020001',
    '3A022233', '3B023303', '3C020F84', '3D028507', '3E020001', '3F020001', '40027530', '4102001E', '4202003C',
    '48020E42',
    '63020000', '64020001', f'6506{time16()}', f'6806{time16()}', '80020001', '81020001', '82020001', '83020001',
    '84020001',
    '85020001', '86020001', '87020001', '88020001', '89020000', '8A020009', '8B02015E', '8C02015E', '8D02015E',
    '8E02015E',
    '8F02015E', '9002015E', '9102015E', '9202015E', '93027530', '94027530', '95027530', '96027530', '9702003C',
    '9802003C',
    '9902003C', '9A02003C', '9B02003C', '9C02003C', '9D02003C', '9E02003C', '9F020001', 'A0020001', 'A102003C',
    'A202003C',
    'A3020001', 'A4020001', 'A5020001', 'A6020001', 'A7020001', 'A802003C', 'A9025431', f'CC04{time16()[:-6]}00',
    'CF020001',
    'D0020001', 'D1020001', 'D2020000', f'D406{time16()}', 'D702000A', 'D8020001', 'D9020001', 'DA02015E', 'DB02015E',
    'DC02015E', 'DD020001', 'DE02015E'
]

combined_tlv_packages = ''.join(tlv_packages)
print(combined_tlv_packages)

BMS数据长度 = f'{hex(int(len(TLV包数 + TLV包1 + TLV包2 + TLV包3 + TLV包4 + TLV包5 + TLV包6 + TLV包7 + TLV包8 + TLV包9 + TLV包10 + TLV包11 + TLV包12 + TLV包13 + TLV包14 + TLV包15 + TLV包16 + TLV包17 + TLV包18 + TLV包19 + TLV包20 + TLV包21 + TLV包22 + TLV包23 + TLV包24 + TLV包25 + TLV包26 + TLV包27 + TLV包28 + TLV包29 + TLV包30 + TLV包31 + TLV包32 + TLV包33 + TLV包34 + TLV包35 + TLV包36 + TLV包37 + TLV包38 + TLV包39 + TLV包40 + TLV包41 + TLV包42 + TLV包43 + TLV包44 + TLV包45 + TLV包46 + TLV包47 + TLV包48 + TLV包49 + TLV包50 + TLV包51 + TLV包52 + TLV包53 + TLV包54 + TLV包55 + TLV包56 + TLV包57 + TLV包58 + TLV包59 + TLV包60 + TLV包61 + TLV包62 + TLV包63 + TLV包64 + TLV包65 + TLV包66 + TLV包67 + TLV包68 + TLV包69 + TLV包70 + TLV包71 + TLV包72 + TLV包73 + TLV包74 + TLV包75 + TLV包76 + TLV包77 + TLV包78 + TLV包79 + TLV包80 + TLV包81 + TLV包82 + TLV包83 + TLV包84 + TLV包85 + TLV包86 + TLV包87 + TLV包88 + TLV包89 + TLV包90) / 2))[2:]}'.zfill(
    4)
print(BMS数据长度)
消息属性 = f'{hex(int(len(时间 + BMS协议版本指令 + BMS数据长度 + TLV包数 + TLV包1 + TLV包2 + TLV包3 + TLV包4 + TLV包5 + TLV包6 + TLV包7 + TLV包8 + TLV包9 + TLV包10 + TLV包11 + TLV包12 + TLV包13 + TLV包14 + TLV包15 + TLV包16 + TLV包17 + TLV包18 + TLV包19 + TLV包20 + TLV包21 + TLV包22 + TLV包23 + TLV包24 + TLV包25 + TLV包26 + TLV包27 + TLV包28 + TLV包29 + TLV包30 + TLV包31 + TLV包32 + TLV包33 + TLV包34 + TLV包35 + TLV包36 + TLV包37 + TLV包38 + TLV包39 + TLV包40 + TLV包41 + TLV包42 + TLV包43 + TLV包44 + TLV包45 + TLV包46 + TLV包47 + TLV包48 + TLV包49 + TLV包50 + TLV包51 + TLV包52 + TLV包53 + TLV包54 + TLV包55 + TLV包56 + TLV包57 + TLV包58 + TLV包59 + TLV包60 + TLV包61 + TLV包62 + TLV包63 + TLV包64 + TLV包65 + TLV包66 + TLV包67 + TLV包68 + TLV包69 + TLV包70 + TLV包71 + TLV包72 + TLV包73 + TLV包74 + TLV包75 + TLV包76 + TLV包77 + TLV包78 + TLV包79 + TLV包80 + TLV包81 + TLV包82 + TLV包83 + TLV包84 + TLV包85 + TLV包86 + TLV包87 + TLV包88 + TLV包89 + TLV包90) / 2))[2:]}'.zfill(
    4)
print(消息属性)
c = get_xor(
    消息ID + 消息属性 + 手机号 + 流水号 + 时间 + BMS协议版本指令 + BMS数据长度 + TLV包数 + combined_tlv_packages)
异或校验 = f'{get_bcc(c)}'.zfill(2)
协议尾 = '7E'
data = 协议头 + 消息ID + 消息属性 + 手机号 + 流水号 + 时间 + BMS协议版本指令 + BMS数据长度 + TLV包数 + combined_tlv_packages + 异或校验 + 协议尾
print(get_xor(data).upper())
print(data.upper())

# if __name__ == '__main__':
#     data = '6821001301300000888800052408311123320004A3A4022802015E29027530'
#     q = '7e0b03003f1033057751830002000000000000000000000000000000000000002306271723003131313131313131313131313131313132323232323232323232323232323232323232c66666747e'
#     # print(q.upper())
#     a = get_xor(data)
#     print(a)
#     b = get_bcc(a)
#     print(b)
# print(b)
# print(a)
# now_time = time.strftime('%Y%m%d%H%M%S', time.localtime())
# print(now_time[2:])
