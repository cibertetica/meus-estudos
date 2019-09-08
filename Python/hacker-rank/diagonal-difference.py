def diagonalDifference(ar):
    l = r = 0
    for c in range(0, ar[-1] + 1, 4):
        print(c)
        c = l
        l *= c
    print(l)
    print()
    for c in range(2, ar[-1], 2):
        print(c)
        c = r
        r *= c
    print(r)

ar = [0, 1, 2, 3, 4, 5, 6, 7, 8]

diagonalDifference(ar)