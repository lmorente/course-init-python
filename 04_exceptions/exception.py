#Name excception
try:
    name = input("What is your name?:")

    if(len(name)) > 1:
        completed = "Name is " +  name

    print(completed)
except:
    print("name not completed")
else:
    print("name is correct")
finally:
    print("end")

#Multiple exceptions
"""
except Exception as e:
    print(e._name())
"""
try:
    number = input("Number:")
    print(number*number)
except TypeError:
    print("Must be a number")
except ValueError:
    print("Input a number")

#own exception
age = int(input("How old are you?"))

if age < 0 or age > 100:
    raise ValueError("Age value is not correct")