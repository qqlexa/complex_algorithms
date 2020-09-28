def read_params():
    with open("INPUT_13.txt") as f:
        n, m = f.readline().split()

        array = list()

        matrix = f.readlines()
        for i in range(len(matrix)):
            array.append(list(matrix[i].replace("\n", "").split()))
            for j in range(len(array[i])):
                array[i][j] = int(array[i][j])

    return array, int(n), int(m)


def save_params(params):
    with open("OUTPUT_13.txt", "w") as f:
        f.write(str(params))
        print("SAVED")


def find_finish(array, n, m, i, j):
    ways = 0

    if array[i][j] == 0:
        print("FINISH")
        return 1

    if j + array[i][j] < m:
        # - - - >
        ways += find_finish(array, n, m, i, j + array[i][j])

    if i + array[i][j] < n:
        # down
        ways += find_finish(array, n, m, i + array[i][j], j)

    return ways


def main():
    array, n, m = read_params()
    print(n, m)
    for row_array in array:
        print(row_array)

    ways = find_finish(array, n, m, 0, 0)
    print(ways)
    save_params(ways)


if __name__ == '__main__':
    main()
"""
N M
3 4
2 1 1 2
3 2 1 44
3 1 1 0

ANS :   3
"""
