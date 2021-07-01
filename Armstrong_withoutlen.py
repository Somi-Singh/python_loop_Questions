sum=0
i=int(input("enter any num"))
m=i
while i>0:
    c=i%10
    d=c**3
    i=i//10
    sum=sum+d
if sum==m:
    print("Armstrong num")
else:
    print("no Armstrong num")