#include <iostream>
#include <string>
#include <vector>
#include <cstring>

std::vector<int> numA, numB;
int lenA, lenB, num;

int memo[100+1][100+1];

int solve(int indexA, int indexB) {
    if ((indexA > lenA) || (indexB > lenB))
        return 0;

    int valA = numA.at(indexA);
    int valB = numA.at(indexB);

    if (memo[indexA][indexB] == -1) {
        int result = 0;

        for (int newIndexA = indexA + 1; newIndexA <= lenA; newIndexA++) {
            int newVal = numA.at(newIndexA);
            if ((newVal > valA) && (newVal > valB))
                result = std::max(result, solve(newIndexA, indexB));
        }

        for (int newIndexB = indexB + 1; newIndexB <= lenB; newIndexB++) {
            int newVal = numB.at(newIndexB);
            if ((newVal > valA) && (newVal > valB))
                result = std::max(result, solve(indexA, newIndexB));
        }

        memo[indexA][indexB] = result;
    }

    return memo[indexA][indexB] + 1;
}

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    int N;
    std::cin >> N;
    for (int i = 0; i < N; i++) {
        numA.clear();
        numB.clear();
        std::cin >> lenA >> lenB;

        for (int i = 0; i < lenA; i++) {
            std::cin >> num;
            numA.push_back(num);
        }
        
        for (int i = 0; i < lenB; i++) {
            std::cin >> num;
            numB.push_back(num);
        }

        memset(memo, -1, sizeof(memo));

        int result = 0;

        for (int i = 0; i <= lenA; i++)
            for (int j = 0; j <= lenB; j++)
                result = std::max(result, solve(i, j) - 1);

        std::cout << result << std::endl; // 랙?
    }

    return 0;
}