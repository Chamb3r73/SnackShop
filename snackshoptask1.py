# SNACK SHOP TASK 1

# define menu dictionary
menu = {

    "Burger": "Price: 150 - Code: 1",
    "Cola": "Price: 50 - Code: 2",
    "Juice": "Price: 60 - Code: 3",
    "Salad": "Price: 100 - Code: 4",
    "Fries": "Price: 90 - Code: 5",
    "Fruit": "Price: 40 - Code: 6"

}

# print the menu
print('Snack Shop Menu')
for i in menu:
    print(f'{i} - {menu[i]}')
print('-----------------------------')


# define snacks dictionary
snacks = {

    "1": "Burger - Price: 150",
    "2": "Cola - Price: 50",
    "3": "Juice - Price: 60",
    "4": "Salad - Price: 100",
    "5": "Fries - Price: 90",
    "6": "Fruit - Price: 40"

}

# get order
print('To choose an item, type its code')
item = (input('Choose your item: '))

# print order
print(f'Your order is: {snacks[item]}')
