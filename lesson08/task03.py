class NotNumberError(Exception):
    def __init__(self, text):
        self.text = text

    def __str__(self):
        return self.text


if __name__ == '__main__':
    my_list = []

    while True:
        user_input = input('Введите число для заполнения списка, или "N" для выхода -')

        if user_input == 'N' or user_input == 'n':
            break

        try:
            if not user_input.isdigit():
                raise NotNumberError(f"'{user_input}' не является числовым форматом")

            my_list.append(int(user_input))
            print(my_list)
        except NotNumberError as w:
            print(w)

    print(my_list)
