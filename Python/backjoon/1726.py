'''
https://www.acmicpc.net/problem/1726

목표: 명령으로 로봇 제어해서, 특정 위치로 가는 것 + 특정 방향 바라보기

1. Go k (k 는 1, 2, 3)
    현재 위치에서 바라보는 방향으로 k 칸 이동

2. Turn dir (dir 는 left | right)
    왼쪽 / 오른쪽 90도 회전

그리드인데, 0 과 1 이 있고, 0은 갈 수 있고, 1는 갈 수 없다.

그리드 크기: 최대 100x100

약간 변형이 되어있는 길찾기(다익스트라? BFS? DFS?) 문제가 아닌가?
기억 안나요: https://namu.wiki/w/%EB%8B%A4%EC%9D%B5%EC%8A%A4%ED%8A%B8%EB%9D%BC%20%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98#s-3
'''

from dataclasses import dataclass
from enum import Enum
import heapq
from operator import truediv
from sys import maxsize
from typing import List

class Direction(Enum):
    EAST = 0
    WEST = 1
    SOUTH = 2
    NORTH = 3

@dataclass
class Position:
    x: int
    y: int
    cost: int = maxsize
    direction: Direction = Direction.EAST
    visited = False
    in_queue = False

    # used by heapify
    def __lt__(self, other):
        return self.cost < other.cost

    # debug string

    def __repr__(self) -> str:
        return f'({self.y}, {self.x}), valid: {isValid(self.y, self.x)}, cost: {self.cost}, direction: {self.direction}'

# 세로 M, 가로 N
M, N = map(int, input().split())

grid: List[List[Position]] = []

for y in range(M):
    li = list()
    for x, value in enumerate(map(int, input().split())):
        li.append(Position(x, y, value))

    grid.append(li)

start_y, start_x, start_direction = map(int, input().split())
dest_y, dest_x, dest_direction = map(int, input().split())

pqueue = []

def solve():
    heapq.heappush(pqueue, grid[start_y][start_x])

    while len(pqueue) > 0:
        pos = heapq.heappop(pqueue)

        print(f'current node: ${pos}')

        updateNode(pos)

        grid[y][x].in_queue = True
        grid[y][x].visited = True

        if y == dest_y and x == dest_x:
            break

        # fix broken by updating values
        heapq.heapify(pqueue)
    
    print(grid[dest_y][dest_x].cost)

def updateNode(pos: Position):
    global pqueue

    y, x = pos.y, pos.x

    for rot in [0, -1, 1, 2]:
        newDirection = turn(pos.direction, rot)
        new_y, new_x = moveForward(y, x, newDirection)

        if isValid(new_y, new_x) is not True:
            continue

        newPosition = grid[new_y][new_x]

        newCost = grid[y][x].cost + abs(rot)

        newPosition.cost = min(newCost, newPosition.cost)
        newPosition.direction = newDirection

        if newPosition.in_queue is not True:
            heapq.heappush(pqueue, newPosition)
            newPosition.in_queue = True

        print(f'updating adjacent node ${newPosition}, cost: ${newCost}')

# what if value is -1????
def turn(direction: Direction, value: int) -> int:
    return (direction.value + value) & 0b11

def isValid(y: int, x: int) -> bool:
    if y < 0 or y >= M:
        return False
    elif x < 0 or x >= N:
        return False
    elif grid[y][x] == 1:
        return False

    return True

def moveForward(y: int, x: int, direction: int):
    if direction == Direction.EAST.value:
        return (y, x + 1)
    elif direction == Direction.WEST.value:
        return (y, x - 1)
    elif direction == Direction.SOUTH.value:
        return (y - 1, x)
    elif direction == Direction.NORTH.value:
        return (y + 1, x)
    else:
        raise Exception()

solve()
