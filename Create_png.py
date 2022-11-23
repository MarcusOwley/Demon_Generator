import database
import dcreate
import host_life_base
import apoints_base
from PIL import Image, ImageDraw, ImageFont

try:
   print_name = Image.open('charsheet_001.jpg')
except:
   print("Unable to load image")


# Шапка -----------------------------------------------------------------------------
idraw = ImageDraw.Draw(print_name)

name_host = host_life_base.name
host_lifestyle = host_life_base.host_life
host_concepte_print = host_life_base.host_concepte
mask_host = host_life_base.mask

font = ImageFont.truetype("arial.ttf", size = 14)
font1 = ImageFont.truetype("arial.ttf", size = 12)
font2 = ImageFont.truetype("arial.ttf", size = 24)
font3 = ImageFont.truetype("arial.ttf", size = 10)

idraw.text((100, 73), name_host, font=font)
idraw.text((347, 115), host_lifestyle, font=font1)
idraw.text((340, 130), host_concepte_print, font=font1)
idraw.text((315, 95), mask_host, font=font)


# Атрибуты -----------------------------------------------------------------------------

if apoints_base.priority_1[0] == 'Сила' or apoints_base.priority_1[1] == 'Выносливость' or apoints_base.priority_1[2] == 'Ловкость':
    idraw.text((212, 183), apoints_base.print_point_1, font=font2)
    idraw.text((212, 201), apoints_base.print_point_2, font=font2)
    idraw.text((212, 219), apoints_base.print_point_3, font=font2)
    print("--------->STR_1")
elif apoints_base.priority_1[0] == 'Обаяние' or apoints_base.priority_1[1] == 'Манипулирование' or apoints_base.priority_1[2] == 'Внешность':
    idraw.text((417, 183), apoints_base.print_point_1, font=font2)
    idraw.text((417, 201), apoints_base.print_point_2, font=font2)
    idraw.text((417, 219), apoints_base.print_point_3, font=font2)
    print("--------->CHAR_1")
else:
    idraw.text((623, 183), apoints_base.print_point_1, font=font2)
    idraw.text((623, 201), apoints_base.print_point_2, font=font2)
    idraw.text((623, 219), apoints_base.print_point_3, font=font2)
    print("--------->INT_1")

if apoints_base.priority_2[0] == 'Сила' or apoints_base.priority_2[1] == 'Выносливость' or apoints_base.priority_2[2] == 'Ловкость':
    idraw.text((212, 183), apoints_base.print_point_4, font=font2)
    idraw.text((212, 201), apoints_base.print_point_5, font=font2)
    idraw.text((212, 219), apoints_base.print_point_6, font=font2)
    print("--------->STR_2")
elif apoints_base.priority_2[0] == 'Обаяние' or apoints_base.priority_2[1] == 'Манипулирование' or apoints_base.priority_2[2] == 'Внешность':
    idraw.text((417, 183), apoints_base.print_point_4, font=font2)
    idraw.text((417, 201), apoints_base.print_point_5, font=font2)
    idraw.text((417, 219), apoints_base.print_point_6, font=font2)
    print("--------->CHAR_2")
else:
    idraw.text((623, 183), apoints_base.print_point_4, font=font2)
    idraw.text((623, 201), apoints_base.print_point_5, font=font2)
    idraw.text((623, 219), apoints_base.print_point_6, font=font2)
    print("--------->INT_2")

if apoints_base.priority_3[0] == 'Сила' or apoints_base.priority_3[1] == 'Выносливость' or apoints_base.priority_3[2] == 'Ловкость':
    idraw.text((212, 183), apoints_base.print_point_7, font=font2)
    idraw.text((212, 200), apoints_base.print_point_8, font=font2)
    idraw.text((212, 218), apoints_base.print_point_9, font=font2)
    print("--------->STR_3")
elif apoints_base.priority_3[0] == 'Обаяние' or apoints_base.priority_3[1] == 'Манипулирование' or apoints_base.priority_3[2] == 'Внешность':
    idraw.text((417, 183), apoints_base.print_point_7, font=font2)
    idraw.text((417, 200), apoints_base.print_point_8, font=font2)
    idraw.text((417, 218), apoints_base.print_point_9, font=font2)
    print("--------->CHAR_3")
else:
    idraw.text((623, 183), apoints_base.print_point_7, font=font2)
    idraw.text((623, 200), apoints_base.print_point_8, font=font2)
    idraw.text((623, 218), apoints_base.print_point_9, font=font2)
    print("--------->INT_3")


# Способности -----------------------------------------------------------------------------

# Таланты -----------------------------------------------------------------------------
if database.talents_abilities[0] == 'Бдительность':
    idraw.text((203, 301), apoints_base.print_talent_1, font=font2)
elif database.talents_abilities[0] == 'Атлетизм':
    idraw.text((203, 318), apoints_base.print_talent_1, font=font2)
elif database.talents_abilities[0] == 'Осведомленность':
    idraw.text((203, 335), apoints_base.print_talent_1, font=font2)
elif database.talents_abilities[0] == 'Рукапашный бой':
    idraw.text((203, 318), apoints_base.print_talent_1, font=font2)
elif database.talents_abilities[0] == 'Уворот':
    idraw.text((203, 318), apoints_base.print_talent_1, font=font2)
elif database.talents_abilities[0] == 'Эмпатия':
    idraw.text((203, 318), apoints_base.print_talent_1, font=font2)
elif database.talents_abilities[0] == 'Выразительность':
    idraw.text((203, 318), apoints_base.print_talent_1, font=font2)
elif database.talents_abilities[0] == 'Запугивание':
    idraw.text((203, 318), apoints_base.print_talent_1, font=font2)
elif database.talents_abilities[0] == 'Интуиция':
    idraw.text((203, 318), apoints_base.print_talent_1, font=font2)
elif database.talents_abilities[0] == 'Лидерство':
    idraw.text((203, 318), apoints_base.print_talent_1, font=font2)
elif database.talents_abilities[0] == 'Знание улиц':
    idraw.text((203, 318), apoints_base.print_talent_1, font=font2)
elif database.talents_abilities[0] == 'Хитрость':
    idraw.text((203, 318), apoints_base.print_talent_1, font=font2)
else:
    print("ERROR1")

if database.talents_abilities[1] == 'Бдительность':
    idraw.text((203, 301), apoints_base.print_talent_2, font=font2)
elif database.talents_abilities[1] == 'Атлетизм':
    idraw.text((203, 318), apoints_base.print_talent_2, font=font2)
elif database.talents_abilities[1] == 'Осведомленность':
    idraw.text((203, 335), apoints_base.print_talent_2, font=font2)
elif database.talents_abilities[1] == 'Рукапашный бой':
    idraw.text((203, 352), apoints_base.print_talent_2, font=font2)
elif database.talents_abilities[1] == 'Уворот':
    idraw.text((203, 369), apoints_base.print_talent_2, font=font2)
elif database.talents_abilities[1] == 'Эмпатия':
    idraw.text((203, 386), apoints_base.print_talent_2, font=font2)
elif database.talents_abilities[1] == 'Выразительность':
    idraw.text((203, 403), apoints_base.print_talent_2, font=font2)
elif database.talents_abilities[1] == 'Запугивание':
    idraw.text((203, 420), apoints_base.print_talent_2, font=font2)
elif database.talents_abilities[1] == 'Интуиция':
    idraw.text((203, 437), apoints_base.print_talent_2, font=font2)
elif database.talents_abilities[1] == 'Лидерство':
    idraw.text((203, 454), apoints_base.print_talent_2, font=font2)
elif database.talents_abilities[1] == 'Знание улиц':
    idraw.text((203, 471), apoints_base.print_talent_2, font=font2)
elif database.talents_abilities[1] == 'Хитрость':
    idraw.text((203, 488), apoints_base.print_talent_2, font=font2)
else:
    print("ERROR2")

if database.talents_abilities[2] == 'Бдительность':
    idraw.text((203, 301), apoints_base.print_talent_3, font=font2)
elif database.talents_abilities[2] == 'Атлетизм':
    idraw.text((203, 318), apoints_base.print_talent_3, font=font2)
elif database.talents_abilities[2] == 'Осведомленность':
    idraw.text((203, 335), apoints_base.print_talent_3, font=font2)
elif database.talents_abilities[2] == 'Рукапашный бой':
    idraw.text((203, 352), apoints_base.print_talent_3, font=font2)
