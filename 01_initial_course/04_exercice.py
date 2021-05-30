"""
   Show by even numbers from 1 to 100
"""
def is_even(number):
    return number % 2 == 0

even_number = []
for i in range(1,101):
    if is_even(i):
        even_number.append(i)

print(even_number)