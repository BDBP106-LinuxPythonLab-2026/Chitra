point=int(input("Enter any point:"))
if point>=0 and point<=90:
    print(point,"lies in 1st quadrant")
elif  point<=180 and  point>90:
    print(point,"lies in the 2nd quadrant")
elif point>180 and point <=270:
    print(point,"lies in the 3rd quadrant")
else:
    print(point,"lies in the 4th quadrant")




