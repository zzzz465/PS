N = int(input())
M = int(input())
broken_buttons = list(map(int, input().split()))
available_buttons = sorted({1, 2, 3, 4, 5, 6, 7, 8, 9, 0} - set(broken_buttons))

# 1. 사용 가능한 수로 N이랑 최대한 가까운 수 만들기
