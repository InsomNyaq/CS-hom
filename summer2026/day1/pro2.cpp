#include<bits/stdc++.h>
using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n = 0;
    cin >> n;
    vector<string> a (n);

    for(int i = 0; i < n; i++){
        cin >> a[i];
    }

    sort(a.begin(), a.end(), [](string x, string y) { return x + y > y + x; });

    for(string s : a){
        cout << s;

    }
    cout << '\n';
    
    return 0;
}