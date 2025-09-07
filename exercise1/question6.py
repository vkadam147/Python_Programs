# 6. Print the multiplication table of a given number.

num=int(input("enter a no"))

for i in range(1,11):
    print(f"{num} X {i} = {num*i}")

def mul(num):
    for i in range(1,11):
        print(f"{num} X {i} = {num*i}")
mul(num)


start=int(input("enter start"))
end=int(input("enter end"))

# for i in range(start,end+1):
#     for j in range(1,11):
#         print(f"{i} x {j} ={i*j}")
#     print("----------------------------------------------")

for i in range(start,end+1):
    mul(i)