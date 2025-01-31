x1=int(input("enter your x cordinate of center of circle-"))
y1=int(input("enter your y cordinate of center of circle-"))
r=int(input("enter the radius of circle_"))
x2=int(input("enter your x cordinate of unkown point -"))
y2=int(input("enter your y cordinate of unknown point -"))
dis=pow(pow((x2-x1),2)+ pow((y2-y1),2),0.5)
if dis>r:
    print("point is outside the circle.")
elif dis==r:
    print("point is lies on the circle.")
else:
    print("point is inside the circle.")
