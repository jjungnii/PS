#include <iostream>
using namespace std;

pair<char,char> tree[26];

void preorder(char curr){
    if(curr == '.')
        return;
    
    cout << curr;
    preorder(tree[curr-'A'].first);
    preorder(tree[curr-'A'].second);
}

void inorder(char curr){
    if(curr == '.')
        return;

    inorder(tree[curr-'A'].first);
    cout << curr;
    inorder(tree[curr-'A'].second);
}

void postorder(char curr){
    if(curr == '.')
        return;

    postorder(tree[curr-'A'].first);
    postorder(tree[curr-'A'].second);
    cout << curr;
}

int main(){
    int N;
    char parent, left, right;
  
    cin >> N;
    
    for(int i = 0; i < N; ++i){
        cin >> parent >> left >> right;
        tree[parent-'A'] = {left, right};
    }
  
    preorder('A');
    cout << "\n";
    inorder('A');
    cout << "\n";
    postorder('A');
}