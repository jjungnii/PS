#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

static vector<long> tree;

void setTree(int i);
long getSum(int s, int e);
void changeVal(int index, long val);

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int N, M, K;
    cin >> N >> M >> K;

    int treeHeight = (int)ceil(log2(N));
    int treeSize = (1 << (treeHeight + 1));
    int leafNodeStartIndex = treeSize / 2;

    tree.resize(treeSize);

    // 리프 노드 초기화
    for(int i = 0; i < N; ++i){
        cin >> tree[leafNodeStartIndex + i];
    }
    
    // 세그먼트 트리 구성
    setTree(treeSize - 1);

    for(int i = 0; i < M + K; ++i){
        long a, s, e;
        cin >> a >> s >> e;
        if(a == 1){
            changeVal(leafNodeStartIndex + s - 1, e);
        } else if(a == 2){
            cout << getSum(leafNodeStartIndex + s - 1, leafNodeStartIndex + e - 1) << "\n";
        }
    }

}

void setTree(int i){
    while(i > 1){
        tree[i / 2] = tree[i / 2 * 2] + tree[i / 2 * 2 + 1];
        i -= 2;
    }
}

void changeVal(int index, long val){
    long diff = val - tree[index];
    while(index > 0){
        tree[index] += diff;
        index /= 2;
    }
}

long getSum(int s, int e){
    long partSum = 0;
    while(s <= e){
        if(s % 2 == 1) partSum += tree[s++];
        if(e % 2 == 0) partSum += tree[e--];
        s /= 2;
        e /= 2;
    }
    return partSum;
}