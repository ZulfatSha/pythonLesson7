import math

# Задания по функции filter
# Вывод четных чисел
numbers = [1, 2, 3, 4, 5, 6]

def filter_num(x):
    '''
    :param x: число списка
    :return: вывод четных чисел
    '''
    if (x % 2) == 0:
        return True
    else:
        return False
result = filter(filter_num, numbers)
print(list(result))

# Список строк с дубликатами
list1 = ["Python", "C++", "Java", "Go"]
list2 = ["Python", "Scala", "JavaScript", "Go", "PHP", "C++"]

# функция, которая проверяет строки на вхождение
def filter_duplicate(string_to_check):
    if string_to_check in ll:
        return False
    else:
        return True
# filter() удаляет повторяющиеся строки
ll = list2
out_filter = list(filter(filter_duplicate, list1))
ll = list1
out_filter += list(filter(filter_duplicate, list2))
print("Отфильтрованный список:", out_filter)


# Задания по функции map
# Возведение чисел во 2-ую степень
def function_num(x):
    '''
    :param x: число списка
    :return: вывод произведения чисел
    '''
    return x**2
print(list(map(function_num, numbers)))


# Задания по функции sorted
# Сортировка списка на четные и нечетные числа

print('Sorted by z-numbers:')
z = [1, 2, 3, 4, 5, 6]
def function_sorted(x):
    '''
    :param x: число списка
    :return: вывод четных чисел в левой части списка
    '''
    return x % 2
    # if x % 2 == 0:
    #     return x
    # else:
    #     return x + 100

print(sorted(z, key=function_sorted))


# Функции math

# Задания по Число пи
print('Задание по числу Пи')
print(math.pi)

# Задания по функции hypot
# Вычисление гипотенузы
def function_hypot(x, y):
    '''
        :param x: длина катета 1
        :param y: длина катета 2
        :return: вычисление гипотенузы
        '''
    result = (math.hypot(x, y))
    return result

print(function_hypot(30, 40))

# Задания по функции sqrt
# Извлечение квадратного корня
def function_sqrt(x):
    '''
            :param x: число
            :return: квадратный корень числа x
    '''
    result = math.sqrt(x)
    return result

print(math.sqrt(81))

# Задания по функции pow
# Функция возведения чисел в степень
def function_pow(a, b):
    '''
    :param a: число
    :param b: степень
    :return: возведение числа в степень
    '''
    result = (math.pow(a, b))
    return result

print(math.pow(3, 4))