import os

def organize(path):
    try:
        os.rmdir(path)
    except OSError:
        print('Não foi possível apagar esse diretório.')
    else:
        print('Diretório apagado com sucesso.')

directory = 'C:/Users/Martha/Downloads/New'

organize(directory)