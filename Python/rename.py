import os

def rename(path):
    c = 0
    for name in os.listdir(path):
        dst = str(c) + '.png'
        src = path + name
        dst = path + dst
        os.rename(src, dst)
        c += 1

directory = 'c:/Users/Martha/Downloads/images/'
rename(directory)