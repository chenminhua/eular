def get_value(s):
    return sum([ord(c)-64 for c in s])

with open('p022_names.txt') as f:
    names = f.read().split(",")
    names = [n[1:-1] for n in names]
    names = sorted(names)

res = 0
for i,v in enumerate(names):
    res += (i+1) * get_value(v)
print res
