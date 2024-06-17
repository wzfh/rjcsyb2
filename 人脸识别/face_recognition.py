"""
    通过摄像头识别人脸（LBPH识别器（训练的数据，和当前的人脸图片））得到编号。编号和人脸的对应关系，标记人脸和名字并展示画面
    创建识别器，加载训练数据
    读取文件构造编号和人脸的关系
    打开摄像头
    循环取每帧画面
    人脸检测且提取人脸部分
    遍历人脸进行识别
    框出人脸部分且实时展示画面（画面上带有  ）
    关闭摄像头和窗口
"""
import os
import cv2 as cv
from cv2 import face
from hong import *
from train import *
from imput_face import img_extract_faces


def get_color_text(confidence, name):
    if confidence > 85:
        return BGR_RED, "unknown"
    return BGR_GREEN, name


def main():
    # 创建识别器
    recognizer = cv.face.LBPHFaceRecognizer_create()
    recognizer.read(TRAIN_DATA_SAVE_PATH)
    # 读取文件构造编号和人脸的关系。以字典的形式保存编号和人脸名字的关系
    name_map = {int(f.split('.')[0]): f.split('.')[1] for f in os.listdir(IMG_SAVE_PATH)}
    # 打开摄像头
    cap = cv.VideoCapture(0)
    if not cap.isOpened():
        print('连接摄像头失败')

    print("按q退出")

    # 循环取每帧画面
    while True:
        ret, frame = cap.read()
        if not ret:
            print('读取失败')
            break

        # 人脸检测，且提取人脸部分。
        faces, gray = img_extract_faces(frame)
        # 遍历人脸进行识别
        for x, y, w, h in faces:
            img_id, confidence = recognizer.predict(gray[y: y + h, x: x + w])
            # 返回图片编号和置信度。置信度为两张图片的相似程度

            # 框出人脸且实时展示画面
            color, text = get_color_text(confidence, name_map[img_id])
            cv.putText(
                img=frame, text=text, org=(x, y),
                fontFace=cv.FONT_HERSHEY_SIMPLEX, fontScale=FONT_SCALE,
                color=color, thickness=TEXT_THICKNESS
            )
            cv.circle(
                img=frame, center=(x + w // 2, y + h // 2),
                radius=w // 2,
                color=color, thickness=GRAPH_THICKNESS
            )
        cv.imshow(FACE_RECOGNITION_WINDOW_NAME, frame)
        if cv.waitKey(1) == ord('q'):
            break

    # 关闭摄像头，释放空间
    cap.release()
    cv.destroyAllWindows()


if __name__ == '__main__':
    main()