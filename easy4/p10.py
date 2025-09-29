"""
Problem:
Building on the previous exercise, write a function that returns True or False 
based on whether or not an inventory item (an ID number) is available. As before, 
the function takes two arguments: an item ID and a list of transactions. 
The function should return True only if the sum of the quantity values of the item's 
transactions is greater than zero. Notice that there is a movement property in each transaction object. 
A movement value of 'out' will decrease the item's quantity.

You may (and should) use the transactions_for function from the previous exercise.


input: id and list of transactions
output: boolean that determines if sum of quantity values of items transactions is greater than zero

rules:
    explicit:
    - transactions are subtracted or added based on their movement 
    - use previously created function
    implicit:
    - no need to handle bad input

datastructure:
list

algorithm:
1.) first using previous transactions, return all for the current item
2.) create a total variable equal to the first transaction
3.) for each transaction alter the total
4.) return total > 0
"""

def transactions_for(id, transactions):
    return [transaction 
            for transaction in transactions
            if transaction['id'] == id]


def is_item_available(id, transactions):
    item_transactions = transactions_for(id,transactions)
    total = 0
    for item in item_transactions:
        if item["movement"] == "in":
            total += item["quantity"]
        else:
            total -= item["quantity"]
    return total > 0

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

print(is_item_available(101, transactions) == False)  # True
print(is_item_available(103, transactions) == False)  # True
print(is_item_available(105, transactions) == True)   # True