first = int(input('Ввести первое число: '))
second = int(input('Ввести второе число: '))
third = int(input('Ввести третие число: '))
if first == 10 and second == 10 and third == 10:
    print(3)
elif first == 10 and second == 10 or third == 10:
    print(2)
elif not first == 10 and second == 10 and third == 10:
    print(0)

