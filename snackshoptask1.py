# SNACK SHOP TASK 1

# define menu dictionary
menu = {

    "Burger": "Price: 150 - Code: 0",
    "Cola": "Price: 50 - Code: 1",
    "Juice": "Price: 60 - Code: 2",
    "Salad": "Price: 100 - Code: 3",
    "Fries": "Price: 90 - Code: 4",
    "Fruit": "Price: 40 - Code: 5"

}

# print the menu
print('Snack Shop Menu')
for i in menu:
    print(f'{i} - {menu[i]}')
print('-----------------------------')


# define snacks dictionary
snacks = {

    "0": "Burger - Price: 150",
    "1": "Cola - Price: 50",
    "2": "Juice - Price: 60",
    "3": "Salad - Price: 100",
    "4": "Fries - Price: 90",
    "5": "Fruit - Price: 40"

}

# get order
print('To choose an item, type its code')
item = (input('Choose your item: '))

# print order
print(f'Your order is: {snacks[item]}')
