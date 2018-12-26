print('''ShopListCreator''')


def start():
    menu = None
    print('Hello, this program creates your shop list.')
    while menu != "1" or menu != "Create new list" or menu != "2" or menu != "Exit":
        menu = input('''Menu:
1 - Create new list
2 - Exit
>>> ''')
        if menu == "1" or menu == "Create new list":
            new_list()
            break
        elif menu == "2" or menu == "Exit":
            exit(0)
        else:
            print("Error: The answer isn't right")
            continue


def new_list():
    shoplist = {}
    add_item(shoplist)


def add_item(shoplist):
    item = None
    while item != "Stop":
        item = input("Write the name of the thing or \"Stop\" to stop making a list >>> ")
        if item != "Stop" and item != "":
            set_quantity(item, shoplist)
        elif item == "":
            print("Error: Name of the thing can't be empty. Please try again")
            continue
        elif item == "Stop":
            show_lists1(shoplist)
            break


def set_quantity(item, shoplist):
    while True:
        try:
            quantity = int(input("Write the quantity of wanted thing >>> "))
            add_to_list(item, quantity, shoplist)
            break
        except ValueError:
            print("Error: Quantity should be number. Please, try again.")
            continue


def add_to_list(item, quantity, shoplist):
    shoplist[str(item)] = int(quantity)


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
    print('''---------------------------------
|    Here's your list. Enjoy    |
|           :Example:           |
|Name of item - Quantity of item|
---------------------------------''')
    for x in range(len(format2) // 2):
        print("{0} - {1}".format(format2[currindx2], format2[currindx2 + 1]))
        currindx2 += 2
    restart(format2)


def restart(format2):
    r = None
    while r != "1" or r != "Go to menu" or r != "2" or r != "Save list" or r != "Exit":
        r = input('''What do you want to do?
1 - Go to menu
2 - Save list
3 - Exit
>>> ''')
        if r == "1" or r == "Go to menu":
            start()
            break
        elif r == "2" or r == "Save list":
            savefile(format2)
            break
        elif r == "3" or r == "Exit":
            exit(0)
        else:
            print("Answer is not right. Please try again")
            continue


def savefile(format2):
    currindx2 = 0
    filename = input("How do you want to name your list? >>> ")
    file = open(f'{filename}.txt', 'w')
    file.write('''---------------------------------
|    Here's your list. Enjoy    |
|           :Example:           |
|Name of item - Quantity of item|
---------------------------------\n''')
    for x in range(len(format2) // 2):
        file.write("{0} - {1}\n".format(format2[currindx2], format2[currindx2 + 1]))
        currindx2 += 2
    file.close()
    restartsave()


def restartsave():
    rs = None
    while rs != "1" or rs != "Go to menu" or rs != "2" or rs != "Exit":
        rs = input('''What do you want to do?
1 - Go to menu
2 - Exit
>>>  ''')
        if rs == "1" or rs == "Go to menu":
            start()
            break
        elif rs == "2" or rs == "Exit":
            exit(0)
        else:
            print("Error: Answer is not right. Please try again")
            continue


start()
