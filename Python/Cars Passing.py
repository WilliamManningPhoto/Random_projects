passes = 0
zeros = 0

for car in A:
    if car == 0:
        zeros += 1
    else:  # car == 1
        passes += zeros
