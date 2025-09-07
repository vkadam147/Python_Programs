#2. Find whether a number is even or odd

# Without using any function

num=int(input("Enter a no:"))
if num%2==0:
    print("even no")
else:
    print("odd no")

#with user defined fun with parameter abd return
def is_even_odd(num):
    return num%2==0

num=int(input("Enter a no:"))
if is_even_odd(num):
    print("even")
else:
    print("odd")