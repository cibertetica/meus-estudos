# exercício 18
# cálculo de seno, cosseno e tangente.
#modifiquei um pouco o exercício atribuindo uma variável para a conversão de ângulo para radiano, para ficar mais legível

import math
angle = float(input('Informe um ângulo: '))
radian = math.radians(angle) # converte ângulo de graus para radianos
print(f'O valor do seno é {math.sin(radian):.2f}. ')
print(f'O valor do coseno é {math.cos(radian):.2f}. ')
print(f'O valor da tangente é {math.tan(radian):.2f}. ')