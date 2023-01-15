"""
МОДУЛЬ 3
1. В подпрограмме Мой банковский счет;
2. Добавить сохранение суммы счета в файл.

При первом открытии программы на счету 0
После того как мы воспользовались программой и вышли сохранить сумму счета
При следующем открытии программы прочитать сумму счета, которую сохранили
...
3. Добавить сохранение истории покупок в файл

При первом открытии программы истории нет.
После того как мы что нибудь купили и закрыли программу сохранить историю покупок.
При следующем открытии программы прочитать историю и новые покупки уже добавлять к ней;
...
4. Формат сохранения количество файлов и способ можно выбрать самостоятельно.

"""
"""
def run_bill():
    
    Функция запускает программу личный счет
    :return
    if __name__ == "__main__":
    print(run_bill())
"""
import os
FILE_NAME = 'orders.txt'
FILE_NAME_BILL = 'bill.txt'

def run_bill():
    bill_sum = 0
    if os.path.exists(FILE_NAME_BILL):
        with open(FILE_NAME_BILL, 'r') as f:
            bill_sum = int(f.read())

    history = []
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, 'r') as f:
            for name in f:
                history.append(name.replace('\n', ''))

    while True:
        print('1. пополнение счета')
        print('2. покупка')
        print('3. история покупок')
        print('4. выход')
        print(f'Ваш счет {bill_sum}')

        choice = input('Выберите пункт меню')
        if choice == '1':
            cost = int(input('Введите сумму'))
            bill_sum += cost
        elif choice == '2':
            cost = int(input('Введите сумму покупки'))
            if cost > bill_sum:
                print('Недостаточно средств')
            else:
                bill_sum -= cost
                name = input('Введите название покупки')
                history.append((name, cost))
        elif choice == '3':

            print(history)
        elif choice == '4':
            with open(FILE_NAME, 'w') as f:
                for name in history:
                    f.write(f'{name}\n')

            with open(FILE_NAME_BILL, 'w') as f:
                f.write(f'{bill_sum}')

            break
        else:

            print('Неверный пункт меню')

if __name__ == "__main__":
    print(run_bill())