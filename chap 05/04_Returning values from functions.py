# ----------------------------------------
# return is one of those keywords
# You can use functions that return a value by "return"
# ----------------------------------------

def withdraw_mony(current_balance, amount):
    if (current_balance >= amount):
        current_balance = current_balance - amount
    print("The balance is", current_balance)


withdraw_mony(100, 80)


def withdraw_mony(current_balance, amount):
    if (current_balance >= amount):
        current_balance = current_balance - amount
        return current_balance


balance = withdraw_mony(100, 80)

if (balance <= 50):
    print("We need to make a deposit")
else:
    print("Nothing to see here!")