elif database.talents_abilities[2] == 'Уворот':
    idraw.text((203, 369), apoints_base.print_talent_3, font=font2)
elif database.talents_abilities[2] == 'Эмпатия':
    idraw.text((203, 386), apoints_base.print_talent_3, font=font2)
elif database.talents_abilities[2] == 'Выразительность':
    idraw.text((203, 403), apoints_base.print_talent_3, font=font2)
elif database.talents_abilities[2] == 'Запугивание':
    idraw.text((203, 420), apoints_base.print_talent_3, font=font2)
elif database.talents_abilities[2] == 'Интуиция':
    idraw.text((203, 437), apoints_base.print_talent_3, font=font2)
elif database.talents_abilities[2] == 'Лидерство':
    idraw.text((203, 454), apoints_base.print_talent_3, font=font2)
elif database.talents_abilities[2] == 'Знание улиц':
    idraw.text((203, 471), apoints_base.print_talent_3, font=font2)
elif database.talents_abilities[2] == 'Хитрость':
    idraw.text((203, 488), apoints_base.print_talent_3, font=font2)
else:
    print("ERROR3")

if database.talents_abilities[3] == 'Бдительность':
    idraw.text((203, 301), apoints_base.print_talent_4, font=font2)
elif database.talents_abilities[3] == 'Атлетизм':
    idraw.text((203, 318), apoints_base.print_talent_4, font=font2)
elif database.talents_abilities[3] == 'Осведомленность':
    idraw.text((203, 335), apoints_base.print_talent_4, font=font2)
elif database.talents_abilities[3] == 'Рукапашный бой':
    idraw.text((203, 352), apoints_base.print_talent_4, font=font2)
elif database.talents_abilities[3] == 'Уворот':
    idraw.text((203, 369), apoints_base.print_talent_4, font=font2)
elif database.talents_abilities[3] == 'Эмпатия':
    idraw.text((203, 386), apoints_base.print_talent_4, font=font2)
elif database.talents_abilities[3] == 'Выразительность':
    idraw.text((203, 403), apoints_base.print_talent_4, font=font2)
elif database.talents_abilities[3] == 'Запугивание':
    idraw.text((203, 420), apoints_base.print_talent_4, font=font2)
elif database.talents_abilities[3] == 'Интуиция':
    idraw.text((203, 437), apoints_base.print_talent_4, font=font2)
elif database.talents_abilities[3] == 'Лидерство':
    idraw.text((203, 454), apoints_base.print_talent_4, font=font2)
elif database.talents_abilities[3] == 'Знание улиц':
    idraw.text((203, 471), apoints_base.print_talent_4, font=font2)
elif database.talents_abilities[3] == 'Хитрость':
    idraw.text((203, 488), apoints_base.print_talent_4, font=font2)
else:
    print("ERROR4")

if database.talents_abilities[4] == 'Бдительность':
    idraw.text((203, 301), apoints_base.print_talent_5, font=font2)
elif database.talents_abilities[4] == 'Атлетизм':
    idraw.text((203, 318), apoints_base.print_talent_5, font=font2)
elif database.talents_abilities[4] == 'Осведомленность':
    idraw.text((203, 335), apoints_base.print_talent_5, font=font2)
elif database.talents_abilities[4] == 'Рукапашный бой':
    idraw.text((203, 352), apoints_base.print_talent_5, font=font2)
elif database.talents_abilities[4] == 'Уворот':
    idraw.text((203, 369), apoints_base.print_talent_5, font=font2)
elif database.talents_abilities[4] == 'Эмпатия':
    idraw.text((203, 386), apoints_base.print_talent_5, font=font2)
elif database.talents_abilities[4] == 'Выразительность':
    idraw.text((203, 403), apoints_base.print_talent_5, font=font2)
elif database.talents_abilities[4] == 'Запугивание':
    idraw.text((203, 420), apoints_base.print_talent_5, font=font2)
elif database.talents_abilities[4] == 'Интуиция':
    idraw.text((203, 437), apoints_base.print_talent_5, font=font2)
elif database.talents_abilities[4] == 'Лидерство':
    idraw.text((203, 454), apoints_base.print_talent_5, font=font2)
elif database.talents_abilities[4] == 'Знание улиц':
    idraw.text((203, 471), apoints_base.print_talent_5, font=font2)
elif database.talents_abilities[4] == 'Хитрость':
    idraw.text((203, 488), apoints_base.print_talent_5, font=font2)
else:
    print("ERROR5")

if database.talents_abilities[5] == 'Бдительность':
    idraw.text((203, 301), apoints_base.print_talent_6, font=font2)
elif database.talents_abilities[5] == 'Атлетизм':
    idraw.text((203, 318), apoints_base.print_talent_6, font=font2)
elif database.talents_abilities[5] == 'Осведомленность':
    idraw.text((203, 335), apoints_base.print_talent_6, font=font2)
elif database.talents_abilities[5] == 'Рукапашный бой':
    idraw.text((203, 352), apoints_base.print_talent_6, font=font2)
elif database.talents_abilities[5] == 'Уворот':
    idraw.text((203, 369), apoints_base.print_talent_6, font=font2)
elif database.talents_abilities[5] == 'Эмпатия':
    idraw.text((203, 386), apoints_base.print_talent_6, font=font2)
elif database.talents_abilities[5] == 'Выразительность':
    idraw.text((203, 403), apoints_base.print_talent_6, font=font2)
elif database.talents_abilities[5] == 'Запугивание':
    idraw.text((203, 420), apoints_base.print_talent_6, font=font2)
elif database.talents_abilities[5] == 'Интуиция':
    idraw.text((203, 437), apoints_base.print_talent_6, font=font2)
elif database.talents_abilities[5] == 'Лидерство':
    idraw.text((203, 454), apoints_base.print_talent_6, font=font2)
elif database.talents_abilities[5] == 'Знание улиц':
    idraw.text((203, 471), apoints_base.print_talent_6, font=font2)
elif database.talents_abilities[5] == 'Хитрость':
    idraw.text((203, 488), apoints_base.print_talent_6, font=font2)
else:
    print("ERROR6")

if database.talents_abilities[6] == 'Бдительность':
    idraw.text((203, 301), apoints_base.print_talent_7, font=font2)
elif database.talents_abilities[6] == 'Атлетизм':
    idraw.text((203, 318), apoints_base.print_talent_7, font=font2)
elif database.talents_abilities[6] == 'Осведомленность':
    idraw.text((203, 335), apoints_base.print_talent_7, font=font2)
elif database.talents_abilities[6] == 'Рукапашный бой':
    idraw.text((203, 352), apoints_base.print_talent_7, font=font2)
elif database.talents_abilities[6] == 'Уворот':
    idraw.text((203, 369), apoints_base.print_talent_7, font=font2)
elif database.talents_abilities[6] == 'Эмпатия':
    idraw.text((203, 386), apoints_base.print_talent_7, font=font2)
elif database.talents_abilities[6] == 'Выразительность':
    idraw.text((203, 403), apoints_base.print_talent_7, font=font2)
elif database.talents_abilities[6] == 'Запугивание':
    idraw.text((203, 420), apoints_base.print_talent_7, font=font2)
elif database.talents_abilities[6] == 'Интуиция':
    idraw.text((203, 437), apoints_base.print_talent_7, font=font2)
elif database.talents_abilities[6] == 'Лидерство':
    idraw.text((203, 454), apoints_base.print_talent_7, font=font2)
elif database.talents_abilities[6] == 'Знание улиц':
    idraw.text((203, 471), apoints_base.print_talent_7, font=font2)
elif database.talents_abilities[6] == 'Хитрость':
    idraw.text((203, 488), apoints_base.print_talent_7, font=font2)
else:
    print("ERROR7")

if database.talents_abilities[7] == 'Бдительность':
    idraw.text((203, 301), apoints_base.print_talent_8, font=font2)
elif database.talents_abilities[7] == 'Атлетизм':
    idraw.text((203, 318), apoints_base.print_talent_8, font=font2)
elif database.talents_abilities[7] == 'Осведомленность':
    idraw.text((203, 335), apoints_base.print_talent_8, font=font2)
elif database.talents_abilities[7] == 'Рукапашный бой':
    idraw.text((203, 352), apoints_base.print_talent_8, font=font2)
elif database.talents_abilities[7] == 'Уворот':
    idraw.text((203, 369), apoints_base.print_talent_8, font=font2)
elif database.talents_abilities[7] == 'Эмпатия':
    idraw.text((203, 386), apoints_base.print_talent_8, font=font2)
