# exercício 25
# verificar se existe o sobrenome "Silva" no nome de alguém

name = input('Qual é o seu nome completo? ').strip()
print('Tem Silva no seu nome? ')
print('SILVA' in name.upper()) # coloca tudo em letras maiúsculas para evitar possíveis erros caso a capitalização seja diferente