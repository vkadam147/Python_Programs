# 8. Reverse a number using a loop.
num=int(input("Enter a num:"))
reverse=0

while num!=0:
    rem=num%10
    reverse=reverse*10+rem
    num=num//10
print(reverse)


def reverse_no(num):
    reverse=0
    while num!=0:
        rem=num%10
        reverse=reverse*10+rem
        num=num//10
    return reverse
num1=int(input("enter a no"))
print(reverse_no(num1))