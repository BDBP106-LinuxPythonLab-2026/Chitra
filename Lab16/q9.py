num=int(input("Enter a number:"))
rev=0
while num > 0:
    n=num % 10
    rev=rev * 10 + n
    num=num // 10
print("Reverse number is :",rev)