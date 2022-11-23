import database
import random
import numpy as np


faith = 0

backpoints_state = True

atributes = [database.atributes_phys, database.atributes_social, database.atributes_mental]

a_points = 7
b_points = 5
c_points = 3

random.shuffle(atributes)

priority_1 = atributes[0]
priority_2 = atributes[1]
priority_3 = atributes[2]

talents_points = 13
skills_points = 9
knowledges_points = 5

random.shuffle(database.talents_abilities)
random.shuffle(database.skills_abilities)
random.shuffle(database.knowledges_abilities)

random.shuffle(database.backgrounds)

backgrounds_points = 5

first_ability = 0
second_ability = 0
third_ability = 0
first_ability_1 = 0
second_ability_1 = 0
third_ability_1 = 0
first_ability_2 = 0
second_ability_2 = 0
third_ability_2 = 0

while a_points > 0:
    #print(a_points)
    if a_points == 0 :
        break
    div_point = random.randint(1,min(3,a_points))
    a_points = a_points - div_point
    first_ability = first_ability + div_point
    if a_points == 0 :
        break
    div_point = random.randint(1,min(3,a_points))
    a_points = a_points - div_point
    second_ability = second_ability + div_point
    if a_points == 0 :
        break
    div_point = random.randint(1,min(3,a_points))
    a_points = a_points - div_point
    third_ability = third_ability + div_point

while b_points > 0:
    #print(b_points)
    if b_points == 0 :
        break
    div_point = random.randint(1,min(3,b_points))
    b_points = b_points - div_point
    first_ability_1 = first_ability_1 + div_point
    if b_points == 0 :
        break
    div_point = random.randint(1,min(3,b_points))
    b_points = b_points - div_point
    second_ability_1 = second_ability_1 + div_point
    if b_points == 0 :
        break
    div_point = random.randint(1,min(3,b_points))
    b_points = b_points - div_point
    third_ability_1 = third_ability_1 + div_point

while c_points > 0:
    #print(c_points)
    if c_points == 0 :
        break
    div_point = random.randint(1,min(3,c_points))
    c_points = c_points - div_point
    first_ability_2 = first_ability_2 + div_point
    if c_points == 0 :
        break
    div_point = random.randint(1,min(3,c_points))
    c_points = c_points - div_point
    second_ability_2 = second_ability_2 + div_point
    if c_points == 0 :
        break
    div_point = random.randint(1,min(3,c_points))
    c_points = c_points - div_point
    third_ability_2 = third_ability_2 + div_point



talent_1 = 0
talent_2 = 0
talent_3 = 0
talent_4 = 0
talent_5 = 0
talent_6 = 0
talent_7 = 0
talent_8 = 0
talent_9 = 0
talent_10 = 0
talent_11 = 0
talent_12 = 0
skills_1 = 0
skills_2 = 0
skills_3 = 0
skills_4 = 0
skills_5 = 0
skills_6 = 0
skills_7 = 0
skills_8 = 0
skills_9 = 0
skills_10 = 0
skills_11 = 0
skills_12 = 0
knowledges_1 = 0
knowledges_2 = 0
knowledges_3 = 0
knowledges_4 = 0
knowledges_5 = 0
knowledges_6 = 0
knowledges_7 = 0
knowledges_8 = 0
knowledges_9 = 0
knowledges_10 = 0
knowledges_11 = 0
knowledges_12 = 0



