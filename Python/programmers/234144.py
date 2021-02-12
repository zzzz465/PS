import math

def solution(a, b):
    gcd = math.gcd(a, b)
    m = int((a / gcd) * (b / gcd)) * gcd

    return [gcd, m]
