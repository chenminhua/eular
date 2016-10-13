#coding:utf8
def ispalindorm(n):
    s = str(n)
    return s == s[::-1]

l = []
for i in range(999,100,-1):
    for j in range(999,100,-1):
        if ispalindorm(i*j):
            l.append(i*j)

print max(l)
