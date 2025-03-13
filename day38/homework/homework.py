#1
def fibonacci(n):
    fib_sequence = [0, 1]
    for i in range(2, n):
        next_num = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_num)
    return fib_sequence

print(fibonacci(10))

#2
def calculate_sum(x):
    total = 0
    for i in range(x + 1):
        total += i
    return total

print(calculate_sum(10)) 

