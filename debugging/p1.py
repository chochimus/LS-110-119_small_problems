def decrease(counter):
    return counter - 1

counter = 10

for _ in range(10):
    print(counter)
    counter = decrease(counter) # instead, set counter to the returned value of the decrease function

print('LAUNCH!')


# The reason for this is that the change to the local variable counter in the decrease function
# doesn't affect the global counter variable and it isn't saved to that variable either so there
# is no change