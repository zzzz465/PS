N = int(input())

def normalize(text):
    result = []
    wildcard = False
    for char in text:
        if char == '*':
            if not wildcard:
                wildcard = True

        else:
            if wildcard:
                result.append('*')
                wildcard = False
            result.append(char)

    if wildcard:
        result.append('*')

    return ''.join(result)

def solve(regex, text):
    index = 0
    while (index < len(regex) and index < len(text)) and (regex[index] == text[index] or regex[index] == '?'):
        index += 1

    if index == len(regex):
        return len(text) == index

    if regex[index] == '*':
        skip = 0
        while skip + index <= len(text):
            if (solve(regex[index + 1:], text[index + skip:])):
                return True

            skip += 1

        return False

    return False

for _ in range(N):
    regex = normalize(input())
    cases = int(input())

    results = []

    for i in range(cases):
        text = input()

        result = solve(regex, text)
        if (result):
            results.append(str(text))

    print('\n'.join(sorted(results)))

