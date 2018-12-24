print('''ShopListCreator''')


def start():
    print('Hello, this program creates your shop list.')
    menu = input('''Menu:
1 - Create new list
2 - Exit
>>> ''')
    if menu == "1" or menu == "Create new list":
        new_list()
    elif menu == "2" or menu == "Exit":
        exit(0)
    else:
        print("The answer isn't right")
        start()


def new_list():
    shoplist = {}
    add_item(shoplist)


def add_item(shoplist):
    item = None
    while item != "Stop":
        item = input("Write the name of the thing or \"Stop\" to stop making a list >>> ")
        if item != "Stop":
            set_quantity(item, shoplist)
        elif item == "Stop":
            show_lists1(shoplist)


def set_quantity(item, shoplist):
    quantity = None
    try:
        quantity = int(input("Write the quantity of wanted thing >>> "))
        add_to_list(item, quantity, shoplist)
    except ValueError:
        print("Error: Quantity should be number. Please, try again.")
        set_quantity(item, shoplist)


def add_to_list(item, quantity, shoplist):
    shoplist[str(item)] = int(quantity)
    add_item(shoplist)


def show_lists1(shoplist):
    format1 = list(shoplist.items())
    showlists2(format1)


def showlists2(format1):
    currindx = 0
    format2 = []
    for x in range(len(format1)):
        format2 += list(format1[int(currindx)])
        currindx += 1
    showlists3(format2)


def showlists3(format2):
    currindx2 = 0
    print('''↓    Here's your list. Enjoy    ↓
↓           :Example:           ↓
↓Name of item - Quantity of item↓''')
    for x in range(len(format2) // 2):
        print("{0} - {1}".format(format2[currindx2], format2[currindx2 + 1]))
        currindx2 += 2
    restart()


def restart():
    r = input('''What do you want to do?"
1 - Go to menu
2 - Exit
>>> ''')
    if r == "1" or r == "Go to menu":
        start()
    elif r == 2 or r == "Exit":
        exit(0)


start()