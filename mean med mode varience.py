num = [int(e) for e in input("Number : ").split()]

def mean(num):
    return sum(num)/len(num)

def median(num):
    num = sorted(num)
    if len(num) % 2 != 0:
        return num[len(num)//2]
    else:
        return (num[len(num)//2] + num[len(num)//2 - 1]) / 2

def mode(num):
    count = dict()
    for i in num:
        if i not in count:
            count[i] = 1
        else:
            count[i] += 1
    count = sorted(count.items(), key = lambda x : x[1] , reverse = True)
    return count[0]

def variance(num,mean):
    count = []
    for i in num:
        count.append((i - mean) ** 2)
    return sum(count)/len(count)

print("Here is your result!!!")
print("Mean = "+ str(mean(num)))
print("Median = "+str(median(num)))
print("Mode = "+str(mode(num)[0])+" and have frequency = "+str(mode(num)[1]))
print("Varirance = "+str(variance(num,mean(num))))

















































