new_list = [14, 2.8, (2 + 4j), 'abc', None, True, {'id': 1}, [1, 2], (1, 2)]


def my_type(el):
    num = 1
    for el in range(len(new_list)):
        print(f"Тип данных № {num} {(type(new_list[el]))}")
        num += 1
    return


my_type(new_list)
