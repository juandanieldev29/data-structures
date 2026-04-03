counter = 0


# Naive approach without using memoization

# def fib(n):
#     global counter
#     counter += 1
#     if n == 0 or n == 1:
#         return n
#     return fib(n - 1) + fib(n - 2)


# Optimized approach with memoization

memo = [None] * 100

def fib(n):
    global counter
    counter += 1

    if memo[n] is not None:
        return memo[n]
    
    if n == 0 or n == 1:
        return n
    
    memo[n] = fib(n - 1) + fib(n - 2)

    return memo[n]

n = 7

print('\nFib of ', n, '=', fib(n))
print('\nCounter ', counter)
