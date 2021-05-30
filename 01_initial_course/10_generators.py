"""
  def funcion_name():
       yield

  Retun iterable
  https://www.youtube.com/watch?v=TLVnoqXGWpY&list=PLU8oAlHdN5BlvPxziopYZRd55pdqFwkeS&index=19
  https://www.youtube.com/watch?v=ucaHqGII350&list=PLU8oAlHdN5BlvPxziopYZRd55pdqFwkeS&index=20
"""

def even_generate(limit):
    number = 1
    numbers = []
    while number < limit:
        numbers.append(number*2)
        number += 1
    return numbers


print(even_generate(8))

def even_generate_generators(limit):
    number = 1
    while number < limit:
        yield number*2
        number += 1


example = even_generate_generators(8)
print(next(example), next(example))

#* indeterminate numbers of element, type tuple
def cities_generate(*cities):
    for city in cities:
        for letter in city:
            yield letter

def cities_generate_from(*cities):
    for city in cities:
        yield from city

letters = cities_generate("Madrid", "Barcelona")
print(next(letters))

letters_from = cities_generate_from("Madrid", "Barcelona")
print(next(letters_from))