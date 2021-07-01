num=int(input("enter any number"))
a=num
sum=0
while num>0:
    i=1
    fac=1
    rem=num%10
    while i<=rem:
        fac=fac*i
        i+=1
    sum+=fac
    num=num//10
if sum==a:
    print("num is strong")
else:
    print("num is not strong")