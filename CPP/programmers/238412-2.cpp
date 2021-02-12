// 스타 수열 구하기
#include <string>
#include <vector>
#include <climits>
#include <algorithm>

// #include <iostream> // 필요없음 디버깅용

using namespace std;

vector<int> counter;
int n; // a의 크기
int max_len = 0;

void solve(const vector<int>& record) {
    counter = vector<int>(n, 0);

    for (int i = 1; i < record.size(); i += 2) {
        // 2단계씩 건너뛰며 검색
        auto val1 = record.at(i-1);
        auto val2 = record.at(i);

        if (val1 == val2)
            counter.at(val1) += 1;
        else {
            counter.at(val1) += 1;
            counter.at(val2) += 1;
        }
    }

    for (auto val : counter)
        if (val == record.size() / 2) { // 존재함
            max_len = max(max_len, (int)record.size());
            return;
        }
}

void DFS(const vector<int>& a, const vector<int>& record, int index) {
    if (index >= a.size()) {
        if (record.size() > 0 && record.size() % 2 == 0) {
            if (max_len < record.size()) // 가능성이 있을 경우
                solve(record);
        }

        return;
    }

    auto Select = record;
    Select.push_back(a.at(index));
    DFS(a, Select, index + 1);

    if(record.size() + a.size() - index > max_len) {
        auto notSelect = record;
        DFS(a, notSelect, index + 1);
    }
}

int solution(vector<int> a) {
    n = a.size();

    vector<int> record;
    DFS(a, record, 0);

    // cout << max_len; // 디버깅용!!!!

    return max_len;
}

int main() {
    vector<int> vect1 { 0 };
    vector<int> vect2 { 5, 2, 3, 3, 5, 3 };
    vector<int> vect3 { 0, 3, 3, 0, 7, 2, 0, 2, 2, 0 };
    int res1 = solution(vect1);
    int res2 = solution(vect2);
    int res3 = solution(vect3);

    return 0;
}