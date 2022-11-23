import database
import random
import names

name = names.get_full_name()

mask = random.choice(database.dchar)
character = random.choice(database.dchar)

host_life = random.choice(database.host_concepte)

if host_life == 'Артист':
    final_concepte = random.choices(database.host_concepte_artist)
elif host_life == 'Бродяга':
    final_concepte = random.choices(database.host_concepte_hobo)
elif host_life == 'Дитя':
    final_concepte = random.choices(database.host_concepte_child)
elif host_life == 'Интеллектуал':
    final_concepte = random.choices(database.host_concepte_intelegence)
elif host_life == 'Ночной заводила':
    final_concepte = random.choices(database.host_concepte_raver)
elif host_life == 'Политик':
    final_concepte = random.choices(database.host_concepte_politic)
elif host_life == 'Преступник':
    final_concepte = random.choices(database.host_concepte_crime)
elif host_life == 'Профессионал':
    final_concepte = random.choices(database.host_concepte_professional)
elif host_life == 'Рабочий':
    final_concepte = random.choices(database.host_concepte_worker)
elif host_life == 'Религиозный деятель':
    final_concepte = random.choices(database.host_concepte_missioner)
elif host_life == 'Репортер':
    final_concepte = random.choices(database.host_concepte_reporter)
elif host_life == 'Светский лев':
    final_concepte = random.choices(database.host_concepte_vip)
elif host_life == 'Солдат':
    final_concepte = random.choices(database.host_concepte_soldier)
elif host_life == 'Сыщик':
    final_concepte = random.choices(database.host_concepte_detective)
elif host_life == 'Чужак':
    final_concepte = random.choices(database.host_concepte_outlander)
else:
    print('No way, fuck!')

host_concepte = final_concepte[0]