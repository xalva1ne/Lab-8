import math


def quadratic_equation(a: float, b:float, c:float):
    """
    Лабораторная работа №6
    Функция находит корни квадратного уравнения по коэффициентам.

    :param a: Входная переменная квадратного уровнения.
    :param b: Входная переменная квадратного уровнения.
    :param c: Входная переменная квадратного уровнения.
    :return: Результат вычислений.
    """


    D = (b ** 2) - (4 * a * c)

    if a == 0:
        x = -c / b
        return f'Корень x = {round(x, 2)}'
    else:
        if D > 0:
            # Два корня
            x1 = (-b + math.sqrt(D)) / (2 * a)
            x2 = (-b - math.sqrt(D)) / (2 * a)
            return f'Корень x1 = {round(x1, 2)}, корень x2 = {round(x2, 2)}'
        elif D == 0:
            # Один корень
            x1 = -b / (2 * a)
            return f'Корень один, он равен {round(x1, 2)}'
        else:
            # Комплексные корни
            x1 = -b / (2 * a)
            x2 = math.sqrt(-D) / (2 * a)
            return f'Комплексные корни\n{round(x1, 2)} + {round(x2, 2)}i\n{round(x1, 2)} - {round(x1, 2)}i'


print(quadratic_equation.__doc__)
print(quadratic_equation(float(input('Введите коэффициент A: ')), float(input('Введите коэффициент B: ')),
                         float(input('Введите коэффициент C: '))))
print('--------------------------------------')


def even_numbers_in_tuple(numbers: tuple):
    """
    Лабораторная работа №7.1
    Функция считает количетсво четных чисел в кортеже.

    :param numbers: Входные данные чисел кортежа.
    :return: Вывод результата вычислений.
    """

    counter = 0

    for num in numbers:
        if num % 2 == 0:
            counter += 1

    return f'Количество четных чисел в кортеже: {counter}'

print(even_numbers_in_tuple.__doc__)
print(even_numbers_in_tuple(tuple(map(int, input('Введите числа для кортежа через пробел: ').split()))))
print('--------------------------------------')


def negative_numbers_in_tuple(numbers: tuple):
    """
    Лабораторная работа №7.2
    Функция составляет список, содержащий отрицательные числа, на основе кортежа, данным пользователем.

    :param numbers: Входные данные чисел кортежа.
    :return: Вывод полученного списка.
    """

    numbers_list = []

    for num in numbers:
        if num < 0:
            numbers_list.append(num)

    return f'Кортеж: {numbers}\nСписок основанный на кортеже: {numbers_list}'


print(negative_numbers_in_tuple.__doc__)
print(negative_numbers_in_tuple(tuple(map(int, input('Введите числа для кортежа через пробел: ').split()))))
print('--------------------------------------')


def set_compare(first_set: set, second_set: set):
    """
    Лабораторная работа №7.3
    Функция определяет, состоят ли оба мжожества из всех десяти цифр.

    :param first_set: Входные данные чисел первого множества.
    :param second_set: Входные данные чисел второго множества.
    :return: Вывод полученного результата.
    """

    numbers = set('0123456789')
    combined_set = first_set.union(second_set)

    if combined_set == numbers:
        return f'В записи этих двух строк используются все десять цифр'
    else:
        return f'В записи этих двух строк НЕ используются все десять цифр'


print(set_compare.__doc__)
print(set_compare(set(input('Введите числа для первого множества через пробел: ').split()),
                  set(input('Введите числа для второго множества через пробел: ').split())))
print('--------------------------------------')


def students_dictionary(students: list):
    """
    Лабораторная работа №7.4
    Функция сортирует словарь со студентам по оценке по математике.

    :param students: Входные данные о студентах.
    """
    sorted_students = sorted(students, key=lambda x: x["Оценка по математике"], reverse=True)

    for student in sorted_students:
        print(student)


print(students_dictionary.__doc__)
print(students_dictionary(
    [
        {'Фамилия': 'Браташин',
         'Имя': 'Арсений',
         'Пол': 'Мужской',
         'Оценка по химии': 3,
         'Оценка по математике': 4,
         'Оценка по физике': 3},
        {'Фамилия': 'Карташов',
         'Имя': 'Илья',
         'Пол': 'Мужской',
         'Оценка по химии': 4,
         'Оценка по математике': 5,
         'Оценка по физике': 4},
        {'Фамилия': 'Ларионов',
         'Имя': 'Антонов',
         'Пол': 'Мужской',
         'Оценка по химии': 2,
         'Оценка по математике': 3,
         'Оценка по физике': 3},
        {'Фамилия': 'Ларин',
         'Имя': 'Владимир',
         'Пол': 'Мужской',
         'Оценка по химии': 3,
         'Оценка по математике': 4,
         'Оценка по физике': 4},
        {'Фамилия': 'Курако',
         'Имя': 'Вячеслав',
         'Пол': 'Мужской',
         'Оценка по химии': 4,
         'Оценка по математике': 5,
         'Оценка по физике': 5},
        {'Фамилия': 'Ерохин',
         'Имя': 'Максим',
         'Пол': 'Мужской',
         'Оценка по химии': 5,
         'Оценка по математике': 5,
         'Оценка по физике': 5},
        {'Фамилия': 'Натаровский',
         'Имя': 'Александр',
         'Пол': 'Мужской',
         'Оценка по химии': 4,
         'Оценка по математике': 4,
         'Оценка по физике': 5},
        {'Фамилия': 'Казанцев',
         'Имя': 'Максим',
         'Пол': 'Мужской',
         'Оценка по химии': 3,
         'Оценка по математике': 5,
         'Оценка по физике': 3}
    ]
))
