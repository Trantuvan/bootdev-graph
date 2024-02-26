import math
def prime_factors(n):
    results = []
    
    while n % 2 == 0:
        n //= 2
        results.append(2)
    
    for i in range(3, math.floor(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            n //= i
            results.append(i)

    if n > 2:
        results.append(n)

    return results

print(prime_factors(63))
