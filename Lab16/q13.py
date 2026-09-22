num=int(input("Enter a number:"))
fact=1
for i in range(num,1,-1):
    fact=fact*i
print("Factorial of",num,"is",fact)
