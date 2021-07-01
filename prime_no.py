num=int(input("enter any num"))
c=0
i=1
while i<=num:
    if num%i==0:
        c+=1
    i+=1
if c==2:
    print("prime no")
else:
    print("not prime")