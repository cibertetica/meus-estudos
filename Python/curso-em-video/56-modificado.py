# exercício 56
# analisador de dados de um grupo de pessoas
# faz a média de idades, nome da mulher mais velha e quantas pessoas têm menos de 20 anos

#INICIALIZAÇÃO DE VARIÁVEIS PARA O FOR
age_sum = age_media = oldest_woman = name_oldest = underage = n_underage = 0

for c in range(0, 5):
    print('-' * 5, f'{c + 1}ª Pessoa', '-' * 5)
    name = input('Nome:\n').strip().capitalize()
    age = int(input('Idade:\n'))

    # GÊNERO com verificação
    while True:
        gender = input('Gênero: [M] Masculino | [F] Feminino | [O] Outro\n').upper()[0] # letra maiúscula | usa apenas a primeira letra
        if gender in 'MFO':
            break
        print('Por favor, siga as instruções corretas para informar seu gênero.')
    
    # SOMA DE TODAS AS IDADES DIGITADAS PARA FAZER UMA MÉDIA
    age_sum += age # age_sum = age_sum + age

    # VERIFICAÇÃO PARA SABER O NOME DA MULHER MAIS VELHA
    if c == 1 and gender == 'F': # inicializa a primeira pessoa como mais velha
       oldest_woman = age
       name_oldest = name
    if age > oldest_woman: # verificação e comparação de todas as idades de mulheres
        oldest_woman = age
        name_oldest = name

    # VERIFICAÇÃO PARA SABER QUANTAS PESSOAS TÊM MENOS DE 20 ANOS
    if age <= 20:
        underage = age
        n_underage += 1 # n_underage = n_underage + 1 | faz a contagem de quantas pessoas têm menos de 20 anos

# CÁLCULO DA MÉDIA DAS IDADES
age_media = (age_sum) / 4
print(f'A média de idade desse grupo de pessoas é {age_media:.0f} anos.')

# QUANTAS PESSOAS SÃO MENORES DE 20 ANOS
if n_underage > 1:
    print(f'Nesse grupo existem {n_underage} pessoas menores de 20 anos.')
else:
    print(f'Nesse grupo existe {n_underage} pessoa menor de 20 anos.')

# NOME DA MULHER MAIS VELHA
print(f'{name_oldest} é a mulher mais velha com {oldest_woman} anos.')