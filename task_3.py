"""
Напишите программу которая в файл output.txt получает последовательность символов
в виде строки, образованный последними символами каждой строки файла input.txt
"""

with open("input.txt", "r") as input_file:
    with open("output.txt", "w") as output_file:
        last_ch = ""
        for line in input_file:
            last_ch += line[-2]
        output_file.write(last_ch)
