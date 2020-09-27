from random import randint
from datetime import datetime


def partition(arr, low, high):
    i = low - 1
    pivot = arr[high]

    for j in range(low, high):

        if arr[j] <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)

        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)


def shake_sort(array, low, high):
    for k in range(high, low, -1):
        swapped = False
        for i in range(k, 0, -1):
            if array[i] < array[i - 1]:
                array[i], array[i - 1] = array[i - 1], array[i]
                swapped = True

        for i in range(k):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                swapped = True

        if not swapped:
            break
    return array


def read_array(n, path="lab3.conf"):
    array = list()

    with open(path) as f:
        text = f.read()
        numbers = list(text.split())
        numbers = [int(i) for i in numbers]
        # print(numbers)

    for i in range(n):
        array.append(list())
        for b in range(n):
            try:
                array[i].append(numbers.pop(0))
            except BaseException:
                print("Error")

    return array


def generate_array(n):
    array = list()
    for i in range(n):
        array.append(list())
        for b in range(n):
            array[i].append(randint(0, 9))
    return array


def main():
    n = 10
    # 1 exercise
    print("SHAKE")
    array = read_array(n, "lab3.conf")

    for i in range(len(array)):
        array[i] = shake_sort(array[i], 0, i)
        print(array[i])

    # 2 exercise
    print("QUICK")
    array = read_array(n, "lab3.conf")

    for i in range(len(array)):
        quick_sort(array[i], 0, i)
        print(array[i])

    # 3 exercise

    array = generate_array(500)

    copy_array = list(array)
    clock = datetime.now()
    for i in range(len(copy_array)):
        copy_array[i] = shake_sort(copy_array[i], 0, i)

    delta = clock - datetime.now()
    print("%s microseconds" % delta.microseconds)

    copy_array = list(array)
    clock = datetime.now()
    for i in range(len(copy_array)):
        quick_sort(copy_array[i], 0, i)

    delta = clock - datetime.now()
    print("%s microseconds" % delta.microseconds)


if __name__ == '__main__':
    main()
