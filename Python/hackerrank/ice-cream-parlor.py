import math
import os
import random
import re
import sys
from collections import defaultdict

def whatFlavors(cost, money):
    table = defaultdict(list)

    for i in range(len(cost)):
        price = cost[i]
        table[price].append(i + 1)

    keys = list(table.keys())
    result = [-1, -1]
    for price in keys:
        otherPrice = money - price
        if otherPrice in table:
            if otherPrice == price:
                result = sorted(table[price])[0:2]
            else:
                result = [min(table[price]), min(table[otherPrice])]

            break

    print(' '.join(map(str, sorted(result))))

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        money = int(input())

        n = int(input())

        cost = list(map(int, input().rstrip().split()))

        whatFlavors(cost, money)