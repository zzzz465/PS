#include <iostream>
#include <vector>

using namespace std;

int N;
const int max_size = 16;
int board[max_size][max_size];

bool isValid(int y, int x) {
    return 0 <= y && y < N && 0 <= x && x < N;
}

// 일단 밀고, 그다음 각도(머릿쪽) 을 수정하는 것 만 가능
// 밀면서 회전 가능, 미는 방향은 오른쪽, 아래, 오른쪽 아래 대각선 방향
// 가로 or 세로는 가로방향 or 세로방향으로 밀거나, 밀고 회전시키거나
// 대각선은 밀거나(45도), 밀고 가로/세로로 회전시키거나

bool canPush(int pos[2][2]) {
    // 이전 + 이후
    int tailY, tailX, headY, headX;
    headY = pos[1][1];
    headX = pos[1][0];
    tailY = pos[0][1];
    tailX = pos[0][0];
    if (isValid(headY, headX) && isValid(tailY, tailX)) {
        if (headY == tailY) { // y가 같음 -> 가로
            return board[headY][headX] != 1;
        } else if (headX == tailX) { // x가 같음 -> 세로
            return board[headY][headX] != 1;
        } else {
            return board[headY - 1][headX] != 1 && board[headY][headX - 1] != 1 && board[headY][headX] != 1;
        }
    }

    return false;
}

int totalCount = 0;

void solve(int pos[2][2]) {
    // pos[0] -> 머리, pos[1] -> 꼬리
    // 머리, 꼬리에서 x, y 순으로 배열
    int& headY = pos[1][1];
    int& headX = pos[1][0];
    int& tailY = pos[0][1];
    int& tailX = pos[0][0];
    if (headY == N - 1 && headX == N - 1) {
        // 종료조건
        totalCount += 1;
        return;
    }

    if (headY == tailY) { // y가 같음 -> 가로
        // 오른쪽 밀기
        headX += 1;
        tailX += 1;
        if (canPush(pos)) {
            solve(pos);
        }

        // 대각선 y 밀기
        headY += 1;
        if (canPush(pos))
            solve(pos);

        // 원상복귀
        headY -= 1;

        // 원상복귀
        headX -= 1;
        tailX -= 1;
    } else if (headX == tailX) { // x가 같음 -> 세로
        // 아래 밀기
        headY += 1;
        tailY += 1;

        if (canPush(pos))
            solve(pos);

        // 대각선 x 밀기(45도)
        headX += 1;

        if (canPush(pos))
            solve(pos);

        headX -= 1;

        headY -= 1;
        tailY -= 1;
    } else { // 둘다 아님 -> 대각선
        // 대각선 밀기
        headX += 1;
        headY += 1;
        tailX += 1;
        tailY += 1;

        if (canPush(pos))
            solve(pos);

        headY -= 1; // 윗쪽으로 45도
        if (canPush(pos))
            solve(pos);

        headY += 1;

        headX -= 1; // 아래로 45도
        if (canPush(pos))
            solve(pos);
        headX += 1;

        headX -= 1;
        headY -= 1;
        tailX -= 1;
        tailY -= 1;
    }
}

int main() {
    cin >> N;

    for (int i = 0; i < max_size; i++)
        for (int j = 0; j < max_size; j++)
            board[i][j] = 0;

    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            int val; cin >> val;
            board[i][j] = val;
        }
    }

    int initial[2][2];
    initial[0][0] = 0;
    initial[0][1] = 0;
    initial[1][0] = 1;
    initial[1][1] = 0;

    solve(initial);

    cout << totalCount << "\n";

    return 0;
}