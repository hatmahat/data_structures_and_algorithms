def fac(n):
    if n >= 1:
        return n*fac(n-1)
    else:
        return 1

print(fac(5))
print(fac(4))
print(fac(3))
print(fac(2))
print('-----')

def fib(n):
    if n >= 3:
        return fib(n-1) + fib(n-2)
    else:
        return 1

print(fib(4))
print(fib(5))
print(fib(6))
print('-----')

# A memoized solution
def fib_2(n, memo):
    if memo[n] is not None:
        return memo[n]
    if n == 1 or n == 2:
        result = 1
    else:
        result = fib_2(n-1, memo) + fib_2(n-2, memo)
    memo[n] = result
    return result

def fib_memo(n):
    memo = [None] * (n + 1)
    return fib_2(n, memo)

print(fib_memo(4))
print(fib_memo(5))
print(fib_memo(6))

def fib_bottom_up(n):
    if n == 1 or n == 2:
        return 1
    bottom_up = [None] * (n+1)
    bottom_up[1] = 1
    bottom_up[2] = 1
    for i in range(3, n+1):
        bottom_up[i] = bottom_up[i-1] + bottom_up[i-2]
    return bottom_up[n]

print([0]*3)
print([None]*3)