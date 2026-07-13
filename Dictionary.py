# Dictionary

info = {
    "Name": "Anuradha",
    "Learning": "Python",
    "Subjects": ["C++", "Python", "Java"],
    "Topics": ("Dictionary", "Sets"),
    "Age": 24,
    "Marks": 96.75,
    "is_adult": True,
}

print (type(info))

info["Name"] = "AnuradhaTiwari"
info["Surname"] = "Parasar"
print (info["Name"])
print (info)

null_dict ={}
null_dict["name"] = "Anu"
print (null_dict)

# Nested Dictionary

student = {
    "name": "AnuTiwari",
    "score":{
        "Math": 98,
        "Chem": 97,
        "Physics": 95
    }
}

print (student)
print (student["score"])
print (student["score"]["Math"])

# Dictionary Methods

# print (info.keys())
print (list(info.keys()))
print (list(student.values()))
print (list(student.items()))
print (student.get("name"))

pairs = list(student.items())
print (pairs[0])

new_dect = {"City" : "Delhi"}
student.update(new_dect)
# student.update({"City" : "Delhi"})
print (student)



# Store following word meanings in a python dictionary
# table : "a piece of furniture", "List of facts & figures"
# cat : "a small animal"

dict = {
    "table" : ["a piece of furniture", "List of facts & figures"],
    "cat" : "a small animal"
}

print (dict)


# WAP to enter marks of 3 subjects from the user and store them in a dictionary. Start with an empty dictionary & add one by one. Use subject name as key & marks as value.

subjects = {}

x = int(input("Enter Physics marks: "))
subjects.update({"Physics" : x})

y = int(input("Enter Chemistry marks: "))
subjects.update({"Chemistry" : y})

z = int(input("Enter Math marks: "))
subjects.update({"Math" : z})


print (subjects)
