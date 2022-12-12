from random import sample
from string import ascii_lowercase, ascii_uppercase, digits


def get_random_password(n=8) -> str:
    # Создаем выборку символов для генерации паролей
    endless = ascii_lowercase + ascii_uppercase + digits
    password_list = sample(endless, n)  # Генерируем случайный пароль в виде списка символов
    password_str = "".join(password_list)  # Превращаем список символов в строку

    return password_str


print(get_random_password())
