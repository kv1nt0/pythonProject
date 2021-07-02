import json

with open('file07.json', 'w+', encoding='utf-8') as info_full:
    with open('file07.txt', 'r', encoding='utf-8') as firm_info:
        profit = {line.split()[0]: int(line.split()[2]) - int(line.split()[3]) for line in firm_info}
        result = [profit, {'Средняя прибыль фирм': round(sum([int(i) for i in profit.values() if int(i) > 0]) / len(
            [int(i) for i in profit.values() if int(i) > 0]))}]
    json.dump(result, info_full, ensure_ascii=False, indent=5)