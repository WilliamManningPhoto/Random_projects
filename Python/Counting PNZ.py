A = [3, -1, 0, 5, -2, 0, 7, 6, 2, -3, 0, -4, 1]

def positive_negative_zeros(A):
    Positive = 0
    Negative = 0
    Zeros = 0

    for number in A:
        if number > 0:
            Positive += 1
        elif number < 0:
            Negative += 1
        else:
            Zeros += 1
    print(Positive, Negative, Zeros)

positive_negative_zeros(A)