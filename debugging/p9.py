# data_set = {1, 2, 3, 4, 5}

# for item in data_set:
#   if item % 2 == 0:
#       data_set.remove(item)

# Trying to remove items from a list while iterating over it is a bad practice. Instead we should create a new
# object

data_set = {1, 2, 3, 4, 5}

new_set = {key for key in data_set if key % 2 == 0}

print(new_set)