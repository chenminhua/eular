res = 1
def gcd(a, b):
    if a < b:
        a, b = b, a
    y = a % b
    if y == 0:
        return b
    else:
        a, b = b, y
        return gcd(a,b)

for n in range(2,21):
    res = res * n / gcd(res, n)

print res
