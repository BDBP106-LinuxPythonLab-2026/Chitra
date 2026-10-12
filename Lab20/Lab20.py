#1
n=int(input("Enter a number:"))
if n<0:
    print(n,"is a negative number")
    if n%2==0:
        print("Its is even number")
    else:
        print("It's an odd number")
    if n%3==0 and n%5==0:
        print("Fizzbuzz")
elif n>0:
    print(n,"is a positive number")
    if n%2==0:
        print("Its is even number")
    else:
        print("It's an odd number")
    if n%3==0 and n%5==0:
        print("Fizzbuzz")
else:
    print("number is zero")
#2
a=input("Enter  text:")
vowels=0
consonants=0
digits=0
spaces=0
for b in a:
    if b=="a" or b=="e" or b=="i" or b=="o" or b=="u":
        vowels=vowels+1
    elif b=="A" or b=="E" or b=="I" or b=="O" or b=="U":
        vowels=vowels+1
    else:
        consonants=consonants+1
    if isdigit(b):
        digits=digits+1
    if b==" ":
        spaces=spaces+1
print("Total vowels are:",vowels)
print("Total consonants are:",consonants)
print("Total digits are:",digits)
print("Total spaces are:",spaces)
#3
n=26
num=int(input("Guess the number:"))
count=0
if n==num:
    print("Yayyy!!Guessed it")
for count in range(1,8):
    num=int(input("Guess again"))
    count=count+1
    if num>n:
        print("Too high")
    elif num<n:
        print("Too low")
    else:
        print("Yayy!!Guessed it")
        break
    if count==7:
        print("Okay!!! bonus time", "\n", "So the number is:", n)
        break
if count<7:
     print("The number of attempts taken:",count)
#4
n=int(input("Enter any number:"))
#header
for j in range(1,n+1):
 print(j,end=" ")#normally it goes to nextline but with end it stays in one line adding a space before it
print()
for i in range(1,n+1):
 print(i,end=" ")
 for j in range(1,n+1):
 result=j*i
 print(result,end=" ")
 print()

#5
list = []
num = input("Enter the number of items to be added to the list: ")
for i in range(0, int(num)):
    item = input("Enter the item to be added to the list: ")
    if item.lower() not in list:
        list.append(item.lower())
print("The input list is: ", list)
while True:
    print("Choose from the below if you want any changes in the cart or you can continue with billing")
    print("MENU", "\n", "1.Add item", "\n", "2.Remove item", "\n", "3.View list", "\n", "4.Sort list", "\n", "5.quit")
    n = int(input("Enter your choice:"))
    if n == 1:
        item = input("Enter what you want to add: ")
        list.append(item.lower())
        print("The modified list is: ", list)
    elif n == 2:
        item = input("Enter the item you want to remove")
        item = item.lower()
        if item not in list:
            print("The item you want to remove is not in the list")
            break
        else:
            list.remove(item.lower())
            print("The modified list is:", list)

    elif n == 3:
        if len(list) == 0:
            print("Your shopping list is empty")
        else:
            for number, item in enumerate(list, start=1):
                print(number, ".", item)


    elif n == 4:
        l = sorted(list)
        print(l)

    elif n == 5:
        print("Thank you for shopping:)", "\n", "Come Again!!")
        break

#6

students = [("Asha", 88), ("Ravi", 72), ("Meera", 95), ("Karan", 59), ("Divya", 81)]
sum=0
for student in students:
    if student[1]>=90:
        print(student[0],"grade is A")
    elif student[1] >= 80:
        print(student[0], "grade is B")
    elif student[1] >= 70:
        print(student[0], "grade is C")
    elif student[1] >= 60:
        print(student[0], "grade is D")
    else:
        print(student[0],"grade is F")
    sum=sum+student[1]
average=sum/len(students)
print("Average is:",average)
max=student[1]
min=student[1]
for student in students:
    if student[1]>max:
        highest=student[0]
for student in students:
    if student[1] < min:
        lowest = student[0]
print("Highest scorer is ",highest)
print("Lowest scorer is:",lowest)
#7
para=""" Python is easy to learn, and Python is fun! Learning Python helps beginners,
and beginners enjoy learning. Is Python easy? Yes, Python is easy!"""
para=para.lower()
words=para.lower().split()
count={}
for word in words:
    word=word.strip(".,!?;:")
    if word in count:
        count[word]+=1
    else:
        count[word]=1

    print(word,":",count[word])

max_count=max(count.values())
print("Most frequent word")
for word in sorted(count):
    if count[word]==max_count:
        print(word,":",count[word])
#8
python_class = ["Anil", "Bina", "Chetan", "Deepa", "Anil", "Esha"]
java_class = ["Chetan", "Farhan", "Deepa", "Gita", "Bina"]
python_class=set(python_class)
java_class=set(java_class)
print("Students in both courses are",python_class.intersection(java_class))
print("Students taking only python course are:",python_class-java_class)
print("Students taking only java course are:",java_class-python_class)
unique_students=python_class.union(java_class)
print("Unique students are:",unique_students)
name=input("Enter the name for whom you want to know the course:")
if name in python_class and name in java_class:
       print(name,"has enrolled in both python and java course")
elif name in python_class:
    print(name,"has enrolled in python course")
elif name in java_class:
    print(name,"has enrolled in java class")
else:
    print(name,"has not enrolled in any of the courses")
#9
while True:
    password = input("Enter a password:")
    isupper = False
    islower = False
    isdigit = False
    has_special = False
    has_space = False
    special_chars = {"!", "@", "#", "$", "%", "&", "*"}
    for ch in password:
            if ch.isupper():
                isupper=True
            if ch.islower():
                islower=True
            if ch.isdigit():
                isdigit=True
            if ch in special_chars:
                has_special = True
            if ch.isspace():
                has_space = True
    if len(password)<9:
         print("Password should be at least 8 characters")
    if not isupper:
         print("There should be at least 1 uppercase character")
    if not islower:
         print("There should be at least 1 lowercase character")
    if not isdigit:
            print("There should be at least 1 digit")
    if not has_special:
         print("There should be at least 1 special character")
    if has_space:
         print("There should be at least 1 space character")
    if "password" in password.lower():
         print("Password should not contain the word:password")
    if (
            len(password) >= 8 and isupper and islower and isdigit and has_special and not has_space and "password" not in password.lower()):
        print("You are good to go!")
        break
    else:
        print("Please enter a valid password")

#10

inventory = {
"pen": (10.0, 50), # (price, quantity in stock)
"notebook": (45.0, 20),
"eraser": (5.0, 100),

"marker": (30.0, 15),
}
cart={}
while True:
    order=input("Enter order or done to finish:")
    if order.lower() == "done":
        break
    print(order)
    item = order.split()
    if len(item) != 2:
        print("Please enter item and quantity, for example: pen 3")
        continue
    item,quantity=item
    if item not in inventory:
        print("Item not available")
        continue
    try:
        quantity=int(quantity)
    except ValueError:
        print("Please enter a valid quantity")
        continue
    if quantity <= 0:
        print("Quantity must be greater than 0")
        continue
    price,stock=inventory[item]
    if quantity>stock:
        print("Not enough stock")
        continue
    if item in cart:
        cart[item]+=quantity
    else:
        cart[item]=quantity
    inventory[item]=(price,stock-quantity)
    print(f"Added {quantity} {item}s to cart.")