while talents_points > 0:                                                   #<--------------------Talents abilities
    #print(talents_points)
    if talents_points == 0 :
        break
    div_point = random.randint(1,min(3,talents_points))
    talents_points = talents_points - div_point
    talent_1 = talent_1 + div_point
    if talents_points == 0 :
        break
    div_point = random.randint(1,min(3,talents_points))
    talents_points = talents_points - div_point
    talent_2 = talent_2 + div_point
    if talents_points == 0 :
        break
    div_point = random.randint(1,min(3,talents_points))
    talents_points = talents_points - div_point
    talent_3 = talent_3 + div_point
    if talents_points == 0 :
        break
    div_point = random.randint(1,min(3,talents_points))
    talents_points = talents_points - div_point
    talent_4 = talent_4 + div_point
    if talents_points == 0 :
        break
    div_point = random.randint(1,min(3,talents_points))
    talents_points = talents_points - div_point
    talent_5 = talent_5 + div_point
    if talents_points == 0 :
        break
    div_point = random.randint(1,min(3,talents_points))
    talents_points = talents_points - div_point
    talent_6 = talent_6 + div_point
    if talents_points == 0 :
        break
    div_point = random.randint(1,min(3,talents_points))
    talents_points = talents_points - div_point
    talent_7 = talent_7 + div_point
    if talents_points == 0 :
        break
    div_point = random.randint(1,min(3,talents_points))
    talents_points = talents_points - div_point
    talent_8 = talent_8 + div_point
    if talents_points == 0 :
        break
    div_point = random.randint(1,min(3,talents_points))
    talents_points = talents_points - div_point
    talent_9 = talent_9 + div_point
    if talents_points == 0 :
        break
    div_point = random.randint(1,min(3,talents_points))
    talents_points = talents_points - div_point
    talent_10 = talent_10 + div_point
    if talents_points == 0 :
        break
    div_point = random.randint(1,min(3,talents_points))
    talents_points = talents_points - div_point
    talent_11 = talent_11 + div_point
    if talents_points == 0 :
        break
    div_point = random.randint(1,min(3,talents_points))
    talents_points = talents_points - div_point
    talent_12 = talent_12 + div_point


while skills_points > 0:                                                                            #<--------------------Skills abilities
    #print(skills_points)
    if skills_points == 0 :
        break
    div_point = random.randint(1,min(3,skills_points))
    skills_points = skills_points - div_point
    skills_1 = skills_1 + div_point
    if skills_points == 0 :
        break
    div_point = random.randint(1,min(3,skills_points))
    skills_points = skills_points - div_point
    skills_2 = skills_2 + div_point
    if skills_points == 0 :
        break
    div_point = random.randint(1,min(3,skills_points))
    skills_points = skills_points - div_point
    skills_3 = skills_3 + div_point
    if skills_points == 0 :
        break
    div_point = random.randint(1,min(3,skills_points))
    skills_points = skills_points - div_point
    skills_4 = skills_4 + div_point
    if skills_points == 0 :
        break
    div_point = random.randint(1,min(3,skills_points))
    skills_points = skills_points - div_point
    skills_5 = skills_5 + div_point
    if skills_points == 0 :
        break
    div_point = random.randint(1,min(3,skills_points))
    skills_points = skills_points - div_point
    skills_6 = skills_6 + div_point
    if skills_points == 0 :
        break
    div_point = random.randint(1,min(3,skills_points))
    skills_points = skills_points - div_point
    skills_7 = skills_7 + div_point
    if skills_points == 0 :
        break
    div_point = random.randint(1,min(3,skills_points))
    skills_points = skills_points - div_point
    skills_8 = skills_8 + div_point
    if skills_points == 0 :
        break
    div_point = random.randint(1,min(3,skills_points))
    skills_points = skills_points - div_point
    skills_9 = skills_9 + div_point
    if skills_points == 0 :
        break
    div_point = random.randint(1,min(3,skills_points))
    skills_points = skills_points - div_point
    skills_10 = skills_10 + div_point
    if skills_points == 0 :
        break
    div_point = random.randint(1,min(3,skills_points))
    skills_points = skills_points - div_point
    skills_11 = skills_11 + div_point
    if skills_points == 0 :
        break
    div_point = random.randint(1,min(3,skills_points))
    skills_points = skills_points - div_point
    skills_12 = skills_12 + div_point

