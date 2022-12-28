# largest prime factor

# to optimise: for every factor found add all factors for that number and apply memoisation
factors_memo = {}
calc_count = 0

def factors(x):
    if x <= 0: return []
    if x == 1: return [1]
    global calc_count
    res_start = [1]
    res_end = [x]
    if x not in factors_memo:
        calc_count += 1
        if x > 3:
            for n in range(2,x//2+1):
                if x % n == 0:
                    if n in res_end: break
                    res_start.append(n)
                    n_pair = x//n
                    if n_pair not in res_start:
                        res_end.insert(0,n_pair)
        factors_memo[x] = res_start + res_end
    return factors_memo[x]

prime = {}
def isPrime(x):
    if x not in prime:
        prime[x] = len(factors(x)) == 2
    return prime[x]
    
print([n for n in factors(600851475143) if isPrime(n)][-1])
    
