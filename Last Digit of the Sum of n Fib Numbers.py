def fib_sum(a):
    # Principle used : Sum of the first n Fibonacci numbers  = fib(n+2) - 1
    a += 3
    arr = [0] * a
    arr[0], arr[1] = 0, 1
    for i in range(2, a):
        arr[i] = arr[i - 1] + arr[i - 2]
    return (arr[-1] - 1) % 10
