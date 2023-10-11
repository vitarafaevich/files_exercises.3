"""
Напишите программу которая запрашивает имя файла, номер строки и
выводит на экран строку файла с заданным номером.
обработайте все необходимые исключительные ситуации
"""
try:
    f_name = input()
    l_name = int(input())
    with open(f_name, 'r') as file:
        line = file.readlines()
        if l_name > len(line):
            print('Error')
        else:
            print(line[l_name - 1])
except FileNotFoundError:
    print("Error")
