A = [1,3,6,4,1,2]
def smallest_missing_integer(A):
    n = len(A)
    present = [False] * (n + 1)

    for number in A:
        if 1 <= number <= n:
            present[number] = True

    for i in range(1, n + 1):
        if not present[i]:
            return i

    print(n + 1)