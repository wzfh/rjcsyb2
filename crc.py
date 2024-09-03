import binascii


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


# data='787811010863013865432142010032000001A38B0D0A'
# res=crc1(data)
# print(res)


def shebeihao2Vip(sSim):
    if sSim is None or sSim == "":
        return None
    try:
        sTemp = []
        sIp = []
        if len(sSim) == 11:
            sTemp.append(int(sSim[3:5]))
            sTemp.append(int(sSim[5:7]))
            sTemp.append(int(sSim[7:9]))
            sTemp.append(int(sSim[9:11]))
            iHigt = int(sSim[1:3]) - 30
            print(iHigt)
        elif len(sSim) == 10:
            sTemp.append(int(sSim[2:4]))
            sTemp.append(int(sSim[4:6]))
            sTemp.append(int(sSim[6:8]))
            sTemp.append(int(sSim[8:10]))
            iHigt = int(sSim[0:2]) - 30
            print(iHigt)
        elif len(sSim) == 9:
            sTemp.append(int(sSim[1:3]))
            sTemp.append(int(sSim[3:5]))
            sTemp.append(int(sSim[5:7]))
            sTemp.append(int(sSim[7:9]))
            iHigt = int(sSim[0:1])
            print(iHigt)
        elif len(sSim) < 9:
            sSim = "140" + sSim.zfill(8)
            sTemp.append(int(sSim[3:5]))
            sTemp.append(int(sSim[5:7]))
            sTemp.append(int(sSim[7:9]))
            sTemp.append(int(sSim[9:11]))
            iHigt = int(sSim[1:3]) - 30
            print(iHigt)
        else:
            return None
        print(sTemp)
        if (iHigt & 0x8) != 0:
            sIp.append(sTemp[0] | 128)
            print(sTemp[0] | 128)
        else:
            sIp.append(sTemp[0])
            print(sTemp[0])
        if (iHigt & 0x4) != 0:
            sIp.append(sTemp[1] | 128)
            print(sTemp[1] | 128)
        else:
            sIp.append(sTemp[1])
            print(sTemp[1])
        if (iHigt & 0x2) != 0:
            sIp.append(sTemp[2] | 128)
            print(sTemp[2] | 128)
        else:
            sIp.append(sTemp[2])
            print(sTemp[2])
        if (iHigt & 0x1) != 0:
            sIp.append(sTemp[3] | 128)
            print(sTemp[3] | 128)
        else:
            sIp.append(sTemp[3])
            print(sTemp[3])
        print(sIp)
        ipstr = ""
        for ip in sIp:
            ss = str(hex(ip))[2:].zfill(2)
            ipstr += ss
        print(ipstr.upper())
        return ipstr.upper()
    except Exception as e:
        print("设备号转伪ip失败！原因：%s" % e)
        return None


# shebeihao2Vip('13534912299')

# import os
#
# # 替换为你的文件夹路径
# folder_path = r'C:\Users\rjcsyb2\Desktop\BSJ-协议解析器'
#
# # 获取文件夹内的所有文件名
# # current_directory = os.getcwd()
# # print(current_directory)
# import subprocess
#
# # # 遍历文件名并处理每个文件
# #
# #
# exe = os.path.join(folder_path, 'BSJ_dataParser.exe')
#
# # subprocess.Popen(exe1)
# subprocess.run(exe)
import os


def check_ipv4():
    # 执行ipconfig命令
    result = os.popen('ipconfig').read()
    # print(result)

    # 判断IPv4地址是否为'192.168.10.1'
    if '192.168.130.201' in result:
        return True
    else:
        return False


if __name__ == '__main__':
    data = '7E 68 21 02 0B 01 30 00 00 88 88 00 01 24 09 02 16 49 55 00 04 02 01 7F 00 02 0D 8C 01 02 0D 8E 02 02 0D 93 03 02 0D 91 04 02 0D 90 05 02 0D 90 06 02 0D 93 07 02 0D 92 08 02 0D 90 09 02 0D 90 0A 02 0D 93 0B 02 0D 92 0C 02 0D 8F 0D 02 0D 8E 0E 02 0D 92 0F 02 0D 92 10 02 0D 90 11 02 0D 8F 12 02 0D 93 13 02 0D 92 14 02 0D 8F 15 02 0D 8F 16 02 00 00 17 02 00 00 18 02 00 00 19 02 00 00 1A 02 00 00 1B 02 00 00 1C 02 00 00 1D 02 00 00 1E 02 00 00 1F 02 00 00 20 02 00 00 21 02 00 00 22 02 00 FF 23 02 00 FF 24 02 00 FF 25 02 00 FF 26 02 00 FF 27 02 00 FF 28 02 02 FB 29 02 75 30 2A 02 03 E7 2B 02 0D 93 2C 02 0D 8C 2D 02 00 00 2E 02 00 00 2F 02 00 00 30 02 01 F3 31 02 00 16 32 02 00 02 33 02 00 00 34 02 00 00 35 02 00 00 36 02 00 00 37 02 0D 90 38 02 00 07 39 02 00 00 3A 02 CC 30 3B 02 00 00 3C 02 00 00 3D 02 00 00 3E 02 00 00 3F 02 00 00 40 02 75 30 41 02 00 00 42 02 00 4D 43 02 FF FF 44 02 FF FF 45 02 FF FF 46 02 FF FF 47 02 00 00 48 02 00 00 49 02 00 00 4A 02 00 00 4B 02 00 00 4C 02 00 00 4D 02 00 00 4E 02 00 00 4F 02 00 00 50 02 00 00 51 02 00 00 52 02 00 00 53 02 00 00 54 02 00 00 55 02 00 00 56 02 00 00 57 02 00 00 58 02 00 00 59 02 00 00 5A 02 00 00 5B 02 00 00 5C 02 00 00 5D 02 00 00 5E 02 00 00 5F 02 00 00 60 02 00 00 61 02 00 00 62 02 00 00 63 02 FF FF 64 02 FF FF 65 02 FF FF 66 02 FF FF 67 02 FF FF 68 02 FF FF 69 02 FF FF 6A 02 FF FF 6B 02 FF FF 6C 02 FF FF 6D 02 FF FF 6E 02 FF FF 6F 02 FF FF 70 02 FF FF 71 02 FF FF 72 02 FF FF 73 02 FF FF 74 02 FF FF 75 02 FF FF 76 02 FF FF 77 02 FF FF 78 02 FF FF 79 02 FF FF 7A 02 FF FF 7B 02 FF FF 7C 02 FF FF 7D 01 02 FF FF 7D 02 02 FF FF 7F 02 FF FF FD 7E'
    print(data[2:3])
    if data[2:3] == " ":
        print('格式化')
    else:
        print('weigeshihua1')
