"""
PROBLEM:
Write a program that solicits six (6) numbers from the user and prints a message
that describes whether the sixth number appears among the first five.

input: six (6) numbers from the user
output: whether or not the 6th number appears in the first 5

rules:
explicit: 
    - the return string should be of the format {6th} is/isn't in {1,2,3,4,5}

implicit:
    - only last number is checked for membership
    - ordering matches input
questions:

are inputs guaranteed to be integers?
should I handle the empty string?

data structure: list

algorithm:

- get valid integer input
- store integer in list
- repeat 5 times
- get valid 6th integer
- check if integer is in list
- print result

"""

def get_postfix(index):
    match index:
        case 1:
            return f"{index}st"
        case 2:
            return f"{index}nd"
        case 3:
            return f"{index}rd"
        case 6:
            return "last"
        case 4|5|_:
            return f"{index}th"
        
def get_int(index):
    number = input(f"Enter the {get_postfix(index)} number: ")
    return number
        

def result(final_number, final_list):
    included = "is" if final_number in final_list else "isn't"
    return f"{final_number} {included} in {','.join(final_list)}."

num_list = []
for i in range(1,6):
    num_list.append(get_int(i))

last = get_int(6)
print(result(last, num_list))
