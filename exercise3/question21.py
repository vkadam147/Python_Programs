# 21. Find all Armstrong numbers between 1 and 1000.

def is_arm(num):
    temp=num
    sum=0
    while num!=0:
        rem=num%10
        sum=sum+rem**3
        num=num//10
    return temp==sum
def arm_range(start,end):
    for x in range(start,end+1):
        if is_arm(x):
            print(x)
arm_range(1,1000)

    
    




    