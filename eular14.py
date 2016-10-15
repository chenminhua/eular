def collatz(n, count=1):
    while n > 1:
        count += 1
        if n % 2 == 0:
            n = n/2
        else:
            n = 3*n + 1
    return count

m = 0
res = 1
for i in range(1000000):
    c = collatz(i)
    if c > m:
        m = c
        res = i

print res
