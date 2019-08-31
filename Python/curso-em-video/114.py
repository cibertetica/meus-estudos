# exercício 114
# programa para verificar se a internet está disponível no computador

import urllib.request
def internet(url):
    try:
        urllib.request.urlopen(f'http://{input(url)}/', timeout=10)
        return print('Site disponível!')
    except:
        return print('Site não disponível. Verifique sua internet. \nSe estiver tudo certo, tente mais tarde; o site pode estar com problemas.')

internet('Digite a url do site (sem https): ')