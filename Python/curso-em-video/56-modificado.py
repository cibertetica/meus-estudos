# exercício 56
# analisador de dados de um grupo de pessoas
# faz a média de idades, nome da mulher mais velha e quantas pessoas têm menos de 20 anos

#INICIALIZAÇÃO DE VARIÁVEIS PARA O FOR
age_sum = 0 # soma da idade
age_media = 0 # média da idade
oldest_woman = 0 # mulher mais velha
name_oldest = 0 # nome da mulher mais velha
underage = 0 # menores de idade
n_underage = 0 # número de maiores de idade

for c in range(1, 5):
    print('-' * 5, f'{c}ª Pessoa', '-' * 5)
    name = input('Nome:\n').strip().capitalize()
    age = int(input('\nIdade:\n'))
    gender = input(
'''
Gênero: 
[M] Masculino
[F] Feminino
[O] Outro
'''
    ).strip() # ignora espaços que podem ser digitados pelo usuário

    # VERIFICAÇÃO DA INFORMAÇÃO GÊNERO
    gender = gender.upper() # coloca tudo em letras maiúsculas para ajudar a identificar se o gênero está informado corretamente
    if gender != 'M' and gender != 'F' and gender != 'O': # verificação se o gênero está informado corretamente
        print('Por favor, siga as instruções corretas para informar seu gênero. Aceito apenas as opções \"M\", \"F\" e \"O\"')
    
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