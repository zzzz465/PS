#include "iostream"
#include "list"

void solve() {
    int N, K;
    std::cin >> N >> K;

    std::list<int> survivors;
    for (int i = 1; i <= N; i++)
        survivors.push_back(i);

    int size = N;
    auto iterator = survivors.begin();
    while (size > 2) {
        /*
        std::cout << "Before: ";
        for (int i : survivors)
            std::cout << i << " ";
        std::cout << "\n";
        */

        // int val = *iterator;
        // std::cout << "suicide: " << val << "\n";
        if (iterator != --survivors.end()) {
            iterator = survivors.erase(iterator); // iterator 가 arg로 들어가고, iterator는 ++ 된다음 erase 함수 실행
        } else {
            survivors.erase(iterator);
            iterator = survivors.begin();
        }
        size -= 1;

        /*
        std::cout << "After: ";
        for (int i : survivors)
            std::cout << i << " ";
        std::cout << "\n";
        */
        
        // std::cout << "pointing: " << *iterator << "\n";
        for (int i = 0; i < K - 1; i++)
            if (++iterator == survivors.end())
                iterator = survivors.begin();
    }

    for(int i : survivors)
        std::cout << i << " ";
    std::cout << "\n";
}

int main() {
    int T;
    std::cin >> T;

    for (int i = 0; i < T; i++)
        solve();

    return 0;
}