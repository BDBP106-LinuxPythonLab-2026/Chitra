num=int(input("enter the number"))
sum=0
for i in range(1,num):
    n=num%10
    sum=sum+n
    num=num//10

print("Sum of digits is:",sum)
