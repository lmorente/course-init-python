"""
 for
 while
 (continue, pass, else, break)
"""
# range(2) = range(0,2) = [0, 2)
for i in range(2):
    print("Hi!", end=" ")


#mail evaluator example
def mail_evaluator(mail):
    result = False
    for i in mail:
        if i == "@":
            result = True
    return result

user_mail = input("What is your mail?")
print(mail_evaluator(user_mail))

#color example
def my_favorite_color_evaluator(color):
    return color.lower() == "blue"

answer = False
attempts = 0

while answer == False:
    attempts += 1
    user_color = input("Do you know my favorite color?")
    answer = my_favorite_color_evaluator(user_color)
    if attempts == 2:
        break

#character counter example
def character_counter (input):
    counter = 0
    for i in input:
        if i == " ":
            continue
        counter += 1
    return counter

variable = input("We evaluate your text. Enter text:")
print(character_counter(variable))