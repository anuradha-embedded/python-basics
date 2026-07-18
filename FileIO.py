

f = open("Demo.txt", "r")
# data = f.read()
# print(data)

line1 = f.readline()
print(line1)

line2 = f.readline()
print(line2)

# print(type(data))
f.close()

f = open("Demo.txt", "r+")
f.write("This is a demo file for testing purpose")
print(f.read())


f = open("Demo.txt", "w+")
f.read()
f.write("This is a demo file")
print(f.read())


f = open("Demo.txt", "a+")
f.read()
f.write("\nI am Anuradha Tiwari Parasar")
print(f.read())

with open("Demo.txt", "r") as f:
    data = f.read()
    print(data)
    
with open("Demo.txt", "w") as f:
    f.write("This is a demo file for testing purpose")
    
    # Delete the file
    
    # import os
    # os.remove("Sample.txt")
    
    
# Create a new file “practice.txt” using python. Add the following data in it:
# Hi everyone
# we are learning File I/O

# using Java.

# I like programming in Java.

# with open("practice.txt", "w") as f:
#     f.write("Hi everyone\n")
#     f.write("we are learning File I/O\n")
#     f.write("using Java.\n")
#     f.write("I like programming in Java.\n")

# WAF that replace all occurrences of “java” with “python” in above file.
with open("practice.txt", "r") as f:
    data = f.read()
    
new_data = data.replace("java", "python")

with open("practice.txt", "w") as f:
    f.write(new_data)
    
print(new_data)

# Search if the word “learning” exists in the file or not.

# word = "learning"
# with open("practice.txt", "r") as f:
#     data = f.read()
# if (data.find(word) != -1):
#     print("Word exists in the file")
    
# else:
#     print("Word does not exist in the file")
    
    
# WAF to find in which line of the file does the word “learning”occur first.
# Print -1 if word not found.

def check_for_line():
    word = "learning"
    data = True
    line_no = 1
    with open("practice.txt", "r") as f:
        while data:
            data = f.readline()
            if (word in data):
                print("Word exists in line no:", line_no)
                return line_no
            
            line_no += 1
    print("-1")
    
check_for_line()


# From a file containing numbers separated by comma, print the count of even numbers.

with open("Numbers.txt", "r") as f:
    data = f.read()
    print(data)
    
    # num = " "
    # for i in range(len(data)):
    #     if (data[i] == ","):
    #         print(int(num))
    #         num = " "
            
    #     else:
    #         num += data[i]
            
        #     num += data[i]
        # else:
        #     if (int(num) % 2 == 0):
        #         print(num)
        #     num = " "
    nums = data.split(",")
    print(nums)
    count = 0
    for val in nums:
        if (int(val) % 2 == 0):
            count += 1
    print("Count of even numbers:", count)
            
        