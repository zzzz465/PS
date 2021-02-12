from typing import List


def solution(phone_book: List[str]):
    phone_book.sort(key= lambda x: len(x))

    for i in range(len(phone_book)):
        for j in range(i + 1, len(phone_book)):
            for k in range(len(phone_book[i])):
                if phone_book[i][k] != phone_book[j][k]:
                    break
            
            else:
                return False

    return True
