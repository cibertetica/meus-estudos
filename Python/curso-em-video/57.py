# exercício 57
# cadastro de gênero que não pára até que a pessoa digite a informação correta
gender = input(
'''
Informe seu gênero:
[M] Masculino
[F] Feminino
[O] Outro
'''
).strip().upper()[0]
while gender not in 'MFO':
    gender = input('Dados inválidos! Por favor digite apenas uma das opções a seguir.\n[M] Masculino\n[F] Feminino\n[O] Outro:\n').strip().upper()[0]
print('Cadastrado com sucesso!')
print(f'[{gender}]')