import config
import os

def rename(path, ext):
    for f in os.listdir(path):
        if ext == '.srt':
            new_f = f.replace('.srt', '.txt')
        if ext == '.txt':
            new_f = f.replace('.txt', '.srt')
        try:
            os.rename(path + f, path + new_f)
        except Exception as error:
            print(error)
        else:
            print('Renomeado com sucesso!')

while True:
    try:
        option = int(input('[1] Converter SRT para TXT\n[2] Converter TXT para SRT\n'))
    except:
        print('Opção inválida!')
    if option == 1 or option == 2:
        if option == 1:
            ext = '.srt'
        if option == 2:
            ext = '.txt'
        break
    print('Opção não disponível.')

rename(config.directory, ext)