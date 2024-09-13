# import cv2
# import numpy as np
#
# img = cv2.imread(r"C:\Users\rjcsyb2\Desktop\4.jpg")
# new = np.clip(2.0 * img - 160, 0, 255).astype(np.uint8)
# cv2.imwrite(r"C:\Users\rjcsyb2\Desktop\5.jpg", new)


import requests
import os

url = 'http://v3-web.douyinvod.com/ccf9c167c751910568734c8db51c733e/66e292fd/video/tos/cn/tos-cn-ve-15/o07ApXBPiRc1cthm3eCYABnAP8RIENQfgzNcvi/?a=6383&ch=26&cr=3&dr=0&lr=all&cd=0%7C0%7C0%7C3&cv=1&br=1755&bt=1755&cs=0&ds=3&ft=pEaFx4hZffPdh6~kv1zNvAq-antLjrKVvsZ.RkaHxmBEljVhWL6&mime_type=video_mp4&qs=0&rc=N2doNTc6NzhoZGhoOztkZEBpM3Y5cXY5cnR1dTMzNGkzM0BjNi0vXjZjXy8xYDE2LjNgYSNgYi80MmRzNmRgLS1kLWFzcw%3D%3D&btag=c0000e00028000&cquery=100x_100z_100o_100w_100B&dy_q=1726113914&feature_id=aa7df520beeae8e397df15f38df0454c&l=20240912120513A45FF7A885E8A0676463'
file_name = 'video.mp3'
save_path = r'E:\迅雷下载\批量视频去重\视频批量去重剪辑+解析下载\输入视频文件夹\\' + file_name

response = requests.get(url)
with open(save_path, 'wb') as f:
    f.write(response.content)

print(f'视频已成功下载到 {save_path}')
