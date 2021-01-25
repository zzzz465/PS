#include <iostream>
#include <vector>
#include <string>

using namespace std;
string s1, s2;

int memo[1000][1000];

int findLongest(int index1, int index2, int count) {
    if (index1 >= s1.size() || index2 >= s2.size()) return count;

    char c1 = s1.at(index1);

    int& max_len = memo[index1][index2];
    if (max_len != -1) return max_len;
    max_len = 0;

    for (int i = index2; i < s2.size(); i++) {
        if (s2.at(i) == c1) {
            // 선택하냐, 안하냐로 갈림
            max_len = max(max_len, findLongest(index1+1, i+1, count+1));
            break;
        }
    }

    max_len = max(max_len, findLongest(index1+1, index2, count));

    return max_len;
}

int main() {
    cin >> s1 >> s2;

    for (int i = 0; i < 1000; i++)
        for (int j = 0; j < 1000; j++)
            memo[i][j] = -1;

    int result = findLongest(0, 0, 0);
    cout << result;

    return 0;
}