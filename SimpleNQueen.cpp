#include <iostream>
#include <stdlib.h>
using namespace std;

int x[10], n;
int count = 0;   // To count solutions

bool place(int r, int c) {
    for(int i = 1; i < r; i++) {
        if(x[i] == c || abs(x[i] - c) == abs(i - r))
            return false;
    }
    return true;
}

void queen(int r) {
    for(int c = 1; c <= n; c++) {
        if(place(r, c)) {
            x[r] = c;

            if(r == n) {

                cout << "\nSolution " << ++count << ":\n";

                for(int i = 1; i <= n; i++) {
                    for(int j = 1; j <= n; j++) {
                        if(x[i] == j)
                            cout << "Q ";
                        else
                            cout << "- ";
                    }
                    cout << endl;
                }
            }
            else {
                queen(r + 1);
            }
        }
    }
}

int main() {
    cout << "Enter number of queens: ";
    cin >> n;

    queen(1);

    return 0;
}
