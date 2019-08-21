# exercício 109
# aprimoração dos exercícios 107-108
# construindo função / módulo para formatação da moeda no formato de real

# programa principal

import calc110

money = float(input('Informe o preço: R$ '))
increment = int(input('Informe a porcentagem para aumento: '))
discount = int(input('Informe a porcentagem para o desconto: '))

calc110.resume(money, increment, discount)