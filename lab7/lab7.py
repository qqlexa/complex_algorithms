def read_params():
    with open("INPUT.txt") as f:
        n = f.readline(2)
        array = f.readlines()
        for i in range(len(array)):
            array[i] = array[i].replace("\n", "")
        n = int(n.replace("\n", ""))
    return array, n


def save_params(max_square):
    with open("OUTPUT.txt", "w") as f:
        f.write(str(max_square))
        print("SAVED")


def create_square(i, j, max_i, max_j):
    return {"from_i": i, "from_j": j, "to_i": max_i, "to_j": max_j, "square": 1}


def calculate_square(from_i, from_j, to_i, to_j):
    return (to_i + 1 - from_i) * (to_j + 1 - from_j)


def print_square(square, array):
    for i in range(square["from_i"], square["to_i"] + 1):
        for j in range(square["from_j"], square["to_j"] + 1):
            print(array[i][j], end=" ")
        print()


def side(i, j):
    return max(i, j) - min(i, j)


def has_null(square, array):
    for i in range(square["from_i"], square["to_i"] + 1):
        for j in range(square["from_j"], square["to_j"] + 1):
            if not int(array[i][j]):
                return True
    return False


def main():
    array, n = read_params()

    squares = list()

    print(array)
    print(n)

    print("The field")
    for i in range(n):
        for j in range(len(array[i])):
            print(array[i][j], end=" ")
        print()
    print()

    for i in range(len(array)):
        for j in range(len(array[i])):
            if int(array[i][j]):
                size_side = min(side(i, len(array) - 1), side(j, len(array) - 1))

                border_i = i + size_side
                border_j = j + size_side
                square = create_square(i, j, border_i, border_j)

                # print("New square with coords: x{x} y{y}".format(x=i, y=j))
                while has_null(square, array):
                    # print(square)
                    # print_square(square, array)

                    square["to_i"] = square["to_i"] - 1 if square["to_i"] > square["from_i"] else square[
                        "from_i"]

                    square["to_j"] = square["to_j"] - 1 if square["to_j"] > square["from_j"] else square[
                        "from_j"]

                square["square"] = calculate_square(square["from_i"], square["from_j"], square["to_i"], square["to_j"])
                # print_square(square, array)

                squares.append(square)

    max_square = 1
    for square in squares:
        print(square)
        if max_square < square["square"]:
            max_square = square["square"]

    print("Count of squares - %s" % len(squares))

    print("MAX SQUARE")
    print(max_square)

    save_params(max_square)


if __name__ == '__main__':
    main()
