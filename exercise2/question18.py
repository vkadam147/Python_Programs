# 18. Print all odd numbers between 1 and N.

def odd_range(start,end):
    for i in range(start,end):
        if i%2!=0:
            print(i)
odd_range(10,20)
