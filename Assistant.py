a = input('Введите список фамилий:')
my_list = a.split()
for surname in my_list:
    current_surname = len(surname)
    if current_surname < 3:
        print('Есть: ' + surname)
    elif surname[-1] == '.':
        print('Есть: ' + surname)
print('Проверка завершена!')
