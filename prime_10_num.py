num=int(input("enter a num"))
i=1
prime_count=0
while 1:
    j=2
    count=0
    while j<=i:
        if i%j==0:
            count+=1
        j+=1
    if count==1:
        print(i)
        prime_count+=1
    if prime_count==num:
        break
    i+=1