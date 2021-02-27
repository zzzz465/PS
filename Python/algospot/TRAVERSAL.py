T = int(input())

def postfixPrint(prefix, infix):
    if len(prefix) == 0:
        return
    
    head = prefix[0]
    headIndex = infix.index(head)
    postfixPrint(prefix[1:headIndex + 1], infix[0:headIndex])
    postfixPrint(prefix[headIndex + 1:], infix[headIndex + 1:])

    print(head, end=" ")

for _ in range(T):
    N = int(input())
    prefixes = list(map(int, input().split()))
    infixes = list(map(int, input().split()))

    postfixPrint(prefixes, infixes)
    print()
