def start():
    print("Добро пожаловать в игру 'Крестики-Нолики'")
    print("Ходы в формате x y")
    print("x - номер строки")
    print("y - номер столбца")

def show():
    print()
    print("    | 0 | 1 | 2 | ")
    for i, value in enumerate(field):
        value_str = f"  {i} | {' | '.join(value)} | "
        print(value_str)
    print()

def steps():
    while True:
        step = input("Ваш ход: ").split()
        if len(step) != 2:
            print("Ошибка: ходы в формате x y")
            print("x - номер строки")
            print("y - номер столбца")
            continue

        x, y = step

        if not(x.isdigit()) or not(y.isdigit()):
            print("Ошибка: введите числа")
            continue

        x, y = int(x), int(y)

        if 0 > x or x > 2 or 0 > y or y > 2:
            print("Ошибка: направильные координаты")
            continue

        if field[x][y] != " ":
            print("Поле занято")
            continue

        return x, y

def final():
    win = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)))
    for i in win:
        line = []
        for c in i:
            line.append(field[c[0]][c[1]])
        if line == ["X", "X", "X"]:
            print("Победа X")
            return True
        if line == ["0", "0", "0"]:
            print("Победа 0")
            return True
    return False


start()
field = [[" "] * 3 for i in range(3)]
count = 0
while True:
    count += 1
    show()
    if count % 2 == 1:
        print(" Ходит крестик!")
    else:
        print(" Ходит нолик!")

    x, y = steps()

    if count % 2 == 1:
        field[x][y] = "X"
    else:
        field[x][y] = "0"

    if final():
        break

    if count == 9:
        print("Ничья")
        break