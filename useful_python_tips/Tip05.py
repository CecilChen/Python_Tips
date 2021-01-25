names = ['Peter Parker', 'Clark Kent', 'Wade Wilon', 'Bruce Wayne']
heroes = ['Spiderman', 'Superman', 'Deadpool', 'Batman']
universes = ['Marvel', 'DC', 'Marvel', 'DC']

for name, hero, universe in zip(names, heroes, universes):
    print(f'{name} is actually {hero} from {universe}')