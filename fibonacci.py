#using recursion

def fibonacci(num):
    if num == 0 or num == 1:
        print(num)
    else:
        print((num-1)+(num-2))
fibonacci(8)