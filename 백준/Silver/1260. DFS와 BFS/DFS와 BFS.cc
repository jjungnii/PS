#include <iostream>
#include <vector>
#include <queue>
#include <string.h>
#include <algorithm>

#define MAX_N 10000

using namespace std;

vector<int> Graph[MAX_N + 1];
int Visited[MAX_N + 1];

void dfs(int v){
    Visited[v] = true;
    cout << v << " ";
    for(int i = 0; i < Graph[v].size(); ++i){
        int idx = Graph[v][i];
        if(!Visited[idx] && idx)
            dfs(idx);
    }
}

void bfs(int v){
    queue<int> q;
    q.push(v);
    Visited[v] = true;

    while(!q.empty()){
        int curr = q.front();
        q.pop();
        cout << curr << " ";

        for(int i = 0; i < Graph[curr].size(); ++i){
            int idx = Graph[curr][i];
            if(!Visited[idx] && idx){
                q.push(idx);
                Visited[idx] = true;
            }
        }
    }
}

int main(){

    int N, M, V, v1, v2;

    cin >> N >> M >> V;

    for(int i = 0; i < M; ++i){
        cin >> v1 >> v2;
        Graph[v1].push_back(v2);
        Graph[v2].push_back(v1);
    }

    for (int i = 1; i <= N; ++i) {
		sort(Graph[i].begin(), Graph[i].end());
	}
    
    dfs(V);
    cout << "\n";
    memset(Visited, false, sizeof(Visited));
    bfs(V);
}