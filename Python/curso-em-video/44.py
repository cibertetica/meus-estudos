# exercício 44 
# cálculo de formas de pagamento e seus devidos descontos

price = float(input('Preço das compras: R$ '))

print(
'''
FORMAS DE PAGAMENTO:
[1] à vista em dinheiro ou cheque
[2] à vista no cartão
[3] 2x no cartão
[4] 3x ou mais no cartão
'''
)
option = int(input('Qual é a opção? '))

if option == 1:
    discount = price * (10/100)
    total = price - discount
    print(f'O preço fica R$ {total:.2f}. ')
    print(f'Desconto de R$ {discount:.2f}. ')
elif option == 2:
    discount = (price * (5/100))
    total = price - discount
    print(f'O preço fica R$ {total:.2f}. ')
    print(f'Desconto de R$ {discount:.2f}. ')
elif option == 3:
    parcel = price / 2
    print(f'O preço fica R$ {price:.2f}. ')
    print(f'Parcelado em 2x de R$ {parcel:.2f}. ')
    print(f'Sem descontos ou acréscimos. ')
elif option == 4:
    addition = (price * (20/100))
    total = price + addition
    parcel = total / 3
    print(f'O preço fica R$ {total:.2f}.')
    print(f'Parcelado em 3x de R$ {parcel:.2f}')
    print(f'Acréscimo de R$ {addition:.2f}. ')
else:
    print('Opção inválida!')