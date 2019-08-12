# exercício 57 modificado
# cadastro de gênero que não pára até que a pessoa digite a informação correta

while True:
    gender = input('Informe seu gênero: [M -> Masculino | F -> Feminino | O -> Outro]\n').upper()[0]
    if gender in 'MFO':
        break
    print('Dados inválidos!')

print(f'Cadastrado com sucesso!\n{gender}')