result = []
features = {'Название': '', 'Цена': '', 'Количество': '', 'Единица измерения': ''}
analytics = {'Название': [], 'Цена': [], 'Количество': [], 'Единица измерения': []}
num = 0
while True:
    if input('Для выхода из программы нажмите "Q", для продолжения нажмите "Enter": ').upper() == 'Q':
        break
    num += 1
    features = features.copy() # Так я и не понял что будет без этой строчки
    for feat in features:
        added = input(f'Введите значение свойства "{feat}": ')
        features[feat] = int(added) if feat == 'цена' or feat == 'количество' else added
        analytics[feat].append(features[feat])
    result.append((num, features))
    print(f'\n Структура товаров\n {result}')
    print(f'\n Текущая аналитика по товарам: \n {"-" * 50}')
    for primus, follow in analytics.items():
        print(f'{primus[:24]:>25}: {follow}')
    print('-' * 50)