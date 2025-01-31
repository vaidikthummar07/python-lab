x1=int(input("enter your x cordinate of point 1-"))
y1=int(input("enter your y cordinate of point 1-"))
x2=int(input("enter your x cordinate of point 2-"))
y2=int(input("enter your y cordinate of point 2-"))
x3=int(input("enter your x cordinate of point 3-"))
y3=int(input("enter your y cordinate of point 3-"))
m1=(y3-y1)/(x3-x1)
m2=(y2-y1)/(x2-x1)
if m1==m2:
    print ("all points are on one straight line.")
else:
    print ("all points are not on one straight line.")
