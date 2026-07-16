# Functions

# def sum (a,b):
#     s = a + b
#     print (s)
#     return s
    
# sum(5,7)
# sum(4,11)
# sum(8,10)

# Function Defination
def calc_sum (a,b): #Parameters
    return a +b
    
sum = calc_sum(127, 342) #Function call; Arguments
print (sum)

# Calculate average of 3 values

def calc_avg (a,b,c):
    avg = (a + b + c) / 3
    print (avg)
    return avg
    
calc_avg(5,7,8)
    
# def calc_avg (a,b,c):
#     return (a + b + c) / 3
  
# avg = calc_avg(6,7,8)
# print (avg)

print ("Anuradha", end = "$")
print ("Tiwari")

# Default Parameter

def calc_prod (a=1, b=2):
    print(a * b)
    return a * b
    
calc_prod()

# WAF to print the length of a list. ( list is the parameter)

cities = ["Delhi", "Gurgaon", "Noida", "Pune", "Mumbai"]
fruits = ["Mango", "Apple", "Banana", "Pears", "Grapes", "Papaya"]

def print_len (list):
    print (len(list))
    return len
    
print_len (cities)
print_len (fruits)
    

# WAF to print the elements of a list in a single line. ( list is the parameter)

nums = [2,4,6,8,10,12]

# def print_el (list):
#     print (list)
#     return list
    
# print_el (nums)

def print_list(list):
    for element in list:
        print (element, end = " ")
        
print_list(nums)
print()

# WAF to find the factorial of n. (n is the parameter)

def calc_fact (n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
        
    print (fact)
    
calc_fact (6)

# WAF to convert USD to INR.

def converter(usd_val):
    inr_val = usd_val * 96.60
    
    print (usd_val,"USD =", inr_val, "INR")
    
converter(5)