while knowledges_points > 0:                                                                            #<--------------------Skills abilities
    #print(knowledges_points)
    if knowledges_points == 0 :
        break
    div_point = random.randint(1,min(3,knowledges_points))
    knowledges_points = knowledges_points - div_point
    knowledges_1 = knowledges_1 + div_point
    if knowledges_points == 0 :
        break
    div_point = random.randint(1,min(3,knowledges_points))
    knowledges_points = knowledges_points - div_point
    knowledges_2 = knowledges_2 + div_point
    if knowledges_points == 0 :
        break
    div_point = random.randint(1,min(3,knowledges_points))
    knowledges_points = knowledges_points - div_point
    knowledges_3 = knowledges_3 + div_point
    if knowledges_points == 0 :
        break
    div_point = random.randint(1,min(3,knowledges_points))
    knowledges_points = knowledges_points - div_point
    knowledges_4 = knowledges_4 + div_point
    if knowledges_points == 0 :
        break
    div_point = random.randint(1,min(3,knowledges_points))
    knowledges_points = knowledges_points - div_point
    knowledges_5 = knowledges_5 + div_point
    if knowledges_points == 0 :
        break
    div_point = random.randint(1,min(3,knowledges_points))
    knowledges_points = knowledges_points - div_point
    knowledges_6 = knowledges_6 + div_point
    if knowledges_points == 0 :
        break
    div_point = random.randint(1,min(3,knowledges_points))
    knowledges_points = knowledges_points - div_point
    knowledges_7 = knowledges_7 + div_point
    if knowledges_points == 0 :
        break
    div_point = random.randint(1,min(3,knowledges_points))
    knowledges_points = knowledges_points - div_point
    knowledges_8 = knowledges_8 + div_point
    if knowledges_points == 0 :
        break
    div_point = random.randint(1,min(3,knowledges_points))
    knowledges_points = knowledges_points - div_point
    knowledges_9 = knowledges_9 + div_point
    if knowledges_points == 0 :
        break
    div_point = random.randint(1,min(3,knowledges_points))
    knowledges_points = knowledges_points - div_point
    knowledges_10 = knowledges_10 + div_point
    if knowledges_points == 0 :
        break
    div_point = random.randint(1,min(3,knowledges_points))
    knowledges_points = knowledges_points - div_point
    knowledges_11 = knowledges_11 + div_point
    if knowledges_points == 0 :
        break
    div_point = random.randint(1,min(3,knowledges_points))
    knowledges_points = knowledges_points - div_point
    knowledges_12 = knowledges_12 + div_point

back_points_1 = 0
back_points_2 = 0
back_points_3 = 0
back_points_4 = 0
back_points_5 = 0
back_points_6 = 0
back_points_7 = 0
back_points_8 = 0
back_points_9 = 0
back_points_10 = 0
back_points_11 = 0

while backgrounds_points > 0:
    print(backgrounds_points)
    if backgrounds_points == 0 :
        break
    div_point = random.randint(1,min(5,backgrounds_points))
    backgrounds_points = backgrounds_points - div_point
    back_points_1 = back_points_1 + div_point
    if backgrounds_points == 0 :
        break
    div_point = random.randint(1,min(5,backgrounds_points))
    backgrounds_points = backgrounds_points - div_point
    back_points_2 = back_points_2 + div_point
    if backgrounds_points == 0 :
        break
    div_point = random.randint(1,min(5,backgrounds_points))
    backgrounds_points = backgrounds_points - div_point
    back_points_3 = back_points_3 + div_point
    if backgrounds_points == 0 :
        break
    div_point = random.randint(1,min(5,backgrounds_points))
    backgrounds_points = backgrounds_points - div_point
    back_points_4 = back_points_4 + div_point
    if backgrounds_points == 0 :
        break
    div_point = random.randint(1,min(5,backgrounds_points))
    backgrounds_points = backgrounds_points - div_point
    back_points_5 = back_points_5 + div_point
    if backgrounds_points == 0 :
        break
    div_point = random.randint(1,min(5,backgrounds_points))
    backgrounds_points = backgrounds_points - div_point
    back_points_6 = back_points_6 + div_point
    if backgrounds_points == 0 :
        break
    div_point = random.randint(1,min(5,backgrounds_points))
    backgrounds_points = backgrounds_points - div_point
    back_points_7 = back_points_7 + div_point
    if backgrounds_points == 0 :
        break
    div_point = random.randint(1,min(5,backgrounds_points))
    backgrounds_points = backgrounds_points - div_point
    back_points_8 = back_points_8 + div_point
    if backgrounds_points == 0 :
        break
    div_point = random.randint(1,min(5,backgrounds_points))
    backgrounds_points = backgrounds_points - div_point
    back_points_9 = back_points_9 + div_point
    if backgrounds_points == 0 :
        break
    div_point = random.randint(1,min(5,backgrounds_points))
    backgrounds_points = backgrounds_points - div_point
    back_points_10 = back_points_10 + div_point
    if backgrounds_points == 0 :
        break
    div_point = random.randint(1,min(5,backgrounds_points))
    backgrounds_points = backgrounds_points - div_point
    back_points_11 = back_points_11 + div_point

