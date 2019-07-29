# exercício 86
# matriz em python

matrix = [ [], [], []]

for x in range(0, 3): # x = horizontal | y = vertical
    for y in range(0, 3):
        matrix[y].append(int(input(f'Digite um valor para [{x + 1}, {y + 1}]: ')))

print(f'''
Matriz:

[ {matrix[0][0]} | {matrix[0][1]} | {matrix[0][2]} ]
[ {matrix[1][0]} | {matrix[1][1]} | {matrix[1][2]} ]
[ {matrix[2][0]} | {matrix[2][1]} | {matrix[2][2]} ]
'''
)
