#include <iostream>
#include <fstream>
#include <string>
using namespace std;



char** read_rules(char** arr_rules, int arr_count[6]) {
    ifstream file("input.txt");
    if (file.is_open()) {
        for (int i = 0; i < 6; i++) {
            string tp;
            getline(file, tp);
            for (int j = 0; j < arr_count[i]; j++) {
                arr_rules[i][j] = tp[j];
            }

        }
        file.close();
        for (int i = 0; i < 6; i++) {
            for (int j = 0; j < arr_count[i]; j++) {
                cout << arr_rules[i][j];
            }
            cout << endl;
        }
    }
    return arr_rules;



}

int read_count(int arr_count[6], char& letter, int& n ){
    ifstream file("input.txt"); 
    if (file.is_open()){
        for (int i = 0; i < 6; i++) {
            string tp;
            getline(file, tp);
            arr_count[i] = tp.length();

        }


        file >> letter;
        file >> n;
        file.close();
    }
    return 0;

}

int find_way(char** arr_rules, int arr_count[6], char letter, int n){
    int way = 0;

    for ()

    return way;
}

int main()
{
    int arr_count[6] = { 0 };
    char letter;
    int n;
    read_count(arr_count, letter, n);
    for (int i = 0; i < 6; i++) {
        cout << arr_count[i] << " ";
    }
    cout << endl;
    cout << letter << endl;
    cout << n << endl;
    char* arr_n = new char[arr_count[0]];
    char* arr_s = new char[arr_count[1]];
    char* arr_w = new char[arr_count[2]];
    char* arr_e = new char[arr_count[3]];
    char* arr_u = new char[arr_count[4]];
    char* arr_d = new char[arr_count[5]];

    char** arr_rules = {arr_n, arr_s, arr_w, arr_e, arr_u, arr_d}
    arr_rules = read_rules(arr_rules, arr_count);

    int way = find_way(arr_rules, arr_count, letter, n); 

    return 0;
}