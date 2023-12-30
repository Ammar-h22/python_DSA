# 1) Integers are immutable i.e they cannot be changed. 
#    Once we put a number lets say 11 into a particular place in the memory, 
#    then we cannot change that number 11.

# 2) Dictionaries are mutable i.e they can be changed.


# Integer example
num1 = 11
num2 = num1

print('Before updating the value of num2:')
print('num1 =', num1)
print('num2 =', num2)

print('\nnum1 points to:', id(num1))
print('num2 points to:', id(num2))

num2 = 22

print('\nAfter updating the value of num2:')
print('num1 =', num1)
print('num2 =', num2)

print('\nnum1 points to:', id(num1))
print('num2 points to:', id(num2))

# Dictionary example

dict1 = {'value': 11}
dict2 = dict1

print('\nBefore updating the value of dict2:')
print('dict1 =', dict1)
print('dict2 =', dict2)

print('\ndict1 points to:', id(dict1))
print('dict2 points to:', id(dict2))

dict2['value'] = 22

print('\nAfter updating the value of dict2:')
print('dict1 =', dict1)
print('dict2 =', dict2)

print('\ndict1 points to:', id(dict1))
print('dict2 points to:', id(dict2))
