# 22. Find all palindrome numbers between 1 and 500.

def is_palindrome(num):
    reverse=0
    temp=num

    while num!=0:
        rem=num%10
        reverse=reverse*10+rem
        num=num//10
    return temp==reverse

def palindrome_range(start,end):
    for x in range(start,end):
        if is_palindrome(x):
            print(x)
palindrome_range(1,500)