# SNACK SHOP TASK 1

# set variables
totalprice = 0

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

    "1": "Burger",
    "2": "Cola",
    "3": "Juice",
    "4": "Salad",
    "5": "Fries",
    "6": "Fruit"

}

# define prices dictionary
prices = {

    "1": "150",
    "2": "50",
    "3": "60",
    "4": "100",
    "5": "90",
    "6": "40"

}

# get order
print('To choose an item, type its code. Specify the number of an item by giving a number next to the item code seperated by a full stop, eg: "3.2" to buy 2 juices. Seperate different items by commas')
loop = True
while loop == True:
    try:
        items = str(input('Choose your items: '))
        itemsplit = items.split(', ')
        numberofitem = []
        for i in itemsplit:
            numberofitem.append(i.split('.')[-1])
        itemcode = []
        for i in itemsplit:
            itemcode.append(i.split('.')[0])
        loop = False
    except:
        print('Sorry! That was not a valid code. Try again')

# print order
length = len(itemcode)
for i in range(length):
    print(f'Your order is: \n{numberofitem[i]} x {snacks[itemcode[i]]} - Price: {int(prices[itemcode[i]]) * int(numberofitem[i])}')
    totalprice += int(prices[itemcode[i]]) * int(numberofitem[i])
print(f'Total price = {totalprice}')