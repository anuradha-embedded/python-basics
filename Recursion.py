
#Recursion

#prints n to 1 backwards
# Recursive function
def show(n):
    if (n==0):
        return
    print(n)
    show(n-1)
    
show(6)

# Return Factorial of n

def fact(n):
    if(n == 0 or n == 1):
        return 1
        
    else:
        return n * fact(n-1)
        
        
print (fact(6))

# Write a recursive function to calculate the sum of first n natural numbers.

def calc_sum (n):
    if(n == 1):
        return 1
    else:
        return n + calc_sum(n-1)
        
        
print (calc_sum(4))

# Write a recursive function to print all elements in a list.
# Hint : use list & index as parameters.

def print_list(list,idx=0):
    if(idx == len(list)):
        return
    print(list[idx])
    print_list(list,idx+1)
    
fruits = ["Mango", "Apple", "Banana", "Pears", "Grapes", "Papaya"]
print_list(fruits)

