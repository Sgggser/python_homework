import pprint
import string
import csv



def get_data_from_csv(filename):

    f = open(filename, "r")
    list_dicts = [row for row in csv.DictReader(f)] # получаем список словарей
    f.close()

    return list_dicts


def print_sex_distribution(passengers):
    male_num = 0
    female_num = 0
    for person in passengers:
        if person['Sex'] == 'male':
            male_num += 1
        elif person['Sex'] == 'female':
            female_num += 1
    print("Male: %d, %.2f per cent" % (male_num, 100*male_num/len(passengers)))
    print("Female: %d, %.2f per cent" % (female_num, 100*female_num/len(passengers)))
    print()
    male_num = 0
    female_num = 0
    for person in passengers:
        if person['Survived'] == '1' and person['Sex'] == 'male':
            male_num += 1
        elif person['Survived'] == '1' and person['Sex'] == 'female':
            female_num += 1
    print('Male survived: %d \nFemale survived %d' % (male_num, female_num))



def print_pclass_distribution(passengers):
    pclass = [0, 0, 0]
    pclass_survived = [0, 0, 0]
    for person in passengers:
        pclass[int(person['Pclass'])-1] += 1
        pclass_survived[int(person['Pclass']) - 1] += int(person['Survived'])
    print('1st class: %d \n2nd class: %d \n3rd class: %d' % (pclass[0], pclass[1], pclass[2]))
    print()
    print('--- Survived ---')
    print('1st class: %d \n2nd class: %d \n3rd class: %d' % (pclass_survived[0], pclass_survived[1], pclass_survived[2]))


passengers = get_data_from_csv(r'C:\Users\ADMIN\PycharmProjects\Sgggser\Classwork\titanic.csv')

print('Total passengers: %s' % len(passengers))
print_sex_distribution(passengers)
print()
print('Total distributed by class: %s' % len(passengers))
print_pclass_distribution(passengers)