#В модуле написать тесты для встроенных функций filter, map, sorted,
# а также для функций из библиотеки math: pi, sqrt, pow, hypot.
# Чем больше тестов на каждую функцию - тем лучше

import math
from python_tst import filter_num, filter_duplicate, function_num, function_sorted, function_sqrt
from python_tst import function_hypot, function_pow

# Вывод четных чисел
def test_filter_num():
    assert filter_num(2) == True

# Список строк с дубликатами
def test_filter_duplicate():
    assert filter_duplicate("Python") == False
    assert filter_duplicate("Scala") == True

# Возведение чисел во 2-ую степень
def test_function_num():
    assert function_num(2)

# Сортировка списка на четные и нечетные числа
def test_function_sorted():
    assert function_sorted(2) == 0

# Число пи
def test_function_pi():
    assert math.pi

# Вычисление гипотенузы
def test_function_hypot():
    assert function_hypot(30, 40)

#Извлечение квадратного корня
def test_function_sqrt():
    assert function_sqrt(81)

# Функция возведения чисел в степень
def test_function_pow():
    assert function_pow(3, 4) == 81
    assert function_pow(2, 3) == 8