elif database.talents_abilities[7] == 'Выразительность':
    idraw.text((203, 403), apoints_base.print_talent_8, font=font2)
elif database.talents_abilities[7] == 'Запугивание':
    idraw.text((203, 420), apoints_base.print_talent_8, font=font2)
elif database.talents_abilities[7] == 'Интуиция':
    idraw.text((203, 437), apoints_base.print_talent_8, font=font2)
elif database.talents_abilities[7] == 'Лидерство':
    idraw.text((203, 454), apoints_base.print_talent_8, font=font2)
elif database.talents_abilities[7] == 'Знание улиц':
    idraw.text((203, 471), apoints_base.print_talent_8, font=font2)
elif database.talents_abilities[7] == 'Хитрость':
    idraw.text((203, 488), apoints_base.print_talent_8, font=font2)
else:
    print("ERROR8")

if database.talents_abilities[8] == 'Бдительность':
    idraw.text((203, 301), apoints_base.print_talent_9, font=font2)
elif database.talents_abilities[8] == 'Атлетизм':
    idraw.text((203, 318), apoints_base.print_talent_9, font=font2)
elif database.talents_abilities[8] == 'Осведомленность':
    idraw.text((203, 335), apoints_base.print_talent_9, font=font2)
elif database.talents_abilities[8] == 'Рукапашный бой':
    idraw.text((203, 352), apoints_base.print_talent_9, font=font2)
elif database.talents_abilities[8] == 'Уворот':
    idraw.text((203, 369), apoints_base.print_talent_9, font=font2)
elif database.talents_abilities[8] == 'Эмпатия':
    idraw.text((203, 386), apoints_base.print_talent_9, font=font2)
elif database.talents_abilities[8] == 'Выразительность':
    idraw.text((203, 403), apoints_base.print_talent_9, font=font2)
elif database.talents_abilities[8] == 'Запугивание':
    idraw.text((203, 420), apoints_base.print_talent_9, font=font2)
elif database.talents_abilities[8] == 'Интуиция':
    idraw.text((203, 437), apoints_base.print_talent_9, font=font2)
elif database.talents_abilities[8] == 'Лидерство':
    idraw.text((203, 454), apoints_base.print_talent_9, font=font2)
elif database.talents_abilities[8] == 'Знание улиц':
    idraw.text((203, 471), apoints_base.print_talent_9, font=font2)
elif database.talents_abilities[8] == 'Хитрость':
    idraw.text((203, 488), apoints_base.print_talent_9, font=font2)
else:
    print("ERROR9")

if database.talents_abilities[9] == 'Бдительность':
    idraw.text((203, 301), apoints_base.print_talent_10, font=font2)
elif database.talents_abilities[9] == 'Атлетизм':
    idraw.text((203, 318), apoints_base.print_talent_10, font=font2)
elif database.talents_abilities[9] == 'Осведомленность':
    idraw.text((203, 335), apoints_base.print_talent_10, font=font2)
elif database.talents_abilities[9] == 'Рукапашный бой':
    idraw.text((203, 352), apoints_base.print_talent_10, font=font2)
elif database.talents_abilities[9] == 'Уворот':
    idraw.text((203, 369), apoints_base.print_talent_10, font=font2)
elif database.talents_abilities[9] == 'Эмпатия':
    idraw.text((203, 386), apoints_base.print_talent_10, font=font2)
elif database.talents_abilities[9] == 'Выразительность':
    idraw.text((203, 403), apoints_base.print_talent_10, font=font2)
elif database.talents_abilities[9] == 'Запугивание':
    idraw.text((203, 420), apoints_base.print_talent_10, font=font2)
elif database.talents_abilities[9] == 'Интуиция':
    idraw.text((203, 437), apoints_base.print_talent_10, font=font2)
elif database.talents_abilities[9] == 'Лидерство':
    idraw.text((203, 454), apoints_base.print_talent_10, font=font2)
elif database.talents_abilities[9] == 'Знание улиц':
    idraw.text((203, 471), apoints_base.print_talent_10, font=font2)
elif database.talents_abilities[9] == 'Хитрость':
    idraw.text((203, 488), apoints_base.print_talent_10, font=font2)
else:
    print("ERROR10")

if database.talents_abilities[10] == 'Бдительность':
    idraw.text((203, 301), apoints_base.print_talent_11, font=font2)
elif database.talents_abilities[10] == 'Атлетизм':
    idraw.text((203, 318), apoints_base.print_talent_11, font=font2)
elif database.talents_abilities[10] == 'Осведомленность':
    idraw.text((203, 335), apoints_base.print_talent_11, font=font2)
elif database.talents_abilities[10] == 'Рукапашный бой':
    idraw.text((203, 352), apoints_base.print_talent_11, font=font2)
elif database.talents_abilities[10] == 'Уворот':
    idraw.text((203, 369), apoints_base.print_talent_11, font=font2)
elif database.talents_abilities[10] == 'Эмпатия':
    idraw.text((203, 386), apoints_base.print_talent_11, font=font2)
elif database.talents_abilities[10] == 'Выразительность':
    idraw.text((203, 403), apoints_base.print_talent_11, font=font2)
elif database.talents_abilities[10] == 'Запугивание':
    idraw.text((203, 420), apoints_base.print_talent_11, font=font2)
elif database.talents_abilities[10] == 'Интуиция':
    idraw.text((203, 437), apoints_base.print_talent_11, font=font2)
elif database.talents_abilities[10] == 'Лидерство':
    idraw.text((203, 454), apoints_base.print_talent_11, font=font2)
elif database.talents_abilities[10] == 'Знание улиц':
    idraw.text((203, 471), apoints_base.print_talent_11, font=font2)
elif database.talents_abilities[10] == 'Хитрость':
    idraw.text((203, 488), apoints_base.print_talent_11, font=font2)
else:
    print("ERROR11")

if database.talents_abilities[11] == 'Бдительность':
    idraw.text((203, 301), apoints_base.print_talent_12, font=font2)
elif database.talents_abilities[11] == 'Атлетизм':
    idraw.text((203, 318), apoints_base.print_talent_12, font=font2)
elif database.talents_abilities[11] == 'Осведомленность':
    idraw.text((203, 335), apoints_base.print_talent_12, font=font2)
elif database.talents_abilities[11] == 'Рукапашный бой':
    idraw.text((203, 352), apoints_base.print_talent_12, font=font2)
elif database.talents_abilities[11] == 'Уворот':
    idraw.text((203, 369), apoints_base.print_talent_12, font=font2)
elif database.talents_abilities[11] == 'Эмпатия':
    idraw.text((203, 386), apoints_base.print_talent_12, font=font2)
elif database.talents_abilities[11] == 'Выразительность':
    idraw.text((203, 403), apoints_base.print_talent_12, font=font2)
elif database.talents_abilities[11] == 'Запугивание':
    idraw.text((203, 420), apoints_base.print_talent_12, font=font2)
elif database.talents_abilities[11] == 'Интуиция':
    idraw.text((203, 437), apoints_base.print_talent_12, font=font2)
elif database.talents_abilities[11] == 'Лидерство':
    idraw.text((203, 454), apoints_base.print_talent_12, font=font2)
elif database.talents_abilities[11] == 'Знание улиц':
    idraw.text((203, 471), apoints_base.print_talent_12, font=font2)
elif database.talents_abilities[11] == 'Хитрость':
    idraw.text((203, 488), apoints_base.print_talent_12, font=font2)
else:
    print("ERROR12")

# Навыки -----------------------------------------------------------------------------

if database.skills_abilities[0] == 'Знание животных':
    idraw.text((409, 301), apoints_base.print_skills_1, font=font2)
elif database.skills_abilities[0] == 'Ремесло':
    idraw.text((409, 318), apoints_base.print_skills_1, font=font2)
elif database.skills_abilities[0] == 'Взрывное дело':
    idraw.text((409, 335), apoints_base.print_skills_1, font=font2)
elif database.skills_abilities[0] == 'Вождение':
    idraw.text((409, 352), apoints_base.print_skills_1, font=font2)
elif database.skills_abilities[0] == 'Этикет':
    idraw.text((409, 369), apoints_base.print_skills_1, font=font2)
elif database.skills_abilities[0] == 'Огнестрельное оружие':
    idraw.text((409, 386), apoints_base.print_skills_1, font=font2)
elif database.skills_abilities[0] == 'Фехтование':
    idraw.text((409, 403), apoints_base.print_skills_1, font=font2)