mass_points_1 = [database.backgrounds[0], back_points_1]
mass_points_2 = [database.backgrounds[1], back_points_2]
mass_points_3 = [database.backgrounds[2], back_points_3]
mass_points_4 = [database.backgrounds[3], back_points_4]
mass_points_5 = [database.backgrounds[4], back_points_5]
mass_points_6 = [database.backgrounds[5], back_points_6]
mass_points_7 = [database.backgrounds[6], back_points_7]
mass_points_8 = [database.backgrounds[7], back_points_8]
mass_points_9 = [database.backgrounds[8], back_points_9]
mass_points_10 = [database.backgrounds[9], back_points_10]
mass_points_11 = [database.backgrounds[10], back_points_11]

if mass_points_1[0] == 'Договоры' or mass_points_1[0] == 'Последователи':
    faith = faith + mass_points_1[1]
if mass_points_2[0] == 'Договоры' or mass_points_2[0] == 'Последователи':
    faith = faith + mass_points_2[1]
if mass_points_3[0] == 'Договоры' or mass_points_3[0] == 'Последователи':
    faith = faith + mass_points_3[1]
if mass_points_4[0] == 'Договоры' or mass_points_4[0] == 'Последователи':
    faith = faith + mass_points_4[1]
if mass_points_5[0] == 'Договоры' or mass_points_5[0] == 'Последователи':
    faith = faith + mass_points_5[1]
if mass_points_6[0] == 'Договоры' or mass_points_6[0] == 'Последователи':
    faith = faith + mass_points_6[1]
if mass_points_7[0] == 'Договоры' or mass_points_7[0] == 'Последователи':
    faith = faith + mass_points_7[1]
if mass_points_8[0] == 'Договоры' or mass_points_8[0] == 'Последователи':
    faith = faith + mass_points_8[1]
if mass_points_9[0] == 'Договоры' or mass_points_9[0] == 'Последователи':
    faith = faith + mass_points_9[1]
if mass_points_10[0] == 'Договоры' or mass_points_10[0] == 'Последователи':
    faith = faith + mass_points_10[1]
if mass_points_11[0] == 'Договоры' or mass_points_11[0] == 'Последователи':
    faith = faith + mass_points_11[1]

first_one = priority_1[0], first_ability + 1, priority_1[1], second_ability + 1, priority_1[2], third_ability + 1
first_two = priority_2[0], first_ability_1 + 1, priority_2[1], second_ability_1 + 1, priority_2[2], third_ability_1 + 1
first_three =  priority_3[0], first_ability_2 + 1, priority_3[1], second_ability_2 + 1, priority_3[2], third_ability_2 + 1

second_one = database.talents_abilities[0], talent_1, database.talents_abilities[1], talent_2, database.talents_abilities[2], talent_3, database.talents_abilities[3], talent_4, database.talents_abilities[4], talent_5, database.talents_abilities[5], talent_6, database.talents_abilities[6], talent_7, database.talents_abilities[7], talent_8, database.talents_abilities[8], talent_9, database.talents_abilities[9], talent_10, database.talents_abilities[10], talent_11, database.talents_abilities[11], talent_12
second_two = database.skills_abilities[0], skills_1, database.skills_abilities[1], skills_2, database.skills_abilities[2], skills_3, database.skills_abilities[3], skills_4, database.skills_abilities[4], skills_5, database.skills_abilities[5], skills_6, database.skills_abilities[6], skills_7, database.skills_abilities[7], skills_8, database.skills_abilities[8], skills_9, database.skills_abilities[9], skills_10, database.skills_abilities[10], skills_11, database.skills_abilities[11], skills_12
second_three = database.knowledges_abilities[0], knowledges_1, database.knowledges_abilities[1], knowledges_2, database.knowledges_abilities[2], knowledges_3, database.knowledges_abilities[3], knowledges_4, database.knowledges_abilities[4], knowledges_5, database.knowledges_abilities[5], knowledges_6, database.knowledges_abilities[6], knowledges_7, database.knowledges_abilities[7], knowledges_8, database.knowledges_abilities[8], knowledges_9, database.knowledges_abilities[9], knowledges_10, database.knowledges_abilities[10], knowledges_11, database.knowledges_abilities[11], knowledges_12

