# weakly typed#############
text = "Python course"
print(text); text = 34; print(text)

#concatenate################
greating = "Hi!"
course = "This is the course"
number = 1

print("Example:{}".format(number))
print(f"{greating} {course} {number}")

#data type################
null = None
string = "text"
integer = 99
decimal = 0.45
boolean = True
byte = b"Hi"
range= range(9)
print(type(boolean))

#collection################
list_example = [10, "twenty", 30]
tuple_example = ("unmodifiable", "element")
dictionary = {
    "name": "lourdes",
    "course": "python"
}

#conversion################
number_text = 23
number_value = int(number_text)
decimal = str(number_text / 10)
decimal = float(decimal)

#mathematical operators####
first = 77
second = 34
third = 2

subtract = first - second
sum = first + second
divide = second / third
rest_division = first % third
multiplication = second * third

#assignment################
age = 55
age += 5

#input / output data#######
name = input("What is your name?")
print(f"Welcome {name}!")
