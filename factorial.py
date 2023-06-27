# using recursion
# 1!=1
# 2!=2*1
# 3!=3*2*1
# 4!=4*3*2*1
# 5!=5*4*3*2*1
def factorial(num):
    if num == 1 or num == 0:
        return num
    else:
        return num * factorial(num - 1)


print(factorial(5))
