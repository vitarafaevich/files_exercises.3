"""
Напишите программу, которая считывает текст из файла input.txt
и записывает этот текст в верхнем регистре файла output.txt
"""

with open('input txt', 'r') as f:
    text = f.read()
text = text.upper
with open('output.txt', 'w') as file:
    file.write(text)