if backpoints_state:
    back_print_1 = ""
    back_print_2 = ""
    back_print_3 = ""
    back_print_4 = ""
    back_print_5 = ""
    back_print_6 = ""
    back_print_7 = ""
    back_print_8 = ""
    back_print_9 = ""
    back_print_10 = ""
    back_print_11 = ""
    if back_points_1 > 0:
        print("Backgrounds is: ------------ ", database.backgrounds[0], back_points_1)
        back_print_1 = database.backgrounds[0]
    if back_points_2 > 0:
        print("Backgrounds is: ------------ ", database.backgrounds[1], back_points_2)
        back_print_2 = database.backgrounds[1]
    if back_points_3 > 0:
        print("Backgrounds is: ------------ ", database.backgrounds[2], back_points_3)
        back_print_3 = database.backgrounds[2]
    if back_points_4 > 0:
        print("Backgrounds is: ------------ ", database.backgrounds[3], back_points_4)
        back_print_4 = database.backgrounds[3]
    if back_points_5 > 0:
        print("Backgrounds is: ------------ ", database.backgrounds[4], back_points_5)
        back_print_5 = database.backgrounds[4]
    if back_points_6 > 0:
        print("Backgrounds is: ------------ ", database.backgrounds[5], back_points_6)
        back_print_6 = database.backgrounds[5]
    if back_points_7 > 0:
        print("Backgrounds is: ------------ ", database.backgrounds[6], back_points_7)
        back_print_7 = database.backgrounds[6]
    if back_points_8 > 0:
        print("Backgrounds is: ------------ ", database.backgrounds[7], back_points_8)
        back_print_8 = database.backgrounds[7]
    if back_points_9 > 0:
        print("Backgrounds is: ------------ ", database.backgrounds[8], back_points_9)
        back_print_9 = database.backgrounds[8]
    if back_points_10 > 0:
        print("Backgrounds is: ------------ ", database.backgrounds[9], back_points_10)
        back_print_10 = database.backgrounds[9]
    if back_points_11 > 0:
        print("Backgrounds is: ------------ ", database.backgrounds[10], back_points_11)
        back_print_11 = database.backgrounds[10]
    
    back_print = back_print_1 + "\n" + back_print_2 + "\n" + back_print_3 + "\n" + back_print_4 + "\n" + back_print_5 + "\n" + back_print_6 + "\n" + back_print_7 + "\n" + back_print_8 + "\n" + back_print_9 + "\n" + back_print_10 + "\n" + back_print_11
    print(back_print)



print_point_1 = " "
print_point_2 = " "
print_point_3 = " "
print_point_4 = " "
print_point_5 = " "
print_point_6 = " "
print_point_7 = " "
print_point_8 = " "
print_point_9 = " "

# Принт абилок

if first_ability == 1:
    print_point_1 = "•"
elif first_ability == 2:
    print_point_1 = "••"
elif first_ability == 3:
    print_point_1 = "•••"
elif first_ability == 4:
    print_point_1 = "••••"

if second_ability == 1:
    print_point_2 = "•"
elif second_ability == 2:
    print_point_2 = "••"
elif second_ability == 3:
    print_point_2 = "•••"
elif second_ability == 4:
    print_point_2 = "••••"

if third_ability == 1:
    print_point_3 = "•"
elif third_ability == 2:
    print_point_3 = "••"
elif third_ability == 3:
    print_point_3 = "•••"
elif third_ability == 4:
    print_point_3 = "••••"
#----------------------------
if first_ability_1 == 1:
    print_point_4 = "•"
elif first_ability_1 == 2:
    print_point_4 = "••"
elif first_ability_1 == 3:
    print_point_4 = "•••"
elif first_ability_1 == 4:
    print_point_4 = "••••"

if second_ability_1 == 1:
    print_point_5 = "•"
elif second_ability_1 == 2:
    print_point_5 = "••"
elif second_ability_1 == 3:
    print_point_5 = "•••"
elif second_ability_1 == 4:
    print_point_5 = "••••"

if third_ability_1 == 1:
    print_point_6 = "•"
elif third_ability_1 == 2:
    print_point_6 = "••"
elif third_ability_1 == 3:
    print_point_6 = "•••"
elif third_ability_1 == 4:
    print_point_6 = "••••"
#----------------------------
if first_ability_2 == 1:
    print_ability_7 = "•"
elif first_ability_2 == 2:
    print_point_7 = "••"
elif first_ability_2 == 3:
    print_point_7 = "•••"
