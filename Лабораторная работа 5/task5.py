from string import ascii_uppercase, ascii_lowercase, digits
from random import sample


def get_random_password(n=8) -> str:
    symbols = ascii_uppercase + ascii_lowercase + digits
    list_of_symbols = sample(symbols, n)

    return ''.join(list_of_symbols)


print(get_random_password())
