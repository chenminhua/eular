def main():
    for i in range(1,1000):
        for j in range(1,1000-i):
            k = 1000 - i -j
            a,b,c = sorted([i,j,k])
            if a**2 + b**2 == c**2:
                print a*b*c
                return
main()
