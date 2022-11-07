#!/bin/python3

x = [4, True, 'Hi'] #Here x is a reference to the list and to copy the list we need to use y=x[:]
x.append('Hello')
x.extend([1, 2, 3, 4, 5])
x.pop(2)
x[0] = 6
print(x)
