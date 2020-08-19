import os
import config
import shutil

def moving(path):
    for f in os.listdir(path):
        filetype = f[-3:]
        if filetype == 'mp4' or filetype == 'mkv' or filetype == 'avi':
            directory = 'video'
        elif filetype == 'mp3' or filetype == 'm4a':
            directory = 'music'
        elif filetype == 'jpg' or filetype == 'png':
            directory = 'images'
        else:
            directory = f'{filetype}'
    
        try:
            os.mkdir(path + directory)
        except Exception as error:
            print(error)
        else:
            print(f'Pasta {directory} criada com sucesso!')

        try:
            shutil.move(path + f, path + '/' + directory)
        except Exception as error:
            print(error)
        else:
            print(f'Arquivo {f}movido com sucesso!')

moving(config.directory)