def solution(A):
    N = len(A)
    seen = set()

    for x in A:
        if x < 1 or x > N or x in seen:
            return 0
        seen.add(x)

    return 1
