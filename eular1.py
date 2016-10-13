#coding:utf8
#If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
#Find the sum of all the multiples of 3 or 5 below 1000.
#所有三的倍数+所有五的倍数-所有十五的倍数
all3 = [n for n in range(1,1000) if n%3==0]
all5 = [n for n in range(1,1000) if n%5==0]
all15 = [n for n in range(1,1000) if n%15==0]
print sum(all3) + sum(all5) - sum(all15)
