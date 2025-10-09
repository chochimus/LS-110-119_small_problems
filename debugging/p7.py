def sum_times_factor(numbers, factor):
    return factor * sum(numbers)

numbers = [1, 2, 3, 4]
print(sum_times_factor(numbers, 2) == 20)

# Redifining sum function and also trying to call redefined function with one argument. Rename outer function.