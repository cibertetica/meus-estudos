# exercício 34
# reajuste de salário
# quem recebe até R$ 1250,00 terá 15% de aumento.
# quem recebe acima disso terá 10% de aumento.

salary = float(input('Informe seu salário atual: '))

if salary <= 1250.00:
    salary = salary + (salary * (15 / 100))
    print(f'Você terá 15% de aumento.\nSeu salário ficará R$ {salary:.2f}.')
else:
    salary = salary + (salary * (10 / 100))
    print(f'Você terá 10% de aumento.\nSeu salário ficará R$ {salary:.2f}.')