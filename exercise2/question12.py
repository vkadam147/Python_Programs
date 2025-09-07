#   12. Check whether a number is prime.

num=int(input("enter a num:"))

flag=True
for i in range(2,num):
    if num%i==0:
        flag=False
        break
if flag:
    print("prime")
else:
    print("not prime")


def is_prime(num):
    for i in range(2,num):
        if num%i==0:
            return False
    return True

if is_prime(num):
    print("prime")
else:
    print("not prime")














