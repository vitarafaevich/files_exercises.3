"""
Напиши программу которая в файл output.txt записывает только те строки
файла input.txt, которые начинаются с латинского символа А
"""

with open("input.txt", "r") as input_file:
    with open("output.txt", "w") as output_file:
        for line in input_file:
            if line.startswith("A") or line.startswith("a"):
                output_file.write(line)
