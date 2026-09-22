from operator import concat

num=int(input("Enter a number:"))
ori=num
rev=0
while num > 0:
    n=num % 10
    rev=rev * 10 + n
    num=num // 10

if ori==rev:
    print(ori,"is palindrome")
else:
    print(ori,"is not a palindrome")
