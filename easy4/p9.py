"""
Problem:
Write a function that takes two arguments, an inventory item ID and a list of transactions, 
and returns a list containing only the transactions for the specified inventory item.

input: intventory item ID and list of transactions
output: list containing only transactions for specified inventory item

rules:
    explicit:
    - list of dictionary items
    implicit:
    - expect valid input

datastructure:
list

algorithm:
1.) create empty list answer
2.) if id of element = input id, add element to list
3.) repeat for all elements in transactions
4.) return answer
"""

def transactions_for(id, transactions):
    return [transaction 
            for transaction in transactions
            if transaction['id'] == id]

transactions = [
    {"id": 101, "movement": 'in',  "quantity":  5},
    {"id": 105, "movement": 'in',  "quantity": 10},
    {"id": 102, "movement": 'out', "quantity": 17},
    {"id": 101, "movement": 'in',  "quantity": 12},
    {"id": 103, "movement": 'out', "quantity": 20},
    {"id": 102, "movement": 'out', "quantity": 15},
    {"id": 105, "movement": 'in',  "quantity": 25},
    {"id": 101, "movement": 'out', "quantity": 18},
    {"id": 102, "movement": 'in',  "quantity": 22},
    {"id": 103, "movement": 'out', "quantity": 15},
]

print(transactions_for(101, transactions) ==
      [
          {"id": 101, "movement": "in",  "quantity":  5},
          {"id": 101, "movement": "in",  "quantity": 12},
          {"id": 101, "movement": "out", "quantity": 18},
      ]) # True