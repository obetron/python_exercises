"""
Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn. Go to the editor
Sample value of n is 5
Expected Result : 615
"""

n = int(input('Enter values of n:'))
n1 = int('%s' %n)
n2 = int('%s%s'%(n,n))
n3 = int('%s%s%s'%(n, n, n))
print(n1+n2+n3)

a = int(input('Enter values of a:'))
a1 = str(a) + str(a)
a2 = str(a) + str(a) + str(a)
print(a + int(a1) + int(a2))
