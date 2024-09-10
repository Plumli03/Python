# f= open("水果的價格.txt",encoding="utf-8",mode="r") #big5中文
#
# # #f.read()#str then split
# # str_all=f.read()
# # list_all= str_all.split('\n')[:-1]
# #
# # for n,i in enumerate(list_all): #enumerate n,i 數字,元素
# #     list1=i.split(',')
# #     list1[1]=float(list1[1])
# #     list1[2]=float(list1[2])
# #     list_all[n]=list1 #元素無法當索引用數字enumerate
# # print(list_all)
#
#
# # #f.readline() # 一行str 需loop
# # list_all=[]
# # str1=f.readline()
# # while str1 !='' :
# #     # print(repr(str1))
# #     # str1 = f.readline()
# #     list1=str1.split(',')
# #     list1[1]=float(list1[1])
# #     list1[2]=float(list1[2])
# #     # print(list1)
# #
# #     list_all.append(list1)
# #     str1=f.readline()
# # print(list_all)
#
#
# #f.readlines() #list ['str', '']
# list_all=f.readlines()
#
# for n,i in enumerate(list_all): #enumerate n,i 數字,元素
#     list1=i.split(',')
#     list1[1]=float(list1[1])
#     list1[2]=float(list1[2])
#     list_all[n]=list1 #元素無法當索引用數字enumerate
# print(list_all)
#
# f.close()

with open("水果的價格.txt",mode="r") as f: #唯讀mode="r"
#tab code區塊 自動close f檔案物件
    list_all = f.readlines()
    for n, i in enumerate(list_all):  # enumerate n,i 數字,元素
        list1 = i.split(',')
        list1[1] = float(list1[1])
        list1[2] = float(list1[2])
        list_all[n] = list1  # 元素無法當索引用數字enumerate
    print(list_all) #[['Oranges', 5.6, 1.33], ['Apples', 2.0, 0.54], ['Grapes', 10.2, 10.96]]


with open("水果的價格1.txt", mode="w") as f:
    for n, t in enumerate(list_all):
        t[1] = str(t[1]+800)
        t[2] = str(t[2])
        list_all[n] = ','.join(t) + '\n'
    print(list_all)  # ['Oranges,5.6,1.33\n', 'Apples,2.0,0.54\n', 'Grapes,10.2,10.96\n']
    # f.writelines(list_all)

    #''.join str
    a=''.join(list_all)
    print(a)
    print(type(a))
    f.write(a)