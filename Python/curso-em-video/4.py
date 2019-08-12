# exercício 4
# analisando uma variável

value = input('Digite algo qualquer: ')

print('O tipo primitivo desse valor é', type(value)) # tipo primitivo
print('Só tem espaços?', value.isspace())
print('É um número?', value.isnumeric()) # formada apenas por números
print('É alfabético?', value.isalpha()) # formada apenas por letras
print('É alfanumérico?', value.isalnum()) # composta de números E letras
print('Está em letras maiúsculas?', value.isupper())
print('Está em letras minúsculas?', value.islower())
print('Está capitalizada?', value.iscapitalize()) # formatada com palavras começando com maiúscula e continuando com minúscula
