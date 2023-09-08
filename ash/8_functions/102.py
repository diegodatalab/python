#
# * 102. Returning List

ids = [1,2,3,6,4,5,2,1,7,8,9,3,4,5,10,0,6]

def remove_duplicates(numbers):
    new_list = []
    for number in numbers:
        if number not in new_list:
            new_list.append(number)
            new_list.sort()
    return new_list

result = remove_duplicates(ids)
print(result)


def set_remove_dup(numbers2):
    """Set items are unordered, unchangeable, and do not allow duplicate values."""
    return list(set(numbers2))


result_set = set_remove_dup(ids)
print(result_set)