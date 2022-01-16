'''
https://www.acmicpc.net/problem/1726 첫 번째 시도는 다익스트라를 이용했는데, 실패한 이유가 무엇인가?
'''
from cmath import cos
import collections
from dataclasses import dataclass
from enum import Enum
from sys import maxsize

M, N = map(int, input().split())


class ValueType(Enum):
    VALID = 0
    INVALID = 1


@dataclass
class Node:
    y: int
    x: int
    valueType: ValueType
    # cost = maxsize


class Direction(Enum):
    EAST = 0
    SOUTH = 1
    WEST = 2
    NORTH = 3


def to_direction(value: int):
    if value == 1:
        return Direction.EAST
    elif value == 2:
        return Direction.WEST
    elif value == 3:
        return Direction.SOUTH
    elif value == 4:
        return Direction.NORTH
    else:
        raise Exception()


grid = list()
costMemo = collections.defaultdict(lambda: ([maxsize] * 4))

def cost_memo_key(y: int, x: int):
    return (y, x)

# returns minimum value???
def get_memoized_value(y: int, x: int, direction: Direction):
    global costMemo

    key = cost_memo_key(y, x)
    
    return costMemo[key][direction.value]

def set_memoized_value(y: int, x: int, value: int, direction: Direction):
    global costMemo

    key = cost_memo_key(y, x)

    for rot in [0, -1, 1, 2]:
        new_direction = rotate(direction, rot)
        rotation_cost = abs(rot)

        costMemo[key][new_direction.value] = min(costMemo[key][new_direction.value], value + rotation_cost)

for y in range(M):
    line = []
    for x, valueType in enumerate(map(int, input().split())):
        line.append(Node(y, x, ValueType(valueType)))

    grid.append(line)

start_y, start_x, start_direction = map(int, input().split())
dest_y, dest_x, dest_direction = map(int, input().split())

# 1-based to 0-based
start_y -= 1
start_x -= 1
dest_y -= 1
dest_x -= 1
start_direction = to_direction(start_direction)
dest_direction = to_direction(dest_direction)

queue = collections.deque()


def solve():
    start_node = grid[start_y][start_x]
    # start_node.cost = 0
    queue.append((start_node, 0, start_direction))

    node: Node
    direction: Direction
    cost: int

    result_cost = maxsize

    while len(queue) > 0:
        node, cost, direction = queue.popleft()

        if node.y == dest_y and node.x == dest_x:
            cost += calculate_rotation_cost(dest_direction, direction)
            result_cost = min(result_cost, cost)
        else:
            update_adjacent_node(node, direction, cost)

    print(result_cost)

def calculate_rotation_cost(to: Direction, base: Direction):
    for rot in [0, -1, 1, 2]:
        new_direction = rotate(base, rot)
        if new_direction == to:
            return abs(rot)


def update_adjacent_node(node: Node, direction: Direction, cost: int):
    global grid, queue, costMemo

    for distance in [1, 2, 3]:
        for rotation in [0, 1, -1, 2]:
            new_direction = rotate(direction, rotation)
            new_position = move(node.y, node.x, new_direction, distance)

            if is_valid_move(new_position[0], new_position[1], node.y, node.x) is not True:
                continue

            other_node = grid[new_position[0]][new_position[1]]
            new_cost = cost + abs(rotation) + 1

            memoized_cost = get_memoized_value(*new_position, new_direction)
            if new_cost < memoized_cost:
                set_memoized_value(*new_position, new_cost, new_direction)
                queue.append((other_node, new_cost, new_direction))

            # print(
                # f'updating node: {(other_node.y, other_node.x)}, cost: {new_cost}, direction: {new_direction}')


def move(y: int, x: int, direction: Direction, distance: int):
    if direction == Direction.NORTH:
        return y - distance, x
    elif direction == Direction.SOUTH:
        return y + distance, x
    elif direction == Direction.WEST:
        return y, x - distance
    elif direction == Direction.EAST:
        return y, x + distance
    else:
        raise Exception()


def rotate(before: Direction, rotation: int) -> Direction:
    value = (before.value + rotation) & 0b11

    return Direction(value)


def is_valid_move(new_y: int, new_x: int, old_y: int, old_x: int) -> bool:
    nodes = get_nodes_in_range(new_y, new_x, old_y, old_x)

    if nodes is None:
        return False

    for node in nodes:
        if node.valueType == ValueType.INVALID:
            return False

    return True


def get_nodes_in_range(to_y: int, to_x: int, from_y: int, from_x: int):
    global grid

    nodes = []

    for y in range(min(from_y, to_y), max(from_y, to_y) + 1):
        for x in range(min(from_x, to_x), max(from_x, to_x) + 1):
            if is_valid_index(y, x) is not True:
                return None

            node = grid[y][x]
            nodes.append(node)

    return nodes


def is_valid_index(y: int, x: int) -> bool:
    global M, N

    if y < 0 or y >= M:
        return False
    elif x < 0 or x >= N:
        return False

    return True


solve()
