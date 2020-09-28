import random
from colorama import Fore
from colorama import Style


def print_array(array, n, m):
    for i in range(n):
        for j in range(m):
            if j > i:
                print("{green}{a}{reset}".format(green=Fore.GREEN, a=array[i][j], reset=Style.RESET_ALL), end=" ")
            else:
                print("{red}{a}{reset}".format(red=Fore.RED, a=array[i][j], reset=Style.RESET_ALL), end=" ")
        print()


def sort_array_with_nulls(n, m, array_values, array_i, array_j):
    swap_count = True
    while swap_count:
        swap_count = False
        c = 0

        while c < len(array_values):
            i = array_i[c]
            j = array_j[c]
            if m > j > i:
                next_i = array_i[c + 1]
                if i == next_i:
                    if array_j[c + 1] == j + 1:
                        if array_values[c] > array_values[c + 1]:
                            array_values[c], array_values[c + 1] = array_values[c + 1], array_values[c]
                            swap_count = True

                    else:
                        if array_values[c] > 0 and array_j[c] + 1 < m:
                            array_j[c] += 1
                            swap_count = True

                        elif array_values[c] < 0 and array_j[c] - 1 > i:
                            array_j[c] -= 1
                            swap_count = True
                else:
                    if array_values[c] > 0 and array_j[c] + 1 < m:
                        array_j[c] += 1
                        swap_count = True

                    elif array_values[c] < 0 and array_j[c] - 1 > i:
                        array_j[c] -= 1
                        swap_count = True
            c += 1
    return array_values, array_i, array_j


def sort_matrix(array, n, m):
    swap_count = True
    while swap_count:
        swap_count = False
        for i in range(n):
            for j in range(0, m - 1):
                if j > i:
                    if array[i][j] > array[i][j + 1]:
                        array[i][j], array[i][j + 1] = array[i][j + 1], array[i][j]
                        swap_count = True

    return array


def transform_to_matrix(n, m, array_values, array_i, array_j):
    array = list()
    for i in range(n):
        array.append(list())
        for j in range(m):
            array[i].append(0)

    index = 0
    while index < len(array_values):
        array[array_i[index]][array_j[index]] = array_values[index]
        index += 1
    return array


def transform_to_compact(array, n, m):
    array_values = list()
    array_i = list()
    array_j = list()

    for i in range(n):
        for j in range(m):
            if array[i][j]:
                array_values.append(array[i][j])
                array_i.append(i)
                array_j.append(j)
    return array_values, array_i, array_j


def gen_array(n, m):
    array = list()  # array [n x n]
    for i in range(n):
        array.append(list())
        for j in range(m):
            if random.uniform(0, 1) < 0.35:
                array[i].append(random.randint(1, 9))
            else:
                array[i].append(0)
    return array


def main():
    n = 10
    m = 10

    array = gen_array(n, m)

    print_array(array, n, m)

    array_values, array_i, array_j = transform_to_compact(array, n, m)

    print()
    print(array_values)
    print(array_i)
    print(array_j)

    # 6. Сортувати по правій частині від головної діагоналі
    array_values, array_i, array_j = sort_array_with_nulls(n, m, array_values, array_i, array_j)
    array = transform_to_matrix(n, m, array_values, array_i, array_j)
    print()

    print_array(array, n, m)

    print(array_values)
    print(array_i)
    print(array_j)


if __name__ == '__main__':
    main()
