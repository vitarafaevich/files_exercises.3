"""
Как задание 4, только проверяем существование файла до ввода строки
"""

cnt = 0
while True:
    try:
        f_name = input()
        with open(f_name, 'r') as file:
            break
    except FileNotFoundError:
        cnt += 1
        print('Error')
if cnt == 0:
    l_name = input()
    line = file.readlines()
    if l_name > len(line):
        print('Error')
    else:
        print(line[l_name - 1])
