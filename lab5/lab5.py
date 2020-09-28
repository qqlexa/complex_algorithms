# 6.	Задано натуральне число n, дiйснi числа a(1),...,a(n).
# Якщо послiдовнiсть a(1),...,a(n) впорядкована так, що a(1) <= a(2),...,<= a(n),
# то залишити її без змiнення. Інакше одержати послiдовнiсть a(n),...,a(1).
"""
I.	Створити лінійний однозв’язний список, вивести  його.
	Якщо в списку є елемент із заданим ключем, вилучити його, а два настуні поміняти місцями.
	Виконати завдання згідно варіанту.

II.	Створити двозв’язний список, вивести  його.
	Якщо в списку є елемент із заданим ключем, вилучити його.
	Виконати завдання згідно варіанту з двозвязним спмском.

	Якщо завдання вимагає перенесення елементів (даних) у новий список, то недоцільно виділяти для таких елементів (даних) нові ділянки динамічної пам’яті.
	Найкраще вилучити такі елементи зі старого списку, не витираючи їх з пам’яті, а потім під’єднати відокремлені елементи (дані) у відповідному місці до нового списку.
	Наприкінці роботи програми треба обов’язково витерти всі створені списки, звільнивши повністю зайняту динамічну пам’ять.

"""

from random import uniform

# union any {
#     int value;
#     char* value
#     . . . . .
# }
# typedef struct list {
#    int i;
#    union value;
#
#    list* next;
#    list* prev;
#
#
# }


n = 15
my_list = list()
#


for i in range(n):
    my_list.append(round(uniform(10, 100), 2))

print(my_list)

key = float(input("I. Enter key for deleting: "))

for i in range(n):
    if my_list[i] == key:
        print("Found!")
        my_list.pop(i)
        print("Deleted!")
        if i < n - 2:
            my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
        break
print(my_list)

key = float(input("II. Enter key for deleting: "))

for i in range(n):
    if my_list[i] == key:
        print("Found!")
        my_list.pop(i)
        print("Deleted!")
        break
print(my_list)

for i in range(n - 1):
    if my_list[i] > my_list[i + 1]:
        my_list = my_list[::-1]
        break

print(my_list)

del my_list
