import cv2 as cv
import os
from hong import *
import numpy as np


def main():
    # 获取图片完整路径
    image_paths = [os.path.join(IMG_SAVE_PATH, f) for f in os.listdir(IMG_SAVE_PATH)]
    # 遍历列表中的图片
    faces = [cv.imread(image_path, 0) for image_path in image_paths]

    # 获取训练对象
    img_ids = [int(f.split('.')[0]) for f in os.listdir(IMG_SAVE_PATH)]
    recognizer = cv.face.LBPHFaceRecognizer_create()
    recognizer.train(faces, np.array(img_ids))
    print(faces, np.array(img_ids))
    # 保存文件
    recognizer.write(TRAIN_DATA_SAVE_PATH)


if __name__ == '__main__':
    main()