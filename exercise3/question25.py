# 25. Check whether a number is a Perfect number (sum of proper divisors = num

def is_perfect(num):
    sum=0

    for i in range(1,num):
        if num%i==0:
            sum=sum+i
    return sum==num
if is_perfect(6):
    print("perfect")
else:
    print("not perfect")

for j in range(1,1000):
    if is_perfect(j):
        print(j)






