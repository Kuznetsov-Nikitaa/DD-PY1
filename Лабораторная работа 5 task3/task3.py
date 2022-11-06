from random import randint, choice

# Вариант 1


def get_unique_list_numbers1() -> list[int]:
    list_ = []
    i = 1
    while i != 16:
        randint_ = randint(-10, 10)
        if randint_ not in list_:
            list_.append(randint_)
            i += 1

    return list_


list_unique_numbers = get_unique_list_numbers1()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))


# Вариант 2


def get_unique_list_numbers2() -> list[int]:
    unique_list_numbers = list(range(-10, 10))
    list_ = []
    for _ in range(15):
        number = choice(unique_list_numbers)
        list_.append(number)
        unique_list_numbers.remove(number)

    return list_


list_unique_numbers = get_unique_list_numbers2()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
