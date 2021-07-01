i=2
ev=0
odd=0
while i<=100:
    j=2
    c=0
    while j<=i:
        if i%j==0:
            c+=1
        j+=1
    if c==1:
        if i%2==0:
            print(i,"is even prime")
            ev+=1
        else:
            print(i,"is odd prime")
            odd+=1
    i+=1
print(ev,"even number")
print(odd,"odd number")