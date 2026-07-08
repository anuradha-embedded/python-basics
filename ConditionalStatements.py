
light = "Green"

if(light == "Red"):
    print ("Stop")
    
elif(light == "Yellow"):
    print ("Wait")
    
elif(light == "Green"):
    print ("Go")
    
else:
    print ("Light is not working")
    
    
    #Nesting 
age =84

if(age >= 18):
    
    if(age > 80):
        print ("Can not Vote.")
        
    else:
         print ("Can Vote.")
        
else:
    print ("Can not Vote.")
    
    
marks = int(input("Enter student marks:"))

if(marks >= 90):
    grade = "A"
    
elif(marks >= 80 and marks < 90):
    grade = "B"
    
elif(marks >= 70 and marks < 80):
    grade = "C"
    
elif(marks >= 40 and marks < 70  ):
    grade = "D"
    
else:
    print ("Fail")

print ("Grade of Student:", grade)
    
    
    
# WAP to find the greatest of 3 numbers entered by user.

a = int(input("First number = " ))
b = int(input("Second number = " ))
c = int(input("Third number = " ))

if(a>b and a>c):
    print ("Greatest number is: ", a)
    
elif(b>c):
    print ("Greatest number is: ", b)
    
else:
    print ("Greatest number is: ", c)