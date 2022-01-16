N = int(input())  # 3 <= N <= 40
free_seat_no = int(input())  # 1 <= K <= N

# 자유석이 없을 때를 생각해보자. -> 애초에 불가능하네.
# 자유석이 반드시 있어야 변화가 가능하다.
# 자유석에 미리 한명을 할당하면?

'''
N = 4 일 때... 8개

1 | 1 2 [_] 4 -> 자유석이 비어있음
2 | 2 1 [_] 4 -> 자리 바꾸기
3 | _ 2 [1] 4 -> 자유석에 1을 할당
4 | 2 _ [1] 4
5 | 1 _ [2] 4 -> 자유석에 2를 할당
6 | _ 1 [2] 4
7 | 1 2 [4] _ -> 자유석에 4를 할당
8 | 2 1 [4] _ -> 자유석에 4를 할당 + 자리바꾸기

자유석: 누군가를 할당 했거나, 안했거나
이를 제외하면 전부 같다?

K 에서의 경우의 수를 계산하기 위해선...
1. K-1 이 비었는가?
2. K+1 이 비었는가?

달리 말하면, K+1 에서 볼 때, K-2 와 K-1 을 보면 된다.

자유석을 특별하게 생각하지 말고, _ 인 사람이 앉았다고 생각하자.
이 때, 항상 왼쪽과만 자리를 바꾼다고 생각하자.

K 위치에서 경우의 수는 다음과 같다.
1. K-1 이 자리를 바꿨을 경우 -> 
'''


def solve():
    pass


solve()
