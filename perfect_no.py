num=int(input("enter any num"))
sum=0
i=1
while i<num:
    if num%i==0:
        sum+=i
    i+=1
if num==sum:
    print("perfect num")
else:
    print("not perfect")