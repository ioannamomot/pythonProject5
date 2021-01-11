
def qwerty():
    a = float(input("Введи первое число: "))
    b = float(input("Введи второе число: "))
    c = float(input("Введи шаговое число: "))

    while a <= b:
        a += c
        if a < b:
            print(str(a) + ' Пока что нет')

        elif a > b:
            print(str(a) + ' Дождались!')

qwerty()