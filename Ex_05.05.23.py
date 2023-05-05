import csv

def age_sport (data):
    """
    Спортсменнов с каким возрастом больше всего
    :param data:
    :return:
    """
    list_age = {}
    for row in data:
        k = row[2]
        if k not in list_age.keys():
            list_age[k] = 1
        else:
            list_age[k] += 1
    max_age = dict([max(list_age.items(), key=lambda x: x[1])])
    return max_age

def F_medals(data):
    """
    Скпортсменки какой страны заработали больше медалий
    :param data:
    :return:
    """
    Country_medals = {}
    for row in data:
        f = row[1]
        if row[5] == 'F':
            if f not in Country_medals.keys():
                Country_medals[f] = int(row[11])
            else:
                Country_medals[f] += int(row[11])
    max_Country_medals = dict([max(Country_medals.items(), key=lambda x: x[1])])
    return max_Country_medals

def min_sport(data):
    """
    В каком спорте меньше всего участников
    :param data:
    :return:
    """
    total_in_sport = {}
    for row in data:
        k = row[12]
        if k not in total_in_sport.keys():
            total_in_sport[k] = 1
        else:
            total_in_sport[k] += 1
    min_total_in_sport = dict([min(total_in_sport.items(), key=lambda x: x[1])])
    return min_total_in_sport

def age_medals(data):
    """
    Возраст получивший больше всего медалей
    :param data:
    :return:
    """
    age_medals = {}
    for row in data:
        k = row[2]
        m = row[11]
        if k not in age_medals.keys():
            age_medals[k] = int(m)
        else:
            age_medals[k] += int(m)
    max_age_medals = dict([max(age_medals.items(), key=lambda x: x[1])])
    return max_age_medals
if __name__ == '__main__':
    df = []
    with open('london_athletes.csv', encoding='UTF-8') as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            df.append(row)

    print(f'Больше всего участников с возрастом {age_sport(df)}')
    print(f'Больше всего медалей у спортсменок {F_medals(df)}')
    print(f'Меньше всего участие принимали в {min_sport(df)}')
    print(f'Возраст получивший больше всего медалей {age_medals(df)}')
