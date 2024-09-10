with open("alice blue.txt",mode="r") as f:
    a = f.readlines()
    print(a)  # ['alice blue\n', '\n', '240\n', '\n', '248\n', '\n', '255\n', '\n', 'AliceBlue\n', '\n'
    print(len(a)) #6079/4=759.9


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
        print('%-15s %3d %3d %3d  #%02X%02X%02X' % (a[n].strip(),r,g,b,r,g,b))

        # '{:<12s}  {:3d} {:3d} {:3d} #{:02X}{:02X}{:02X} '.format(a[n].strip(),r,g,b,r,g,b)
        # # print('{:<12s}  {:3d} {:3d} {:3d} #{:02X}{:02X}{:02X} '.format(a[n].strip(),r,g,b,r,g,b))
        print('{0:<12s}  {1:3d} {2:3d} {3:3d} #{1:02X}{2:02X}{3:02X} '.format(a[n].strip(),r,g,b))

        str1=f'{a[n].strip():<12s}  {r:3d} {g:3d} {b:3d} #{r:02X}{g:02X}{b:02X} '
        print(str1)

    # YellowGreen     154 205  50  #9ACD32


