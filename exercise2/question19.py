# 19. Find the power of a number without using the ** operato

# base=5
# power=3
# pow=1
# for x in range(power):
#     pow=pow*base
# print(pow)


def power(base,power1):
    pow=1
    for x in range(power1):
        pow=pow*base
    return pow
print(power(20,3))
