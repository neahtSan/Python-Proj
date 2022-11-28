'''
Python: Recursion - Exercise from w3resource (https://www.w3resource.com/python-exercises/data-structures-and-algorithms/python-recursion.php)
'''

# 1. Write a Python program to calculate the sum of a list of numbers

def sum_list(num):
    if len(num) == 1:
        return num[0]
    return num[0] + sum_list(num[1:])

print(sum_list([1, 2, 3, 4, 5]))

# 2. Write a Python program to converting an Integer to a string in any base.

'''
skip for now
'''

# 3. Write a Python program of recursion list sum.

def sum_list_advance(numList):
    ans = 0
    for i in numList:
        if type(i) == int:
            ans += i
        else:
            ans = ans + sum_list_advance(i)
    return ans

print(sum_list_advance([1, 2, [3,4], [5,6]]))

# 4. Write a Python program to get the factorial of a non-negative integer

def factorial(num):
    if num == 1:
        return num
    return num * factorial(num - 1)

print(factorial(5))

# 5. Write a Python program to solve the Fibonacci sequence using recursion -> return list of fibonanci

'''
don't understand 
'''

# 10. Write a Python program to calculate the value of 'a' to the power 'b'

def power(a,b):
    if b == 1:
        return a
    return a * power(a, b-1)

print(power(3,4))


























