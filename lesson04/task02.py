old_list = [5, 7, 11, 29, 53, 8, 9, 5, 2, 4, 6, 33]
new_list = [el for num, el in enumerate(old_list) if old_list[num - 1] < old_list[num]]
print(old_list)
print(new_list)

from random import randint

random_list = [randint(0, 100) for el in range(0, randint(2, 20))]
new_random_list = [w for num, w in enumerate(random_list[1:]) if w > random_list[num]]
print(random_list)
print(new_random_list)