elif first_ability_2 == 4:
    print_point_7 = "••••"

if second_ability_2 == 1:
    print_point_8 = "•"
elif second_ability_2 == 2:
    print_point_8 = "••"
elif second_ability_2 == 3:
    print_point_8 = "•••"
elif second_ability_2 == 4:
    print_point_8 = "••••"

if third_ability_2 == 1:
    print_point_9 = "•"
elif third_ability_2 == 2:
    print_point_9 = "••"
elif third_ability_2 == 3:
    print_point_9 = "•••"
elif third_ability_2 == 4:
    print_point_9 = "••••"


# Принт талантов
if talent_1 == 1:
    print_talent_1 = "•"
elif talent_1 == 2:
    print_talent_1 = "••"
elif talent_1 == 3:
    print_talent_1 = "•••"
else:
    print_talent_1 = " "

if talent_2 == 1:
    print_talent_2 = "•"
elif talent_2 == 2:
    print_talent_2 = "••"
elif talent_2 == 3:
    print_talent_2 = "•••"
else:
    print_talent_2 = " "

if talent_3 == 1:
    print_talent_3 = "•"
elif talent_3 == 2:
    print_talent_3 = "••"
elif talent_3 == 3:
    print_talent_3 = "•••"
elif talent_3 == 4:
    print_talent_3 = "•••"
else:
    print_talent_3 = " "

if talent_4 == 1:
    print_talent_4 = "•"
elif talent_4 == 2:
    print_talent_4 = "••"
elif talent_4 == 3:
    print_talent_4 = "•••"
else:
    print_talent_4 = " "

if talent_5 == 1:
    print_talent_5 = "•"
elif talent_5 == 2:
    print_talent_5 = "••"
elif talent_5 == 3:
    print_talent_5 = "•••"
else:
    print_talent_5 = " "

if talent_6 == 1:
    print_talent_6 = "•"
elif talent_6 == 2:
    print_talent_6 = "••"
elif talent_6 == 3:
    print_talent_6 = "•••"
else:
    print_talent_6 = " "


if talent_7 == 1:
    print_talent_7 = "•"
elif talent_7 == 2:
    print_talent_7 = "••"
elif talent_7 == 3:
    print_talent_7 = "•••"
else:
    print_talent_7 = " "


if talent_8 == 1:
    print_talent_8 = "•"
elif talent_8 == 2:
    print_talent_8 = "••"
elif talent_8 == 3:
    print_talent_8 = "•••"
else:
    print_talent_8 = " "


if talent_9 == 1:
    print_talent_9 = "•"
elif talent_9 == 2:
    print_talent_9 = "••"
elif talent_9 == 3:
    print_talent_9 = "•••"
else:
    print_talent_9 = " "


if talent_10 == 1:
    print_talent_10 = "•"
elif talent_10 == 2:
    print_talent_10 = "••"
elif talent_10 == 3:
    print_talent_10 = "•••"
else:
    print_talent_10 = " "


if talent_11 == 1:
    print_talent_11 = "•"
elif talent_11 == 2:
    print_talent_11 = "••"
elif talent_11 == 3:
    print_talent_11 = "•••"
else:
    print_talent_11 = " "


if talent_12 == 1:
    print_talent_12 = "•"
elif talent_12 == 2:
    print_talent_12 = "••"
elif talent_12 == 3:
    print_talent_12 = "•••"
else:
    print_talent_12 = " "

#___________________________________________

if skills_1 == 1:
    print_skills_1 = "•"
elif skills_1 == 2:
    print_skills_1 = "••"
elif skills_1 == 3:
    print_skills_1 = "•••"
else:
    print_skills_1 = " "

if skills_2 == 1:
    print_skills_2 = "•"
elif skills_2 == 2:
    print_skills_2 = "••"
elif skills_2 == 3:
    print_skills_2 = "•••"
else:
    print_skills_2 = " "

if skills_3 == 1:
    print_skills_3 = "•"
elif skills_3 == 2:
    print_skills_3 = "••"
elif skills_3 == 3:
    print_skills_3 = "•••"
else:
    print_skills_3 = " "

if skills_4 == 1:
    print_skills_4 = "•"
elif skills_4 == 2:
    print_skills_4 = "••"
elif skills_4 == 3:
    print_skills_4 = "•••"
