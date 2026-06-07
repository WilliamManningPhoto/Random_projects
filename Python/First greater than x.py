A = [1, 4, 2, 8, 5]
X = 3

def first_greater_than_x(A, X):
    for index, value in enumerate(A):
        if value > X:
            return index
    return -1  # Return -1 if no element is greater than X

result = first_greater_than_x(A, X)
print(result)  # Output: 1