"""
Problem:
Write a function that implements a miniature stack-and-register-based programming 
language that has the following commands (also called operations or tokens):

n - place an integer value n in the register, do not modify stack
PUSH - push the current register value onto the stack. Leave the value in the register
ADD - pop a value from the stack and add it to the register value, storing the result in the register
SUB - pop a value from the stack and subtract it from the register value, storing the result in the register
MULT - pop a value from the stack and multiply it by the register value, storing the result in the register
DIV - pop a value from the stack and divide the register value by the popped stack value,
storing the integer result back in the register
REMAINDER - pop a value from the stack and divide the register value by the popped stack value,
storing the integer remainder of the division back in the register
POP - remove the topmost item from the stack and place it in the register
PRINT - print the register value

input: string
output: results depending on rules

rules:
    explicit:
    - all input will be valid
    implicit:
    - don't expect bad input

datastructure:
list

                                           
"""

def minilang(command):
    tokens = command.split()
    stack = []
    register = 0

    for token in tokens:
        match token:
            case 'PUSH':
                stack.append(register)
            case 'ADD':
                register += stack.pop()
            case 'SUB':
                register -= stack.pop()
            case 'MULT':
                register *= stack.pop()
            case 'DIV':
                register //= stack.pop()
            case 'REMAINDER':
                register %= stack.pop()
            case 'POP':
                register = stack.pop()
            case 'PRINT':
                print(register)
            case _:
                register = int(token)
    return register

minilang('PRINT')
# 0

minilang('5 PUSH 3 MULT PRINT')
# 15

minilang('5 PRINT PUSH 3 PRINT ADD PRINT')
# 5
# 3
# 8

minilang('5 PUSH POP PRINT')
# 5

minilang('3 PUSH 4 PUSH 5 PUSH PRINT ADD PRINT POP PRINT ADD PRINT')
# 5
# 10
# 4
# 7

minilang('3 PUSH PUSH 7 DIV MULT PRINT')
# 6

minilang('4 PUSH PUSH 7 REMAINDER MULT PRINT')
# 12

minilang('-3 PUSH 5 SUB PRINT')
# 8

minilang('6 PUSH')
# (nothing is printed)         
