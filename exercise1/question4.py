# 4. Find the sum of the first N natural numbers.

start=int(input("enter start"))
end=int(input("enter end"))
sum=0
for i in range(start,end+1):
    sum=sum+i
print(sum)

def sum_of_n(start,end):
    sum=0
    while start<=end:
        sum=sum+start
        start+=1
    return sum

print(sum_of_n(start,end))