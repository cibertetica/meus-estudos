# exercício 36
# calcular se alguém tem condições de financiar uma casa
# levando em conta que a prestação deve ser menor do que 30% do salário da pessoa

home = float(input('Valor da casa a ser financiada: R$ '))
years = int(input('Em quantos anos será financiada: '))
salary = float(input('Salário a analisar: R$ '))
parcel = home / (years * 12) # um ano tem 12 meses, esse cálculo é para saber em quantos meses será financiada e depois quanto será a parcela mensal
print(f'Financiando uma residência de valor R$ {home:.2f} em {years} anos, a parcela mensal é de R$ {parcel:.2f}.\n')

minimo = salary * (30 / 100)
if parcel < minimo:
    print('Financiamento aprovado!')
else:
    print('Financiamento reprovado!')
