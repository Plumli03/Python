# 人臉辨識動態

import dlib,numpy
from PIL import Image, ImageDraw, ImageFont
import pickle
import cv2

font_file = r"C:\Users\Hcedu\Desktop\python\老師zip\NotoSansTC-Regular.ttf"  # 思源黑體
_font = ImageFont.truetype(font_file,12) # PIL

def print_array_details(a):
    print('Dimensions: %d, shape: %s, dtype: %s' % (a.ndim, a.shape, a.dtype))

pickle_file1=r'C:\Users\Hcedu\Desktop\python\照片\'
pickle_file2='./原始大頭照/staff_candidate.pickle'

with open(pickle_file1, 'rb') as f1:
    descriptors = pickle.load(f1)  # 載入 30 個 基準人頭的特徵矩陣，每一個元素都是 numpy

with open(pickle_file2, 'rb') as f2:
    candidate = pickle.load(f2)    # 載入候選人姓名

predictor = "shape_predictor_68_face_landmarks.dat"  #人臉68特徵點模型
recogmodel = "dlib_face_recognition_resnet_model_v1.dat"  #人臉辨識模型

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor(predictor)
facerec = dlib.face_recognition_model_v1(recogmodel)  #讀入人臉辨識模型

cap = cv2.VideoCapture('vtest1.x264.aac.mp4')     # 讀取電腦攝影機鏡頭影像
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))    # 取得影像寬度
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))  # 取得影像高度

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 30.0, (width,  height))  # 產生空的影片，fps=30
if not cap.isOpened():
    print("Cannot open camera")
    exit()
while True:
    ret, frame = cap.read()
    if not ret:
        print("Cannot receive frame")
        break
    imgObj = Image.fromarray(frame)  # 產生一個 ImageObject
    rects = detector(frame, 1)       # 讀到了一個畫面

    dist = []
    dict_face_dist = {}
    for n, d in enumerate(rects):
        shape = predictor(frame, d)  # 特徵點偵測
        feature = facerec.compute_face_descriptor(frame, shape)  # 取得128維特徵向量
        d_test = numpy.array(feature)  # 128維特徵向量轉成 numpy
        # 計算歐式距離
        for item in descriptors:
            dist_ = numpy.linalg.norm(item - d_test)
            dist.append(dist_)
        dict_face_dist[n] = [(d.left(), d.top(), d.right(), d.bottom()), dist]
        dist = []
    draw = ImageDraw.Draw(imgObj)
    for n, key in enumerate(dict_face_dist):

        # 將比對人名和比對出來的歐式距離組成一個dict
        c_d = dict(zip(candidate, dict_face_dist[key][1]))
        # 根據歐式距離由小到大排序
        cd_sorted = sorted(c_d.items(), key=lambda d: d[1])
        # 取得最短距離就為辨識出的人名
        rec_name = cd_sorted[0][0] + str(n)
        # rec_name = cd_sorted[0][0] + str(round(cd_sorted[0][1],2))
        print(f'{str(key) + cd_sorted[0][0]:10s} {round(cd_sorted[0][1], 2)}')
        if round(cd_sorted[0][1], 2) <= 0.99:
            left = dict_face_dist[key][0][0]
            top = dict_face_dist[key][0][1]
            right = dict_face_dist[key][0][2]
            bottom = dict_face_dist[key][0][3]
            draw.rectangle(((left, top), (right, bottom)), outline='blue')
            # txt_w, txt_h = draw.textsize(rec_name, font=_font)
            draw.rectangle(((left, bottom), (right, bottom + 20 + 10)), fill='blue', outline='blue')
            draw.text((left + 8, bottom + 5), rec_name, fill='white', font=_font)

    img = numpy.array(imgObj)
    out.write(img)       # 將取得的每一幀圖像寫入空的影片
    cv2.imshow('image processing', img)
    if cv2.waitKey(int(1000/30)) == ord('q'):
        break             # 按下 q 鍵停止
cap.release()
out.release()      # 釋放資源
cv2.destroyAllWindows()