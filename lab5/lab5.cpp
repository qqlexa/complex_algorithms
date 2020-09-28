#include <iostream>
#include <ctime>

using namespace std;

typedef struct single_node {
	int value;

	single_node* next;

};

typedef struct double_node {
	int value;

	double_node* prev;
	double_node* next;

};

typedef struct single_list {
	single_node* head;
	single_node* tail;
};

typedef struct double_list {
	double_node* head;
	double_node* tail;
};

int len_list(double_list list) {
	double_node* node = list.head;
	int i = 1;
	do {
		i++;
		node = node->next;
	} while (node->next != NULL);
	return i;
}

int len_list(single_list list) {
	single_node* node = list.head;
	int i = 1;
	do {
		i++;
		node = node->next;
	} while (node->next != NULL);
	return i;
}

void print_list(single_list list) {
	single_node* node = list.head;
	int i = 1;
	cout << "#" << ") " << "ADRESS      " << "NEXT         " << "value is " << endl;
	do {
		cout << i << ") " << node << " " << node->next << "         " << node->value;
		cout << endl;
		i++;
		node = node->next;
	} while (node->next != NULL);
	cout << endl;
}

void print_list(double_list list) {
	double_node* node = list.head;
	int i = 1;
	cout << "#" << ") " << "ADRESS      " << "PREV        " << "NEXT         " << "value is " << endl;
	do {
		cout << i << ") " << node << " " << node->prev << " " << node->next << "         " << node->value;
		cout << endl;

		i++;
		node = node->next;
	} while (node->next != NULL);
	cout << endl;
}

bool is_orderly_list(single_list list) {
	if (len_list(list) < 2)
		return true;

	single_node* node = list.head;
	do {
		if (node->value > node->next->value) {
			return false;
		}
		node = node->next;
	} while (node->next->next != NULL);
	return true;
}

bool is_orderly_list(double_list list) {
	if (len_list(list) < 2)
		return true;

	double_node* node = list.head;
	do {
		if (node->value > node->next->value) {
			return false;
		}
		node = node->next;
	} while (node->next->next != NULL);
	return true;
}

void delete_node(single_list& list, int value) {
	single_node* node = list.head;
	single_node* node_next, *node_end;
	single_node* prev_buf = NULL;
	do {
		if (node->value == value) {
			node_next = node->next;
			if (prev_buf){
				// delete
				prev_buf->next = node_next;
				
				// swap
				if (node_next->next) {
					node_end = node_next->next->next;
					if (node_end) {
						prev_buf->next = node_next->next; // 8 > 6
						node_next->next->next = node_next; // 6 > 0
						node_next->next = node_end;
					}
				}
				
				// 1 2 4 5 6
			}
			else {
				list.head = node_next->next;
				node_next->next = list.head->next;
				list.head->next = node_next;

				cout << "Now head is " << list.head->value << endl;

			}
			delete[] node;
			return;
		}
		prev_buf = node;
		node = node->next;
	} while (node->next != NULL);
}

void delete_node(double_list& list, int value) {
	double_node* node = list.head;
	do {
		if (node->value == value) {
			if (node->prev) {
				node->prev->next = node->next;
				node->next->prev = node->prev;
			}
			else {
				list.head = node->next;
			}
			delete[] node;
			return;
		}
		node = node->next;
	} while (node->next != NULL);
}

void reverse_list(single_list& list) {
	single_node* node = list.head;
	single_node* buf, * prev_buf, * next_buf, * head_buf;
	head_buf = node;

	buf = node;
	next_buf = node->next;

	buf->next = NULL;

	do {
		prev_buf = node;

		node = next_buf;

		next_buf = node->next;

		node->next = prev_buf;


	} while (next_buf->next != NULL);
	list.tail = head_buf;
	list.tail->next = next_buf;

	list.head = node;
}

void reverse_list(double_list& list) {
	double_node* node = list.head;
	double_node* buf, * head_buf;
	buf = list.tail->prev;
	head_buf = node;
	list.tail->prev = node;
	list.head = buf;

	do {
		buf = node->next;
		node->next = node->prev;
		node->prev = buf;

		node = node->prev;
	} while (node->next != NULL);
	list.tail = node;
	head_buf->next = node;
}

single_node* generate_single_node() {
	int value = rand() % 10;
	single_node* node = new single_node;
	node->value = value;
	node->next = NULL;
	return node;
}

double_node* generate_double_node(double_node* prev) {
	double_node* node = new double_node;
	node->prev = prev;
	node->next = NULL;
	return node;
}

single_list generate_single_list(int n) {
	int value;

	single_list list;
	single_node* node;
	int i = 1;
	list.head = generate_single_node();
	list.head->value = rand() % 10;
	list.head->next = generate_single_node();

	list.tail = list.head->next;

	while (i < n) {
		i++;
		value = rand() % 10;
		list.tail->next = generate_single_node();
		list.tail->value = value;
		list.tail = list.tail->next;
	}

	return list;
}

double_list generate_double_list(int n) {
	int value;

	double_list list;
	double_node* node;
	int i = 1;
	list.head = generate_double_node(NULL);
	list.head->value = rand() % 10;
	list.head->next = generate_double_node(list.head);
	list.head->prev = NULL;

	list.tail = list.head->next;

	while (i < n) {
		i++;
		value = rand() % 10;
		list.tail->next = generate_double_node(list.tail);
		list.tail->value = value;
		list.tail = list.tail->next;
	}

	return list;
}


int main() {
	/*
		# 6.	Задано натуральне число n, дiйснi числа a(1),...,a(n).
	# Якщо послiдовнiсть a(1),...,a(n) впорядкована так, що a(1) <= a(2),...,<= a(n),
	# то залишити її без змiнення. Інакше одержати послiдовнiсть a(n),...,a(1).

	I.	Створити лінійний однозв’язний список, вивести  його.
		Якщо в списку є елемент із заданим ключем, вилучити його, а два настуні поміняти місцями.
		Виконати завдання згідно варіанту.

	II.	Створити двозв’язний список, вивести  його.
		Якщо в списку є елемент із заданим ключем, вилучити його.
		Виконати завдання згідно варіанту з двозвязним спмском.

		Якщо завдання вимагає перенесення елементів (даних) у новий список, то недоцільно виділяти для таких елементів (даних) нові ділянки динамічної пам’яті.
		Найкраще вилучити такі елементи зі старого списку, не витираючи їх з пам’яті, а потім під’єднати відокремлені елементи (дані) у відповідному місці до нового списку.
		Наприкінці роботи програми треба обов’язково витерти всі створені списки, звільнивши повністю зайняту динамічну пам’ять.

	
	*/

	srand(time(0));
	int n, key;
	do {
		cout << "n must be > 5" << endl << " >> ";
		cin >> n;
	} while (n < 5);

	cout << "I ex" << endl;

	single_list s_list = generate_single_list(n);
	print_list(s_list);

	cout << "Enter a key for deleting" << endl << " >> ";
	cin >> key;
	delete_node(s_list, key);
	print_list(s_list);

	if (!is_orderly_list(s_list)) {
		cout << "Reversing " << endl;
		reverse_list(s_list);
	}
	print_list(s_list);

	cout << endl << endl << endl;

	cout << "II ex" << endl;

	double_list d_list = generate_double_list(n);
	print_list(d_list);

	cout << "Enter a key for deleting" << endl << " >> ";
	cin >> key;
	delete_node(d_list, key);
	print_list(d_list);

	if (!is_orderly_list(d_list)) {
		cout << "Reversing " << endl;
		reverse_list(d_list);
	}
	print_list(d_list);

	return 1;
}