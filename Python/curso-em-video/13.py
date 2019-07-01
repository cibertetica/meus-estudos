# exercício 13
# reajuste / aumento de salário de 15%

salary = float(input('Informe seu salário atual: R$ '))
newsalary = salary + (salary * (15 /100))
print(f'Com o reajuste de 15%, seu salário sobe para R$ {newsalary:.2f}. ')