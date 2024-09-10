with open("rank.txt",mode="r") as f:
    list_all = f.readlines()
    print(repr(list_all))

    import random
    for n, item in enumerate(list_all):
        ty = random.randint(80, 105)
        m = random.randint(1, 12)
        d = random.randint(1, 28)
        birth = str(ty) + '-' + str(m) + '-' + str(d)
        list_all[n] = item.strip() +'\t'+ birth+ '\n'
    print(repr(list_all))

with open("生日.txt",mode="w") as f:
    f.writelines(list_all)