elif database.skills_abilities[0] == 'Актерство':
    idraw.text((409, 420), apoints_base.print_skills_1, font=font2)
elif database.skills_abilities[0] == 'Безопасность':
    idraw.text((409, 437), apoints_base.print_skills_1, font=font2)
elif database.skills_abilities[0] == 'Маскировка':
    idraw.text((409, 454), apoints_base.print_skills_1, font=font2)
elif database.skills_abilities[0] == 'Выживание':
    idraw.text((409, 471), apoints_base.print_skills_1, font=font2)
elif database.skills_abilities[0] == 'Технология':
    idraw.text((409, 488), apoints_base.print_skills_1, font=font2)
else:
    print("1ERROR")

if database.skills_abilities[1] == 'Знание животных':
    idraw.text((409, 301), apoints_base.print_skills_2, font=font2)
elif database.skills_abilities[1] == 'Ремесло':
    idraw.text((409, 318), apoints_base.print_skills_2, font=font2)
elif database.skills_abilities[1] == 'Взрывное дело':
    idraw.text((409, 335), apoints_base.print_skills_2, font=font2)
elif database.skills_abilities[1] == 'Вождение':
    idraw.text((409, 352), apoints_base.print_skills_2, font=font2)
elif database.skills_abilities[1] == 'Этикет':
    idraw.text((409, 369), apoints_base.print_skills_2, font=font2)
elif database.skills_abilities[1] == 'Огнестрельное оружие':
    idraw.text((409, 386), apoints_base.print_skills_2, font=font2)
elif database.skills_abilities[1] == 'Фехтование':
    idraw.text((409, 403), apoints_base.print_skills_2, font=font2)
elif database.skills_abilities[1] == 'Актерство':
    idraw.text((409, 420), apoints_base.print_skills_2, font=font2)
elif database.skills_abilities[1] == 'Безопасность':
    idraw.text((409, 437), apoints_base.print_skills_2, font=font2)
elif database.skills_abilities[1] == 'Маскировка':
    idraw.text((409, 454), apoints_base.print_skills_2, font=font2)
elif database.skills_abilities[1] == 'Выживание':
    idraw.text((409, 471), apoints_base.print_skills_2, font=font2)
elif database.skills_abilities[1] == 'Технология':
    idraw.text((409, 488), apoints_base.print_skills_2, font=font2)
else:
    print("2ERROR")

if database.skills_abilities[2] == 'Знание животных':
    idraw.text((409, 301), apoints_base.print_skills_3, font=font2)
elif database.skills_abilities[2] == 'Ремесло':
    idraw.text((409, 318), apoints_base.print_skills_3, font=font2)
elif database.skills_abilities[2] == 'Взрывное дело':
    idraw.text((409, 335), apoints_base.print_skills_3, font=font2)
elif database.skills_abilities[2] == 'Вождение':
    idraw.text((409, 352), apoints_base.print_skills_3, font=font2)
elif database.skills_abilities[2] == 'Этикет':
    idraw.text((409, 369), apoints_base.print_skills_3, font=font2)
elif database.skills_abilities[2] == 'Огнестрельное оружие':
    idraw.text((409, 386), apoints_base.print_skills_3, font=font2)
elif database.skills_abilities[2] == 'Фехтование':
    idraw.text((409, 403), apoints_base.print_skills_3, font=font2)
elif database.skills_abilities[2] == 'Актерство':
    idraw.text((409, 420), apoints_base.print_skills_3, font=font2)
elif database.skills_abilities[2] == 'Безопасность':
    idraw.text((409, 437), apoints_base.print_skills_3, font=font2)
elif database.skills_abilities[2] == 'Маскировка':
    idraw.text((409, 454), apoints_base.print_skills_3, font=font2)
elif database.skills_abilities[2] == 'Выживание':
    idraw.text((409, 471), apoints_base.print_skills_3, font=font2)
elif database.skills_abilities[2] == 'Технология':
    idraw.text((409, 488), apoints_base.print_skills_3, font=font2)
else:
    print("3ERROR")

if database.skills_abilities[3] == 'Знание животных':
    idraw.text((409, 301), apoints_base.print_skills_4, font=font2)
elif database.skills_abilities[3] == 'Ремесло':
    idraw.text((409, 318), apoints_base.print_skills_4, font=font2)
elif database.skills_abilities[3] == 'Взрывное дело':
    idraw.text((409, 335), apoints_base.print_skills_4, font=font2)
elif database.skills_abilities[3] == 'Вождение':
    idraw.text((409, 352), apoints_base.print_skills_4, font=font2)
elif database.skills_abilities[3] == 'Этикет':
    idraw.text((409, 369), apoints_base.print_skills_4, font=font2)
elif database.skills_abilities[3] == 'Огнестрельное оружие':
    idraw.text((409, 386), apoints_base.print_skills_4, font=font2)
elif database.skills_abilities[3] == 'Фехтование':
    idraw.text((409, 403), apoints_base.print_skills_4, font=font2)
elif database.skills_abilities[3] == 'Актерство':
    idraw.text((409, 420), apoints_base.print_skills_4, font=font2)
elif database.skills_abilities[3] == 'Безопасность':
    idraw.text((409, 437), apoints_base.print_skills_4, font=font2)
elif database.skills_abilities[3] == 'Маскировка':
    idraw.text((409, 454), apoints_base.print_skills_4, font=font2)
elif database.skills_abilities[3] == 'Выживание':
    idraw.text((409, 471), apoints_base.print_skills_4, font=font2)
elif database.skills_abilities[3] == 'Технология':
    idraw.text((409, 488), apoints_base.print_skills_4, font=font2)
else:
    print("4ERROR")

if database.skills_abilities[4] == 'Знание животных':
    idraw.text((409, 301), apoints_base.print_skills_5, font=font2)
elif database.skills_abilities[4] == 'Ремесло':
    idraw.text((409, 318), apoints_base.print_skills_5, font=font2)
elif database.skills_abilities[4] == 'Взрывное дело':
    idraw.text((409, 335), apoints_base.print_skills_5, font=font2)
elif database.skills_abilities[4] == 'Вождение':
    idraw.text((409, 352), apoints_base.print_skills_5, font=font2)
elif database.skills_abilities[4] == 'Этикет':
    idraw.text((409, 369), apoints_base.print_skills_5, font=font2)
elif database.skills_abilities[4] == 'Огнестрельное оружие':
    idraw.text((409, 386), apoints_base.print_skills_5, font=font2)
elif database.skills_abilities[4] == 'Фехтование':
    idraw.text((409, 403), apoints_base.print_skills_5, font=font2)
elif database.skills_abilities[4] == 'Актерство':
    idraw.text((409, 420), apoints_base.print_skills_5, font=font2)
elif database.skills_abilities[4] == 'Безопасность':
    idraw.text((409, 437), apoints_base.print_skills_5, font=font2)
elif database.skills_abilities[4] == 'Маскировка':
    idraw.text((409, 454), apoints_base.print_skills_5, font=font2)
elif database.skills_abilities[4] == 'Выживание':
    idraw.text((409, 471), apoints_base.print_skills_5, font=font2)
elif database.skills_abilities[4] == 'Технология':
    idraw.text((409, 488), apoints_base.print_skills_5, font=font2)
else:
    print("5ERROR")

if database.skills_abilities[5] == 'Знание животных':
    idraw.text((409, 301), apoints_base.print_skills_6, font=font2)
elif database.skills_abilities[5] == 'Ремесло':
    idraw.text((409, 318), apoints_base.print_skills_6, font=font2)
elif database.skills_abilities[5] == 'Взрывное дело':
    idraw.text((409, 335), apoints_base.print_skills_6, font=font2)
elif database.skills_abilities[5] == 'Вождение':
    idraw.text((409, 352), apoints_base.print_skills_6, font=font2)
elif database.skills_abilities[5] == 'Этикет':
    idraw.text((409, 369), apoints_base.print_skills_6, font=font2)
elif database.skills_abilities[5] == 'Огнестрельное оружие':
    idraw.text((409, 386), apoints_base.print_skills_6, font=font2)
elif database.skills_abilities[5] == 'Фехтование':
    idraw.text((409, 403), apoints_base.print_skills_6, font=font2)
elif database.skills_abilities[5] == 'Актерство':
    idraw.text((409, 420), apoints_base.print_skills_6, font=font2)
elif database.skills_abilities[5] == 'Безопасность':
    idraw.text((409, 437), apoints_base.print_skills_6, font=font2)
