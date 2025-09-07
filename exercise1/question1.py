# 1. Check whether a number is positive, negative, or zero.
# Without using any function
num=int(input("enter a no:"))
if num<0:
    print("negative")
elif num>0:
    print("positive")
else:
    print("zero")

# With user defined function with parameter without return 

def is_positive(num):
    if num<0:
        print("negative")
    elif num>0:
        print("positive")
    else:
        print("zero")
num=int(input("enter a no:"))
is_positive(num)
