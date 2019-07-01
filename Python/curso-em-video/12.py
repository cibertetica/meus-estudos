# exercício 12
# cálculo de desconto de 5% de um produto

price = float(input('Informe o preço habitual do produto: R$ '))
newprice = price - (price * (5 / 100)) # cálculo de porcentagem e diminuição desse valor da porcentagem no valor na variável preço.
print(f'O produto no valor de R$ {price:.2f} com 5% de desconto fica R$ {newprice:.2f}. ')