from pprint import pprint

# Все-таки удалось вместить все в одну строчку
list_dict_num = [
    {'bin': bin(number_10), 'dec': number_10, 'hex': hex(number_10), 'oct': oct(number_10)} for number_10 in range(16)
]


pprint(list_dict_num)
