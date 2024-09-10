f= open("rank.txt",encoding="utf-8") #big5中文
str1 =f.read() # print(repr(str1))
f.close()

list = str1.split('\n')
list = list[:-1] #最後有\n 切片
print(list)

script=[]
for n in list:
    no= n.split('\t')[0].zfill(2)
    name= n.split('\t')[1]
    aver= n.split('\t')[5]
    bt= n.split('\t')[6]
    script.append( [no,name,aver,bt]) #(no,name, math)tuple
print(script)

分類=[0,0,0,0]
for i in script:
    match i[3]:
        case 'A'  :
             分類[0]+=1
        case 'B'  :
            分類[1]+=1
        case 'O'  :
             分類[2]+=1
        case 'AB' :
             分類[3]+=1
print(分類)


import matplotlib.pyplot as plt
plt.rc('font', family='Microsoft JhengHei') #中文

血型 = ['A', 'B', 'AB', 'O']
plt.bar(血型, 分類, color=['red', 'green', 'blue', 'yellow'])
plt.xlabel('blood血型')
plt.ylabel('人數')
plt.title('stats')
plt.show()



