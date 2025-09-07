# 15. Check whether a number is an Armstrong number.

def is_arm(num):
    arm=0
    temp=num

    while num!=0:
        rem=num%10
        arm=arm+(rem**3)
        num=num//10
    # return temp==arm
    if temp==arm:
        return True
    else:
        return False
if is_arm(123):
    print("arm")
else:
    print("not arm")
