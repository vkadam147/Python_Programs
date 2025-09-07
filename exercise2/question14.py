# 14. Check whether a number is a palindrome.
num=int(input("enter a num:"))
reverse=0
temp=num

while num!=0:
    rem=num%10
    reverse=reverse*10+rem
    num=num//10

if reverse==temp:
    print("palindrome")
else:
    print("not palindrome")

def is_palindrome(num):
    reverse=0
    temp=num
    while num!=0:
        reverse=reverse*10+(num%10)
        num=num//10
    return temp==reverse
if is_palindrome(121):
    print("palindrome")
else:
    print("not palindrome")
    