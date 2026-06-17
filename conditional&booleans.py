
# language = 'java'    

# if language == 'Python':
#     print('language is python')
    
# elif language == 'C++':
#     print('language is C++')
    
# else:
#     print('No match')



# and
# or
# not

user = 'admin'
password = 'admin12'
logged_in = False

if not logged_in:
    print('Please log in')
    
else:
    print('Welcome back, admin')

# if user == 'admin' and password == 'admin123':

if user == 'admin' or password == 'admin123':
    print('Access granted')
else:
    print('Access denied')
    
    
    # use of 'is'
    
a = [1, 2, 3]
b = [1, 2, 3]

# print(a == b)  # Output: True
# print(id(a))  # Output: memory address of a
# print(id(b))  # Output: memory address of b
print(a is b)  # Output: False





# False Values in Python:
# - False
# - None
# - 0 (zero of any numeric type)
# - 0.0 (zero float)
# - None
# - Empty sequences and collections: '', [], {}, set(), etc.
# - Custom objects that implement __bool__() or __len__() to return False



condition = False
condition = None
condition = 0

if condition:
    print('Evaluated to True')
    
else:
    print('Evaluated to False')