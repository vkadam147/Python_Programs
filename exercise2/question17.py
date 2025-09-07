# 17. Print all even numbers between 1 and N.

def even_range(start,end):
    for i in range(start,end+1):
        if i%2==0:
            print(i)
even_range(1,10)