#include <iostream>
#include <string>
#include <cstring>
#include <vector>

std::vector<char> idols, fans;
std::vector<int> idolsToCheck; // 아이돌중에 M만 체크하면 되고, 그 M에 해당하는 index들을 역순으로 가짐
std::vector<int> jump; // 얼마만큼 이동해야 하는가?

void prepare() {
    idolsToCheck.clear();
    jump = std::vector<int>(idols.size(), 1);

    for (int i = jump.size() - 1; i >= 0; i--)
        if (idols[i] == 'M') {
            for (int j = i; j >= 0; j--) {
                if (idols[j] == 'F') {
                    jump[i] = i - j;
                    break;
                }
            }
            idolsToCheck.push_back(i);
        }

    jump[0] = 1;
    /*
    std::cout << "jump vector is" << "\n";
    for (int i : jump) {
        std::cout << i << " ";
    }
    std::cout << "\n";
    */
}

int solve() {
    prepare();

    int count = 0;
    int index = 0;
    START:
    while (index + idols.size() <= fans.size()) {
        for(int i : idolsToCheck) { // 뒤에서 앞으로 가면서 조건위배 체크
            int fanIndex = index + i;
    
            if (fanIndex >= fans.size())
                goto END;
    
            if (idols[i] == 'M' && fans[fanIndex] == 'M') {
                index += jump[i];
                goto START;
            }
        }

        count += 1;
        index += 1;
    }

    END:

    return count;
}

int main() {
    // std::ios::sync_with_stdio(false);
    int C;
    std::cin >> C;

    for (int a = 0; a < C; a++) {
        std::string _idols, _fans;
        std::cin >> _idols >> _fans;
        idols = std::vector<char>(_idols.begin(), _idols.end());
        fans = std::vector<char>(_fans.begin(), _fans.end());
        int result = solve();

        std::cout << result << "\n";
    }

    return 0;
}