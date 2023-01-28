# Напишите функцию, которая в качестве параметра принимает число n и отображает n первых чисел Фибоначчи, не считая 0.
# Sample Input:
# 3
# Sample Output:
# 0 1 1 2

fib1 = fib2 = 1

n = int(input())

print(fib1, fib2, end=' ')

for i in range(2, n):
    fib1, fib2 = fib2, fib1 + fib2
    print(fib2, end=' ')