# exercício 56
# analisador de dados de um grupo de pessoas
# faz a média de idades, nome da mulher mais velha e quantas pessoas têm menos de 20 anos

#INICIALIZAÇÃO DE VARIÁVEIS PARA O FOR
age_sum = 0 # soma da idade
age_media = 0 # média da idade
oldest_woman = 0 # mulher mais velha
name_oldest = 0 # nome da mulher mais velha
underage = 0 # menores de idade
ofage = 0 # maiores de idade

for c in range(1, 5):
    print('-' * 5, f'{c}ª Pessoa', '-' * 5)
    name = input('Nome:\n').strip()
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
    if c == 1 and gender == 'F':
       oldest_woman = ofage
       ofage = age
       name_oldest = name
    if age > ofage:
        oldest_woman = ofage
        name_oldest = name
    elif age < ofage:
        underage = ofage

    # VERIFICAÇÃO PARA SABER QUANTAS PESSOAS TÊM MENOS DE 20 ANOS
    

# CÁLCULO DA MÉDIA DAS IDADES
age_media = (age_sum) / 4
print(f'A média de idade desse grupo de pessoas é {age_media:.0f} anos.')

# QUANTAS PESSOAS SÃO MENORES DE 21 ANOS

# NOME DA MULHER MAIS VELHA
print(f'{name_oldest} é a mulher mais velha com {oldest_woman} anos.')