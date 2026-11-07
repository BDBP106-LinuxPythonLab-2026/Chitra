#1
class Car:
    def __init__(self, make, model, year, color, started=False, speed=0, max_speed=200):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.started = started
        self.speed = speed
        self.max_speed = max_speed

    showroom = "NewAge"

    @classmethod
    def change_showroom(cls, name):
        cls.showroom = name

    def __str__(self):
        return f"{self.make} {self.model} {self.color} ({self.year})"

    @staticmethod
    def show_intro_message():
        print("This class represents a car")
# a
toyota_camry = Car("Toyota", "Camry", 2022, "Black")
print(toyota_camry.make)
print(toyota_camry.model)
print(toyota_camry.year)
print(toyota_camry.color)
print(toyota_camry.started)
print(toyota_camry.speed)
print(toyota_camry.max_speed)
# b
ford_mustang = Car("Ford", "Mustang", 2022, "Black")
print(ford_mustang.make)
print(ford_mustang.model)
print(ford_mustang.year)
print(ford_mustang.color)
print(ford_mustang.started)
print(ford_mustang.speed)
print(ford_mustang.max_speed)
# c
# print(Car.make)
# Attribute Error because make is an instance attribute. It is created using self.make when an object is initialized, not directly inside the class namespace.
print("make" in toyota_camry.__dict__)
print("make" in ford_mustang.__dict__)
# d
print(Car.__dict__)
# Car.__dict__ displays the namespace of the Car class. It contains special attributes such as __module__, __init__, and __doc__. The __static_attributes__ tuple lists attribute names accessed through self in the class's methods. Instance attributes such as color, make, and speed are stored in the instance's __dict__, not directly in the class's dictionary.
# e
print(Car.showroom)
Car.change_showroom("Premium equipments")
print(Car.showroom)
print(Car.__dict__)
# Output is NewAge and then Premium equipments
# .__dict__ statement now prints the class dictionary, including showroom with its updated value and the change_showroom method.
# f
print(toyota_camry.__dict__)
# toyota_camry.__dict__ contains the instance's attribute whereas Car.__dict__ contains the class level members including methods and class attributes.
# g
print(str(toyota_camry))
print(str(ford_mustang))
# h
Car.show_intro_message()
#2
import time
def calculate_time(func):
    def wrapper(*args):
        start=time.time()
        result=func(*args)
        end=time.time()
        print("Time taken:",end-start,"seconds")
        return result
    return wrapper

class LinearAlgebra:
    def __init__(self,A,B):
        self.A=A
        self.B=B
    @property
    def A(self):
        return self._A
    @A.setter
    def A(self,value):
        self._A=value
    @property
    def B(self):
        return self._B
    @B.setter
    def B(self, value):
        self._B = value

    @calculate_time
    def multiply(self):
        rows_A=len(self.A)
        cols_A=len(self.A[0])
        rows_B = len(self.B)
        cols_B = len(self.B[0])
        if cols_A!=rows_B:
            raise ValueError("Matrix multiplication not possible")
        result=[]
        for i in range(rows_A):
            row=[]
            for j in range(cols_B):
                total=0
                for k in range(cols_A):
                    total+=self.A[i][k]*self.B[k][j]
                row.append(total)
            result.append(row)
        return result
r1=int(input("Rows of A: "))
c1=int(input("Columns of A: "))
A=[]
print("Enter elements of A row by row: ")
for i in range(r1):
    row=[]
    for j in range(c1):
        row.append(int(input()))
    A.append(row)
r2=int(input("Rows of B: "))
c2=int(input("Columns of B: "))
B=[]
print("Enter elements of B row by row: ")
for i in range(r2):
    row=[]
    for j in range(c2):
        row.append(int(input()))
    B.append(row)
obj=LinearAlgebra(A,B)
try:
    result=obj.multiply()
    print("Product matrix: ")
    for row in result:
        print(row)
except ValueError as e:
    print(e)

#3
import re
number=int(input("Enter a 3 digit integer"))
pattern=r"^(?:00[0-9]|0[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$"
if re.fullmatch(pattern,str(number)):
    print("The number is valid")
else:
    print("The number is not valid")
#4
number=input("Enter a 3 digit integer")
pattern=r"^(?:0|[1-9]\d?|1\d{2}|2[0-4]\d|25[0-5])$"
if re.match(pattern,number):
    print("The number is valid")
else:
    print("The number is not valid")
#5
import re

str=input("enter an email address: ")
pattern=r"^[A-Z a-z 0-9]+[@]\w+[.]\w+$"
if re.match(pattern,str):
    print("Email address is valid")
else:
    print("Email address is invalid")
#6
import re
pattern=r"[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}"
line=input("Enter a csv line: ")
fields=line.split(",")
if len(fields)>3:
    email=fields[2].strip()
    if re.fullmatch(pattern, email):
        print("Third field contains an email address")
    else:
        print("Third field is not an Email address")
else:
    print("CSV must contain more than 3 fields")
#7
import re
text=input("Enter a piece of text: ")
pattern=r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}'
emails=re.findall(pattern,text)
unique_emails=[]
for email in emails:
    if email not in unique_emails:
        unique_emails.append(email)
print("Unique email adresses are: ")
for email in unique_emails:
    print(email)
#8
import re
text=input("Enter a piece of text: ")
pattern=r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}'
def mask_email(match):
    email=match.group()
    parts=email.split("@")
    username=parts[0]
    domain=parts[1]
    if len(username)<=2:
        masked=username[0]+"*"*(len(username)-1)
    else:
        masked=username[0]+"*"*(len(username)-2)+username[-1]
    return masked+"@"+domain
result=re.sub(pattern,mask_email,text)
print(result)
#9
import re
dna="ATCGCGAATTCAATGTACTGC"
pattern=r'GAATTC'
if re.search(pattern,dna):
    print("ECoRI restriction site found")
else:
    print("ECoRI restriction site not found")