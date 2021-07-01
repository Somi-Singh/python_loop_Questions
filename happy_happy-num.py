user=int(input("enter any num"))
sum=0
while user>0:
    r=user%10
    sum=sum+r**2
    user=user//10
if sum==1:
    print("happy number")
else:
    print("not happy number")