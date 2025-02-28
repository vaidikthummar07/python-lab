def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact = fact *i
    return fact
#nCr
n=int(input("n:"))
r=int(input("r:"))
if r>n:
    print("error")
else:
    num= factorial(n)
    denom= ((factorial(n-r))*(factorial(r)))
    nCr=num//denom
print (f"{n}C{r}={nCr}")

#nPr
if r>n:
    print("error")
else:
    num= factorial(n)
    denom= factorial(n-r)
    nPr=num//denom
print (f"{n}P{r}={nPr}")
