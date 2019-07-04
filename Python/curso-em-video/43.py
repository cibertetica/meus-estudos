# exercício 43 
# cálculo de IMC

weight = float(input('Insira seu peso: '))
height = float(input('Insira sua altura:  '))
bmi = weight / (height ** 2) # bmi - body mass index | imc em inglês
#bmi = weight / (pow(height, 2))
print(f'\nSeu IMC é {bmi:.1f}.\n')
if bmi < 18.5:
    print('Abaixo do peso.')
# forma não simplificada de fazer: 
#elif bmi >= 18.5 and bmi < 25:
#    print('Peso ideal.')
elif 18.5 <= bmi < 25:
    print('Peso ideal.')
# forma não simplificada de fazer:
#elif bmi >= 25 and bmi < 30:
#   print('Sobrepeso.)
elif 25 <= bmi < 30:
    print('Sobrepeso.')
# forma não simplficada de fazer:
#elif bmi >= 30 and bmi < 40:
#    print('Obesidade.')
elif 30 <= bmi < 40:
    print('Obesidade.')
else:
    print('Obesidade mórbida.')