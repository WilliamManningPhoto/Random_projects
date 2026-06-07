A = [1, 1, 2, 2, 2, 3, 1, 1]

def longest_run(A):
    if not A:
        return 0

    max_run_length = 1
    current_run_length = 1

    for i in range(1, len(A)):
        if A[i] == A[i - 1]:
            current_run_length += 1
        else:
            max_run_length = max(max_run_length, current_run_length)
            current_run_length = 1

    max_run_length = max(max_run_length, current_run_length)
    return max_run_length

print(longest_run(A))