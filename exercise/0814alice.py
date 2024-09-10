with open("alice blue.txt",mode="r") as f:
    a = f.readlines()
    print(a)  # ['alice blue\n', '\n', '240\n', '\n', '248\n', '\n', '255\n', '\n', 'AliceBlue\n', '\n'
    print(len(a)) #6079/4=759.9

    list1=[]
    for n in range(0,len(a),8): #gap=8
        # .strip()去除前後空白和換行符
        # print([a[n].strip(),int(a[n+2]),int(a[n+4]),int(a[n+6]) ])
        #YellowGreen 154 205 50
        #加[] ['YellowGreen', 154, 205, 50]

        # list1.append([a[n].strip(),int(a[n+2]),int(a[n+4]),int(a[n+6]) ])
        #[['alice blue', 240, 248, 255], ['AliceBlue', 240, 248, 255],...]

        r = int(a[n+2])
        g = int(a[n + 4])
        b = int(a[n + 6])
        #hex(5) '0x5' 不須前2 補0 int
        hex4='#'+hex(r)[2:].zfill(2)+hex(g)[2:].zfill(2)+hex(b)[2:].zfill(2)
        list1.append(','.join([a[n].strip(),str(r),str(g),str(b),hex4]) +'\n')

    print(list1) #不可再for內 只1次
    # ['alice blue,240,248,255,#f0f8ff',

with open("顏色.txt",mode='w') as q:
    q.writelines(list1) #['alice blue,240,248,255,#f0f8ff\n',

