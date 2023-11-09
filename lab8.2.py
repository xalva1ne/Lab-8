def even_numbers_in_tuple_recursive(numbers: tuple, index=0, counter=0):
    """
    Лабораторная работа №7.1
    Рекурсивная функция считает количетсво четных чисел в кортеже.

    :param numbers: Входные данные чисел кортежа.
    :param index: Индекс текущего элемента в кортеже (по умолчанию 0).
    :param counter: Переменная для подсчета четных чисел (по умолчанию 0).
    :return: Количество четных чисел в кортеже.
    """

    if index == len(numbers):
        return counter
    else:
        if numbers[index] % 2 == 0:
            counter += 1
        return even_numbers_in_tuple_recursive(numbers, index + 1, counter)


result = even_numbers_in_tuple_recursive((1, 2, 3, 4, 5, 6, 7, 8, 9, 0))
print(even_numbers_in_tuple_recursive.__doc__)
print(f'Количество четных чисел в кортеже: {result}')
