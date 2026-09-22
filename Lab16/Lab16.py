#1.
#name = input("Enter your name:")
#print(name.title())

#2
import math

#p = int(input("Enter principal amount:"))
#r = int(input("Enter rate of interest:"))
t = int(input("Enter time:"))
n = int(input("Enter value for n:"))
simint = float(p * r * t)
a = float(p * (1 + (r / n))**(n * t))
print("Simple interest is:",simint)
print("Amount is:",a)
