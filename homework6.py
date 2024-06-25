my_dict = {'Vlad': 1974, 'Gleb': 2011, 'Nata': 1978}
print('Dict:', my_dict)
print("Existing value:", my_dict.get('Vlad'))
print("Not existing value:", my_dict.get('Luba'))
my_dict.update({'Luba': 1949, 'Bruno': 2020})
print(my_dict)
a = my_dict.pop('Bruno')
print(my_dict)
print(a)
my_set = {1, 1, 2, 3, 3, 'help', 545, 'help', 656}
print(my_set)
my_set = {1, 1, 2, 3, 3, 'help', 545, 'help', 656, 4, 5}
print(my_set.discard('help'))
print(my_set)