A = 2452

Zero_Count = 0
Max_Zero_Count = 0

B = bin(A)
print(B)

for i in bin(A)[2:]:
    if i == '0':
        Zero_Count += 1
    else:
        if Zero_Count > Max_Zero_Count:
            Max_Zero_Count = Zero_Count
        Zero_Count = 0
print(Max_Zero_Count)