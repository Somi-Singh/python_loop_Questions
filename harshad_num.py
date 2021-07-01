num=int(input("enter any num"))
sum=0
a=num
while num>0:
    rem=num%10
    sum=sum+rem
    num=num//10
if a%sum==0:
    print("harshad num")
else:
    print("not harshad")