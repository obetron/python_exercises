"""
Write a Python program to accept a filename from the user and print the extension of that. Go to the editor
Sample filename : abc.java
Output : java
"""

filename = input('Enter filename: ')
filenameList = filename.split('.')
print('Output:', filenameList[-1])
print('Output:', repr(filenameList[-1]))
