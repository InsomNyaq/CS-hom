// #include <bits/stdc++.h>
// using namespace std;
// using ll = long long;

// int main() {
//     ios::sync_with_stdio;
//     cin.tie(nullptr);

//     stack<int> s1, s2;
//     int N = 0;
//     cin >> N;
//     char input;
//     int element;

//     for (int i = 0; i < N; i++){
//         cin >> input;

//         if (input == 'I'){
//             cin >> element;
//             s1.push(element);
//         }
//         else if (input == 'O'){
//             int count = 0;

//             if(!s2.empty()){
//                 int ans = s2.top();
//                 s2.pop();
//                 count++;

//                 cout << ans << " " << count << '\n';
//             }else if (!s1.empty()){
//                 while(!s1.empty()){
//                     s2.push(s1.top());
//                     count++;

//                     s1.pop();
//                     count++;
//                 }
//                 int ans = s2.top();
//                 s2.pop();
//                 count++;

//                 cout << ans << " " << count << '\n';
//             }
//             else{
//                 cout << "ERROR\n";
//             }
//         }
//     }

//         return 0;
// }

// #include <bits/stdc++.h>
// using namespace std;
// using ll = long long;

// int main() {
//     ios::sync_with_stdio;
//     cin.tie(nullptr);
//     int n, k;
//     cin >> n >> k;

//     vector<int> a(n);
//     for (int i = 0; i < n; i++){
//         cin >> a[i];
//     }

//     deque<int> qmin, qmax;

//     for (int i = 0; i < n; i++){
//         while(!qmin.empty() && qmin.front() < i-k){
//             qmin.pop_front();
//         }

//         while(!qmin.empty() && a[qmax.back()] >= a[i])
//         {
//             qmin.pop_back();
//         }

//         qmin.push_back(i);

//         if (i >= k-1){
//             cout << a[qmin.front()];
//             if ( i!= n -1 ){
//                 cout << ' ';
//             }
//         }
//     }
//         cout << '\n';

//     // 第二行：最大值
//     for (int i = 0; i < n; i++) {
//         // 删除已经离开窗口的元素
//         while (!qmax.empty() && qmax.front() <= i - k) {
//             qmax.pop_front();
//         }

//         // 删除比当前元素小的元素
//         while (!qmax.empty() && a[qmax.back()] <= a[i]) {
//             qmax.pop_back();
//         }

//         qmax.push_back(i);

//         // 窗口形成之后输出最大值
//         if (i >= k - 1) {
//             cout << a[qmax.front()];
//             if (i != n - 1) {
//                 cout << ' ';
//             }
//         }
//     }

//     cout << '\n';

//         return 0;
// }

// #include <bits/stdc++.h>
// using namespace std;
// using ll = long long;

// const int MAXN = 1000005;

// int parent[MAXN];
// int sz[MAXN];

// int find(int x) {
//     if (parent[x] == x) {
//         return x;
//     }

//     return parent[x] = find(parent[x]);
// }

// void unite(int a, int b) {
//     a = find(a);
//     b = find(b);

//     if (a == b) {
//         return;
//     }

//     if (sz[a] < sz[b]) {
//         swap(a, b);
//     }

//     parent[b] = a;

//     sz[a] = sz[a] + sz[b];
// }

// int main() {
//     ios::sync_with_stdio(false);
//     cin.tie(nullptr);

//     int n, m, p;
//     cin >> n >> m >> p;

//     for (int i = 0; i < n; i++) {
//         parent[i] = i;
//         sz[i] = 1;
//     }

//     for (int i = 0; i < m; i++) {
//         int a, b;
//         cin >> a >> b;
//         unite(a, b);
//     }

//     for (int j = 0; j < p; j++) {
//         int pi, pj;
//         cin >> pi >> pj;

//         if (find(pi) == find(pj)) {
//             cout << "Yes\n";
//         } else {
//             cout << "No\n";
//         }
//     }

//     return 0;
// }

// #include <bits/stdc++.h>
// using namespace std;
// using ll = long long;
// int dx[8] = {1, 1, -1, -1, 2, 2, -2, -2};
// int dy[8] = {2, -2, 2, -2, 1, -1, 1, -1};

// int dist[32][32] = {};

// int main() {
//     ios::sync_with_stdio(false);
//     cin.tie(nullptr);
//     int n, m, x1, y1;
//     cin >> n >> m >> x1 >> y1;
//     int x2, y2;
//     cin >> x2 >> y2;

//     memset(dist, -1, sizeof(dist)); // 未访问的设置成-1
//     queue<pair<int, int>> q;

//     q.push({x1, y1});
//     dist[x1][y1] = 0;

//     while (!q.empty()) {
//         auto [x, y] = q.front();
//         q.pop();

//         for (int i = 0; i < 8; i++) {
//             int nx = x + dx[i];
//             int ny = y + dy[i];

//             // go over the edge:
//             if (nx < 0 || nx >= n || ny < 0 || ny >= m) {
//                 continue;
//             }
//             // have already visit this node;
//             if (dist[nx][ny] != -1) {
//                 continue;
//             }

//             dist[nx][ny] = dist[x][y] + 1;
//             q.push({nx, ny});
//         }
//     }

//     if (dist[x2][y2] == -1) {
//         cout << 0 << "\n";
//     } else {
//         cout << dist[x2][y2] << "\n";
//     }

//     return 0;
// }

#include<bits/stdc++.h>
using namespace std;
using ll = long long;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    


    return 0;
}
