import database
import dcreate
import host_life_base
import apoints_base


print(host_life_base.name)
print("Host's mask is: " + host_life_base.mask)
print('Concepte is: ', host_life_base.host_life, host_life_base.host_concepte)

if database.create_demon:
    print("Demon's character is: " + host_life_base.character)
    print("Demon's House is: ", dcreate.house_demon)
    print("Group is: ", dcreate.group_of_demon)
    print('Apocalyptic form is: ', dcreate.apocalyptic_form)
    print('Torment is: ', dcreate.torment)
    print('LORE POINTS - ', dcreate.lore_points_checked)

print("Abilities is:  ------------ ", apoints_base.first_one)
print("Abilities is:  ------------ ", apoints_base.first_two)
print("Abilities is:  ------------ ", apoints_base.first_three)


print("Talents is: ------------ ", apoints_base.second_one)
print("Skills is: ------------ ", apoints_base.second_two)
print("Knowledges is: ------------ ", apoints_base.second_three)

print('Faith: ------------ ', apoints_base.faith)


