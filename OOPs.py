#OOPs: object oriented programming.


class Car:
    color = "Blue"
    make = "BMW"
    model = "X5"
    
car1 = Car()
print (car1.color)

car2 = Car()
print (car2.make)
print (car2.model)


class Student:
    
    college_name = "IIT" # Class Attribute
    name = "Unknown"
    # # Default Constructor
    # def __init__(self):
    #   pass
    
    # Parameterized Constructor
    def __init__(self,name,roll_No,marks):
        self.name = name #Object Attribute
        self.roll_No = roll_No
        self.marks = marks
        
    def welcome(self):
        print ("Welcome Student!", self.name)
        
    def get_marks(self):
        return self.marks
        
    
    
s1 = Student("Abhay",20,[89,91,94])

s1.welcome()
print (s1.name)
print (s1.get_marks())
# print (s1.marks)
print (s1.roll_No)
print (s1.college_name)

s2 = Student("Vivek",40,86)
s2.welcome()
print (s2.name)
print (s2.marks)
print (s2.roll_No)
print (Student.college_name)

# Create student class that takes name & marks of 3 subjects as arguments in constructor.
# Then create a method to print the average.

class Students:
    
    # def __init__(self,name,math,physics,chemistry):
    def __init__(self,name,marks):
        
        self.name = name
        self.marks = marks
        
    @staticmethod
    def hello():
        print ("Hello Everyone")
        
    def average(self):
        # average = (self.math+self.physics+self.chemistry)/3
        sum = 0
        for val in self.marks:
            sum += val
        average = sum / len(self.marks)
        print ("Average marks of", self.name, "is:", average)
        
        return average
        
s1 = Students("Karan",[96,98,94])
s1.hello()
print (s1.name)
print (s1.average())

s1.name = "Rahul"
print (s1.average())


# Abstraction: Hiding the implementation details from the user. User only knows what the object does instead of how it does it.
class Car:
    
    def __init__(self):
        
        self.acc = False
        self.clutch = False
        self.brk = False
        
    def start(self):
        
        self.clutch = True
        self.acc = True
        
        print ("Car Started.")
        
car1 = Car()
car1.start()


# Create Account class with 2 attributes - balance & account no.
# Create methods for debit, credit & printing the balance.

class Account:
    
    def __init__(self,bal,acc):
        
        self.balance = bal
        self.account_no = acc
     # Debit Method
    def debit(self,amount):
        self.balance -= amount 
        print ("Rs", amount,"was debited from your account no:", self.account_no)
        print ("Total Balance=", self.get_balance())
        
    # Credit Method
    def credit(self,amount):
        self.balance += amount
        print ("Rs", amount,"was credited in your acount no:", self.account_no)
        print ("Total Balance=", self.get_balance())
        
    # Printing the balance method
    def get_balance(self):
        return self.balance
       
        
        
        
acc1 = Account(10000,1235468)
acc1.debit(1000)
acc1.credit(600)
acc1.credit(60000)
acc1.debit(10000)

# print (acc1.balance)
# print (acc1.account_no)