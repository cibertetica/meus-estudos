# exercício 69
# Mais um programa de análise de dados
# Cadastra idade e gênero de uma pessoa, ao final contabiliza quantas pessoas têm mais de 18 anos, quantas mulheres com menos de 20 anos e quantos homens foram cadastrados

amount = amount_older = amount_men = amount_women_younger = 0

print('Cadastro de pessoas\n')
while True:
    age = int(input('Idade: '))
    gender = input('Gênero: [M/F/O] ').upper().strip()[0]
    # caso a opção de gênero não seja informada corretamente
    while gender != 'F' and gender != 'M' and gender != 'O':
        print('Opção Inválida!')
        gender = input('Informe seu gênero de maneira correta:\n[M -> Masculino | F -> Feminino | O -> Outro] ').upper().strip()[0]
    
    # análise do montante de pessoas
    amount += 1 # número de pessoas cadastradas
    if age > 18:
        amount_older += 1
    if gender == 'M':
        amount_men += 1
    if gender == 'F' and age < 20:
        amount_women_younger += 1
    
    # continuar ou não o cadastro?
    continue_register = input('Continuar registro de pessoas? [S/N] ').upper().strip()[0]
    while continue_register != 'S' and continue_register != 'N':
        print('Opção inválida!')
        continue_register = input('Continuar registro de pessoas? [apenas S ou N] ').upper().strip()[0]
    if continue_register == 'N':
        break

# informações para serem mostradas no final
print(f''' 
Você cadastrou {amount} pessoas.
Cadastrou {amount_older} pessoas maiores de 18 anos.
Cadastrou {amount_men} homens.
Cadastrou {amount_women_younger} mulheres menores de 20 anos.
'''
)


