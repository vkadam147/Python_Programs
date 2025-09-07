# 16. Find the largest of three numbers using if-else.

def largest_no(no1,no2,no3):
    if no1>no2 and no1>no3:
        return no1
    elif no2>no1 and no2>no3:
        return no2
    else:
        return no3
a=int(input("enter a no")) 
b=int(input("enter a no"))    
c=int(input("enter a no"))    

print(largest_no(a,b,c))
    
   