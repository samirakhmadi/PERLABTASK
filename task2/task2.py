"""
Напишите программу, которая рассчитывает положение точки относительно окружности. Координаты центра окружности и его
радиус считываются из файла1.

Пример:
1 1
5

Координаты точек считываются из файла2.
Пример:
0 0
1 6
6 6

Файлы передаются программе в качестве аргументов. Файл с координатами и радиусом окружности - 1 аргумент, файл
с координатами точек - 2 аргумент. Координаты в диапазоне float. Количество точек от 1 до 100.
Вывод каждого положения точки заканчивается символом новой строки.

Соответствия ответов:
0 - точка лежит на окружности
1 - точка внутри
2 - точка снаружи
"""
import sys


def where_is_dote(r:int, x_crcl:float, y_crcl:float, x1:float, y1:float):
   """
   This function take 5 args (coordinate of dote, coordinate centre of circle and radius ) and check where
   is dote relative to the circle: inside, outside, on circle
   :param r: radius of circle
   :param x_crcl: coord x of circle
   :param y_crcl: coord y of circle
   :param x1: coord x of dote
   :param y1: coord y of dote
   :return: print( 0 - dote on circle, 1 - dote inside, 2 - dote outside)
   """
   if ((x1 - x_crcl) ** 2 + (y1 - y_crcl) ** 2) < r ** 2:
        print(1, end="\n")
   elif (x1 - x_crcl) ** 2 + (y1 - y_crcl) ** 2 == r ** 2:
        print(0, end="\n")
   else:
        print(2, end="\n")


file1 = sys.argv[1]
file2 = sys.argv[2]
circle_list = []
dots_list = []

# read file1 and make list with coordinate center of circle and radius:
with open(f'{file1}', "r", encoding="utf-8") as file:
    for line in file:
        circle_list.append(line.strip().rsplit(maxsplit=-1))

x_crcl, y_crcl, r = float(circle_list[0][0]), float(circle_list[0][1]), int(*circle_list[1])

# read file2 and make list with coordinate of dots:
with open(f'{file2}', "r", encoding="utf-8") as file:
    for row in file:
        dots_list.append(row.strip().rsplit(maxsplit=-1))

i = 1  # count dots, must be less than or 100
for element in dots_list:
    if i <= 100:
        x1, y1 = float(element[0]), float(element[1])
        where_is_dote(r, x_crcl, y_crcl, x1, y1)  # call function for chek place for dot and print result
        i += 1
    else:
        break
