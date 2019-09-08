def compareTriplets(a, b):
    alice = bob = 0
    for c in range(0, 3):
        if a[c] > b[c]:
            alice += 1
        elif a[c] == b[c]:
            pass
        else:
            bob += 1
    points = [alice, bob]
    return points

a = [5, 6, 7]
b = [3, 6, 10]

print(compareTriplets(a, b))