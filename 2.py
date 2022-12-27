# typed on phone
# Todo: check memoisation is working 
limit = 4000000

def fib(x, memo={}):
    if x <= 2:
        return 1
    if x in memo:
        return memo[x]
    return fib(x-1,memo) + fib(x-2, memo)

memo ={}

i = 1
res = 0
while True:
    n = fib(i,memo)
    print(n)
    if n >= limit: break
    if n % 2 == 0:
        res += n
    i += 1
print(n, res)
