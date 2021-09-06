"""
Дан массив целых чисел nums. Напишите программу, выводящую минимальное количество ходов, требуемых для приведения всех
элементов к одному числу. За один ход можно уменьшить или увеличить число массива на 1.
Пример:
nums = [1, 2, 3]
Решение: [1, 2, 3] => [2, 2, 3] => [2, 2, 2]
Минимальное количество ходов: 2
Элементы массива читаются из файла, переданного в качестве аргумента командной строки.
Пример:
На вход подаётся файл с содержимым:
1
10
2
9
Вывод в консоль:
16
"""
import sys
import numpy as np


file = sys.argv[1]
nums = []

with open(f'{file}', "r", encoding="utf-8") as file:
    for line in file:
        Nums = line.strip().rsplit(maxsplit=-1)
        nums.append(*Nums)

nums_result = np.array([int(i) for i in nums])
print(int(np.sum(np.abs(nums_result-np.median(nums_result)))))
