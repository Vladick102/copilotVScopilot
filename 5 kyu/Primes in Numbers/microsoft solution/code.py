from collections import Counter

def prime_factors(n):
    def get_factors(n):
        i = 2
        factors = []
        while i * i <= n:
            if n % i:
                i += 1
            else:
                n //= i
                factors.append(i)
        if n > 1:
            factors.append(n)
        return factors
    
    factors = get_factors(n)
    count = Counter(factors)
    return ''.join(f'({factor}**{count[factor]})' if count[factor] > 1 else f'({factor})' for factor in sorted(count))