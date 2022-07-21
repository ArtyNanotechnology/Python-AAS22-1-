
from homework import LevenshteinDistance


man = 'Артем'
girl = 'Анна'

names = '''
Абелия 
Абель  
Ава
Августа   
Августина  
Авдотья  
Авелин   
Аврелия  
Аврил   
Аврора   
Агапия 
Аарон   
Авдей   
Адам   
Адриан  
Азат   
Аифал   
Акакий   
Аким   
Александр   
Алексей   
Али   
Алим   
Альберт   
Альфред   
Анатолий   
Андрей   
Антон   
Аполлон   
Арам
Аристарх   
Аркадий   
Арман   
Армен   
Арсений 
'''.split('\n')


man_names_values = {}
girl_names_values = {}


dist = LevenshteinDistance()


if __name__ == "__main__":
    for i in range(len(names)):
        man_names_values.update({names[i]: dist.lev_dist(man, names[i])})

    for i in range(len(names)):
        girl_names_values.update({names[i]: dist.lev_dist(girl, names[i])})



print(f'Выбираем минимальные редакционные расстояния из всех имен к строке "{man}":')
for a, b in man_names_values.items():
    if b <= 2:
        print(f'Между строками "{man}" и "{a}" - {b}.')


print(f'Выбираем минимальные редакционные расстояния из всех имен к строке "{girl}":')
for a, b in girl_names_values.items():
    if b <= 3:
        print(f'Между строками "{girl}" и "{a}" - {b}.')



