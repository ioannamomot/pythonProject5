import exit_module
def mainMenu():
    print("1. Создать Контакт")
    print("2. Найти Контакт")
    print("3. Отредактировать Контакт")
    print("4. Удалить Контакт")
    print("5. Выйти")

    selection=int(input("Выбери действие: "))

    if selection == 1:
        create()
    elif selection == 2:
        search()
    elif selection == 3:
        edit()
    elif selection == 4:
        delete()
    elif selection == 5:
        exit_module.exit()
    else:
        print("Такого действия не существует. Выбери из списка.")

    mainMenu()
    selection = int(input("Выбери действие: "))

def create():
    pass
def search():
    pass
def edit():
    pass
def delete():
    pass
mainMenu()