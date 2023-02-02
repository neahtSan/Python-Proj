def sum_num(a,b):
    return a + b

def test_lambda(func):
    return func(1,2)

print(test_lambda(sum_num))
print(test_lambda(lambda a,b : a + b))

print('------------------')

def list_plus_five(list):
    ans = []
    for i in list:
        ans.append([i, i+5])
    return ans

def test_lambda_list(func):
    return func([1,2,3])

print(test_lambda_list(list_plus_five))
print(test_lambda_list(lambda a: [a, a+5]))