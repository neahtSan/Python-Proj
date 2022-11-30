'''
Python basic (Part -I) [150 exercises with solution]
src: https://www.w3resource.com/python-exercises/python-basic-exercises.php
'''

#2
import sys
 
print("User Current Version:-", sys.version)

#3
import time
from datetime import datetime, date

now = datetime.now()

current_time = now.strftime("%H:%M:%S")

print(f'time {current_time} \ndate {date.today()}')