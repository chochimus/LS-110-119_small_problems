"""
Problem:
Given a dictionary where both keys and values are unique, 
invert this dictionary so that its keys become values and its values become keys.

input: a dictionary with unique values and keys
output: a dictionary with inverted keys and values

rules: 
    explicit:
    - keys and values are unique
    implicit:
    - expect a valid dictionary input

datastructure:
dictionary

algorithm:
1.) get keys and values
2.) create a dictionary using the value as the key and the key as the value

"""

def invert_dict(dict1):
    return {value:key for key, value in dict1.items()}

print(invert_dict({
          'apple': 'fruit',
          'broccoli': 'vegetable',
          'salmon': 'fish',
      }) == {
          'fruit': 'apple',
          'vegetable': 'broccoli',
          'fish': 'salmon',
      })  # True