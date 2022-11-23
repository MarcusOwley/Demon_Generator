import database
import random

lore_points = [1,2,3]
lore_points_checked = random.choice(lore_points)
three_lore_print = ""

first_lore_points = 0
second_lore_ponts = 0
third_lore_ponts = 0

torment = 0

if database.create_demon:
    group_of_demon = random.choice(database.demons_groups)
    house_demon = random.choice(database.houses)
    
    if house_demon == 'Дьяволы':
        torment = 4
        if lore_points_checked == 3:
            first_lore_points = 3
            first_lore = random.choice(database.demons_lore_devils)
            print("Lore is: ", first_lore)
        elif lore_points_checked == 2:
            first_lore_points = 2
            second_lore_ponts = 1
            lore_1 = random.choice(database.demons_lore_devils)
            lore_2 = random.choice(database.demons_lore_devils)
            while lore_1 == lore_2:
                lore_1 = random.choice(database.demons_lore_devils)
                lore_2 = random.choice(database.demons_lore_devils)
            two_lores = lore_1 + "\n" + lore_2
            print("Lore is: ", two_lores)
        else:
            first_lore_points = 1
            second_lore_ponts = 1
            third_lore_ponts = 1
            random.shuffle(database.demons_lore_devils)
            print("Lore is: ", database.demons_lore_devils)   
            three_lore = database.demons_lore_devils[0]
            three_lore_print = database.demons_lore_devils[0] + "\n" + database.demons_lore_devils[1] + "\n" + database.demons_lore_devils[2]
    elif house_demon == 'Кнуты':
        torment = 3
        if lore_points_checked == 3:
            first_lore_points = 3
            first_lore = random.choice(database.demons_lore_scourge)
            print("Lore is: ", first_lore)
        elif lore_points_checked == 2:
            first_lore_points = 2
            second_lore_ponts = 1
            lore_1 = random.choice(database.demons_lore_scourge)
            lore_2 = random.choice(database.demons_lore_scourge)
            while lore_1 == lore_2:
                lore_1 = random.choice(database.demons_lore_scourge)
                lore_2 = random.choice(database.demons_lore_scourge)
            two_lores = lore_1 + "\n" + lore_2
            print("Lore is: ", two_lores)
        elif lore_points_checked == 1:
            first_lore_points = 1
            second_lore_ponts = 1
            third_lore_ponts = 1
            random.shuffle(database.demons_lore_scourge)
            print("Lore is: ", database.demons_lore_scourge)   
            three_lore = database.demons_lore_scourge[0]
            three_lore_print = database.demons_lore_scourge[0] + "\n" + database.demons_lore_scourge[1] + "\n" + database.demons_lore_scourge[2]
    elif house_demon == 'Преступники':
        torment = 3
        if lore_points_checked == 3:
            first_lore_points = 3
            first_lore = random.choice(database.demons_lore_malefactors)
            print("Lore is: ", first_lore)
        elif lore_points_checked == 2:
            first_lore_points = 2
            second_lore_ponts = 1
            lore_1 = random.choice(database.demons_lore_malefactors)
            lore_2 = random.choice(database.demons_lore_malefactors)
            while lore_1 == lore_2:
                lore_1 = random.choice(database.demons_lore_malefactors)
                lore_2 = random.choice(database.demons_lore_malefactors)
            two_lores = lore_1 + "\n" + lore_2
            print("Lore is: ", two_lores)
        else:
            first_lore_points = 1
            second_lore_ponts = 1
            third_lore_ponts = 1
            random.shuffle(database.demons_lore_malefactors)
            print("Lore is: ", database.demons_lore_malefactors)   
            three_lore = database.demons_lore_malefactors[0]
            three_lore_print = database.demons_lore_malefactors[0] + "\n" + database.demons_lore_malefactors[1] + "\n" + database.demons_lore_malefactors[2]
    elif house_demon == 'Изверги':
        torment = 3
        if lore_points_checked == 3:
            first_lore_points = 3
            first_lore = random.choice(database.demons_lore_fiends)
            print("Lore is: ", first_lore)
        elif lore_points_checked == 2:
            first_lore_points = 2
            second_lore_ponts = 1
            lore_1 = random.choice(database.demons_lore_fiends)
            lore_2 = random.choice(database.demons_lore_fiends)
            while lore_1 == lore_2:
                lore_1 = random.choice(database.demons_lore_fiends)
                lore_2 = random.choice(database.demons_lore_fiends)
            two_lores = lore_1 + "\n" + lore_2
            print("Lore is: ", two_lores)
        else:
            first_lore_points = 1
            second_lore_ponts = 1
            third_lore_ponts = 1
            random.shuffle(database.demons_lore_fiends)
            print("Lore is: ", database.demons_lore_fiends)   
            three_lore = database.demons_lore_fiends[0]
            three_lore_print = database.demons_lore_fiends[0] + "\n" + database.demons_lore_fiends[1] + "\n" + database.demons_lore_fiends[2]
    elif house_demon == 'Осквернители':
        torment = 3
        if lore_points_checked == 3:
            first_lore_points = 3
            first_lore = random.choice(database.demons_lore_defilers)
            print("Lore is: ", first_lore)
        elif lore_points_checked == 2:
            first_lore_points = 2
            second_lore_ponts = 1
            lore_1 = random.choice(database.demons_lore_defilers)
            lore_2 = random.choice(database.demons_lore_defilers)
            while lore_1 == lore_2:
                lore_1 = random.choice(database.demons_lore_defilers)
                lore_2 = random.choice(database.demons_lore_defilers)
            two_lores = lore_1 + "\n" + lore_2
            print("Lore is: ", two_lores)
        else:
            first_lore_points = 1
            second_lore_ponts = 1
            third_lore_ponts = 1
            random.shuffle(database.demons_lore_defilers)
            print("Lore is: ", database.demons_lore_defilers)   
            three_lore = database.demons_lore_defilers[0]
            three_lore_print = database.demons_lore_defilers[0] + "\n" + database.demons_lore_defilers[1] + "\n" + database.demons_lore_defilers[2]
    elif house_demon == 'Пожиратели':
        torment = 4
        if lore_points_checked == 3:
            first_lore_points = 3
            first_lore = random.choice(database.demons_lore_devourers)
            print("Lore is: ", first_lore)
        elif lore_points_checked == 2:
            first_lore_points = 2
            second_lore_ponts = 1
            lore_1 = random.choice(database.demons_lore_devourers)
            lore_2 = random.choice(database.demons_lore_devourers)
            while lore_1 == lore_2:
                lore_1 = random.choice(database.demons_lore_devourers)
                lore_2 = random.choice(database.demons_lore_devourers)
            two_lores = lore_1 + "\n" + lore_2
            print("Lore is: ", two_lores)
        else:
            first_lore_points = 1
            second_lore_ponts = 1
            third_lore_ponts = 1
            random.shuffle(database.demons_lore_devourers)
            print("Lore is: ", database.demons_lore_devourers)   
            three_lore = database.demons_lore_devourers[0]
            three_lore_print = database.demons_lore_devourers[0] + "\n" + database.demons_lore_devourers[1] + "\n" + database.demons_lore_devourers[2]
    elif house_demon == 'Убийцы':
        torment = 4
        if lore_points_checked == 3:
            first_lore_points = 3
            first_lore = random.choice(database.demons_lore_slayers)
            print("Lore is: ", first_lore)
        elif lore_points_checked == 2:
            first_lore_points = 2
            second_lore_ponts = 1
            lore_1 = random.choice(database.demons_lore_slayers)
            lore_2 = random.choice(database.demons_lore_slayers)
            while lore_1 == lore_2:
                lore_1 = random.choice(database.demons_lore_slayers)
                lore_2 = random.choice(database.demons_lore_slayers)
            two_lores = lore_1 + "\n" + lore_2
            print("Lore is: ", two_lores)
        else:
            first_lore_points = 1
            second_lore_ponts = 1
            third_lore_ponts = 1
            random.shuffle(database.demons_lore_slayers)
            print("Lore is: ", database.demons_lore_slayers)   
            three_lore = database.demons_lore_slayers[0]
            three_lore_print = database.demons_lore_slayers[0] + "\n" + database.demons_lore_slayers[1] + "\n" + database.demons_lore_slayers[2]
    
    if lore_points_checked == 2:
        if lore_1 == 'Знание Небожителей':
            apocalyptic_form = 'Бел'
        elif lore_1 == 'Знание Пламени':
            apocalyptic_form = 'Нуску'
        elif lore_1 == 'Знание Сияния':
            apocalyptic_form = 'Куингу'
        elif lore_1 == 'Знание Ветра':
            apocalyptic_form = 'Эллиль'
        elif lore_1 == 'Знание Пробуждения':
            apocalyptic_form = 'Даган'
        elif lore_1 == 'Знание Небесного Свода':
            apocalyptic_form = 'Аншар'
        elif lore_1 == 'Знание Земли':
            apocalyptic_form = 'Кишар'
        elif lore_1 == 'Знание Кузнечного дела':
            apocalyptic_form = 'Мумму'
        elif lore_1 == 'Знание Путей':
            apocalyptic_form = 'Анту'
        elif lore_1 == 'Знание Света':
            apocalyptic_form = 'Шамаш'
        elif lore_1 == 'Знание Узоров':
            apocalyptic_form = 'Нинсун'
        elif lore_1 == 'Знание Порталов':
            apocalyptic_form = 'Неду'
        elif lore_1 == 'Знание Желания':
            apocalyptic_form = 'Исхара'
        elif lore_1 == 'Знание Бурь':
            apocalyptic_form = 'Адад'
        elif lore_1 == 'Знание Метаморфоз':
            apocalyptic_form = 'Мамметум'
        elif lore_1 == 'Знание Зверей':
            apocalyptic_form = 'Залту'
        elif lore_1 == 'Знание Плоти':
            apocalyptic_form = 'Аруру'
        elif lore_1 == 'Знание Дикой Природы':
            apocalyptic_form = 'Нинурту'
        elif lore_1 == 'Знание Смерти':
            apocalyptic_form = 'Намтар'
        elif lore_1 == 'Знание Сфер':
            apocalyptic_form = 'Эрешкигаль'
        elif lore_1 == 'Знание Душ':
            apocalyptic_form = 'Нергал'
        else:
            print('ERRORSCUM')

    elif lore_points_checked == 1:
        if three_lore == 'Знание Небожителей':
            apocalyptic_form = 'Бел'
        elif three_lore == 'Знание Пламени':
                apocalyptic_form = 'Нуску'
        elif three_lore == 'Знание Сияния':
                apocalyptic_form = 'Куингу'
        elif three_lore == 'Знание Ветра':
                apocalyptic_form = 'Эллиль'
        elif three_lore == 'Знание Пробуждения':
                apocalyptic_form = 'Даган'
        elif three_lore == 'Знание Небесного Свода':
                apocalyptic_form = 'Аншар'
        elif three_lore == 'Знание Земли':
            apocalyptic_form = 'Кишар'
        elif three_lore == 'Знание Кузнечного дела':
            apocalyptic_form = 'Мумму'
        elif three_lore == 'Знание Путей':
            apocalyptic_form = 'Анту'
        elif three_lore == 'Знание Света':
                apocalyptic_form = 'Шамаш'
        elif three_lore == 'Знание Узоров':
                apocalyptic_form = 'Нинсун'
        elif three_lore == 'Знание Порталов':
                apocalyptic_form = 'Неду'
        elif three_lore == 'Знание Желания':
                apocalyptic_form = 'Исхара'
        elif three_lore == 'Знание Бурь':
                apocalyptic_form = 'Адад'
        elif three_lore == 'Знание Метаморфоз':
                apocalyptic_form = 'Мамметум'
        elif three_lore == 'Знание Зверей':
                apocalyptic_form = 'Залту'
        elif three_lore == 'Знание Плоти':
                apocalyptic_form = 'Аруру'
        elif three_lore == 'Знание Дикой Природы':
                apocalyptic_form = 'Нинурту'
        elif three_lore == 'Знание Смерти':
                apocalyptic_form = 'Намтар'
        elif three_lore == 'Знание Сфер':
                apocalyptic_form = 'Эрешкигаль'
        elif three_lore == 'Знание Душ':
                apocalyptic_form = 'Нергал'
        else:
                print('ERRORSCUM')
    else:
        if first_lore == 'Знание Небожителей':
            apocalyptic_form = 'Бел'
        elif first_lore == 'Знание Пламени':
            apocalyptic_form = 'Нуску'
        elif first_lore == 'Знание Сияния':
            apocalyptic_form = 'Куингу'
        elif first_lore == 'Знание Ветра':
            apocalyptic_form = 'Эллиль'
        elif first_lore == 'Знание Пробуждения':
            apocalyptic_form = 'Даган'
        elif first_lore == 'Знание Небесного Свода':
            apocalyptic_form = 'Аншар'
        elif first_lore == 'Знание Земли':
            apocalyptic_form = 'Кишар'
        elif first_lore == 'Знание Кузнечного дела':
            apocalyptic_form = 'Мумму'
        elif first_lore == 'Знание Путей':
            apocalyptic_form = 'Анту'
        elif first_lore == 'Знание Света':
            apocalyptic_form = 'Шамаш'
        elif first_lore == 'Знание Узоров':
            apocalyptic_form = 'Нинсун'
        elif first_lore == 'Знание Порталов':
            apocalyptic_form = 'Неду'
        elif first_lore == 'Знание Желания':
            apocalyptic_form = 'Исхара'
        elif first_lore == 'Знание Бурь':
            apocalyptic_form = 'Адад'
        elif first_lore == 'Знание Метаморфоз':
            apocalyptic_form = 'Мамметум'
        elif first_lore == 'Знание Зверей':
            apocalyptic_form = 'Залту'
        elif first_lore == 'Знание Плоти':
            apocalyptic_form = 'Аруру'
        elif first_lore == 'Знание Дикой Природы':
            apocalyptic_form = 'Нинурту'
        elif first_lore == 'Знание Смерти':
            apocalyptic_form = 'Намтар'
        elif first_lore == 'Знание Сфер':
            apocalyptic_form = 'Эрешкигаль'
        elif first_lore == 'Знание Душ':
            apocalyptic_form = 'Нергал'
        else:
            print('ERRORSCUM')
else:
    print('YOUR DEMON ALREADY EXIST')

if first_lore_points == 1:
    print_lorepoints_1 = "•"
elif first_lore_points == 2:
    print_lorepoints_1 = "••"
elif first_lore_points == 3:
    print_lorepoints_1 = "•••"
else:
    print_lorepoints_1 = " "

if second_lore_ponts == 1:
    print_lorepoints_2 = "•"
else:
    print_lorepoints_2 = " "

if third_lore_ponts == 1:
    print_lorepoints_3 = "•"
else:
    print_lorepoints_3 = " "

print(three_lore_print)