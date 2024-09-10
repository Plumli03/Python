with (open("成績單.txt") as f):
    list_all=f.readlines()
    print(list_all) #['01\t楊佳錩\t76\t80\t45\tA\t82-5-14\n'

# #split('\t') ['01', '楊佳錩', '76', '80', '45', 'A', '82-5-14\n']
#     a= list_all[0].split('\t')[6].strip().split('-')
#     print(repr(a)) #['82', '5', '14']

    # from datetime import datetime #可只用物件d9=datetime.now()
    import datetime as dt
    yn=dt.datetime.now().year #year 屬性
    mn = dt.datetime.now().month
    dn = dt.datetime.now().day

    age_all = []
    for it in list_all:
        a = it.split('\t')[6].strip().split('-')
        y=int(a[0])+1911
        m=int(a[1])
        d=int(a[2])
        age = yn - y
        if m > mn or (m==mn and d>dn):
            age-=1
        # print(age,end=" ") #loop內每次都要印
        age_all.append(age)
    print(age_all) #[31, 27, 26, 25, 19,
    max_a=max(age_all)
    min_a = min(age_all)

    dict1={}
    for n in range(min_a,max_a+1):
        dict1[n]=0 #key'n' 新增value'0'
    print(dict1) #{8: 0, 9: 0, 10: 0

    for u in age_all: #統計key
        dict1[u]+=1
    print(dict1) #{8: 1, 9: 1, 10: 2, 11: 0, 12: 1


    import matplotlib.pyplot as plt
    plt.rc('font', family='Microsoft JhengHei') #中文

    年齡=list(dict1.keys())
    人數 = list(dict1.values())
    plt.bar(年齡, 人數 , color=['red', 'green', 'blue', 'yellow'])
    plt.xlabel('年齡')
    plt.ylabel('人數')
    plt.title('stats')
    plt.show()
