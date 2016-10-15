'''
1901 jan 1 to 31 dec 2000
how many sundays fell on the first of the month
'''

from datetime import datetime
res = 0
for i in range(1901, 2001):
    for j in range(1, 13):
        if datetime(i,j,1).weekday() == 6: #0 monday,  6 sunday
            res += 1
print res
