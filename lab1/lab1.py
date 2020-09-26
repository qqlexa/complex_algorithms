from random import randint
import datetime


def generate_array(n, m):
    array = []
    for i in range(n):
        array.append(list())
        for j in range(m):
            array[i].append(randint(-10, 2))
    return array


def main():
    keys = [10, 20, 50, 100, 250, 500, 1000, 3000]
    results = []

    for i in keys:

        first_timestamp = datetime.datetime.now()

        currently_array = generate_array(i, i)  # create matrix[i][i]
        print(currently_array)

        for b in range(len(currently_array)):
            count_negative = 0

            for c in currently_array[b]:
                count_negative = count_negative + 1 if c < 0 else count_negative

            if count_negative > i / 2:
                currently_array[b] = currently_array[b][::-1]

        second_timestamp = datetime.datetime.now()

        delta_time = (second_timestamp - first_timestamp).microseconds
        print(currently_array)
        print("key={}. {} microseconds".format(i, delta_time))
        results.append(delta_time)

    print("KEY\tMICROSECONDS")
    for i in range(len(keys)):
        print("{}\t{}".format(keys[i], results[i]))


if __name__ == '__main__':
    main()
