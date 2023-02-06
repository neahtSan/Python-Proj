a = {1:2}
if 2 in a and type(a[2]) == int:
    print(5)

if 'op' in 'abop':
    print(1)
if 'a' in 'abop':
    print(1)
if 'b' in 'abop':
    print(1)
    
def ab(a,b):
    return a+b

x = ab(1,2)
print(x)


body = {'a':'1'}
a = int(body['a'])
print(a)