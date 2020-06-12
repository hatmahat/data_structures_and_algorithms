def linear_sum(S, n):
    """Return the sum of the first n numbers of sequence S."""
    if n == 0:
        return 0
    else:
        return linear_sum(S, n-1) + S[n-1]

def reverse(S, start, stop):
    """Return reverse element in implicit slice S[start:stop]"""
    if start < stop - 1 :                           # implicit range is not empty or the implicit range has not 
        S[start], S[stop-1] = S[stop-1], S[start]   # only one element
        reverse(S, start+1, stop-1)
    return S

def power(x, n):
    """Compute the value x**n for integer n."""
    if n == 0:
        return 1                    # base case
    else:
        return x * power(x, n-1)

def power_eff(x, n):
    """Compute the value x**n for integer n."""
    if n == 0:
        return 1
    else:
        partial = power(x, n//2)        # rely on truncated divison
        result = partial*partial        
        if n % 2 == 1:                  # if n odd, include extra factor of x
            result *= x
        return result

# TESTING
arr1 = [4, 3, 6, 2, 8, 9, 3, 2, 8, 5, 1, 7, 2, 8, 3, 7]
arr2 = [4, 3, 6, 2, 8, 9, 5]

print(linear_sum(arr1, 4))
print(linear_sum(arr2, 2))

print(reverse(arr1, 0, len(arr1)))
print(reverse(arr2, 0, len(arr2)))

print(power(3, 3))
print(power(2, 1))