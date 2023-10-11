"""
Напишите программу которая считывает три целых числа из файла input.txt, делит первое число на второе и прибавляет
третье число, результат записывает в файл output.txt. используйте обработку исключений ValueError и ZeroDivisionError
"""

try:
    with open("input.txt", "r") as f:
        nms = f.read().split()
        num_1, num_2, num_3 = int(nms[0]), int(nms[1]), int(nms[1])
        result = (num_1 / num_2) + num_3
except ValueError:
    print("Error")
except ZeroDivisionError:
    print("Error")
else:
    with open("output.txt", "w") as f:
        f.write(result)
