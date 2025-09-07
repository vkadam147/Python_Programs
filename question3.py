# 3. Print numbers from 1 to 10 using a loop.

start=int(input("enter start"))
end=int(input("enter end"))

for i in range(start,end+1):
    print(i)


while start<=end:
    print(start)
    start+=1

def print_range(start,end):
    for i in range(start,end+1):
        print(i)
print_range(end=5,start=1)