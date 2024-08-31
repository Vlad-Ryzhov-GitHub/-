immutable_var = ( 1, 2, 'a', 'b')
print(immutable_var)
# immutable_var[1] = 100  # Приводит к ошибке так как кортежи не изменяемые
mutable_list = [ 1, 2, 'a', 'b' ]
mutable_list.append('Modified')
print(mutable_list)



