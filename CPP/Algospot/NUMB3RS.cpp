#include <iostream>
#include <vector>
#include <iomanip>
#include <cstring>
#include "algorithm"

std::vector< std::vector<int> > map;
std::vector<double> record;
int n, d, p; // 마을의 수, 지난 일 수, 교도소의 위치 p

// navie 한 방법은 n일에 도달했을때 확률의 합을 구하는 방법
// 최적화된 방법은 n-1 번째에 이곳에 도달할 확률 * n번째 도달할 확률을 구하는 것

int path_memo[50];

int availablePath(int index) {
    int& ret = path_memo[index];
    if (ret != -1) return ret;

    ret = 0;

    for (int i = 0; i < n; i++)
        if (map[index][i] == 1)
            ret += 1;

    return ret;
}

double memo[50][100]; // 50개의 마을을 100일동안 기록

// 반환값: day 날짜에 index에 도달할 확률
double optimizeFind(int index, int day) {
    if (day == 0) return index == p; // 기저사례: 0일차에는 이동 X, 1일차는 이미 기록을 해뒀음

    double& ret = memo[index][day];

    if (ret >= 0) return ret;

    ret = 0;

    for (int i = 0; i < n; i++) {
        // n일차는 i번째 마을에서 index 마을로 올 수 있을때, index 마을로 day -1 에 갈 확률 * index마을에서 여기로 올 확률
        if (map[index][i] == 1) // 여기에서 올 수 있음
            ret += optimizeFind(i, day - 1) / (float)availablePath(i);
    }

    return ret;
}

int find(int val, int day, double percentage) {
    if (day == d) {
        record[val] += percentage;
        return 0;
    }

    int count = 0; // 몇개의 선택지가 있는가?
    for (int i = 0; i < n; i++)
        if (map[val][i] == 1)
            count += 1;

    for (int i = 0; i < n; i++)
        if (map[val][i] == 1)
            find(i, day+1, percentage * (1.0 / (float)count));

    return 0;
}

int main() {
    int T;
    std::cin >> T;
    for (int i = 0; i < T; i++) {
        map.clear();
        record.clear();
        for (int i = 0; i < 50; i++)
            std::fill_n(memo[i], 100, -1.0);

        std::fill_n(path_memo, 50, -1.0);

        std::cin >> n >> d >> p;
        for (int j = 0; j < n; j++) {
            std::vector<int> v;
            record.push_back(0);
            for (int k = 0; k < n; k++) {
                int val;
                std::cin >> val;
                v.push_back(val);
            }
            map.push_back(v);
        }

/*
        // find(p, 0, 1);
        int pathFromJail = availablePath(p);
        float firstProb = 1.0 / (float)pathFromJail;
        for(int i = 0; i < n; i++) {
            if (map[i][p] == 1)
                memo[i][1] = firstProb;
            else
                memo[i][1] = 0;
        }
*/

        int c;
        std::cin >> c;
        std::cout << std::setprecision(8);
        for(int i = 0; i < c; i++) {
            int val;
            std::cin >> val;
            // double result = record[val];
            double result = optimizeFind(val, d);
            std::cout << result << " ";
        }
        std::cout << "\n";
    }

    return 0;
}