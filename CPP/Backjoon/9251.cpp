#include <iostream>
#include <vector>
#include <string>

using namespace std;
string s1, s2;

int memo[1000][1000];

int findLongest(int index1, int index2) {
    if (index1 < 0 || index2 < 0) return 0;

    char c1 = s1.at(index1);
    char c2 = s2.at(index2);

    int& ret = memo[index1][index2];
    if (ret != -1) return ret;

    if (c1 == c2)
         ret = findLongest(index1-1, index2-1) + 1;
    else
        ret = max(findLongest(index1-1, index2), findLongest(index1, index2-1));

    return ret;
}

int main() {
    cin >> s1 >> s2;

    for (int i = 0; i < 1000; i++)
        for (int j = 0; j < 1000; j++)
            memo[i][j] = -1;

    int result = findLongest(s1.size() - 1, s2.size() - 1);
    cout << result;
/*
    for (int i = 0; i < s1.size(); i++) {
        for (int j = 0; j < s2.size(); j++) {
            cout << memo[i][j] << " ";
        }
        cout << "\n";
    }
*/

    return 0;
}