"""
   Collectors: list
   Definition: array, vectors. We can save different types of values
   Start index 0
   list = [] | list()
"""
variable_list = [23, True, "char"]
students = ["Tom", "Mary", "Lewis", "Anna", "Harry"]
numbers = list(range(12, 21))

#Deleted
variable_list.remove(True)
variable_list.pop()
numbers.pop(0)
print(variable_list)
print(numbers)

#Index used
students[4] = "Carl"
print(students[0:3])
print(students[3:])
print(students[3])
print(students[-1])
print(students.index("Anna"))

#Add
students.append("Harry")
students.extend(["Johana", "Caroline", "Robert", "Anna"])
students.insert(2, "Mel")
new_list = variable_list + students
print(new_list*3)

print("Tomas" in students)

for student in students:
    print(f"Hi {student}!")

#multidimesion list
contact_person = [
    ["Jhon", "678234567"],
    ["Carol", "666432987"],
    ["Robert", "63451233896"],
]

print(contact_person[1][1])

#predifined function
numbers.sort()
numbers.reverse()
len(numbers)
print(students.count("Anna"))