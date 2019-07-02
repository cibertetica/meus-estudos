# exercício 29
# radar eletrônico de carros
# se o carro ultrapassa o limite, é multado

velocity = int(input('Velocidade do veículo: '))
if velocity > 80:
    print('Você está ultrapassando a velocidade permitida! O limite é 80 km/h.')
    print(f'Infelizmente será multado. O valor da sua multa é R$ {(velocity - 80) * 7:.2f}.') # 7 reais para cada kilômetro ultrapassado
else:
    print('Está na velocidade permitida. Boa viagem!')