tmp = [[1 for i in range(21)] for i in range(21)]

for i in range(1,21):
    for j in range(1,21):
        tmp[i][j] = tmp[i-1][j] + tmp[i][j-1]

print tmp[20][20]
