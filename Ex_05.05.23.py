'''
import csv

list_age = {}
Country_medals = {}
total_in_sport ={}
with open('london_athletes.csv', encoding='UTF-8') as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        if row[2] not in list_age.keys():
            list_age[row[2]] = 1
        else:
            list_age[row[2]] += 1
        if row[5] == 'F':
            if row[1] not in Country_medals.keys():
                Country_medals[row[1]] = int(row[11])
            else:
                Country_medals[row[1]] += int(row[11])
        if row[12] not in total_in_sport.keys():
            total_in_sport[row[12]] = 1
        else:
            total_in_sport[row[12]] += 1

max_age = dict([max(list_age.items(), key=lambda x: x[1])])
max_Country_medals = dict([max(Country_medals.items(), key=lambda x: x[1])])
min_total_in_sport = dict([min(total_in_sport.items(), key=lambda x: x[1])])

print(f'Больше всего участников с возрастом {max_age}')
print(f'Больше всего медалей у спортсменок {max_Country_medals}')
print(f'Меньше всего участие принимали в {min_total_in_sport}')

'''
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
    
if __name__ == '__main__':
    df = []
    with open('london_athletes.csv', encoding='UTF-8') as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            df.append(row)
    
    max_age = age_sport(df)
    max_Country_medals = F_medals(df)
    min_total_in_sport = min_sport(df)

    print(f'Больше всего участников с возрастом {max_age}')
    print(f'Больше всего медалей у спортсменок {max_Country_medals}')
    print(f'Меньше всего участие принимали в {min_total_in_sport}')