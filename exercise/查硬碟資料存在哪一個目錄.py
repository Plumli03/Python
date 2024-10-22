import os
import re

lines = []

for root, dirs, files in os.walk(r"C:\Users\Hcedu"):

    for file in files :
        # 錄製_2023_03_31_20_41_43_843.mp4
        if re.match(".*[.]csv",file) !=  None  :
        #匹配任何於括號（[]）內出現的字符
        #if re.match("新竹市重要遊憩據點遊客人次統計.xlsx",file) !=  None  :
            print(file)
            # if root not in lines :
            #     print(root)
            #     print('============')
            #     lines.append(root)
            #     lines.append('\n')
# with open('../mp4.txt', 'w', encoding="utf-8") as f:
#     f.writelines(lines)

# import os
# for root, dirs, files in os.walk(r"C://"):
#     for file in files :
#             # if file[-4:] =='.mp4' :
#             if file=='With You.mp4' :
#                 print(root+'\\'+file) #跳脫\\留下\
#                 # a=root + '\\' + file
#                 # os.remove(a)

