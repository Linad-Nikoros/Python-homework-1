# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

num_1=int(input("Введите число,обозначающее день недели: "))

if num_1 < 1 or num_1 > 7:
 print("Вы ввели недопустимое число")
elif num_1==7 or num_1==6:
    print("Это выходной день")
else:
    print("Это НЕ выходной день")