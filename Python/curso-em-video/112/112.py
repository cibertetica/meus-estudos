# exercício 112
# validação de dados monetários no formato brasileiro
# fiz diferente do proposto no vídeo para não ter que usar o mesmo exemplo dos exercícios 108-111

from calc112 import discount
from format112 import real

n = real('Digite o preço: R$ ')
p = float(input('Digite a porcentagem de desconto: '))

print(f'O produto passará a custar {discount(n, p)}')