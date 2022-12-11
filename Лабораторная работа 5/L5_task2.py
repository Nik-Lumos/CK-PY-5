import random


def get_unique_list_numbers() -> list[int]:
    beautiful_list = []  # Будущий список
    for _ in range(15):
        # Запускаем цикл, в котором генерируем новые числа, пока не получим число, которого еще нет в списке
        while True:
            new_number = random.randint(-10, 10)
            if beautiful_list.count(new_number) == 0:
                break
        beautiful_list += [new_number]  # Добавляем число в список

    return beautiful_list


list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
