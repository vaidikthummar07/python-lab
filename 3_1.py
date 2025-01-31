a=(input('enter the word:'))
vowels="aeiou"
count=0
for char in a:
    if char in vowels:
        count+=1
print("vowels in your word is :",count)
