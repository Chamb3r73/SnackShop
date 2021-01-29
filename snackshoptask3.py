# SNACK SHOP TASK 3

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

# define healthy dictionary

healthy = {

    "1": "No",
    "2": "No",
    "3": "Yes",
    "4": "Yes",
    "5": "No",
    "6": "Yes"

}

# get order
print('How to use:\n- To choose an item, type its code.\n- Specify the number of an item by giving a number next to the item code seperated by a full stop, eg: "3.2" to buy 2 juices (do NOT use "4" to buy one salad, use "4.1"). \n- Seperate different items by commas\n-----------------------------')
loop = True
while loop == True:
    try:
        unhealthyOrder = False
        # get order
        items = str(input('Choose your items: '))
        # seperate each item by comma
        itemsplit = items.split(', ')
        numberofitem = []
        # take the item code and multiplier from each side of the full stop
        for i in itemsplit:
            numberofitem.append(i.split('.')[-1])
        itemcode = []
        for i in itemsplit:
            itemcode.append(i.split('.')[0])
        length = len(itemcode)
        
        # check for health
        healthyItems = 0
        unhealthyItems = 0
        for i in range(length):
            if healthy[itemcode[i]] == "Yes":
               healthyItems += (int(numberofitem[i]))
            else:
                unhealthyItems += (int(numberofitem[i]))

        if unhealthyItems > healthyItems:
            unhealthyOrder = True
            print('You have more unhealthy items than healthy items! Please order your food again')

        if unhealthyOrder == True:
            continue
        else:
            # loop for the number of items ordered
            print('Your order is:')
            for i in range(length):
                # print the multiplier of the ith item in the order, the name of the ith item, and the price
                print(f'{numberofitem[i]} x {snacks[itemcode[i]]} - Price: {int(prices[itemcode[i]]) * int(numberofitem[i])}') # use "prices[itemcode[i]]"" to avoid a key error from the dictionary
                totalprice += int(prices[itemcode[i]]) * int(numberofitem[i])
            print(f'Total price = {totalprice}')
            loop = False
    except:
        # catch errors
        print('Sorry! That was not a valid code, or you might have misformatted your order. Try again')
