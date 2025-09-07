# 24. Check whether a number is a Strong number (sum of factorials of digits = number).

def factorial(num):
    fact=1

    while num!=0:
        fact=fact*num
        num-=1
    return fact

def is_strong(num):
    temp=num
    sum=0
    while num!=0:
        rem=num%10
        sum=sum+ factorial(rem)
        num=num//10
    return temp==sum
if is_strong(135):
    print("strong no")
else:
    print("not strong no")

for i in range(1,10000):
    if is_strong(i):
        print(i)