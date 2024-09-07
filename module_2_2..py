first = int(input('Ввести первое число: '))
second = int(input('Ввести второе число: '))
third = int(input('Ввести третие число: '))
if first == second == third:
    print(3)
elif first == second or first != third or second != third:
    print(2)
else:
    print(0)