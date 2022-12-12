import random


def get_unique_list_numbers(start_number: int, end_number: int, n: int) -> list[int]:
    beautiful_list = []  # Будущий список
    # Запускаем цикл, в котором генерируем новые числа, пока не получим число, которого еще нет в списке
    while len(beautiful_list) < n:
        new_number = random.randint(start_number, end_number)
        if beautiful_list.count(new_number) == 0:
            beautiful_list += [new_number]  # Добавляем число в список

    return beautiful_list


list_unique_numbers = get_unique_list_numbers(-10, 10, 15)
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
