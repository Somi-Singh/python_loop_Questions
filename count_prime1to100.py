num=int(input("enter any num"))
i=1
while i<=num:
    j=2
    c=0
    while i>=j:
        if i%j==0:
            c+=1
        j+=1
    if c==1:
        print(i,"is prime")
    i+=1