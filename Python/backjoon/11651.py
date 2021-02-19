N = int(input())

points = [None] * N
for i in range(N):
    a, b = map(int, input().split())
    points[i] = (b, a)

for b, a in sorted(points):
    print(f'{a} {b}')