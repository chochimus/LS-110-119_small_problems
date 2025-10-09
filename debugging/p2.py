def reverse_string(string):
    answer = ""
    for char in string:
        answer = char + answer

    return answer

print(reverse_string("hello"))
print(reverse_string("hello") == "olleh")

# in this case string we're just prepending the existing string with each character then returning the new string
# this results in a string with the reverse value and original in the same string. An example fix would be
# creating a new variable in the function and instead prepending to this string. Otherwise simply use slicing
# for a one-liner return string[::-1]