#include <iostream>
#include <queue>
#include <vector>
#include <cmath>

long long A = 1983;
long long reminder = (long long)std::pow(2, 32);

long long getSignal() {
    long long temp = A;
    A = (A * 214013) % reminder;
    A += 2531011;
    A %= reminder;
    return (temp % 10000) + 1;
}

void clear() {
    A = 1983;
}

int main() {
    int C;
    std::cin >> C;
    for (int i = 0; i < C; i++) {
        int K, N;
        std::cin >> K >> N;
        clear();

        int count = 0;

        std::queue<long long> q;
        int sum = 0;
        
        for (int j = 0; j < N; j++) {
            int next = getSignal();
            sum += next;
            q.push(next);
    
            if (sum == K) {
                count += 1;
            }
    
            while (sum >= K && q.size() > 0) {
                long long front = q.front();
                q.pop();
                sum -= front;

                if (sum == K)
                    count += 1;
            }
        }


        std::cout << count << "\n";
    }

    return 0;
}