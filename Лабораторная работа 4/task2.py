def get_count_char(str_):
    chars_dict = {}
    DEFAULT_COUNT = 0
    for char_ in str_.lower():
        if char_.isalpha():
            chars_dict[char_] = chars_dict.get(char_, DEFAULT_COUNT) + 1
    return chars_dict


main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
print(get_count_char(main_str))


def get_percent_char(chars_dict):
    sum_of_chars = 0
    for char_ in chars_dict:
        sum_of_chars += chars_dict.get(char_)
    for char_ in chars_dict:
        chars_dict[char_] = chars_dict.get(char_) / sum_of_chars * 100
    return chars_dict
