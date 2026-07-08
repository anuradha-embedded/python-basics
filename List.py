marks = [86.3, 64.8, 46.7, 78.2,94.1,46.7]

print (marks)
print (marks[1])
print (len(marks))
print ()

student = ["Aman", 78.2, 19, "Aligarh"]
print (student)
student[0] = "Vishal"
print (student)


# List Slicing

print (marks [1:4])
print (marks [ :5])
print (marks [2: ])
print (marks [-3:-1])


# List Methods
marks.append(88.1)
marks.sort()
print (marks)

marks.sort(reverse = True)
print (marks)

# marks.reverse()
marks.insert(1,92.5)

print (marks)

marks.remove(46.7)
marks.pop(0)
print(marks)


# WAP to ask the user to enter names of their 3 favorite movies & store them in a list

movie1 = str(input("Enter the name of 1st Favorite movie:",))
movie2 = str(input("Enter the name of 2nd Favorite movie:",))
movie3 = str(input("Enter the name of 3rd Favorite movie:",))

movies = [movie1, movie2, movie3]
print (movies)

# movies = []
# movies.append(str(input("Enter the name of 1st Favorite movie:",)))
# movies.append(str(input("Enter the name of 2nd Favorite movie:",)))
# movies.append(str(input("Enter the name of 3rd Favorite movie:",)))
# print (movies)



# movies = []
# movie1 = str(input("Enter the name of 1st Favorite movie:",))
# movies.append(movie1)
# movie2 = str(input("Enter the name of 2nd Favorite movie:",))
# movies.append(movie2)
# movie3 = str(input("Enter the name of 3rd Favorite movie:",))
# movies.append(movie3)
# print (movies)


# WAP to check if a list contains a palindrome of elements.

list1 = [1,2,3,2,1]
list2= [1,2,3,4]

copy_list1 = list1.copy()
copy_list1.reverse()
if(copy_list1 == list1):
    print("Palindrome")
    
else:
    print("Not Palindrome")
    
# Store the given values in a list & sort them from "A" to "D".

grade = ["C", "D", "A", "A", "B", "B", "A"]
grade.sort()
print (grade)