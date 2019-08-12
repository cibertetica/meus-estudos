# exercício 27 
# lê o nome completo de alguém e retorna seu primeiro e último nome

full_name = input('Informe seu nome completo: ').strip()
full_name = full_name.title() # incrementei um pouco capitalizando o nome para ficar mais profissional
name = full_name.split()
print('O seu primeiro nome é' , name[0])
print('O seu último sobrenome é', name[(len(name) - 1)])