def sockMerchant(array):
    pair = 0
    elements = [] # creating new list to deal with duplicates
    for c in array:
        if c not in elements:
            repeat = array.count(c)
            pair += repeat // 2
        elements.append(c)
    del(elements) # deleting list
    return pair
    
        
n = int(input('How many socks John have? '))
ar = [] # list of socks

print('Color sock guide:\n1 - black\n2 - white\n3 - green\n4 - red\n')

for c in range(0, n):
    try:
        ar.append(int(input(f'What is the color of sock in position {c}? ')))
    except:
        print('Data error. Try again.')

pair = sockMerchant(ar)
print(f'There\'s {pair} pairs.')
