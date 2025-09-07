# 11. Print Fibonacci series up to N terms.


n1=0
n2=1

for i in range(1,12):
    print(n1)
    n3=n1+n2
    n1=n2
    n2=n3



def fibbonacci(num):
    n1=0
    n2=1
    for i in range(num+1):
        print(n1)
        n3=n1+n2
        n1=n2
        n2=n3
fibbonacci(10)

def is_fibbonacci(num):
    n1=0
    n2=1
    while True:
        if num==n1:
            return True
        if n1>num:
            return False
        n3=n1+n2
        n1=n2
        n2=n3
if is_fibbonacci(55):
    print("fibbonacci no")

else:
    print("not fibboo")

# Print Fibonacci numbers in the range 100 to 10000
start=int(input("enter start:"))
end=int(input("enter end"))
n1=0
n2=1
while True:
    if n1>=end:
        break
    if n1>=start:
        print(n1)
    
    n3=n1+n2
    n1=n2
    n2=n3

