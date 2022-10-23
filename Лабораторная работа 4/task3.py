def delete(list_, index=None):
    if index is None:
        new_list = list_[0:-1]
    else:
        new_list = list_[0:index] + list_[index + 1::]

    return new_list


print(delete([0, 0, 1, 2], index=0))  # [0, 1]
print(delete([0, 1, 1, 2, 3], index=1))  # [0, 1, 2]
print(delete([0, 1, 2, 3, 4, 4]))  # [0, 1, 2, 3]
