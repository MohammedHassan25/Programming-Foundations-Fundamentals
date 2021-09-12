# Four main categories of jobs

# 1- no parameters and no return value example


def hello():
    print("Hi friends!")


# 2- parameters and no return value example


def grade():
    if grade == "A":
        print("You aced the class!")


# 3- no parameters and return value example


def get_favorite_food():
    food = input("What's your favorite food?")
    return food


# 4- parameters and return value example


def withdraw_mony(current_balance, amount):
    if (current_balance >= amount):
        current_balance = current_balance - amount
        return current_balance
