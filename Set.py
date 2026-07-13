# Set

collection = {1,2,4,5, "Hello", "World",5,2,"Hello"}

print (collection)
print (type(collection))
print (len(collection))

null_set = set() # Empty Set
print (null_set)

# Set Methods
null_set.add(6)
null_set.add(7)
null_set.add(8)
null_set.add(9)
null_set.add("Anu")
null_set.add((1,2,3))
print (null_set)

null_set.remove(9)
null_set.pop()
print (null_set)

null_set.clear()
print (null_set)

set1 = {2,3,4,5}
set2 = {4,5,6,7}

print (set1.union(set2))
print (set1.intersection(set2))



# You are given a list of subjects for students. Assume one classroom is required for 1
# subject. How many classrooms are needed by all students.

# ”python”,“java”,“C++”,“python”,“javascript”,“java”,“python”,“java”,“C++”,“C”

subjects = {
    "python", "java", "C++", "python", "javascript", "java", "python", "java", "C++", "C"
}

print (subjects)
print (len(subjects))

# Figure out a way to store 9 & 9.0 as separate values in the set.(You can take help of built-in data types)

values = {9, "9.0"}
values = {"9", 9.0}
values = {
    ("int" , 9),
    ("float", 9.0)
}
print (values)

