import cv2 as cv
from hong import *
import os


def img_extract_faces(img):  # 将人脸图片转为灰度
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)  # 转成灰度图像
    face_classifier = cv.CascadeClassifier(FACE_CLASSIFIER_PATH)  # 加载级联检测器，人脸特征分类器
    return face_classifier.detectMultiScale(gray, minSize=FACE_MIN_SIZE), gray


def get_image_name(name):  # 获取图片的命名名字，格式：1.lihua.jpg
    # 1.lihua.jpg 格式。如果文件中没有则加入，如果已有则替换
    # 把读出来的图片名称，用字典存，然后用name去字典里面找有没有。
    f = os.listdir(IMG_SAVE_PATH)  # os.listdir(IMG_SAVE_PATH)返回目标路径里的文件列表
    if len(f) == 0:  # 文件列表f的长度为0则表示没有图片，编号为1
        name_number = 1
    else:  # 说明原文件有人脸照片，如果出现相同人脸姓名替换成新的，没有编号为最大值max.name.jpg加入进去。
        name_map = {f.split('.')[1]: int(f.split('.')[0]) for f in os.listdir(IMG_SAVE_PATH)}
        name_number = name_map[name] if name in name_map else max(name_map.values()) + 1
    # return IMG_SAVE_PATH + str(name_number) + "." + name + ".jpg"
    return str(name_number) + "." + name + ".jpg"


def save_face(faces, img, name):  # 保证只有一个人脸出现在画面中
    if len(faces) == 0:
        print('没有检测到人脸，请调整！！！')
    if len(faces) > 1:
        print('检测到多个人脸，请调整！！！')
    x, y, w, h = faces[0]
    # 保存人脸部分，保存到文件夹，格式为 1.李华.jpg 格式。如果文件中没有则加入，如果已有则替换
    cv.imwrite('./data/' + get_image_name(name), img[y: y + h, x: x + w])
    print('录入成功，按 q 键退出')


def main():
    # 人脸录入部分是为了得到人脸的数据，然后后面对人脸进行训练。
    # 人脸数据信息主要有三个部分。1、人脸图片。 2、人脸名字。 3、编号（编号需要和名字需要统一。以为训练数据是拿序号和人脸进行比对）
    # 1、人脸图片（打开摄像头、只取人脸部分、给用户实时展示人脸的画面（把人脸框出来）、保存和退出）
    # 2、人脸名字。（用户输入）
    # 3、编号。（文件名称记录）
    # 打开摄像头
    cap = cv.VideoCapture(0)
    if not cap.isOpened():
        print('连接摄像头失败')

    # 输入人脸的名字
    name = input("请输入姓名：")
    if name == ' ':
        print('姓名不能为空，请重新输入！！！')
    print('姓名输入完成：按 s 保存，按 q 退出。')

    # 循环读取摄像头的每一帧画面,然后识别画面中的人脸，识别后只保存人脸部分，作为训练数据。
    while True:
        ret, frame = cap.read()
        if not ret:
            print('读取失败')
            break

        # 检测人脸，且提取人脸部分。这部分直接使用一个函数封装起来。
        faces, gray = img_extract_faces(frame)

        # 框出人脸
        for x, y, w, h in faces:
            cv.rectangle(
                img=frame, pt1=(x, y), pt2=(x + w, y + h),
                color=BGR_GREEN, thickness=1
            )
        cv.imshow(INPUT_FACE_WINDOWS_NAME, frame)

        # 保存和退出
        k = cv.waitKey(1)
        if k == ord('s'):
            # 保存图像，（只需保存灰度图像）
            save_face(faces, gray, name)
        elif k == ord('q'):
            break

    # 释放内存
    cap.release()
    cv.destroyAllWindows()


if __name__ == '__main__':
    main()

