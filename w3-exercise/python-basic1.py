'''
Python basic (Part -I) [150 exercises with solution]
src: https://www.w3resource.com/python-exercises/python-basic-exercises.php
'''

#1 
sample = "Twinkle, twinkle, little star, How I wonder what you are! Up above the world so high, Like a diamond in the sky. Twinkle, twinkle, little star, How I wonder what you are"
ans = ''
for i in range(len(sample)):
    if sample[i] == 'T':
        for j in sample[i:]:
            if j!= '!' and j != '.' and j != 'H':
                ans += j
            if j == 'H':
                break
    if sample[i] == 'H':
        ans += '\n\t'
        for j in sample[i:]:
            if j != '!':
                ans += j
            else:
                ans += j
                break
    if sample[i] == 'U':
        ans += '\n\t\t'
        for j in sample[i:]:
            if j != ',':
                ans += j
            else:
                ans += ','
                break
    if sample[i] == 'L':
        ans += '\n\t\t'
        for j in sample[i:]:
            if j != '.':
                ans += j
            else:
                ans += '.'
                ans += '\n'
                break
    
    
print(ans)
        