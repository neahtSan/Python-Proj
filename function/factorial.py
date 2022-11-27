def factorial(number):
    if number == 1:
        return number
    return number * factorial(number - 1)

def check_factorial(number):
    ans = 1
    for i in range(number-1):
        ans *= number - i
    return ans



print(f'This is from factorial function \n {factorial(5)}')
print(f'This is from check_factorial function \n {check_factorial(5)}')

print(f'This is from factorial function \n {factorial(20)}')
print(f'This is from check_factorial function \n {check_factorial(20)}')

print(f'This is from factorial function \n {factorial(100)}')
print(f'This is from check_factorial function \n {check_factorial(100)}')