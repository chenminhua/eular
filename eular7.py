#coding:utf8
#如果一个数是质数，它必定不能被其他质数整除，如果一个数是合数，它必定有一个质数的约数
def prime(n):
    count = 1
    primes = [2]
    tmp = 3
    while count < n:
        if all(tmp % prime != 0 for prime in primes):
            primes.append(tmp)
            count += 1
        tmp+=2
    print primes[-1]
prime(10001)
