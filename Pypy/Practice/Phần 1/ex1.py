#1
def sum_two(a, b):
    return a + b
print(sum_two(3, 5))
#2
def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False
print(is_even(4))
print(is_even(7))
#3
def find_max(a, b, c):
    return max(a, b, c)
print(find_max(4, 9, 2))
#4
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n-1)
print(factorial(4))

