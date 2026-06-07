A = [1, 2, 3, 4, 6, 7]

def count_even_numbers(A):
    count = 0
    for number in A:
        if number % 2 ==0:
            count += 1
    return count

print(count_even_numbers(A))  # Output: number of even numbers in the list A