elif database.skills_abilities[5] == 'Маскировка':
    idraw.text((409, 454), apoints_base.print_skills_6, font=font2)
elif database.skills_abilities[5] == 'Выживание':
    idraw.text((409, 471), apoints_base.print_skills_6, font=font2)
elif database.skills_abilities[5] == 'Технология':
    idraw.text((409, 488), apoints_base.print_skills_6, font=font2)
else:
    print("1ERROR")

if database.skills_abilities[6] == 'Знание животных':
    idraw.text((409, 301), apoints_base.print_skills_7, font=font2)
elif database.skills_abilities[6] == 'Ремесло':
    idraw.text((409, 318), apoints_base.print_skills_7, font=font2)
elif database.skills_abilities[6] == 'Взрывное дело':
    idraw.text((409, 335), apoints_base.print_skills_7, font=font2)
elif database.skills_abilities[6] == 'Вождение':
    idraw.text((409, 352), apoints_base.print_skills_7, font=font2)
elif database.skills_abilities[6] == 'Этикет':
    idraw.text((409, 369), apoints_base.print_skills_7, font=font2)
elif database.skills_abilities[6] == 'Огнестрельное оружие':
    idraw.text((409, 386), apoints_base.print_skills_7, font=font2)
elif database.skills_abilities[6] == 'Фехтование':
    idraw.text((409, 403), apoints_base.print_skills_7, font=font2)
elif database.skills_abilities[6] == 'Актерство':
    idraw.text((409, 420), apoints_base.print_skills_7, font=font2)
elif database.skills_abilities[6] == 'Безопасность':
    idraw.text((409, 437), apoints_base.print_skills_7, font=font2)
elif database.skills_abilities[6] == 'Маскировка':
    idraw.text((409, 454), apoints_base.print_skills_7, font=font2)
elif database.skills_abilities[6] == 'Выживание':
    idraw.text((409, 471), apoints_base.print_skills_7, font=font2)
elif database.skills_abilities[6] == 'Технология':
    idraw.text((409, 488), apoints_base.print_skills_7, font=font2)
else:
    print("7ERROR")

if database.skills_abilities[7] == 'Знание животных':
    idraw.text((409, 301), apoints_base.print_skills_8, font=font2)
elif database.skills_abilities[7] == 'Ремесло':
    idraw.text((409, 318), apoints_base.print_skills_8, font=font2)
elif database.skills_abilities[7] == 'Взрывное дело':
    idraw.text((409, 335), apoints_base.print_skills_8, font=font2)
elif database.skills_abilities[7] == 'Вождение':
    idraw.text((409, 352), apoints_base.print_skills_8, font=font2)
elif database.skills_abilities[7] == 'Этикет':
    idraw.text((409, 369), apoints_base.print_skills_8, font=font2)
elif database.skills_abilities[7] == 'Огнестрельное оружие':
    idraw.text((409, 386), apoints_base.print_skills_8, font=font2)
elif database.skills_abilities[7] == 'Фехтование':
    idraw.text((409, 403), apoints_base.print_skills_8, font=font2)
elif database.skills_abilities[7] == 'Актерство':
    idraw.text((409, 420), apoints_base.print_skills_8, font=font2)
elif database.skills_abilities[7] == 'Безопасность':
    idraw.text((409, 437), apoints_base.print_skills_8, font=font2)
elif database.skills_abilities[7] == 'Маскировка':
    idraw.text((409, 454), apoints_base.print_skills_8, font=font2)
elif database.skills_abilities[7] == 'Выживание':
    idraw.text((409, 471), apoints_base.print_skills_8, font=font2)
elif database.skills_abilities[7] == 'Технология':
    idraw.text((409, 488), apoints_base.print_skills_8, font=font2)
else:
    print("8ERROR")

if database.skills_abilities[8] == 'Знание животных':
    idraw.text((409, 301), apoints_base.print_skills_9, font=font2)
elif database.skills_abilities[8] == 'Ремесло':
    idraw.text((409, 318), apoints_base.print_skills_9, font=font2)
elif database.skills_abilities[8] == 'Взрывное дело':
    idraw.text((409, 335), apoints_base.print_skills_9, font=font2)
elif database.skills_abilities[8] == 'Вождение':
    idraw.text((409, 352), apoints_base.print_skills_9, font=font2)
elif database.skills_abilities[8] == 'Этикет':
    idraw.text((409, 369), apoints_base.print_skills_9, font=font2)
elif database.skills_abilities[8] == 'Огнестрельное оружие':
    idraw.text((409, 386), apoints_base.print_skills_9, font=font2)
elif database.skills_abilities[8] == 'Фехтование':
    idraw.text((409, 403), apoints_base.print_skills_9, font=font2)
elif database.skills_abilities[8] == 'Актерство':
    idraw.text((409, 420), apoints_base.print_skills_9, font=font2)
elif database.skills_abilities[8] == 'Безопасность':
    idraw.text((409, 437), apoints_base.print_skills_9, font=font2)
elif database.skills_abilities[8] == 'Маскировка':
    idraw.text((409, 454), apoints_base.print_skills_9, font=font2)
elif database.skills_abilities[8] == 'Выживание':
    idraw.text((409, 471), apoints_base.print_skills_9, font=font2)
elif database.skills_abilities[8] == 'Технология':
    idraw.text((409, 488), apoints_base.print_skills_9, font=font2)
else:
    print("9ERROR")

if database.skills_abilities[9] == 'Знание животных':
    idraw.text((409, 301), apoints_base.print_skills_10, font=font2)
elif database.skills_abilities[9] == 'Ремесло':
    idraw.text((409, 318), apoints_base.print_skills_10, font=font2)
elif database.skills_abilities[9] == 'Взрывное дело':
    idraw.text((409, 335), apoints_base.print_skills_10, font=font2)
elif database.skills_abilities[9] == 'Вождение':
    idraw.text((409, 352), apoints_base.print_skills_10, font=font2)
elif database.skills_abilities[9] == 'Этикет':
    idraw.text((409, 369), apoints_base.print_skills_10, font=font2)
elif database.skills_abilities[9] == 'Огнестрельное оружие':
    idraw.text((409, 386), apoints_base.print_skills_10, font=font2)
elif database.skills_abilities[9] == 'Фехтование':
    idraw.text((409, 403), apoints_base.print_skills_10, font=font2)
elif database.skills_abilities[9] == 'Актерство':
    idraw.text((409, 420), apoints_base.print_skills_10, font=font2)
elif database.skills_abilities[9] == 'Безопасность':
    idraw.text((409, 437), apoints_base.print_skills_10, font=font2)
elif database.skills_abilities[9] == 'Маскировка':
    idraw.text((409, 454), apoints_base.print_skills_10, font=font2)
elif database.skills_abilities[9] == 'Выживание':
    idraw.text((409, 471), apoints_base.print_skills_10, font=font2)
elif database.skills_abilities[9] == 'Технология':
    idraw.text((409, 488), apoints_base.print_skills_10, font=font2)
else:
    print("1ERROR")

if database.skills_abilities[10] == 'Знание животных':
    idraw.text((409, 301), apoints_base.print_skills_11, font=font2)
elif database.skills_abilities[10] == 'Ремесло':
    idraw.text((409, 318), apoints_base.print_skills_11, font=font2)
elif database.skills_abilities[10] == 'Взрывное дело':
    idraw.text((409, 335), apoints_base.print_skills_11, font=font2)
elif database.skills_abilities[10] == 'Вождение':
    idraw.text((409, 352), apoints_base.print_skills_11, font=font2)
elif database.skills_abilities[10] == 'Этикет':
    idraw.text((409, 369), apoints_base.print_skills_11, font=font2)
elif database.skills_abilities[10] == 'Огнестрельное оружие':
    idraw.text((409, 386), apoints_base.print_skills_11, font=font2)
elif database.skills_abilities[10] == 'Фехтование':
    idraw.text((409, 403), apoints_base.print_skills_10, font=font2)
elif database.skills_abilities[10] == 'Актерство':
    idraw.text((409, 420), apoints_base.print_skills_11, font=font2)
elif database.skills_abilities[10] == 'Безопасность':
    idraw.text((409, 437), apoints_base.print_skills_11, font=font2)
elif database.skills_abilities[10] == 'Маскировка':
    idraw.text((409, 454), apoints_base.print_skills_11, font=font2)
elif database.skills_abilities[10] == 'Выживание':
    idraw.text((409, 471), apoints_base.print_skills_11, font=font2)
