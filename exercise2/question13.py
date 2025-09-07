# 13. Print all prime numbers between 1 and N

def is_prime(num):
    for i in range(2,num):
        if num%i==0:
            return False
    return True

def prime_range(start,end):
    for i in range(start,end+1):
        if is_prime(i):
            print(i)

prime_range(1,30)
        





start=int(input("enter start:"))
end=int(input("enter end:"))

for i in range(start,end+1):
    flag=True
    for j in range(2,i):
        if i%j==0:
            flag=False
            break
    if flag:
        print(i)
    

