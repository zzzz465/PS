#include "iostream"
#include <stdio.h>

int main() {
    int T;
    std::cin >> T;
    for (int i = 0; i < T; i++) {
        int H, W, N; // 층수, 방수, 몇번째 손님인지
        std::cin >> H >> W >> N;

        if (H > 1 && W > 1) {
            
            if (N % H == 0) {
                printf("%d%02d\n", )
            }
            // std::string first, last;
        
            printf("%d%02d\n", front, back);
        } else {
            if (H == 1) {
                printf("%d%02d\n", 1, N);
            } else if (W == 1) {
                printf("%d01\n", N);
            }
        }
    }

    return 0;
}