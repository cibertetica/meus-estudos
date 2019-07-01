# exercício 10 incrementado
# coloquei a opção de informar a cotação do dólar no dia

real = float(input('Quanto dinheiro você tem? R$ '))
dolar = float(input('Informe a cotação do dolar hoje: U$$ '))
dolar = real / dolar 
print(f'R$ {real:.2f} vale US$ {dolar:.2f} hoje. ')