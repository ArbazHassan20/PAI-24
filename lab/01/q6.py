def product(lst):
    result = 1
    for i in lst:
        result *= i
    return result

# Example list of numbers
numbers = [1, 3, 5, 7, 9]
print(product(numbers))
