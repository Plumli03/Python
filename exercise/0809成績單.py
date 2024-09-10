f= open("名單.txt",encoding="utf-8") #big5中文
str1 =f.read() # print(repr(str1))
f.close()

list = str1.split('\n')
list = list[1:-1] #最後有\n 切片
print(list)
print(len(list))

# for n,t in enumerate(list):
#     list[n]=t.strip('0123456789\t')
# list.sort()
# print(list)

# name=[]
# no=[]
# for n in list:
#     # name.append(n.strip('0123456789\t')) #strip頭尾
#     name.append(n.split('\t')[1])
#     no.append(n.split('\t')[0].zfill(2))
# print(name)
# print(no)

# script=[]
# for n in list:
#     script.append( (n.split('\t')[0].zfill(2),n.split('\t')[1]) )
# #串列生成
# script=[(n.split('\t')[0].zfill(2),n.split('\t')[1]) for n in list]
# print(script)

bts= ['A', 'B', 'AB', 'O']
import random
script=[]
for n in list:
    no= n.split('\t')[0].zfill(2)
    name= n.split('\t')[1]
    國文 = random.randint(40,100)
    英文 = random.randint(40,100)
    數學 = random.randint(40,100)
    aver= round((國文+英文+數學)/3,1)
    bt= random.choice(bts)
    script.append( [no,name,國文,英文,數學,aver,bt]) #(no,name, math)tuple
print(script)

script=sorted(script,key=lambda x:x[0]) #key=lambda 運算士 x:x[4] 傳入:傳出
print(script)

#名次
n=1; rank=1;score=0
for i in script:
    if i[5]<score:
        rank=n
    i.append(rank)
    n+=1
    score=i[5]

# #a=list.sort變None 不可另存 用BIF sorted(list,key=func) 照學號
# script=sorted(script,key=lambda x:x[0],reverse=False)
# print(script)

# def func(x):
#     return x[6]+str(x[5])
# script=sorted(script,key=func)

# def bn(x):
#     match x[6]:
#         case 'A'  :
#             return "1" + str(x[7]).zfill(2)
#         case 'B'  :
#             return "2" + str(x[7]).zfill(2)
#         case 'O'  :
#             return "3" + str(x[7]).zfill(2)
#         case 'AB' :
#             return "4" + str(x[7]).zfill(2)
# script=sorted(script,key=bn)
# print(script)

# 生成大字串 = '01\t楊佳錩\t76\t80\t45\n02\t童建凱\t41\t71\t54\n...'
大字串 = ''
for t1 in script :
    str1 = t1[0] + '\t' + t1[1] + '\t' + str(t1[2])+ '\t' + str(t1[3])+ '\t' + str(t1[4])+ '\t' + str(t1[5]) + '\t' + str(t1[6])+ '\n'
    大字串 += str1
print(大字串)

f = open('rank.txt',mode='w') #mode='w'創建與複寫
f.write(大字串)
f.close()



