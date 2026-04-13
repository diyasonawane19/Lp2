#include<iostream>
#include<vector>
#include<queue>
#include<stack>
using namespace std;

vector<bool> visit;

void edge(vector<int> adj[], int u, int v)
{
adj[u].push_back(v);
}

void bfs(int s, vector<int> adj[])
{
queue<int> q;
q.push(s);
visit[s] = true;

while(!q.empty())
{
int u = q.front();
cout << u << " ";
q.pop();

for(int i = 0; i < adj[u].size(); i++)
{
if(!visit[adj[u][i]])
{
q.push(adj[u][i]);
visit[adj[u][i]] = true;
}
}
}
}

void dfs(int s, vector<int> adj[])
{
stack<int> stk;
stk.push(s);
visit[s] = true;

while(!stk.empty())
{

int u = stk.top();
cout << u << " ";
stk.pop();

for(int i = 0; i < adj[u].size(); i++)
{
if(!visit[adj[u][i]])
{
stk.push(adj[u][i]);
visit[adj[u][i]] = true;
}
}
}
}

int main()
{
int n, e;
cout << "\n enter the number of vertices: ";
cin >> n;

cout << "\n enter the number of edges: ";
cin >> e;

visit.assign(n, false);

vector<int> adj[n];

int u, v;
cout << "\n enter the edges with source and target vertex:\n";

for(int i = 0; i < e; i++)
{
cin >> u >> v;
edge(adj, u, v);
}

cout << "BFS traversal is: ";
bfs(0, adj);
cout << endl;

visit.assign(n, false);

cout << "DFS traversal is: ";
dfs(0, adj);
cout << endl;

return 0;
}
