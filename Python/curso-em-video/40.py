# exercício 40
# média de aluno

n1 = float(input('Informe a 1ª nota: '))
n2 = float(input('Informe a 2ª nota: '))
average =  (n1 + n2) / 2
print(f'Sua média é de {average:.1f}')

if average >= 7:
    print('Você foi APROVADO.')
elif average >= 5 and average < 7:
    print('Você está em EXAME.')
else:
    print('Você foi REPROVADO.')