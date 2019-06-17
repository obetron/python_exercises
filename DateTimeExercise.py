"""
Write a Python program to display the current date and time.
Sample Output :
Current date and time :
2014-07-05 14:34:14
"""
import datetime

print(datetime.datetime.now())

str_datetime = datetime.datetime.now()
print('Current date and time :')
print(str_datetime.strftime('%Y-%m-%d %X'))
# %X is equal %H:%M:%S
print('Current date and time :')
print(str_datetime.strftime('%Y-%m-%d %H:%M:%S'))
