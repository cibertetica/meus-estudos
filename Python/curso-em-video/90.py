# exercício 90 
# programa que lê nome e média de aluno e guarda as informações em um dicionário

student = {}

student['Nome'] = input('Nome: ').title()
student['Media'] = float(input('Média: '))
if student['Media'] >= 7:
    student['Status'] = 'Aprovado'
elif 5 <= student['Media'] <= 6:
    student['Status'] = 'Recuperação'
else:
    student['Status'] = 'Reprovado'

print('-' * 20)
for k, v in student.items():
    print(f'{k}: {v}')