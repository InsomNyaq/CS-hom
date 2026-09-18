#include<bits/stdc++.h>
using namespace std;



int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int student_num = 0;
    cin >> student_num;

    vector < vector <int>> stu_and_grade(student_num, vector<int>(4));
    for (int i = 0; i < student_num; i++){
        for (int j = 0; j < 3; j++){
            cin >> stu_and_grade[i][j];
        }
    }

    //计算每个学生成绩总分并存储到第四列：
    for (int i = 0; i < student_num; i++){
        int sum = 0;
        for (int j = 0; j < 3; j++){
            sum += stu_and_grade[i][j];
            stu_and_grade[i][3] = sum;
        }
    }

    vector<int> id(student_num);

    for (int i = 0; i < student_num; i++) {
        id[i] = i;
    }


    sort(id.begin(), id.end(), [&](int x, int y) {
        if (stu_and_grade[x][3] != stu_and_grade[y][3]) {
            return stu_and_grade[x][3] > stu_and_grade[y][3];
        }
        if (stu_and_grade[x][0] != stu_and_grade[y][0]) {
            return stu_and_grade[x][0] > stu_and_grade[y][0];
        }
        return x < y;
    });

    for (int i = 0; i < 5; i++) {
        int student_id = id[i] + 1;
        int total_score = stu_and_grade[id[i]][3];

        cout << student_id << " " << total_score << '\n';
    }
        return 0;
}