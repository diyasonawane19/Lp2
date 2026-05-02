#include <iostream>
#include <cstring>   // for memset
using namespace std;

int matrix[10][10], qu[10], front = 0, rear = 0, visited[10];
int stk[10], top = -1, visited1[10];

int main() {
    int n, m, i, j, k, v;

    memset(matrix, 0, sizeof(matrix));
    memset(visited, 0, sizeof(visited));
    memset(visited1, 0, sizeof(visited1));

    cout << "Enter number of vertices: ";
    cin >> n;

    cout << "Enter number of edges: ";
    cin >> m;

    cout << "\nEnter edges (0-based index): \n";
    for (k = 0; k < m; k++) {
        cin >> i >> j;
        matrix[i][j] = 1;
        matrix[j][i] = 1;
    }

    // Display adjacency matrix
    cout << "\nThe adjacency matrix of the graph is:\n";
    for (i = 0; i < n; i++) {
        for (j = 0; j < n; j++) {
            cout << matrix[i][j] << " ";
        }
        cout << endl;
    }

    // BFS
    cout << "\nEnter initial vertex for BFS: ";
    cin >> v;

    cout << "The BFS of the Graph is:\n";
    cout << v << " ";

    visited[v] = 1;
    qu[rear++] = v;

    while (front < rear) {
        v = qu[front++];

        for (j = 0; j < n; j++) {
            if (matrix[v][j] && !visited[j]) {
                cout << j << " ";
                visited[j] = 1;
                qu[rear++] = j;
            }
        }
    }

    // DFS
    cout << "\n\nEnter initial vertex for DFS: ";
    cin >> v;

    cout << "The DFS of the Graph is:\n";
    cout << v << " ";

    visited1[v] = 1;
    stk[++top] = v;   // Fixed here

    while (top >= 0) {
        v = stk[top--];

        for (j = n - 1; j >= 0; j--) {
            if (matrix[v][j] && !visited1[j]) {
                cout << j << " ";
                visited1[j] = 1;
                stk[++top] = j;
            }
        }
    }

    return 0;
}
