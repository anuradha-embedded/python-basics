# For Loop

veggies = ["Potato", "Bringel", "Lady finger", "Tomato", "Carrot"]

for veggi in veggies:
    print (veggi)
    
# For loop for tuple

tup = (1,2,4,5,6,3)

for val in tup:
    print (val)
    
# Print the elements of the following list using a loop:
# [1, 4, 9, 16, 25, 36, 49, 64, 81,100]

list = [1, 4, 9, 16, 25, 36, 49, 64, 81,100]

for el in list:
    print (el)

# Search for a number x in this tuple using loop:
# [1, 4, 9, 16, 25, 36, 49, 64, 81,100]

nums = (1, 4, 9, 16, 25, 36, 49, 64, 81,100)
x = 49
idx = 0

for num in nums:
    
    if(num == x):
        print ("Found x at idx:", idx)
        
        break
    idx +=1
else:
    print ("END")
    
# range() function in for loop

# seq = range(10)

# for i in seq:
for i in range(5): #range(stop)
    print (i)
    

    # for even number
for i in range(2,15,2):   #range(stsrt,stop,step)
    print (i) 
    
# Print numbers from 1 to 100.

for i in range(1,101):#range(stsrt,stop)
    # print (i)
    pass

print ("Empty")


# Print numbers from 100 to 1.

for i in range(100,0,-1): #range(stsrt,stop,step)
    print (i)

# Print the multiplication table of a number n.
# using for & range( )

n = int(input("Enter the number:",))

for i in range(1,11):
    print (i * n)
    
# WAP to find the factorial of first n numbers. (using for)

n = int(input("Enter the number:",))
fact = 1

for i in range(1, n+1):
    fact *= i
    i += 1
    
print ("Factorial of n =", fact)