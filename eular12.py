import numpy as np
def get_divisors_num(n):
    sq = int(np.floor(np.sqrt(n)))
    tmp = 3
    for i in range(2,sq+1):
        if n%i == 0:
            tmp += 2
    if sq * sq == n:
        tmp -= 1
    return tmp

def main():
    i = 7
    cur = 28
    while True:
        if get_divisors_num(cur) > 500:
            print cur
            break
        i += 1
        cur += i

main()