elif database.skills_abilities[10] == 'Технология':
    idraw.text((409, 488), apoints_base.print_skills_11, font=font2)
else:
    print("10ERROR")

if database.skills_abilities[11] == 'Знание животных':
    idraw.text((409, 301), apoints_base.print_skills_12, font=font2)
elif database.skills_abilities[11] == 'Ремесло':
    idraw.text((409, 318), apoints_base.print_skills_12, font=font2)
elif database.skills_abilities[11] == 'Взрывное дело':
    idraw.text((409, 335), apoints_base.print_skills_12, font=font2)
elif database.skills_abilities[11] == 'Вождение':
    idraw.text((409, 352), apoints_base.print_skills_12, font=font2)
elif database.skills_abilities[11] == 'Этикет':
    idraw.text((409, 369), apoints_base.print_skills_12, font=font2)
elif database.skills_abilities[11] == 'Огнестрельное оружие':
    idraw.text((409, 386), apoints_base.print_skills_12, font=font2)
elif database.skills_abilities[11] == 'Фехтование':
    idraw.text((409, 403), apoints_base.print_skills_12, font=font2)
elif database.skills_abilities[11] == 'Актерство':
    idraw.text((409, 420), apoints_base.print_skills_12, font=font2)
elif database.skills_abilities[11] == 'Безопасность':
    idraw.text((409, 437), apoints_base.print_skills_12, font=font2)
elif database.skills_abilities[11] == 'Маскировка':
    idraw.text((409, 454), apoints_base.print_skills_12, font=font2)
elif database.skills_abilities[11] == 'Выживание':
    idraw.text((409, 471), apoints_base.print_skills_12, font=font2)
elif database.skills_abilities[11] == 'Технология':
    idraw.text((409, 488), apoints_base.print_skills_12, font=font2)
else:
    print("12ERROR")

# Познания -----------------------------------------------------------------------------

if database.knowledges_abilities[0] == 'Академические знания':
    idraw.text((615, 301), apoints_base.print_knowledges_1, font=font2)
elif database.knowledges_abilities[0] == 'Знания компьютера':
    idraw.text((615, 318), apoints_base.print_knowledges_1, font=font2)
elif database.knowledges_abilities[0] == 'Финансы':
    idraw.text((615, 335), apoints_base.print_knowledges_1, font=font2)
elif database.knowledges_abilities[0] == 'Расследование':
    idraw.text((615, 352), apoints_base.print_knowledges_1, font=font2)
elif database.knowledges_abilities[0] == 'Правоведение':
    idraw.text((615, 369), apoints_base.print_knowledges_1, font=font2)
elif database.knowledges_abilities[0] == 'Лингвистика':
    idraw.text((615, 386), apoints_base.print_knowledges_1, font=font2)
elif database.knowledges_abilities[0] == 'Медицина':
    idraw.text((615, 403), apoints_base.print_knowledges_1, font=font2)
elif database.knowledges_abilities[0] == 'Оккультизм':
    idraw.text((615, 420), apoints_base.print_knowledges_1, font=font2)
elif database.knowledges_abilities[0] == 'Политика':
    idraw.text((615, 437), apoints_base.print_knowledges_1, font=font2)
elif database.knowledges_abilities[0] == 'Религия':
    idraw.text((615, 454), apoints_base.print_knowledges_1, font=font2)
elif database.knowledges_abilities[0] == 'Исследование':
    idraw.text((615, 471), apoints_base.print_knowledges_1, font=font2)
elif database.knowledges_abilities[0] == 'Наука':
    idraw.text((615, 488), apoints_base.print_knowledges_1, font=font2)
else:
    print("ERR111")

if database.knowledges_abilities[1] == 'Академические знания':
    idraw.text((615, 301), apoints_base.print_knowledges_2, font=font2)
elif database.knowledges_abilities[1] == 'Знания компьютера':
    idraw.text((615, 318), apoints_base.print_knowledges_2, font=font2)
elif database.knowledges_abilities[1] == 'Финансы':
    idraw.text((615, 335), apoints_base.print_knowledges_2, font=font2)
elif database.knowledges_abilities[1] == 'Расследование':
    idraw.text((615, 352), apoints_base.print_knowledges_2, font=font2)
elif database.knowledges_abilities[1] == 'Правоведение':
    idraw.text((615, 369), apoints_base.print_knowledges_2, font=font2)
elif database.knowledges_abilities[1] == 'Лингвистика':
    idraw.text((615, 386), apoints_base.print_knowledges_2, font=font2)
elif database.knowledges_abilities[1] == 'Медицина':
    idraw.text((615, 403), apoints_base.print_knowledges_2, font=font2)
elif database.knowledges_abilities[1] == 'Оккультизм':
    idraw.text((615, 420), apoints_base.print_knowledges_2, font=font2)
elif database.knowledges_abilities[1] == 'Политика':
    idraw.text((615, 437), apoints_base.print_knowledges_2, font=font2)
elif database.knowledges_abilities[1] == 'Религия':
    idraw.text((615, 454), apoints_base.print_knowledges_2, font=font2)
elif database.knowledges_abilities[1] == 'Исследование':
    idraw.text((615, 471), apoints_base.print_knowledges_2, font=font2)
elif database.knowledges_abilities[1] == 'Наука':
    idraw.text((615, 488), apoints_base.print_knowledges_2, font=font2)
else:
    print("ERR222")

if database.knowledges_abilities[2] == 'Академические знания':
    idraw.text((615, 301), apoints_base.print_knowledges_3, font=font2)
elif database.knowledges_abilities[2] == 'Знания компьютера':
    idraw.text((615, 318), apoints_base.print_knowledges_3, font=font2)
elif database.knowledges_abilities[2] == 'Финансы':
    idraw.text((615, 335), apoints_base.print_knowledges_3, font=font2)
elif database.knowledges_abilities[2] == 'Расследование':
    idraw.text((615, 352), apoints_base.print_knowledges_3, font=font2)
elif database.knowledges_abilities[2] == 'Правоведение':
    idraw.text((615, 369), apoints_base.print_knowledges_3, font=font2)
elif database.knowledges_abilities[2] == 'Лингвистика':
    idraw.text((615, 386), apoints_base.print_knowledges_3, font=font2)
elif database.knowledges_abilities[2] == 'Медицина':
    idraw.text((615, 403), apoints_base.print_knowledges_3, font=font2)
elif database.knowledges_abilities[2] == 'Оккультизм':
    idraw.text((615, 420), apoints_base.print_knowledges_3, font=font2)
elif database.knowledges_abilities[2] == 'Политика':
    idraw.text((615, 437), apoints_base.print_knowledges_3, font=font2)
elif database.knowledges_abilities[2] == 'Религия':
    idraw.text((615, 454), apoints_base.print_knowledges_3, font=font2)
elif database.knowledges_abilities[2] == 'Исследование':
    idraw.text((615, 471), apoints_base.print_knowledges_3, font=font2)
elif database.knowledges_abilities[2] == 'Наука':
    idraw.text((615, 488), apoints_base.print_knowledges_3, font=font2)
else:
    print("ERR333")

if database.knowledges_abilities[3] == 'Академические знания':
    idraw.text((615, 301), apoints_base.print_knowledges_4, font=font2)
elif database.knowledges_abilities[3] == 'Знания компьютера':
    idraw.text((615, 318), apoints_base.print_knowledges_4, font=font2)
elif database.knowledges_abilities[3] == 'Финансы':
    idraw.text((615, 335), apoints_base.print_knowledges_4, font=font2)
elif database.knowledges_abilities[3] == 'Расследование':
    idraw.text((615, 352), apoints_base.print_knowledges_4, font=font2)
elif database.knowledges_abilities[3] == 'Правоведение':
    idraw.text((615, 369), apoints_base.print_knowledges_4, font=font2)
elif database.knowledges_abilities[3] == 'Лингвистика':
    idraw.text((615, 386), apoints_base.print_knowledges_4, font=font2)
elif database.knowledges_abilities[3] == 'Медицина':
    idraw.text((615, 403), apoints_base.print_knowledges_4, font=font2)
elif database.knowledges_abilities[3] == 'Оккультизм':
    idraw.text((615, 420), apoints_base.print_knowledges_4, font=font2)
elif database.knowledges_abilities[3] == 'Политика':
    idraw.text((615, 437), apoints_base.print_knowledges_4, font=font2)
