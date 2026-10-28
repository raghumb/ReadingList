# Pow(x, n)
# O(logn)

def myPow(x, n):

    result = 1.0

    # Handle negative exponent
    if n < 0:
        x = 1 / x
        n = -n

    # Stop, when n becomes zero
    while n > 0:

        # If exponent is odd, multiply result by x
        if n % 2 == 1:
            result *= x

        # Square the base
        x *= x

        # Divide exponent by 2
        n //= 2

    return result


print(myPow(2, 10))
print(myPow(2, -2))
print(myPow(2, 3))
