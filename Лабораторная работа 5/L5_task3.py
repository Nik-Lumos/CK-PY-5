import random
import string


def get_random_password(n=8) -> str:
    # Создаем выборку символов для генерации паролей
    endless = string.ascii_lowercase + string.ascii_uppercase + string.digits
    password_list = random.sample(endless, n)  # Генерируем случайный пароль в виде списка символов
    password_str = "".join(password_list)  # Превращаем список символов в строку

    return password_str


print(get_random_password())
