s=input()
temp=s
rev=""
for i in range(len(s)-1,-1,-1):
    rev=rev+s[i]
print(rev)
if rev==temp:
    print("palindrome")
else:
    print("non-palindrome")