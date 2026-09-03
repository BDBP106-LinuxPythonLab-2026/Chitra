#3rd September
#QUESTION 1
q1=2.7/2
print(q1)
q2=2.7//2
print (q2)
q3=10+5j/2
print (q3)
q4=complex(2.2,5.3).conjugate().imag
print(q4)
q5=round(2.5)
print(q5)
q6=round(-2.5)
print(q6)
q7=2//4-1
print(q7)
q8=3*2**2
print(q8)
q9=3**2*2
print(q9)
q10=7//4
print(q10)
q11=7%4
print(q11)
q12=-7%4
print(q12)
#QUESTION 2
a=1
b=2
c=4
print (bool(a and b))
print (not a<b or c>b)
print (bool (type(complex(a,b+c).real) is int))
# QUESTION 3
k = int(input("Enter the value of k: "))
n = int(input("Enter the value of n: "))

if n > 0:
    suma = k + n
    multipli = k * n
    divi = k / n
    modu = k % n
    subt = k - n
print(suma)
print(multipli)
print(divi)
print(modu)
print(subt)
#QUESTION 4
import math
a=float(input("Enter the number (a): "))
b=float(input("Enter the number (b): "))
c=float(input("Enter the number (c): "))
d= (b*b)- 4*a*c
e= math.sqrt(d)
result1= (-b+e) / (2*a)
result2= (-b-e) / (2*a)
print ("Result 1= ", result1)
print ("Result 2= ", result2)
