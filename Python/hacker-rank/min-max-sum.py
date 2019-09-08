def miniMaxSum(arr):
    lower = sum(arr) - max(arr)
    higher = sum(arr) - min(arr)
    print(lower, higher)

arr = [1, 2, 3, 4, 5]

print(miniMaxSum(arr))