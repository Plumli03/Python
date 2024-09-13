import numpy as np
import cv2  #pip opencv-python  opencv C語言影像處理
from PIL import Image #pip pillow

# from PIL import Image  #開中文檔名圖 PIL pillow
# with Image.open(r".\30-李宗迅.jpg") as im:
#     # photoshop 看x,y座標 739,252  1929,1822
#     img=np.array(im)[252:1822,739:1929,:] #彩圖RBG nd.array(height, width, 3)
#     img = Image.fromarray(img) # 將 NumPy 陣列轉換回 Pillow 圖像
#     img.show()
##------------------------
# #圖上寫中文
# from PIL import Image, ImageDraw, ImageFont
# with Image.open(r".\30-李宗迅.jpg").convert("RGBA") as base:
#
#     img=np.array(base)[252:1822,739:1929,:] #彩圖RBG nd.array(height, width, 3)
#     img = Image.fromarray(img) # 將 NumPy 陣列轉換回 Pillow 圖像
#     # make a blank image for the text, initialized to transparent text color
#     txt = Image.new("RGBA", img.size, (255, 255, 255, 0))
#
#     # get a font 字體.otf .ttf  google:NotoSansTC-Black.ttf
#     fnt = ImageFont.truetype(r"C:\Users\Hcedu\Downloads\老師zip\NotoSansTC-Black.ttf", 200)
#     # get a drawing context
#     d = ImageDraw.Draw(txt)
#     # draw text, half opacity不透明度
#     d.text((1000, 800), "原始", font=fnt, fill=(255, 255, 255, 128))
#     # draw text, full opacity
#     d.text((1000, 2000), "30-李宗迅", font=fnt, fill=(255, 255, 255, 255))
#     out = Image.alpha_composite(base, txt)
#     out.show()
##----------
# import urllib.request  #  直接打開網路上的照片
# url = r'https://p3.itc.cn/images01/20230919/91c499baeacb47e0af215305b122820f.jpeg'
# img = np.array(Image.open(urllib.request.urlopen(url)))
# cv2.namedWindow('Face',0)
# cv2.imshow("Face", img[::,::,::-1])   # 顯示影像，reverse轉成GBR模式
# cv2.waitKey(0) #留視窗
# cv2.destroyAllWindows()

##-------------
# CV2 人臉偵測
import cv2

# pictPath = r'haarcascade_frontalcatface.xml' # 看貓臉
# face_cascade = cv2.CascadeClassifier(pictPath)                    # 建立辨識物件
# img = cv2.imread("./照片/cat.jpg")                                       # 讀取貓臉影像
# print(img.shape)  # (431, 576, 3)
# faces = face_cascade.detectMultiScale(img, scaleFactor=1.05,
#         minNeighbors = 9, minSize=(60,60),maxSize=(200,200))

# pictPath = r'haarcascade_frontalface_alt2.xml' # 看人臉
# face_cascade = cv2.CascadeClassifier(pictPath)
# img = cv2.imread("./照片/image (3).png")
# print(img.shape)  # (1773, 2364, 3)
# faces = face_cascade.detectMultiScale(img, scaleFactor=1.03,
#         minNeighbors = 9, minSize=(55,55),maxSize=(80,80))

from PIL import Image
import numpy as np
import cv2

# # Open 中文 image using Pillow
# with Image.open(r".\照片\全班.png") as im: # jpg3層 png4th透明塗層
#     img = np.array(im)
# # Convert the cropped image from RGB (Pillow) to BGR (OpenCV)
# img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

img = np.array(Image.open(r".\照片\404243.jpg").convert(mode="RGB"))

pictPath = r'haarcascade_frontalface_alt2.xml' # 看人臉
face_cascade = cv2.CascadeClassifier(pictPath)
print(img.shape)  # (1773, 2364, 3)
faces = face_cascade.detectMultiScale(img, scaleFactor=1.03,
        minNeighbors = 30, minSize=(10,10),maxSize=(300,300))



# print(faces)  # [ 471  784   68   68]  x y w h
# 標註右下角底色是黃色
cv2.rectangle(img, (img.shape[1]-700, img.shape[0]-100),
              (img.shape[1],img.shape[0]), (0,255,255), -1)
# 標註找到多少的人臉
cv2.putText(img, "Finding " + str(len(faces)) + " face",
            (img.shape[1]-600, img.shape[0]-25),
            cv2.FONT_HERSHEY_COMPLEX, 2, (0,0,255), 2)
# 將人臉框起來, 由於有可能找到好幾個臉所以用迴圈繪出來
for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)      # 藍色框住人臉

cv2.namedWindow('Face',0)
cv2.imshow("Face", img)                                 # 顯示影像
cv2.imshow("Face", img[:,:,::-1])                                 # 顯示影像

cv2.waitKey(0)
cv2.destroyAllWindows()

'''
scaleFactor:圖像大小在每個圖像尺度上減少了多少。
這個值用於創建縮放金字塔，以便檢測圖像中多個縮放的面部
(一些面可能更接近前景，因此更大；其他面可能更小並且在背景中，因此使用不同的縮放)。
比如設置值為1.05，則表明我們在金字塔中的每個級別將圖像的大小減小了5％。

minNeighbors:每個窗口應該有多少個neighbors才能將窗口中的區域視為一個臉。
級聯分類器將檢測面部周圍的多個窗口。
此參數控制需要檢測多少矩形(Neighbors)才能將窗口標記為面部。

minSize:寬度和高度(以像素為單位)的元組，表示窗口的最小尺寸。
小於此大小的邊界框將被忽略。從(30,30)開始並從那裡進行微調是一個好主意。
'''


