import copy

original = [[1], [2], [3]]
copied = copy.deepcopy(original)

original[0][0] = 99

print(copied[0] == [1])

# shallow copy so nested structures can still be altered by the original. Fix: use deepcopy