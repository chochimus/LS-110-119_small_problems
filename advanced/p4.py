"""
Problem:
Write a function that takes two sorted lists as arguments and returns a new list
that contains all the elements from both input lists in ascending sorted order. 
You may assume that the lists contain either all integer values or all string values.

You may not provide any solution that requires you to sort the result list.
You must build the result list one element at a time in the proper order.

Your solution should not mutate the input lists.

input: two sorted lists
output: all elements from both input lists in ascending sorted order

rules:
    explicit
    - assums lists contian either all integer values or all string values
    - may not provide any solution that requires you to sort the result list
    - build result list one element at a time in the proper order
    - should not mutate input lists
    implicit:
    - expect valid input/ no bad input handling necessary
    - lists may be empty

datastructure:
lists

algorithm:
two pointers solution
1.) create two pointers i,j = 0 and answer list = []
2.) if element[i] < element[j] append element[i] to answer, otherwise element[j]
3.) increment whichever pointer was smaller
4.) repeat until either pointer is at the end
5.) append remaining elements from either lists if remaining
6.) return answer
"""

def merge(list1, list2):
    i = j = 0
    answer = []
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            answer.append(list1[i])
            i += 1
        else:
            answer.append(list2[j])
            j += 1
    while i < len(list1):
        answer.append(list1[i])
        i += 1
    while j < len(list2):
        answer.append(list2[j])
        j += 1

    return answer

# All of these examples should print True
print(merge([1, 5, 9], [2, 6, 8]) == [1, 2, 5, 6, 8, 9])
print(merge([1, 1, 3], [2, 2]) == [1, 1, 2, 2, 3])
print(merge([], [1, 4, 5]) == [1, 4, 5])
print(merge([1, 4, 5], []) == [1, 4, 5])

names1 = ['Alice', 'Kim', 'Pete', 'Sue']
names2 = ['Bonnie', 'Rachel', 'Tyler']
names_expected = ['Alice', 'Bonnie', 'Kim', 'Pete',
                  'Rachel', 'Sue', 'Tyler']
print(merge(names1, names2) == names_expected)