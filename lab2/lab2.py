from datetime import datetime


def fact(a):
    if a == 0:
        return 1
    return a ** fact(a - 1)


def recursive_sum_solve(k, x):
    for n in range(1, k + 1):
        currently_factorial = fact(n)
        symbol = -1 if n % 2 == 0 else 1 # 1 or -1

        yield (symbol * x**3) / (currently_factorial + n*n)


def sum_solve(k, x):
    our_sum = 0
    for n in range(1, k + 1):
        currently_factorial = 1
        for i in range(n):
            currently_factorial *= i

        symbol = -1 if n % 2 == 0 else 1
        our_sum += symbol * x**3 / (currently_factorial + n*n)

    return our_sum


def main():
    k = 992
    x = 100

    currently_time = datetime.now()

    recursive_gen = recursive_sum_solve(k=k, x=x)
    result_list = list(recursive_gen)
    print(result_list)
    final_time = datetime.now()

    our_sum = 0
    our_sum += sum([x for x in result_list])

    print("{sum} in {time}mcs".format(sum=our_sum, time=(final_time - currently_time).microseconds))
    currently_time = datetime.now()
    print(our_sum, end=" ")
    final_time = datetime.now()
    print("in {time}mcs".format(time=(final_time - currently_time).microseconds))


if __name__ == '__main__':
    main()
