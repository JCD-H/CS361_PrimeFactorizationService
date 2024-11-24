def find_prime_factors(n):
    factors = []
    # Divide n by 2 until it is odd
    while n % 2 == 0:
        factors.append(2)
        n //= 2

    # Check for odd factors from 3 onwards
    factor = 3
    while factor * factor <= n:
        while n % factor == 0:
            factors.append(factor)
            n //= factor
        factor += 2

    # If n is still greater than 2, then it is a prime number
    if n > 2:
        factors.append(n)

    return factors

if __name__ == '__main__':
    print(find_prime_factors(26)) # a test