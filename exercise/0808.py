#3-14
pro_n ="se" #非空str

part=""
while pro_n!="": # ="" 才停
    valid=False

    pro_n=input("enter(dd-dddd):")
    part=pro_n.split("-")

    if len(part)==2:
        if len(part[0])==2 and len(part[1])==4:
            if part[0].isdigit() and part[1].isdigit():
                valid = True

    print(valid)

