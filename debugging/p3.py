def multiply_list(lst):
    for idx in range(len(lst)):
        lst[idx] *= 2

    return lst

print(multiply_list([1, 2, 3]) == [2, 4, 6])

# In this instance we are multiplying the item in the list by 2, but this value isn't mutating the list and is 
# simply multiplying a copy of the value. If we want to instead alter the original list we should act on its index.
# If instead we want a new list we could use a comprehension:

def multiply_list2(lst):
    return [item * 2 for item in lst]