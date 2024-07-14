first = int(input('Введи число 1: '))
second =  int(input('Введи число 2: '))
third =  int(input('Введи число 3: '))
if first == second and second == third:
    print (3)
elif first == second or first == third:
    print(2)
elif second == third:
    print(2)
else:
    print(0)