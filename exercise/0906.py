# 將每一位同學的人臉特徵記下來

import os
import dlib,cv2,numpy
import pickle

def cv2_imread(filepath) :
    cv_img = cv2.imdecode( numpy.fromfile(filepath,dtype=numpy.uint8) , cv2.IMREAD_UNCHANGED )
    return cv_img

predictor = "shape_predictor_68_face_landmarks.dat"  #人臉68特徵點模型
recogmodel = "dlib_face_recognition_resnet_model_v1.dat"  #人臉辨識模型

face_folder_path = r"./原始大頭照"  # 內存使用中文姓名為檔名的 30 個 jpg 檔

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor(predictor)
facerec = dlib.face_recognition_model_v1(recogmodel)  #讀入人臉辨識模型

descriptors = []   #  存 29 個 基準人頭的特徵矩陣
candidate = []     #  候選人姓名

for root, dirs, files in os.walk(face_folder_path):
    for file in files:
        candidate.append(  os.path.join(root, file).strip(r'./原始大頭照0123456789-\jpg')  )
        # opencv
        img_cv = cv2_imread(os.path.join(root, file))
        rects = detector(img_cv, 1)
        for n, d in enumerate(rects):
            if n == 0:
                shape = predictor(img_cv, d)  # 68特徵點偵測
                feature = facerec.compute_face_descriptor(img_cv, shape)  # 取得128維特徵向量
                descriptors.append( numpy.array(feature) )

pickle_file1 = './原始大頭照/staff_descriptors.pickle'
pickle_file2 = './原始大頭照/staff_candidate.pickle'

with open(pickle_file1, 'wb') as f1:
    pickle.dump(descriptors, f1)

with open(pickle_file2, 'wb') as f2:
    pickle.dump(candidate, f2)