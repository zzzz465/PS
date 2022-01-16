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
from inspect import istraceback
from operator import truediv
from sys import maxsize
from typing import List

inpu

class Direction(Enum):
    EAST = 0
    SOUTH = 1
    WEST = 2
    NORTH = 3


@dataclass
class Position:
    x: int
    y: int
    type: int
    cost: int = maxsize
    direction: Direction = Direction.EAST
    visited = False
    in_queue = False

    # used by heapify
    def __lt__(self, other):
        return self.cost < other.cost

    # debug string

    def __repr__(self) -> str:
        return f'({self.y}, {self.x}), cost: {self.cost}, direction: {self.direction}'


def to_direction(value: int):
    if value == 1:
        return Direction.EAST
    elif value == 2:
        return Direction.WEST
    elif value == 3:
        return Direction.SOUTH
    elif value == 4:
        Direction.NORTH
    else:
        raise Exception()


# 세로 M, 가로 N
M, N = map(int, input().split())

grid: List[List[Position]] = []

for y in range(M):
    li = list()
    for x, type in enumerate(map(int, input().split())):
        li.append(Position(x, y, type))

    grid.append(li)

start_y, start_x, start_direction = map(int, input().split())
dest_y, dest_x, dest_direction = map(int, input().split())

start_y -= 1
start_x -= 1
dest_y -= 1
dest_x -= 1

pqueue = []

start_pos = grid[start_y][start_x]
start_pos.cost = 0
start_pos.direction = to_direction(start_direction)


def solve():
    heapq.heappush(pqueue, grid[start_y][start_x])

    while len(pqueue) > 0:
        pos = heapq.heappop(pqueue)

        # print(f'current node: {pos}')

        updateNode(pos)

        grid[y][x].in_queue = True
        grid[y][x].visited = True

        # fix broken by updating values
        heapq.heapify(pqueue)

    target_pos = grid[dest_y][dest_x]

    # calc rotation cost
    for rot in [-1, 0, 1, 2]:
        new_position = turn(target_pos.direction, rot)
        if Direction(new_position) == to_direction(dest_direction):
            target_pos.cost += abs(rot)

    print(grid[dest_y][dest_x].cost)


def updateNode(pos: Position):
    global pqueue

    y, x = pos.y, pos.x

    for rot in [0, -1, 1, 2]:
        for dist in [1, 2, 3]:
            newDirection = turn(pos.direction, rot)
            new_y, new_x = moveForward(y, x, newDirection, dist)

            if isValid(new_y, new_x, y, x) is not True:
                continue

            newPosition = grid[new_y][new_x]

            newCost = grid[y][x].cost + abs(rot) + 1  # before + rotation + move

            newPosition.cost = min(newCost, newPosition.cost)
            newPosition.direction = Direction(newDirection)

            if newPosition.in_queue is not True:
                heapq.heappush(pqueue, newPosition)
                newPosition.in_queue = True

            # print(f'updating adjacent node {newPosition}')


# what if value is -1????


def turn(direction: Direction, value: int) -> int:
    return (direction.value + value) & 0b11


def isValid(new_y: int, new_x: int, old_y: int, old_x: int) -> bool:
    posArr: List[Position] = getPositions(new_y, new_x, old_y, old_x)

    if posArr is None:
        return False

    for pos in posArr:
        if pos.type == 1:
            return False

    return True


def _validIndex(y: int, x: int) -> bool:
    global grid

    if y < 0 or y >= M:
        return False
    elif x < 0 or x >= N:
        return False

    return True


def getPositions(new_y: int, new_x: int, old_y: int, old_x: int):
    global grid

    pos = list()

    for y in range(min(old_y, new_y), max(old_y, new_y) + 1):
        for x in range(min(old_x, new_x), max(old_x, new_x) + 1):
            if _validIndex(y, x):
                pos.append(grid[y][x])
            else:
                return None

    return pos


def moveForward(y: int, x: int, direction: int, dist: int):
    if direction == Direction.EAST.value:
        return (y, x + dist)
    elif direction == Direction.WEST.value:
        return (y, x - dist)
    elif direction == Direction.SOUTH.value:
        return (y + dist, x)
    elif direction == Direction.NORTH.value:
        return (y - dist, x)
    else:
        raise Exception()


solve()
