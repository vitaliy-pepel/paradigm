
numbers = [8, 3, 5, 7, 6, 4, 9]

def sort_list_imperative(numbers):
    n = len(numbers)
    for i in range(n):
        for j in range(0, n-i-1):
            if numbers[j] < numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
    return numbers

print(sort_list_imperative(numbers))


def sort_list_declarative(numbers):
    return sorted(numbers, reverse=True)

print(sort_list_declarative(numbers))