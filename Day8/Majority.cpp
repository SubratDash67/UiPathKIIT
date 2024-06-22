#include <iostream>
using namespace std;
int findCandidate(int a[], int size) {
    int maj_index = 0, count = 1;
    for (int i = 1; i < size; i++) {
        if (a[maj_index] == a[i])
            count++;
        else
            count--;
        if (count == 0) {
            maj_index = i;
            count = 1;
        }
    }
    return a[maj_index];
}
bool isMajority(int a[], int size, int cand) {
    int count = 0;
    for (int i = 0; i < size; i++)
        if (a[i] == cand)
            count++;
    return count > size / 2;
}
void printMajority(int a[], int size) {
    int cand = findCandidate(a, size);
    if (isMajority(a, size, cand))
        cout << " " << cand << " ";
    else
        cout << "No Majority Element";
}
int main() {
    int a[] = { 1, 3, 3, 1, 2 };
    int size = sizeof(a) / sizeof(a[0]);
    printMajority(a, size);
    return 0;
}
