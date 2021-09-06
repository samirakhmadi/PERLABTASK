
import sys


n = int(sys.argv[1])  # len of array
m = int(sys.argv[2])  # len of step array

array = [i for i in range(1, (n + 1))]  # [1, 2, 3, 4, 5] for n = 5
array2 = array * n ** 2  # Make circle array
make_list_step_m = lambda array2: [array2[i:i+m] for i in range(0, len(array2), m)]  # function make list from circle array with step m
array = make_list_step_m(array2)  # [[1, 2, 3, 4], [5, 1, 2, 3], [4, 5, 1, 2], [3, 4, 5, 1] ...]
list_final = [array[0]]  # make final list where first element is first element of array
i, j = 0, 0

for elements in array:
    if int(list_final[(len(list_final))-1][m-1]) != int(array[i][j]):  # compare last digit of list final with first
                                                                       # digit of next element in array
        i += 1
    elif int(list_final[(len(list_final))-1][m-1]) == int(array[i][j]):
        if elements not in list_final:
            list_final.append(elements)  # append to list final list of digits where first digit is the same of last
        i += 1
    else:
        pass
i = 0
for item in list_final:
    print(list_final[i][0], end="")
    i += 1