elif database.knowledges_abilities[3] == 'Религия':
    idraw.text((615, 454), apoints_base.print_knowledges_4, font=font2)
elif database.knowledges_abilities[3] == 'Исследование':
    idraw.text((615, 471), apoints_base.print_knowledges_4, font=font2)
elif database.knowledges_abilities[3] == 'Наука':
    idraw.text((615, 488), apoints_base.print_knowledges_4, font=font2)
else:
    print("ERR444")

if database.knowledges_abilities[4] == 'Академические знания':
    idraw.text((615, 301), apoints_base.print_knowledges_5, font=font2)
elif database.knowledges_abilities[4] == 'Знания компьютера':
    idraw.text((615, 318), apoints_base.print_knowledges_5, font=font2)
elif database.knowledges_abilities[4] == 'Финансы':
    idraw.text((615, 335), apoints_base.print_knowledges_5, font=font2)
elif database.knowledges_abilities[4] == 'Расследование':
    idraw.text((615, 352), apoints_base.print_knowledges_5, font=font2)
elif database.knowledges_abilities[4] == 'Правоведение':
    idraw.text((615, 369), apoints_base.print_knowledges_5, font=font2)
elif database.knowledges_abilities[4] == 'Лингвистика':
    idraw.text((615, 386), apoints_base.print_knowledges_5, font=font2)
elif database.knowledges_abilities[4] == 'Медицина':
    idraw.text((615, 403), apoints_base.print_knowledges_5, font=font2)
elif database.knowledges_abilities[4] == 'Оккультизм':
    idraw.text((615, 420), apoints_base.print_knowledges_5, font=font2)
elif database.knowledges_abilities[4] == 'Политика':
    idraw.text((615, 437), apoints_base.print_knowledges_5, font=font2)
elif database.knowledges_abilities[4] == 'Религия':
    idraw.text((615, 454), apoints_base.print_knowledges_5, font=font2)
elif database.knowledges_abilities[4] == 'Исследование':
    idraw.text((615, 471), apoints_base.print_knowledges_5, font=font2)
elif database.knowledges_abilities[4] == 'Наука':
    idraw.text((615, 488), apoints_base.print_knowledges_5, font=font2)
else:
    print("ERR555")

if database.knowledges_abilities[5] == 'Академические знания':
    idraw.text((615, 301), apoints_base.print_knowledges_6, font=font2)
elif database.knowledges_abilities[5] == 'Знания компьютера':
    idraw.text((615, 318), apoints_base.print_knowledges_6, font=font2)
elif database.knowledges_abilities[5] == 'Финансы':
    idraw.text((615, 335), apoints_base.print_knowledges_6, font=font2)
elif database.knowledges_abilities[5] == 'Расследование':
    idraw.text((615, 352), apoints_base.print_knowledges_6, font=font2)
elif database.knowledges_abilities[5] == 'Правоведение':
    idraw.text((615, 369), apoints_base.print_knowledges_6, font=font2)
elif database.knowledges_abilities[5] == 'Лингвистика':
    idraw.text((615, 386), apoints_base.print_knowledges_6, font=font2)
elif database.knowledges_abilities[5] == 'Медицина':
    idraw.text((615, 403), apoints_base.print_knowledges_6, font=font2)
elif database.knowledges_abilities[5] == 'Оккультизм':
    idraw.text((615, 420), apoints_base.print_knowledges_6, font=font2)
elif database.knowledges_abilities[5] == 'Политика':
    idraw.text((615, 437), apoints_base.print_knowledges_6, font=font2)
elif database.knowledges_abilities[5] == 'Религия':
    idraw.text((615, 454), apoints_base.print_knowledges_6, font=font2)
elif database.knowledges_abilities[5] == 'Исследование':
    idraw.text((615, 471), apoints_base.print_knowledges_6, font=font2)
elif database.knowledges_abilities[5] == 'Наука':
    idraw.text((615, 488), apoints_base.print_knowledges_6, font=font2)
else:
    print("ERR666")

if database.knowledges_abilities[6] == 'Академические знания':
    idraw.text((615, 301), apoints_base.print_knowledges_7, font=font2)
elif database.knowledges_abilities[6] == 'Знания компьютера':
    idraw.text((615, 318), apoints_base.print_knowledges_7, font=font2)
elif database.knowledges_abilities[6] == 'Финансы':
    idraw.text((615, 335), apoints_base.print_knowledges_7, font=font2)
elif database.knowledges_abilities[6] == 'Расследование':
    idraw.text((615, 352), apoints_base.print_knowledges_7, font=font2)
elif database.knowledges_abilities[6] == 'Правоведение':
    idraw.text((615, 369), apoints_base.print_knowledges_7, font=font2)
elif database.knowledges_abilities[6] == 'Лингвистика':
    idraw.text((615, 386), apoints_base.print_knowledges_7, font=font2)
elif database.knowledges_abilities[6] == 'Медицина':
    idraw.text((615, 403), apoints_base.print_knowledges_7, font=font2)
elif database.knowledges_abilities[6] == 'Оккультизм':
    idraw.text((615, 420), apoints_base.print_knowledges_7, font=font2)
elif database.knowledges_abilities[6] == 'Политика':
    idraw.text((615, 437), apoints_base.print_knowledges_7, font=font2)
elif database.knowledges_abilities[6] == 'Религия':
    idraw.text((615, 454), apoints_base.print_knowledges_7, font=font2)
elif database.knowledges_abilities[6] == 'Исследование':
    idraw.text((615, 471), apoints_base.print_knowledges_7, font=font2)
elif database.knowledges_abilities[6] == 'Наука':
    idraw.text((615, 488), apoints_base.print_knowledges_7, font=font2)
else:
    print("ERR777")

if database.knowledges_abilities[7] == 'Академические знания':
    idraw.text((615, 301), apoints_base.print_knowledges_8, font=font2)
elif database.knowledges_abilities[7] == 'Знания компьютера':
    idraw.text((615, 318), apoints_base.print_knowledges_8, font=font2)
elif database.knowledges_abilities[7] == 'Финансы':
    idraw.text((615, 335), apoints_base.print_knowledges_8, font=font2)
elif database.knowledges_abilities[7] == 'Расследование':
    idraw.text((615, 352), apoints_base.print_knowledges_8, font=font2)
elif database.knowledges_abilities[7] == 'Правоведение':
    idraw.text((615, 369), apoints_base.print_knowledges_8, font=font2)
elif database.knowledges_abilities[7] == 'Лингвистика':
    idraw.text((615, 386), apoints_base.print_knowledges_8, font=font2)
elif database.knowledges_abilities[7] == 'Медицина':
    idraw.text((615, 403), apoints_base.print_knowledges_8, font=font2)
elif database.knowledges_abilities[7] == 'Оккультизм':
    idraw.text((615, 420), apoints_base.print_knowledges_8, font=font2)
elif database.knowledges_abilities[7] == 'Политика':
    idraw.text((615, 437), apoints_base.print_knowledges_8, font=font2)
elif database.knowledges_abilities[7] == 'Религия':
    idraw.text((615, 454), apoints_base.print_knowledges_8, font=font2)
elif database.knowledges_abilities[7] == 'Исследование':
    idraw.text((615, 471), apoints_base.print_knowledges_8, font=font2)
elif database.knowledges_abilities[7] == 'Наука':
    idraw.text((615, 488), apoints_base.print_knowledges_8, font=font2)
else:
    print("ERR888")

if database.knowledges_abilities[8] == 'Академические знания':
    idraw.text((615, 301), apoints_base.print_knowledges_9, font=font2)
elif database.knowledges_abilities[8] == 'Знания компьютера':
    idraw.text((615, 318), apoints_base.print_knowledges_9, font=font2)
elif database.knowledges_abilities[8] == 'Финансы':
    idraw.text((615, 335), apoints_base.print_knowledges_9, font=font2)
elif database.knowledges_abilities[8] == 'Расследование':
    idraw.text((615, 352), apoints_base.print_knowledges_9, font=font2)
elif database.knowledges_abilities[8] == 'Правоведение':
    idraw.text((615, 369), apoints_base.print_knowledges_9, font=font2)
elif database.knowledges_abilities[8] == 'Лингвистика':
    idraw.text((615, 386), apoints_base.print_knowledges_9, font=font2)
elif database.knowledges_abilities[8] == 'Медицина':
    idraw.text((615, 403), apoints_base.print_knowledges_9, font=font2)
elif database.knowledges_abilities[8] == 'Оккультизм':
    idraw.text((615, 420), apoints_base.print_knowledges_9, font=font2)
