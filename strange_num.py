n=100
a=1
i=1
while i<=n:
    j=1
    sum=0
    while j<=i:
        d=a%10
        a=a//10
        sum=sum+d
        j+=1
        a+=1
    if sum%9==0:
        print(sum,"strange")
    i+=1