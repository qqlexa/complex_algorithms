import random


def shift_array(array_values, array_i, array_j, step):
    c = 0

    while c < len(array_values) - 1:

        row_size = 0

        prev_i = array_i[c]
        i = array_i[c + 1]
        n = c

        while i == prev_i and n < len(array_values) - 1:
            row_size += 1

            prev_i = array_i[n]
            i = array_i[n + 1]
            n += 1

        # Shift
        index = 0
        while index < row_size:
            print("Row size % {row_size} to {c}".format(row_size=row_size, c=c))
            new_pos = (c + step) % row_size
            print("First pos {c} to {new_pos}".format(c=c, new_pos=new_pos))
            array_values[c], array_values[new_pos] = array_values[new_pos], array_values[c]
            index += 1

        print("E")
        c = n + 1
        print("n {n} to {c}".format(n=n, c=c))

    return array_values


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

    for line_array in array:
        print(line_array)
    print()

    array_values, array_i, array_j = transform_to_compact(array, n, m)

    print()
    print(array_values)
    print(array_i)
    print(array_j)

    # 13. Змістити кожен рядок на 5 елементів
    array_values = shift_array(array_values, array_i, array_j, 5)
    array = transform_to_matrix(n, m, array_values, array_i, array_j)

    print()

    for row_array in array:
        print(row_array)
    print()

    print(array_values)
    print(array_i)
    print(array_j)


if __name__ == '__main__':
    main()
