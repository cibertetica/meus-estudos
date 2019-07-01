# exercício 15
# ler a quantidade de km percorridos por um carro alugado e por quantos dias ele foi alugado
# calcular o preço a pagar, sabendo que é cobrado R$ 60,00 por dia e R$ 0,15 por km rodado

km = float(input('Quantos kilômetros foram percorridos? '))
days = int(input('Por quantos dias o carro foi alugado? '))
price = (days * 60.00) + (km * 0.15)
print(f'Você vai pagar R$ {price:.2f} por esse carro. ')