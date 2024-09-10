# import cv2
# cap = cv2.VideoCapture(0)
# if not cap.isOpened():
#     print("Cannot open camera")
#     exit()
# while True:
#     ret, frame = cap.read()
#     if not ret:
#         print("Cannot receive frame")
#         break
#     frame = cv2.resize(frame,(540,320))              # 縮小尺寸，避免尺寸過大導致效能不好
#     cv2.imshow('oxxostudio', frame)
#     if cv2.waitKey(1) == ord('q'):
#         break
# cap.release()
# cv2.destroyAllWindows()
###-----------------------
# import dlib
# import cv2
#
# # 選擇第一隻攝影機
# # cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
# cap = cv2.VideoCapture(r'C:\Users\Hcedu\Downloads\53a9a199-41fc-4cd4-bca6-337a3a146f1c.xvid.aac.mp4')
#
# # 調整預設影像大小，預設值很大，很吃效能
# # cap.set(cv2. CAP_PROP_FRAME_WIDTH, 1000)
# # cap.set(cv2. CAP_PROP_FRAME_HEIGHT, 1000)
#
# # 取得預設的臉部偵測器
# detector = dlib.get_frontal_face_detector()
# # 根據shape_predictor方法載入68個特徵點模型，此方法為人臉表情識別的偵測器
# predictor = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')
#
# # 當攝影機打開時，對每個frame進行偵測
#
# while True: #infinite loop
#     # 讀出frame資訊
#     _, frame = cap.read()
#     # frame = cv2.flip(frame,0)
#
#     img_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#     face_rects = detector(img_gray, 0)
#
#     # 取出偵測的結果
#     for d in face_rects:
#         x1 = d.left()
#         y1 = d.top()
#         x2 = d.right()
#         y2 = d.bottom()
#
#         # 繪製出偵測人臉的矩形範圍
#         cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2, cv2.LINE_AA)
#
#         # 找出特徵點位置
#         shape = predictor(img_gray, d)
#
#         # 繪製68個特徵點
#         for i in range(68):
#             cv2.circle(frame, (shape.part(i).x, shape.part(i).y), 2, (128, 128, 128), 2)
#
#     # 輸出到畫面
#     cv2.namedWindow('Face Detection', 0)
#     cv2.imshow("Face Detection", frame)
#
#     # 如果按下ESC键，就退出
#     if cv2.waitKey(10) == 27:
#         break
#
# # 釋放記憶體
# cap.release()
# # 關閉所有視窗
# cv2.destroyAllWindows()
##-------------------
# 使用dlib人臉識別模組 自動處理
import os
import numpy as np
import cv2                #影像處理模組 OpenCV
import dlib               #人臉識別模組 dlib

path = r'.\照片'

name_list = []
for root, dirs, files in os.walk(path):  #找路徑
    for file in files:
        name_list.append(os.path.join(root, file))

print(name_list) #['.\\照片\\01-楊佳錩.jpg', '.\\照片\\02-童建凱.jpg'


# dlib
detector = dlib.get_frontal_face_detector()    # 使用dlib模組提供的人臉偵測函式，基於HOG特徵，建立找尋人臉的物件
predictor = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')
# 人臉68個特徵形狀預測物件的產生，是基于 Ensemble of Regression Trees 理論

# cv2.imdecode解碼 (np.fromfile讀中文檔名)-> ndarray
def cv2_imread(filePath):
    cv_img = cv2.imdecode( np.fromfile(filePath,dtype=np.uint8) , cv2.IMREAD_UNCHANGED )
    return cv_img

for name in name_list :

    img = cv2_imread(name)
    # 取灰度
    img_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    # 先看到人臉在甚麼地方
    rects = detector(img_gray, 1) # 人臉方框的矩形左上右下座標

    #print(dir(rects[0]))  # <class '_dlib_pybind11.rectangle'> 物件
    # 'area', 'bl_corner', 'bottom', 'br_corner', 'center', 'contains', 'dcenter', 'height',
    # 'intersect', 'is_empty', 'left', 'right', 'tl_corner', 'top', 'tr_corner', 'width'

    img1 = img[rects[0].top():rects[0].bottom(), rects[0].left():rects[0].right()] #crop

    path = name[:-4]+'1.jpg'
    #print(path)  # ./113市府AI技術應用與自動控制培訓班(個人大頭照)/劉凡綺1.jpg
    cv2.imencode('.jpg',img1)[1].tofile(path) #cv2.imencode存檔