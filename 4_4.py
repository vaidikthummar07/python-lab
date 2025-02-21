num=int(input("enter a number:"))
count1=0
count2=0
count3=0
check_num=0
reverse_num=0
a=str(num)
no_digits=len(a)
#prime number
for i in range(2,num+1):
    if num%i==0:
        count1+=1
if count1==1:
    print(f"{num}number is prime.")
else:
    print(f"{num} number not is prime.")
#perfect 
for i in range(1,num):
    if num%i==0:
        count2+=i
if count2==num:
    print(f"{num} number is perfect.")
else:
    print(f"{num} number is not perfect.")

#armstrong number
num2 = num
while(num2):
    digit=num2%10
    count3+=(digit**no_digits)
    num2 = num2//10
if count3==num:
    print (f"{num} number is armstrong.")
else:
    print(f"{num} number is not armstrong.")

#palinedrome
num3=num
while (num3):
    reverse_num=(reverse_num*10)+(num3%10)
    num3=num3//10
if reverse_num==num:
    print (f"{num} number is palindrome.")
else:
    print(f"{num} number is not palindrome.")

#automorphic
num4=num*num
last_digit=num4%(10**no_digits)
if last_digit==num:
    print(f"{num} is an automorphic number.")
else:
    print(f"{num} is not an automorphic number.")
