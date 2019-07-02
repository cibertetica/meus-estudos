# exercício 22

# Um programa que lê o nome completo de uma pessoa e mostra o nome com todas as letras maiúsculas e minúsculas
# Quantas letras ao todo, sem contar os espaços
# Quantas letras tem o primeiro nome

name = input('Informe seu nome: ').strip()
print('Seu nome com letras maiúsculas\n' , name.upper())
print('Seu nome com letras minúsculas\n' , name.lower())
print('Seu nome com espaços tem' , len(name) , "letras.")
name = name.split() # converti a string numa espécie de lista com a função split para mostrar só a primeira palavra
print('Seu primeiro nome tem' , len(name[0]) , "letras.")
