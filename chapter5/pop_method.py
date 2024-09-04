#my_dict = {"name": "Akash", "age": 21}
#age = my_dict.pop("age")
#print(age)  # Output: 21
#print(my_dict)  # Output: {'name': 'Akash'}

my_dict = {"name": "Akash", "age": 21}
item = my_dict.popitem()
print(item)  # Output: ('age', 21)
print(my_dict)  # Output: {'name': 'Akash'}
