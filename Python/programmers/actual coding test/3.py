from collections import deque

def solution(K, A):
    results = []
    for i in A:
        q = deque()
        for 