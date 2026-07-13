# while loop

count = 1

while count <= 5:
    print ("Hello")
    count += 1
    
  # Print  odd numbers from 1 to 100.
i = 1

while i <= 100:
    
    if (i % 2 == 0):
        i += 1
        continue
    print (i)
    i += 1
print ("Loop Ended")

i = 100

#  # Print numbers from 100 to 1.
while i >= 1:
    print (i)
    i -= 1

print ("Loop Ended")

# Print the multiplication table of a number n.

n = int(input("Enter the number:",))
i = 1
while i <= 10:
    print (n * i)
    i += 1
    
# Print the element of the following list using a loop: [1,4,9,16,25,36,49,68,81,100]

nums = [1,4,9,16,25,36,49,68,81,100]
idx = 0
while idx < len(nums):
    print (nums[idx])
    idx += 1
    
    

# Search for a number x in this tuple using a loop: (1,4,9,16,25,36,49,68,81,100)

nums = (1,4,9,16,25,36,49,68,81,100)

x = 36
idx = 0
while idx < len(nums):
    
    if (nums[idx] == x):
        print ("Found Number x at idx =", idx)
        
        break
        
    else:
        print("Finding..")
    idx += 1
    
    
# WAP to find the sum of first n numbers. (using while)

n = int(input("Enter the number:",))

sum = 0
i = 1
while i <= n:
    sum += i
    i += 1

print ("Total sum =",sum)