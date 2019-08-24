# exercício 114
# programa para verificar se a internet está disponível no computador

import urllib.request 

def internet():
    try:
        status = urllib.request.urlopen('http://pudim.com.br', timeout=1)
    except Exception as error:
        print(error)
    else:
        print(status)

internet()