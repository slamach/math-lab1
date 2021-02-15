# Лабораторная работа #1 (19)
# @ Свиридов Дмитрий, PЗ213

FILE_IN = "iofiles/input.txt"


def getmat_file():
    with open(FILE_IN, 'rt') as fin:
        try:
            n = int(fin.readline())
            matrix = []
            for line in fin:
                new_row = list(map(int, line.strip().split()))
                if len(new_row) != (n + 1):
                    raise ValueError
                matrix.append(new_row)
            if len(matrix) != n:
                raise ValueError
        except ValueError:
            print("При считывании файла произошла ошибка!")
            return None
    return matrix


def getmat_input():
    print("Вводите коэффициенты матрицы через пробел строка за строкой.")
    while True:
        try:
            n = int(input("Порядок матрицы: "))
            if n <= 0:
                print("Порядок матрицы должен быть положительным.")
            else:
                break
        except ValueError:
            print("Порядок матрицы должен быть целым числом.")
    matrix = []
    print("Коэффициенты матрицы:")
    try:
        for i in range(n):
            matrix.append(list(map(int, input().strip().split())))
            if len(matrix[i]) != (n + 1):
                raise ValueError
    except ValueError:
        print("При считывании коэффициентов матрицы произошла ошибка!")
        return None
    return matrix


def solve(matrix):
    # TODO: Реализовать алгоритм решения
    print(matrix)


def main():
    print("\t\t\tЛабораторная работа #1 (19)")
    print("Метод Гаусса с выбором главного элемента по столбцам")
    print("\nВзять коэффициенты из файла (+) или ввести с клавиатуры (-)?")

    method = input(">>> ")
    while (method != '+') and (method != '-'):
        print("Введите '+' или '-' для выбора способа ввода.")
        method = input(">>> ")

    if method == '+':
        matrix = getmat_file()
    else:
        matrix = getmat_input()

    if matrix is None:
        return

    solve(matrix)


main()
