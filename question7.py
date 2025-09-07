# 7. Count the number of digits in a number.

num=int(input("enter a no"))
a=str(num)
print(len(a))
count=0
while num!=0:
    num//=10
    count+=1
print(count)


def count_digits(num):
    count=0
    while num!=0:
        num//=10
        count+=1
    return count
print(count_digits(1000088))