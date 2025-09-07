# 5. Find the factorial of a number using a loop.

num=int(input("enter a no"))
fact=1
while num!=0:
    fact=fact*num
    num-=1
print(fact)


def fact(num):
    fact1=1
    for i in range(1,num+1):
        fact1=fact1*i
    return fact1
num1=int(input("enter a no"))

print(fact(num1))
