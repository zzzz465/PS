A = input()
B = input()

if len(A) > len(B):
    A, B = B, A

memo = dict()

def solve(AIndex: int, BIndex: int) -> int:
    if AIndex >= len(A) or BIndex >= len(B):
        return 0

    key = (AIndex, BIndex)

    if key not in memo:
        skip = solve(AIndex + 1, BIndex)
    
        val = A[AIndex]
    
        while BIndex < len(B) and B[BIndex] != val:
            BIndex += 1
    
        if BIndex == len(B):
            return skip
    
        take = solve(AIndex + 1, BIndex) + 1

        memo[key] = max(skip, take)
    
    return memo[key]

result = solve(0, 0)

print(result)