elif database.knowledges_abilities[8] == 'Политика':
    idraw.text((615, 437), apoints_base.print_knowledges_9, font=font2)
elif database.knowledges_abilities[8] == 'Религия':
    idraw.text((615, 454), apoints_base.print_knowledges_9, font=font2)
elif database.knowledges_abilities[8] == 'Исследование':
    idraw.text((615, 471), apoints_base.print_knowledges_9, font=font2)
elif database.knowledges_abilities[8] == 'Наука':
    idraw.text((615, 488), apoints_base.print_knowledges_9, font=font2)
else:
    print("ERR999")

if database.knowledges_abilities[9] == 'Академические знания':
    idraw.text((615, 301), apoints_base.print_knowledges_10, font=font2)
elif database.knowledges_abilities[9] == 'Знания компьютера':
    idraw.text((615, 318), apoints_base.print_knowledges_10, font=font2)
elif database.knowledges_abilities[9] == 'Финансы':
    idraw.text((615, 335), apoints_base.print_knowledges_10, font=font2)
elif database.knowledges_abilities[9] == 'Расследование':
    idraw.text((615, 352), apoints_base.print_knowledges_10, font=font2)
elif database.knowledges_abilities[9] == 'Правоведение':
    idraw.text((615, 369), apoints_base.print_knowledges_10, font=font2)
elif database.knowledges_abilities[9] == 'Лингвистика':
    idraw.text((615, 386), apoints_base.print_knowledges_10, font=font2)
elif database.knowledges_abilities[9] == 'Медицина':
    idraw.text((615, 403), apoints_base.print_knowledges_10, font=font2)
elif database.knowledges_abilities[9] == 'Оккультизм':
    idraw.text((615, 420), apoints_base.print_knowledges_10, font=font2)
elif database.knowledges_abilities[9] == 'Политика':
    idraw.text((615, 437), apoints_base.print_knowledges_10, font=font2)
elif database.knowledges_abilities[9] == 'Религия':
    idraw.text((615, 454), apoints_base.print_knowledges_10, font=font2)
elif database.knowledges_abilities[9] == 'Исследование':
    idraw.text((615, 471), apoints_base.print_knowledges_10, font=font2)
elif database.knowledges_abilities[9] == 'Наука':
    idraw.text((615, 488), apoints_base.print_knowledges_10, font=font2)
else:
    print("ERR101010")

if database.knowledges_abilities[10] == 'Академические знания':
    idraw.text((615, 301), apoints_base.print_knowledges_11, font=font2)
elif database.knowledges_abilities[10] == 'Знания компьютера':
    idraw.text((615, 318), apoints_base.print_knowledges_11, font=font2)
elif database.knowledges_abilities[10] == 'Финансы':
    idraw.text((615, 335), apoints_base.print_knowledges_11, font=font2)
elif database.knowledges_abilities[10] == 'Расследование':
    idraw.text((615, 352), apoints_base.print_knowledges_11, font=font2)
elif database.knowledges_abilities[10] == 'Правоведение':
    idraw.text((615, 369), apoints_base.print_knowledges_11, font=font2)
elif database.knowledges_abilities[10] == 'Лингвистика':
    idraw.text((615, 386), apoints_base.print_knowledges_11, font=font2)
elif database.knowledges_abilities[10] == 'Медицина':
    idraw.text((615, 403), apoints_base.print_knowledges_11, font=font2)
elif database.knowledges_abilities[10] == 'Оккультизм':
    idraw.text((615, 420), apoints_base.print_knowledges_11, font=font2)
elif database.knowledges_abilities[10] == 'Политика':
    idraw.text((615, 437), apoints_base.print_knowledges_11, font=font2)
elif database.knowledges_abilities[10] == 'Религия':
    idraw.text((615, 454), apoints_base.print_knowledges_11, font=font2)
elif database.knowledges_abilities[10] == 'Исследование':
    idraw.text((615, 471), apoints_base.print_knowledges_11, font=font2)
elif database.knowledges_abilities[10] == 'Наука':
    idraw.text((615, 488), apoints_base.print_knowledges_11, font=font2)
else:
    print("ERR1111111111")

if database.knowledges_abilities[11] == 'Академические знания':
    idraw.text((615, 301), apoints_base.print_knowledges_12, font=font2)
elif database.knowledges_abilities[11] == 'Знания компьютера':
    idraw.text((615, 318), apoints_base.print_knowledges_12, font=font2)
elif database.knowledges_abilities[11] == 'Финансы':
    idraw.text((615, 335), apoints_base.print_knowledges_12, font=font2)
elif database.knowledges_abilities[11] == 'Расследование':
    idraw.text((615, 352), apoints_base.print_knowledges_12, font=font2)
elif database.knowledges_abilities[11] == 'Правоведение':
    idraw.text((615, 369), apoints_base.print_knowledges_12, font=font2)
elif database.knowledges_abilities[11] == 'Лингвистика':
    idraw.text((615, 386), apoints_base.print_knowledges_12, font=font2)
elif database.knowledges_abilities[11] == 'Медицина':
    idraw.text((615, 403), apoints_base.print_knowledges_12, font=font2)
elif database.knowledges_abilities[11] == 'Оккультизм':
    idraw.text((615, 420), apoints_base.print_knowledges_12, font=font2)
elif database.knowledges_abilities[11] == 'Политика':
    idraw.text((615, 437), apoints_base.print_knowledges_12, font=font2)
elif database.knowledges_abilities[11] == 'Религия':
    idraw.text((615, 454), apoints_base.print_knowledges_12, font=font2)
elif database.knowledges_abilities[11] == 'Исследование':
    idraw.text((615, 471), apoints_base.print_knowledges_12, font=font2)
elif database.knowledges_abilities[11] == 'Наука':
    idraw.text((615, 488), apoints_base.print_knowledges_12, font=font2)
else:
    print("ERR12121212121")


# Преимущества

# Дополнения ---------------------------------------------

idraw.text((72, 588), apoints_base.back_print, font=font3)
idraw.text((178, 583), apoints_base.print_bpoints_1, font=font2)
idraw.text((178, 600), apoints_base.print_bpoints_2, font=font2)
idraw.text((178, 617), apoints_base.print_bpoints_3, font=font2)
idraw.text((178, 634), apoints_base.print_bpoints_4, font=font2)
idraw.text((178, 651), apoints_base.print_bpoints_5, font=font2)


# Знания ---------------------------------------------
if database.create_demon:
    char_demon = host_life_base.character
    demon_house_print = dcreate.house_demon
    demons_group = dcreate.group_of_demon
    apo_form = dcreate.apocalyptic_form

    idraw.text((340, 73), char_demon, font=font)
    idraw.text((512, 73), demon_house_print, font=font)
    idraw.text((560, 95), demons_group, font=font)
    idraw.text((520, 115), apo_form, font=font)


    if dcreate.lore_points_checked == 3:
        idraw.text((285, 585), dcreate.first_lore, font=font3)
        idraw.text((395, 581), dcreate.print_lorepoints_1, font=font2)
        print("one_lore")
    elif dcreate.lore_points_checked == 2:
        idraw.text((285, 585), dcreate.two_lores, font=font3)
        idraw.text((395, 581), dcreate.print_lorepoints_1, font=font2)
        idraw.text((395, 598), dcreate.print_lorepoints_2, font=font2)
        print("two_lore")
    elif dcreate.lore_points_checked == 1:
        idraw.text((285, 585), dcreate.three_lore_print, font=font3)
        idraw.text((395, 581), dcreate.print_lorepoints_1, font=font2)
        idraw.text((395, 598), dcreate.print_lorepoints_2, font=font2)
        idraw.text((395, 615), dcreate.print_lorepoints_3, font=font2)
        print("three_lore")
    else:
        print("LORE_ERRRORRR")
    
    if dcreate.torment == 3:
        idraw.text((274, 768), "•  • •", font=font2)
    elif dcreate.torment == 4:
        idraw.text((274, 768), "•  • •  •", font=font2)

# Добродетели --------------------------------------------------------------

idraw.text((610, 581), apoints_base.conscience_print, font=font2)
idraw.text((610, 598), apoints_base.conviction_print, font=font2)
idraw.text((610, 615), apoints_base.courage_print, font=font2)

# Вера ---------------------------------------------------------------------

idraw.text((272, 702), apoints_base.faith_print, font=font2)


# Печать
print_name.save('print_name2.png')
