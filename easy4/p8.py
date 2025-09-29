"""
Problem:
Write a function that returns a list of all palindromic substrings of a string. 
That is, each substring must consist of a sequence of characters that reads the same forward and backward. 
The substrings in the returned list should be sorted by their order of appearance in the input string. 
Duplicate substrings should be included multiple times.

You may (and should) use the substrings function you wrote in the previous exercise.

For the purpose of this exercise, you should consider all characters and pay attention to case; 
that is, 'AbcbA' is a palindrome, but 'Abcba' and 'Abc-bA' are not. In addition, 
assume that single characters are not palindromes.

input: string
output: all palindromic substrings

rules:
    explicit:
    - substrings must consist of sequence of characters that read the same forward and backward
    - substrings should be sorted by their order of appearance in the input string
    - duplicate substrings should be included multiple times
    - use function from previous exercise 
    - consider all characters (and case)
    - single characters are not palindromes
    implicit:
    - palindromes can sonsist of non alphabetic characters

datastructure:
list

algorithm:
1.) create empty string answer
2.) get all substring 
3.) for each substring if it is a palindrome add it to answer
4.) return answer

"""

def leading_substrings(string):
    return [string[:idx + 1] for idx in range(len(string))]

def substrings(string):
    answer = []
    for i in range(len(string)):
        answer.extend(leading_substrings(string[i:]))
    return answer

def palindromes(string):
    answer = []

    for substr in substrings(string):
        if len(substr) > 1 and substr == substr[::-1]:
            answer.append(substr)
    
    return answer

print(palindromes('abcd') == [])                  # True
print(palindromes('madam') == ['madam', 'ada'])   # True

print(palindromes('hello-madam-did-madam-goodbye') ==
                  [
                      'll', '-madam-', '-madam-did-madam-',
                      'madam', 'madam-did-madam', 'ada',
                      'adam-did-mada', 'dam-did-mad',
                      'am-did-ma', 'm-did-m', '-did-',
                      'did', '-madam-', 'madam', 'ada', 'oo',
                  ])    # True

print(palindromes('knitting cassettes') ==
                  [
                      'nittin', 'itti', 'tt', 'ss',
                      'settes', 'ette', 'tt',
                  ])    # True