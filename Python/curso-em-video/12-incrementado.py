# mesmo exercício 12 mas adicionei uma opção para escolher qual a porcentagem de desconto

price = float(input('Informe o preço habitual do produto: R$ '))
discount = int(input('Informe a porcentagem de desconto a ser atribuída: '))
newprice = price - (price * (discount / 100))
print(f'O produto no valor de R$ {price:.2f} com {discount}% de desconto fica R$ {newprice:.2f}. ')