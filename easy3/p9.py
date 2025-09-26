"""
Problem:
Write a function that takes a list as an argument and reverses its elements, in place. 
That is, mutate the list passed into the function. The returned object should be the 
same object used as the argument.

You may not use the list.reverse method nor may you use a slice ([::-1]).

input: list
output: list reversed in place

rules:
    explicit:
    - cannot use list.reverse or slice
    - in place reversal
    implicit:
    - same list should be returned 

datastructure:
list

algorithm:
1.) create left pointer equal to zero
2.) create right pointer equal to length of list - 1
3.) swap list[left] with list[right]
4.) increment left and decrement right
5.) repeat until left > right
6.) return list
"""

def reverse_list(input_list):
    left = 0
    right = len(input_list) - 1

    while left < right:
        input_list[left], input_list[right] = input_list[right],input_list[left]
        left += 1
        right -= 1
    
    return input_list

list1 = [1, 2, 3, 4]
result = reverse_list(list1)
print(result == [4, 3, 2, 1])               # True
print(list1 is result)                      # True

list2 = ["a", "b", "c", "d", "e"]
result2 = reverse_list(list2)
print(result2 == ['e', 'd', 'c', 'b', 'a']) # True
print(list2 is result2)                     # True

list3 = ["abc"]
result3 = reverse_list(list3)
print(result3 == ['abc'])                   # True
print(list3 is result3)                     # True

list4 = []
result4 = reverse_list(list4)
print(result4 == [])                        # True
print(list4 is result4)                     # True