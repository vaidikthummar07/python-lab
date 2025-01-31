a=int(input("enter the length-"))
b=int(input("enter the breath-"))
area= a*b
perimeter= 2*(a+b)
print("area of rectangle is -",area)
print("perimeter of rectangle is -",perimeter)
if area>perimeter:
    print("area is greater than its perimeter")
else:
    print("area is smaller than its perimeter")


