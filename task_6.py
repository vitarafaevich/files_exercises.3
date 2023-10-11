"""
Как задание 4 и 5, только работаем с номером строки
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
    line = file.readlines()
    max_num = len(line)
    while True:
        l_name = int(input())
        if l_name <= max_num:
            print(line[l_name - 1])
            break
        else:
            continue
