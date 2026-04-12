str = input()
str1=''
for i in str:
    if i.islower() == True:
        str1 += i.upper()
    else: 
        str1 += i.lower()
print(str1)
        


