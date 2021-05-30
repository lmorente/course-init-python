"""
   Collectors: dictionary
   Structure: clave - valor
   The key is unique
   Different types of values
   dictionary = {}
"""

country = {
    "Germany": "Berlin",
    "UK": "London",
    "Spain": "Madrid",
    "Russia": "Moscow"
}

print(country["UK"])

country["Italy"] = "Lisbon"
country["Italy"] = "Rome"
del country["UK"]

