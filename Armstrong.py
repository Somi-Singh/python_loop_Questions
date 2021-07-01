user=input("enter a num")
m=int(user)
n=m
i=0
sum=0
while m>0:
    c=m%10
    d=c**len(user)
    m=m//10
    sum=sum+d
if sum==n:
    print("Armstrong num")
else:
    print("not Armstrong")