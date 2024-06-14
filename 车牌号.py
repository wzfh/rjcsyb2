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
        # elif len(sSim) == 10:
        #     sTemp.append(int(sSim[2:4]))
        #     sTemp.append(int(sSim[4:6]))
        #     sTemp.append(int(sSim[6:8]))
        #     sTemp.append(int(sSim[8:10]))
        #     iHigt = int(sSim[0:2]) - 30
        # elif len(sSim) == 9:
        #     sTemp.append(int(sSim[1:3]))
        #     sTemp.append(int(sSim[3:5]))
        #     sTemp.append(int(sSim[5:7]))
        #     sTemp.append(int(sSim[7:9]))
        #     iHigt = int(sSim[0:1])
        # elif len(sSim) < 9:
        #     sSim = "140" + sSim.zfill(8)
        #     sTemp.append(int(sSim[3:5]))
        #     sTemp.append(int(sSim[5:7]))
        #     sTemp.append(int(sSim[7:9]))
        #     sTemp.append(int(sSim[9:11]))
        #     iHigt = int(sSim[1:3]) - 30
        else:
            return None
        print(iHigt)
        print(sTemp)
        # if (iHigt & 0x8) != 0:
        #     sIp.append(sTemp[0] | 128)
        # else:
        #     sIp.append(sTemp[0])
        if (iHigt & 0x4) != 0:
            sIp.append(sTemp[1] | 128)
        else:
            sIp.append(sTemp[1])
        if (iHigt & 0x2) != 0:
            sIp.append(sTemp[2] | 128)
        else:
            sIp.append(sTemp[2])
        if (iHigt & 0x1) != 0:
            sIp.append(sTemp[3] | 128)
        else:
            sIp.append(sTemp[3])
        ipstr = ""
        for ip in sIp:
            ss = str(hex(ip))[2:].zfill(2)
            ipstr += ss
        print(ipstr.upper())
        print(sIp)
        return ipstr.upper()
    except Exception as e:
        print("设备号转伪ip失败！原因：%s" % e)
        return None
shebeihao2Vip('13585475522')
print( 5 & 0x4)
print(22| 128)
print(128+22)