else:
    print_skills_4 = " "

if skills_5 == 1:
    print_skills_5 = "•"
elif skills_5 == 2:
    print_skills_5 = "••"
elif skills_5 == 3:
    print_skills_5 = "•••"
else:
    print_skills_5 = " "

if skills_6 == 1:
    print_skills_6 = "•"
elif skills_6 == 2:
    print_skills_6 = "••"
elif skills_6 == 3:
    print_skills_6 = "•••"
else:
    print_skills_6 = " "

if skills_7 == 1:
    print_skills_7 = "•"
elif skills_7 == 2:
    print_skills_7 = "••"
elif skills_7 == 3:
    print_skills_7 = "•••"
else:
    print_skills_7 = " "

if skills_8 == 1:
    print_skills_8 = "•"
elif skills_8 == 2:
    print_skills_8 = "••"
elif skills_8 == 3:
    print_skills_8 = "•••"
else:
    print_skills_8 = " "

if skills_9 == 1:
    print_skills_9 = "•"
elif skills_9 == 2:
    print_skills_9 = "••"
elif skills_9 == 3:
    print_skills_9 = "•••"
else:
    print_skills_9 = " "

if skills_10 == 1:
    print_skills_10 = "•"
elif skills_10 == 2:
    print_skills_10 = "••"
elif skills_10 == 3:
    print_skills_10 = "•••"
else:
    print_skills_10 = " "

if skills_11 == 1:
    print_skills_11 = "•"
elif skills_11 == 2:
    print_skills_11 = "••"
elif skills_11 == 3:
    print_skills_11 = "•••"
else:
    print_skills_11 = " "

if skills_12 == 1:
    print_skills_12 = "•"
elif skills_12 == 2:
    print_skills_12 = "••"
elif skills_12 == 3:
    print_skills_12 = "•••"
else:
    print_skills_12 = " "

#_____________________________________________

if knowledges_1 == 1:
    print_knowledges_1 = "•"
elif knowledges_1 == 2:
    print_knowledges_1 = "••"
elif knowledges_1 == 3:
    print_knowledges_1 = "•••"
else:
    print_knowledges_1 = " "

if knowledges_2 == 1:
    print_knowledges_2 = "•"
elif knowledges_2 == 2:
    print_knowledges_2 = "••"
elif knowledges_2 == 3:
    print_knowledges_2 = "•••"
else:
    print_knowledges_2 = " "

if knowledges_3 == 1:
    print_knowledges_3 = "•"
elif knowledges_3 == 2:
    print_knowledges_3 = "••"
elif knowledges_3 == 3:
    print_knowledges_3 = "•••"
else:
    print_knowledges_3 = " "

if knowledges_4 == 1:
    print_knowledges_4 = "•"
elif knowledges_4 == 2:
    print_knowledges_4 = "••"
elif knowledges_4 == 3:
    print_knowledges_4 = "•••"
else:
    print_knowledges_4 = " "

if knowledges_5 == 1:
    print_knowledges_5 = "•"
elif knowledges_5 == 2:
    print_knowledges_5 = "••"
elif knowledges_5 == 3:
    print_knowledges_5 = "•••"
else:
    print_knowledges_5 = " "

if knowledges_6 == 1:
    print_knowledges_6 = "•"
elif knowledges_6 == 2:
    print_knowledges_6 = "••"
elif knowledges_6 == 3:
    print_knowledges_6 = "•••"
else:
    print_knowledges_6 = " "

if knowledges_7 == 1:
    print_knowledges_7 = "•"
elif knowledges_7 == 2:
    print_knowledges_7 = "••"
elif knowledges_7 == 3:
    print_knowledges_7 = "•••"
else:
    print_knowledges_7 = " "

if knowledges_8 == 1:
    print_knowledges_8 = "•"
elif knowledges_8 == 2:
    print_knowledges_8 = "••"
elif knowledges_8 == 3:
    print_knowledges_8 = "•••"
else:
    print_knowledges_8 = " "

if knowledges_9 == 1:
    print_knowledges_9 = "•"
elif knowledges_9 == 2:
    print_knowledges_9 = "••"
elif knowledges_9 == 3:
    print_knowledges_9 = "•••"
else:
    print_knowledges_9 = " "

if knowledges_10 == 1:
    print_knowledges_10 = "•"
elif knowledges_10 == 2:
    print_knowledges_10 = "••"
