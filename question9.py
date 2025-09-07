# 9. Find the sum of digits of a number.

num=int(input("Enter a num:"))
sum=0

while num!=0:
    rem=num%10
    sum=sum+rem
    num//=10
print(sum)

def sum_of_digits(num):
    sum=0
    while num!=0:
        rem=num%10
        sum=sum+rem
        num//=10
    return sum
print(sum_of_digits(123))