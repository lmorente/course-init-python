"""
  Predifined funtion: print(), type(), del, len(), upper(), lower(), ...
  create own function
  optional parameters
  lambda function: anonymous function
"""

def sum(one_number, two_number):
    return one_number + two_number

print(sum(23,2))


def print_employee(name, dni = None):
    print(f"The name is {name}")
    if dni != None:
        print(f"{name}´s dni is {dni}")

print_employee("Anna", "12345678-L")
print_employee("Jhon")


get_current_year = lambda year: f"Year is {year}"
print(get_current_year(2021))