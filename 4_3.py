a=(input("enter string:"))
no_alph=0
no_digits=0
for i in a:
    if i.isalpha():
        no_alph+=1
print(f'no of alpha is {no_alph}')
for i in a:
    if i.isdigit():
        no_digits+=1
print (f'no of digits is {no_digits}')


