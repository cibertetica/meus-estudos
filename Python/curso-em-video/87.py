# exercício 87
# aprimoração do exercício 86
# mostrar a soma de todos os valores pares na matriz, a soma dos valores na terceira coluna e o maior valor na segunda linha

matrix = [[], [], []]
even = []

for x in range(0, 3):
    for y in range(0, 3):
        value = (int(input(f'Digite um valor para [{x + 1}, {y + 1}]: ')))
        matrix[y].append(value)
        if value % 2 == 0:
            even.append(value)

third_amount = matrix[0][2] + matrix[1][2] + matrix[2][2] # soma dos valores da 3ª coluna

print(f'''
Matriz:

[ {matrix[0][0]} | {matrix[0][1]} | {matrix[0][2]} ]
[ {matrix[1][0]} | {matrix[1][1]} | {matrix[1][2]} ]
[ {matrix[2][0]} | {matrix[2][1]} | {matrix[2][2]} ]

Todos os valores pares informados foram {even} e a soma entre todos eles é {sum(even)}
A soma dos valores da terceira coluna {matrix[0][2], matrix[1][2], matrix[2][2]} é {third_amount}
O maior valor da segunda linha {matrix[1][0], matrix[1][1], matrix[1][2]} é {max(matrix[1])}

'''
)