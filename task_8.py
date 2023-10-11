"""
В каждой строке файла input.txt записано одно из натуральных чисел. напишите программу solution.py,
которая удаляет в файле input.txt все строки, содержащие число 100
"""

try:
    with open("input.txt", "r") as f:
        lines = f.readlines()
    with open("input.txt", "w") as f:
        for line in lines:
            if "100" not in line:
                f.write(line)
except FileNotFoundError:
    print("Error, try again :(")
