# exercício 97 
# linha separadora adaptada conforme o tamanho de uma mensagem

def message(text):
    size = len(text) + 4
    print('~'* size)
    print(f'  {text}')
    print('~'* size, '\n')

message('Martha')
message('Curso de Python')