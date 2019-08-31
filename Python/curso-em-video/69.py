# exercício 69
# Mais um programa de análise de dados
# Cadastra idade e gênero de uma pessoa, ao final contabiliza quantas pessoas têm mais de 18 anos, quantas mulheres com menos de 20 anos e quantos homens foram cadastrados

amount = amount_older = amount_men = amount_women_younger = 0

print('Cadastro de pessoas\n')
while True:
    age = int(input('Idade: '))

    # tratamento do input de gênero
    while True:
        gender = input('Gênero: [M -> masculino | F -> feminino | O -> outro] ').upper()[0]
        if gender in 'MFO':
            break
        print('Opção inválida!')

    # análise do montante de pessoas
    amount += 1 # número de pessoas cadastradas
    if age > 18:
        amount_older += 1
    if gender == 'M':
        amount_men += 1
    if gender == 'F' and age < 20:
        amount_women_younger += 1
    
    # continuar ou não o cadastro?
    while True:
        continue_register = input('Continuar registro de pessoas? [S/N] ').upper()[0]
        if continue_register in 'SN':
            break
        print('Opção inválida!')
    if continue_register == 'N':
        break

# informações mostradas no final
print(f''' 
Você cadastrou {amount} pessoas.
Cadastrou {amount_older} pessoas maiores de 18 anos.
Cadastrou {amount_men} homens.
Cadastrou {amount_women_younger} mulheres menores de 20 anos.
'''
)