elif knowledges_10 == 3:
    print_knowledges_10 = "•••"
else:
    print_knowledges_10 = " "

if knowledges_11 == 1:
    print_knowledges_11 = "•"
elif knowledges_11 == 2:
    print_knowledges_11 = "••"
elif knowledges_11 == 3:
    print_knowledges_11 = "•••"
else:
    print_knowledges_11 = " "

if knowledges_12 == 1:
    print_knowledges_12 = "•"
elif knowledges_12 == 2:
    print_knowledges_12 = "••"
elif knowledges_12 == 3:
    print_knowledges_12 = "•••"
else:
    print_knowledges_12 = " "


# Принт бенефитов

if back_points_1 == 1:
    print_bpoints_1 = "•"
elif back_points_1 == 2:
    print_bpoints_1 = "••"
elif back_points_1 == 3:
    print_bpoints_1 = "•••"
elif back_points_1 == 4:
    print_bpoints_1 = "••••"
elif back_points_1 == 5:
    print_bpoints_1 = "•••••"
else:
    print_bpoints_1 = " "

if back_points_2 == 1:
    print_bpoints_2 = "•"
elif back_points_1 == 2:
    print_bpoints_2 = "••"
elif back_points_2 == 3:
    print_bpoints_2 = "•••"
elif back_points_2 == 4:
    print_bpoints_2 = "••••"
elif back_points_2 == 5:
    print_bpoints_2 = "•••••"
else:
    print_bpoints_2 = " "

if back_points_3 == 1:
    print_bpoints_3 = "•"
elif back_points_3 == 2:
    print_bpoints_3 = "••"
elif back_points_3 == 3:
    print_bpoints_3 = "•••"
elif back_points_3 == 4:
    print_bpoints_3 = "••••"
elif back_points_3 == 5:
    print_bpoints_3 = "•••••"
else:
    print_bpoints_3 = " "

if back_points_4 == 1:
    print_bpoints_4 = "•"
elif back_points_4 == 2:
    print_bpoints_4 = "••"
elif back_points_4 == 3:
    print_bpoints_4 = "•••"
elif back_points_4 == 4:
    print_bpoints_4 = "••••"
elif back_points_4 == 5:
    print_bpoints_4 = "•••••"
else:
    print_bpoints_4 = " "

if back_points_5 == 1:
    print_bpoints_5 = "•"
elif back_points_5 == 2:
    print_bpoints_5 = "••"
elif back_points_5 == 3:
    print_bpoints_5 = "•••"
elif back_points_5 == 4:
    print_bpoints_5 = "••••"
elif back_points_5 == 5:
    print_bpoints_5 = "•••••"
else:
    print_bpoints_5 = " "


# Добродетели ----------------------------------------

virtue_pool = 3
conscience = 0
conviction = 0
courage = 0


while virtue_pool > 0:
    #print(c_points)
    if virtue_pool == 0 :
        break
    div_point = random.randint(1,min(3,virtue_pool))
    virtue_pool = virtue_pool - div_point
    conscience = conscience + div_point
    if virtue_pool == 0 :
        break
    div_point = random.randint(1,min(3,virtue_pool))
    virtue_pool = virtue_pool - div_point
    conviction = conviction + div_point
    if virtue_pool == 0 :
        break
    div_point = random.randint(1,min(3,virtue_pool))
    virtue_pool = virtue_pool - div_point
    courage = courage + div_point


if conscience == 1:
    conscience_print = "•"
elif conscience == 2:
    conscience_print = "••"
elif conscience == 3:
    conscience_print = "•••"
else:
    conscience_print = " "

if conviction == 1:
    conviction_print = "•"
elif conviction == 2:
    conviction_print = "••"
elif conviction == 3:
    conviction_print = "•••"
else:
    conviction_print = " "

if courage == 1:
    courage_print = "•"
elif courage == 2:
    courage_print = "••"
elif courage == 3:
    courage_print = "•••"
else:
    courage_print = " "


# Принт веры ------------------------------------

if faith == 1:
    faith_print = "•"
elif faith == 2:
    faith_print = "•  •"
elif faith == 3:
    faith_print = "•  • •"
elif faith == 4:
    faith_print = "•  • •  •"
elif faith == 5:
    faith_print = "•  • •  •  •"
else:
    faith_print = " "