from random import randint
from datetime import datetime
import math

phi = (1 + math.sqrt(5)) / 2


def find_barrier(arr, size, value):
    last = arr[size - 1]
    arr[size - 1] = value
    i = 0
    while True:
        if arr[i] == value:
            break
        i += 1

    arr[size - 1] = last

    if i != size - 1 or value == last:
        return i
    return False


def find_gold_section(arr, low, high, value):
    while high - low < 2:
        a = arr[low]
        b = arr[high]

        x1 = int(b - (b - a) / phi)
        x2 = round(a + (b - a) / phi)

        if arr[x2] < value:
            low = x2

        elif arr[x1] > value:
            high = x1

        else:
            low = x1
            high = x2

    if arr[low] == value:
        return low
    elif arr[low + 1] == value:
        return low + 1
    elif arr[high] == value:
        return high
    else:
        return False


def generate_array(n, max_element):
    array = list()
    for b in range(n):
        array.append(randint(0, max_element))
    return array


def main():
    n = 100000
    number = 10000

    # 1 exercise
    clock = datetime.now()
    array = generate_array(n, number)
    position = find_barrier(array, n, number)
    delta = clock - datetime.now()
    print(position)

    print("Iterations by first method: %s" % n)
    print("%s microseconds" % delta.microseconds)

    # 2 exercise
    clock2 = datetime.now()
    array = list(range(n))
    position = find_gold_section(array, 0, n - 1, number)
    delta = clock2 - datetime.now()
    print(position)

    print("Iterations by second method: %s" % n)
    print("%s microseconds" % delta.microseconds)



if __name__ == '__main__':
    main()
