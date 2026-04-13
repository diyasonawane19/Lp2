#include <iostream>
using namespace std;
void selectionSort(int arr[], int n) {
for (int i = 0; i < n - 1; i++) {
int minIndex = i;
// Find the minimum element in the unsorted part
for (int j = i + 1; j < n; j++) {
if (arr[j] < arr[minIndex]) {
minIndex = j;
}
}
// Swap if needed
if (minIndex != i) {
int temp = arr[i];
arr[i] = arr[minIndex];
arr[minIndex] = temp;
}
}
}
int main() {
int n;
cout << "Enter number of elements: ";
cin >> n;
int arr[n]; // Variable-length array (works in most compilers)
cout << "Enter " << n << " elements:\n";
for (int i = 0; i < n; i++) {
cin >> arr[i];
}
selectionSort(arr, n);
cout << "Sorted array: ";
for (int i = 0; i < n; i++) {
cout << arr[i] << " ";

}
return 0;
}
