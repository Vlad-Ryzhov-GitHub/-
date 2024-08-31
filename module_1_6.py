mi_disk = {'Vasya': 1975, 'Egor': 1999,}
print(mi_disk)
print(mi_disk.get('Vasya'))
print(mi_disk.get('Kamila'))
mi_disk.update({'Kamila': 1981, 'Artem': 1915})
a= mi_disk.pop('Egor')
print(a)
print(mi_disk)

mi_set = {1, 1, 'Яблоко', 'Яблоко', 42.314, 42.314}
print(mi_set)
mi_set.add(5)
mi_set.add(6)
mi_set.discard(1)
print(mi_set)


