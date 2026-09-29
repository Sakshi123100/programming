n=int(input("enter number:"))
rem=0
rev=0
n1=n
while(n!=0):
    rem=n%10
    rev=rev*10+rem
    n=n//10
    print(rev)
if n1==rev:
    print("palindrome")
else:
    print("not palindrome")