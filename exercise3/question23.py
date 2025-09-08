# 23. Find the sum of squares of digits of a number.

def sum_of_sq(num):
    sum=0

    while num!=0:
        rem=num%10
        sum=sum+rem**2
        
        num=num//10
        print("asus vivobook")
    return sum
print(sum_of_sq(234))

