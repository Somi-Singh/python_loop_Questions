target_num=5
i=1
while i<=5:
    num=int(input("enter any num"))
    i+=1
    if num==target_num:
        print("guess correct")
        break
    elif num>target_num:
        print("too high")
    elif num<target_num:
        print("too low")
    else:
        print("your program is finish")
    