from dataclasses import dataclass
from typing import List, Set


def solve(N: int, M: int, broken_buttons: Set[int]):
    available_buttons: Set[int] = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9} - broken_buttons

    min_diff = abs(N - 100)

    for i in range(0, 700000):
        iStr = str(i)

        if len(set(map(int, iStr)) - available_buttons) > 0:
            continue

        diff = abs(N - i) + len(iStr)

        min_diff = min(min_diff, diff)

    # print(min_diff)

    return min_diff


def main():
    N = int(input())
    M = int(input())

    broken_buttons: Set[int] = set()

    if M > 0:
        broken_buttons = set(map(int, input().split()))

    return solve(N, M, broken_buttons)


test_case_raw = """
10
9
1 2 3 4 5 6 7 8 9
11

101
0
1

99
10
0 1 2 3 4 5 6 7 8 9
1

0
0
1

500000
6
0 1 2 3 4 5
166672

0
2
0 1
3

1555
8
0 1 3 4 5 6 7 9
670

944
7
2 3 4 5 6 7 9
59

6
9
0 2 3 4 5 6 7 8 9
6

500000
10
0 1 2 3 4 5 6 7 8 9
499900

101
10
0 1 2 3 4 5 6 7 8 9
1

1
9
1 2 3 4 5 6 7 8 9
2

99999
1
9
7

10
1
0
2

0
3
0 1 2
4

0
9
0 1 2 3 4 5 6 7 8
10

0
10
0 1 2 3 4 5 6 7 8 9
100

1
9
1 2 3 4 5 6 7 8 9
2

1020
0
4

10
2
0 1
2

999
1
9
5

9990
8
1 2 3 4 5 6 7 8
4

123
2
2 3
7

199
1
9
4

9
5
9 8 7 6 5
3

19
1
1
3

5959
4
1 2 3 4
4

56666
0
5

9999
8
0 1 2 3 4 5 6 7
4

10
1
1
2

190000
3
1 2 9
101117

123
3
1 2 5
23

1
9
0 1 2 3 4 5 6 7 8
9

100
10
0 1 2 3 4 5 6 7 8 9
0

99933
2
3 9
73

1023
5
1 2 3 4 0
27

91010
2
1 0
1016

383399
6
1 2 3 4 5 7
216607

6711
2
1 2
6

330
4
0 1 2 3
117

71923
5
4 5 6 7 9
8082

123123
3
1 2 3
23129

499999
2
4 8
7

1111
9
1 2 3 4 5 6 7 8 9
1011

1111
9
0 1 2 3 4 5 6 7 8
115

34311
8
0 1 2 3 4 5 6 7
24316


49445
7
1 2 3 4 5 6 7
30560

933
2
1 2
3

1617
3
1 2 3
621

856
2
5 6
10

1023
8
1 2 3 4 5 6 7 8
27

10900
2
1 0
905

394344
3
1 2 3
5662

99
1
8
1

101
9
0 1 2 3 4 5 6 7 8
1

2420
6
1 2 3 4 5 6
1424

991
1
1
4

30002
3
1 3 4
8

1698
2
6 9
6

499998
3
4 8 9
8

1022
5
1 2 3 4 5
26

1555
8
0 1 3 4 5 6 7 9
670

889
9
0 2 3 4 5 6 7 8 9
226
"""


@dataclass
class TestCase:
    N: int
    M: int
    broken_buttons: List[int]
    expected: int


def parse_test_case(raw: str) -> List[TestCase]:
    tcs = list(map(lambda x: x.strip().split("\n"), raw.split("\n\n")))

    cases: List[TestCase] = []

    for tc in tcs:
        Nstr = ""
        MStr = ""
        broken_buttons_str = ""
        expectedStr = ""

        if len(tc) == 4:
            NStr, MStr, broken_buttons_str, expectedStr = tc
        elif len(tc) == 3:
            NStr, MStr, expectedStr = tc
            broken_buttons_str = "-1"
        else:
            raise Exception()

        cases.append(TestCase(int(NStr), int(MStr), list(map(int, broken_buttons_str.split(" "))), int(expectedStr)))

    return cases


def run_tests(tcs: List[TestCase]) -> None:
    for tc in tcs:
        run_test(tc)


def run_test(tc: TestCase) -> None:
    print(f"running test: {tc}")

    res = solve(tc.N, tc.M, set(tc.broken_buttons))

    if res != tc.expected:
        raise Exception(f"expected: {tc.expected}, actual: {res}. tc: {tc}")
    else:
        print("OK")


tcs = parse_test_case(test_case_raw)
run_tests(tcs)
# print(main())
