side1=int(input("enter side 1:"))
side2=int(input("enter side 2:"))
side3=int(input("enter side 3:"))
if side1==side2==side3:
    print("It is an equilateral triangle")
elif side1!=side2!=side3:
    print("It is a scalene triangle")
else:
    print("It is an isoleces triangle")