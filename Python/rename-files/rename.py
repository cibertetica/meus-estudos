import os
import config

def rename(path):
    c = 0
    for name in os.listdir(path):
        dst = str(c) + '.png'
        src = path + name
        dst = path + dst
        os.rename(src, dst)
        c += 1

rename(config.directory)