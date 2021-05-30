"""
   Collectors: tuple
   Definition: INMUTABLE array, vectors. We can save different types of values
   Characteristic: faster, less memory space.
   Dictionaries: Tuple can be key, but list can´t.
   Start index 0 (equals use of index)
   tuple = ()
"""
example_tuple = ("Jhon", "apple", 23, None, True, 4.56)

#Parse from list to tuple
example_list = list(example_tuple)

#Parse from tuple to list
example_tuple = tuple(example_list)

#Unpaked
name1, fruit, age, nothing, is_green, cm = example_tuple
print(age)