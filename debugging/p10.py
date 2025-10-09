data = [4, 2, 4, 2, 1, 3, 2, 3, 2, 4, 3]
unique_data = list(set(data))
print(unique_data == [4, 2, 1, 3]) # order not guaranteed

# we could use a set comprehension

unique_data = []
seen = set()
for num in data:
    if num not in seen:
        seen.add(num)
        unique_data.append(num)

print(unique_data == [4,2,1,3])